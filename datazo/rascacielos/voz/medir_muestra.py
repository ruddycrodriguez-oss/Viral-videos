#!/usr/bin/env python3
"""Mide una muestra ya ensamblada (sin volver a generar ni alinear). Uso: python medir_muestra.py <carpeta_muestra> <etiqueta> [frases=4]"""
import json, os, sys
import soundfile as sf
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(AQUI, "..", ".."))
import voz, voz_calidad as vc
carpeta, etiqueta = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 4
guion = json.load(open(os.path.join(AQUI, "..", "guion_rascacielos.json"), encoding="utf-8"))
elementos = voz._frases(" ".join(e["texto"] for e in guion["escenas"]))
texto = " ".join(x for t, x in elementos[:n] if t == "frase")
tl = json.load(open(os.path.join(carpeta, "timeline.json"), encoding="utf-8"))
final = os.path.join(carpeta, f"muestra_{etiqueta}.wav")
med = vc.medir(final, texto, voz, tl)
med["ajustes"] = tl["ajustes"]; med["duracion_s"] = round(sf.info(final).duration, 2)
json.dump(med, open(os.path.join(carpeta, f"medidas_{etiqueta}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
r = med["ritmo"]; t = med["tono"]
print(f"[{etiqueta}] {med['duracion_s']} s | WER {med['wer']} ({med['errores_palabras']}/{med['palabras']}) | ritmo {r['wpm_habla']} wpm (con pausas {r['wpm_con_pausas']}) | "
      f"θ={med['theta_reconocidos']} s={med['s_reconocidas']}/{med['s_esperadas']} (c/z: {med['letras_c_o_z']}) | tono {t['rango_st']} st (2-98%: {t.get('rango_2_98_st')}) desv {t['desv_st']} mediana {t['mediana_hz']} Hz")
print("transcripción:", med["transcripcion"]); print("fonemas reconocidos:", med["fonemas_reconocidos"]); print("fonemas esperados  :", med["fonemas_esperados"])
