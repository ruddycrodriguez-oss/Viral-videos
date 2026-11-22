#!/usr/bin/env python3
"""Genera la narración con voz de IA y la alinea palabra por palabra.

Uso: python3 generar_voz.py <guion.json> <voz> <carpeta_salida>
  voz = kokoro:ef_dora | kokoro:em_alex | kokoro:em_santa | chatterbox
Salida: voz.wav (con silencios), timeline.json (palabras, eventos y duración).
Modelos: Kokoro-82M (Apache-2.0) y Chatterbox multilingüe (MIT). Alineación: faster-whisper (MIT).
La carpeta de modelos se toma de la variable MODELOS (por defecto, ./modelos).
"""
import difflib, json, os, re, subprocess, sys, unicodedata
import numpy as np, soundfile as sf

guion, voz, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
MOD = os.environ.get("MODELOS", "modelos")
SR = 24000
data = json.load(open(guion, encoding="utf-8"))
narr = data["narracion"]

# --- 1) frases y marcas ------------------------------------------------------------------
frases = []
for linea in narr.split("\n"):
    for fr in re.split(r"(?<=[.?!])\s+(?=[¿¡A-ZÁÉÍÓÚ{*])", linea.strip()):
        if fr.strip():
            frases.append(fr.strip())

def analizar(fr):
    """Devuelve el texto limpio y la lista de palabras con sus marcas de evento y de término técnico."""
    palabras, pend, termino = [], [], False
    for tok in re.findall(r"\{[a-z0-9_]+\}|\S+", fr):
        m = re.fullmatch(r"\{([a-z0-9_]+)\}", tok)
        if m:
            pend.append(m.group(1)); continue
        # una marca puede ir pegada a la palabra: {ev}palabra
        pegadas = re.findall(r"\{([a-z0-9_]+)\}", tok)
        tok = re.sub(r"\{[a-z0-9_]+\}", "", tok); pend += pegadas
        es_term = tok.startswith("*") or termino
        if tok.startswith("*") and not tok.rstrip(".,;:?!").endswith("*"): termino = True
        if tok.rstrip(".,;:?!").endswith("*"): termino = False
        limpio = tok.replace("*", "")
        palabras.append({"w": limpio, "eventos": pend, "termino": es_term}); pend = []
    return palabras

def texto(pal): return " ".join(p["w"] for p in pal)

# --- 2) voz ------------------------------------------------------------------------------
def sintetizar_kokoro(nombre):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(MOD, "kokoro-v1.0.onnx"), os.path.join(MOD, "voices-v1.0.bin"))
    def f(t):
        a, sr = k.create(t, voice=nombre, speed=1.04, lang="es-419")
        return a.astype(np.float32), sr
    return f

def sintetizar_chatterbox():
    import torch
    from chatterbox.mtl_tts import ChatterboxMultilingualTTS
    m = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
    def f(t):
        w = m.generate(t, language_id="es")
        return w.squeeze().cpu().numpy().astype(np.float32), m.sr
    return f

if voz.startswith("kokoro:"): tts = sintetizar_kokoro(voz.split(":")[1])
elif voz == "chatterbox": tts = sintetizar_chatterbox()
else: raise SystemExit("voz desconocida")

def remuestrear(a, sr, sr2):
    if sr == sr2: return a
    n = int(len(a) * sr2 / sr); return np.interp(np.linspace(0, len(a) - 1, n), np.arange(len(a)), a).astype(np.float32)

audio = [np.zeros(int(0.35 * SR), np.float32)]
tramos = []   # (inicio_s, fin_s, palabras)
cursor = 0.35
for i, fr in enumerate(frases):
    pal = analizar(fr)
    a, sr = tts(texto(pal))
    a = remuestrear(a, sr, SR)
    # recorta silencio sobrante en los extremos
    nz = np.where(np.abs(a) > 0.01)[0]
    if len(nz): a = a[max(0, nz[0] - int(0.03 * SR)): nz[-1] + int(0.08 * SR)]
    tramos.append((cursor, cursor + len(a) / SR, pal))
    audio.append(a); cursor += len(a) / SR
    pausa = 0.42 if fr.rstrip().endswith("?") else 0.28
    audio.append(np.zeros(int(pausa * SR), np.float32)); cursor += pausa
audio.append(np.zeros(int(0.5 * SR), np.float32)); cursor += 0.5
x = np.concatenate(audio)
sf.write(os.path.join(out, "voz_cruda.wav"), x, SR)

# --- 3) alineación palabra por palabra (faster-whisper, solo para medir tiempos) ----------
def norm(s):
    s = unicodedata.normalize("NFD", s.lower()); s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9ñ]", "", s)
from faster_whisper import WhisperModel
wm = WhisperModel(os.environ.get("WHISPER", "small"), device="cpu", compute_type="int8")
palabras_tl, eventos = [], {}
for (t0, t1, pal) in tramos:
    seg = x[int(t0 * SR): int(t1 * SR)]
    tmp = os.path.join(out, "_seg.wav"); sf.write(tmp, seg, SR)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-ar", "16000", "-ac", "1", os.path.join(out, "_seg16.wav")], check=True)
    a16, _ = sf.read(os.path.join(out, "_seg16.wav"), dtype="float32")
    segs, _ = wm.transcribe(a16, language="es", word_timestamps=True, vad_filter=False)
    ws = [w for s in segs for w in s.words]
    ref = [norm(p["w"]) for p in pal]; hyp = [norm(w.word) for w in ws]
    sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
    tiempo = [None] * len(pal)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): tiempo[i1 + k] = (ws[j1 + k].start, ws[j1 + k].end)
    # interpolar lo que no coincidió, entre vecinos conocidos (o los bordes de la frase)
    dur = t1 - t0
    idx = [i for i, v in enumerate(tiempo) if v]
    if not idx:                                   # sin coincidencias: reparto proporcional a las letras
        L = np.array([max(1, len(p["w"])) for p in pal], float); c = np.concatenate([[0], np.cumsum(L)]) / L.sum() * dur
        tiempo = [(c[i], c[i + 1]) for i in range(len(pal))]
    else:
        for i in range(len(pal)):
            if tiempo[i]: continue
            a = max([j for j in idx if j < i], default=None); b = min([j for j in idx if j > i], default=None)
            ta = tiempo[a][1] if a is not None else 0.0; tb = tiempo[b][0] if b is not None else dur
            na = (a + 1) if a is not None else 0; nb = b if b is not None else len(pal)
            n = max(1, nb - na); k = i - na
            tiempo[i] = (ta + (tb - ta) * k / n, ta + (tb - ta) * (k + 0.9) / n)
    for p, (s0, s1) in zip(pal, tiempo):
        ini, fin = t0 + s0, t0 + min(s1, dur)
        palabras_tl.append({"w": re.sub(r"[¿¡.,;:?!…]", "", p["w"]), "ini": round(ini, 3), "fin": round(max(fin, ini + 0.12), 3), "termino": p["termino"]})
        for ev in p["eventos"]: eventos[ev] = round(ini, 3)
# la palabra mostrada dura hasta la siguiente (los huecos pequeños se cubren en la escena)
dur_total = round(cursor + 0.2, 2)
json.dump({"duracion": dur_total, "eventos": eventos, "palabras": palabras_tl, "voz": voz}, open(os.path.join(out, "timeline.json"), "w"), ensure_ascii=False, indent=1)
for f in ("_seg.wav", "_seg16.wav"):
    try: os.remove(os.path.join(out, f))
    except OSError: pass
print("duración", dur_total, "s;", len(palabras_tl), "palabras;", len(eventos), "eventos")
