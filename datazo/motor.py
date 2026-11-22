"""Motor de animación de Datazo: paleta, tipografía, logo, subtítulos, curvas y sprites
dibujados por código (todo es obra propia; no se usan imágenes ni personajes de terceros).

Solo depende de Pillow y numpy. La fuente Inter (licencia OFL) se lee del sistema.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30

# --- Paleta de Datazo: fondo azul oscuro, letras amarillas y blancas -----------------
BG = (9, 24, 48)            # azul oscuro de fondo
BG2 = (15, 38, 72)          # azul medio para formas y pistas
BG3 = (24, 54, 98)          # azul claro para líneas
YELLOW = (255, 210, 31)
WHITE = (255, 255, 255)
SOFT = (200, 214, 235)      # blanco azulado para textos secundarios
ORANGE = (247, 168, 51)     # cuerpo del guepardo
ORANGE_D = (214, 128, 24)   # patas lejanas
CREAM = (255, 226, 160)
INK = (24, 22, 38)          # manchas
RED = (255, 99, 99)

FONT_DIR = "/usr/share/fonts/opentype/inter/"


def font(weight="Bold", size=60):
    return ImageFont.truetype(f"{FONT_DIR}Inter-{weight}.otf", size)


# --- Curvas de easing ----------------------------------------------------------------
def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def lerp(a, b, t):
    return a + (b - a) * t


def ease_out(t):
    t = clamp(t)
    return 1 - (1 - t) ** 3


def ease_in_out(t):
    t = clamp(t)
    return 3 * t * t - 2 * t * t * t


def ease_back(t, s=1.70158):
    t = clamp(t)
    return 1 + (s + 1) * (t - 1) ** 3 + s * (t - 1) ** 2


# --- Utilidades de dibujo ------------------------------------------------------------
def rgba(c, a=255):
    return (c[0], c[1], c[2], a)


def catmull(points, closed=True, n=10):
    """Spline de Catmull-Rom: convierte puntos de control en un contorno suave."""
    pts = list(points)
    m = len(pts)
    out = []
    rng = range(m) if closed else range(m - 1)
    for i in rng:
        p0 = pts[(i - 1) % m] if closed or i > 0 else pts[i]
        p1 = pts[i]
        p2 = pts[(i + 1) % m]
        p3 = pts[(i + 2) % m] if closed or i + 2 < m else pts[(i + 1) % m]
        for k in range(n):
            t = k / n
            t2, t3 = t * t, t * t * t
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    return out


def thick_line(d, p, q, width, fill):
    """Línea con extremos redondeados."""
    d.line([p, q], fill=fill, width=int(width))
    r = width / 2
    for c in (p, q):
        d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=fill)


def limb(d, root, ang1, len1, ang2, len2, w1, w2, fill):
    """Pata o brazo de dos tramos. Ángulos en grados medidos desde la vertical hacia abajo
    (positivo = hacia adelante, a la derecha). El segundo ángulo es relativo al primero.
    Devuelve (rodilla, pie)."""
    a1 = math.radians(ang1)
    knee = (root[0] + len1 * math.sin(a1), root[1] + len1 * math.cos(a1))
    a2 = math.radians(ang1 + ang2)
    foot = (knee[0] + len2 * math.sin(a2), knee[1] + len2 * math.cos(a2))
    thick_line(d, root, knee, w1, fill)
    thick_line(d, knee, foot, w2, fill)
    return knee, foot


def text_size(d, s, f):
    b = d.textbbox((0, 0), s, font=f)
    return b[2] - b[0], b[3] - b[1]


def draw_text_center(img, s, cx, cy, f, fill, stroke=0, stroke_fill=None, alpha=255):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text((cx, cy), s, font=f, fill=rgba(fill, alpha), anchor="mm",
           stroke_width=stroke, stroke_fill=rgba(stroke_fill or BG, alpha))
    img.alpha_composite(layer)


# --- Logo: una D dentro de un rombo amarillo ---------------------------------------------
_logo_cache = {}


def logo(size):
    if size in _logo_cache:
        return _logo_cache[size]
    s = 4
    big = Image.new("RGBA", (size * s, size * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    c = size * s / 2
    r = size * s / 2 * 0.98
    d.polygon([(c, c - r), (c + r, c), (c, c + r), (c - r, c)], fill=rgba(YELLOW))
    f = font("Black", int(size * s * 0.52))
    d.text((c, c + size * s * 0.02), "D", font=f, fill=rgba(BG), anchor="mm")
    img = big.resize((size, size), Image.LANCZOS)
    _logo_cache[size] = img
    return img


# --- Fondo ---------------------------------------------------------------------------
_bg_cache = {}


def background():
    """Fondo azul oscuro con una trama muy sutil de rombos (se calcula una sola vez)."""
    if "bg" in _bg_cache:
        return _bg_cache["bg"].copy()
    img = Image.new("RGBA", (W, H), rgba(BG))
    d = ImageDraw.Draw(img)
    step = 180
    for gy in range(-1, H // step + 2):
        for gx in range(-1, W // step + 2):
            cx = gx * step + (step // 2 if gy % 2 else 0)
            cy = gy * step
            r = 9
            d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=rgba(BG2))
    _bg_cache["bg"] = img
    return img.copy()


# --- Sprites -------------------------------------------------------------------------
def cheetah(phase, S=3, w=470, h=240):
    """Guepardo corriendo hacia la derecha. phase en radianes (ciclo de galope)."""
    img = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    def P(x, y):
        return (x * S, y * S)

    bounce = -12 * (0.5 + 0.5 * math.sin(2 * phase + 0.6))   # el cuerpo sube en la fase aérea
    stretch = 8 * math.sin(2 * phase)                        # la columna se estira y se encoge

    def body_pt(x, y):
        return P(x + 30 + (stretch * (x - 190) / 140), y + bounce)

    # patas lejanas (más oscuras) primero
    hind_root = body_pt(98, 124)
    front_root = body_pt(272, 122)
    far_color = rgba(ORANGE_D)
    near_color = rgba(ORANGE)
    for root, off, amp, flex, far in (
        (hind_root, 0.9, 50, 85, True), (front_root, 0.3, 46, 80, True),
    ):
        ph = phase + off
        up = amp * math.sin(ph)
        lo = -flex * (0.45 + 0.55 * math.cos(ph))
        k, f = limb(d, root, up, 52 * S, lo, 56 * S, 15 * S, 12 * S, far_color)
        d.ellipse([f[0] - 9 * S, f[1] - 5 * S, f[0] + 13 * S, f[1] + 7 * S], fill=far_color)

    # cola
    tail_pts = [body_pt(76, 98), body_pt(44, 92 + 4 * math.sin(phase)), body_pt(14, 104 + 7 * math.sin(phase + 0.8)),
                body_pt(6, 126 + 8 * math.sin(phase + 1.2)), body_pt(20, 146 + 6 * math.sin(phase + 1.6))]
    tl = catmull(tail_pts, closed=False, n=14)
    for i in range(len(tl) - 1):
        wd = (15 - 8 * i / len(tl)) * S
        thick_line(d, tl[i], tl[i + 1], wd, rgba(ORANGE))
    for i in range(int(len(tl) * 0.55), len(tl) - 2, 4):
        thick_line(d, tl[i], tl[i + 1], 6 * S, rgba(INK))

    # cuerpo
    body = catmull([body_pt(70, 96), body_pt(125, 80), body_pt(195, 82), body_pt(255, 86), body_pt(298, 94),
                    body_pt(312, 108), body_pt(285, 132), body_pt(230, 140), body_pt(170, 134),
                    body_pt(112, 130), body_pt(70, 118)], closed=True, n=12)
    d.polygon(body, fill=rgba(ORANGE))
    # vientre claro
    belly = catmull([body_pt(120, 124), body_pt(190, 118), body_pt(262, 120), body_pt(286, 130),
                     body_pt(230, 140), body_pt(170, 134)], closed=True, n=8)
    d.polygon(belly, fill=rgba(CREAM))
    # manchas (posiciones fijas, siguen al cuerpo)
    spots = [(95, 100), (118, 92), (142, 98), (166, 90), (190, 97), (214, 90), (238, 98), (262, 93),
             (284, 101), (108, 114), (136, 110), (160, 108), (186, 109), (212, 108), (240, 112), (268, 110)]
    for (sx, sy) in spots:
        c = body_pt(sx, sy)
        r = 5.2 * S
        d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=rgba(INK))

    # cuello y cabeza
    neck = catmull([body_pt(268, 88), body_pt(296, 62), body_pt(326, 50), body_pt(340, 72), body_pt(312, 112)],
                   closed=True, n=10)
    d.polygon(neck, fill=rgba(ORANGE))
    hc = body_pt(340, 58)
    d.ellipse([hc[0] - 25 * S, hc[1] - 23 * S, hc[0] + 25 * S, hc[1] + 23 * S], fill=rgba(ORANGE))
    mz = body_pt(360, 68)
    d.ellipse([mz[0] - 17 * S, mz[1] - 12 * S, mz[0] + 15 * S, mz[1] + 12 * S], fill=rgba(CREAM))
    nose = body_pt(373, 62)
    d.ellipse([nose[0] - 5 * S, nose[1] - 4 * S, nose[0] + 4 * S, nose[1] + 4 * S], fill=rgba(INK))
    for ex in ((322, 38), (336, 32)):
        e = body_pt(*ex)
        d.polygon([(e[0] - 7 * S, e[1] + 8 * S), (e[0] + 1 * S, e[1] - 12 * S), (e[0] + 10 * S, e[1] + 8 * S)], fill=rgba(ORANGE_D))
    ey = body_pt(348, 53)
    d.ellipse([ey[0] - 4 * S, ey[1] - 4 * S, ey[0] + 4 * S, ey[1] + 4 * S], fill=rgba(INK))
    t1, t2 = body_pt(350, 58), body_pt(358, 80)
    thick_line(d, t1, t2, 4.5 * S, rgba(INK))
    for (sx, sy) in ((318, 66), (326, 78), (306, 74), (331, 44)):
        c = body_pt(sx, sy)
        d.ellipse([c[0] - 3.3 * S, c[1] - 3.3 * S, c[0] + 3.3 * S, c[1] + 3.3 * S], fill=rgba(INK))

    # patas cercanas
    for root, off, amp, flex in ((hind_root, 0.9 + math.pi, 50, 85), (front_root, 0.3 + math.pi, 46, 80)):
        ph = phase + off
        up = amp * math.sin(ph)
        lo = -flex * (0.45 + 0.55 * math.cos(ph))
        k, f = limb(d, root, up, 52 * S, lo, 56 * S, 16 * S, 12.5 * S, near_color)
        d.ellipse([f[0] - 9 * S, f[1] - 5 * S, f[0] + 13 * S, f[1] + 7 * S], fill=near_color)
        c = (k[0], k[1])
        d.ellipse([c[0] - 4 * S, c[1] - 4 * S, c[0] + 4 * S, c[1] + 4 * S], fill=rgba(INK))
    return img


def sprinter(phase, S=3, w=270, h=320):
    """Velocista genérico (silueta blanca, sin rasgos ni parecido con nadie en concreto)."""
    img = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    def P(x, y):
        return (x * S, y * S)

    bob = -6 * (0.5 + 0.5 * math.sin(2 * phase + 0.4))
    hip = P(128, 168 + bob)
    lean = math.radians(18)
    sh = (hip[0] + 88 * S * math.sin(lean), hip[1] - 88 * S * math.cos(lean))
    body_w = rgba(WHITE)
    # piernas (la lejana primero, en gris azulado)
    far = rgba(SOFT)
    for ph_off, col in ((math.pi, far), (0, body_w)):
        ph = phase + ph_off
        th = 52 * math.sin(ph)
        sh_rel = -(18 + 92 * max(0.0, math.sin(ph + 0.9)))
        k, f = limb(d, hip, th, 76 * S, sh_rel, 78 * S, 25 * S, 18 * S, col)
        d.polygon([(f[0] - 6 * S, f[1] - 4 * S), (f[0] + 26 * S, f[1] + 5 * S), (f[0] - 8 * S, f[1] + 9 * S)], fill=rgba(YELLOW))
    # torso
    thick_line(d, hip, sh, 40 * S, body_w)
    # pantalón corto amarillo
    thick_line(d, hip, (hip[0] + 10 * S * math.sin(lean), hip[1] - 10 * S), 44 * S, rgba(YELLOW))
    # brazos (contrarios a las piernas)
    for ph_off, col in ((0, far), (math.pi, body_w)):
        ph = phase + ph_off
        up = -60 * math.sin(ph) + 20
        lo = 85 + 20 * math.sin(ph)
        limb(d, (sh[0] - 2 * S, sh[1] + 4 * S), up, 44 * S, -lo + 40, 42 * S, 15 * S, 13 * S, col)
    # cabeza
    hc = (sh[0] + 20 * S, sh[1] - 26 * S)
    d.ellipse([hc[0] - 21 * S, hc[1] - 22 * S, hc[0] + 21 * S, hc[1] + 22 * S], fill=body_w)
    thick_line(d, (hc[0] - 22 * S, hc[1] - 4 * S), (hc[0] + 22 * S, hc[1] - 4 * S), 7 * S, rgba(YELLOW))
    return img


def paste_sprite(img, sprite, x, y, scale, flip=False):
    """Reduce el sprite (supersampleado) y lo pega con su esquina superior izquierda en (x, y)."""
    nw, nh = int(sprite.width * scale / 3), int(sprite.height * scale / 3)
    small = sprite.resize((nw, nh), Image.LANCZOS)
    if flip:
        small = small.transpose(Image.FLIP_LEFT_RIGHT)
    img.alpha_composite(small, (int(x), int(y)))
    return small.size


# --- Subtítulos grandes -------------------------------------------------------------------
def draw_caption(img, text, highlight=(), cy=1330, size=92, alpha=255, max_w=900):
    """Subtítulo centrado, blanco con contorno azul; las palabras de `highlight` van en amarillo."""
    f = font("ExtraBold", size)
    d = ImageDraw.Draw(img)
    words = text.split()
    # partir en líneas que quepan
    lines, cur = [], []
    for w_ in words:
        trial = " ".join(cur + [w_])
        if text_size(d, trial, f)[0] > max_w and cur:
            lines.append(cur)
            cur = [w_]
        else:
            cur.append(w_)
    if cur:
        lines.append(cur)
    lh = int(size * 1.18)
    y0 = cy - (len(lines) - 1) * lh / 2
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    hl = {h_.lower().strip(".,;:¿?¡!") for h_ in highlight}
    for i, line in enumerate(lines):
        total = text_size(ld, " ".join(line), f)[0]
        x = W / 2 - total / 2
        sp = text_size(ld, " ", f)[0] or int(size * 0.28)
        for w_ in line:
            col = YELLOW if w_.lower().strip(".,;:¿?¡!") in hl else WHITE
            ww = ld.textlength(w_, font=f)
            ld.text((x, y0 + i * lh), w_, font=f, fill=rgba(col, alpha), anchor="lm",
                    stroke_width=max(4, size // 14), stroke_fill=rgba(BG, alpha))
            x += ww + sp
    img.alpha_composite(layer)


def header(img, label="DATAZO", alpha=255):
    """Logo y nombre del canal arriba a la izquierda (fuera de las zonas que tapa la interfaz de Shorts)."""
    lg = logo(96)
    img.alpha_composite(lg, (56, 128))
    draw = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(draw)
    d.text((170, 176), label, font=font("Black", 54), fill=rgba(WHITE, alpha), anchor="lm")
    img.alpha_composite(draw)
