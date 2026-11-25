#!/usr/bin/env python3
"""Consistencia de timbre entre las frases de una muestra: similitud coseno de hablante (CAM++, el codificador de Ming) entre las tomas elegidas.

Una misma persona suele dar > 0,8; las tomas «diseñadas» por separado (cada frase con su semilla) dan ~0,4 a 0,6, es decir, suenan como voces distintas.
Uso (entorno v_ming): python consistencia.py <repo_ming> <campplus.onnx> <wav1> <wav2> ...   (solo medición)"""
import sys, os
import numpy as np, soundfile as sf, torch, torchaudio
repo, onnx, wavs = sys.argv[1], sys.argv[2], sys.argv[3:]
sys.path.insert(0, repo)
from spkemb_extractor import SpkembExtractor
ext = SpkembExtractor(onnx)
E = []
for w in wavs:
    x, sr = sf.read(w, dtype="float32"); x = x.mean(1) if x.ndim > 1 else x
    e = ext(torchaudio.functional.resample(torch.from_numpy(x).unsqueeze(0), sr, 16000))
    e = (e if torch.is_tensor(e) else torch.tensor(e)).reshape(-1).float(); E.append(e / e.norm())
S = (torch.stack(E) @ torch.stack(E).T).numpy(); m = ~np.eye(len(S), dtype=bool)
print("similitud de hablante:\n", np.round(S, 2)); print("media %.3f | mínima %.3f" % (S[m].mean(), S[m].min()))
