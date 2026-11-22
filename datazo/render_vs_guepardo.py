#!/usr/bin/env python3
"""Datazo VS: Guepardo vs Usain Bolt. Genera el MP4 vertical (1080x1920, 30 fps, sin audio),
el archivo de subtítulos .srt y la guía de tiempos para grabar la voz.

Uso: python3 -I render_vs_guepardo.py [salida.mp4] [--prueba SEGUNDO ...]
  --prueba 3.0 12.5   guarda esos fotogramas como PNG en lugar de generar el vídeo.
Todo el dibujo es propio (código); no hay imágenes ni personajes de terceros.
"""
import json
import math
import os
import subprocess
import sys
from multiprocessing import Pool

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import motor as m  # noqa: E402

W, H, FPS = m.W, m.H, m.FPS

# ------------------------------------------------------------------ DATOS (verificados)
CFG = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos_vs_guepardo.json"), encoding="utf-8"))
T_CHEETAH = CFG["guepardo_s"]          # segundos en 100 m
T_BOLT = CFG["bolt_s"]
BOLT_SPLITS = CFG.get("bolt_parciales")  # [[metros, segundos], ...] o null
BOLT_KMH = CFG["bolt_kmh"]
CHEETAH_KMH = CFG["guepardo_kmh_texto"]  # texto, p. ej. "más de 100"
CHEETAH_KMH_BAR = CFG["guepardo_kmh_barra"]
BOLT_AT_FINISH_M = CFG.get("bolt_metros_cuando_llega_guepardo")  # int o null

# ------------------------------------------------------------------ GUION (subtítulos = locución)
CAPTIONS = CFG["subtitulos"]  # lista de {ini, fin, texto, resalta[]}
TOTAL = CFG["duracion_total_s"]

# ------------------------------------------------------------------ DISEÑO
START_X, FIN_X = 300, 960
GROUND_C, GROUND_R = 600, 940           # suelo de cada carril
T_RACE0 = CFG["inicio_carrera_s"]       # instante del disparo de salida
P1_END = CFG["fin_presentacion_s"]


def fmt(x):
    return f"{x:.2f}".replace(".", ",")


def hermite(ts, ds):
    """Interpolación monótona suave (Fritsch-Carlson simplificada) de la distancia en el tiempo."""
    ts, ds = np.array(ts, float), np.array(ds, float)
    dk = np.diff(ds) / np.diff(ts)
    mk = np.zeros_like(ts)
    mk[0], mk[-1] = dk[0], dk[-1]
    for i in range(1, len(ts) - 1):
        mk[i] = 0.0 if dk[i - 1] * dk[i] <= 0 else 2 / (1 / dk[i - 1] + 1 / dk[i])

    def f(t):
        if t <= ts[0]:
            return 0.0
        if t >= ts[-1]:
            return float(ds[-1])
        i = int(np.searchsorted(ts, t) - 1)
        h = ts[i + 1] - ts[i]
        s = (t - ts[i]) / h
        h00, h10, h01, h11 = 2 * s**3 - 3 * s**2 + 1, s**3 - 2 * s**2 + s, -2 * s**3 + 3 * s**2, s**3 - s**2
        return float(h00 * ds[i] + h10 * h * mk[i] + h01 * ds[i + 1] + h11 * h * mk[i + 1])

    return f


if BOLT_SPLITS:
    _pts = [(0.0, 0.0)] + [(s, mt) for mt, s in BOLT_SPLITS] + [(T_BOLT, 100.0)]
    _pts = sorted(set(_pts))
    _bolt_f = hermite([p[0] for p in _pts], [p[1] for p in _pts])
else:
    _bolt_f = None


def dist_cheetah(tr):
    """Metros recorridos por el guepardo tras `tr` segundos de carrera (aceleración 2 s y ritmo constante)."""
    if tr <= 0:
        return 0.0
    acc = 2.0
    v = 100.0 / (T_CHEETAH - acc / 2)
    if tr <= acc:
        return v * tr * tr / (2 * acc)
    if tr <= T_CHEETAH:
        return v * acc / 2 + v * (tr - acc)
    # frena tras la meta
    e = tr - T_CHEETAH
    tau = 0.45
    return 100.0 + v * tau * (1 - math.exp(-e / tau))


def dist_bolt(tr):
    if tr <= 0:
        return 0.0
    if tr <= T_BOLT:
        if _bolt_f:
            return _bolt_f(tr)
        acc = 3.0
        v = 100.0 / (T_BOLT - acc / 2)
        return v * tr * tr / (2 * acc) if tr <= acc else v * acc / 2 + v * (tr - acc)
    e = tr - T_BOLT
    v = 12.0
    tau = 0.5
    return 100.0 + v * tau * (1 - math.exp(-e / tau))


def speed_cheetah(tr):
    return (dist_cheetah(tr + 0.02) - dist_cheetah(tr - 0.02)) / 0.04 if tr > 0 else 0.0


def speed_bolt(tr):
    return (dist_bolt(tr + 0.02) - dist_bolt(tr - 0.02)) / 0.04 if tr > 0 else 0.0


# ------------------------------------------------------------------ CAPAS ESTÁTICAS
_static = {}


def lanes_layer():
    if "lanes" in _static:
        return _static["lanes"]
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(L)
    for g in (GROUND_C, GROUND_R):
        d.rounded_rectangle([60, g - 4, 1020, g + 44], radius=14, fill=m.rgba(m.BG2))
        for k in range(0, 101, 10):
            x = START_X + (FIN_X - START_X) * k / 100
            hh = 26 if k % 50 == 0 else 14
            d.line([(x, g + 4), (x, g + 4 + hh)], fill=m.rgba(m.BG3), width=4)
        if g == GROUND_R:
            for k, lab in ((0, "0"), (50, "50"), (100, "100 m")):
                x = START_X + (FIN_X - START_X) * k / 100
                d.text((x, g + 74), lab, font=m.font("Bold", 30), fill=m.rgba(m.SOFT, 170), anchor="mm")
    # meta (cuadros)
    for g in (GROUND_C, GROUND_R):
        x0 = FIN_X
        for r in range(8):
            for c in range(2):
                col = m.WHITE if (r + c) % 2 == 0 else m.BG
                d.rectangle([x0 + c * 14, g - 4 - 174 + r * 22, x0 + c * 14 + 13, g - 4 - 174 + r * 22 + 21], fill=m.rgba(col))
        d.rectangle([x0, g - 4 - 174, x0 + 28, g - 4 - 174 + 176], outline=m.rgba(m.YELLOW), width=3)
    _static["lanes"] = L
    return L


# ------------------------------------------------------------------ ESCENA
def sprite_xy_cheetah(tr, tt):
    """Devuelve (x, y_suelo, escala, fase) del guepardo según la etapa."""
    if tt < P1_END:
        return 540 - 200, GROUND_C, 0.95, 0.9 + 6.0 * tt        # corre en el sitio durante la presentación
    return None


def draw_frame(t):
    img = m.background()
    m.header(img)
    d = ImageDraw.Draw(img)

    tr = t - T_RACE0                                    # tiempo de carrera
    # transición presentación -> carriles
    k = m.ease_in_out((t - P1_END) / 0.7)
    in_p1 = t < P1_END + 0.7

    # ---- posiciones y escalas
    sc_c = m.lerp(0.95, 0.72, k)
    sc_r = m.lerp(0.95, 0.72, k)
    g_c = GROUND_C
    g_r = m.lerp(1020, GROUND_R, k)

    # nariz del guepardo en unidades del sprite: 403; frente del velocista: 196
    NOSE_U, FRONT_U = 403, 196

    def nose_px(dm):
        return START_X + (FIN_X - START_X) * dm / 100

    if t < P1_END:
        cx_nose = 540 + 190
        rx_front = 540 + 100
    else:
        cx_nose = m.lerp(540 + 190, nose_px(dist_cheetah(tr)), k)
        rx_front = m.lerp(540 + 100, nose_px(dist_bolt(tr)), k)

    # fases de carrera
    racing_c = tr > 0 and tr < T_CHEETAH + 0.9
    racing_r = tr > 0 and tr < T_BOLT + 0.8
    if t < P1_END:
        ph_c, ph_r = 0.9 + 6.2 * t, 0.6 + 5.2 * t       # corren en el sitio
    elif racing_c or (tr <= 0 and False):
        ph_c = 6.0 * tr * (0.6 + 0.4 * min(1, speed_cheetah(tr) / 18))
    else:
        ph_c = 2.7
    if t >= P1_END:
        if racing_r:
            ph_r = 5.0 * tr * (0.6 + 0.4 * min(1, speed_bolt(tr) / 11))
        else:
            ph_r = 3.15
    if 0 < t - P1_END < 0.7:                            # al reordenar, siguen en el sitio
        ph_c, ph_r = 0.9 + 6.2 * t, 0.6 + 5.2 * t
    if tr <= 0 and t >= P1_END + 0.7:
        ph_c, ph_r = 2.7, 3.15                          # esperando la salida

    # carriles y meta
    lane_alpha = k
    if lane_alpha > 0:
        L = lanes_layer().copy()
        if lane_alpha < 1:
            L.putalpha(L.getchannel("A").point(lambda v: int(v * lane_alpha)))
        img.alpha_composite(L)

    # sprites
    cs = m.cheetah(ph_c)
    rs = m.sprinter(ph_r)
    cx = cx_nose - NOSE_U * sc_c
    cy = g_c - 232 * sc_c
    m.paste_sprite(img, cs, cx, cy, sc_c)
    rx = rx_front - FRONT_U * sc_r
    ry = g_r - 322 * sc_r
    m.paste_sprite(img, rs, rx, ry, sc_r)

    # ---- presentación: títulos y VS
    if t < P1_END + 0.7:
        a = int(255 * (1 - m.clamp(k * 2.5)))
        if a > 0:
            m.draw_text_center(img, "GUEPARDO", 540, g_c + 82, m.font("Black", 112), m.YELLOW, alpha=a)
            m.draw_text_center(img, "BOLT", 540, g_r + 90, m.font("Black", 112), m.WHITE, alpha=a)
            vs_s = m.ease_back((t - 0.5) / 0.5)
            vs_layer = Image.new("RGBA", (260, 260), (0, 0, 0, 0))
            vd = ImageDraw.Draw(vs_layer)
            r = 120
            vd.polygon([(130, 10), (250, 130), (130, 250), (10, 130)], fill=m.rgba(m.YELLOW))
            vd.text((130, 134), "VS", font=m.font("Black", 92), fill=m.rgba(m.BG), anchor="mm")
            sz = max(1, int(190 * vs_s * (1.0 if a == 255 else (a / 255))))
            vs_small = vs_layer.resize((sz, sz), Image.LANCZOS)
            img.alpha_composite(vs_small, (900 - sz // 2, 880 - sz // 2))

    # ---- etiquetas de carril y relojes
    if k > 0.55:
        la = int(255 * m.clamp((k - 0.55) / 0.45))
        card_r = m.ease_out((t - P1_END) / 0.5)
        card_c = m.ease_out((t - CFG["tarjeta_guepardo_s"]) / 0.5)
        # guepardo
        y_lab = g_c - 232 * sc_c - 58
        m.draw_text_center(img, "GUEPARDO", 230, y_lab, m.font("Black", 52), m.YELLOW, alpha=la)
        lab_c = "RÉCORD GUINNESS" if card_c > 0.01 else ""
        # velocista
        y_lab_r = g_r - 322 * sc_r - 40
        m.draw_text_center(img, "USAIN BOLT", 250, y_lab_r, m.font("Black", 52), m.WHITE, alpha=la)

        def clock(tt_cap, dist_t, cx_, cy_, col):
            if tr <= 0:
                txt, col2, size = "0,00 s", m.SOFT, 76
            elif tr < tt_cap:
                txt, col2, size = fmt(tr) + " s", m.WHITE, 76
            else:
                pop = m.ease_back((tr - tt_cap) / 0.35)
                txt, col2, size = fmt(tt_cap) + " s", col, int(76 + 20 * min(1.0, pop))
            return txt, col2, size

        txt, col2, size = clock(T_CHEETAH, None, 0, 0, m.YELLOW)
        m.draw_text_center(img, txt, 880, y_lab, m.font("Black", size), col2, alpha=la)
        txt, col2, size = clock(T_BOLT, None, 0, 0, m.YELLOW)
        m.draw_text_center(img, txt, 880, y_lab_r, m.font("Black", size), col2, alpha=la)
        # tarjetas de récord (debajo del nombre)
        if card_r > 0.01 and tr <= 0:
            m.draw_text_center(img, "récord mundial · 100 m", 262, y_lab_r + 50, m.font("SemiBold", 32), m.SOFT, alpha=int(la * card_r))
        if card_c > 0.01 and tr <= 0:
            m.draw_text_center(img, "récord Guinness · 100 m", 262, y_lab + 50, m.font("SemiBold", 32), m.SOFT, alpha=int(la * card_c))

    # ---- cuenta atrás y salida
    c0 = CFG["cuenta_atras_s"]
    if c0 <= t < T_RACE0:
        n = 3 - int((t - c0) / ((T_RACE0 - c0) / 3))
        n = max(1, min(3, n))
        ph = ((t - c0) % ((T_RACE0 - c0) / 3)) / ((T_RACE0 - c0) / 3)
        s = 1.0 + 0.35 * (1 - m.ease_out(ph * 2))
        m.draw_text_center(img, str(n), 540, 1230, m.font("Black", int(250 * s)), m.YELLOW, stroke=8, stroke_fill=m.BG, alpha=int(255 * (1 - 0.3 * ph)))
    if T_RACE0 <= t < T_RACE0 + 0.6:
        ph = (t - T_RACE0) / 0.6
        m.draw_text_center(img, "¡YA!", 540, 1230, m.font("Black", int(230 * (1 + 0.2 * ph))), m.YELLOW, stroke=8, stroke_fill=m.BG, alpha=int(255 * (1 - ph)))

    # ---- marca de “dónde iba Bolt” cuando llega el guepardo
    if BOLT_AT_FINISH_M and T_CHEETAH <= tr < T_BOLT + 0.5:
        a = int(255 * m.ease_out((tr - T_CHEETAH) / 0.3))
        xb = nose_px(dist_bolt(T_CHEETAH))
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        yb0, yb1 = g_r - 180, g_r + 4
        for y in range(int(yb0), int(yb1), 18):
            ld.line([(xb, y), (xb, y + 9)], fill=m.rgba(m.YELLOW, a), width=5)
        ld.rounded_rectangle([xb - 76, yb0 - 62, xb + 76, yb0 - 8], radius=16, fill=m.rgba(m.YELLOW, a))
        ld.text((xb, yb0 - 35), f"≈ {BOLT_AT_FINISH_M} m", font=m.font("Black", 38), fill=m.rgba(m.BG, a), anchor="mm")
        img.alpha_composite(layer)

    # ---- ventaja final
    if tr >= T_BOLT + 0.3 and t < CFG["fin_resultados_s"]:
        a = m.ease_out((tr - T_BOLT - 0.3) / 0.4)
        diff = T_BOLT - T_CHEETAH
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        ld.rounded_rectangle([170, 1100, 910, 1190], radius=30, fill=m.rgba(m.YELLOW, int(255 * a)))
        ld.text((540, 1145), f"Ganó el guepardo por {fmt(diff)} s", font=m.font("Black", 50), fill=m.rgba(m.BG, int(255 * a)), anchor="mm")
        img.alpha_composite(layer)

    # ---- barras de velocidad
    t_b0, t_b1 = CFG["barras_ini_s"], CFG["barras_fin_s"]
    if t_b0 <= t < t_b1 + 0.4:
        a = m.ease_out((t - t_b0) / 0.4) * (1 - m.clamp((t - t_b1) / 0.4))
        gr = m.ease_out((t - t_b0 - 0.2) / 0.9)
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        top = 1278
        full = 540
        ld.text((540, top - 52), "Velocidad media en su récord de 100 m", font=m.font("SemiBold", 32), fill=m.rgba(m.SOFT, int(255 * a)), anchor="mm")
        rows = (("BOLT", BOLT_KMH, f"{BOLT_KMH:.1f} km/h".replace(".", ","), m.WHITE),
                ("GUEPARDO", CHEETAH_KMH_BAR, f"{CHEETAH_KMH} km/h", m.YELLOW))
        scale = CHEETAH_KMH_BAR
        for i, (nm, val, lab, col) in enumerate(rows):
            y = top + i * 78
            ld.text((50, y), nm, font=m.font("Black", 30), fill=m.rgba(m.SOFT, int(255 * a)), anchor="lm")
            L = max(20, full * val / scale * gr)
            ld.rounded_rectangle([270, y - 26, 270 + L, y + 26], radius=18, fill=m.rgba(col, int(255 * a)))
            ld.text((270 + L + 14, y), lab, font=m.font("Black", 38), fill=m.rgba(col, int(255 * a)), anchor="lm")
        img.alpha_composite(layer)

    # ---- nota de honestidad
    if t >= P1_END + 0.7 and t < CFG["fin_resultados_s"]:
        m.draw_text_center(img, "Tiempos reales · trayecto ilustrativo", 540, g_r + 112, m.font("Medium", 30), m.SOFT, alpha=170)

    # ---- subtítulos
    end_card = t >= CFG["tarjeta_final_s"]
    if not end_card:
        for c in CAPTIONS:
            if c["ini"] <= t < c["fin"]:
                a = int(255 * m.clamp((t - c["ini"]) / 0.12))
                m.draw_caption(img, c["texto"], c.get("resalta", []), cy=CFG.get("subtitulos_y", 1470), size=80, alpha=a)
                break

    # ---- tarjeta final
    if end_card:
        a = m.ease_out((t - CFG["tarjeta_final_s"]) / 0.4)
        img = m.background()
        lg = m.logo(300)
        img.alpha_composite(lg, (540 - 150, 560))
        m.draw_text_center(img, "DATAZO", 540, 960, m.font("Black", 130), m.WHITE)
        m.draw_text_center(img, "Datos curiosos en menos de un minuto", 540, 1070, m.font("SemiBold", 44), m.YELLOW)
        m.draw_text_center(img, CFG["frase_final"], 540, 1280, m.font("ExtraBold", 66), m.WHITE, stroke=5)
        if a < 1:
            base = m.background()
            base.alpha_composite(Image.blend(base, img, a))
            img = Image.blend(base.copy(), img, a)
    return img.convert("RGB")


def _render(i):
    return np.asarray(draw_frame(i / FPS), dtype=np.uint8).tobytes()


def write_srt(path):
    def ts(x):
        h, r = divmod(x, 3600)
        mi, r = divmod(r, 60)
        s, ms = divmod(r, 1)
        return f"{int(h):02d}:{int(mi):02d}:{int(s):02d},{int(ms * 1000):03d}"
    with open(path, "w", encoding="utf-8") as f:
        for i, c in enumerate(CAPTIONS, 1):
            f.write(f"{i}\n{ts(c['ini'])} --> {ts(c['fin'])}\n{c['texto']}\n\n")


def main():
    args = sys.argv[1:]
    if "--prueba" in args:
        i = args.index("--prueba")
        outdir = os.environ.get("PRUEBAS", "/tmp")
        for s in args[i + 1:]:
            p = os.path.join(outdir, f"frame_{float(s):05.2f}.png")
            draw_frame(float(s)).save(p)
            print(p)
        return
    out = args[0] if args else "datazo_vs_guepardo_bolt.mp4"
    n = int(round(TOTAL * FPS))
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-profile:v", "high",
           "-level", "4.1", "-movflags", "+faststart", "-an", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    with Pool(4) as pool:
        for k, buf in enumerate(pool.imap(_render, range(n), chunksize=6)):
            p.stdin.write(buf)
            if k % 150 == 0:
                print(f"fotograma {k}/{n}", flush=True)
    p.stdin.close()
    p.wait()
    write_srt(os.path.splitext(out)[0] + ".srt")
    print("listo:", out)


if __name__ == "__main__":
    main()
