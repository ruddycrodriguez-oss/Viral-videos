# Datazo (@Datazo123go): datos curiosos en español, solo Shorts, sin cara

Canal de YouTube Shorts que ya existe. El trabajo en este repositorio es **producir videos para él**. El plan de lanzar un canal nuevo de Excel quedó **descartado** y `nicho.md` se conserva solo como archivo histórico (no usarlo para decidir nada de Datazo).

## El canal

- **Qué es:** «datos curiosos en menos de un minuto». Temas: ciencia, espacio, historia, animales y fútbol. Con el formato C, «Así se construye», se añaden explicaciones de ingeniería.
- **Formato:** solo Shorts, en español, sin mostrar la cara del dueño.
- **Estado (22-nov-2026):** 4 Shorts y 31 suscriptores. Una batalla tipo meme tuvo 140 vistas y un dato de fútbol 19. Son muestras diminutas: no sacar conclusiones de ellas.
- **Voz: obligatoria y de IA en todos los Shorts, de código abierto y generada aquí, sin servicios de pago** (ver la sección «Voz de IA»). **Ningún video se entrega sin voz.** Cambio de rumbo del 23-nov-2026: la voz Kokoro y el diorama Three.js quedaron **descartados** y **no se usa ElevenLabs** ni ningún otro servicio de voz de pago.
- **Temas que no quiere tratar:** ninguno declarado. Preguntar antes de proponer temas sensibles.

## Estilo visual de Datazo (formatos A y B; no cambiar sin avisar)

- Ilustración plana, fondo azul oscuro, letras amarillas y blancas.
- Logo: una D en un rombo amarillo. Paleta en `datazo/motor.py`: fondo `(9, 24, 48)`, amarillo `(255, 210, 31)`, blanco `(255, 255, 255)`, azul medio `(15, 38, 72)`.
- Tipografía: Inter (licencia OFL), instalada en el sistema. No se commitea la fuente.
- Todo el dibujo se hace **por código**. No se usan imágenes ni personajes de terceros.

## Reglas del canal (obligatorias, para todos los formatos)

1. **Verificar cada dato y cada explicación técnica en al menos 2 fuentes confiables independientes y anotarlas.** Organismos oficiales o instituciones (NASA, ESA, NOAA, Smithsonian, FIFA, World Athletics, Guinness, ACP, USGS, universidades, revistas científicas). Blogs, Wikipedia y sitios de curiosidades no cuentan. Dos páginas que copian la misma fuente cuentan como una. Si un dato solo llega a una fuente, o es una estimación o un cálculo propio, **se dice en el guion y en su documento**. Si una fuente no se pudo abrir (por ejemplo Britannica, que devuelve 403), no se cita como leída.
2. **Cada Short tiene un ángulo propio.** La política de contenido no auténtico de YouTube (renombrada el 15-jul-2025 y reformulada en julio de 2026 en tres categorías: genérico o repetitivo, insatisfactorio o desagradable, y personas de IA en temas sensibles) no permite el contenido repetitivo, hecho con plantillas o producido en masa, ni presentaciones de imágenes o texto sin narrativa. Sí permite series donde cada video tiene su enfoque y estructuras comunes como una misma intro y outro («same intro and outro, but the bulk of your content is different»). Cada Short cambia tema, cifras, ilustración **y su matiz propio** (el «Ojo» en los formatos A y B; el problema real y su solución en el formato C). La política se aplica al **canal completo**.
3. **Solo personajes y recursos propios o de licencia libre.** Nada de personajes de memes, dibujos o marcas de otros. Contendientes y objetos son animales, planetas, lugares u objetos reales dibujados por código, sin marcas ni logotipos reales.
4. **Revisar cada Short contra la política de «contenido para niños» (COPPA).** Resumen verificado (YouTube Help 9528076, 9527654, 9684541 y la guía de la FTC de nov-2019; no es asesoría legal):
   - YouTube decide por factores: tema, audiencia prevista (por ejemplo, según los metadatos), niños como actores o modelos, personajes, celebridades o juguetes que atraen a niños, lenguaje pensado para niños, actividades de juego, canciones, cuentos o poemas infantiles. La audiencia mixta cuenta como «para niños».
   - Un canal de datos curiosos con ilustración o animación **no es «para niños» automáticamente** («animated content that appeals to everyone» figura como audiencia general; la FTC dice que los colores vivos o los personajes animados no bastan). Pero YouTube **no tiene una regla específica** sobre animación para adultos, así que se decide Short por Short.
   - Riesgo propio del canal: la ilustración plana de animales o planetas, el lenguaje simple, los formatos de «batalla/VS» y el **estilo 3D low-poly del formato C** (parecido a un juego de bloques) se acercan a «personajes que atraen a niños». Mitigación: tono de audiencia general, sin mascotas, rimas, canciones, voces infantiles ni personajes con cara caricaturesca, y **no mencionar niños ni menores de 13 en título, etiquetas, descripción ni «Acerca de»**.
   - Configuración: Studio → Configuración → Canal → Configuración avanzada → Audiencia (sí / no / revisar cada video). El ajuste de cada video anula el del canal. La opción prudente es **«revisar cada video»**. Anotar por escrito el criterio de cada Short.
   - Si se marca «para niños» se pierden comentarios, campana de notificaciones, tarjetas y pantallas finales, anuncios personalizados, y a nivel de canal membresías y Posts; YouTube admite una posible caída de ingresos. Si YouTube detecta un error, puede anular la elección (apelable una vez por video). La responsabilidad de marcar bien es del creador; la FTC puede sancionar hasta US$53.088 por infracción (cifra vigente en 2026; es un tope).
5. **Especificaciones técnicas:** vertical **1080×1920**, H.264 yuv420p a 30 fps con `faststart`, subtítulos grandes, y la zona inferior (≈ los últimos 360 px) y la superior (≈ los primeros 130 px) libres de lo importante por la interfaz de Shorts. **Duración: formatos A y B, menos de 60 s; formato C, de 60 a 90 s.** YouTube admite Shorts verticales o cuadrados de hasta 3 minutos ([ayuda 15424877](https://support.google.com/youtube/answer/15424877?hl=en); la fecha de entrada en vigor difiere entre versiones de la página: oct-2024 o dic-2025).
6. **Sin música.** El dueño la añade al subir. El MP4 lleva la voz de IA y los **efectos de sonido propios** (ver «Efectos de sonido»); ninguna música.
7. **Cierre fijo en todos los videos del canal (decidido el 23-nov-2026):** «Ahora ya lo sabes. Esto fue un Datazo.» Sin intro ni logo grande: **el primer segundo es la imagen más impactante**. En los formatos A y B el cierre fijo va al final, después de la pregunta o el voto.
8. **Antes de producir un guion, verificar sus datos y avisar al dueño de lo que no se confirme** (qué dato, qué fuente falta y la redacción segura propuesta). No se produce con datos sin confirmar.

## Voz de IA (obligatoria; la crea Claude, de código abierto, sin servicios de pago)

- **Todos los Shorts** llevan narración con voz de IA en **español latino neutro**, de **narrador masculino**: enérgica, cálida y clara, «como un documental divertido». Si no se puede generar en el entorno, **detenerse y decir qué se necesita**.
- **Descartadas por el dueño (23-nov-2026):** Kokoro `em_alex` (la voz de los Shorts anteriores) y todo servicio de pago (ElevenLabs incluido). Otras descartadas antes por licencia, origen dudoso o no ser la elegida: Chatterbox, Piper, Coqui XTTS-v2, F5-TTS, Kani-TTS, OmniVoice (modelo CC-BY-NC).
- **Voz original, no clonada:** se diseña con modelos «voice design» (la voz sale de una descripción en texto). **No se clona a ninguna persona real ni la voz de otro video**, ni se presenta la voz como un experto humano. **Ancla de timbre (decidido por Claude, 25-nov-2026):** cada toma «diseñada» por separado suena como una persona distinta (similitud de hablante CAM++ ≈ 0,58 entre frases). Para que todas las frases suenen igual, se diseña la voz con la descripción, se elige **una toma propia del modelo (audio sintético) como ancla** y las demás frases se generan con el modo de referencia del modelo usando solo esa ancla (similitud ≈ 0,79 a 0,86). Nunca se usa audio de una persona real ni de otro video como referencia.
- **Licencia comercial obligatoria** (el canal se monetizará): solo modelos con licencia que permita uso comercial (Apache-2.0, MIT). Guardar copia de la tarjeta de licencia con fecha en `datazo/construye/licencias/` y anotar que son declaraciones del autor, no asesoría legal.
- **Modelos probados (pesos Apache-2.0 o MIT; ver `datazo/rascacielos/voz/` y `muestras/LEEME.md`):** Qwen3-TTS-12Hz-1.7B-VoiceDesign y -Base (Apache-2.0; pasa las medidas), VoxCPM2 (Apache-2.0; pasa, con ritmo algo alto) y Ming-3.0-tts-0.5B (MIT; **descartado por las medidas**: errores y «θ»). No probado: Zonos3-Mini (Apache-2.0). Descripción base del narrador en `generar_crudos.py` (`ESTILO_BASE`).
- **Voz elegida: PENDIENTE.** Claude entrega 3 muestras de 15 s con la escena 1 del guion y **espera la elección del dueño**; esa voz se registra aquí y se usa siempre igual en todos los Shorts.
- **Proceso (lo aplican `datazo/voz.py` y `datazo/voz_calidad.py`):**
  0. **Seseo por texto:** para la voz, la c ante e/i y la z se escriben «s» (`voz.texto_seseo`: «cien» → «sien»); los subtítulos conservan la ortografía. Así ningún modelo puede decir «θ».
  1. **Frase por frase** con pausas naturales (respetando ¿? y ¡!). Pausas: **0,4 s tras cada oración**, **0,3 s tras cada coma** (también `;` y `:`), **+0,2 s** antes de cada «Pero» y «Entonces». Se generan varias tomas por frase y se elige la mejor por las medidas.
  2. **Velocidad y expresividad** ajustadas con el estilo descrito y la velocidad del habla. Si el video pasa de su límite, **se recorta el guion; no se acelera la voz**.
  3. **Mejora del audio** (ffmpeg): filtro de graves, quitar ruido, ecualización cálida con presencia, de-esser, compresión, limitador y **normalización a −14 LUFS** en dos pasadas (pico real máximo −1 dBTP).
  4. **Descartar por medidas** (Claude no puede escuchar): una voz que falle cualquiera de estas se descarta.
- **Medidas obligatorias de aceptación (umbrales fijados por el dueño):**
  - **Transcripción sin errores** (Whisper `medium`; los números se comparan hablados): WER = 0.
  - **160 a 175 palabras por minuto** de habla (palabras habladas: «9,58» son «nueve cincuenta y ocho»; frase recortada y sin pausas largas).
  - **c y z suenan como «s» (seseo)**, comprobado con un reconocedor de fonemas (`facebook/wav2vec2-lv-60-espeak-cv-ft`): **ningún «θ»** y las «s» esperadas del fonetizador es-419 presentes.
  - **Entonación variada**, no plana: unos **12 semitonos** de rango de tono (percentiles 5 a 95 de F0 con pYIN; banda de aceptación 10 a 15). Criterio añadido por Claude (no del dueño): se registra la mediana de F0 (CREPE como referencia; pYIN da medianas más altas con voces sintéticas) y se prefiere un tono de narrador masculino (la mediana de F0 de un hombre adulto suele estar entre ≈100 y 180 Hz); si sale mucho más agudo, se baja en la descripción de la voz.
  - **−14 LUFS** integrados (tolerancia ±0,5), pico real ≤ −1 dBTP.
- **Naturalidad:** Claude no puede escuchar; la naturalidad y el acento los juzga el dueño. **Si ninguna voz llega a sonar natural, se dice claro en vez de entregar una voz mala.**
- **Pronunciación:** los nombres propios y términos técnicos se comprueban con la transcripción automática; si alguno falla, se corrige su escritura solo para la voz (`PRONUNCIACION` en `voz.py`) y los subtítulos conservan la ortografía original. Los números con género (p. ej. «660 toneladas» → «seiscientas sesenta») se fuerzan con `660|seiscientas_sesenta`.

- **Contenido alterado o sintético (YouTube, ayuda 14328491 «Disclosing use of GenAI content»):** YouTube pide divulgar el contenido de IA que *parece realista* (persona real, evento o lugar real alterado, escena realista que no ocurrió, música como foco). No pide divulgar lo claramente animado ni la IA usada para guiones o subtítulos. **Ningún texto oficial trata una voz TTS neutra sobre una animación.** Por eso, **al subir, marcar «Sí» en «AI use»** (YouTube Studio → Atributos): es la opción prudente, no una obligación demostrada. YouTube dice que divulgar no limita el alcance ni la elegibilidad para monetizar, y que sancionará a quien decida *sistemáticamente* no divulgar (etiqueta manual, retirada de contenido o suspensión del YPP). Si se marca «Sí», el audio de IA aparece como etiqueta en la descripción ampliada (en Shorts, la etiqueta superpuesta se reserva para contenido fotorrealista o con alteración significativa). Tras la primera subida, anotar qué etiqueta aparece.

## Efectos de sonido

- Efectos en cada momento clave (impacto, crujido, grieta, retumbar, sacudida, ascensor, «ding», etc.), **con licencia comercial**. Para evitar licencias de terceros, **se sintetizan por código** (numpy/scipy: whoosh, golpe, crujido, grieta, retumbo, campanilla, «pop»): son obra propia y no hay nada que atribuir. Si algún día se usa una biblioteca externa, guardar la licencia con fecha en `datazo/construye/licencias/`.
- Van mezclados bajo la voz (la voz manda), con el mismo −14 LUFS final. Ninguna música.

## Formatos fijos

### A. «DATAZO EN 40» y B. «DATAZO VS» (detalle y 10 guiones en `datazo/guiones.md`)

- **A:** gancho (0-3 s) → dato central (3-14 s) → por qué (14-27 s) → **Ojo** (27-36 s) → cierre con pregunta (36-40 s).
- **B:** pregunta VS (0-3 s) → contendientes con un dato real cada uno (3-11 s) → duelo animado a escala real (11-22 s) → veredicto con el dato que lo explica (22-33 s) → Ojo y voto (33-40 s). El resultado **siempre** se explica con un dato real citado.

### C. «Así se construye» (60 a 90 s)

Se toma de una cuenta de referencia **solo la fórmula**; temas, guiones, escenas, frases y cierre son 100 % propios. **No copiar guiones, escenas ni frases de otras cuentas. No hacer el tema del puente.** **Cambio de rumbo (23-nov-2026): el diorama Three.js y la voz Kokoro del primer video (Canal de Panamá) quedaron descartados.**

**Fórmula:**
1. **Gancho en el primer segundo:** una pregunta directa sobre cómo se construye algo, sobre **la imagen más impactante** (sin intro ni logo grande).
2. **Cadena de 5 a 6 pasos:** la solución más simple → aparece un problema real → se resuelve → se nombra la pieza técnica. **Cada problema se ve fallar en pantalla** (grietas, hundimiento, balanceo) con **sacudida de cámara**.
3. **Un momento cotidiano** que el espectador reconozca de su vida diaria.
4. **Cierre fijo de Datazo, igual en todos los videos:** «Ahora ya lo sabes. Esto fue un Datazo.» (plano final del resultado completo, p. ej. al atardecer).

**Estilo visual (nuevo):**
- **Imágenes generadas con IA en estilo 3D low-poly**, con **el mismo estilo y la misma ciudad en todas las escenas** (prefijo de estilo idéntico en todos los prompts y una «biblia de la ciudad» en texto; una imagen maestra de referencia si el modelo lo admite). Se animan por código con **zooms, paneos y sacudidas**.
- **Generación de imágenes:** primero una opción **gratuita con licencia comercial**. Si no hay ninguna que sirva, **decir cuánto cuesta cada video antes de gastar y pedir la clave con el formulario seguro del entorno (nunca en el chat)**. Opción recomendada por la investigación del 23-nov-2026 (por probar): Cloudflare Workers AI con FLUX.1 [schnell] (pesos Apache-2.0; plan gratuito de 10.000 «neuronas» al día; cuenta propia y token por formulario seguro; coste si se pasa del cupo ≈ US$0,02 por video de 30 imágenes, **cálculo propio**). Alternativa local sin servicio, FLUX.2 [klein] 4B (Apache-2.0) con stable-diffusion.cpp, pero tarda minutos por imagen en esta CPU. No usar modelos de licencia no comercial (p. ej. FLUX.2 klein 9B, SDXL-Turbo).
- Unas 10 a 15 imágenes clave por video; el resto de planos se derivan con recortes, zooms y paneos de ellas.
- **Cifras grandes en pantalla** cuando se mencionan; **el término técnico en amarillo y MAYÚSCULAS** al nombrarlo.
- **Subtítulos palabra por palabra**, al centro, blancos con borde negro, **sincronizados con la voz**.
- **Sin logo grande ni intro.** Marca de agua mínima y discreta si hace falta.
- Las escenas son esquemáticas (no están a escala): decirlo si hace falta.

**Ritmo (para que no aburra):**
- **Un cambio visual cada 2 a 3 segundos** (corte, zoom, paneo o cambio de pieza).
- Cada problema se ve fallar con sacudida de cámara; **efectos de sonido** en cada momento clave; **cifras grandes** al mencionarlas.

**Archivos:** `datazo/construye/temas.md` (10 temas, borrador sin verificar), `datazo/rascacielos/guion_rascacielos.json` (guion del rascacielos) y, como archivo histórico del formato descartado, `datazo/construye/` (Three.js, Kokoro, Canal de Panamá).

## Producción

### Formatos A y B (Pillow + ffmpeg)

- Motor: `datazo/motor.py`. Modelo de vídeo: `datazo/render_vs_guepardo.py` y su `datos_vs_guepardo.json`. El VS de guepardo y Bolt existente lleva la **voz Kokoro (descartada)**: hay que **rehacerlo con la voz nueva** cuando el dueño la elija. Marcas de la narración (las entiende `datazo/voz.py`): `{evento}palabra`, `//` (corte de subtítulo), `*resaltado*`, `9,58|nueve_cincuenta_y_ocho` (lo que se ve | lo que se dice) y `[[silencio 5.95 evento]]` (la carrera animada, en tiempo real).
- **Formato A:** todavía no tiene motor de animación propio (solo existen sus guiones); la voz, los tiempos y los subtítulos por frases (`voz.subtitulos_por_frases`) ya están listos para cuando se construya.
- Cada video lleva MP4, `.srt` y guía de tiempos.

### Formato C (imágenes IA low-poly + animación por código + voz de código abierto)

1. **Voz, etapa A (entorno del modelo):** `generar_crudos.py <qwen|voxcpm> <narracion.json> <salida> [--frases 0,1,2] [--tomas N]` genera por frase las tomas crudas (`crudos/NN_tomaK.wav`) y `frases.json`. Los entornos (venv con torch CPU, `qwen-tts` o `voxcpm`) no persisten entre sesiones.
2. **Voz, etapa B (entorno de medición: torch, transformers, librosa, faster-whisper, kokoro-onnx solo por su fonetizador):** `ensamblar_muestra.py <etapa_a> <etiqueta> <salida> [--frases N] [--toma K] [--wpm 167]` recorta, ajusta el tempo a las palabras por minuto objetivo, alinea palabras (faster-whisper), inserta las pausas, genera `timeline.json`, aplica `voz_calidad.mejorar_audio` (−14 LUFS) y `voz_calidad.medir` (WER, wpm, θ/s, rango de tono) en `medidas_<etiqueta>.json`.
3. **Imágenes** de la escena (ver «Estilo visual»), animadas por código con las marcas de tiempo de `timeline.json`; sonidos sintetizados; render a **1080×1920, 30 fps** y mezcla final con la voz a −14 LUFS.
4. **Revisar fotogramas** antes del render final y comprobar el MP4 (ver checklist).
5. **Entrega:** MP4 vertical 1080×1920 y un archivo de publicación (`*_publicar.txt`) con **título (≤ 100 caracteres), descripción con fuentes y 3 hashtags**, en la rama.

## Checklist antes de publicar un Short

1. ¿Cada cifra y explicación técnica tiene 2 fuentes anotadas? ¿Lo estimado o calculado está marcado? ¿Se avisó al dueño de lo que no se confirmó **antes** de producir?
2. ¿El matiz propio es distinto del de los últimos Shorts? ¿Sin elementos de terceros (personaje, marca, música, mapa)? ¿Las imágenes de IA tienen licencia comercial y la misma ciudad y estilo en todas las escenas?
3. ¿Hay algún factor de «contenido para niños»? Anotar el criterio. Título, etiquetas y descripción sin menciones a menores.
4. ¿Los récords y cifras que pueden cambiar siguen vigentes? **Ojo con el fútbol:** el Mundial de 2026 ya se jugó y los récords «actuales» pueden haber cambiado.
5. Voz: ¿es la elegida por el dueño, de código abierto y con licencia comercial registrada, y pasa las medidas (WER 0, 160 a 175 wpm, sin «θ», ≈12 st, −14 LUFS)? Al subir, **«AI use» = Sí**.
6. Ritmo: ¿un cambio visual cada 2 a 3 s, problemas que se ven fallar con sacudida, efectos de sonido, cifras grandes y primer segundo impactante sin intro ni logo grande? ¿Cierre fijo «Ahora ya lo sabes. Esto fue un Datazo.»?
7. Revisar el MP4 final: 1080×1920, duración correcta, subtítulos palabra por palabra legibles y sincronizados, voz presente, efectos de sonido, sin música.

## Cómo trabajar en este repositorio

- Citar la fuente de cada dato; marcar como «estimado» lo que no se pueda comprobar; no inventar cifras ni canales.
- No incluir datos personales del dueño ni el nombre de otros negocios suyos en búsquedas web ni en peticiones a servicios externos.
- No pedir claves ni contraseñas en el chat.
- Confirmar con el dueño antes de publicar, enviar o crear algo fuera de este repositorio.
- Ramas: trabajar en `claude/youtube-shorts-niche-strategy-e9z168`. No crear pull requests sin que el dueño lo pida.


## Pendientes

1. **Elegir la voz del narrador** entre las 3 muestras de 15 s (escena 1 del rascacielos) y aprobar o corregir los datos de la escena 2 antes de producir el video.
2. Decidir la generación de imágenes: probar 3 imágenes con la opción gratuita recomendada (requiere cuenta y clave por el formulario seguro) o, si no sirve, aprobar el coste por video.
3. El Short del Canal de Panamá (voz Kokoro + Three.js) quedó **descartado** por el cambio de rumbo: no subirlo salvo que el dueño diga lo contrario. Rehacer el VS de guepardo y Bolt con la voz nueva.
4. Escuchar los MP4 y las muestras: Claude no puede oír, solo comprueba lo medible.
5. Decidir el ajuste de audiencia del canal en YouTube Studio («revisar cada video» recomendado).
6. Declarar los temas que el dueño no quiere tratar.
7. Verificar, tema por tema, los datos de `temas.md` antes de escribir cada guion.
8. Construir el motor de animación del formato A.
9. Posible limpieza del historial de la rama: un commit automático subió por error unos 718 fotogramas temporales (≈100 MB). Ya no están en el árbol, pero siguen en la historia; limpiarlo exige un push forzado y necesita permiso del dueño.
