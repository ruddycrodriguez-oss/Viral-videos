#!/usr/bin/env python3
"""Elige la mejor toma de cada frase por medidas objetivas (el asistente no puede escuchar).

Para cada `crudos/NN_tomaK.wav` mide: errores de transcripción (Whisper medium) contra la frase, «θ» y «s» con el reconocedor de fonemas,
mediana y rango de tono (pYIN) y palabras por minuto crudas. Criterio de orden: menos errores, luego menos «θ», luego tono más cercano al objetivo.
Uso: python elegir_tomas.py <etapa_a> <narracion.json> [--objetivo-hz 150]
Escribe <etapa_a>/seleccion.json y `tomas.json` (todas las medidas) y imprime la cadena para `ensamblar_muestra.py --toma`.
Se ejecuta en el entorno de medición (torch, transformers, librosa, faster-whisper, kokoro-onnx)."""
import argparse, json, os, sys
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
import voz, voz_calidad as vc

ap = argparse.ArgumentParser(); ap.add_argument("etapa_a"); ap.add_argument("narracion"); ap.add_argument("--objetivo-hz", type=float, default=150.0)
ap.add_argument("--frases", default="")
a = ap.parse_args()
narr = json.load(open(a.narracion, encoding="utf-8"))
texto = narr["narracion"] if "narracion" in narr else " ".join(e["texto"] for e in narr["escenas"])
frases = [x for t, x in voz._frases(texto) if t == "frase"]
info = json.load(open(os.path.join(a.etapa_a, "frases.json"), encoding="utf-8"))["tomas"]
filtro = {int(x) for x in a.frases.split(",")} if a.frases else None
res = []
for t in info:
    if filtro is not None and t["frase"] not in filtro: continue
    orig = frases[t["frase"]]
    ref = [vc._norm_palabra(w) for w in vc.palabras_habladas(orig, voz)]
    x16 = vc.cargar16(t["archivo"])
    hip_txt = vc._expandir_digitos(vc.transcribir(x16), voz)
    hip = [vc._norm_palabra(w) for w in hip_txt.split() if vc._norm_palabra(w)]
    w, err = vc.wer(ref, hip)
    rec = vc.fonemas_reconocidos(x16); tn = vc.tono(x16)
    voz_s = len(x16) / 16000
    m = {"frase": t["frase"], "toma": t["toma"], "errores": err, "palabras": len(ref), "transcripcion": hip_txt, "theta": rec.count("θ"),
         "s": rec.count("s"), "tono": tn, "wpm_crudo": round(len(ref) / voz_s * 60, 1), "duracion": round(voz_s, 2)}
    m["puntaje"] = round(err * 10 + m["theta"] * 10 + abs(tn["mediana_hz"] - a.objetivo_hz) / 40, 2)
    res.append(m)
    print(f"frase {m['frase']} toma {m['toma']}: errores {err}/{len(ref)} θ={m['theta']} tono {tn['mediana_hz']} Hz rango {tn['rango_st']} st | {hip_txt}", flush=True)
mejor = {}
for m in res:
    if m["frase"] not in mejor or m["puntaje"] < mejor[m["frase"]]["puntaje"]: mejor[m["frase"]] = m
sel = {str(k): v["toma"] for k, v in sorted(mejor.items())}
json.dump(res, open(os.path.join(a.etapa_a, "tomas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(sel, open(os.path.join(a.etapa_a, "seleccion.json"), "w"), indent=1)
print("SELECCION --toma", ",".join(str(v) for k, v in sorted(sel.items(), key=lambda kv: int(kv[0]))))
print("errores totales de la selección:", sum(v["errores"] for v in mejor.values()), "| θ:", sum(v["theta"] for v in mejor.values()))
