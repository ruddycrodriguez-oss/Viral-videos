# Canal de YouTube Shorts: "Excel para ventas y negocios"

Decisión aprobada por el dueño del canal el 22-nov-2026. El análisis completo, con fuentes y puntajes, está en `nicho.md`. Este archivo guarda solo la decisión y las reglas de trabajo.

## Decisión

- **Nicho:** Excel para ventas y negocios (reportes de ventas, KPIs, pipeline, forecast, márgenes). Es la versión enfocada del nicho de Excel.
- **Idioma:** español.
- **Voz:** la del dueño. Sin cara en pantalla. No usar voz de IA.
- **Formato:** solo Shorts, con grabación de pantalla vertical. Ritmo de 5–7 por semana. Un video largo al mes como apoyo para las horas de visualización.
- **Meta de ingresos:** vender plantillas propias y servicios de reportes. Los anuncios de Shorts son un objetivo de largo plazo, no el plan.
- **Descartado como canal principal:** perfumes (Nova Parfum). Si algún día se hace, será un segundo canal con reglas aparte.
- **Estado de la validación:** aprobado **sin datos de la API de YouTube**, porque `YOUTUBE_API_KEY` no estaba disponible en el entorno. Sigue pendiente correr `buscar_canales.py` con las cinco consultas de `nicho.md` (sección 3 bis, "Pendiente: la API"). Si esos datos contradicen la recomendación, hay que revisarla con el dueño antes de cambiar nada.

## Contexto del dueño

- Vive en Panamá. Domina ventas y desarrollo de negocios, reportes de ventas y KPIs en Excel, marketing digital, comunicación y oratoria.
- Presupuesto de herramientas: $0–30 USD al mes.
- Temas que no quiere tratar: ninguno declarado todavía. Preguntar antes de proponer temas sensibles.

## Reglas de contenido

1. Cada Short muestra una **demostración real en pantalla** con **datos de ejemplo inventados**. Nunca usar datos reales de clientes ni de la tienda Nova Parfum.
2. Evitar la plantilla repetida (política de contenido no auténtico de YouTube, que puede quitar la monetización de **todo el canal**). Cada Short cambia el caso, los datos y la decisión que se toma con el resultado, no solo la fórmula. No más de 2 Shorts seguidos con la misma estructura.
3. Primer segundo: un gancho claro. Guion de 3 líneas. Cierre con "enlace en mi perfil".
4. Nada de asesoría financiera ni de inversión. Los ejemplos de ventas y KPIs son educativos.
5. Revisar la página de permisos de Microsoft antes de publicar capturas de Excel.
6. No usar clips ni material ajeno. Declarar el contenido sintético donde YouTube lo exija (por ejemplo, si se genera algún fondo con IA).
7. La IA sirve para ideas, guiones y edición. El criterio, los ejemplos y la voz son del dueño.

## Reglas de ingresos y enlaces (verificadas el 20-nov-2026)

- Los enlaces en la descripción y los comentarios de un Short **no son clicables**. Todo el embudo pasa por el **enlace de perfil** del canal.
- **YouTube Shopping afiliado no está disponible para creadores basados en Panamá.** No contar con él. Revisar YouTube Studio → Ingresos cada mes.
- Plantillas: **Gumroad** (cobro a banco en USD) o **Payhip con PayPal Business**. Stripe propio y Etsy no están disponibles en Panamá. PayPal en Panamá cobra 5,40 % + USD 0,30 por venta y 1 % (mínimo USD 15) por retirar a banco local. Lemon Squeezy reportó cierre de registros nuevos el 16-nov-2026: no apoyarse en él sin comprobarlo.
- Afiliados externos de software: **sin confirmar** para residentes de Panamá. No ponerlos en el plan hasta que aprueben la cuenta. Un exceso de enlaces de afiliados puede considerarse spam.
- Programa de Socios de YouTube: Panamá es elegible. Nivel de 500 suscriptores (fan funding) = 500 subs + 3 subidas en 90 días + 3.000 horas de formato largo o 3 M de vistas de Shorts en 90 días. Anuncios: 1.000 subs + 4.000 horas o 10 M de vistas de Shorts. Desde el 1-feb-2027, los solicitantes nuevos necesitan 8.000 horas o 20 M de vistas de Shorts. Quedan sin aclarar las solicitudes pendientes en esa fecha.
- Cobro de AdSense desde Panamá: cheque, wire o PayPal Hyperwallet. Umbral de USD 100. Enviar el formulario fiscal de EE. UU. (W-8BEN) antes del 10 de diciembre de cada año. Es probable, y es inferencia, que la retención sobre vistas de EE. UU. sea 30 %. Consultar con un contador.

## Plan de validación de 30 días (resumen; detalle en `nicho.md`, sección 8)

- 22–30 Shorts y 1 video largo. Medir visto vs. deslizado, % promedio visto, suscriptores por 1.000 vistas y la mediana de vistas por Short.
- No existen referencias oficiales de YouTube para estas métricas: comparar contra la propia base del canal.
- Criterios para cambiar (propuestos, no son datos de mercado): día 14, ajustar ganchos antes de tocar el nicho; día 30, cambiar de subtema si la mediana es <300 vistas y ningún Short supera 3.000; cambiar de nicho solo tras un segundo ciclo de 20 Shorts con la misma señal y menos de 0,3 suscriptores por 1.000 vistas.

## Pendientes

1. Correr `buscar_canales.py` con las cinco consultas cuando exista la clave (en la configuración del entorno, como secreto de red para `www.googleapis.com` con la cabecera `x-goog-api-key`, o como variable `YOUTUBE_API_KEY`; una sesión nueva la recibe). Actualizar puntajes y canales de ejemplo. El script sigue sin probarse contra la API real.
2. Confirmar afiliados externos, Lemon Squeezy y cualquier cambio en la lista de países de YouTube Shopping.
3. Traducir al español los ganchos de las 20 ideas genéricas de `nicho.md` (sección 6). Las 8 ideas de ventas ya están en español.
4. Preguntar los temas que el dueño no quiere tratar.

## Cómo trabajar en este repositorio

- Citar la fuente de cada dato. Marcar como "estimado" lo que no se pueda comprobar. No inventar cifras ni canales.
- Los puntajes de `nicho.md` son juicio con datos parciales. Ver la advertencia de la sección 0.
- Nunca pedir al dueño que pegue claves en el chat. Usar el formulario seguro del entorno o su configuración.
- No incluir el nombre de la tienda ni datos personales del dueño en búsquedas web ni en peticiones a servicios externos.
- Confirmar con el dueño antes de publicar, enviar o crear algo fuera de este repositorio.
- Ramas: trabajar en `claude/youtube-shorts-niche-strategy-e9z168`. No crear pull requests sin que el dueño lo pida.
