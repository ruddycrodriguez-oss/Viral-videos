# Muestras de voz del rascacielos (25-nov-2026)

Texto de las tres muestras (≈17 s): escena 1 completa **más las dos primeras frases de la escena 2** (la escena 1 sola dura ≈8 s hablada, así que no llega a 15 s):

> ¿Cómo se construye un edificio de cien pisos sin que se caiga? Lo más loco está colgado cerca de la punta. Si apilas ladrillos, levantas una torre. Pero cada piso aplasta a los de abajo y las paredes de la base engordan.

Archivos (`.m4a` para escuchar en el iPad; `.wav` es el original sin compresión, 48 kHz mono):

| Muestra | Archivo | Modelo (licencia) | Descripción de la voz |
|---|---|---|---|
| **1** | `voz1_baritono_maduro_qwen3tts` | Qwen3-TTS 1.7B VoiceDesign + Base (Apache-2.0) | Barítono grave, cálido y con carácter, de unos 40 y tantos años; documental con humor. |
| **2** | `voz2_joven_brillante_qwen3tts` | Qwen3-TTS 1.7B VoiceDesign + Base (Apache-2.0) | Barítono medio, más joven y brillante; divulgador entusiasta. |
| **3** | `voz3_voxcpm2` | VoxCPM2 (Apache-2.0) | Narrador de unos 35 años, cálido y enérgico (descripción base de `generar_crudos.py`). |

Las tres son **voces diseñadas con una descripción en texto** (textos en `../estilos/` y en `generar_crudos.py`). **No se clonó a nadie.** Para que todas las frases suenen como la misma persona, la voz se fijó con una **toma propia del modelo (audio sintético) como ancla**; no se usó audio de ninguna persona ni de ningún video.

## Medidas (no puedo oír: esto es lo único que puedo comprobar)

| Medida (umbral) | 1 Qwen barítono | 2 Qwen joven | 3 VoxCPM2 | A Qwen cálido (descartada) | Ming 0.5B (descartada) |
|---|---|---|---|---|---|
| Errores de transcripción, Whisper medium (0) | **0 / 42** | **0 / 42** | **0 / 42** | 0 / 42 | **1 / 42** |
| «θ» en el reconocedor de fonemas (0) | **0** | **0** | **0** | 0 | **2** |
| «s» reconocidas de las esperadas | 20 / 21 | 20 / 21 | 21 / 21 | 21 / 21 | 19 / 21 |
| Palabras por minuto de habla (160 a 175), cuenta oficial | 167,2 | 167,7 | 169,1 | 167,3 | 167,6 |
| Palabras por minuto sobre la alineación (sin las pausas ≥ 0,25 s) | 173,6 | 171,9 | **179,2** | 174,8 | 171,9 |
| Rango de tono p5 a p95 (≈ 12 st; banda 10 a 15) | **13,3 st** | 15,0 st | **11,4 st** | **17,9 st** | **19,3 st** |
| Tono medio, CREPE (hombre adulto ≈ 100 a 180 Hz) | **124 Hz** | 171 Hz | 168 Hz | 138 Hz | 143 Hz |
| Volumen (−14 LUFS, ±0,5) | −14,4 | −14,0 | −14,0 | −14,2 | −14,1 |
| Pico real (≤ −1 dBTP) | −1,0 | −1,0 | −1,0 | −1,0 | −1,0 |
| Parecido de timbre entre frases (CAM++; > 0,8 ≈ misma persona) | **0,86** | 0,80 | 0,77 | 0,79 | 0,55 (sin ancla) |
| Cuánto hubo que frenar la voz del modelo | ×0,88 | ×0,82 | ×0,78 | ×0,79 | ×0,81 |

- **Descartadas por las medidas:** Ming-3.0-tts-0.5B (MIT) falla en transcripción y «θ», y su timbre no se mantiene; la voz «A» de Qwen se pasa de rango de tono (17,9 st). Qwen y VoxCPM2 aprueban las medidas obligatorias con las matizaciones de la tabla.
- Los modelos hablan más deprisa (190 a 216 palabras por minuto) que las 160 a 175 pedidas, así que se **frenaron con Rubber Band** (cambio de ritmo sin cambiar el tono). La voz 1 es la que menos se frenó. Si al oírlas notas algo metálico o «arrastrado», es la señal de ese ajuste.
- «Palabras por minuto, cuenta oficial» es la de `voz.py` (frase recortada, sin pausas ≥ 0,4 s). La segunda fila es más estricta (solo suma lo que dura cada palabra) y **da más alto** porque descuenta las pausas de coma de 0,3 s que se insertan; la voz 3 es la única que se pasa de 175 con ella.
- «θ» y «s» vienen de un reconocedor automático (`wav2vec2` fonemas); el reconocedor no es perfecto; como control, con la voz Kokoro (que sí dice «s») da 0 «θ».
- Los números son de **esta** muestra de 17 s: no demuestran que suene natural. **Eso lo juzgas tú al oírlas.** Ninguna medida detecta si una voz suena robótica.
