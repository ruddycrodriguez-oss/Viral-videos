#!/usr/bin/env python3
"""Voz de IA para cualquier guion de Datazo (formatos A, B y C).
Uso: MODELOS=<carpeta> python3 narrar.py <narracion.json> <carpeta_salida> [terminos,clave]
El JSON lleva {"narracion": "..."} con las marcas descritas en voz.py. Genera voz.wav, timeline.json y verificacion_voz.json."""
import json, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import voz

narracion, salida = sys.argv[1], sys.argv[2]
voz.TERMINOS = sys.argv[3].split(",") if len(sys.argv) > 3 else []
tl = voz.narrar(json.load(open(narracion, encoding="utf-8"))["narracion"], salida, os.environ.get("MODELOS", "modelos"))
shutil.copyfile(os.path.join(salida, "voz_cruda.wav"), os.path.join(salida, "voz.wav"))
