"""Calidad de la voz de Datazo: cadena de mejora de audio y mediciones objetivas (el asistente no puede escuchar, así que mide).

Mejora (ffmpeg): filtro de graves, reducción de ruido, ecualización cálida y con presencia, de-esser suave, compresión, limitador y
normalización en dos pasadas a -14 LUFS (pico real máximo -1 dBTP).

Mediciones sobre una voz ya ensamblada:
  * transcripción con Whisper y tasa de errores de palabras (WER) contra el guion (los números se comparan hablados);
  * palabras por minuto (cuenta de la muestra elegida: frase recortada sin pausas largas) y también con todas las pausas;
  * reconocimiento de fonemas (wav2vec2 espeak) para comprobar que la c (ante e, i) y la z suenan como «s» y no como «θ»;
  * rango de tono (F0 con pYIN): percentiles 5 a 95 en semitonos, y desviación típica.
Se ejecuta en un entorno con torch, transformers, librosa, faster-whisper y kokoro-onnx (solo por su fonetizador espeak)."""
import json, os, re, subprocess, unicodedata
import numpy as np

LUFS_OBJETIVO = -14.0
CADENA = ("highpass=f=75,afftdn=nr=9:nf=-45:tn=1,"
          "equalizer=f=130:t=q:w=0.9:g=1.6,equalizer=f=320:t=q:w=1.0:g=-1.5,equalizer=f=3200:t=q:w=1.0:g=2.2,"
          "deesser=i=0.35:m=0.5:f=0.5,"
          "acompressor=threshold=-21dB:ratio=3:attack=8:release=150:makeup=3,alimiter=limit=0.89:level=disabled")


def mejorar_audio(entrada, salida, lufs=LUFS_OBJETIVO):
    """Aplica la cadena y normaliza en dos pasadas. Devuelve las mediciones de loudnorm de la pasada final."""
    base = ["ffmpeg", "-hide_banner", "-nostats", "-y", "-i", entrada, "-af"]
    p1 = subprocess.run(base + [f"{CADENA},loudnorm=I={lufs}:TP=-1.0:LRA=9:print_format=json", "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", p1.stderr, re.S)
    d = json.loads(m.group(0))
    filtro = (f"{CADENA},loudnorm=I={lufs}:TP=-1.0:LRA=9:measured_I={d['input_i']}:measured_TP={d['input_tp']}:"
              f"measured_LRA={d['input_lra']}:measured_thresh={d['input_thresh']}:offset={d['target_offset']}:linear=true")
    subprocess.run(base + [filtro, "-ar", "48000", "-c:a", "pcm_s16le", salida], capture_output=True, check=True)
    p3 = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", salida, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True)
    i_ = re.findall(r"I:\s+(-?[\d.]+) LUFS", p3.stderr); pk = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", p3.stderr)
    return {"lufs": float(i_[-1]) if i_ else None, "pico_dbfs": float(pk[-1]) if pk else None}


def _norm_palabra(s):
    s = unicodedata.normalize("NFD", s.lower()); s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9ñ]", "", s)


def palabras_habladas(texto, voz_mod):
    """Texto del guion -> lista de palabras tal y como se dicen (números en palabras), sin signos ni marcas."""
    out = []
    for fr in [x for t, x in voz_mod._frases(texto) if t == "frase"]:
        for p in voz_mod._analizar(fr): out += p["hab"]
    return out


def wer(ref, hip):
    d = np.zeros((len(ref) + 1, len(hip) + 1), int)
    d[:, 0] = np.arange(len(ref) + 1); d[0, :] = np.arange(len(hip) + 1)
    for i in range(1, len(ref) + 1):
        for j in range(1, len(hip) + 1):
            d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + (ref[i - 1] != hip[j - 1]))
    return d[-1, -1] / max(1, len(ref)), int(d[-1, -1])


def cargar16(ruta):
    import soundfile as sf
    tmp = ruta + ".16k.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", ruta, "-ar", "16000", "-ac", "1", tmp], check=True)
    x, _ = sf.read(tmp, dtype="float32"); os.remove(tmp)
    return x


_wm = {}
def transcribir(x16, modelo="medium"):
    from faster_whisper import WhisperModel
    if modelo not in _wm: _wm[modelo] = WhisperModel(modelo, device="cpu", compute_type="int8")
    segs, _ = _wm[modelo].transcribe(x16, language="es", vad_filter=False)
    return " ".join(s.text.strip() for s in segs)


def _expandir_digitos(texto, voz_mod):
    return re.sub(r"\d{1,3}(?:\.\d{3})*|\d+", lambda m: voz_mod.num2es(int(m.group(0).replace(".", ""))), texto)


_fon = {}
def fonemas_reconocidos(x16):
    import torch
    from transformers import AutoProcessor, AutoModelForCTC
    nombre = "facebook/wav2vec2-lv-60-espeak-cv-ft"
    import espeakng_loader   # el tokenizador de fonemas necesita la biblioteca espeak-ng (la trae este paquete)
    os.environ.setdefault("PHONEMIZER_ESPEAK_LIBRARY", espeakng_loader.get_library_path())
    os.environ.setdefault("ESPEAK_DATA_PATH", espeakng_loader.get_data_path())
    if "m" not in _fon:
        _fon["p"] = AutoProcessor.from_pretrained(nombre); _fon["m"] = AutoModelForCTC.from_pretrained(nombre).eval()
    with torch.no_grad():
        ent = _fon["p"](x16, sampling_rate=16000, return_tensors="pt")
        ids = _fon["m"](ent.input_values).logits.argmax(-1)
    return _fon["p"].batch_decode(ids)[0]


def fonemas_esperados(texto, voz_mod):
    from kokoro_onnx.tokenizer import Tokenizer
    t = Tokenizer()
    frases = [x for tp, x in voz_mod._frases(texto) if tp == "frase"]
    return " ".join(t.phonemize(voz_mod._texto_voz(voz_mod._analizar(f)), "es-419") for f in frases)


def tono(x16, sr=16000):
    import librosa
    f0, voz, _ = librosa.pyin(x16, fmin=65, fmax=350, sr=sr, frame_length=1024, hop_length=160)
    v = f0[~np.isnan(f0)]
    if len(v) < 20: return {"rango_st": 0.0, "desv_st": 0.0, "mediana_hz": 0.0, "voz_pct": 0.0}
    st = 12 * np.log2(v / np.median(v))
    return {"rango_st": round(float(np.percentile(st, 95) - np.percentile(st, 5)), 1), "rango_2_98_st": round(float(np.percentile(st, 98) - np.percentile(st, 2)), 1),
            "desv_st": round(float(np.std(st)), 2), "mediana_hz": round(float(np.median(v)), 1), "voz_pct": round(100 * len(v) / len(f0), 1)}


def ritmo(timeline, n_palabras):
    """Palabras por minuto con el timeline ensamblado: (a) sin pausas (suma de lo que dura cada palabra y los huecos < 0,25 s), (b) con todo."""
    P = timeline["palabras"]
    habla = 0.0
    for i, p in enumerate(P):
        habla += p["fin"] - p["ini"]
        if i + 1 < len(P) and 0 < P[i + 1]["ini"] - p["fin"] < 0.25: habla += P[i + 1]["ini"] - p["fin"]
    total = P[-1]["fin"] - P[0]["ini"]
    return {"wpm_habla": round(n_palabras / habla * 60, 1), "wpm_con_pausas": round(n_palabras / total * 60, 1), "segundos_totales": round(total, 1)}


def medir(wav, texto, voz_mod, timeline=None, whisper="medium"):
    """Mediciones objetivas de un audio ya procesado. `texto` = guion con marcas."""
    x16 = cargar16(wav)
    ref = [_norm_palabra(w) for w in palabras_habladas(texto, voz_mod)]
    hip_txt = _expandir_digitos(transcribir(x16, whisper), voz_mod)
    hip = [_norm_palabra(w) for w in hip_txt.split() if _norm_palabra(w)]
    w, n_err = wer(ref, hip)
    rec = fonemas_reconocidos(x16); esp = fonemas_esperados(texto, voz_mod)
    cz = len(re.findall(r"c(?=[eiéí])|z", " ".join(palabras_habladas(texto, voz_mod)).lower()))
    r = {"transcripcion": hip_txt, "wer": round(w, 3), "errores_palabras": n_err, "palabras": len(ref),
         "fonemas_reconocidos": rec, "fonemas_esperados": esp,
         "theta_reconocidos": rec.count("θ"), "s_reconocidas": rec.count("s"), "s_esperadas": esp.count("s"), "letras_c_o_z": cz,
         "tono": tono(x16)}
    if timeline: r["ritmo"] = ritmo(timeline, len(ref))
    return r
