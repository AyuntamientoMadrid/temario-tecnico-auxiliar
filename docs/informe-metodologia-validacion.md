# Informe de Metodología y Validación

**Contrato:** Elaboración y publicación de material formativo de oposiciones de tecnología del Ayuntamiento de Madrid
**Expediente:** 300/2026/00147
**Órgano de contratación:** Gerencia del Organismo Autónomo Informática del Ayuntamiento de Madrid (IAM)
**Responsable del contrato:** Miguel Ángel Rodríguez Ramos, Subdirector General de Sistemas y Tecnología
**Adjudicatario:** Etrivium Learn, S.L. · NIF B09800814 · Plaza de la Cebada, 14, 2.º D, 28005 Madrid
**Fecha de inicio:** 16/03/2026
**Fecha de finalización:** 16/10/2026
**Versión del documento:** 1.0
**Fecha:** 15/10/2026

---

## Índice

1. Introducción
2. Resumen de entregables
3. Herramientas de IA utilizadas
4. Metodología por fases
5. Prompts y flujos de trabajo de IA
6. Procedimiento de verificación humana
7. Cumplimiento normativo y requisitos de IA (MAIA)
8. Propiedad intelectual y transferencia de conocimiento
9. Conclusiones
- Anexo I. Inventario de fuentes utilizadas
- Anexo II. Catálogo de prompts (y documento complementario «Flujo de trabajo con IA»)
- Anexo III. Registro de incidencias detectadas en la validación

---

## 1. Introducción

### 1.1 Objeto

Este informe da cumplimiento al apartado 3 del Informe de condiciones técnicas y administrativas del expediente 300/2026/00147. Describe la metodología seguida para elaborar y publicar el material formativo destinado a preparar la oposición de **Técnicos Auxiliares de Tecnologías de la Información y Comunicaciones (Grupo C1)** del Ayuntamiento de Madrid, según el programa publicado en el BOAM n.º 10.032, de 23 de diciembre de 2025.

### 1.2 Alcance

El trabajo ha comprendido:

- El temario teórico de los 40 temas del programa: 10 del bloque administrativo y 30 del bloque técnico.
- Las baterías de preguntas tipo test de cada tema, los casos prácticos con sus preguntas tipo test y un simulacro de la parte práctica.
- La plataforma web interactiva de estudio y autoevaluación: estática, sin servidor y con autocorrección.
- La publicación en el repositorio del Ayuntamiento de Madrid en GitHub, con despliegue en GitHub Pages.

### 1.3 Contenido del informe

Conforme a lo exigido en el contrato, el informe recoge:

- Los prompts y flujos de trabajo de IA utilizados para generar el material (apartado 5 y Anexo II).
- El procedimiento de verificación humana aplicado para garantizar la ausencia de errores y de «alucinaciones» (apartado 6 y Anexo III).
- El inventario de fuentes utilizadas (Anexo I).

Los anexos se entregan también en formato CSV, para poder filtrarlos y reutilizarlos.

---

## 2. Resumen de entregables

### 2.1 Repositorio

| Elemento | Valor |
|---|---|
| URL del repositorio | <https://github.com/AyuntamientoMadrid/temario-tecnico-auxiliar> |
| URL de publicación (GitHub Pages) | <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/> |
| Licencia aplicada | CC0 1.0 Universal, determinada por el IAM al crear el repositorio |
| Fecha de la última publicación | `[PENDIENTE: fecha del despliegue verificado]` |

### 2.2 Estructura del repositorio

```
/
├── README.md                     Descripción, cifras, formatos, licencias y contacto
├── LICENSE                       CC0 1.0 Universal (determinada por el IAM)
├── index.html                    Web: portada, temario, exámenes, simulacros, progreso
├── temas/tema-01 … tema-40.html  Web: página de cada tema
├── assets/                       CSS, JavaScript, imágenes y banco de preguntas (JSON)
├── temario/
│   ├── administrativo/tema-01 … tema-10/   tema-NN.md · tema-NN.pdf · diagramas/*.svg
│   └── tecnico/tema-11 … tema-40/          tema-NN.md · tema-NN.pdf · diagramas/*.svg
├── tests/
│   ├── administrativo/tema-NN.{json,md}    Banco del tema + preguntas de sus casos
│   ├── tecnico/tema-NN.{json,md}
│   └── simulacro-practico.{json,md}
├── herramientas/                 Scripts y datos para regenerar web, Markdown y PDF
├── docs/
│   ├── mantenimiento.md          Guía de mantenimiento y actualización
│   └── informe-metodologia-validacion.md   Este informe
└── .github/workflows/pages.yml   Despliegue automático en GitHub Pages
```

### 2.3 Cifras del material

| Bloque | Nº de temas | Preguntas tipo test (banco) | Casos prácticos | Preguntas sobre los casos | Diagramas | Formatos |
|---|---|---|---|---|---|---|
| Administrativo | 10 | 1.525 | 60 | 612 | 121 | Web / Markdown / PDF / JSON |
| Técnico | 30 | 1.765 | 88 | 880 | 432 | Web / Markdown / PDF / JSON |
| **Total** | **40** | **3.290** | **148** | **1.492** | **553** | |

A esto se suma un **simulacro de la parte práctica**: un supuesto y 30 preguntas tipo test con el formato del examen de 21 de junio de 2025. La web permite además generar **simulacros teóricos** de 90 preguntas aleatorias que cubren los 40 temas y un **examen por tema**.

Las 1.525 preguntas del bloque administrativo citan su base legal. En 1.415 se cita el artículo. En las 110 restantes la pregunta trata de la estructura de la norma (título o capítulo), de una de sus disposiciones (adicional, transitoria, derogatoria o final), de su exposición de motivos o fecha, o de un instrumento no articulado (Plan de Igualdad, organigrama municipal, sentencia del Tribunal Constitucional), y la referencia cita ese precepto o documento.

---

## 3. Herramientas de IA utilizadas

| Herramienta / modelo | Proveedor | Versión | Tipo de licencia | Uso en el proyecto |
|---|---|---|---|---|
| Claude, mediante Claude Code (asistente que trabaja sobre los ficheros del proyecto) y subagentes | Anthropic | Familia Claude Opus 4 (Opus 4.7 en la fase final) durante la generación y revisión (marzo-octubre de 2026); Claude Opus 5.5 en las correcciones previas a la entrega (octubre de 2026) | Suscripción Team del adjudicatario | Herramienta principal: registro de fuentes, redacción de los 40 temas, bancos de test, casos, diagramas SVG, generación del código web, scripts de QA, revisiones transversales (cotejo con el BOE, normas caducadas, diagramas) y preguntas de los casos y el simulacro |
| ChatGPT | OpenAI | Modelos vigentes en 2026 | Licencia propia del adjudicatario | Contraste de normativa; validación y revisión de contenidos; generación de la imagen de portada de la web |
| Copilot | Microsoft | Versión vigente en 2026 | Licencia propia del adjudicatario | Contraste de normativa; validación y revisión de contenidos |
| Gemini | Google | Versión vigente en 2026 | Licencia propia del adjudicatario | Contraste de normativa; validación y revisión de contenidos |

**Criterio de selección.**

- **Claude Code** se eligió como herramienta principal porque trabaja directamente sobre los ficheros del proyecto. Puede leer los textos oficiales descargados, escribir los ficheros de cada tema, ejecutar los scripts de comprobación y repetir el ciclo hasta que el QA pasa. Así cada afirmación queda trazada a una fuente registrada y cada corrección se aplica de forma uniforme en todos los temas afectados.
- La herramienta no decide qué se publica: el criterio de publicación es la aprobación del IAM (apartado 6).
- **ChatGPT, Copilot y Gemini** se usaron como **verificadores cruzados**, no como generadores del temario. Contrastar una misma afirmación normativa o técnica con modelos de proveedores distintos, entrenados de forma independiente, ayuda a detectar errores que un único modelo tiende a repetir. Ninguna divergencia entre modelos se resolvió por mayoría: se resolvió acudiendo a la fuente oficial (BOE, estándar o documentación primaria), que es el criterio del apartado 6.

**Sostenibilidad económica.**

- Las licencias y suscripciones de IA las ha aportado el adjudicatario, como prevé el pliego, sin coste para el Ayuntamiento.
- **El material publicado no depende de ningún servicio de IA para funcionar ni para mantenerse.** La web es HTML, CSS y JavaScript estáticos servidos por GitHub Pages.
- Las herramientas de regeneración (`herramientas/`) son scripts de Python de código abierto, con dependencias gratuitas: BeautifulSoup, pandoc y Playwright.
- Cualquier actualización futura puede hacerse a mano, editando los ficheros de datos (apartado 8.2), sin licencias de pago.

---

## 4. Metodología por fases

El flujo completo, con su diagrama, se describe en el documento complementario **«Flujo de trabajo con IA»** (entregado al IAM junto con el Anexo II). Sus fases son las del pliego.

### Fase 1. Identificación y recopilación de fuentes

- **Temario oficial:** programa de la convocatoria de Técnico/a Auxiliar TIC (C1), BOAM n.º 10.032, de 23 de diciembre de 2025, y bases específicas. Los 40 enunciados oficiales se reproducen literalmente al inicio de cada tema y sirven de referencia para comprobar su cobertura («literalidad del título»).
- **Fuentes del bloque administrativo:**
  - Texto consolidado del BOE de la Constitución y de las leyes del programa.
  - Normativa autonómica (BOCM) y municipal (BOAM), entre ella el Reglamento Orgánico del Gobierno y de la Administración del Ayuntamiento de Madrid (2004), los decretos de organización de las Áreas de Gobierno, la Ordenanza de Transparencia, el Acuerdo-Convenio y el Plan de Igualdad.
  - Son 56 fuentes normativas (Anexo I.1) y 23 documentos del Ayuntamiento (Anexo I.4).
- **Fuentes del bloque técnico:** 879 fuentes (Anexo I.2), entre ellas:
  - normas ISO/IEC y UNE-EN (57);
  - RFC de la IETF (154);
  - especificaciones de consorcios (W3C, IEEE, ETSI…; 83);
  - Esquema Nacional de Seguridad y guías CCN-STIC;
  - Esquema Nacional de Interoperabilidad;
  - documentación oficial de fabricantes (194);
  - manuales de referencia de la disciplina (71).
- **Exámenes anteriores** (Anexo I.3): examen teórico y práctico de Técnico/a Auxiliar TIC (C1) del Ayuntamiento de Madrid de 21 de junio de 2025, con sus plantillas correctoras, y seis supuestos prácticos de referencia. Se usaron como modelo de formato (tres opciones, supuesto de unas 200 palabras con 30 preguntas), de estilo y de nivel. El análisis del examen está en el prompt P-02 del Anexo II.
- **Criterios de fiabilidad de las fuentes:** cada tema tiene un registro de fuentes de tres niveles (Anexo I.5):
  - **Tier 1 · canónica:** texto oficial, estándar o manual de referencia. Todo dato examinable debe poder reconducirse a ella.
  - **Tier 2 · complementaria:** documentación de fabricantes, guías e informes.
  - **Tier 3 · contexto.**
  - **Descartadas:** enciclopedias colaborativas, blogs, foros, academias, contenido generado por IA sin fuente y material comercial. Se registran para que la validación pueda comprobar el criterio.

  En los 40 temas hay 1.003 usos de fuentes Tier 1, 330 de Tier 2, 98 de Tier 3 y 62 entradas descartadas. Ningún tema carece de fuentes Tier 1.

### Fase 2. Generación de contenidos teóricos

- **Proceso:**
  - Cada tema se generó como un conjunto de nueve ficheros Markdown: índice, fuentes, contenido, diagramas, test, casos prácticos, validación y registro de cambios.
  - La página web del tema se ensambló a partir de esos ficheros con un script, nunca a mano.
  - La IA plantea antes de redactar las decisiones de alcance (secciones fuera del esqueleto oficial, contexto de los casos) como preguntas cerradas, y las decide la persona responsable.
  - Los prompts de esta fase son P-03 a P-08 del Anexo II.
- **Trazabilidad con la normativa vigente:**
  - Cada afirmación del contenido cita en línea el identificador de su fuente registrada; por ejemplo, `[LPACAP]` o `[RD1112-2018]`.
  - En el bloque administrativo se cita además el artículo. Se sigue la convención fijada por la revisión jurídica: sin paréntesis cuando el artículo forma parte de la oración («Conforme al artículo 130.3 LBRL…»), entre paréntesis cuando es un inciso de apoyo («… a la Junta de Gobierno (art. 8 ROGA)»).
  - Las citas se cotejaron precepto a precepto con el texto consolidado del BOE (apartado 6).
- **Actualización tecnológica:**
  - Cada estándar se cita con su edición vigente, comprobada en la fuente primaria.
  - Cuando una norma ha sido sustituida, el registro de fuentes muestra dos filas, la vigente y la histórica. Ejemplos: ISO/IEC 25010:2011 → 2023, RFC 8446 → RFC 9846 (julio de 2026) y SQL:2016 → SQL:2023.
  - Un cambio detectado en un tema se busca en toda la serie el mismo día. Esta regla se adoptó cuando una actualización del RFC de TLS 1.3 se aplicó primero en un solo tema; está descrita en el apartado 5.10 del documento de flujo.

### Fase 3. Generación de baterías de test

- **Preguntas administrativas:**
  - Generación asistida con referencia al artículo o precepto correspondiente (P-09).
  - Tras la revisión jurídica, toda pregunta sale del **texto literal de la norma**, sin supuestos de aplicación, doctrina ni interpretación.
  - Los distractores son variaciones verosímiles del literal.
  - 150 a 165 preguntas por tema.
- **Preguntas técnicas:**
  - 60 por tema (25 en el tema 11), con cobertura proporcional a las secciones del tema (P-10).
  - Son de nueva generación a partir del contenido aprobado. Los exámenes anteriores se usaron como patrón de formato, nivel y estilo, no como fuente de preguntas reutilizadas.
- **Preguntas sobre los casos prácticos y simulacro práctico:**
  - Unas 10 preguntas tipo test por caso: 1.420 en los temas 2-40, más las 72 originales del tema 1.
  - Un supuesto con 30 preguntas para el simulacro (P-11 y P-12).
  - Cada pregunta se verificó con una cita literal del contenido aprobado. La verificación de cada tema queda documentada en una tabla de respaldo.
- **Criterios de calidad:**
  - Tres opciones y una sola correcta.
  - Distractores plausibles.
  - Sin ambigüedades ni duplicados.
  - Respuesta correcta repartida de forma equilibrada entre a, b y c. Se mide con un script en cada generación, porque al redactar de corrido la IA tiende a concentrar la respuesta correcta en una letra (apartado 5.7 del documento de flujo).

### Fase 4. Desarrollo del material web interactivo

- **Tecnologías:** HTML, CSS y JavaScript, con arquitectura estática sin servidor ni base de datos y sin dependencias externas de ejecución.
- **Funcionalidades:**
  - Autocorrección de cada test, con contador de aciertos, fallos y preguntas en blanco.
  - Nota calculada como en las bases (+1 por acierto, −1/3 por error, 0 en blanco, sobre 10).
  - Examen por tema, simulacros teóricos de 90 preguntas aleatorias y simulacro práctico.
  - Pausar y reanudar.
  - Revisión de las respuestas con su explicación y su referencia.
  - Seguimiento del avance por epígrafe, guardado solo en el navegador del usuario (`localStorage`), sin registro ni datos personales.
  - Impresión o PDF de cada tema con el avance.
  - Menú plegable.
- **Accesibilidad:**
  - Objetivo de conformidad: WCAG 2.1 AA.
  - Prueba automática con axe-core 4.10.2 (reglas WCAG 2.0 y 2.1, niveles A y AA) sobre las 44 páginas: portada, pantallas de la aplicación y 40 temas. **Las 44 páginas no presentan incidencias** (evidencia conservada por el adjudicatario).
  - Diagramas con `role="img"` y texto alternativo.
  - Navegación por teclado y enlace para saltar al contenido.
  - Contraste del texto sobre la imagen de portada medido (≥ 4,5:1).
  - La declaración de accesibilidad es la de los procesos selectivos TIC del Ayuntamiento.
- **Diseño responsivo:**
  - Comprobado de forma automática en los 40 temas a 390 px de ancho (sin desbordes horizontales) y en escritorio (1.280 px), con Chromium.
  - Prueba automatizada en los tres motores de navegador del mercado (Chromium, base de Chrome y Edge; WebKit, base de Safari; y Firefox), a 390 px con emulación móvil y táctil y a 1.280 px: 45 páginas sin desbordes ni errores de JavaScript y examen de tema operativo (evidencia conservada por el adjudicatario).
- **Uso de asistentes de código IA:**
  - El código se generó con Claude Code (P-13 a P-15).
  - Se revisó con pruebas funcionales automatizadas (Playwright): avance y persistencia, nota con penalización, casos, examen de tema, simulacros, impresión y ausencia de errores de JavaScript.
  - El código no carga scripts de terceros salvo la analítica institucional Siteimprove del Ayuntamiento.

### Fase 5. Publicación y despliegue

- **Estructuración del repositorio:** un único repositorio, `AyuntamientoMadrid/temario-tecnico-auxiliar`, con la web en la raíz y el temario, los tests, las herramientas y la documentación en carpetas propias (apartado 2.2).
- **Licencia:** CC0 1.0 Universal para todo el contenido y el código, según lo determinado por el IAM en el repositorio de la organización. Quedan fuera el escudo y el logotipo municipales: CC0 no afecta a los derechos de marca.
- **Verificación del despliegue:** `[PENDIENTE: fecha y resultado]`. Procedimiento:
  - publicación mediante GitHub Actions;
  - comprobación HTTP 200 de todas las páginas;
  - comparación byte a byte de los ficheros publicados con los del repositorio;
  - ausencia de errores de JavaScript;
  - prueba funcional sobre la URL pública.

  Este procedimiento se aplicó en cada publicación previa del proyecto.

---

## 5. Prompts y flujos de trabajo de IA

### 5.1 Flujo general

```
Material de partida (BOAM 10.032, esqueletos del IAM, examen 2025)
  → Fuentes oficiales registradas (Tier 1/2/3) y vigencia comprobada
  → Decisiones de alcance (persona responsable)
  → Generación asistida (9 ficheros por tema)
  → QA automatizado (si falla, se vuelve a generar)
  → Publicación de trabajo v1.0 «Pendiente de validación»
  → Revisión humana (checklist, prompt maestro, revisión jurídica, revisión técnica del IAM)
  → Corrección quirúrgica + subida de versión + registro de cambios + propagación a toda la serie
  → Validación del IAM (aprobación de los 40 temas, octubre de 2026)
  → Plataforma con el contenido aprobado → publicación → verificación en vivo
```

El detalle de cada etapa, de las herramientas de QA automatizado y de lo que el QA no ve está en el documento complementario **«Flujo de trabajo con IA»** (entregado al IAM junto con el Anexo II), apartados 2 a 4.

### 5.2 Prompts representativos

El Anexo II recoge 20 prompts (P-01 a P-20) agrupados por fase.

- **Ocho son literales**: se conservan en ficheros de trabajo o en el registro de sesiones de la herramienta, sobre todo los encargos de octubre de 2026. Se citan indicando la herramienta y la fecha de la sesión.
- **Doce están reconstruidos** a partir de las plantillas, los scripts y las cabeceras normalizadas de los ficheros generados. De la fase de generación de los temas (abril-agosto de 2026) no se conservan las transcripciones.

Cada prompt indica su naturaleza y su fichero de origen.

#### 5.2.1 Síntesis de normativa (bloque administrativo)

- **Herramienta:** Claude Code.
- **Entrada:** texto consolidado de la norma (BOE, BOCM o BOAM), enunciado oficial del tema e índice o esqueleto facilitado por el IAM.
- **Prompt:** P-03 (reconstruido) del Anexo II. La revisión posterior es P-18 (literal): revisión jurídica de T1-T10 y cotejo precepto a precepto con el BOE.
- **Resultado esperado y observaciones:**
  - Tema que sigue el orden del enunciado oficial, con cada precepto citado y comprobable.
  - La experiencia del proyecto muestra que **el riesgo principal de la IA en este bloque no es inventar normas, sino alterar levemente su literal**: un artículo mal numerado, una letra añadida a una enumeración o un plazo desfasado. Por eso se instauró el cotejo precepto a precepto (apartado 6).

#### 5.2.2 Síntesis de contenido técnico

- **Herramienta:** Claude Code.
- **Prompts:** P-04 (redacción de un tema técnico siguiendo el esqueleto oficial), P-05 (las 9 piezas de un tema), P-06 (diagramas SVG) y P-07 (casos prácticos). Todos reconstruidos; ver el Anexo II.

#### 5.2.3 Generación de preguntas tipo test

- **Herramienta:** Claude Code y subagentes.
- **Ejemplos *few-shot* utilizados:**
  - El banco del tema 1 validado por el IAM, como patrón de los bancos administrativos.
  - El examen de 21 de junio de 2025 (parte teórica y práctica), como patrón de formato y nivel.
  - Los casos tipo test del tema 1, como ejemplo de estilo de las preguntas de los casos.
- **Prompts:** P-09 y P-10 (bancos, reconstruidos), P-11 (preguntas de los casos, literal) y P-12 (simulacro práctico, literal).

#### 5.2.4 Generación del código web

- **Herramienta:** Claude Code.
- **Prompts:** P-13 (generador de la página de cada tema), P-14 (plataforma con los 40 temas) y P-15 (cambios de interfaz pedidos por el Ayuntamiento). Ver el Anexo II.

El catálogo completo de prompts figura en el Anexo II.

---

## 6. Procedimiento de verificación humana

### 6.1 Equipo revisor

| Perfil | Cualificación | Ámbito de revisión |
|---|---|---|
| Equipo IAM (revisión jurídica) | Personal jurídico del Ayuntamiento de Madrid | Bloque administrativo (T1-T10): exactitud normativa, literalidad de las citas, criterios de las preguntas. Revisión de estilo de los 40 temas |
| Equipo eTrivium · Dirección de calidad formativa | Personal del adjudicatario | Calidad de los contenidos y de la estructura del temario y de la evaluación; revisión de los temas al publicarse (abril-septiembre de 2026). Interlocución con el IAM en la validación |
| Equipo IAM (validación técnica) | Personal técnico del Organismo Autónomo Informática | Validación de los 40 temas: cobertura del enunciado oficial, coherencia entre temas, preguntas del bloque técnico, plataforma web |
| Equipo eTrivium · Implementación técnica (revisión editorial) | Personal del adjudicatario | Cotejo con el BOE consolidado, barridos de normas caducadas, revisión visual de diagramas, registro de cambios |
| Equipo eTrivium · Implementación técnica (QA automatizado) | Personal del adjudicatario | Scripts de verificación: ortografía, recuentos, reparto de respuestas, SVG, pruebas funcionales y de accesibilidad |

### 6.2 Criterios de revisión

**Temario administrativo**

- Contraste de cada afirmación con el texto consolidado vigente de la norma.
- Comprobación de los números de artículo, apartado y letra citados.
- Comprobación de que la norma no ha sido derogada ni modificada. Ejemplos de reformas incorporadas: la cuarta reforma de la Constitución (art. 69.3, 2026) y los permisos del TREBEP tras el RDL 9/2025.
- Citas literales sin alteraciones; valoraciones e interpretaciones solo dentro de las cajas identificadas.
- Cobertura del enunciado oficial del BOAM, sin normativa ajena.

**Temario técnico**

- Contraste con la documentación oficial o los estándares.
- Comprobación de la vigencia de versiones, productos y tecnologías.
- Cobertura literal del enunciado oficial de cada tema y fronteras entre temas próximos, por ejemplo en el bloque de redes.

**Preguntas tipo test**

- Una única respuesta correcta.
- Respuesta correcta respaldada por la fuente citada.
- Sin ambigüedades ni errores de redacción.
- Sin duplicados.
- Reparto equilibrado de la respuesta correcta entre a, b y c.

**Código web**

- Funcionamiento correcto de la autocorrección, los contadores y la calificación.
- Accesibilidad (WCAG 2.1 AA) y diseño responsivo.
- Sin dependencias externas innecesarias ni credenciales en el código.

### 6.3 Proceso

1. **QA automatizado previo** de cada tema generado:
   - ortografía (hunspell es_ES);
   - referencias cruzadas contra el BOAM;
   - recuentos y reparto de respuestas;
   - restos de formato;
   - validez y geometría de los diagramas (texto desbordado, solapes);
   - capturas de pantalla;
   - prueba del motor de test.

   Lo que el QA no ve (contraste del color, flechas mal dirigidas, sentido jurídico) se revisa a ojo, captura a captura. Detalle en el documento de flujo, apartado 4.
2. **Publicación de trabajo** (v1.0, «Pendiente de validación») y **primera revisión** con el checklist del tema y el prompt maestro de validación (P-08 y P-17).
3. **Registro de incidencias** en el registro de cambios de cada tema, con versión visible. El Anexo III las consolida.
4. **Corrección quirúrgica:**
   - sobre el Markdown fuente;
   - sincronización con la página web;
   - subida de versión;
   - propagación de la corrección a todos los temas que comparten el dato;
   - nuevo QA.
5. **Revisiones transversales** sobre la serie completa:
   - revisión jurídica de T1-T10 con cotejo precepto a precepto con el BOE consolidado (octubre de 2026);
   - normas caducadas e ISO/IEC 25010:2023 (T11-T40);
   - barrido visual de los diagramas de los 40 temas;
   - consistencia entre temas;
   - literalidad de los títulos.
6. **Validación del IAM y aprobación final** de los 40 temas (8 de octubre de 2026) y de la plataforma V3 publicada con ellos, que incluye los exámenes, los simulacros teórico y práctico y las preguntas tipo test de los casos (octubre de 2026). Solo el contenido validado alimenta la plataforma entregada, con las correcciones previas a la entrega del punto 7.
7. **Corrección previa a la entrega (11 de octubre de 2026)**, en tres rondas, con evidencia antes/después y fundamento, documentados por el adjudicatario:
   - primera: todas las incidencias de gravedad alta que seguían abiertas, junto con otras menores;
   - segunda: las propuestas de contenido pendientes de los informes de validación del Ayuntamiento (temas 1, 2, 3 y 11);
   - tercera (11-10-2026): el resto de discrepancias entre las soluciones orientativas de los casos y el contenido aprobado, y las incidencias de contenido que quedaban abiertas.

   Además, se enlazaron las normas en la sección Fuentes de los 40 temas (819 enlaces verificados uno a uno, sin cambiar el texto visible).

### 6.4 Resultados

Fecha de corte: 11-10-2026, tras la corrección previa a la entrega (punto 7 del apartado 6.3). Fuente: Anexo III, con 582 registros.

| Tipo de contenido | Elementos revisados | Incidencias detectadas | Tasa de error | Corregidas |
|---|---|---|---|---|
| Temas administrativos | 10 temas | 219 registros (166 de fondo) | 10 de 10 temas con algún error de fondo en su primera versión | 218 de 219 (1 no aplicada por criterio) |
| Temas técnicos | 30 temas | 114 registros (39 de fondo) | 18 de 30 temas con algún error de fondo | 111 de 114 (3 descartadas) |
| Preguntas administrativas | 1.525 | 774 preguntas modificadas | 50,8 % (ver nota) | 774 |
| Preguntas técnicas | 1.765 | 30 preguntas (5 de fondo) | 1,7 % (0,3 % de fondo) | 30 |
| Preguntas de casos | 1.492 | 84 registros | 5,6 % (orientativa) | 80 (4 no aplicadas por criterio) |
| Diagramas | 553 | ≈ 235 (estimación) | ≈ 42 % | ≈ 235 |

**Cómo leer la tabla.**

- **La tasa de las preguntas administrativas mide sobre todo un cambio de criterio**, no solo errores. La revisión jurídica exigió que todas las preguntas salieran del literal de la norma, y se reescribieron bancos enteros: en el tema 6, las 160 preguntas. Donde el registro distingue los motivos, la mayoría de las preguntas se ajustaron al literal sin que hubiera un error de respuesta.
- **Diagramas:** la cifra suma un barrido visual (≈ 150 corregidos, sin recuento individual) y 85 correcciones registradas aparte, que pueden solaparse. Es un orden de magnitud. Las 323 incidencias de composición corregidas en el QA previo a la publicación no se cuentan.
- **Elementos de fondo:** son las incidencias de gravedad alta o media.
- El cálculo de cada fila y qué cifras son exactas o estimadas está en `anexos/datos-6.4-6.5.md`.

**Incidencias abiertas a la fecha de corte.** El 11-10-2026 quedaban 62 incidencias sin cerrar, 11 de ellas de gravedad alta. Las dos primeras rondas de la corrección previa a la entrega cerraron las 11 graves y otras 14, y añadieron 6 registros nuevos, ya corregidos (I-576 a I-581). Además, una incidencia que figuraba como corregida (I-333, homogeneización de castellano e inglés en el tema 11) se reclasificó como parcial al comprobar que no se había aplicado de forma general. Tras esas dos rondas quedaban 38 abiertas, ninguna grave. La tercera ronda (11-10-2026) corrigió otras 30: 28 discrepancias entre la solución orientativa de los casos y el contenido aprobado (dos de ellas, I-346 e I-347, también en el contenido del tema 11), la homogeneización de castellano e inglés del tema 11 (I-333) y la denominación 802.1AX del tema 37 (I-539). Se cerró también la etiqueta del hub «Contenido práctico» de la maqueta V3, tras comprobar el 11-10-2026 que ya no existe en la web entregada (I-572), y se añadió un registro nuevo, ya corregido: la fecha de la Orden PRE/1716/2011 en las Fuentes del tema 34 (I-582).

A 11-10-2026, el Anexo III registra **una sola incidencia abierta, como parcial, y ninguna de gravedad alta**: los enlaces a las normas (I-570). La normativa estatal (BOE) y de la UE (EUR-Lex) está enlazada en las Fuentes de los 40 temas, pero la normativa municipal (salvo 4 normas) y las normas ISO/ISO-IEC y CCN-STIC siguen sin enlace porque sus URL no se han podido verificar (madrid.es, iso.org y ccn-cert bloquean la verificación automática).

Otras 6 propuestas, que no son errores de contenido sino de alcance, quedan como **no aplicadas por criterio** y se cuentan como cerradas: por decisión del adjudicatario se mantiene el alcance aprobado por el Ayuntamiento en el §12 del tema 1 (I-011), en las preguntas de casos apoyadas en material complementario de los temas 16, 22, 26 y 28 (I-379, I-426, I-463 e I-477) y en los siete temas que despliegan pocas materias del título en muchas secciones (I-564).

Por no ser errores, tampoco se aplicaron otras dos propuestas del informe del tema 11: la revisión individual de los 12 diagramas (tarea de validación del Ayuntamiento) y llevar a la tabla de Fuentes las referencias de Microsoft (sí se añadieron el RFC 3629 y la ISO/IEC 25012). En el tema 3 se mantiene el diagrama D8, que el Ayuntamiento dio por apto.

### 6.5 Tipología de errores detectados

| Tipo | Qué es | Registros | Graves | Abiertas |
|---|---|---|---|---|
| Referencia normativa incorrecta | Artículo mal numerado, remisión equivocada o cita «literal» alterada | 176 | 55 | 0 |
| Alucinación | Precepto, frase, sentencia o dato inexistente presentado como si estuviera en la fuente | 22 | 13 | 0 |
| Norma derogada o desactualizada | Norma derogada o redacción superada presentada como vigente | 22 | 13 | 0 |
| Dato técnico desactualizado | Estándar o especificación sustituidos por una edición posterior | 30 | 4 | 0 |
| Respuesta marcada incorrecta | La opción dada como correcta no lo es, o la letra estaba mal etiquetada | 16 | 8 | 0 |
| Pregunta ambigua | Más de una opción defendible | 31 | 0 | 0 |
| Distractor deficiente | Distractores no verosímiles, duplicados o respuesta correcta concentrada en una letra | 16 | 0 | 0 |
| Fuera del programa oficial | Contenido o preguntas que el enunciado del BOAM no pide | 41 | 0 | 0 |
| Coherencia entre temas | Remisiones cruzadas erróneas, solapes, incoherencias de formato | 35 | 0 | 1 |
| Diagrama | Texto ilegible o desbordado, flechas mal dirigidas, notación incorrecta | 86 | 0 | 0 |
| Ortografía y estilo | Diacríticos, etiquetas internas visibles, frases sobre el examen | 107 | 0 | 0 |

*Graves:* registros de gravedad alta; ninguno sigue abierto. *Abiertas:* pendientes o parciales a 11-10-2026; no hay ninguna pendiente y queda una parcial (I-570). Las 6 no aplicadas por criterio (5 de «Fuera del programa oficial» y 1 de «Coherencia entre temas») se cuentan como cerradas.

**Ejemplos reales** (los identificadores remiten al Anexo III):

- **Alucinación.**
  - Se atribuía al art. 46 TREBEP un preaviso de 48 horas en unos apartados que no existen (I-254, tema 9).
  - El art. 53.1 LPACAP aparecía con una letra inexistente (I-139, tema 6).
  - Las medidas LGTBI en las empresas se atribuían a una «disposición adicional 11.ª» de la Ley 4/2023 que no existe; están en su art. 15 (I-297, tema 10).
- **Referencia normativa incorrecta.**
  - El art. 53.1 CE se hacía remitir al art. 81, cuando remite al 161.1.a) (I-012, tema 1).
  - Se afirmaba que los ingresos de derecho privado se cobran por apremio, contra lo que dispone el art. 4 TRLHL (I-222, tema 8).
- **Norma derogada.**
  - Los Foros Locales aparecían como vigentes, cuando están derogados por el Reglamento Orgánico 7/2021 (I-095, tema 4).
  - Las infraestructuras comunes de telecomunicaciones se atribuían a la Ley 9/2014, derogada por la Ley 11/2022 (tema 37).
- **Desactualización.**
  - Faltaba la cuarta reforma constitucional, de 2026 (I-024, tema 1).
  - Los permisos por nacimiento no recogían las 19 semanas del RDL 9/2025 (I-110, tema 5).
  - El modelo de calidad ISO/IEC 25010 de 2011 se presentaba como vigente, en lugar del de 2023 (I-448, tema 25).
  - TLS 1.3 se citaba por el RFC 8446, obsoleto desde el RFC 9846 (75 apariciones en siete temas).
- **Respuesta marcada incorrecta.** Tres preguntas del tema 22 tenían mal etiquetada la letra correcta. El script de reparto de respuestas las detectó antes de publicar (I-419).

**Conclusión de la validación.**

- Los errores de fondo se concentraron en el **bloque administrativo**: los diez temas tenían alguno frente al BOE consolidado, aunque varios no los había señalado el QA automático ni la primera revisión. Esto confirma que **la verificación humana precepto a precepto es imprescindible** con material generado por IA y que una revisión «por plausibilidad» no basta.
- En el bloque técnico, el riesgo dominante fue la **vigencia de los estándares**: ediciones sustituidas durante el propio proyecto.
- Los defectos de **composición de los diagramas** solo se detectan por inspección visual.

---

## 7. Cumplimiento normativo y requisitos de IA (MAIA)

### 7.1 Protección de datos

Conforme al apartado 16 del informe de condiciones, la ejecución del contrato no implica tratamiento de datos personales responsabilidad del Ayuntamiento.

- No se han introducido datos personales en las herramientas de IA. Los insumos han sido normativa pública, documentación técnica, exámenes publicados y el material facilitado por el IAM.
- La plataforma no recoge datos personales:
  - no tiene registro ni formularios;
  - el progreso se guarda solo en el navegador del usuario;
  - la única analítica es la institucional del Ayuntamiento (Siteimprove).

Por ello no procede la Evaluación de Impacto en Protección de Datos (EIPD).

### 7.2 Evaluación de riesgos de IA

El proyecto **no pone en producción modelos de IA ni realiza inferencia sobre datos de la ciudadanía**. La IA se ha usado como herramienta de apoyo para elaborar un material estático, y todo el contenido publicado ha sido validado por personas y aprobado por el IAM. El producto final no contiene ningún componente de IA. Por ello no procede la Evaluación de Impacto de Riesgo en IA (*AI Risk Assessment*) previa a una puesta en producción, prevista en la cláusula 18 para sistemas que se pongan en producción.

### 7.3 Reglamento (UE) 2024/1689 de Inteligencia Artificial

- **Transparencia:**
  - El material publicado no contiene ultrasuplantaciones (*deepfakes*) ni texto publicado sin revisión humana para informar sobre asuntos de interés público. El IAM ha considerado que no procede etiquetarlo como contenido generado por IA.
  - El repositorio informa de cómo se elaboró y enlaza este informe (README, apartado «Cómo se ha elaborado»).
  - La imagen de portada se generó con IA y no representa a personas reales.
- **Supervisión humana:** véase el apartado 6.
- **Trazabilidad:** véanse el Anexo I (fuentes), el Anexo II (prompts) y el Anexo III (incidencias). Cada tema conserva su registro de cambios con versión.

### 7.4 Seguridad de la información

Se ha cumplido, en lo aplicable, el ENS (RD 311/2022) y la Política de Seguridad del Ayuntamiento de Madrid:

- **Sitio estático:** no hay servidor de aplicaciones, ni base de datos, ni autenticación, ni formularios.
- **Sin credenciales, claves ni tokens** en el código ni en el historial del repositorio.
- **Despliegue con GitHub Actions** usando solo acciones oficiales de GitHub (`checkout`, `configure-pages`, `upload-pages-artifact`, `deploy-pages`) y permisos mínimos (`contents: read`, `pages: write`, `id-token: write`).
- **Gestión de accesos al repositorio** a cargo de la organización `ayuntamientomadrid`. Tras la entrega, el adjudicatario no necesita conservar permisos de escritura.
- **Sin recursos de terceros** en tiempo de ejecución salvo la analítica institucional.

---

## 8. Propiedad intelectual y transferencia de conocimiento

### 8.1 Cesión de derechos

El adjudicatario cede al Ayuntamiento de Madrid los derechos de propiedad intelectual sobre los materiales generados y el código desarrollado, para su libre publicación y distribución pública. El repositorio se publica bajo CC0 1.0 Universal, la licencia determinada por el IAM, que permite la reutilización libre, incluso sin reconocimiento.

### 8.2 Mantenimiento y actualización

El material puede mantenerse **sin depender del adjudicatario ni de herramientas de IA**. La guía completa está en `docs/mantenimiento.md`. En resumen:

- **Fuente única:** `herramientas/datos/`, con un fichero JSON por tema (contenido, diagramas, casos, fuentes y banco de preguntas), las preguntas de los casos y el simulacro práctico.
- **Formato de las preguntas:** `{q, o, c, r, e}`, es decir:
  - `q`: enunciado;
  - `o`: tres opciones;
  - `c`: índice de la correcta;
  - `r`: referencia normativa o técnica;
  - `e`: explicación.

  En `tests/` se publica una versión legible con las claves en español.
- **Regeneración:** `generar_web.py` (web), `exportar_md.py` (Markdown, SVG y tests) y `generar_pdf.py` (PDF). Son scripts de Python con dependencias libres.
- **Redespliegue:** basta con un *push* a la rama `main`; GitHub Actions publica en GitHub Pages en un par de minutos.
- **Añadir temas o preguntas:** se añaden objetos al JSON del tema y se comprueba el reparto de la respuesta correcta. La guía incluye un comando de una línea para hacerlo.

### 8.3 Recomendaciones

Ante cada nueva convocatoria, o cuando se produzca un cambio normativo o tecnológico relevante, se recomienda revisar:

- **Programa:** comparar los 40 enunciados con el BOAM de la convocatoria.
- **Normativa con reformas frecuentes:**
  - Constitución: reformas del art. 49 (2024) y del art. 69.3 (2026).
  - TREBEP: permisos.
  - LPACAP.
  - TRLHL.
  - Organización municipal: número y denominación de las Áreas de Gobierno (tema 3) y organización de los Distritos (tema 4).
  - Acuerdo-Convenio y Plan de Igualdad del Ayuntamiento, cuando se renueven.
- **Estándares técnicos:**
  - Ediciones de ISO/IEC 25010, WCAG y EN 301 549.
  - RFC de TLS y otros protocolos.
  - ENS y guías CCN-STIC.
  - OWASP Top 10: conviene unificar la edición citada en toda la serie.
  - Versiones de sistemas operativos y productos.
- **Regla de propagación:** cuando un dato se corrige en un tema, buscarlo en los 40 (`grep` sobre `herramientas/datos/`) y corregirlo en todos el mismo día.

---

## 9. Conclusiones

Se han elaborado, validado y publicado los entregables del contrato:

- el temario completo de los 40 temas del programa oficial en formato web, Markdown y PDF;
- 3.290 preguntas tipo test;
- 148 casos prácticos con 1.492 preguntas;
- un simulacro práctico;
- una plataforma web estática, accesible y responsiva con autocorrección, contador de aciertos y fallos, exámenes por tema y simulacros.

Todo está en un repositorio del Ayuntamiento de Madrid y es mantenible sin dependencia del adjudicatario.

La IA generativa ha permitido producir un volumen de material que, por métodos tradicionales, habría requerido mucho más tiempo. El proyecto confirma también lo que anticipaba el pliego: **la IA no sustituye a la validación humana**. El registro de 582 incidencias muestra que los errores típicos de la IA (preceptos alterados, normas superadas, datos inexistentes presentados con apariencia de rigor) solo se eliminan con un procedimiento sistemático:

- cotejo con la fuente oficial;
- revisión por perfiles especializados;
- QA automatizado de lo medible;
- validación final del órgano contratante.

A la fecha de corte del registro (11-10-2026) no queda abierta ninguna incidencia de gravedad alta: de los 582 registros, 570 están corregidos, 5 descartados, 6 no aplicados por criterio (propuestas de alcance, no errores, en las que se mantiene el alcance aprobado por el Ayuntamiento) y 1 parcial, de gravedad media: los enlaces a las normas, que cubren la normativa estatal y de la UE de los 40 temas, pero no la municipal ni las normas ISO y CCN-STIC, cuyas URL no se han podido verificar. No queda ninguna pendiente.

---

## Anexos

- **Anexo I. Inventario de fuentes utilizadas:** `anexos/anexo-I-fuentes.md` y `.csv`. Contiene 949 fuentes distintas y 10 materiales de examen.
- **Anexo II. Catálogo de prompts:** 20 prompts, más el documento complementario «Flujo de trabajo con IA». Como el repositorio es de acceso público, se entregan directamente al IAM y no se publican.
- **Anexo III. Registro de incidencias detectadas en la validación:** `anexos/anexo-III-incidencias.md` y `.csv`. Contiene 582 registros. El cálculo de las cifras del apartado 6.4 está en `anexos/datos-6.4-6.5.md`.
- **Evidencias:** la auditoría de accesibilidad (axe-core), las pruebas funcionales y de navegadores y el detalle de las correcciones previas a la entrega las conserva el adjudicatario, a disposición del IAM.

---

*Documento elaborado por Etrivium Learn, S.L. en el marco del expediente 300/2026/00147.*
