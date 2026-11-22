> **ARCHIVO HISTÓRICO (22-nov-2026).** Este análisis se hizo para lanzar un canal nuevo de Excel para ventas y negocios. Ese plan quedó **descartado**: el dueño ya tiene un canal, Datazo (@Datazo123go), y solo quiere producir videos para él. No se usa para decidir nada del canal actual. Las reglas vigentes están en `CLAUDE.md`. Se conserva por si sirve de referencia (datos de Panamá, reglas del Programa de Socios y de enlaces en Shorts, cobros desde Panamá), que **pueden haber cambiado**.

# Selección de nicho para canal de YouTube Shorts sin cara

Fecha del análisis: 20-nov-2026 (decisión aprobada el 22-nov-2026, ver sección 4). Investigación hecha solo con búsqueda web: no había `YOUTUBE_API_KEY`, así que **no hay estadísticas de la API de YouTube**.

## 0. Lo que debes saber antes de leer

1. **Contexto que me diste:** vives en Panamá; dominas ventas y desarrollo de negocios, reportes de ventas y KPIs en Excel, marketing digital, y comunicación y oratoria; $0–30 USD/mes, 5–7 Shorts/semana; tienes una tienda de perfumes (Nova Parfum). En "cómo ganar dinero" escribiste "videos que generen ingresos", así que no elegiste una vía concreta. Asumo anuncios + afiliados + producto propio.
2. **Respuestas del 22-nov-2026:** idioma **español**, voz **propia**, Nova Parfum vende en **Panamá** y perfumes queda descartado como canal principal. Los temas que no quieres tratar siguen sin declarar. Las secciones anteriores se escribieron antes de estas respuestas, así que donde hablan de voz de IA o dejan el idioma abierto, manda `CLAUDE.md`.
3. **Los puntajes son juicio mío**, apoyado en los datos citados. Ningún dato público mide "competencia" o "viralidad potencial" por nicho. Todo puntaje de esas dos columnas es **estimado**.
4. **Sigo sin canales de ejemplo que cumplan todos los criterios** (Shorts + sin cara + menos de 50 mil suscriptores + crecimiento rápido). La sección 3 bis lista los candidatos parciales que sí pude comprobar, con sus límites.
5. **Los datos reales de la API de YouTube siguen pendientes.** El entorno "Videos Virales" no tiene ninguna variable ni secreto guardado (comprobado el 22-nov-2026) y se rechazó el formulario para guardar la clave, así que `buscar_canales.py` no se ejecutó. **Ningún puntaje de este archivo viene de la API**: son juicio mío con investigación web verificada. Cómo resolverlo: sección 3 bis, "Pendiente: la API".

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
| YouTube Shopping afiliado | **No disponible para ti**: exige que el creador esté basado en uno de 18 países y Panamá no figura (ver sección 3 bis). El idioma del contenido no cambia esto | Ídem |
| Advertencia | — | Un experto citado por un resumen de video afirma que en LatAm el formato largo rinde más que el corto. No lo pude contrastar |

**Datos medidos de RPM y CPM por país** (fuente: [AIR Media-Tech](https://air.io/en/air-data-findings/youtube-monetization-statistics-2026), estudios de 2026; un verificador independiente comprobó las cifras contra la página):

| Mercado | RPM de Shorts | CPM de formato largo |
|---|---|---|
| EE. UU. | $0,328 | $14,67 |
| Reino Unido y Canadá | ≈ $0,165 | sin dato en mi extracto |
| España | sin dato | $2,81 |
| México | $0,040 | $0,91 |
| Colombia | sin dato | $0,62 |

No hallé RPM de Shorts desglosado por idioma, ni para España, Colombia, Argentina, Chile o Panamá. Estas cifras confirman que el inglés paga varias veces más por vista de Shorts. **Pero** los anuncios de Shorts quedan lejos por los umbrales de la sección 1, así que esa ventaja solo pesaría a largo plazo.

Notas:

- **Audiencia hispana:** Cervantes cuenta 635,7 M de hablantes potenciales de español, 65,5 M de ellos en EE. UU. En EE. UU., el 85 % de los adultos hispanos usa YouTube (Pew). El alcance publicitario de YouTube (DataReportal, no son usuarios únicos) suma ≈ 188 M entre México, España, Argentina y Colombia a finales de 2025, frente a 254 M en EE. UU. con la misma base de fecha.
- **Poder adquisitivo:** el PIB per cápita en paridad de poder adquisitivo de EE. UU. es unas 3,3–3,5 veces el de México (fuente primaria no abierta; cifra de la investigación).
- **Qué falta:** no encontré datos de compra de plantillas o afiliados por mercado ni de conversión por idioma. Para tu caso (ingresos por plantillas y servicios), ese es el dato que decidiría y no existe.
- **Mi lectura:** el inglés gana si el criterio es el RPM. El español gana si el criterio es tu experiencia y tu voz propia. Con los anuncios fuera de alcance al inicio, no hay base de datos para decretar un ganador. Es decisión tuya (sección 4).

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

## 3 bis. Actualización del 20-nov-2026: Panamá, dos nichos nuevos y datos verificados

Esta sección salió de ocho investigaciones web, cada una revisada por un verificador independiente que intentó refutarla. Donde el verificador corrigió algo, uso la corrección. Cada verificador abrió las páginas oficiales de Google/YouTube por su cuenta.

### Qué cambia por vivir en Panamá

| Tema | Resultado | Confianza |
|---|---|---|
| **Programa de afiliados de YouTube Shopping** | **No eres elegible hoy.** La página oficial exige que el canal esté *basado* en uno de estos 18 países: Argentina, Brasil, Alemania, India, Indonesia, Japón, Corea, Malasia, México, Países Bajos, Filipinas, Polonia, Singapur, Taiwán, Tailandia, Reino Unido, EE. UU. y Vietnam. Panamá no está, ni en inglés ni en español. Apuntar a audiencias de otros países **no** da elegibilidad. Ver [la página oficial](https://support.google.com/youtube/answer/13376398) | Verificado (dos lecturas) |
| Cambios futuros | YouTube dijo el [23-sep-2026](https://blog.youtube/intl/es-419/news-and-events/made-on-youtube-26-juntamos-a-marcas-y-creadores/) que ampliaría el programa a 35 países antes de fin de año, **sin publicar la lista**. La página de elegibilidad parece ir rezagada respecto a los anuncios, así que revisa YouTube Studio → Ingresos cada mes | Verificado el anuncio; el resultado es incierto |
| Etiquetado de Amazon en Shorts | Disponible solo en 11 países (Australia, Brasil, Egipto, Francia, Alemania, India, Arabia Saudita, España, Reino Unido, EE. UU. y EAU). Panamá no está ([ayuda](https://support.google.com/youtube/answer/17105501)) | Verificado |
| **Programa de Socios (anuncios) y fan funding** | **Sí disponible en Panamá**, incluido el nivel ampliado de 500 suscriptores (membresías, Super Chat/Stickers, Super Thanks) ([lista oficial](https://support.google.com/youtube/answer/13429240?hl=en)) | Verificado |
| Nivel de 500 suscriptores después del 1-feb-2027 | Sigue vigente: 500 subs + 3 subidas públicas en 90 días + 3.000 horas de formato largo **o** 3 M de vistas de Shorts en 90 días. El blog oficial dice que los umbrales de fan funding y Shopping "permanecen sin cambios". La cifra de 500 la respaldan la página de ayuda del YPP ampliado y los anuncios de Shopping, no el blog del YPP | Verificado, con la salvedad indicada |
| Solicitudes pendientes el 1-feb-2027 | **Ninguna fuente oficial lo aclara.** Terceros se contradicen. No lo des por hecho | No resuelto |
| Canal "activo" desde el 1-feb-2027 | Para seguir en el YPP: 1.000 horas, **o** 1 M de vistas de Shorts en 90 días, **o** subir 2 videos largos o 5 Shorts cada 90 días. Tu ritmo de 5–7 por semana lo cumple ([ayuda](https://support.google.com/youtube/answer/12843009?hl=en)) | Verificado |
| **Cobro de AdSense desde Panamá** | Cheque, transferencia bancaria (wire) o PayPal Hyperwallet. EFT figura como "No". Western Union ya no se ofrece. Umbral de pago: USD 100 | Verificado |
| **Impuestos de EE. UU.** | Todo creador monetizado envía información fiscal (W-8BEN si no eres de EE. UU.) antes del 10 de diciembre de cada año. Sin ella, Google puede retener hasta 24 % de los ingresos mundiales. Con ella, la retención es 0–30 % **solo sobre lo ganado con espectadores de EE. UU.** Panamá no figura en la lista de tratados del IRS, así que **probablemente aplique 30 %** sobre esa parte. Eso es **inferencia**: Google no publica la tasa por país. Consúltalo con un contador. No investigué el tratamiento fiscal en Panamá | Verificado el marco; inferencia en la tasa |

### Cómo llevar clientes y cobrar desde Panamá

**Enlaces (reglas oficiales vigentes, verificadas en 12 páginas de ayuda):**

- Los enlaces en la descripción y en los comentarios de un Short **no son clicables**.
- **Sí son clicables:** los enlaces de perfil del canal (hasta 14), los de acuerdos de marca, "Related Video" en Shorts (apunta solo a contenido propio y exige acceso a funciones avanzadas) y los del programa de afiliados de Shopping (que no tienes). También las menciones y hashtags de Shorts.
- No pude confirmar oficialmente enlaces superpuestos en el banner, ni un mínimo de suscriptores para los enlaces de perfil. La página oficial tampoco exige uno.
- Las políticas permiten contenido de afiliados, pero advierten que publicar afiliados en exceso en cuentas dedicadas puede considerarse spam, y prohíben el contenido creado *únicamente* para sacar tráfico de YouTube.
- **Consecuencia práctica:** todo el embudo pasa por **el enlace de perfil**. Cada Short debe decir "enlace en mi perfil" y esa página debe ser clara.

**Dónde vender plantillas desde Panamá** (la investigación leyó las páginas oficiales; lo que no pudo abrir va marcado):

| Opción | Estado para residentes de Panamá | Nota |
|---|---|---|
| **Gumroad** | Utilizable: pago a cuenta bancaria en USD | Un verificador corrigió un detalle: PayPal solo es la alternativa en países **sin** depósito bancario. Panamá sí tiene depósito, así que no cuentes con PayPal en Gumroad |
| **Payhip** | Utilizable con **PayPal Business** | Panamá no está en la lista corta de PayPal personal; hace falta cuenta Business |
| **PayPal en Panamá** | Recibir y retirar | Comisión de **5,40 % + USD 0,30** por venta comercial y **1 % (mínimo USD 15)** por retirar a banco local. Los límites de retiro no se pudieron confirmar |
| Stripe propio | **No disponible** | Verificado |
| Etsy | **No abre tiendas en Panamá** | Verificado en dos páginas oficiales |
| Lemon Squeezy | La investigación reporta que **cerró registros nuevos el 16-nov-2026** y dejará de procesar pagos el 31-mar-2027. Panamá figuraba en su lista de pagos por banco | **Compruébalo tú**; el verificador no contradijo el cierre, pero tampoco lo reabrió |
| Hotmart | No pude confirmarlo | Su centro de ayuda es dinámico y solo devolvió títulos |

**Afiliados externos desde Panamá:**

- **No aceptan afiliados nuevos:** Shopify Collabs y Notion. Canva reemplazó su programa por "Canvassador", que según resúmenes de búsqueda está cerrado a solicitudes (**secundario**; Canva dio 403).
- **Amazon Associates:** ninguna página oficial que se pudo leer dice si se aprueba a residentes de Panamá. **Sin confirmar.**
- **Skillshare, Domestika, Udemy y Microsoft** (vía Impact, PayPal o transferencia): sus páginas oficiales no excluyen a Panamá, pero ninguna publica lista de países. Udemy dio 403 y Microsoft 503, así que son lecturas de resúmenes. **Sin confirmar:** pruébalo solicitando el alta.
- Mi conclusión: **no construyas el plan sobre afiliados externos de software hasta confirmar la aceptación de tu cuenta.** Tu mejor activo es el producto propio (plantillas y servicios).

### Evaluación de los dos nichos nuevos (misma tabla y mismos pesos)

| # | Nicho | Demanda | Competencia | Ingr. ext. | Facilidad IA | Riesgo | Perenne | **Total** |
|---|---|---|---|---|---|---|---|---|
| I | **Excel para ventas y negocios** (versión enfocada de A) | 5 | 7 | 8 | 8 | 8 | 9 | **7,35** |
| J | **Perfumes de diseñador y árabes** (hacia Nova Parfum) | 8 | 3 | 8 | 6 | 4 | 7 | **6,05** |

**Por qué estos puntajes** (todos son estimaciones mías; la fuente respalda solo lo indicado):

- **I, Excel para ventas:**
  - *Demanda 5:* menor que la del Excel genérico, porque la audiencia es más estrecha. No obtuve volumen de búsqueda.
  - *Competencia 7:* los canales grandes de Excel son de formato largo ([vidIQ](https://vidiq.com/youtube-stats/channel/@leilagharani/), 20-nov-2026: Kevin Stratvert 4,5 M, Leila Gharani 3,1 M). Un canal grande como Leila Gharani tiene una mediana de unas 78 mil vistas por Short. No encontré competidores pequeños de "Excel para ventas" en Shorts con cifras.
  - *Ingresos 8:* encaja con plantillas de KPIs y servicios de reportes. **No pude verificar precios** de plantillas en Etsy ni Gumroad (listados con 403 o sin precio visible).
  - *Facilidad 8:* tu experiencia da sello propio, que es lo que YouTube pide. La voz de IA no se menciona como causa de rechazo en la política oficial.
  - *Riesgo 8:* hay un riesgo documentado por los **términos de Microsoft sobre capturas de pantalla** (revisa su página de permisos antes de publicar) y el riesgo de plantilla repetida.
- **J, Perfumes:**
  - *Demanda 8 (secundario):* Euromonitor (14-sep-2026) reporta que las fragancias árabes pasaron de USD 2.800 M en 2023 a USD 4.900 M en 2025. El blog de YouTube dijo que hubo más de 770 M de vistas relacionadas con fragancias en 90 días (1-mar a 27-may-2024, global; sin dato de Shorts). **No hay datos de Shorts ni de Panamá.** Otras cifras de TikTok Shop y Amazon salieron de prensa y de Spate sin atribución completa; no las uses como firmes.
  - *Competencia 3:* Jeremy Fragrance tiene ≈ 2,5 M de suscriptores (varios rastreadores coinciden). Feedspot lista decenas de canales de perfume con menos de 50 mil, **sin datos de Shorts, de cara ni de crecimiento**.
  - *Riesgo 4:* YouTube prohíbe vender o promover falsificaciones (marca o logo idéntico o casi indistinguible). Su página **no menciona** "réplica", "clone" ni "inspirado en". Google Ads y Merchant Center sí prohíben "replica", "knock off", "clone" y "fake" junto a una marca, y suspenden la cuenta **sin aviso previo**. No investigué el derecho de marcas de Panamá. Las reseñas con plantilla repetida son el riesgo central del YPP, aunque YouTube dice que un canal de reseñas es aceptable si cada video tiene un enfoque distinto.
  - *Ingresos 8 pero con fricción:* una tienda propia deja margen directo, pero ya vimos que **no hay enlaces clicables en Shorts** salvo el perfil. Tampoco pude confirmar que puedas conectar tu tienda a YouTube Shopping desde Panamá: la tabla oficial de países de Merchant Center **no incluye a Panamá** según dos lecturas independientes (esa lista cubre anuncios de Shopping y fichas gratuitas; no cubre expresamente las etiquetas de YouTube). Confírmalo en YouTube Studio.
  - *Facilidad 6:* el stock sirve poco; lo natural es filmar tus propios frascos (manos y producto, sin cara).
- **Objetivo distinto:** J no es un canal para el YPP. Es publicidad para tu tienda y se mide en visitas y ventas a Nova Parfum. **Antes de puntuar bien o mal este nicho necesito saber en qué país vende y envía tu tienda.** Si vende en Panamá o Centroamérica, el Short debe ganar clientes locales, y eso cambia el contenido.

### Tabla ajustada con la nueva evidencia (top 5)

Solo ajusté un puntaje por evidencia: **A, competencia 7 → 6**, porque los canales grandes de Excel ya publican Shorts con mediana de unos 78 mil. Los demás se mantienen.

| Nicho | Total |
|---|---|
| B. Inglés para hispanohablantes | **7,55** |
| A. Excel/Sheets/productividad (ajustado; antes 7,60) | **7,45** |
| C. Carrera/entrevistas/CV | **7,40** |
| I. Excel para ventas y negocios | **7,35** |
| J. Perfumes (Nova Parfum) | **6,05** |

**Lectura honesta:** A, B, C e I quedan dentro de 0,2 puntos. **La tabla no decide.** Lo que desempata es lo que declaraste: dominas reportes de ventas y KPIs en Excel (I y A), ventas y marketing (I) y comunicación y oratoria (C). **B no coincide con nada de lo que dijiste dominar.** Ese desempate es un criterio ajeno a la tabla; lo digo para que lo valores tú.

### Canales de ejemplo: lo que sí se pudo comprobar

No encontré **ningún** canal que cumpla Shorts + sin cara + menos de 50 mil + crecimiento rápido. Es preferible 0 reales que uno inventado. Candidatos parciales:

| Canal | Datos comprobados | Límites |
|---|---|---|
| [Ms Excel (@msexcels)](https://vidiq.com/youtube-stats/channel/@msexcels/) | Creado el 7-oct-2024 (India); 37,4 mil suscriptores en unos 13 meses. De sus 48 subidas recientes (25-abr a 16-nov-2026), **42 son Shorts** de 12–29 s. Un verificador corrigió la lectura inicial que lo daba por canal de video largo | **No pude confirmar que no muestre la cara.** Hay que abrir sus videos. Los datos vienen de vidIQ y developereducators, no de la fuente primaria |
| [Analytics with Adam](https://vidiq.com/youtube-stats/channel/@analyticswithadam/) | 46 mil suscriptores; 24 Shorts de sus 48 subidas recientes, con 57 a 2.112 vistas | Crece despacio (fuentes contradictorias). Cara sin confirmar. Peor referencia |
| In the Now (de Kapwing), [caso documentado](https://kapwing.com/resources/we-grew-a-faceless-youtube-channel-to-1000-subscribers) | Sin cara, voz de IA, casi todo Shorts y menos de 50 mil. **≈ 1,2 mil suscriptores en 157 días, con 1,1 M de vistas totales** | Está **fuera de tus nichos**. Sirve como referencia realista del ritmo, no como modelo de nicho |

Referencia útil, **de un solo canal**: los 3 M de vistas de Shorts en 90 días del nivel ampliado quedan muy lejos de 1,1 M de vistas **totales** en 157 días. No generalices a partir de un caso.

### Pendiente: la API de YouTube

`YOUTUBE_API_KEY` no llegó a esta sesión (comprobado dos veces). Según la documentación del entorno, **una variable nueva solo la recibe una sesión nueva**. Qué hacer:

1. Confirma que la guardaste en la configuración del entorno (menú del entorno en la barra del título → Edit), con ese nombre exacto, como variable de entorno.
2. **Abre una sesión nueva** sobre este repositorio. No me pegues la clave en el chat.
3. En la sesión nueva ejecutaré estas búsquedas y ajustaré los puntajes con datos reales:

```
python3 buscar_canales.py "reporte de ventas excel" es
python3 buscar_canales.py "excel kpi dashboard sales" en
python3 buscar_canales.py "excel para ventas" es
python3 buscar_canales.py "perfumes árabes reseña" es
python3 buscar_canales.py "arabic perfume review" en
```

Cada consulta usa 200 unidades de la cuota diaria (el script hace dos páginas de resultados). El script sigue **sin probarse** contra la API real.

---

## 4. Recomendación final

**Decisión aprobada el 22-nov-2026: "Excel para ventas y negocios", en español y con voz propia.** Se aprobó **sin datos de la API** (el dueño eligió "aprobar ahora, validar después"). Si la API contradice esta recomendación, hay que revisarla antes de cambiar nada. Las reglas del canal están en `CLAUDE.md`.

**Versión del 20-nov-2026, que reemplaza a la anterior** (antes recomendé Excel genérico en inglés, antes de saber que vives en Panamá y qué dominas).

**Recomiendo el nicho I: "Excel para ventas y negocios"**, con plantillas propias de KPIs y reportes de ventas, y servicios de reportes como ingreso principal. **La tabla no lo hace ganador** (está a 0,2 puntos de otros tres); lo elijo por tres razones que **no** salen de la tabla:

1. **Coincide con lo que dominas** (reportes de ventas, KPIs en Excel, ventas, marketing). Tu experiencia es el "sello propio" que pide la política de contenido no auténtico.
2. **No depende de lo que no tienes.** Shopping afiliado no está disponible en Panamá y los afiliados externos de software están sin confirmar. Las plantillas y los servicios sí se pueden cobrar desde Panamá (Gumroad, Payhip con PayPal Business).
3. **Es el embudo natural**: el Short muestra un reporte real y el enlace de perfil vende la plantilla.

Lo que **no** sé y condiciona la recomendación:

- **Idioma (resuelto: español):** el inglés paga unas 4–8 veces más por vista de Shorts (AIR: $0,328 en EE. UU. y $0,040 en México), pero los anuncios de Shorts están lejos y no existen datos de venta de plantillas por idioma. Se eligió español; es coherente con tu dominio del idioma y del nicho.
- **Voz (resuelto: la tuya):** dominas la **oratoria**, y una voz propia es difícil de confundir con producción en masa.
- **Perfumes (J) (resuelto: descartado como canal principal):** 6,05. Nova Parfum vende en Panamá. Si algún día se hace, sería un **segundo canal** y con los ajustes de política explicados arriba.
- **Alternativa:** si prefieres que el canal gire en torno a tu oratoria y comunicación, C ("Carrera/entrevistas/CV") también encaja con lo que dominas (7,40).
- **Esto no es una promesa de resultados.** No encontré ningún canal verificado que cumpla todos los criterios y los únicos datos de crecimiento son de un canal de otro nicho (≈ 1,2 mil suscriptores en 157 días).

---

## 5. Ruta de ingresos antes de cumplir los requisitos del YPP

**No esperes al YPP para ganar dinero.** Mientras tanto:

1. **Producto propio (la vía más controlable):**
   - plantillas de Excel/Sheets de ventas y KPIs (dashboard de ventas, seguimiento de pipeline, reporte mensual), vendidas en Gumroad o Payhip (sección 3 bis, tabla de plataformas);
   - un servicio puntual (construir o automatizar un reporte de ventas para una pyme).
2. **Afiliados externos:** **no los des por seguros desde Panamá.** Shopify Collabs y Notion no aceptan afiliados nuevos, y Amazon Associates, Skillshare, Domestika, Udemy y Microsoft están sin confirmar para residentes de Panamá (sección 3 bis). Prueba solicitando el alta y no pongas esta vía en tus cuentas hasta que te aprueben. Las políticas de YouTube avisan de que un exceso de enlaces de afiliados en cuentas dedicadas puede considerarse spam.
3. **Dónde poner los enlaces:** los enlaces en la descripción y en los comentarios de un Short **no son clicables** (regla oficial vigente). Usa el **enlace de perfil del canal** (hasta 14), el enlace "Related Video" a tus propios videos si tu canal tiene acceso a funciones avanzadas, y los videos largos. Cada Short debe terminar diciendo "enlace en mi perfil".
4. **Captación de contactos:** una hoja de cálculo gratuita a cambio de un correo. Útil para vender después.
5. **YouTube Shopping afiliado:** **no está disponible para creadores basados en Panamá** (sección 3 bis). Revisa YouTube Studio → Ingresos cada mes por si Panamá entra en la ampliación a 35 países. Mientras tanto, no cuentes con esta vía.
6. **Fan funding** (membresías, Super Chat, Super Thanks): sí disponible en Panamá desde el nivel ampliado de 500 suscriptores, que sigue vigente después del 1-feb-2027.
7. **Patrocinios:** con <50k suscriptores serán pocos y poco rentables (estimado). YouTube anuncia incentivos para acuerdos de marca, sin detalles todavía.

### Cuánto tardarías en cumplir los requisitos (estimado)

No hay datos confiables de tiempo para canales nuevos. Lo único que se puede afirmar es la aritmética de la sección 1:

- Ritmo de 5–7 Shorts/semana → 65–91 Shorts por trimestre.
- Para el nivel ampliado por Shorts (3 M en 90 días): 33–46 mil vistas por Short. Para 10 M: 110–154 mil. Para 20 M: 220–308 mil.
- Para la **vía de formato largo** (8.000 horas para solicitantes nuevos desde el 1-feb-2027): 8.000 horas son 480.000 minutos. Con una retención media de 4 minutos por vista, hacen falta ≈ 120.000 vistas de videos largos (cálculo mío; la retención real puede variar mucho).
- **Mi expectativa, sin respaldo de datos:** meses a años. La mayoría de los canales no alcanza estos umbrales. Si en 90 días tu mediana de vistas por Short es de cientos, el YPP está lejos.
- **Recomendación:** además de los Shorts, publica 1–2 videos largos al mes sobre los mismos temas. Los Shorts atraen, y las horas de formato largo son la vía realista a los anuncios.

---

## 6. 20 ideas de Shorts (Excel / Google Sheets) y 8 ideas de ventas y negocios

Las 20 primeras son de Excel genérico (nicho A). Para el nicho recomendado (**I, Excel para ventas y negocios**) hay 8 ideas específicas en la tabla de después. Úsalas primero y completa con las genéricas.

Los ganchos de estas 20 ideas están en inglés y hay que **traducirlos**: el idioma aprobado es el español. Las 8 ideas de ventas ya están en español. Cada Short debe mostrar una **demostración real en pantalla** con datos distintos, para no caer en la plantilla repetida.

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


### 8 ideas específicas de ventas y negocios (nicho I)

Los ganchos van en español. Si eliges inglés, tradúcelos. Usa **datos de ejemplo inventados por ti** (nunca datos reales de clientes ni de tu tienda).

| # | Gancho (primer segundo) | Guion en 3 líneas | Qué se ve |
|---|---|---|---|
| V1 | "Tu reporte de ventas miente si no haces esto." | 1) Los totales mensuales ocultan quién vende de verdad. 2) Una tabla dinámica por vendedor lo muestra. 3) Compara el top 3 con el resto. | Ventas por vendedor ordenadas, con el top 3 resaltado |
| V2 | "Calcula tu tasa de cierre en 10 segundos." | 1) Oportunidades ganadas ÷ oportunidades totales. 2) Escribe la fórmula con CONTAR.SI. 3) Formato de porcentaje y una alerta. | Hoja de pipeline con la tasa calculada |
| V3 | "Cuánto vale de verdad un cliente." | 1) Ticket promedio × compras por año. 2) Dos fórmulas con PROMEDIO y CONTAR.SI. 3) Resultado y qué decisión tomar. | Tabla de clientes con la columna de valor anual |
| V4 | "El forecast de ventas más simple que sí sirve." | 1) Toma los últimos 6 meses. 2) Usa PRONOSTICO.LINEAL. 3) Dibuja la línea y marca que es una estimación. | Gráfico de ventas con la línea de tendencia |
| V5 | "Un KPI que cambia de color solo." | 1) Meta mensual en una celda. 2) Formato condicional: verde, ámbar y rojo. 3) Cambia una cifra y mira el color. | Tablero con tres KPIs en semáforo |
| V6 | "Tu pipeline en una sola hoja." | 1) Etapa, monto y probabilidad. 2) Multiplica monto por probabilidad. 3) Suma el pipeline ponderado. | Columnas del pipeline con el total ponderado |
| V7 | "Resta esto antes de celebrar tu margen." | 1) Margen = (precio − costo) ÷ precio. 2) Hazlo en una columna y copia hacia abajo. 3) Ordena y mira los productos que pierden. | Lista de productos con el margen en rojo |
| V8 | "Tu reporte mensual en 3 pasos." | 1) Importa el CSV. 2) Una tabla dinámica y un gráfico. 3) Guárdalo como plantilla para el mes siguiente. | Flujo desde el archivo hasta el tablero listo |

Para evitar el riesgo de "plantilla repetida", cada Short debe cambiar el caso, los datos y la decisión que se toma con el resultado, no solo la fórmula.

---

## 7. Herramientas y costo estimado por Short

**Todos los precios son estimados y no los verifiqué. Comprueba las tarifas vigentes antes de contratar.**

| Etapa | Herramienta | Costo mensual estimado |
|---|---|---|
| Guion e ideas | Claude (esta sesión) | incluido en tu plan |
| Voz | Tu propia voz con un micrófono (el del teléfono o uno básico) | $0 (un micrófono USB básico sería un gasto único, **estimado**, sin verificar precio) |
| Grabación de pantalla | OBS Studio o grabador del sistema | $0 |
| Edición y subtítulos | CapCut o DaVinci Resolve (versiones gratuitas) | $0 |
| Miniatura/gráficos | Canva (plan gratuito) | $0 |

- **Costo por Short:** con tu propia voz y herramientas gratuitas, **≈ $0**. Queda holgura dentro de tus $0–30 mensuales.
- **Tiempo por Short:** estimo 20–45 minutos entre guion, grabación, voz y edición (**estimado**).

---

## 8. Plan de validación de 30 días

### Qué hacer

- **22–30 Shorts** en 30 días (5–7 por semana). Un tema y una voz consistentes.
- **Variación:** no más de 2 Shorts seguidos con la misma estructura. Cambia el caso de uso, el ejemplo y el gancho.
- **1 video largo** (5–8 min) en la semana 3 o 4 como prueba de formato largo.
- **Marcado de contenido:** declara el contenido sintético (por ejemplo, un fondo generado con IA) donde YouTube lo exija. Revisa la política vigente de divulgación. Con voz propia, esto aplica solo si usas material generado.

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
- **Actualización del 20-nov-2026 (Panamá, nichos nuevos):**
  - Elegibilidad de afiliados de YouTube Shopping (18 países): https://support.google.com/youtube/answer/13376398
  - Etiquetado de Amazon en YouTube Shopping (11 países): https://support.google.com/youtube/answer/17105501
  - Ampliación a 35 países, Made on YouTube 2026: https://blog.youtube/intl/es-419/news-and-events/made-on-youtube-26-juntamos-a-marcas-y-creadores/
  - Programa ampliado del YPP (lista de países, incluye Panamá): https://support.google.com/youtube/answer/13429240?hl=en
  - Definición de canal activo desde el 1-feb-2027: https://support.google.com/youtube/answer/12843009?hl=en
  - Enlaces clicables y no clicables en Shorts: https://support.google.com/youtube/answer/13748639
  - Políticas de spam y prácticas engañosas: https://support.google.com/youtube/answer/2801973
  - Merchant Center, políticas de falsificación: https://support.google.com/merchants/answer/6149993?hl=en
  - AIR Media-Tech, RPM y CPM por país: https://air.io/en/air-data-findings/youtube-monetization-statistics-2026
  - Estadísticas de canales (terceros): https://vidiq.com/youtube-stats/channel/@msexcels/ · https://vidiq.com/youtube-stats/channel/@analyticswithadam/ · https://vidiq.com/youtube-stats/channel/@leilagharani/
  - Kapwing, canal sin cara con voz de IA: https://kapwing.com/resources/we-grew-a-faceless-youtube-channel-to-1000-subscribers
  - Spate sobre fragancias (secundario): https://www.spate.nyc/blog/fragrance-trends-2026-on-google-tiktok-and-instagram
  - Documentación de cobro y tarifas de PayPal, Gumroad, Payhip, Lemon Squeezy y Etsy: páginas oficiales de cada plataforma, leídas por la investigación; revisa las vigentes antes de abrir cuenta.
