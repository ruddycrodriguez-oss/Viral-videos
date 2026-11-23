#!/usr/bin/env python3
"""Etapa B de la voz: toma los audios crudos de un modelo (etapa A), ajusta el ritmo, une las frases con pausas (0,4 s por oración,
0,3 s por coma), mejora el audio (ruido, ecualización, compresión, -14 LUFS), mide y guarda la muestra.

Uso: python ensamblar_muestra.py <carpeta_etapa_A> <etiqueta> <salida> [--frases 4] [--toma 0] [--wpm 167]
Entorno: el de las mediciones (torch + transformers + librosa + faster-whisper + kokoro-onnx)."""
import argparse, json, os, sys
import numpy as np, soundfile as sf
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", ".."))
import voz, voz_calidad as vc

ap = argparse.ArgumentParser()
ap.add_argument("etapa_a"); ap.add_argument("etiqueta"); ap.add_argument("salida")
ap.add_argument("--frases", type=int, default=4); ap.add_argument("--toma", default="0"); ap.add_argument("--wpm", type=float, default=167)
a = ap.parse_args()
os.makedirs(a.salida, exist_ok=True)
guion = json.load(open(os.path.join(AQUI, "..", "guion_rascacielos.json"), encoding="utf-8"))
texto_total = " ".join(e["texto"] for e in guion["escenas"])
elementos = voz._frases(texto_total)
n = a.frases
texto = " ".join(x for t, x in elementos[:n] if t == "frase")          # las primeras n oraciones del guion
info = json.load(open(os.path.join(a.etapa_a, "frases.json"), encoding="utf-8"))
tomas = {}
for t in info["tomas"]: tomas.setdefault(t["frase"], {})[t["toma"]] = t["archivo"]
crudos = {}
for k in range(n):
    toma = int(a.toma.split(",")[k]) if "," in a.toma else int(a.toma)
    audio, sr = sf.read(tomas[k][toma], dtype="float32")
    crudos[k] = (audio, sr)
tl = voz.narrar(texto, a.salida, ajustes={"wpm": a.wpm, "etiqueta_voz": a.etiqueta, "inicio": 0.15, "final": 0.30}, crudos=crudos)
cruda = os.path.join(a.salida, "voz_cruda.wav"); final = os.path.join(a.salida, f"muestra_{a.etiqueta}.wav")
lou = vc.mejorar_audio(cruda, final)
med = vc.medir(final, texto, voz, tl)
med["loudness"] = lou; med["ajustes"] = tl["ajustes"]; med["duracion_s"] = round(sf.info(final).duration, 2)
json.dump(med, open(os.path.join(a.salida, f"medidas_{a.etiqueta}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
r = med["ritmo"]; t = med["tono"]
print(f"[{a.etiqueta}] {med['duracion_s']} s | LUFS {lou['lufs']} pico {lou['pico_dbfs']} | WER {med['wer']} ({med['errores_palabras']}/{med['palabras']}) | "
      f"ritmo {r['wpm_habla']} wpm (con pausas {r['wpm_con_pausas']}) | θ={med['theta_reconocidos']} s={med['s_reconocidas']}/{med['s_esperadas']} (c/z: {med['letras_c_o_z']}) | "
      f"tono {t['rango_st']} st (2-98%: {t.get('rango_2_98_st')}) desv {t['desv_st']} mediana {t['mediana_hz']} Hz")
print("transcripción:", med["transcripcion"])
