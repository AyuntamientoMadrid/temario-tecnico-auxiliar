# Temario de Técnico/a Auxiliar de Tecnologías de la Información y Comunicaciones (C1)

Material formativo abierto para preparar la oposición de **Técnico/a Auxiliar de Tecnologías de la Información y Comunicaciones (Grupo C1, subgrupo C1)** del Ayuntamiento de Madrid. Sigue el programa oficial publicado en el BOAM n.º 10.032, de 23 de diciembre de 2025.

**Web:** <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/>

Lo publica el Organismo Autónomo Informática del Ayuntamiento de Madrid (IAM) dentro del expediente 300/2026/00147.

## Qué contiene

| | Bloque administrativo | Bloque técnico | Total |
|---|---|---|---|
| Temas | 10 (temas 1-10) | 30 (temas 11-40) | **40** |
| Preguntas tipo test | 1.525 | 1.765 | **3.290** |
| Casos prácticos | 60 | 88 | **148** |
| Preguntas tipo test sobre los casos | 612 | 880 | **1.492** |
| Diagramas | | | **553** |

También incluye un **simulacro práctico** (un supuesto y 30 preguntas) con el formato de la parte práctica del examen.

Las preguntas del bloque administrativo citan su base legal: el artículo y la norma o, cuando la pregunta trata de la estructura de una ley o de una de sus disposiciones, el título, el capítulo o la disposición correspondiente.

## Formatos

- **Web interactiva** (raíz del repositorio): los 40 temas con índice, contenido, diagramas, casos y fuentes, más un examen por tema y simulacros de 90 preguntas aleatorias.
  - Los tests se corrigen solos y cuentan aciertos, fallos y preguntas en blanco.
  - La nota se calcula como en las bases de la convocatoria: +1 por acierto, −1/3 por error, 0 en blanco, sobre 10.
  - El progreso se guarda solo en el navegador de cada persona (`localStorage`): no hay servidor, ni registro, ni cookies propias.
- **Markdown**: `temario/administrativo/tema-NN/tema-NN.md` y `temario/tecnico/tema-NN/tema-NN.md`. Los diagramas están en la carpeta `diagramas/` de cada tema, en SVG.
- **PDF**: `tema-NN.pdf` en la misma carpeta de cada tema.
- **Baterías de test**: `tests/administrativo/` y `tests/tecnico/`, en JSON (para reutilizarlas) y en Markdown (para leerlas). `tests/simulacro-practico.*` contiene el simulacro práctico.

## Estructura

```
/
├── index.html                  Web: portada, temario, exámenes, simulacros, progreso
├── temas/tema-NN.html          Web: página de cada tema
├── assets/                     CSS, JavaScript, imágenes y banco de preguntas (JSON)
├── temario/
│   ├── administrativo/tema-01 … tema-10/   tema-NN.md · tema-NN.pdf · diagramas/
│   └── tecnico/tema-11 … tema-40/
├── tests/
│   ├── administrativo/tema-NN.{json,md}
│   ├── tecnico/tema-NN.{json,md}
│   └── simulacro-practico.{json,md}
├── herramientas/               Scripts para regenerar la web, el Markdown y los PDF
├── docs/                       Mantenimiento, informe de metodología y validación (Anexos I y III)
├── LICENSE                     CC0 1.0 Universal
└── .github/workflows/pages.yml Publicación en GitHub Pages
```

## Formato de las preguntas (JSON)

```json
{
  "numero": 1,
  "pregunta": "De acuerdo con la Constitución Española, España se constituye en:",
  "opciones": { "a": "Un Estado social y democrático de derecho.", "b": "…", "c": "…" },
  "correcta": "a",
  "referencia": "CE, art. 1.1",
  "explicacion": ""
}
```

## Tecnología y accesibilidad

- HTML, CSS y JavaScript estáticos, sin dependencias externas ni servidor. Se publica tal cual en GitHub Pages.
- Diseño responsivo, revisado a 390 px de ancho.
- Navegable con teclado y con textos alternativos en los diagramas.
- Objetivo de conformidad: WCAG 2.1 AA.
- Declaración de accesibilidad: <https://ayuntamientomadrid.github.io/Procesos-selectivos-TIC/accesibilidad.html>

## Mantenimiento

Cómo corregir una pregunta, actualizar un tema y volver a publicar: [docs/mantenimiento.md](docs/mantenimiento.md).

## Cómo se ha elaborado

El material se ha elaborado con herramientas de inteligencia artificial y lo han revisado personas. Cómo se hizo, cómo se verificó y qué fuentes se consultaron: [docs/informe-metodologia-validacion.md](docs/informe-metodologia-validacion.md), con el inventario de fuentes (Anexo I) y el registro de incidencias de la validación (Anexo III). El catálogo de prompts (Anexo II) se ha entregado directamente al IAM y no se publica.

## Licencia

Todo el contenido de este repositorio (temario, preguntas, casos, diagramas, PDF y código de la web y de `herramientas/`) se publica bajo **[CC0 1.0 Universal](LICENSE)**, la licencia que ha determinado el IAM. Puedes copiarlo, modificarlo y redistribuirlo, también con fines comerciales, sin pedir permiso.

- El escudo y el logotipo del Ayuntamiento de Madrid (`assets/img/firma*.svg`, `favicon.ico`) son signos distintivos de la institución. CC0 no renuncia a derechos de marca (apartado 4.a), así que su uso se rige por el Manual de identidad corporativa del Ayuntamiento.
- Los textos normativos citados (BOE, BOCM, BOAM) no están sujetos a propiedad intelectual (art. 13 de la Ley de Propiedad Intelectual).

## Contacto

Buzón de los procesos selectivos TIC: [procesosselectivostic@madrid.es](mailto:procesosselectivostic@madrid.es)

Este material es de apoyo al estudio y no sustituye a las bases ni a la normativa oficial. En caso de discrepancia, prevalece siempre el texto publicado en el BOE, el BOCM o el BOAM.
