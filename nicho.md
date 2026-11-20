# Selección de nicho para canal de YouTube Shorts sin cara

Fecha del análisis: 20-nov-2026. Investigación hecha solo con búsqueda web: no había `YOUTUBE_API_KEY`, así que **no hay estadísticas de la API de YouTube**.

## 0. Lo que debes saber antes de leer

1. **Contexto que me diste:** voz de IA, comparar español e inglés, $0–30 USD/mes, 5–7 Shorts/semana. En "cómo ganar dinero" escribiste "videos que generen ingresos", así que no elegiste una vía concreta. Asumo anuncios + afiliados + producto propio.
2. **Lo que me falta** y que cambia el resultado: países objetivo, temas que dominas y temas que no quieres. Estos datos afectan sobre todo al desempate del Top 3 (sección 3).
3. **Los puntajes son juicio mío**, apoyado en los datos citados. Ningún dato público mide "competencia" o "viralidad potencial" por nicho. Todo puntaje de esas dos columnas es **estimado**.
4. **No encontré canales de ejemplo verificados.** Las búsquedas web devolvieron blogs de herramientas de IA, no canales con cifras comprobables. No te pongo enlaces inventados. En la sección 3 hay búsquedas para abrir y el script `buscar_canales.py` para hacerlo con datos reales cuando exista la clave.

---

## 1. Hallazgo principal: los anuncios de Shorts son casi inalcanzables

### Reglas del Programa de Socios de YouTube (YPP)

**Vigentes hoy** (fuente: [Google Help, ayuda del YPP](https://support.google.com/youtube/answer/72851?hl=en)):

| Nivel | Requisitos | Qué desbloquea |
|---|---|---|
| Completo | 1.000 suscriptores + 4.000 horas de visualización (365 días) **o** 10 M de vistas de Shorts (90 días) | Reparto de ingresos por anuncios |
| Ampliado (500 subs) | 500 suscriptores + 3 subidas públicas (90 días) + 3.000 horas de formato largo **o** 3 M de vistas de Shorts (90 días) | Funciones de fan funding (ver notas). Fuente: [Google Help](https://support.google.com/youtube/answer/13429240?hl=en), vía buscador; no lo abrí completo |

Las horas de visualización de Shorts **no cuentan** para las 4.000 horas. Solo cuentan las de videos largos públicos.

**Cambios del 1 de febrero de 2027** (fuente primaria: [YouTube Blog](https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/)):

- Los creadores con **10 M de vistas calificadas de Shorts en 90 días** serán elegibles para reparto de ingresos de anuncios y suscripciones **en Shorts**.
- Quien esté por debajo sigue en el YPP y gana con el formato largo. Los ingresos de Shorts se reanudan solos al volver a superar 10 M.
- Los **nuevos solicitantes** necesitarán **8.000 horas calificadas (365 días) o 20 M de vistas de Shorts (90 días)**. Los miembros actuales no se ven afectados.
- El blog anuncia además: bonos de YouTube Shopping, incentivos para acuerdos con marcas y bonos por iniciar o impulsar tendencias. Dice que dará más detalles.
- El plazo del 31 de enero de 2027 para aceptar los nuevos términos aparece en la página de ayuda del YPP. Solo afecta a quien ya está en el programa.

**Sin resolver, verifícalo en YouTube Studio antes de apostar por esto:**

- El blog **no menciona** el nivel de 500 suscriptores. No sé si se mantiene después del 1-feb-2027.
- Varias guías de terceros dicen que el umbral de suscriptores sigue en 1.000. No contradicen el blog, pero sus detalles son menos fiables.
- El blog **tampoco** dice cómo tratará a quien tenga una solicitud pendiente el 1-feb-2027.

### Política de "contenido no auténtico"

Fuentes: [Google Help](https://support.google.com/youtube/answer/1311392?hl=en), [Tubefilter](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/), [TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/). YouTube dice que es una aclaración, no una norma nueva. Estos son los criterios que usé para descartar nichos.

- **No elegible:**
  - contenido repetitivo o mínimamente variado entre videos;
  - presentaciones de imágenes o texto en desplazamiento sin narrativa ni valor educativo;
  - contenido de IA basado en plantillas genéricas que sugiere producción en masa;
  - clips de IA inconexos pegados para sorprender.
- **Elegible:**
  - intro y outro compartidos con contenido principal distinto;
  - cada video con su propio enfoque o concepto;
  - IA para editar guiones o generar fondos, si el resultado muestra tu visión creativa.
- **El alcance es el canal completo:** si hay videos que incumplen, puede perderse la monetización de todo el canal.
- **Voz de IA y stock:** la página de Google no los trata de forma específica. Es una zona gris (fuente: la misma página).
- **Contenido reutilizado** (política aparte): los comentarios y clips con narrativa añadida pueden ser elegibles. Las compilaciones sin narrativa y el contenido copiado sin cambios sustanciales no lo son.

**Nichos descartados por esta política:**

- frases motivacionales con plantilla;
- "Top 10" con presentaciones de imágenes;
- historias de Reddit con texto en desplazamiento;
- resúmenes de películas, series o deportes con clips ajenos;
- compilaciones;
- "cuentos" de IA genéricos;
- hechos curiosos aleatorios sin voz propia.

### Lo que esto implica (aritmética sobre los umbrales oficiales, **estimado** donde corresponde)

Con 5–7 Shorts/semana publicas unos **65–91 Shorts en 90 días**. El promedio de vistas por Short que necesitarías:

| Meta (90 días) | Vistas promedio por Short |
|---|---|
| 3 M (nivel ampliado, si sigue vigente) | ≈ 33.000–46.000 |
| 10 M (anuncios en Shorts, miembros) | ≈ 110.000–154.000 |
| 20 M (solicitante nuevo por la vía Shorts) | ≈ 220.000–308.000 |

El único dato de un canal de prueba que encontré dice lo siguiente. Es [BudgetPixel](https://budgetpixel.com/learn/how-to-start-a-faceless-youtube-channel), un proveedor de herramientas que probó su propio canal: 39 Shorts en 9 días dieron ~92.000 vistas y 117 suscriptores, es decir ~2.400 vistas por Short. A ese ritmo, 3 M de vistas exigirían ≈ 1.270 Shorts. Es un solo dato, autoinformado y de un vendedor. No lo trates como promedio del mercado, pero sirve para ver la distancia.

### Cuánto pagan los anuncios de Shorts (poco)

- La [investigación de AIR Media-Tech](https://air.io/air-data-findings/what-is-youtube-shorts-rpm-in-your-niche-in-2026) (274 canales, actualizada el 17-sep-2026) mide un RPM de Shorts de **$0,02 a $1,48** según el nicho. La cifra más alta es música.
- Otras medidas de AIR: Lifestyle ≈ $0,16–0,20; Artesanía ≈ $0,11; Infantil $0,02–0,05. Educación, Finanzas y Negocios **no tienen cifra de Shorts medida** en el texto.
- El RPM de Shorts es el **3–14 % del RPM de formato largo** en casi todos los nichos ([AIR](https://air.io/air-data-findings/youtube-shorts-rpm-vs-long-form-how-much-do-shorts-earn-in-2026)).
- Según [Influencer Marketing Hub](https://influencermarketinghub.com/youtube-shorts-rpm/), que cita entrevistas de Digiday, los creadores dicen que sus RPM de Shorts casi siempre quedan por debajo de $0,20.
- Las tablas de blogs ($0,15–0,45 para finanzas, por ejemplo) son estimaciones de terceros sin metodología pública.

**Conclusión práctica:** con RPM de $0,10–0,45, 10 M de vistas valdrían unos **$1.000–4.500 cada 90 días** (aritmética mía, **estimado**). Diseña el canal para ganar **fuera de los anuncios** desde el día 1.

---

## 2. Cómo comparan español e inglés (con lo poco que se pudo comprobar)

| Aspecto | Inglés (EE. UU./RU/CA) | Español (LatAm) |
|---|---|---|
| CPM/RPM | Más alto. Dato concreto: ninguno verificable para Shorts | Una guía en español estima CPM de $5–18 (finanzas); es una estimación de terceros sin comprobar |
| Competencia | Más alta (estimado; sin dato) | Más baja (estimado; sin dato) |
| Afiliados y productos | Más programas y mayor poder de compra (estimado) | Menos programas; el cobro y el IVA complican (estimado) |
| YouTube Shopping afiliado | Disponible en EE. UU. según la ayuda de Google | Depende del país; ver nota abajo |
| Advertencia | — | Un experto citado por un resumen de video afirma que en LatAm el formato largo rinde más que el corto. No lo pude contrastar |

Notas:

- **Shopping afiliado:** requiere estar en el YPP y tener ≥500 suscriptores ([YouTube Blog, 25-mar-2026](https://blog.youtube/creator-and-artist-stories/youtube-shopping-expansion-500-subscribers/)). Permite etiquetar productos en Shorts. La lista de países no la pude confirmar: la ayuda menciona EE. UU., India y Japón, y hay lanzamientos recientes en el Reino Unido, Australia y Medio Oriente. Falta confirmar México, Colombia, España y los demás.
- **Mi lectura:** como los anuncios no son el motor, el RPM importa menos y el poder de compra de la audiencia importa más. Eso inclina a **inglés** si el objetivo es afiliados o producto. El **español** conviene si tu dominio del idioma, tu mercado o tu producto son hispanos.

---

## 3. Los 20 nichos, los 8 finalistas y sus puntajes

### 20 nichos considerados

Finanzas personales (conceptos) · Herramientas de IA (tutoriales) · Excel/Sheets/productividad con software · Inglés para hispanohablantes · Carrera/entrevistas/CV · Ciencia y espacio · Psicología · Historia (microhistorias) · Salud y sueño · Cocina con stock · Bricolaje/hogar · Geografía y mapas · Animales y naturaleza · Trivia/quiz · Aprender programación · Frases motivacionales · Historias de terror · Crimen real · Cripto · Películas/series explicadas.

Los últimos 5 de la lista quedaron fuera por la política de contenido no auténtico o de derechos de autor, o por riesgo de políticas (cripto, salud como tema sensible, crimen real). Los demás cayeron frente a los finalistas en el desempate.

### Tabla comparativa (1–10; 10 siempre es lo más favorable)

Pesos: Demanda y potencial viral 20 % · Poca competencia 15 % · Ingresos fuera de anuncios 20 % · Facilidad con IA y sello propio 15 % · Bajo riesgo de políticas y derechos 20 % · Perenne 10 %.

| # | Nicho | Demanda | Competencia | Ingr. ext. | Facilidad IA | Riesgo | Perenne | **Total** |
|---|---|---|---|---|---|---|---|---|
| A | Excel/Sheets/productividad | 6 | 7 | 8 | 7 | 9 | 9 | **7,60** |
| B | Inglés para hispanohablantes | 8 | 5 | 8 | 8 | 7 | 10 | **7,55** |
| C | Carrera/entrevistas/CV | 6 | 6 | 7 | 8 | 9 | 9 | **7,40** |
| D | Finanzas personales (conceptos) | 8 | 3 | 8 | 7 | 5 | 9 | **6,60** |
| E | Herramientas de IA (tutoriales) | 9 | 3 | 8 | 8 | 6 | 3 | **6,55** |
| F | Ciencia y espacio | 7 | 4 | 3 | 7 | 8 | 10 | **6,25** |
| G | Psicología | 8 | 3 | 4 | 8 | 6 | 9 | **6,15** |
| H | Historia (microhistorias) | 7 | 4 | 3 | 7 | 7 | 10 | **6,05** |

**Todas las columnas son estimaciones mías.** Qué las respalda y qué no:

- **Respaldo parcial:**
  - La demanda de finanzas y de IA aparece en varias guías de nichos (p. ej. [Opus](https://www.opus.pro/blog/faceless-youtube-niches-2026), [Yoola](https://yoola.com/blog/best-faceless-youtube-niches-that-still-work-in-2026)). Son blogs comerciales.
  - AIR reporta RPM de formato largo de $14,97–18,23 en Educación y Ciencia, pero eso no es RPM de Shorts.
  - Las fuentes sobre finanzas aconsejan no dar asesoría regulada. De ahí el 5 en riesgo.
  - Una guía advierte que los tutoriales que reproducen contenido ya saturado pueden caer en la política de contenido no auténtico (vía [Tubefilter](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/)).
- **Sin datos:** la competencia real, el potencial viral y la facilidad de monetizar por afiliado en cada nicho. Los puntajes de afiliados reflejan que estos nichos (software, cursos, herramientas, apps) tienen programas conocidos de pago recurrente, pero **no verifiqué las condiciones de ningún programa concreto**.
- **Inglés para hispanohablantes (B):** bajé "Riesgo" a 7 porque las tarjetas de vocabulario con texto en pantalla se parecen a "texto en desplazamiento sin narrativa". Solo funciona con explicación propia y ejemplos.
- **Diferencia mínima:** los tres primeros están a 0,2 puntos. Con estas estimaciones, el orden entre A, B y C **no es estadísticamente distinguible**. Decide el desempate con lo que tú domines y con tu idioma objetivo.

### Top 3

#### 1. Excel / Google Sheets / productividad con software (7,60)

- **Pros:**
  - Es útil de forma concreta y el contenido es perenne.
  - Una grabación de pantalla propia da sello propio y encaja con "video original": el creador usa la IA para guion y voz, pero el contenido es una demostración real.
  - Riesgo bajo de derechos de autor.
  - Hay afiliados (software, cursos) y producto propio natural: plantillas de hoja de cálculo.
- **Contras:**
  - La demanda viral es moderada (6).
  - Hay que grabar la pantalla de cada Short, así que 5–7 por semana es más trabajo que con stock.
  - Hay muchos canales de Excel (estimado).
  - Si todos los Shorts siguen la misma plantilla, se corre el riesgo de "repetitivo". Hay que variar el caso de uso.
- **Estilo visual:** grabación de pantalla vertical con zoom a las celdas, teclas en pantalla y subtítulos grandes. Voz de IA con tono claro.
- **Canales de ejemplo:** no verificados. Abre estas búsquedas y filtra a mano: [excel tips shorts](https://www.youtube.com/results?search_query=excel+tips+shorts), [google sheets tips shorts](https://www.youtube.com/results?search_query=google+sheets+tips+shorts), [trucos excel shorts](https://www.youtube.com/results?search_query=trucos+excel+shorts). Busca canales con <50 mil suscriptores y varios Shorts con muchas más vistas que suscriptores.

#### 2. Inglés para hispanohablantes (7,55)

- **Pros:**
  - Es el nicho más perenne (10) y de mucha demanda en LatAm (estimado).
  - Natural para un producto propio: mini-curso, PDF, plantillas, sesiones.
  - Afiliados a apps y plataformas de clases.
  - Fácil de producir con IA (voz y texto).
- **Contras:**
  - Riesgo real de parecer texto con poca sustancia. Hay que explicar el porqué, no solo traducir.
  - Audiencia en español: anuncios y afiliados de menor valor (estimado).
  - Mucha competencia de academias grandes (estimado).
- **Estilo visual:** texto animado en pantalla + escenas cortas generadas con IA que ilustren la frase. Voz de IA bilingüe en dos voces.
- **Canales de ejemplo:** no verificados. Búsquedas: [inglés para hispanohablantes shorts](https://www.youtube.com/results?search_query=ingl%C3%A9s+para+hispanohablantes+shorts), [aprender inglés frases shorts](https://www.youtube.com/results?search_query=aprender+ingl%C3%A9s+frases+shorts).

#### 3. Carrera, entrevistas y CV (7,40)

- **Pros:**
  - Riesgo bajo, perenne.
  - Ingresos externos claros: revisión de CV, plantillas, herramientas de CV, cursos.
  - Fácil con IA (guiones de preguntas y respuestas).
- **Contras:**
  - Demanda viral media.
  - La IA tiende a dar consejos genéricos, que son justo lo que la política castiga. Hace falta ejemplo concreto.
  - Depende del país: el mercado laboral cambia.
- **Estilo visual:** texto en pantalla con ejemplos de CV (antes/después) y videos de stock sin rostro identificable.
- **Canales de ejemplo:** no verificados. Búsquedas: [interview tips shorts](https://www.youtube.com/results?search_query=interview+tips+shorts), [consejos entrevista trabajo shorts](https://www.youtube.com/results?search_query=consejos+entrevista+trabajo+shorts).

### Cómo conseguir los canales de ejemplo con datos reales

1. Crea una clave de la YouTube Data API v3:
   1. En Google Cloud Console crea un proyecto.
   2. Activa "YouTube Data API v3".
   3. Crea una clave en "Credenciales".
   4. Restríngela a esa API.
2. Guárdala en los ajustes del entorno como variable `YOUTUBE_API_KEY`: menú del entorno en la barra del título de la sesión → Edit. **No me la pegues en el chat.** Una sesión nueva la recibirá.
3. Ejecuta `python3 buscar_canales.py "excel tips" en`. El script lista canales de <50k suscriptores con la razón vistas/suscriptores de su mejor video reciente. Todavía no lo probé contra la API real. Tú debes confirmar que son Shorts reales y sin cara.

---

## 4. Recomendación final

**Excel / Google Sheets / productividad, en inglés**, con producto propio (plantillas) y afiliados de software como vía de ingresos. Esto sale de la tabla, pero con **condiciones** porque el empate con B y C es técnico:

- **Por qué A:** es el que mejor cumple lo que YouTube premia: demostración propia (grabación de pantalla), útil y variada. Encaja con tu presupuesto (herramientas gratuitas) y es perenne. La política de contenido no auténtico es el riesgo que más pesa en tu contexto, y aquí es el menor.
- **Por qué inglés:** los anuncios no serán tu motor. El poder de compra de la audiencia para afiliados y plantillas sí importa. Es una inferencia mía, sin datos de Shorts que la prueben.
- **Cuándo elegir otro:**
  - Si tu mercado, tu producto o tu voz son hispanos, haz A en español.
  - Si no quieres grabar pantalla cada vez, B es la alternativa. Exige disciplina para evitar el "texto en pantalla sin narrativa".
- **Esto no es una promesa de resultados.** No encontré ningún caso verificado de un canal de Shorts sin cara que alcance los umbrales con AI y cuota de $0–30.

---

## 5. Ruta de ingresos antes de cumplir los requisitos del YPP

**No esperes al YPP para ganar dinero.** Mientras tanto:

1. **Producto propio (la vía más controlable):**
   - plantillas de Excel/Sheets (presupuesto, seguimiento de hábitos, facturas), vendidas en una tienda externa;
   - un servicio puntual (limpiar o automatizar una hoja de cálculo).
2. **Afiliados externos:** recomienda software de pago recurrente con tu enlace. Revisa las condiciones de cada programa (hay restricciones sobre dónde poner el enlace).
3. **Dónde poner los enlaces:** en la descripción del canal (sección Acerca de), en el comentario fijado y en videos largos. Verifica en vivo si los enlaces de la descripción de un Short son clicables. No lo pude confirmar y YouTube ha restringido enlaces en Shorts antes.
4. **Captación de contactos:** una hoja de cálculo gratuita a cambio de un correo. Útil para vender después.
5. **YouTube Shopping:** exige estar en el YPP con ≥500 suscriptores. Entra solo cuando llegues al nivel ampliado (si sigue vigente después del 1-feb-2027).
6. **Patrocinios:** con <50k suscriptores serán pocos y poco rentables (estimado). YouTube anuncia incentivos para acuerdos de marca, sin detalles todavía.

### Cuánto tardarías en cumplir los requisitos (estimado)

No hay datos confiables de tiempo para canales nuevos. Lo único que se puede afirmar es la aritmética de la sección 1:

- Ritmo de 5–7 Shorts/semana → 65–91 Shorts por trimestre.
- Para el nivel ampliado por Shorts (3 M en 90 días): 33–46 mil vistas por Short. Para 10 M: 110–154 mil. Para 20 M: 220–308 mil.
- Para la **vía de formato largo** (8.000 horas para solicitantes nuevos desde el 1-feb-2027): 8.000 horas son 480.000 minutos. Con una retención media de 4 minutos por vista, hacen falta ≈ 120.000 vistas de videos largos (cálculo mío; la retención real puede variar mucho).
- **Mi expectativa, sin respaldo de datos:** meses a años. La mayoría de los canales no alcanza estos umbrales. Si en 90 días tu mediana de vistas por Short es de cientos, el YPP está lejos.
- **Recomendación:** además de los Shorts, publica 1–2 videos largos al mes sobre los mismos temas. Los Shorts atraen, y las horas de formato largo son la vía realista a los anuncios.

---

## 6. 20 ideas de Shorts para el nicho ganador (Excel / Google Sheets)

Los ganchos van en inglés (idioma recomendado) y el guion en español. Si eliges español, traduce el gancho. Cada Short debe mostrar una **demostración real en pantalla** con datos distintos, para no caer en la plantilla repetida.

| # | Gancho (primer segundo) | Guion en 3 líneas | Qué se ve |
|---|---|---|---|
| 1 | "Stop using VLOOKUP." | 1) VLOOKUP busca solo hacia la derecha. 2) XLOOKUP busca en cualquier dirección. 3) Escribe la fórmula y compara resultados. | Dos hojas lado a lado, fórmula resaltada |
| 2 | "Delete duplicates in 3 seconds." | 1) Selecciona la columna. 2) Datos → Quitar duplicados. 3) Muestra el antes y el después. | Lista de 500 filas que baja a 120 |
| 3 | "Split full names in one keystroke." | 1) Escribe el primer nombre a mano. 2) Presiona Ctrl+E. 3) Excel rellena el resto. | Columna de nombres completos que se divide |
| 4 | "Add a dropdown in 10 seconds." | 1) Selecciona las celdas. 2) Validación de datos → Lista. 3) Escribe las opciones. | Celda con flecha desplegable |
| 5 | "Make overdue dates turn red." | 1) Selecciona las fechas. 2) Formato condicional → regla con HOY(). 3) Cambia una fecha y mira el color. | Calendario de tareas con fechas en rojo |
| 6 | "Your header vanishes when you scroll?" | 1) Vista → Inmovilizar fila. 2) La cabecera queda fija. 3) Desplázate para probarlo. | Tabla larga con la fila fija arriba |
| 7 | "Press Ctrl+T on any messy range." | 1) Selecciona los datos. 2) Ctrl+T los convierte en tabla. 3) Filtros, formato y fórmulas se ajustan solos. | Rango plano que se transforma en tabla |
| 8 | "Build a pivot table in 10 seconds." | 1) Selecciona los datos. 2) Insertar → Tabla dinámica. 3) Arrastra campos y mira el total. | Ventas por mes y por vendedor |
| 9 | "Build a monthly budget with 3 formulas." | 1) SUMA para ingresos y gastos. 2) Una resta para el saldo. 3) Formato condicional para alertar. | Hoja de presupuesto que se rellena en pantalla |
| 10 | "One formula returns a sorted unique list." | 1) UNICOS lista sin repetir. 2) ORDENAR lo ordena. 3) Se actualiza al añadir filas. | Lista de clientes que crece sola |
| 11 | "Pull data from another Google Sheet." | 1) IMPORTRANGE con la URL. 2) Autoriza el acceso. 3) Los datos se sincronizan. | Dos pestañas del navegador |
| 12 | "Live data in a Google Sheet." | 1) Fórmula GOOGLEFINANCE con un símbolo. 2) Muestra precio y variación. 3) Aclara que es solo un ejemplo técnico, no una recomendación. | Hoja con cotización que cambia |
| 13 | "Combine 5 cells without typing 5 times." | 1) TEXTJOIN con separador. 2) Selecciona el rango. 3) Mira el resultado. | Columnas de ciudad, calle y número que se fusionan |
| 14 | "Make a habit tracker with checkboxes." | 1) Insertar → Casilla. 2) CONTAR.SI cuenta los marcados. 3) Un gráfico muestra la racha. | Cuadrícula de hábitos con casillas |
| 15 | "5 shortcuts that save an hour a week." | 1) Ctrl+Shift+L para filtros. 2) Ctrl+Flecha para saltar al final. 3) Alt+= para sumar. | Teclas grandes en pantalla con cada acción |
| 16 | "Why is your number not adding up?" | 1) Los números guardados como texto no suman. 2) Convierte con Texto en columnas. 3) La suma ahora es correcta. | Celdas con triángulo verde que se corrigen |
| 17 | "Hide ugly errors with one function." | 1) SI.ERROR envuelve la fórmula. 2) Define el texto alternativo. 3) La hoja queda limpia. | Columna con #N/A que pasa a "—" |
| 18 | "A project timeline in 60 seconds." | 1) Fechas de inicio y duración. 2) Formato condicional por fórmula. 3) Las barras forman el diagrama. | Cuadrícula que se rellena como Gantt |
| 19 | "3 formula mistakes that silently break your totals." | 1) Referencias sin $. 2) Rangos que no incluyen la fila nueva. 3) Texto en lugar de números. | Fórmula errónea y su corrección, una tras otra |
| 20 | "Let AI write your formula — then check it." | 1) Describe lo que quieres a una IA. 2) Copia la fórmula. 3) Pruébala con 3 casos antes de usarla. | Chat de IA y hoja de cálculo en pantalla dividida |

Ideas 2, 4, 6, 7 y 15 son muy básicas y las cubren muchos canales. Úsalas para entrar y aporta casos de uso reales en cada una.

---

## 7. Herramientas y costo estimado por Short

**Todos los precios son estimados y no los verifiqué. Comprueba las tarifas vigentes antes de contratar.**

| Etapa | Herramienta | Costo mensual estimado |
|---|---|---|
| Guion e ideas | Claude (esta sesión) | incluido en tu plan |
| Voz de IA | Plan gratuito de un generador de voz | $0–$22 |
| Grabación de pantalla | OBS Studio o grabador del sistema | $0 |
| Edición y subtítulos | CapCut o DaVinci Resolve (versiones gratuitas) | $0 |
| Miniatura/gráficos | Canva (plan gratuito) | $0 |

- **Costo por Short:** si usas solo herramientas gratuitas, **≈ $0**. Con una suscripción de voz de $22 y 22–30 Shorts al mes, serían **≈ $0,70–1,00 por Short** (aritmética mía). Entra en tus $0–30.
- **Tiempo por Short:** estimo 20–45 minutos entre guion, grabación, voz y edición (**estimado**).

---

## 8. Plan de validación de 30 días

### Qué hacer

- **22–30 Shorts** en 30 días (5–7 por semana). Un tema y una voz consistentes.
- **Variación:** no más de 2 Shorts seguidos con la misma estructura. Cambia el caso de uso, el ejemplo y el gancho.
- **1 video largo** (5–8 min) en la semana 3 o 4 como prueba de formato largo.
- **Marcado de contenido:** declara el contenido sintético (voz de IA) donde YouTube lo exija. Revisa la política vigente de divulgación.

### Métricas (en YouTube Studio; ubicación y nombres pueden variar)

| Métrica | Cómo leerla | Referencia |
|---|---|---|
| **Visto vs. deslizado** | % que ve el Short en lugar de pasar | YouTube no publica referencias. Guías de creadores: 70–79 % es aceptable y ≥80 % es fuerte. Compara contra tu **propia base** |
| **% promedio visto** | Qué parte del Short se ve | Sin referencia oficial. Guías de creadores sugieren ≥75 %. Más del 100 % indica repetición |
| **Suscriptores por 1.000 vistas** | Suscriptores ganados ÷ vistas × 1.000 | No encontré referencia fiable. Mi criterio propuesto: ≥1 es una señal buena (**estimado, criterio mío**) |
| Vistas por Short (mediana) | Más fiable que el promedio | Mi criterio propuesto, abajo |

### Cuándo cambiar

Estos criterios son **propuestos por mí, no datos de mercado**. El único punto de comparación que encontré es el canal de prueba de BudgetPixel (~2.400 vistas por Short, autoinformado).

- **Día 14 (≈10–14 Shorts):** revisa visto vs. deslizado de cada Short. Si el 70 % de los Shorts queda por debajo de tu base, **cambia ganchos y primeros 2 segundos** antes de tocar el nicho.
- **Día 30 (≥20 Shorts):** cambia de **subtema** si la mediana de vistas es <300 y ningún Short supera 3.000. Cambia de **nicho** si, tras un segundo ciclo de 20 Shorts con ajustes, siguen así y los suscriptores por 1.000 vistas están por debajo de 0,3.
- **Persiste** si hay al menos un Short que supere con claridad al resto y puedas repetir su patrón con otro caso de uso.
- **No cambies por una racha corta.** 20 Shorts es una muestra pequeña y la distribución de vistas es muy desigual.

---

## Fuentes

- YouTube Blog, cambios del YPP 2027: https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/
- Google Help, ayuda del YPP: https://support.google.com/youtube/answer/72851?hl=en
- Google Help, YPP ampliado: https://support.google.com/youtube/answer/13429240?hl=en
- Google Help, contenido no auténtico: https://support.google.com/youtube/answer/1311392?hl=en
- Tubefilter, aclaración de julio de 2026: https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/
- TechCrunch, 20-jul-2026: https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- YouTube Blog, Shopping con 500 suscriptores: https://blog.youtube/creator-and-artist-stories/youtube-shopping-expansion-500-subscribers/
- AIR Media-Tech, RPM de Shorts por nicho: https://air.io/air-data-findings/what-is-youtube-shorts-rpm-in-your-niche-in-2026
- AIR Media-Tech, Shorts vs. formato largo: https://air.io/air-data-findings/youtube-shorts-rpm-vs-long-form-how-much-do-shorts-earn-in-2026
- Influencer Marketing Hub, referencias de RPM: https://influencermarketinghub.com/youtube-shorts-rpm/
- BudgetPixel, canal de prueba (autoinformado): https://budgetpixel.com/learn/how-to-start-a-faceless-youtube-channel
- Guías de nichos (blogs comerciales): https://www.opus.pro/blog/faceless-youtube-niches-2026 · https://yoola.com/blog/best-faceless-youtube-niches-that-still-work-in-2026
- Análisis de terceros sobre los cambios de 2027: https://vidiq.com/blog/post/youtube-partner-program-changes-2027/ · https://www.searchenginejournal.com/youtube-updates-partner-program-terms-shorts-payout-rules/585331/
