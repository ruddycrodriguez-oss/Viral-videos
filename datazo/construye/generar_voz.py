#!/usr/bin/env python3
"""Voz del formato C. Uso: MODELOS=<carpeta> python3 generar_voz.py <guion.json> <carpeta_salida> [terminos,clave]
Atajo de datazo/narrar.py con los términos clave del Canal de Panamá por defecto."""
import os, subprocess, sys
aqui = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
if len(args) < 3: args.append("Panamá,Canal,Chagres,Culebra,Gatún,esclusa,compuertas,veintiséis,Datazo,gravedad")
sys.exit(subprocess.call([sys.executable, os.path.join(aqui, "..", "narrar.py")] + args))
