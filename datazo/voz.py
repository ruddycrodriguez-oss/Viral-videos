"""Narración con voz de IA para todos los formatos de Datazo (A, B y C).

Voz: Kokoro-82M (pesos Apache-2.0), voz `em_alex`, fonética de español latinoamericano (`es-419`: la c y la z suenan como s).
Ajustes del dueño (22-23 nov 2026):
  * Velocidad: unas 170 palabras por minuto de habla (la muestra iba a unas 193). Se calibra sola; nunca se acelera para ganar tiempo.
  * Pausas: 0,4 s tras cada oración y 0,3 s tras cada coma (también `;` y `:`); un poco más (+0,2 s) antes de cada «Pero» y «Entonces».
  * Entonación: se sintetiza frase por frase, respetando ¿? y ¡!, y se unen los audios con esas pausas.
  * Pronunciación: se comprueba con una transcripción automática que los nombres propios y términos técnicos se entiendan.
  * No se clona ninguna voz.

Marcas del guion:  {evento}palabra   -> el evento ocurre cuando empieza esa palabra
                   *término*         -> término técnico (se muestra en amarillo y mayúsculas)
                   [[silencio 9.6]]  -> silencio de 9,6 s (por ejemplo, mientras corre una carrera animada)
"""
import difflib, json, os, re, subprocess, unicodedata
import numpy as np

SR = 24000
AJUSTES = {
    "voz": "em_alex", "lang": "es-419",
    "wpm": 170,                  # palabras por minuto de habla
    "pausa_oracion": 0.40, "pausa_coma": 0.30, "extra_pero": 0.20,
    "inicio": 0.35, "final": 0.50,
    # La velocidad de Kokoro se calibra por guion para que las PALABRAS HABLADAS por minuto (cuenta de la muestra: frase recortada sin
    # pausas largas) lleguen a `wpm`. Con el guion del Canal de Panamá sale 0,82. Un intento previo fallaba por contar «9,58» como una
    # palabra cuando la voz dice cinco: subía la velocidad a 1,28 y la voz salía atropellada. `velocidad_fija` fuerza un valor.
    "velocidad_fija": None,
    "velocidad_inicial": 0.85,
}
# Respelling solo para la voz (los subtítulos conservan la ortografía original)
PRONUNCIACION = {"Datazo": "Da-ta-zo"}   # con «Datazo» a secas, el transcriptor oía «The Atasso» o «da atazo»; con guiones lo entienden los dos modelos
TERMINOS = []                    # términos que la verificación debe encontrar en la transcripción


def _norm(s):
    """Forma de comparación: sin acentos ni signos, y con el seseo latinoamericano (c/z = s; b = v; h muda)."""
    s = unicodedata.normalize("NFD", s.lower()); s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9ñ]", "", s)
    return re.sub(r"c(?=[ei])", "s", s).replace("z", "s").replace("v", "b").replace("h", "")


_UN = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis",
       "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco", "veintiséis", "veintisiete",
       "veintiocho", "veintinueve"]
_DE = {3: "treinta", 4: "cuarenta", 5: "cincuenta", 6: "sesenta", 7: "setenta", 8: "ochenta", 9: "noventa"}
_CE = {1: "ciento", 2: "doscientos", 3: "trescientos", 4: "cuatrocientos", 5: "quinientos", 6: "seiscientos", 7: "setecientos", 8: "ochocientos", 9: "novecientos"}
UNIDADES = {"km/h": "kilómetros por hora", "km": "kilómetros", "m": "metros", "s": "segundos", "kg": "kilogramos", "t": "toneladas", "%": "por ciento",
            "°C": "grados Celsius", "m²": "metros cuadrados", "km²": "kilómetros cuadrados"}


def num2es(n):
    """Entero (0 a 999 999 999) -> palabras en español."""
    if n < 30: return _UN[n]
    if n < 100: d, u = divmod(n, 10); return _DE[d] + ("" if u == 0 else " y " + _UN[u])
    if n == 100: return "cien"
    if n < 1000: c, r = divmod(n, 100); return _CE[c] + ("" if r == 0 else " " + num2es(r))
    if n < 1_000_000: m, r = divmod(n, 1000); return ("mil" if m == 1 else num2es(m) + " mil") + ("" if r == 0 else " " + num2es(r))
    m, r = divmod(n, 1_000_000); return ("un millón" if m == 1 else num2es(m) + " millones") + ("" if r == 0 else " " + num2es(r))


def _num(n): return num2es(n)


def _sin_signos(w):
    """Quita los signos de los extremos (¿ ¡ . , ; : ? ! …) pero no los de dentro: «9,58» se queda como «9,58»."""
    return re.sub(r"^[¿¡(«\"]+|[.,;:?!…)»\"]+$", "", w)


def _hablado(core, previo_num):
    """Palabra mostrada (sin signos) -> lista de palabras habladas. `previo_num`: la palabra anterior era un número."""
    if "|" in core: return core.split("|", 1)[1].replace("_", " ").split()
    if re.fullmatch(r"\d{1,3}(\.\d{3})+|\d+", core): return num2es(int(core.replace(".", ""))).split()
    if re.fullmatch(r"\d+,\d+", core):
        e, d = core.split(",")
        return num2es(int(e)).split() + ["coma"] + (num2es(int(d)).split() if not d.startswith("0") else [x for ch in d for x in num2es(int(ch)).split()])
    if previo_num and core in UNIDADES: return UNIDADES[core].split()
    return [core]


def _analizar(fr):
    """Frase -> lista de palabras con (texto, puntuación final, eventos, término)."""
    palabras, pend, termino = [], [], False
    corte_pend = False
    for tok in re.findall(r"\{[a-z0-9_]+\}|\S+", fr):
        m = re.fullmatch(r"\{([a-z0-9_]+)\}", tok)
        if m:
            pend.append(m.group(1)); continue
        if tok == "//":
            if palabras: palabras[-1]["corte"] = True
            continue
        pend += re.findall(r"\{([a-z0-9_]+)\}", tok)
        tok = re.sub(r"\{[a-z0-9_]+\}", "", tok)
        es_term = tok.startswith("*") or termino
        if tok.startswith("*") and not tok.rstrip(".,;:?!").endswith("*"): termino = True
        if tok.rstrip(".,;:?!").endswith("*"): termino = False
        limpio = tok.replace("*", "")
        core = limpio.strip("¿¡(«»)\"").rstrip(".,;:?!…)»\"")
        previo = bool(palabras) and bool(re.search(r"\d", palabras[-1]["w"]))
        hab = _hablado(core, previo)
        mostrar = limpio.split("|")[0]
        palabras.append({"w": mostrar, "hab": hab, "corte": False, "pre": limpio[:len(limpio) - len(limpio.lstrip("¿¡(«"))], "post": re.search(r"[.,;:?!…)»\"]*$", limpio.split("|")[0]).group(0), "eventos": pend, "termino": es_term}); pend = []
    return palabras


def _frases(narracion):
    """Divide en oraciones (conservando ¿? ¡!) y en pausas explícitas [[silencio N]]."""
    out = []
    for linea in narracion.split("\n"):
        linea = linea.strip()
        if not linea: continue
        for trozo in re.split(r"(\[\[silencio [0-9.]+(?: [a-z0-9_]+)?\]\])", linea):
            trozo = trozo.strip()
            if not trozo: continue
            m = re.fullmatch(r"\[\[silencio ([0-9.]+)(?: ([a-z0-9_]+))?\]\]", trozo)
            if m: out.append(("silencio", (float(m.group(1)), m.group(2)))); continue
            for fr in re.split(r"(?<=[.?!])\s+(?=[¿¡A-ZÁÉÍÓÚ{*])", trozo):
                if fr.strip(): out.append(("frase", fr.strip()))
    return out


def _texto_voz(pal):
    partes = []
    for p in pal:
        h = list(p["hab"]); h[0] = p["pre"] + h[0]; h[-1] = h[-1] + p["post"]; partes.append(" ".join(h))
    t = " ".join(partes)
    for a, b in PRONUNCIACION.items(): t = re.sub(rf"\b{re.escape(a)}\b", b, t)
    return t


def _recortar(a, margen=0.03):
    nz = np.where(np.abs(a) > 0.01)[0]
    return a[max(0, nz[0] - int(margen * SR)): nz[-1] + int(margen * SR)] if len(nz) else a


def _remuestrear(a, sr):
    if sr == SR: return a.astype(np.float32)
    from scipy.signal import resample_poly
    from math import gcd
    g = gcd(int(sr), SR)
    return resample_poly(a, SR // g, int(sr) // g).astype(np.float32)


def _estirar(a, factor):
    """Cambia el ritmo sin cambiar el tono (factor > 1 = más rápido). Se usa solo para ajustes pequeños (±12 %)."""
    if abs(factor - 1.0) < 0.005: return a
    import librosa
    return librosa.effects.time_stretch(a, rate=factor).astype(np.float32)


def narrar(narracion, salida, modelos=None, ajustes=None, whisper="medium", verbose=True, crudos=None):
    """Genera `voz_cruda.wav`, `timeline.json` y `verificacion_voz.json` en `salida`. Devuelve el timeline.
    Con `crudos` ({posición de la frase: (audio, sr)}) usa audios ya generados por otro modelo (la etapa A de la voz) y solo ajusta el
    ritmo con un cambio de tempo; sin `crudos`, usa la ruta antigua de Kokoro (voz descartada el 24-nov-2026, se conserva por historia)."""
    import soundfile as sf   # solo hace falta para generar la voz (el render de vídeo solo lee el timeline)
    A = dict(AJUSTES); A.update(ajustes or {})
    os.makedirs(salida, exist_ok=True)
    elementos = _frases(narracion)
    frases = [(i, _analizar(txt)) for i, (tipo, txt) in enumerate(elementos) if tipo == "frase"]

    def sintetizar(pal, vel):
        from kokoro_onnx import Kokoro
        global _kokoro
        if "_kokoro" not in globals() or _kokoro is None:
            _kokoro = Kokoro(os.path.join(modelos, "kokoro-v1.0.onnx"), os.path.join(modelos, "voices-v1.0.bin"))
        a, sr = _kokoro.create(_texto_voz(pal), voice=A["voz"], speed=vel, lang=A["lang"])
        a = a.astype(np.float32)
        if sr != SR: a = np.interp(np.linspace(0, len(a) - 1, int(len(a) * SR / sr)), np.arange(len(a)), a).astype(np.float32)
        nz = np.where(np.abs(a) > 0.01)[0]
        return a[max(0, nz[0] - int(0.03 * SR)): nz[-1] + int(0.03 * SR)] if len(nz) else a

    def habla_activa(a, pausa_larga=0.40):
        """Duración de una frase para medir las palabras por minuto: la frase recortada, sin sus pausas largas (>= 0,4 s, por ejemplo
        la de «…»). Es la misma cuenta que se hizo con la muestra elegida (una pausa de 0,5 s descontada). Las pausas cortas de
        coma sí cuentan, porque forman parte del ritmo de habla."""
        fr = int(0.02 * SR); n = len(a) // fr
        if n == 0: return len(a) / SR
        e = np.abs(a[: n * fr]).reshape(n, fr).mean(axis=1) > 0.004
        quitar, run = 0.0, 0
        for v in list(e) + [True]:
            if not v: run += 1
            else:
                if run * 0.02 >= pausa_larga: quitar += run * 0.02
                run = 0
        return len(a) / SR - quitar

    # --- 1) calibrar la velocidad: palabras por minuto de habla = objetivo (la voz nunca se acelera para ganar tiempo)
    palabras_tot = sum(len(q["hab"]) for _, p in frases for q in p)   # palabras habladas: «9,58» se dice «nueve coma cincuenta y ocho»
    vel = A["velocidad_fija"] or A["velocidad_inicial"]
    if crudos is not None:
        # audios de otro modelo: se recortan, se pasan a 24 kHz y se ajusta el tempo hasta las palabras por minuto pedidas
        crudos = {pos: _recortar(_remuestrear(np.asarray(a, np.float32), sr)) for pos, (a, sr) in crudos.items()}
        wpm0 = palabras_tot / sum(habla_activa(c) for c in crudos.values()) * 60
        tempo = min(1.12, max(0.88, A["wpm"] / wpm0))
        crudos = {pos: _recortar(_estirar(c, tempo)) for pos, c in crudos.items()}
        wpm = palabras_tot / sum(habla_activa(c) for c in crudos.values()) * 60
        A["wpm_antes_del_tempo"] = round(wpm0, 1); A["tempo"] = round(tempo, 3)
        if verbose: print(f"ritmo del modelo {wpm0:.1f} palabras/min; tempo {tempo:.3f} -> {wpm:.1f}", flush=True)
    else:
      for ronda in range(1 if A["velocidad_fija"] else 5):
        crudos = {i: sintetizar(p, vel) for i, p in frases}
        wpm = palabras_tot / sum(habla_activa(c) for c in crudos.values()) * 60
        if verbose: print(f"calibración {ronda}: velocidad {vel:.3f} -> {wpm:.1f} palabras/min de habla", flush=True)
        if A["velocidad_fija"] or abs(wpm - A["wpm"]) <= 2.0: break
        vel *= (A["wpm"] / wpm) ** 1.3
    A["velocidad_kokoro"] = round(vel, 3); A["wpm_logrado"] = round(wpm, 1)
    # comprobación independiente de la puntuación: palabras por minuto de articulación (quitando todo hueco >= 0,12 s)
    def articulacion(a):
        fr = int(0.02 * SR); n = len(a) // fr
        e = np.abs(a[: n * fr]).reshape(n, fr).mean(axis=1) > 0.004
        quitar, run = 0.0, 0
        for v in list(e) + [True]:
            if not v: run += 1
            else:
                if run * 0.02 >= 0.12: quitar += run * 0.02
                run = 0
        return len(a) / SR - quitar
    A["wpm_articulacion"] = round(palabras_tot / sum(articulacion(c) for c in crudos.values()) * 60, 1)

    # --- 2) alinear palabra por palabra (faster-whisper solo mide tiempos)
    from faster_whisper import WhisperModel
    wm = WhisperModel(whisper, device="cpu", compute_type="int8")
    def alinear(a, pal):
        tmp = os.path.join(salida, "_seg.wav"); sf.write(tmp, a, SR)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-ar", "16000", "-ac", "1", os.path.join(salida, "_seg16.wav")], check=True)
        a16, _ = sf.read(os.path.join(salida, "_seg16.wav"), dtype="float32")
        segs, _ = wm.transcribe(a16, language="es", word_timestamps=True, vad_filter=False)
        # transcripción -> (token, inicio, fin); los números que escribe el transcriptor se expanden a palabras
        toks, trans = [], []
        for w in (w for s in segs for w in s.words):
            txt = w.word.strip(); trans.append(txt)
            if re.fullmatch(r"\d{1,3}(\.\d{3})*|\d+", txt.strip(" ,.")):
                pals = num2es(int(re.sub(r"\D", "", txt))).split(); L = sum(len(x) for x in pals); c = w.start
                for x in pals:
                    d = (w.end - w.start) * len(x) / L; toks.append((_norm(x), c, c + d)); c += d
            else:
                toks.append((_norm(txt), w.start, w.end))
        flat = [(_norm(x), i) for i, p in enumerate(pal) for x in p["hab"]]
        sm = difflib.SequenceMatcher(None, [f[0] for f in flat], [x[0] for x in toks], autojunk=False)
        tt = [None] * len(flat)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                for q in range(i2 - i1): tt[i1 + q] = (toks[j1 + q][1], toks[j1 + q][2])
        t = [None] * len(pal); ok = [False] * len(pal)
        for i in range(len(pal)):
            idxs = [q for q, f in enumerate(flat) if f[1] == i]
            known = [tt[q] for q in idxs if tt[q]]
            if known: t[i] = (known[0][0], known[-1][1]); ok[i] = len(known) == len(idxs)
        dur = len(a) / SR
        idx = [i for i, v in enumerate(t) if v]
        if not idx:
            L = np.array([max(1, len(p["w"])) for p in pal], float); c = np.concatenate([[0], np.cumsum(L)]) / L.sum() * dur
            t = [(c[i], c[i + 1]) for i in range(len(pal))]
        else:
            for i in range(len(pal)):
                if t[i]: continue
                a_ = max([j for j in idx if j < i], default=None); b_ = min([j for j in idx if j > i], default=None)
                ta = t[a_][1] if a_ is not None else 0.0; tb = t[b_][0] if b_ is not None else dur
                na = (a_ + 1) if a_ is not None else 0; nb = b_ if b_ is not None else len(pal)
                n = max(1, nb - na); q = i - na
                t[i] = (ta + (tb - ta) * q / n, ta + (tb - ta) * (q + 0.9) / n)
        return t, ok, " ".join(trans)

    # --- 3) montar: pausas de coma y de oración, extra antes de «Pero»/«Entonces»
    audio = [np.zeros(int(A["inicio"] * SR), np.float32)]
    cursor = A["inicio"]
    palabras_tl, eventos, informe = [], {}, {"frases": [], "terminos": {}, "pausas": {"comas": 0, "oraciones": 0, "extra_pero": 0}}
    eventos_pend = []
    n_el = len(elementos)
    for pos, (tipo, txt) in enumerate(elementos):
        if tipo == "silencio":
            seg, ev_s = txt
            if ev_s: eventos[ev_s] = round(cursor, 3)
            audio.append(np.zeros(int(seg * SR), np.float32)); cursor += seg
            continue
        pal = _analizar(txt)
        a = crudos[pos]
        t, ok, transcrito = alinear(a, pal)
        # cortes en las comas
        cortes = []
        for i, p in enumerate(pal[:-1]):
            if re.search(r"[,;:]$", p["w"]):
                hueco = t[i + 1][0] - t[i][1]
                extra = A["extra_pero"] if _norm(pal[i + 1]["w"]) in ("pero", "entonces") else 0.0
                ins = max(0.0, A["pausa_coma"] - max(0.0, hueco)) + extra
                corte = (t[i][1] + t[i + 1][0]) / 2 if hueco > 0 else t[i][1] + 0.01
                cortes.append((corte, ins)); informe["pausas"]["comas"] += 1
                if extra: informe["pausas"]["extra_pero"] += 1
        # construir el audio de la frase con las pausas insertadas y mapear los tiempos
        trozos, previo, acumulado = [], 0.0, 0.0
        cortes_mapa = []
        for corte, ins in sorted(cortes):
            ic = int(corte * SR)
            trozos.append(a[int(previo * SR):ic]); trozos.append(np.zeros(int(ins * SR), np.float32))
            acumulado += ins; cortes_mapa.append((corte, acumulado)); previo = corte
        trozos.append(a[int(previo * SR):])
        def mapear(x):
            add = 0.0
            for c, ac in cortes_mapa:
                if c <= x: add = ac
            return x + add
        for ev in eventos_pend: eventos[ev] = round(cursor + mapear(t[0][0]), 3)
        eventos_pend = []
        for p, (s0, s1), ok_ in zip(pal, t, ok):
            ini = cursor + mapear(s0); fin = cursor + mapear(min(s1, len(a) / SR))
            palabras_tl.append({"w": _sin_signos(p["w"]), "wp": p["w"], "ini": round(ini, 3), "fin": round(max(fin, ini + 0.12), 3), "termino": p["termino"], "corte": p["corte"], "final_oracion": bool(re.search(r"[.?!]$", p["w"]))})
            for ev in p["eventos"]: eventos[ev] = round(ini, 3)
            informe["terminos"].setdefault(_norm(p["w"]), []).append(bool(ok_))
        fr_audio = np.concatenate(trozos); audio.append(fr_audio); cursor += len(fr_audio) / SR
        informe["frases"].append({"texto": txt, "transcripcion": transcrito, "palabras_coinciden": f"{sum(ok)}/{len(ok)}"})
        # pausa tras la oración (+extra si la siguiente oración empieza con Pero / Entonces)
        sig = next((e for e in elementos[pos + 1:] if e[0] == "frase"), None)
        pausa = A["pausa_oracion"]
        if sig and _norm(_analizar(sig[1])[0]["w"]) in ("pero", "entonces"):
            pausa += A["extra_pero"]; informe["pausas"]["extra_pero"] += 1
        audio.append(np.zeros(int(pausa * SR), np.float32)); cursor += pausa; informe["pausas"]["oraciones"] += 1
    audio.append(np.zeros(int(A["final"] * SR), np.float32)); cursor += A["final"]
    x = np.concatenate(audio)
    sf.write(os.path.join(salida, "voz_cruda.wav"), x, SR)
    dur_total = round(len(x) / SR + 0.2, 2)
    tl = {"duracion": dur_total, "eventos": eventos, "palabras": palabras_tl, "voz": A.get("etiqueta_voz") or ("kokoro:" + A["voz"]), "ajustes": A}
    json.dump(tl, open(os.path.join(salida, "timeline.json"), "w"), ensure_ascii=False, indent=1)

    # --- 4) verificación de pronunciación: nombres propios y términos técnicos
    falla = {}
    for t_ in TERMINOS:
        r = informe["terminos"].get(_norm(t_), [])
        if r: falla[t_] = f"{sum(r)}/{len(r)} reconocidas"
    informe["terminos_clave"] = falla
    informe["resumen"] = {"duracion_s": dur_total, "palabras": len(palabras_tl), "ajustes": A}
    informe.pop("terminos", None)
    json.dump(informe, open(os.path.join(salida, "verificacion_voz.json"), "w"), ensure_ascii=False, indent=1)
    for f in ("_seg.wav", "_seg16.wav"):
        try: os.remove(os.path.join(salida, f))
        except OSError: pass
    if verbose:
        print(f"duración {dur_total} s; {len(palabras_tl)} palabras; {len(eventos)} eventos; velocidad Kokoro {A['velocidad_kokoro']}; {A['wpm_logrado']} palabras/min")
    return tl


def subtitulos_por_frases(tl, max_hueco=0.7):
    """Subtítulos de los formatos A y B: bloques de palabras (cortados donde el guion pone «//», o al final de cada oración),
    con su inicio y fin tomados de la voz. Devuelve [{ini, fin, texto, resalta}]."""
    bloques, cur = [], []
    for p in tl["palabras"]:
        cur.append(p)
        if p.get("corte") or p.get("final_oracion"):
            bloques.append(cur); cur = []
    if cur: bloques.append(cur)
    out = []
    for i, b in enumerate(bloques):
        ini = b[0]["ini"]; fin = b[-1]["fin"]
        sig = bloques[i + 1][0]["ini"] if i + 1 < len(bloques) else None
        if sig is not None and sig - fin < max_hueco: fin = sig
        else: fin += 0.2
        out.append({"ini": round(ini, 3), "fin": round(fin, 3), "texto": " ".join(w.get("wp", w["w"]) for w in b),
                    "resalta": [w["w"] for w in b if w["termino"]]})
    return out
