# Mantenimiento del temario

Guía para que el IAM, o quien designe, corrija o actualice el material y lo vuelva a publicar sin depender de quien lo elaboró ni de herramientas de pago.

## 1. De dónde sale cada cosa

Todo se genera a partir de los datos de `herramientas/datos/`. **No edites a mano** `index.html`, `temas/`, `assets/data/`, `temario/` ni `tests/`: la siguiente generación sobrescribe esos cambios.

| Fichero de datos | Qué contiene | Qué genera |
|---|---|---|
| `herramientas/datos/extract/tema-NN.json` | Un tema completo: título, ficha, epígrafes, contenido, diagramas, casos, fuentes y banco de preguntas | Web, Markdown, PDF y test |
| `herramientas/datos/casos-test/tema-NN.json` | Preguntas tipo test de cada caso práctico (temas 2-40) | Bloque «Preguntas tipo test sobre este caso» |
| `herramientas/datos/simulacro-practico.json` | Supuesto y 30 preguntas del simulacro práctico | Simulacro práctico de la web y `tests/simulacro-practico.*` |
| `herramientas/plantillas/index.html` | Pantallas de la aplicación: portada, progreso, exámenes y simulacros | `index.html` |
| `assets/css/app.css`, `assets/js/app.js` | Estilos y lógica de la web | Se editan directamente |

### Campos de `tema-NN.json`

- `titulo`, `subtitulo`: cabecera del tema.
- `epigrafes`: lista `{id, t, lvl}` de los apartados. `lvl` vale 2 para los apartados y 3 para los subapartados. Los `id` (`ep-1`, `ep-2`…) deben coincidir con los del contenido.
- `contenido`, `diagramas`, `casos`, `fuentes`, `indiceExtra`: HTML de cada pestaña. Los diagramas son SVG en línea.
- `preguntas`: banco de test. Cada pregunta es `{q, o, c, r, e}`:
  - `q`: el enunciado.
  - `o`: las tres opciones.
  - `c`: el índice de la correcta (0 = a, 1 = b, 2 = c).
  - `r`: la referencia (norma y artículo, o fuente técnica).
  - `e`: la explicación.
- `casosData`: solo en el tema 1, que tiene casos tipo test con su propio formato.

## 2. Instalación (una sola vez)

```bash
python3 -m pip install -r herramientas/requirements.txt
python3 -m playwright install chromium      # solo para los PDF
# pandoc, para el Markdown: https://pandoc.org/installing.html
```

## 3. Tareas habituales

### Corregir una pregunta

1. Abre `herramientas/datos/extract/tema-NN.json`, busca el enunciado y corrige `q`, `o`, `c`, `r` o `e`.
2. Si cambias la respuesta correcta, revisa también la explicación (`e`).
3. Mantén **tres opciones**, **una sola correcta** y la cita de la norma con su artículo en `r`.
4. Sigue el paso 4.

Las preguntas de los casos están en `herramientas/datos/casos-test/tema-NN.json`, con el mismo formato.

### Actualizar un tema por un cambio normativo

1. Localiza la norma en `fuentes` y en `contenido` del `tema-NN.json`. Busca también en los **otros 39 temas**, porque una misma norma suele citarse en varios:
   ```bash
   grep -l "Ley 39/2015" herramientas/datos/extract/*.json herramientas/datos/casos-test/*.json
   ```
2. Corrige el texto, la referencia y, si cambia, la respuesta de las preguntas afectadas.
3. Contrasta cada cambio con el **texto consolidado del BOE**. No basta con que el resultado parezca plausible.

### Añadir preguntas

Añade objetos al final de `preguntas`. Antes de publicar, comprueba que la respuesta correcta se reparte de forma parecida entre a, b y c. Si no, quien estudia aprende a «cantar» la letra dominante:

```bash
python3 -c "import json,collections,sys; d=json.load(open(sys.argv[1])); print(collections.Counter('abc'[p['c']] for p in d['preguntas']))" herramientas/datos/extract/tema-07.json
```

## 4. Regenerar y publicar

Desde la raíz del repositorio:

```bash
python3 herramientas/generar_web.py      # web: index.html, temas/, assets/js/temas.js, assets/data/
python3 herramientas/exportar_md.py      # temario/*.md, diagramas SVG y tests/
python3 herramientas/generar_pdf.py      # temario/*.pdf (o solo algunos temas: generar_pdf.py 7 8)
git add -A && git commit -m "fix: corrige la pregunta 12 del tema 7" && git push
```

Al hacer *push* a `main`, el flujo `.github/workflows/pages.yml` publica la web en GitHub Pages en un par de minutos.

- GitHub Pages guarda en caché hasta 10 minutos.
- La web pide CSS, JS y datos con una huella de versión (`?v=…`) que cambia en cada generación, así que nadie ve una mezcla de versiones.

### Comprobaciones antes del push

- `generar_web.py` termina con `OK · 40 temas · N preguntas`.
- Abre `index.html` con un servidor local (`python3 -m http.server`) y prueba:
  - un examen de tema;
  - un simulacro;
  - la página del tema modificado;
  - la impresión (Imprimir → Guardar como PDF).
- Revisa los diagramas modificados en la propia página: un SVG mal cerrado puede dejar media figura sin pintar sin que ningún script dé error.

## 5. Cambiar la URL de publicación

Si el repositorio cambia de nombre o de organización, cambia `SITE_URL` en `herramientas/generar_web.py` (lo usan las etiquetas `og:url` y `og:image`) y las URL de `README.md` y de `herramientas/exportar_md.py`, y regenera.

## 6. Qué conviene revisar en cada convocatoria

- **Programa**: compara el temario con el BOAM de la nueva convocatoria. Los enunciados oficiales están en `OFICIAL`, dentro de `generar_web.py`.
- **Normativa con reformas frecuentes**: CE (reformas del art. 49 en 2024 y del art. 69.3 en 2026), TREBEP (permisos), LPACAP, TRLHL, Plan de Igualdad del Ayuntamiento, organigrama y número de Áreas de Gobierno (tema 3).
- **Estándares técnicos**: versiones de ISO/IEC 25010, WCAG y EN 301 549, RFC de TLS (el RFC 9846 sustituye al 8446), ENS (RD 311/2022) y guías CCN-STIC, sistemas operativos y versiones de producto.
- La lista completa de fuentes de cada tema está en su apartado «Fuentes» y en el Anexo I del [informe de metodología](informe-metodologia-validacion.md).
