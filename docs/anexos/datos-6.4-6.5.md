# Datos para los apartados 6.4 y 6.5 del Informe de Metodología y Validación

**Fecha de corte:** 11-10-2026, tras las tres rondas de correcciones previas a la entrega (11-10-2026) y el enlazado de las Fuentes · **Fuente principal:** `anexo-III-incidencias.csv`, con 582 registros (los IDs `I-NNN` remiten a esa tabla) · **Evidencias de esas correcciones:** `evidencias/correcciones-previas-entrega-juridicas.md`, `evidencias/correcciones-previas-entrega-tecnicas.md` y `evidencias/enlaces-fuentes.md`

---

## 6.4 Resultados

| Tipo de contenido | Elementos revisados | Incidencias detectadas | Tasa de error | Corregidas |
|---|---|---|---|---|
| Temas administrativos | 10 temas | 219 registros, 166 de fondo | **10 de 10 temas con errores de fondo (100,0 %)** | 218 de 219 (1 no aplicada por criterio) |
| Temas técnicos | 30 temas | 114 registros, 39 de fondo | **18 de 30 temas con errores de fondo (60,0 %)** | 111 de 114 (3 descartadas) |
| Preguntas administrativas | 1.525 (banco) | 774 preguntas | 50,8 % | 774 (0 pendientes) |
| Preguntas técnicas | 1.765 (banco) | 30 preguntas, 5 de ellas de fondo | 1,7 % en total; 0,3 % de fondo | 30 (0 pendientes) |
| Preguntas de casos | 1.492 | 84 registros | 5,6 % (orientativa) | 80 (4 no aplicadas por criterio) |
| Diagramas | 553 SVG | ≈235 (estimada) | ≈42,5 % (estimada) | ≈235 (0 pendientes) |

### Cómo se ha calculado cada fila (y qué cifras son exactas)

**Temas administrativos y técnicos**

- **Elementos revisados (exacta):** son los 10 temas del bloque administrativo y los 30 del técnico.
- **Incidencias detectadas (exacta):** son los registros del Anexo III con ámbito *contenido* o *fuentes*. Los test, los casos y los diagramas tienen fila propia en esta tabla.
  - Se considera **de fondo** toda incidencia de gravedad alta o media.
  - Hay registros que agrupan varios preceptos; por ejemplo, el I-146 reúne 10 citas no literales de la LPACAP en el T6.
- **Tasa de error:** porcentaje de temas con al menos una incidencia de fondo en su contenido.
  - En el bloque administrativo, **los 10 temas** tenían errores de fondo frente al BOE consolidado.
  - En el técnico no tienen ninguna registrada T12, T13, T14, T15, T26, T28, T33, T35, T36, T38, T39, T40. En casi todos ellos, lo que se registró son frases sobre el examen, diagramas o secciones fuera del título.
- **Corregidas (exacta):** registros en estado *Corregida*.
  - No queda ninguno abierto. La tercera ronda (11-10-2026) corrigió I-539 (T37: «IEEE 802.1AX (antes 802.3ad)») e I-333 (T11: homogeneización general de castellano e inglés), y añadió I-582 (T34, Fuentes: la Orden PRE/1716/2011 es de 9 de junio, no de 20 de junio), ya corregida; por eso el bloque técnico pasa de 113 a 114 registros.
  - I-011 (T1: el §12 duplica materia del Tema 2) queda como **no aplicada (criterio)**: por decisión del adjudicatario se mantiene el alcance aprobado por el Ayuntamiento, porque no es un error de contenido. Cuenta como cerrada, no como abierta.
  - Las correcciones previas a la entrega cerraron I-043 (T2, supletoriedad del art. 149.3), I-068 (T3, art. 130.3 LBRL) e I-335 (T11, «a traves»), y añadieron I-580 (T11 §6.4: requisitos de Windows 11, Secure Boot y TPM), ya corregida.

**Preguntas administrativas**

- **Elementos revisados (exacta):** el banco publicado tiene 1.525 preguntas: T1-T5, T7, T8 y T10 con 150 cada uno, T6 con 160 y T9 con 165. Se ha contado en `assets/data/preguntas.json` de la plataforma.
- **Incidencias detectadas.** Se suman dos partidas:
  - **768 preguntas modificadas en la revisión jurídica** (cifra exacta, sacada de los changelogs v1.2-v1.4 del 01-10-2026): T1 40, T2 32, T3 29, T4 51, T5 69, T6 160, T7 139, T8 55, T9 117 y T10 76.
  - **6 preguntas modificadas en la corrección previa a la entrega (11-10-2026):** en el T1, las P68, P70 y P71, que duplicaban otras del banco (I-009), se sustituyen por preguntas sobre los arts. 20.5, 17.2 y 25.3 CE; en el T3, las P90, P91 y P92 pasan a la redacción vigente del art. 130.3 LBRL y a la excepción para determinados directores generales (I-068, I-069). Ninguna de las seis figura entre las preguntas sustituidas o precisadas del T3 en su changelog v1.2; en el T1, el changelog no lista las preguntas por número.
  - Antes de esa corrección figuraban como pendientes 4 de ellas (las tres del T1 y la P91 del T3); la P90 y la P92 se suman ahora porque también se modificaron.
  - Además, se añadió la explicación a la P101 del T1 (LO 11/1995) y a la P65 del T2 (LO 6/1982 y LO 3/1983), sin cambiar enunciado ni opciones: no se suman.
- **Ojo al interpretar la tasa.** Mide sobre todo un **cambio de criterio**, no solo errores:
  - La revisión jurídica exigió que toda pregunta saliera del texto literal de la norma, sin supuestos de aplicación, doctrina ni interpretación.
  - En el T6 se reescribieron las 160 para usar distractores que fueran variaciones leves del literal.
  - Los changelogs no separan, en todos los temas, cuántas de esas preguntas contenían un error de contenido. Donde sí lo hacen:
    - T1: 20 corregidas al literal y 20 sustituidas.
    - T3: 22 sustituidas y 7 con la referencia precisada.
    - T9: 55 sustituidas y 62 retocadas.
    - T8: 50 reescritas, 4 con la referencia corregida y 1 con el enunciado ajustado.
  - Las 20 preguntas pedagógicas de cada tema se rehicieron aparte y **no se suman** aquí.

**Preguntas técnicas**

- **Elementos revisados (exacta):** el banco publicado tiene 1.765 preguntas: T11 con 25 y T12-T40 con 60 cada uno.
- **Incidencias detectadas (exacta, salvo lo indicado):** son las preguntas publicadas que se modificaron después de su publicación, o que siguen señaladas:
  - **T11, las 25 preguntas:** faltaba el «¿» de apertura, había tildes y en 10 aparecía la etiqueta interna «[v2]» (I-343, I-344). Entre ellas están las 4 de fondo señaladas por el Equipo IAM (validación técnica), P14, P17, P23 y P25 (I-328 a I-331), **corregidas el 11-10-2026** con las propuestas del Ayuntamiento. En la misma corrección se simplificó el enunciado de la P6 (I-578), se acotó la P18 a la función de altas, bajas y modificaciones del Padrón (I-332) y se reordenó el texto de las opciones de 8 preguntas para equilibrar el reparto en a 8 · b 8 · c 9 (I-349). Todas son preguntas del mismo banco de 25, que ya se contaba entero, así que la cifra no cambia.
  - **T23 P43:** solo de forma (I-433).
  - **T25 P6 y P7:** ISO/IEC 25010:2023 (I-450 y I-451).
  - **T22 P42 y P52:** solo cambia la etiqueta del RFC; la respuesta no cambia (I-422 y I-423).
  - **T29 y T32:** las referencias del RFC 8446 en el test se actualizaron, pero el changelog no dice en cuántas preguntas. **No se suman.**
- **Detectado en el QA previo a la publicación, y fuera de la tasa:**
  - 3 preguntas del T22 con la letra correcta mal etiquetada (I-419).
  - El bloque P31-P60 del primer borrador del T36, que se salía del alcance del tema (I-525).
  - El reparto sesgado de las respuestas del T13 v1.0 (I-354).

**Preguntas de casos**

- **Elementos revisados (exacta): 1.492 preguntas.**
  - 1.420 son las preguntas tipo test generadas sobre los casos de T2-T40. Se ha contado en `_tools-qa/v3/casos-test/tema-NN.json`: 39 ficheros, 10 preguntas por caso.
  - 72 son las del T1, en 6 casos (`tema-1-changelog.md`, v1.0).
  - El simulacro práctico (30 preguntas) queda fuera.
- **Incidencias detectadas (exacta):** son los registros del Anexo III con ámbito *caso*.
  - Casi todas son discrepancias entre la **solución orientativa** y el contenido aprobado, encontradas al verificar cada pregunta con una cita literal.
  - En 30 de ellas se reformuló la pregunta para que solo hubiera una respuesta válida.
  - La corrección previa a la entrega cerró 12 de los 44 registros pendientes: las 4 preguntas de casos del T1 señaladas por el Equipo IAM (validación técnica) (I-004 a I-006 e I-008), la cuestión 4 del caso 1 del T3 (I-071), el caso 1 del T11 (I-332, I-348) y las soluciones de T5, T7, T10, T19 y T23 con error de gravedad alta (I-133, I-214, I-309, I-400, I-434). Añadió además 4 registros ya corregidos: I-576 (T1, caso 5, P1), I-577 (erratas de los casos del T1), I-579 (T11, matiz de la cuestión 5) e I-581 (T23, `<script>` insertado con innerHTML).
  - La tercera ronda (11-10-2026) cerró los **32 restantes**, ninguno de gravedad alta:
    - **28 corregidos**: las discrepancias entre la solución orientativa y el contenido aprobado de T2, T4, T5, T6, T7, T9, T10, T11, T13, T16, T18-T23, T27, T28, T30, T32, T34 y T37-T39. Donde hacía falta se ajustaron también el contenido (T4 §9; T11 §6.3.1, en I-346 e I-347, que dejan de ser parciales) o la pregunta de casos-test, siempre sin cambiar la letra correcta.
    - **4 no aplicados por criterio** (I-379, I-426, I-463 e I-477): señalan preguntas apoyadas en material complementario; por decisión del adjudicatario se mantiene el alcance aprobado por el Ayuntamiento, porque no son errores de contenido. Cuentan como cerrados.
  - **No queda ninguno abierto.**
- **La tasa es orientativa:** el numerador cuenta discrepancias, que no siempre afectan a una pregunta tipo test.

**Diagramas**

- **Elementos revisados (exacta): 553 ficheros SVG** en `00_Informe_Final/01_Repositorio/temario/**/diagramas/diagrama-*.svg`.
  - Son 121 del bloque administrativo y 432 del técnico.
  - El T11 no aporta SVG a esa carpeta, porque sus diagramas van incrustados en el contenido.
- **Incidencias detectadas (estimada): ≈235**, suma de dos partidas:
  - **≈150 diagramas corregidos en el barrido visual del 06-10-2026.** Es la estimación del registro de sesión («~560 revisados, ~150 corregidos»); no hay recuento diagrama a diagrama.
  - **85 correcciones de diagramas ya publicados registradas fuera de ese barrido** en changelogs e informes. Son 26 registros: diagramas que arrastraban un error de contenido (T5, T6, T9 y T10), defectos señalados por la revisión jurídica o por el validador, y el CSS sin aislar del T5.
  - Las dos partidas pueden solaparse, porque un mismo diagrama pudo corregirse dos veces. Por eso la cifra es un orden de magnitud y no un recuento.
- **Pendientes:** ninguno. Los cuatro que quedaban (I-042, I-047, I-069 e I-386) se corrigieron el 11-10-2026. En esa misma corrección se cerraron los restos de D1 y D12 del T2 (I-039) y de D6 (I-041), y se corrigieron los SVG «BIOS vs UEFI» y UTF-8 del T11 (I-328, I-330), que van incrustados en el contenido. Son diagramas que ya estaban en las partidas de arriba, así que la estimación no cambia.
- **Fuera de la tasa:** el **QA previo a la publicación** corrigió además 323 incidencias de composición en 24 registros. Por ejemplo, 158 en la primera medición de los diagramas del T39 (I-546) y 70 desbordes del T40 (I-557). Cuentan textos, no diagramas.

---

## 6.5 Tipología de errores detectados

Recuento sobre los 582 registros del Anexo III a 11-10-2026 («alta» = gravedad alta; «abiertas» = pendientes más parciales). Ninguna incidencia de gravedad alta queda abierta, y solo una sigue abierta como parcial (I-570, enlaces a las normas). Las 6 no aplicadas por criterio (I-011, I-379, I-426, I-463, I-477 e I-564) son propuestas de alcance, no errores de contenido, y se cuentan como cerradas. Los ejemplos son reales y llevan su ID.

| Tipo | Qué es | Registros | Alta | Abiertas | No aplicadas (criterio) |
|---|---|---|---|---|---|
| Referencia normativa incorrecta | Artículo mal numerado, remisión equivocada o cita «literal» alterada. | 176 | 55 | 0 | 0 |
| Alucinación | Precepto, frase, sentencia o dato inexistente, presentado como si estuviera en la fuente. | 22 | 13 | 0 | 0 |
| Norma derogada o desactualizada | Norma derogada o redacción superada, presentada como vigente. | 22 | 13 | 0 | 0 |
| Dato técnico desactualizado | Estándar o especificación sustituidos por otra edición. | 30 | 4 | 0 | 0 |
| Respuesta marcada incorrecta | La opción dada como correcta no lo es, o la letra estaba mal etiquetada. | 16 | 8 | 0 | 0 |
| Pregunta ambigua (más de una válida) | Más de una opción defendible. Se ve sobre todo al contrastar las soluciones orientativas de los casos con el contenido. | 31 | 0 | 0 | 0 |
| Distractor deficiente | Distractores no verosímiles, preguntas duplicadas o reparto de la respuesta correcta sesgado. | 16 | 0 | 0 | 0 |
| Fuera del programa oficial | Contenido, preguntas o secciones que el enunciado oficial (BOAM 10.032) no pide. | 41 | 0 | 0 | 5 |
| Coherencia entre temas | Remisiones cruzadas erróneas, solapes o incoherencias de formato en la serie. | 35 | 0 | 1 | 1 |
| Diagrama (composición, contraste, flechas) | Texto ilegible o desbordado, flechas mal dirigidas o notación incorrecta. | 86 | 0 | 0 | 0 |
| Ortografía y estilo | Pérdida de diacríticos, etiquetas internas visibles, frases sobre el examen y valoraciones fuera de las cajas. | 107 | 0 | 0 | 0 |
| **Total** | | **582** | **93** | **1** | **6** |

### Ejemplos reales por tipo

**Referencia normativa incorrecta**

- **I-012** · T1 · Contenido §5 (art. 53.1 CE): Se decía que el art. 53.1 CE remite al art. 81 CE; en realidad remite al art. 161.1.a) (recurso de inconstitucionalidad).
- **I-117** · T5 · Contenido (art. 63.d) TREBEP): La separación del servicio como causa de pérdida de la condición se citaba como art. 66; es el art. 63.d).
- **I-233** · T8 · Contenido (art. 31.5 TRLHL): El coste soportado de las contribuciones especiales se citaba en el art. 31.2; está en el art. 31.5.
- **I-200** · T7 · Contenido (art. 126 LPACAP): La inadmisión se citaba como art. 126.2 y el plazo de resolución como 126.1; son el 126.1 y el 126.3.
- **I-222** · T8 · Contenido (ingresos de derecho privado, art. 4 TRLHL): Se afirmaba que el cobro impagado de los ingresos de derecho privado va por apremio «(art. 2.2)»; el art. 4 TRLHL los sujeta a las normas y procedimientos del derecho privado.
- **I-040** · T2 · Contenido §5 y §11, D6 y caso 4 (acceso de Madrid a la autonomía): Vincula la constitución de la Comunidad de Madrid por el art. 144.a directamente con la LO 3/1983; la autorización es la LO 6/1982 y la LO 3/1983 aprueba después el Estatuto.

**Alucinación**

- **I-254** · T9 · Contenido §10.3 (art. 46 TREBEP): Se atribuía al art. 46 TREBEP un preaviso de 48 horas y un plazo de objeciones de 24 horas en unos apartados 46.3-46.5 que no existen (el dato de las 48 h venía de v1.0).
- **I-139** · T6 · Contenido §4 (art. 53.1 LPACAP): El catálogo del art. 53.1 LPACAP incluía una letra inexistente («utilizar las lenguas oficiales»); el artículo tiene nueve letras (a-i).
- **I-297** · T10 · Contenido (medidas LGTBI en empresas): Las medidas en las empresas se atribuían a una «DA 11.ª» de la Ley 4/2023 que no existe; están en el art. 15.
- **I-021** · T1 · Contenido (art. 139.1 CE): Se atribuía a la CE una frase inexistente («por razón de su origen o vecindad»).
- **I-230** · T8 · Contenido (art. 1 TRLHL): Se citaba entre comillas que el TRLHL «tiene por objeto la regulación de la actividad financiera», frase que no está en la ley.
- **I-340** · T11 · Contenido §2.2 (capas de software) y diagrama: Se atribuía a la ISO/IEC 25010 una división del software en cuatro capas (sistema, utilidad, middleware, aplicación), pero la norma define un modelo de calidad del producto, no capas de software (atribución introducida en la v3.0)
- **I-329** · T11 · Test, pregunta 17 y contenido §1.5/§2.3 (calidad del dato e ISO 8000): Atribuye a ISO 8000 «las 4 dimensiones canónicas» de calidad del dato (exactitud, completitud, consistencia, oportunidad); la atribución normativa cerrada no es correcta.

**Norma derogada o desactualizada**

- **I-024** · T1 · Contenido §8, índice, Diagrama D6, Fuentes y Validación (reformas de la CE): El tema hablaba de «tres» reformas de la CE y omitía la cuarta: reforma del art. 69.3 CE de 19 de mayo de 2026 (senador propio de Formentera, BOE núm. 123 de 20-5-2026).
- **I-025** · T1 · Contenido §5.2 (art. 27 CE, ley de desarrollo): Se citaba como ley de desarrollo la LO 6/2001 de Universidades, derogada; la vigente es la LO 2/2023 del Sistema Universitario.
- **I-095** · T4 · Contenido §12 (caja de participación) y caso 6: Se presentaban como vigentes los Foros Locales, derogados por el Reglamento Orgánico 7/2021, de 1 de junio, de los Consejos de Proximidad de los Distritos de Madrid.
- **I-110** · T5 · Contenido (art. 49 TREBEP): Permisos por nacimiento, adopción y del otro progenitor con duración desfasada; la redacción vigente (RDL 9/2025) fija 19 semanas y añade el permiso parental del art. 49.g).
- **I-141** · T6 · Contenido (art. 9.2.c LPACAP): Se describía la «clave concertada» como sistema de identificación del art. 9.2, redacción superada por la vigente letra c) tras el RDL 14/2019 y la Ley 11/2022.
- **I-066** · T3 · Contenido §3.2, D3, caso 1 y test P20, P138, P140 (gerente de distrito): Usa «gerente de distrito» como órgano directivo; en el ROGA vigente (art. 7.3) los órganos directivos de los distritos son los coordinadores de Distrito.
- **I-530** · T37 · Contenido (ICT, Ley 11/2022): Las ICT se atribuían al art. 45 de la derogada Ley 9/2014, como repiten varias fuentes secundarias; el precepto vigente es el art. 55 de la Ley 11/2022 (la disposición adicional tercera remite además al RDL 1/1998)

**Dato técnico desactualizado**

- **I-448** · T25 · Contenido §1.3, «Dato clave» (accesibilidad en ISO/IEC 25010): El «Dato clave» afirmaba que la accesibilidad es una subcaracterística de la usabilidad, lo que es falso con la ISO/IEC 25010:2023: la accesibilidad desaparece como subcaracterística y su contenido lo cubren la inclusividad y la asistencia al usuario, dentro de la capacidad de interacción
- **I-422** · T22 · Fuentes, Contenido §6.1 y Test pregunta 42 (RFC 8446): Se citaba el RFC 8446 (2018) como especificación vigente de TLS 1.3, obsoletado por el RFC 9846 (julio de 2026); el hallazgo se hizo el 20-08-2026 al generar el T35 pero no se propagó hacia atrás hasta el barrido (8 ocurrencias entre .md e index.html)
- **I-423** · T22 · Fuentes, Contenido §6.5 y Test pregunta 52 (RFC 1831): Se citaba el RFC 1831 como especificación de RPC v2, obsoletado por el RFC 5531 (mayo de 2009), con el mismo título y protocolo (4 ocurrencias en .md y 4 en index.html)
- **I-387** · T18 · Fuentes [ISO-C]: Se citaba ISO/IEC 9899:2018 (C17) como norma vigente del lenguaje C; está sustituida por ISO/IEC 9899:2024 (C23, octubre de 2024). Ningún contenido depende de la diferencia
- **I-341** · T11 · Contenido §1.7.8 (tipos SQL) y Fuentes [ISO-9075]: Se presentaba SQL:2016 (ISO/IEC 9075:2016) como estándar SQL de referencia, anulado y sustituido por SQL:2023 (ISO/IEC 9075:2023)

**Respuesta marcada incorrecta**

- **I-419** · T22 · Test (3 preguntas): Durante la redacción manual del test, 3 preguntas tenían mal etiquetada la letra de la respuesta correcta; lo detectó el script de verificación y rebalanceo antes de publicar
- **I-330** · T11 · Test, pregunta 23 (UTF-8 y BMP): Da «3 bytes» como respuesta para cualquier carácter del BMP; en UTF-8 un carácter del BMP ocupa 1, 2 o 3 bytes (3 solo en U+0800-U+FFFF).
- **I-005** · T1 · Caso 3, pregunta 14 (protección de datos): La respuesta correcta presenta la protección de datos como integrada en el derecho a la intimidad; es un derecho fundamental autónomo con fundamento en el art. 18.4 CE.
- **I-214** · T7 · Caso 3, cuestión 3 (doble silencio, art. 24.1 LPACAP): La solución da por estimatorio el silencio de la alzada en una solicitud de autorización de uso común especial de la vía pública, que la propia cuestión 1 encaja en la excepción del dominio público; según el contenido aprobado (§5.3) el silencio sería desestimatorio.
- **I-400** · T19 · Caso 2, cuestión 3 (contador del cursor): El pseudocódigo de la solución pone «p_num_bonificados = 0» dentro del cuerpo del bucle, de modo que el contador se reinicia en cada iteración y el parámetro OUT devolvería siempre 1 o 0; la inicialización debe ir antes de abrir el cursor.

**Pregunta ambigua (más de una válida)**

- **I-352** · T12 · Caso 3, cuestión 1 (RAID): La solución propone RAID 5, 6 o 10 y no menciona RAID 1, que según el contenido (§5.6) también tolera el fallo de un disco: una pregunta en positivo tendría dos opciones defendibles.
- **I-135** · T5 · Caso 1, cuestión 2 (art. 10.1 TREBEP): El «proyecto temporal de digitalización» del supuesto encaja también en el interino por programas temporales (art. 10.1.c), pero la solución lo encuadra solo en exceso o acumulación de tareas (art. 10.1.d): dos respuestas defendibles.

**Distractor deficiente**

- **I-155** · T6 · Test (banco de 160): Preguntas no basadas en el texto literal del precepto citado y con distractores no ajustados; las 160 se reescriben con distractores que son variaciones leves.
- **I-242** · T8 · Test (banco de 150): referencia corregida P79, 88, 108 y 145; enunciado ajustado P66: Preguntas de supuestos de aplicación, de opinión, de doctrina o con datos erróneos: 50 reescritas al texto literal, 4 con la referencia corregida y 1 con el enunciado ajustado; respuestas correctas concentradas en la a) (102 de 150).
- **I-009** · T1 · Test, preguntas 11/68, 12/70, 13/69 y 14/71: Cuatro parejas de preguntas duplicadas o casi literales (libertad de expresión, reunión, asociación, educación) que evalúan el mismo conocimiento.
- **I-354** · T13 · Test (60 preguntas): Distribución de la opción correcta sesgada hacia la B (A=16, B=37, C=7)

**Fuera del programa oficial**

- **I-167** · T7 · Contenido §3.4 (buena administración): Epígrafe sobre la buena administración como principio transversal basado en la Carta de Derechos Fundamentales de la UE, fuera del enunciado del temario.
- **I-252** · T9 · Contenido §7.2 (disciplinas preventivas): Epígrafe sobre las cuatro disciplinas preventivas, la formación y las auditorías (RSP), añadido en v1.1, retirado por la revisión jurídica (el changelog no indica el motivo).
- **I-385** · T18 · Contenido §7 (Tendencias actuales): El apartado final no figura en el enunciado oficial del tema y se presentaba sin distinguirlo de la materia exigible (criterio de literalidad del título fijado el 02-09-2026)

**Coherencia entre temas**

- **I-315** · T11 · Contenido §1.7.7 (referencia cruzada TAD): Remitía al «Tema 27 (Estructuras de datos y algoritmos)»; los TAD están en el Tema 13 (Tipos abstractos y Estructuras de datos)
- **I-176** · T7 · Diagrama D1: El diagrama sugería que la Ley 40/2015 se estudia en el Tema 7.

**Diagrama (composición, contraste, flechas)**

- **I-375** · T16 · Diagrama D1 (CSS de los SVG): Los estilos de los diagramas no estaban aislados: la caja «FÍSICO» del D1 tenía el texto oscuro sobre fondo oscuro
- **I-406** · T20 · Diagrama D11 (notación de relaciones UML): La composición y la agregación se dibujaban con puntas de flecha en lugar de rombos, contra la notación UML
- **I-431** · T23 · Diagrama D1: La flecha verde de D1 tenía la punta al revés
- **I-553** · T40 · Diagrama D12: STUN y TURN aparecían en la misma fila entre los dos NAT, con lo que se leía que están en el camino del media, lo contrario de lo que dice el texto (detectado en la captura con el QA en verde)

**Ortografía y estilo**

- **I-002** · T1 · Todos los ficheros (README, test, casos, diagramas, validación, contenido, fuentes, índice, changelog, index.html): Pérdida sistemática de tildes y ñ en 6 de 10 ficheros (régimen sin diacríticos): ~1.300 tildes, ~110 ñ y 5 errores léxicos («aprueble», «cine al», «cenirte», «se ampliar», «senalen»); el HTML hereda el texto sin tildes.
- **I-003** · T1 · Contenido, test, casos, diagramas, Validación y Fuentes (ortografía): Pérdida de diacríticos (tildes y ñ) repartida por todo el tema, sobre todo en el contenido embebido del HTML (banco, casos, diagramas, pestañas).
- **I-313** · T11 · Todos los ficheros (contenido, test, casos, diagramas, validación, index.html): Falta sistemática de tildes y ñ en casi todos los ficheros: ≈1.080 tildes, ≈45 ñ, ≈30 signos de puntuación (¿ ausente en las preguntas), ≈5 de concordancia y ≈80 de otros tipos.
- **I-343** · T11 · Test, preguntas 16-25: Diez enunciados del test mostraban la etiqueta interna «[v2]» (detectado en la revisión de la plataforma por el Ayuntamiento el 09-10-2026)

### Patrones que explican los errores

- **Las citas «literales» salen alteradas, aunque la norma esté vigente.** Comprobar la vigencia no basta. En los 10 temas jurídicos había artículos con la numeración desplazada (31.2 por 31.5, 87.3 por 87.2, 66 por 63.d), apartados inventados y frases entrecomilladas que no están en la norma. La medida fue cotejar cada precepto con el texto consolidado del BOE.
- **Las fuentes secundarias propagan denominaciones antiguas.** Las ICT se atribuían a la derogada Ley 9/2014 (I-530) y se usaban nombres del RD 3/2010 en las medidas del ENS (I-512, I-487). La fuente válida es la oficial, no la que más se repite.
- **Las correcciones no se propagaban a los temas ya publicados.** El caso del RFC 9846 se describe en III.2. La regla actual es buscar el mismo error en los 40 temas en la misma sesión.
- **El QA automático da falsos OK en los diagramas.** `getBBox` comprueba la composición, pero no el contraste, la dirección de las flechas ni si un rótulo cuadra con lo que encabeza. La revisión de las capturas es obligatoria.
- **El QA dentro de cada tema no ve las incoherencias entre temas.** Las detectó el Equipo IAM (validación técnica) el 08-09-2026, y se resolvieron con la plantilla común de la plataforma V3.

---

## Ciclo de versiones por tema

Lo que sigue sale del changelog de cada tema. La versión final es la publicada a 11-10-2026. Las correcciones previas a la entrega (tres rondas, 11-10-2026) y el enlazado de las Fuentes no figuran en esta tabla: el Anexo III las registra con la versión «entrega 2026-10-16». Los saltos de versión menores (v1.x) incluyen cambios que no corrigen errores, como la ficha de extensión y el tiempo de estudio (v1.1/v2.2 del 06-09-2026).

| Tema | Versión inicial | Versión final | Nº de versiones | Preguntas del banco | Hitos |
|---|---|---|---|---|---|
| T1 | v1.0 (23-04-2026) | v2.5 (06-10-2026) | 7 | 150 | Ampliación de derechos (v2.0); ortografía, 489 diacríticos (v2.1); ficha de estudio (v2.2); revisión jurídica y cotejo BOE, 4.ª reforma (v2.3); diagramas (v2.4); citas (v2.5). |
| T2 | v1.0 (15-06-2026) | v1.5 (06-10-2026) | 6 | 150 | Nuevo diagrama D13 a petición de la Equipo eTrivium · Dirección de calidad formativa (v1.1); ficha (v1.2); revisión jurídica y correcciones de fondo (v1.3); diagramas (v1.4); citas (v1.5). |
| T3 | v1.0 (15-06-2026) | v1.4 (06-10-2026) | 5 | 150 | Ficha (v1.1); revisión jurídica contra ROGA consolidado: coordinadores de Distrito, art. 8, 22 preguntas sustituidas (v1.2); diagramas (v1.3); citas (v1.4). |
| T4 | v1.0 (15-06-2026) | v1.4 (06-10-2026) | 5 | 150 | Ficha (v1.1); revisión jurídica: Foros Locales derogados, BOE Ley 22/2006, 36 preguntas reescritas (v1.2); diagramas (v1.3); citas (v1.4). |
| T5 | v1.0 (20-06-2026) | v1.6 (06-10-2026) | 7 | 150 | Correcciones de la Equipo eTrivium · Dirección de calidad formativa y diagramas (v1.1); CSS de SVG aislado (v1.2); ficha (v1.3); cotejo TREBEP, 19 semanas, 69 preguntas (v1.4); diagramas (v1.5); citas (v1.6). |
| T6 | v1.0 (25-06-2026) | v1.5 (06-10-2026) | 6 | 160 | Generación; ampliación pedida por la Equipo eTrivium · Dirección de calidad formativa (art. 53, archivo, lobbies, +10 preguntas); ficha de estudio; revisión jurídica y cotejo BOE (test reescrito); diagramas; convención de citas. |
| T7 | v1.0 (25-06-2026) | v1.4 (06-10-2026) | 5 | 150 | Generación (publicada 30-06); ficha de estudio; revisión jurídica y cotejo BOE con ~27 preceptos corregidos y 139 preguntas tocadas; diagramas; art. 34.2, D1 y citas. |
| T8 | v1.0 (25-06-2026) | v1.5 (06-10-2026) | 6 | 150 | Generación con auditoría de cifras; supuestos de tasas y gestión ATM; ficha; revisión jurídica (16 correcciones de fondo); diagramas; ejemplo de precio público y citas. |
| T9 | v1.0 (25-06-2026) | v1.5 (06-10-2026) | 6 | 165 | Generación; ampliación de profundidad (150→165 preguntas); ficha; revisión jurídica (art. 46 TREBEP inventado, Acuerdo-Convenio, 117 preguntas); diagramas; citas. |
| T10 | v1.0 (25-06-2026) | v1.4 (06-10-2026) | 5 | 150 | Generación con III Plan verificado; ficha; revisión jurídica (LOIEMH, Ley 4/2023 con preceptos inexistentes, 76 preguntas reescritas); diagramas; citas. |
| T11 | v1.0 (16-04-2026) | v3.6 (09-10-2026) | 9 | 25 | v2.0 y v3.0 ampliaciones tras la revisión de la Equipo eTrivium · Dirección de calidad formativa; v3.1 IAM (11 refs cruzadas, contraste SVG); v3.2 ñ; v3.4 ISO 25010:2023; v3.5 capas/SQL:2023 y diagramas; v3.6 test |
| T12 | v1.0 (02-07-2026) | v1.3 (06-10-2026) | 4 | 60 | v1.0 generación; v1.1 ficha de estudio; v1.2 correcciones comunes; v1.3 barrido de diagramas |
| T13 | v1.0 (11-06-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación (test sesgado a B); v1.1 feedback IAM (índice, notación, listas); v1.2 ficha; v1.3 correcciones comunes; v1.4 CSS SVG y diagramas |
| T14 | v1.0 (11-06-2026) | v1.4 (06-10-2026) | 4 | 60 | v1.0 generación; v1.2 ficha (no consta v1.1); v1.3 correcciones comunes; v1.4 CSS SVG y barrido de diagramas |
| T15 | v1.0 (11-06-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 pestaña Índice; v1.2 ficha; v1.3 correcciones comunes; v1.4 CSS SVG, D1/D5 y diagramas |
| T16 | v1.0 (20-06-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 literalidad del título (5→8 secciones, DTE complementario); v1.3 correcciones comunes; v1.4 CSS SVG y diagramas |
| T17 | v1.0 (20-06-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 literalidad del título (2→4 secciones); v1.3 correcciones comunes; v1.4 CSS SVG, D4 y diagramas |
| T18 | v1.0 (06-07-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 apartado complementario; v1.3 C17→C23, ISO 25010:2023 y correcciones comunes; v1.4 diagramas |
| T19 | v1.0 (13-07-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 apartado complementario; v1.3 ISO 25010:2023 y correcciones comunes; v1.4 diagramas |
| T20 | v1.0 (13-07-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 apartado complementario; v1.3 ISO 25010:2023 y correcciones comunes; v1.4 D11 UML y diagramas |
| T21 | v1.0 (13-07-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 conversor Markdown y apartado complementario (dos entradas v1.2); v1.3 ISO 25010:2023 y correcciones comunes; v1.4 barrido de diagramas |
| T22 | v1.0 (21-07-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 apartado complementario; v1.3 RFC 8446→9846, RFC 1831→5531 y correcciones comunes; v1.4 barrido de diagramas |
| T23 | v1.0 (21-07-2026) | v1.4 (09-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 RFC 8446→9846 y correcciones comunes; v1.3 barrido de diagramas (D1); v1.4 pregunta 43 (revisión del Ayto) |
| T24 | v1.0 (17-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 conversor Markdown; v1.3 RFC 8446→9846, ISO 25010:2023 y correcciones comunes; v1.4 barrido de diagramas |
| T25 | v1.0 (20-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 literalidad (3→4 secciones); v1.3 ISO 25010:2023/25019, RFC 9846 y correcciones comunes; v1.4 diagramas |
| T26 | v1.0 (20-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 apartado complementario; v1.3 correcciones comunes; v1.4 barrido de diagramas |
| T27 | v1.0 (20-08-2026) | v1.3 (06-10-2026) | 4 | 60 | v1.0 generación; v1.1 ficha; v1.2 ISO 25010:2023 y correcciones comunes; v1.3 barrido de diagramas |
| T28 | v1.0 (20-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 apartado complementario; v1.3 correcciones comunes; v1.4 barrido de diagramas |
| T29 | v1.0 (20-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 apartado complementario; v1.3 RFC 8446→9846 y correcciones comunes; v1.4 barrido de diagramas |
| T30 | v1.0 (27-08-2026) | v1.3 (06-10-2026) | 4 | 60 | v1.0 generación; v1.1 ficha (condición del IAM al validar el T30); v1.2 correcciones comunes; v1.3 barrido de diagramas |
| T31 | v1.0 (26-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha; v1.2 apartado complementario; v1.3 RFC 8446→9846 y correcciones comunes; v1.4 barrido de diagramas |
| T32 | v1.0 (27-08-2026) | v1.3 (06-10-2026) | 4 | 60 | v1.0 generación (D2 truncado, corregido el mismo día); v1.1 ficha; v1.2 RFC 8446→9846 y correcciones comunes; v1.3 barrido de diagramas |
| T33 | v1.0 (27-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha de extensión; v1.2 apartado complementario marcado; v1.3 normas vigentes y correcciones comunes; v1.4 barrido de diagramas |
| T34 | v1.0 (27-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha de extensión; v1.2 apartado complementario marcado; v1.3 normas vigentes y correcciones comunes; v1.4 barrido de diagramas |
| T35 | v1.0 (27-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha de extensión; v1.2 apartado complementario marcado; v1.3 normas vigentes y correcciones comunes; v1.4 barrido de diagramas |
| T36 | v1.0 (27-08-2026) | v1.3 (06-10-2026) | 4 | 60 | v1.0 generación; v1.1 ficha de extensión; v1.2 normas vigentes y correcciones comunes; v1.3 barrido de diagramas |
| T37 | v1.0 (27-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha de extensión; v1.2 apartado complementario marcado; v1.3 normas vigentes y correcciones comunes; v1.4 barrido de diagramas |
| T38 | v1.0 (27-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha de extensión; v1.2 apartado complementario marcado; v1.3 normas vigentes y correcciones comunes; v1.4 barrido de diagramas |
| T39 | v1.0 (27-08-2026) | v1.3 (06-10-2026) | 4 | 60 | v1.0 generación; v1.1 ficha de extensión; v1.2 normas vigentes y correcciones comunes; v1.3 barrido de diagramas |
| T40 | v1.0 (27-08-2026) | v1.4 (06-10-2026) | 5 | 60 | v1.0 generación; v1.1 ficha de extensión; v1.2 apartado complementario marcado; v1.3 normas vigentes y correcciones comunes; v1.4 barrido de diagramas |

**Resumen del ciclo:**

- Los 40 temas parten de una versión v1.0. El T11 (piloto, 16-04-2026) llegó a la v3.6 tras 9 versiones, y el T1 a la v2.5 tras 7.
- El resto termina entre la v1.3 y la v1.6.
- En total, 205 versiones registradas en los changelogs, 165 de ellas posteriores a la v1.0, con una media de 5,1 versiones por tema.
- Todos los temas subieron de versión en las dos tandas de octubre: la revisión jurídica, las normas caducadas y las correcciones comunes (01/02-10), y el barrido visual de diagramas (06-10).
