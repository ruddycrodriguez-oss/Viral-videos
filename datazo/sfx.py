#!/usr/bin/env python3
"""Efectos de sonido de Datazo, sintetizados por código (numpy + scipy). Son obra propia: no usan muestras ni bibliotecas de terceros, así que
no hay licencia que atribuir ni que renovar (regla «Efectos de sonido» de CLAUDE.md).

Uso:  import sfx;  y = sfx.efecto("impacto", seed=3)            # array float32 mono a SR = 48000
      mezcla = sfx.mezclar([(1.25, "impacto", 0.9), (3.0, "crujido", 0.6)], duracion=10.0)
      python3 sfx.py <carpeta>  -> escribe cada efecto como WAV de muestra y muestra sus picos."""
import os, sys
import numpy as np
from scipy import signal

SR = 48000


def _rng(seed): return np.random.default_rng(seed)
def _t(d): return np.arange(int(d * SR)) / SR
def _env(n, ataque=0.005, caida=0.2, curva=3.0):
    t = np.arange(n) / SR
    a = np.clip(t / max(ataque, 1e-4), 0, 1)
    return a * np.exp(-curva * t / max(caida, 1e-3))
def _filtro(x, tipo, f, orden=4):
    f = np.clip(np.atleast_1d(np.asarray(f, dtype=float)) / (SR / 2), 1e-4, 0.999)
    sos = signal.butter(orden, float(f[0]) if tipo in ("lowpass", "highpass") else list(f), btype=tipo, output="sos")
    return signal.sosfilt(sos, x)
def _norm(x, pico=0.9):
    m = np.max(np.abs(x)) or 1.0
    return (x / m * pico).astype(np.float32)


def whoosh(d=0.6, f0=300, f1=3500, seed=0):
    """Barrido de ruido filtrado (corte de cámara, paneo rápido)."""
    r = _rng(seed); n = int(d * SR); x = r.standard_normal(n)
    out = np.zeros(n); pasos = 24; seg = n // pasos
    for i in range(pasos):
        f = f0 * (f1 / f0) ** (i / (pasos - 1)); a, b = i * seg, (i + 1) * seg if i < pasos - 1 else n
        out[a:b] = _filtro(x, "bandpass", [f * 0.7, min(f * 1.4, 20000)], 2)[a:b]
    t = np.arange(n) / n
    return _norm(out * np.sin(np.pi * t) ** 1.5)


def impacto(d=1.1, seed=0):
    """Golpe grave con cola (algo pesado cae o choca)."""
    r = _rng(seed); n = int(d * SR); t = _t(d)
    f = 38 + 120 * np.exp(-t * 14); tono = np.sin(2 * np.pi * np.cumsum(f) / SR) * _env(n, 0.002, 0.45, 4)
    ruido = _filtro(r.standard_normal(n), "lowpass", 1800) * _env(n, 0.001, 0.12, 5)
    return _norm(tono * 0.9 + ruido * 0.55)


def grieta(d=0.9, seed=0):
    """Chasquidos secos encadenados (se parte el suelo o una pared)."""
    r = _rng(seed); n = int(d * SR); y = np.zeros(n)
    for k in range(7):
        i = int(r.uniform(0, 0.55) * SR) + k * 400; ln = int(r.uniform(0.03, 0.12) * SR)
        if i + ln >= n: continue
        c = _filtro(r.standard_normal(ln), "highpass", 1500) * np.exp(-np.arange(ln) / SR * r.uniform(40, 90))
        y[i:i + ln] += c * r.uniform(0.4, 1.0)
    y += _filtro(r.standard_normal(n), "lowpass", 160) * _env(n, 0.01, 0.35, 4) * 0.5
    return _norm(y)


def crujido(d=1.4, seed=0):
    """Madera o ladrillo que cruje bajo carga: pulsos irregulares con resonancia."""
    r = _rng(seed); n = int(d * SR); pulsos = np.zeros(n)
    t = 0.0
    while t < d - 0.05:
        i = int(t * SR); ln = int(r.uniform(0.01, 0.05) * SR)
        pulsos[i:i + ln] += r.standard_normal(min(ln, n - i)) * np.exp(-np.arange(min(ln, n - i)) / SR * 120) * r.uniform(0.3, 1)
        t += r.uniform(0.02, 0.14)
    y = _filtro(pulsos, "bandpass", [350, 2600], 2)
    return _norm(y * _env(n, 0.05, d * 0.9, 1.5))


def retumbo(d=1.8, seed=0):
    """Temblor grave sostenido (hundimiento, tierra que cede)."""
    r = _rng(seed); n = int(d * SR); t = _t(d)
    y = _filtro(r.standard_normal(n), "lowpass", 90, 4) * (0.6 + 0.4 * np.sin(2 * np.pi * 7 * t + r.uniform(0, 6)))
    y += np.sin(2 * np.pi * 42 * t) * 0.35
    return _norm(y * np.sin(np.pi * np.linspace(0, 1, n)) ** 0.7)


def viento(d=2.5, seed=0):
    """Ráfaga de viento (el edificio se balancea)."""
    r = _rng(seed); n = int(d * SR); t = np.linspace(0, 1, n)
    mod = 0.5 + 0.5 * np.sin(2 * np.pi * (1.3 * t) + r.uniform(0, 6))
    y = _filtro(r.standard_normal(n), "bandpass", [250, 1600], 2) * (0.3 + 0.7 * mod)
    return _norm(y * np.sin(np.pi * t) ** 0.6, 0.7)


def campana(f=880, d=1.6, seed=0):
    """«Ding» con parciales de campana (ascensor que llega, dato clave)."""
    t = _t(d); y = np.zeros_like(t)
    for k, (m, a, c) in enumerate([(1, 1.0, 3.0), (2.0, 0.5, 4.0), (2.76, 0.35, 5.0), (5.4, 0.18, 8.0)]):
        y += a * np.sin(2 * np.pi * f * m * t) * np.exp(-c * t)
    return _norm(y * np.minimum(1, t / 0.002))


def pop(d=0.18, seed=0):
    """Aparición de una cifra o pieza (corte seco y brillante)."""
    n = int(d * SR); t = _t(d); f = 300 + 900 * np.exp(-t * 28)
    return _norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * _env(n, 0.001, 0.06, 4))


def ascensor(d=2.0, seed=0):
    """Zumbido de ascensor que acelera (tono que sube + aire)."""
    r = _rng(seed); n = int(d * SR); t = _t(d)
    f = 70 + 150 * (t / d) ** 1.5; saw = signal.sawtooth(2 * np.pi * np.cumsum(f) / SR)
    y = _filtro(saw, "lowpass", 700) * 0.6 + _filtro(r.standard_normal(n), "bandpass", [300, 2500], 2) * 0.25 * (t / d)
    return _norm(y * np.minimum(1, t / 0.15) * np.minimum(1, (d - t) / 0.2))


def balanceo(d=1.6, seed=0):
    """Tintineo metálico grave (la esfera de acero se mueve): campana grave con vaivén."""
    t = _t(d); y = np.sin(2 * np.pi * 196 * t) * np.exp(-2.2 * t) + 0.5 * np.sin(2 * np.pi * 523 * t) * np.exp(-3.5 * t)
    return _norm(y * (1 + 0.25 * np.sin(2 * np.pi * 2.2 * t)) * np.minimum(1, t / 0.004), 0.8)


EFECTOS = {"whoosh": whoosh, "impacto": impacto, "grieta": grieta, "crujido": crujido, "retumbo": retumbo, "viento": viento,
           "campana": campana, "pop": pop, "ascensor": ascensor, "balanceo": balanceo}


def efecto(nombre, **kw):
    if nombre not in EFECTOS: raise KeyError(f"efecto desconocido: {nombre}")
    return EFECTOS[nombre](**kw)


def mezclar(eventos, duracion, seed=0):
    """eventos: [(segundo_de_inicio, nombre, volumen 0..1)] -> pista mono float32 de `duracion` s."""
    y = np.zeros(int(duracion * SR) + SR, dtype=np.float32)
    for k, ev in enumerate(eventos):
        t0, nombre, vol = ev[:3]; e = efecto(nombre, seed=seed + k) * vol; i = int(t0 * SR)
        y[i:i + len(e)] += e[: len(y) - i]
    return np.clip(y[: int(duracion * SR)], -1, 1)


if __name__ == "__main__":
    import soundfile as sf
    d = sys.argv[1] if len(sys.argv) > 1 else "sfx_demo"; os.makedirs(d, exist_ok=True)
    for nombre in EFECTOS:
        y = efecto(nombre, seed=1); sf.write(os.path.join(d, nombre + ".wav"), y, SR)
        print(f"{nombre:9s} {len(y)/SR:4.2f} s  pico {np.max(np.abs(y)):.2f}  rms {np.sqrt(np.mean(y**2)):.3f}  NaN: {bool(np.isnan(y).any())}")
