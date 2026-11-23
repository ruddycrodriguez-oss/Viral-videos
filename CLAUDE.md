# Datazo (@Datazo123go): datos curiosos en español, solo Shorts, sin cara

Canal de YouTube Shorts que ya existe. El trabajo en este repositorio es **producir videos para él**. El plan de lanzar un canal nuevo de Excel quedó **descartado** y `nicho.md` se conserva solo como archivo histórico (no usarlo para decidir nada de Datazo).

## El canal

- **Qué es:** «datos curiosos en menos de un minuto». Temas: ciencia, espacio, historia, animales y fútbol. Con el formato C, «Así se construye», se añaden explicaciones de ingeniería.
- **Formato:** solo Shorts, en español, sin mostrar la cara del dueño.
- **Estado (22-nov-2026):** 4 Shorts y 31 suscriptores. Una batalla tipo meme tuvo 140 vistas y un dato de fútbol 19. Son muestras diminutas: no sacar conclusiones de ellas.
- **Voz: obligatoria y de IA en todos los Shorts** (ver la sección «Voz de IA»). **Ningún video se entrega sin voz.**
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
   - Riesgo propio del canal: la ilustración plana de animales o planetas, el lenguaje simple, los formatos de «batalla/VS» y el **diorama 3D low-poly del formato C** (parecido a un juego de bloques) se acercan a «personajes que atraen a niños». Mitigación: tono de audiencia general, sin mascotas, rimas, canciones, voces infantiles ni personajes con cara caricaturesca, y **no mencionar niños ni menores de 13 en título, etiquetas, descripción ni «Acerca de»**.
   - Configuración: Studio → Configuración → Canal → Configuración avanzada → Audiencia (sí / no / revisar cada video). El ajuste de cada video anula el del canal. La opción prudente es **«revisar cada video»**. Anotar por escrito el criterio de cada Short.
   - Si se marca «para niños» se pierden comentarios, campana de notificaciones, tarjetas y pantallas finales, anuncios personalizados, y a nivel de canal membresías y Posts; YouTube admite una posible caída de ingresos. Si YouTube detecta un error, puede anular la elección (apelable una vez por video). La responsabilidad de marcar bien es del creador; la FTC puede sancionar hasta US$53.088 por infracción (cifra vigente en 2026; es un tope).
5. **Especificaciones técnicas:** vertical **1080×1920**, H.264 yuv420p a 30 fps con `faststart`, subtítulos grandes, y la zona inferior (≈ los últimos 360 px) y la superior (≈ los primeros 130 px) libres de lo importante por la interfaz de Shorts. **Duración: formatos A y B, menos de 60 s; formato C, de 60 a 90 s.** YouTube admite Shorts verticales o cuadrados de hasta 3 minutos ([ayuda 15424877](https://support.google.com/youtube/answer/15424877?hl=en); la fecha de entrada en vigor difiere entre versiones de la página: oct-2024 o dic-2025).
6. **Sin música.** El dueño la añade al subir. El MP4 lleva la voz de IA (pista de audio) y ninguna música ni efectos.

## Voz de IA (obligatoria)

- **Todos los Shorts** llevan narración con voz de IA en **español latino neutro**, natural y con energía. Si no se puede generar en el entorno, **detenerse y decir qué se necesita**.
- **Licencia comercial obligatoria** (el canal se monetizará). Hay que guardar copia de la tarjeta de licencia con fecha en `datazo/construye/licencias/` y anotar que son declaraciones del autor, no asesoría legal.
- **Voz elegida (23-nov-2026): la muestra 2, Kokoro-82M `em_alex`, siempre la misma en todos los Shorts.** Fonética `es-419`: la **c y la z suenan como «s»**, igual que en la muestra 2. Licencia: pesos Apache-2.0 (declaración del autor; procedencia de cada voz no documentada y algo de entrenamiento con audio sintético de TTS cerrados; copia de la tarjeta en `datazo/construye/licencias/`). **No se clona la voz de ningún video ni persona.** Descartadas: Chatterbox (MIT, marca de agua Perth), Kokoro `ef_dora`, Piper `es_MX-claude`, `es_MX-ald`, `es_AR-daniela`, Coqui XTTS-v2, F5-TTS y Kani-TTS (por licencia, origen dudoso o no ser la elegida).
- **Ajustes de la voz (los aplica `datazo/voz.py`; no cambiarlos sin avisar):**
  - **Velocidad:** unas **170 palabras por minuto** de habla (la muestra iba a unas 193), contando las **palabras habladas** (los números se dicen con varias: «9,58» es «nueve cincuenta y ocho») sobre la frase recortada y sin sus pausas largas (≥ 0,4 s), que es la cuenta que se hizo con la muestra. `voz.py` calibra la velocidad de Kokoro por guion: **0,82 en el Canal de Panamá (170,6) y 0,93 en el VS de guepardo y Bolt (170,5)**. Un primer intento falló por contar «9,58» como una palabra: subía la velocidad a 1,28 y la voz salía atropellada. **Si el video pasa de su límite, se recorta el guion; no se acelera la voz.**
  - **Pausas:** **0,4 s después de cada oración** y **0,3 s después de cada coma** (también tras `;` y `:`); **+0,2 s** antes de cada «Pero» y de cada «Entonces».
  - **Entonación:** se genera **frase por frase**, respetando ¿? y ¡!, y se unen los audios con esas pausas para que no suene plana. Las pausas de coma se insertan en el audio de la frase ya generada, por la alineación de palabras, para no romper su entonación.
  - **Pronunciación:** tras generar, una transcripción automática comprueba que los **nombres propios y términos técnicos** se entiendan (`verificacion_voz.json`). Si alguno falla, se corrige su escritura solo para la voz (tabla `PRONUNCIACION` de `voz.py`); los subtítulos conservan la ortografía original.
- Con API de pago como respaldo (por ejemplo ElevenLabs de pago; su plan gratuito es solo no comercial): **la clave se pide con el formulario seguro del entorno, nunca en el chat.**
- No imitar la voz de una persona real ni presentar la voz como un experto humano.
- **Claude no puede escuchar audio:** la naturalidad y el acento los juzga el dueño. Lo medible (claridad con transcripción automática, duración) sí se comprueba.
- **Contenido alterado o sintético (YouTube, ayuda 14328491 «Disclosing use of GenAI content»):** YouTube pide divulgar el contenido de IA que *parece realista* (persona real, evento o lugar real alterado, escena realista que no ocurrió, música como foco). No pide divulgar lo claramente animado ni la IA usada para guiones o subtítulos. **Ningún texto oficial trata una voz TTS neutra sobre una animación.** Por eso, **al subir, marcar «Sí» en «AI use»** (YouTube Studio → Atributos): es la opción prudente, no una obligación demostrada. YouTube dice que divulgar no limita el alcance ni la elegibilidad para monetizar, y que sancionará a quien decida *sistemáticamente* no divulgar (etiqueta manual, retirada de contenido o suspensión del YPP). Si se marca «Sí», el audio de IA aparece como etiqueta en la descripción ampliada (en Shorts, la etiqueta superpuesta se reserva para contenido fotorrealista o con alteración significativa). Tras la primera subida, anotar qué etiqueta aparece.

## Formatos fijos

### A. «DATAZO EN 40» y B. «DATAZO VS» (detalle y 10 guiones en `datazo/guiones.md`)

- **A:** gancho (0-3 s) → dato central (3-14 s) → por qué (14-27 s) → **Ojo** (27-36 s) → cierre con pregunta (36-40 s).
- **B:** pregunta VS (0-3 s) → contendientes con un dato real cada uno (3-11 s) → duelo animado a escala real (11-22 s) → veredicto con el dato que lo explica (22-33 s) → Ojo y voto (33-40 s). El resultado **siempre** se explica con un dato real citado.

### C. «Así se construye» (60 a 90 s)

Se toma de una cuenta de referencia **solo la fórmula**; temas, guiones, escenas, frases y cierre son 100 % propios. **No copiar guiones, escenas ni frases de otras cuentas. No hacer el tema del puente.**

**Fórmula:**
1. **Gancho en el primer segundo:** una pregunta directa sobre cómo se construye algo.
2. **Cadena de 5 a 6 pasos:** la solución más simple → aparece un problema real → se resuelve → se nombra la pieza técnica.
3. **Un momento cotidiano** que el espectador reconozca de su vida diaria.
4. **Cierre propio de Datazo, igual en todos los videos:** «Esto fue Datazo. ¿Qué construimos mañana?»

**Estilo:**
- Diorama 3D low-poly en corte transversal (capas de tierra, agua, árboles, nubes), con cámara en diagonal que se mueve despacio.
- Cada paso agrega o cambia una pieza. **Flechas rojas** para las fuerzas; **partículas** para agua o erosión.
- **Subtítulos palabra por palabra** al centro, blancos con borde negro; el **término técnico en amarillo y MAYÚSCULAS** al nombrarlo.
- Logo de Datazo pequeño en una esquina.
- Voz de IA (ver arriba), con la animación y los subtítulos **sincronizados palabra por palabra** con la voz.
- Los dioramas son esquemáticos (no están a escala): decirlo si hace falta.

**Archivos:** `datazo/construye/temas.md` (10 temas, borrador sin verificar), `datazo/construye/guion_canal_panama.md` (primer guion) y `datazo/construye/muestras_voz.md`.

## Producción

### Formatos A y B (Pillow + ffmpeg)

- Motor: `datazo/motor.py`. Modelo de vídeo: `datazo/render_vs_guepardo.py` y su `datos_vs_guepardo.json`. **Con voz de IA (obligatoria):** primero `MODELOS=<carpeta> python3 datazo/narrar.py datazo/narracion_vs_guepardo.json datazo/salida/voz_vs_guepardo` (genera `voz.wav`, `timeline.json` y `verificacion_voz.json`) y después `python3 -I datazo/render_vs_guepardo.py datazo/salida/<nombre>.mp4 --voz datazo/salida/voz_vs_guepardo`: los tiempos de escenas, la salida de la carrera y los subtítulos salen de la voz, y el MP4 lleva la voz normalizada a −16 LUFS, sin música. Con `--prueba 3.0 12.5` guarda fotogramas PNG. Marcas de la narración: `{evento}palabra`, `//` (corte de subtítulo), `*resaltado*`, `9,58|nueve_cincuenta_y_ocho` (lo que se ve | lo que se dice) y `[[silencio 5.95 evento]]` (la carrera animada, en tiempo real). Para un guion A o B nuevo: escribir su `narracion_*.json` con esas marcas y su render.
- **Formato A:** todavía no tiene motor de animación propio (solo existen sus guiones); la voz, los tiempos y los subtítulos por frases (`voz.subtitulos_por_frases`) ya están listos para cuando se construya.
- Cada video lleva MP4, `.srt` y guía de tiempos.

### Formato C (Three.js en Chromium sin pantalla + voz local)

1. **Preparar el entorno** (no persiste entre sesiones): `cd datazo/construye && npm install`; `python3 -m venv v && v/bin/pip install kokoro-onnx soundfile faster-whisper` (y, para Chatterbox, `torch==2.6.0 torchaudio==2.6.0` desde el índice CPU de PyTorch y `chatterbox-tts`); modelos de Kokoro (`kokoro-v1.0.onnx` y `voices-v1.0.bin`) de las publicaciones del proyecto `kokoro-onnx` y carpeta `MODELOS`. Playwright y Chromium ya están instalados.
2. **Voz y tiempos:** `MODELOS=<carpeta> v/bin/python generar_voz.py guion_canal_panama.json salida/<nombre>` (atajo de `datazo/narrar.py`; voz `em_alex`) genera `voz_cruda.wav` y `timeline.json` (palabras con su inicio y fin, eventos y duración). La alineación usa faster-whisper (MIT) solo para medir tiempos. Copiar `voz_cruda.wav` como `voz.wav`.
3. **Render:** `node render.js salida/<nombre> salida/<nombre>.mp4 3` captura cada fotograma con WebGL por software (≈0,4 s por fotograma) y los une con la voz (volumen normalizado a −16 LUFS).
4. **Revisar fotogramas** con `node fotograma.js <carpeta> t1 t2 …` antes del render final; la escena lee `timeline.json` por parámetro (`?tl=`).
- Las marcas del guion `{evento}` disparan las animaciones en el instante exacto en que se dice la palabra siguiente; `*término*` marca el término técnico.

## Checklist antes de publicar un Short

1. ¿Cada cifra y explicación técnica tiene 2 fuentes anotadas? ¿Lo estimado o calculado está marcado?
2. ¿El matiz propio es distinto del de los últimos Shorts? ¿Sin elementos de terceros (personaje, marca, música, mapa)?
3. ¿Hay algún factor de «contenido para niños»? Anotar el criterio. Título, etiquetas y descripción sin menciones a menores.
4. ¿Los récords y cifras que pueden cambiar siguen vigentes? **Ojo con el fútbol:** el Mundial de 2026 ya se jugó y los récords «actuales» pueden haber cambiado.
5. Voz: ¿es la elegida, con licencia comercial registrada? Al subir, **«AI use» = Sí**.
6. Revisar el MP4 final: 1080×1920, duración correcta, subtítulos legibles y sincronizados, voz presente, sin música.

## Cómo trabajar en este repositorio

- Citar la fuente de cada dato; marcar como «estimado» lo que no se pueda comprobar; no inventar cifras ni canales.
- No incluir datos personales del dueño ni el nombre de otros negocios suyos en búsquedas web ni en peticiones a servicios externos.
- No pedir claves ni contraseñas en el chat.
- Confirmar con el dueño antes de publicar, enviar o crear algo fuera de este repositorio.
- Ramas: trabajar en `claude/youtube-shorts-niche-strategy-e9z168`. No crear pull requests sin que el dueño lo pida.

## Pendientes

1. Subir a YouTube el Short del Canal de Panamá con `datazo/construye/salida/canal_de_panama_publicar.txt` (título, descripción con fuentes y 3 hashtags) y **«AI use» = Sí**; tras subirlo, anotar qué etiqueta aparece en YouTube.
2. Escuchar el MP4 de Panamá y el VS de guepardo y Bolt: Claude no puede oír, solo comprobó la claridad con una transcripción automática (en el VS, «Usain» y «Sarah» salieron menos claros que el resto).
3. Decidir el ajuste de audiencia del canal en YouTube Studio («revisar cada video» recomendado).
4. Declarar los temas que el dueño no quiere tratar.
5. Verificar, tema por tema, los datos de `temas.md` antes de escribir cada guion.
6. Construir el motor de animación del formato A (la voz ya está lista).
7. Posible limpieza del historial de la rama: un commit automático subió por error unos 718 fotogramas temporales (≈100 MB). Ya no están en el árbol, pero siguen en la historia; limpiarlo exige un push forzado y necesita permiso del dueño.
