#!/usr/bin/env python3
"""Etapa A de la voz: genera cada FRASE por separado con un modelo abierto de «diseño de voz» (la voz se crea desde una descripción;
no se clona ninguna persona). Guarda `crudos/NN_tomaK.wav` (sin pausas ni procesado) y `frases.json`.

Uso: python generar_crudos.py <qwen|voxcpm> <narracion.json> <carpeta_salida> [--frases 0,1,2,3] [--tomas 2] [--estilo texto.txt]
Entornos: v_qwen (qwen-tts) o v_vox (voxcpm), ambos con PyTorch CPU. La etapa B (ensamblado, medición y procesado de audio) corre en otro entorno."""
import argparse, json, os, sys, time
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
import voz

ap = argparse.ArgumentParser()
ap.add_argument("modelo"); ap.add_argument("narracion"); ap.add_argument("salida")
ap.add_argument("--frases", default=""); ap.add_argument("--tomas", type=int, default=1); ap.add_argument("--estilo", default=""); ap.add_argument("--sin-seseo", action="store_true", help="no reescribir c/z como s")
ap.add_argument("--semilla0", type=int, default=0, help="desplaza las semillas (tomas nuevas)")
a = ap.parse_args()
os.makedirs(os.path.join(a.salida, "crudos"), exist_ok=True)

ESTILO_BASE = ("A male narrator in his mid-thirties speaking neutral Latin American Spanish. Deep, warm baritone voice with a low pitch, "
               "like the host of a funny science documentary: friendly smile in the voice, energetic, very clear and well articulated, "
               "lively and expressive intonation with wide pitch variation, confident and playful, enthusiastic but never shouting, natural conversational pace.")
estilo = open(a.estilo, encoding="utf-8").read().strip() if a.estilo else ESTILO_BASE
narr = json.load(open(a.narracion, encoding="utf-8"))
texto = narr["narracion"] if "narracion" in narr else " ".join(e["texto"] for e in narr["escenas"])
elementos = voz._frases(texto)
frases = [(i, voz._analizar(x), x) for i, (t, x) in enumerate(elementos) if t == "frase"]
quedan = [int(x) for x in a.frases.split(",")] if a.frases else list(range(len(frases)))

import torch
torch.set_num_threads(os.cpu_count() or 4)
if a.modelo == "qwen":
    from qwen_tts import Qwen3TTSModel
    modelo = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign", device_map="cpu", dtype=torch.float32)
    def sintetizar(t, extra=""):
        w, sr = modelo.generate_voice_design(text=t, instruct=(estilo + (" " + extra if extra else "")), language="Spanish")
        return np.asarray(w[0], dtype=np.float32), sr
elif a.modelo == "voxcpm":
    from voxcpm import VoxCPM
    modelo = VoxCPM.from_pretrained("openbmb/VoxCPM2", load_denoiser=False)
    desc = "(" + estilo + ")"
    def sintetizar(t, extra=""):
        w = modelo.generate(text=desc + t, cfg_value=2.0, inference_timesteps=10)
        return np.asarray(w, dtype=np.float32), modelo.tts_model.sample_rate
else:
    raise SystemExit("modelo desconocido")

info = []
for k in quedan:
    i, pal, orig = frases[k]
    t = voz._texto_voz(pal)
    if not a.sin_seseo: t = voz.texto_seseo(t)   # c/z -> s solo para la voz (los subtítulos no cambian)
    for toma in range(a.tomas):
        torch.manual_seed(1000 * k + toma + a.semilla0)
        t0 = time.time()
        audio, sr = sintetizar(t)
        ruta = os.path.join(a.salida, "crudos", f"{k:02d}_toma{toma}.wav")
        sf.write(ruta, audio, sr)
        info.append({"frase": k, "toma": toma, "texto": t, "archivo": ruta, "sr": sr, "duracion": round(len(audio) / sr, 2), "segundos_calculo": round(time.time() - t0, 1)})
        print(f"frase {k} toma {toma}: {len(audio)/sr:.1f} s de audio en {time.time()-t0:.0f} s de cálculo | {t[:50]}", flush=True)
json.dump({"modelo": a.modelo, "estilo": estilo, "tomas": info}, open(os.path.join(a.salida, "frases.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
