"""Ficha de estudio de cada tema: extensión, diagramas, preguntas y horas estimadas."""
import html
import math
import re

# --- Formula acordada -------------------------------------------------------
# Contenido teorico a ritmo de estudio activo (no de lectura corrida),
# los diagramas a una hora por cada cinco, y el test a dos minutos por pregunta
# (60 preguntas = 2 h, que es lo que se comprometio con el IAM).
PALABRAS_POR_HORA = 1500
DIAGRAMAS_POR_HORA = 5
PREGUNTAS_POR_HORA = 30

MARCA_INI = "<!-- ficha-estudio:ini -->"
MARCA_FIN = "<!-- ficha-estudio:fin -->"

CSS = """
/* ficha-estudio */
.ficha-estudio{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0}
.ficha-estudio .fe-item{flex:1 1 260px;border:1px solid rgba(127,127,127,.28);
  border-left:3px solid #c77a1b;border-radius:6px;padding:10px 14px}
.ficha-estudio .fe-k{display:block;font-size:11px;letter-spacing:.09em;
  text-transform:uppercase;opacity:.72;margin-bottom:3px}
.ficha-estudio .fe-v{display:block;font-size:15px;font-weight:600;line-height:1.4}
.ficha-estudio .fe-n{font-weight:400;font-size:13px;opacity:.75}
@media print{.ficha-estudio .fe-item{break-inside:avoid}}
"""


def limpio(fragmento):
    """Texto visible: fuera scripts, estilos, SVG y comentarios."""
    for pat in (r"(?is)<script.*?</script>", r"(?is)<style.*?</style>",
                r"(?is)<svg.*?</svg>", r"(?s)<!--.*?-->"):
        fragmento = re.sub(pat, "", fragmento)
    return html.unescape(re.sub(r"(?s)<[^>]+>", " ", fragmento)).split()


def medir(doc):
    """Devuelve (palabras del contenido teorico, diagramas, preguntas)."""
    diagramas = len(re.findall(r"<svg\b", doc))
    # Las tres plantillas escriben la clave de forma distinta:
    #   "correct": 0   ·   correct: 0   ·   ok: 'a'
    preguntas = len(re.findall(r"""["']?correct["']?\s*:""", doc)) or \
        len(re.findall(r"""["']?ok["']?\s*:\s*["']""", doc))

    palabras = None
    for ancla in (r'id="tab-contenido"', r'id="contenido-body"'):
        m = re.search(ancla, doc)
        if not m:
            continue
        resto = doc[m.end():]
        fin = re.search(r'id="(tab-diagramas|diagramas|diagramas-body)"', resto)
        palabras = len(limpio(resto[:fin.start()] if fin else resto))
        break
    return palabras, diagramas, preguntas


def horas(palabras, diagramas, preguntas):
    h = (palabras / PALABRAS_POR_HORA
         + diagramas / DIAGRAMAS_POR_HORA
         + preguntas / PREGUNTAS_POR_HORA)
    lo = int(math.floor(h))
    return h, "%d-%d" % (lo, lo + 2)


def redondea_palabras(n):
    """~22.500 en vez de 22.497: la precision falsa resta credibilidad."""
    if n >= 10000:
        v = int(round(n / 500.0) * 500)
    elif n >= 1000:
        v = int(round(n / 100.0) * 100)
    else:
        v = n
    return "{:,}".format(v).replace(",", ".")


def bloque(palabras, diagramas, preguntas, rango):
    ext = "~%s palabras &middot; %d diagramas" % (redondea_palabras(palabras), diagramas)
    if preguntas:
        ext += " &middot; %d preguntas de test" % preguntas
    return (
        '%s<div class="ficha-estudio">'
        '<div class="fe-item"><span class="fe-k">Extensi&oacute;n</span>'
        '<span class="fe-v">%s</span></div>'
        '<div class="fe-item"><span class="fe-k">Tiempo estimado de estudio</span>'
        '<span class="fe-v">%s horas '
        '<span class="fe-n">(primera vuelta completa, sin contar repasos)</span>'
        '</span></div></div>%s' % (MARCA_INI, ext, rango, MARCA_FIN)
    )


# Las plantillas antiguas abrevian ("~11K palabras"), las nuevas no ("~27.500 palabras")
