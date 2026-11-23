#!/usr/bin/env python3
"""Etapa A de la voz con Ming-3.0-tts-0.5B (MIT): genera cada FRASE por separado y guarda `crudos/NN_tomaK.wav` (sin pausas ni procesado)
y `frases.json`, con los mismos argumentos y el mismo formato que `generar_crudos.py` (Qwen3-TTS-VoiceDesign y VoxCPM2).

La voz NO se clona: Ming recibe una descripción de estilo en texto (tarea FREEFORM: «describe la voz y la entrega con una instrucción en
lenguaje natural», sin audio de referencia, `use_zero_spk_emb=True`) y diseña la voz. Con `--tarea voice_design` usa la tarea VOICE_DESIGN
(la descripción va como `controls={"style": ...}`; los ejemplos oficiales están en chino).

Uso: python generar_crudos_ming.py <narracion.json> <carpeta_salida> [--frases 0,1,2,3] [--tomas 2] [--estilo texto.txt]
         [--tarea freeform|voice_design] [--ancla <toma.wav> [--ancla-texto "texto de esa toma"]]
         [--repo <carpeta del clon>] [--pesos <carpeta o id de HF>]
--ancla (opcional, apagada por defecto): sin ella cada frase diseña su voz desde cero y el timbre cambia de una toma a otra. Con ella, la tarea
FREEFORM sigue la voz de una toma ya generada por el propio modelo (audio sintético, nunca de una persona real) y mantiene la instrucción de
estilo. El texto de la toma se toma de `frases.json` junto a su carpeta `crudos/`, o de --ancla-texto.
Requisitos (no están en el repositorio): clon de https://github.com/inclusionAI/Ming-3.0-tts (variable MING_REPO o --repo),
pesos `inclusionAI/Ming-3.0-tts-0.5B` (MING_PESOS o --pesos; si no, se descargan de Hugging Face), y un entorno con
torch==2.6.0 y torchaudio==2.6.0 (CPU) más `pip install -r requirements.txt` del clon (transformers 4.46.3, diffusers 0.33.0, etc.).
Se ejecuta con `python -I` (modo aislado), por eso el clon se añade a sys.path aquí.
La etapa B (ensamblado, medición y procesado de audio) corre en otro entorno."""
import argparse, json, os, sys, time
os.environ.setdefault("TQDM_DISABLE", "1")  # sin barras de progreso (una por cada paso de decodificación)
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
import voz

ap = argparse.ArgumentParser()
ap.add_argument("narracion"); ap.add_argument("salida")
ap.add_argument("--frases", default=""); ap.add_argument("--tomas", type=int, default=1); ap.add_argument("--estilo", default="")
ap.add_argument("--tarea", default="freeform", choices=["freeform", "voice_design"])
ap.add_argument("--ancla", default=""); ap.add_argument("--ancla-texto", default="")
ap.add_argument("--repo", default=os.environ.get("MING_REPO", ""))
ap.add_argument("--pesos", default=os.environ.get("MING_PESOS", "inclusionAI/Ming-3.0-tts-0.5B"))
a = ap.parse_args()
if not a.repo or not os.path.isfile(os.path.join(a.repo, "ming_tts.py")):
    raise SystemExit("Falta el clon de https://github.com/inclusionAI/Ming-3.0-tts: pasa --repo <carpeta> o define MING_REPO")
os.makedirs(os.path.join(a.salida, "crudos"), exist_ok=True)

ancla_texto = a.ancla_texto
if a.ancla and not ancla_texto:
    fj = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(a.ancla))), "frases.json")
    for x in (json.load(open(fj, encoding="utf-8"))["tomas"] if os.path.isfile(fj) else []):
        if os.path.basename(x["archivo"]) == os.path.basename(a.ancla): ancla_texto = x["texto"]
    if not ancla_texto: raise SystemExit("No encuentro el texto de la toma ancla: pasa --ancla-texto")

ESTILO_BASE = ("A male narrator in his mid-thirties speaking neutral Latin American Spanish with seseo (the letters c and z are pronounced as s). "
               "Deep to medium-low baritone voice, not high-pitched; warm, energetic and very clear, like the host of a funny science documentary: "
               "friendly smile in the voice, lively and expressive intonation with wide pitch variation, confident, playful, "
               "enthusiastic but never shouting, natural conversational pace.")
estilo = open(a.estilo, encoding="utf-8").read().strip() if a.estilo else ESTILO_BASE
narr = json.load(open(a.narracion, encoding="utf-8"))
texto = narr["narracion"] if "narracion" in narr else " ".join(e["texto"] for e in narr["escenas"])
elementos = voz._frases(texto)
frases = [(i, voz._analizar(x), x) for i, (t, x) in enumerate(elementos) if t == "frase"]
quedan = [int(x) for x in a.frases.split(",")] if a.frases else list(range(len(frases)))

sys.path.insert(0, a.repo)
import torch
torch.set_num_threads(os.cpu_count() or 4)
from loguru import logger
logger.remove(); logger.add(sys.stderr, level="WARNING")  # el modelo imprime el prompt completo en INFO
from ming_tts import MingTTS

t0 = time.time()
modelo = MingTTS(a.pesos, device="cpu", text_normalization=False)  # sin pynini: los números ya vienen escritos con letras (voz._texto_voz)
# El código del proyecto carga en bfloat16 y asume torch.autocast de CUDA; en CPU eso falla («mat1 and mat2 must have the same dtype»),
# así que se pasa todo a float32 (es el modo que se probó: ver frases.json).
modelo.model.to(torch.float32)
@torch.inference_mode()
def _codificar_prompt_fp32(onda):  # igual que BailingMM.encode_prompt_latent, pero sin forzar bfloat16 (solo se usa con --ancla)
    onda = onda.to(dtype=torch.float32)
    lat, _ = modelo.model.audio.encode_latent(onda, torch.tensor([onda.size(1)], dtype=torch.long))
    return lat
modelo.model.encode_prompt_latent = _codificar_prompt_fp32
print(f"modelo cargado en {time.time()-t0:.0f} s (CPU, float32, {modelo.sample_rate} Hz)", flush=True)

def sintetizar(t):
    if a.tarea == "freeform" and a.ancla:
        w = modelo.synthesize(task="FREEFORM", text=t, language_id="es", instruction=estilo,
                              prompt_wav_path=os.path.abspath(a.ancla), prompt_text=ancla_texto, use_spk_emb=True)
    elif a.tarea == "freeform":
        w = modelo.synthesize(task="FREEFORM", text=t, language_id="es", instruction=estilo, use_zero_spk_emb=True)
    else:
        w = modelo.synthesize(task="VOICE_DESIGN", text=t, language_id="es", controls={"style": estilo}, use_zero_spk_emb=True)
    return w.float().cpu().numpy().reshape(-1).astype(np.float32), modelo.sample_rate

info = []
for k in quedan:
    i, pal, orig = frases[k]
    t = voz.texto_seseo(voz._texto_voz(pal))
    for toma in range(a.tomas):
        torch.manual_seed(1000 * k + toma)
        t0 = time.time()
        audio, sr = sintetizar(t)
        ruta = os.path.join(a.salida, "crudos", f"{k:02d}_toma{toma}.wav")
        sf.write(ruta, audio, sr)
        info.append({"frase": k, "toma": toma, "texto": t, "archivo": ruta, "sr": sr, "duracion": round(len(audio) / sr, 2), "segundos_calculo": round(time.time() - t0, 1)})
        print(f"frase {k} toma {toma}: {len(audio)/sr:.1f} s de audio en {time.time()-t0:.0f} s de cálculo | {t[:50]}", flush=True)
json.dump({"modelo": "ming-3.0-tts-0.5b:" + a.tarea + (":ancla" if a.ancla else ""), "estilo": estilo, "tomas": info}, open(os.path.join(a.salida, "frases.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
