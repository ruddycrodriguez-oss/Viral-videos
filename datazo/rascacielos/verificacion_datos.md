# Verificación de datos: «Así se construye: un rascacielos» (23 a 25-nov-2026)

Regla del canal: cada dato con **2 fuentes independientes que se abrieron y se leyeron**. Una página que no abrió (403, 503, vacía) **no cuenta como leída**. Las citas vienen de la extracción de las páginas; conviene una última comprobación literal antes de publicar. **No es asesoría de ingeniería.**

**Estado del guion: NO está listo para producir tal cual.** Hay datos que se confirman, pero **cuatro frases se apoyan en algo que ninguna fuente leída dice** y piden una decisión del dueño (sección «Decisiones»).

## Escena 2 (ladrillos, Chicago)

| Frase del guion | Estado | Fuentes leídas |
|---|---|---|
| Edificio de **dieciséis pisos** en Chicago | Confirmado (con matices) | NPS, formulario del Monadnock: «Sixteen stories high with an attic, it rises 215 feet»; SAH Archipedia (Society of Architectural Historians / University of Virginia Press): «Standing sixteen stories and 210 feet high». HABS (NPS/Library of Congress) dice «16 stories, and a 17th story attic» pero es de la misma familia que el NPS. CTBUH da 17 plantas y mide el bloque completo (1893). |
| **Paredes de ≈1,8 m** («casi dos metros»; en pantalla 1,8 METROS) | Confirmado | Seis pies en la base: NPS, SAH Archipedia («Six-foot thick walls … at the ground floor»), Chicago Landmarks (ciudad de Chicago: «six-foot thick walls at the base»), Chicago Architecture Center («six-feet-thick at the corners»). **6 × 0,3048 = 1,83 m es conversión propia**; «casi dos metros» es un redondeo generoso (≈9 % menos). |
| «**necesitó** paredes…» | **No confirmado** | Ninguna fuente dice que lo necesitara: fue una elección de diseño (SAH: los hermanos Brooks «preferred the known durability of load-bearing masonry»; el Chicago Architecture Center dice que se consideró incluir columnas de acero). |
| «Cada piso aplasta a los de abajo y las paredes de la base engordan» | Explicación estructural estándar **sin cita literal** | NPS: muros «tapering slightly as they rise»; HABS: «gradually taper». Ninguna página abierta enuncia la causa; se marca como explicación general. |

El dato corresponde a la **mitad norte** (1889-91), no al bloque completo (1893). No dar altura exacta (197 a 215 pies según la fuente; «más de 60 metros» es compatible con todas). No decir que es «el más alto de ladrillo»: **no se confirma** (el Ayuntamiento de Filadelfia, de mampostería de carga, es más alto; ASCE).

## Escena 3 (esqueleto de acero)

| Frase | Estado | Fuentes leídas |
|---|---|---|
| Un esqueleto de acero **sostiene** el edificio | Confirmado | Chicago Public Library (entrada institucional, 6-abr-2014): «a skeleton of steel beams holds the floors, and the interior and exterior walls up»; Chicago Architecture Center, Architecture Encyclopedia («Skeleton Frame Construction»): soporta toda la carga. |
| «…que **lleva el peso hasta el suelo**» | **No confirmado literalmente** | Ni NPS, ni CPL, ni CAC lo dicen en la página abierta (el buscador sugirió «transfers loads to the ground» del CAC y la cita **no apareció** en la página leída). Se puede mostrar en la imagen (columnas hasta la base) sin decirlo como dato. |
| «El vidrio **solo cuelga**, como una cortina» | Confirmado con matiz | NPS (Standards for the Treatment of Historic Properties, 2017, «Curtain Walls»): no soporta el peso del edificio y se cuelga o ancla al sistema estructural; CPL: «exterior walls do not support the weight of the building»; CAC: «non-load-bearing curtains». **«Solo cuelga» no está respaldado** (el muro cortina también transmite a la estructura la carga del viento; esa parte no se leyó). |

Además: el Home Insurance Building (1885) tenía, según el Chicago Architecture Center, estructura de **hierro fundido**, no de acero, y su muro cortina era de piedra. No atribuir el acero a 1885 ni decir «el primer rascacielos».

## Escena 4 (cimentación profunda)

| Frase | Estado | Fuentes leídas |
|---|---|---|
| Un edificio muy pesado **puede hundirse** (asentarse) | Confirmado | Torre Milenio de San Francisco: STRUCTURE magazine («settlement exceeding 16 inches» en 2015; proyección original «4 to 6 inches») y ENR (asentamiento desde 2008; 30 in de inclinación). **16 pulgadas = 40,6 cm (conversión propia).** El asentamiento es **lento**; que la tierra «se agriete» es dramatización visual (ninguna fuente lo describe). |
| Perforar y bajar **columnas de concreto hasta el terreno firme** = cimentación profunda | Confirmado | FHWA, «A Quarter Century of Geotechnical Research» (pilotes y pozos perforados llevan la carga a un estrato más profundo y rígido, p. ej. roca; «a drilled shaft is a machine-excavated hole filled with concrete»); FHWA GEC 12 («upper soil strata too compressible or too weak…»). Ejemplo: Torre Milenio, 18 pilotes en roca a 220 ft. El terreno firme no siempre es roca. |

## Escena 5 (amortiguador de masa, Taipéi 101)

| Frase | Estado | Fuentes leídas |
|---|---|---|
| Una gran masa colgada frena el balanceo | Confirmado | Guinness World Records («a heavy weight that is not directly attached to the structure it sits inside»); CTBUH («a large spherical steel pendulum that offsets lateral movements»); Thornton Tomasetti («hangs from the 92nd floor»); Penn State (D. Russell: la masa se mueve en oposición). |
| «Si el edificio se va a un lado, la bola se va al **otro**» | Confirmado solo de forma indirecta | Penn State: «In the higher frequency mode the two masses move in opposite…». Redacción más segura: «por inercia se queda atrás y se mueve en sentido contrario». El freno real lo hacen sus amortiguadores. |
| **660 toneladas** | Confirmado | Guinness («660-tonne (728 ton)»), Academia Sinica («660 metric tons»), Business Insider («660 metric tons»). CTBUH y Thornton Tomasetti dan 728 y 730 toneladas **cortas**; 728 t cortas = 660,4 t métricas (conversión propia). Un artículo de 2004, previo a la apertura, decía 680 t. |
| Ubicación y tamaño | Confirmado | Entre los pisos 87 y 92 (Guinness, Business Insider); esfera de 5,5 m (Academia Sinica). |
| Número de placas (41) o de cables | **No confirmado**: no usar | Una sola fuente secundaria; el sitio oficial no se pudo leer. |

«660 toneladas» se dice «seiscientas sesenta toneladas» (femenino): en `voz.py` se fuerza con `660|seiscientas_sesenta`.

## Escena 6 (ascensor y oídos)

| Frase | Estado | Fuentes leídas |
|---|---|---|
| Los ascensores más rápidos pasan de **60 km/h** | Confirmado (y se queda corto) | Mitsubishi Electric, Shanghai Tower: 73,8 km/h (1.230 m/min); Hitachi, Guangzhou CTF Finance Centre: 75,6 km/h (récord Guinness 2019). Son velocidades **nominales**, no del viaje. No se abrió la página actual de Guinness. |
| «Allá arriba el aire tiene menos presión» | Confirmado | NOAA JetStream («air pressure»); NASA Glenn, Earth Atmosphere Model. En ≈400 m baja ≈4,7 kPa (≈4,6 %): **cálculo propio** con el modelo de la NASA. |
| «Por eso se te tapan los oídos» | Confirmado con matiz | Cleveland Clinic; UTHealth Houston (McGovern): ocurre cuando la presión **cambia más rápido** de lo que la trompa de Eustaquio puede igualarla. Decir solo «menos presión» simplifica. |

## Decisiones que necesito del dueño antes de producir

1. **Escena 2:** quitar «necesitó» (no está respaldado). Propuesta: «En Chicago, un edificio de ladrillo de dieciséis pisos tiene paredes de casi dos metros en la base» (con «≈ 1,8 m» en pantalla), o «de un metro ochenta».
2. **Escena 3:** quitar «lleva el peso hasta el suelo» y «solo cuelga». Propuesta: «Entonces, cambias las paredes por un esqueleto de acero que sostiene todo el edificio. Ahora la fachada de vidrio se cuelga de ese esqueleto, como una cortina, y ya no sostiene nada del edificio.» (la imagen puede mostrar las columnas hasta el suelo).
3. **Escena 5:** «la bola se va al otro lado» → «por inercia se mueve en sentido contrario».
4. **Escena 6:** «allá arriba el aire tiene menos presión» → «la presión del aire cambia más rápido de lo que tus oídos pueden igualarla».

## No se pudo abrir (no cuentan como leídas)

Britannica (403), Library of Congress `loc.gov/pictures/item/il0049` (403; el PDF de datos HABS sí se leyó), Encyclopedia of Chicago (503), PBS Building Big (403), WBDG muros cortina (cargó vacía), CTBUH «Buildings Without Walls» (404), Mayo Clinic (403), sitio oficial de Taipei 101 (sin datos), ICE/Ingenia (403), Cambridge phase-trans (503).
