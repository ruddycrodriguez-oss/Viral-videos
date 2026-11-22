# Muestras de voz para «Así se construye»

Elige **una** y la usaré en todos los Shorts del canal. La misma frase en las tres, con el volumen igualado (−16 LUFS) para que el volumen no influya:

> «¿Cómo se construye un canal que sube barcos por encima de una montaña? Empieza con una idea muy simple… y termina con un problema enorme.»

| Muestra | Archivo | Motor y voz | Duración |
|---|---|---|---|
| **1** | `voces/muestra_1_kokoro_dora.m4a` | Kokoro-82M, `ef_dora` (femenina) | 8,3 s |
| **2** | `voces/muestra_2_kokoro_alex.m4a` | Kokoro-82M, `em_alex` (masculina) | 8,3 s |
| **3** | `voces/muestra_3_chatterbox.m4a` | Chatterbox multilingüe, voz por defecto (sin clonar a nadie) | 6,4 s |

## Lo que sí comprobé y lo que no

- **No puedo escuchar audio.** No sé cuál suena más natural, ni si el acento te parece latino neutro, ni si «tiene energía». Eso lo decides tú de oído.
- **Claridad (medida, no opinión):** pasé las tres por un transcriptor automático (Whisper `small`) y devolvió la frase completa y correcta en las tres (100 % de coincidencia).
- **Ritmo:** la muestra 3 dice la frase en 6,4 s (unas 4 palabras por segundo); las 1 y 2, en 8,3 s (unas 3). La 3 es más rápida. En el Short se puede ajustar.
- **Acento:** Kokoro está configurado con fonética de español latinoamericano (`es-419`), pero el autor **no declara el acento** de sus voces. Chatterbox tampoco lo declara para su voz por defecto.

## Licencias (declaración de cada autor; no es asesoría legal)

| Motor | Licencia | Lo que implica para un canal monetizado | Reservas |
|---|---|---|---|
| Kokoro-82M | **Apache-2.0** (pesos) | Permite uso comercial; no exige atribución por el audio generado | La tarjeta dice que se entrenó con audio permisivo o sin derechos de autor, **pero admite audio sintético de TTS cerrados de grandes proveedores**. No documenta de dónde sale cada voz. Es una declaración del autor, sin contraste independiente. Guardé copia de la tarjeta y de `VOICES.md` con fecha (`licencias/`) |
| Chatterbox multilingüe | **MIT** | Permite uso comercial | Añade a **todo** el audio una marca de agua imperceptible (Perth) y pide «no usar el modelo para hacer cosas malas». No leí sus datos de entrenamiento. Genera mucho más lento en este entorno (sin GPU) |

**Descartadas por licencia o por falta de origen claro** (hallazgo del 22-nov-2026): Piper `es_MX-claude` (voz base no documentada), Piper `es_MX-ald` (Unlicense, pero el propio Piper duda de que quien subió los datos tuviera los derechos), Piper `es_AR-daniela` (derivada de una voz con licencia no comercial), Coqui XTTS-v2 (licencia no comercial), F5-TTS (CC-BY-NC) y Kani-TTS (licencia contradictoria). Las voces de España de Piper con licencia limpia (`davefx`, `carlfm`, `sharvard`) tienen acento peninsular, no latino neutro.

## Si ninguna te convence

Hay una vía de pago con mejor calidad: una API de voz con plan comercial (por ejemplo, ElevenLabs de pago; su plan gratuito es **solo no comercial**). Necesitaría una clave y te la pediría con el formulario seguro, nunca en el chat. No la he usado ni la necesito para producir con las tres muestras.

## Qué pasa cuando elijas

1. Genero la narración completa con esa voz (Kokoro tarda unos 2 minutos; Chatterbox, bastante más).
2. Alineo cada palabra con su momento exacto en el audio, y la animación y los subtítulos se calculan a partir de esos tiempos.
3. Renderizo el Short (1080×1920, con voz y sin música) y lo dejo en `datazo/construye/salida/`.
