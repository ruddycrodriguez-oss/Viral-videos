# Datazo (@Datazo123go): datos curiosos en menos de un minuto

Canal de YouTube Shorts que ya existe. El trabajo en este repositorio es **producir videos para él**. El plan de lanzar un canal nuevo de Excel quedó **descartado** y `nicho.md` se conserva solo como archivo histórico (no usarlo para decidir nada de Datazo).

## El canal

- **Qué es:** datos curiosos en menos de un minuto. Temas: ciencia, espacio, historia, animales y fútbol.
- **Formato:** solo Shorts, en español, sin mostrar la cara del dueño.
- **Estado (22-nov-2026):** 4 Shorts y 31 suscriptores. Una batalla tipo meme tuvo 140 vistas y un dato de fútbol 19. Son muestras diminutas: no sacar conclusiones de ellas.
- **Voz:** **sin decidir** (el dueño dejó `[la mía / voz de IA / solo texto en pantalla]` sin elegir). Mientras tanto, cada video se entrega **sin audio**, con subtítulos grandes y una guía de tiempos para que el dueño grabe su voz encima. Preguntar antes de asumir una voz.
- **Temas que no quiere tratar:** ninguno declarado. Preguntar antes de proponer temas sensibles.

## Estilo visual (no cambiar sin avisar)

- Ilustración plana, fondo azul oscuro, letras amarillas y blancas.
- Logo: una D en un rombo amarillo. Paleta en `datazo/motor.py`: fondo `(9, 24, 48)`, amarillo `(255, 210, 31)`, blanco `(255, 255, 255)`, azul medio `(15, 38, 72)`.
- Tipografía: Inter (licencia OFL), que está instalada en el sistema. No se commitea la fuente.
- Todo el dibujo se hace **por código** (`datazo/motor.py`): guepardo, velocista, logo, subtítulos. No se usan imágenes ni personajes de terceros.

## Reglas del canal (obligatorias)

1. **Verificar cada dato en al menos 2 fuentes confiables independientes y anotarlas.** Organismos oficiales o instituciones (NASA, ESA, NOAA, Smithsonian, FIFA, World Athletics, Guinness, universidades, revistas científicas). Blogs, Wikipedia y sitios de curiosidades no cuentan. Dos páginas que copian la misma fuente cuentan como una. Si un dato solo llega a una fuente, o es una estimación o un cálculo propio, **se dice en el guion y en `guiones.md`**.
2. **Cada Short tiene un ángulo propio.** La política de contenido no auténtico de YouTube (aclarada en julio de 2026) no permite el contenido repetitivo, hecho con plantillas o producido en masa, ni presentaciones de imágenes o texto sin narrativa. Sí permite series donde cada video tiene su enfoque y estructuras comunes como una intro y una outro. Cada Short cambia tema, cifras, ilustración **y el bloque «Ojo»** (un matiz con fuentes). Si el «Ojo» de dos Shorts seguidos se parece, cambiar uno. La política se aplica al **canal completo**: unos videos con plantilla pueden quitar la monetización de todo.
3. **Solo personajes y recursos propios o de licencia libre.** Nada de personajes de memes, dibujos o marcas de otros. Los contendientes de un VS son animales, planetas, lugares u objetos reales dibujados por código. Mapas y siluetas, propios.
4. **Revisar cada Short contra la política de «contenido para niños» (COPPA).** Resumen verificado (YouTube Help 9528076, 9527654, 9684541 y la guía de la FTC de nov-2019; no es asesoría legal):
   - YouTube decide por factores: tema, audiencia prevista (por ejemplo, según los metadatos), niños como actores o modelos, personajes, celebridades o juguetes que atraen a niños, lenguaje pensado para niños, actividades de juego, canciones, cuentos o poemas infantiles. La audiencia mixta cuenta como «para niños».
   - Un canal de datos curiosos con ilustración plana **no es «para niños» automáticamente** (YouTube lista «animated content that appeals to everyone» como audiencia general; la FTC dice que los colores vivos o los personajes animados no bastan). Pero YouTube **no tiene una regla específica** sobre animación para adultos, así que se decide Short por Short.
   - Riesgo propio del canal: ilustración de animales y planetas, lenguaje simple y formatos tipo «batalla/VS» se acercan a «personajes que atraen a niños». Mitigación: tono de audiencia general, sin mascotas, sin rimas ni canciones, sin voces infantiles, sin personajes con cara caricaturesca, y **no mencionar niños ni menores de 13 en título, etiquetas, descripción ni «Acerca de»**.
   - Configuración: Studio → Configuración → Canal → Configuración avanzada → Audiencia (sí / no / revisar cada video). El ajuste de cada video anula el del canal. La opción prudente es **«revisar cada video»**. Anotar por escrito el criterio de cada Short (campo «Audiencia» de `guiones.md`).
   - Si se marca «para niños» se pierden comentarios, campana de notificaciones, tarjetas y pantallas finales, anuncios personalizados, y a nivel de canal membresías y Posts; YouTube admite una posible caída de ingresos. Si YouTube detecta un error, puede anular la elección (apelable una vez por video). La responsabilidad de marcar bien es del creador; la FTC puede sancionar hasta US$53.088 por infracción (cifra vigente en 2026; es un tope).
5. **Especificaciones técnicas:** vertical **1080×1920**, **menos de 60 s**, subtítulos grandes (≈80 px), H.264 yuv420p a 30 fps con `faststart`. Dejar libre la zona inferior (≈ los últimos 360 px) y la superior (≈ los primeros 130 px) por la interfaz de Shorts.
6. **Sin música.** El dueño la añade al subir. El MP4 va sin pista de audio.

## Formatos fijos (detalle y 10 guiones en `datazo/guiones.md`)

- **A. «DATAZO EN 40»:** gancho (0-3 s) → dato central (3-14 s) → por qué (14-27 s) → **Ojo** (27-36 s) → cierre con pregunta (36-40 s).
- **B. «DATAZO VS»:** pregunta VS (0-3 s) → contendientes con un dato real cada uno (3-11 s) → duelo animado a escala real (11-22 s) → veredicto con el dato que lo explica (22-33 s) → Ojo y voto (33-40 s). El resultado **siempre** se explica con un dato real citado.

## Producción (cómo se hace un video)

- Motor: `datazo/motor.py` (Pillow + numpy; ffmpeg codifica). Videos: `datazo/render_vs_guepardo.py` (el modelo) y su `datos_vs_guepardo.json` (datos, tiempos y subtítulos). Para un video nuevo: copiar ambos, cambiar los datos y el dibujo.
- Comando: `python3 -I datazo/render_vs_guepardo.py datazo/salida/<nombre>.mp4`. Tarda ≈ 2,5 minutos con 4 núcleos. Con `--prueba 3.0 12.5` guarda fotogramas PNG para revisar antes de renderizar. Siempre mirar fotogramas antes del render final.
- Cada video lleva: MP4, `.srt` y una **guía de tiempos** (`datazo/guia_grabacion_*.md`) para que el dueño grabe su voz encima.
- Los videos terminados quedan en `datazo/salida/` en la rama de trabajo para descargarlos desde el iPad.
- Límites del entorno: **no se puede grabar voz ni generar música**; no hay navegador para animaciones web (el dibujo es con Pillow).

## Estado de los guiones y del primer video

- Hecho: `guiones.md` (5 de formato A y 5 de formato B) y el video **Guepardo vs Usain Bolt** (`datazo/salida/datazo_vs_guepardo_bolt.mp4`, 42 s).
- Verificación **parcial** (decirlo en el guion si se usan): A5 (la anécdota de los dos balones del Mundial de 1930 tiene una sola fuente institucional y una crítica), B1 (5,95 s de la guepardo proviene de una sola medición; los parciales de Bolt tienen una sola fuente secundaria) y B4 (la cifra del Imperio romano solo se leyó en Turchin 2006).

## Checklist antes de publicar un Short

1. ¿Cada cifra tiene 2 fuentes anotadas en `guiones.md`? ¿Lo estimado o calculado está marcado?
2. ¿El «Ojo» es distinto del de los últimos Shorts?
3. ¿Hay algún elemento de terceros (personaje, marca, música, mapa)? Si sí, quitarlo.
4. ¿Algún factor de «contenido para niños»? Anotar el criterio. Título, etiquetas y descripción sin menciones a menores.
5. ¿Los récords y cifras que pueden cambiar siguen vigentes? **Ojo con el fútbol:** el Mundial de 2026 ya se jugó (jun-jul 2026) y los récords «actuales» pueden haber cambiado. Evitar «récord actual» sin comprobarlo.
6. Revisar el MP4 final: 1080×1920, <60 s, subtítulos legibles, sin audio.

## Cómo trabajar en este repositorio

- Citar la fuente de cada dato; marcar como «estimado» lo que no se pueda comprobar; no inventar cifras ni canales. Si el verificador no pudo abrir una fuente (por ejemplo Britannica, que devuelve 403), no citarla como leída.
- No incluir datos personales del dueño ni el nombre de otros negocios suyos en búsquedas web ni en peticiones a servicios externos.
- No pedir claves ni contraseñas en el chat.
- Confirmar con el dueño antes de publicar, enviar o crear algo fuera de este repositorio.
- Ramas: trabajar en `claude/youtube-shorts-niche-strategy-e9z168`. No crear pull requests sin que el dueño lo pida.

## Pendientes

1. Decidir la voz (propia, de IA o solo texto en pantalla).
2. Declarar los temas que el dueño no quiere tratar.
3. Elegir el siguiente video de `guiones.md` para producir.
4. Decidir en YouTube Studio el ajuste de audiencia del canal («revisar cada video» recomendado) y confirmarlo con el criterio de cada Short.
