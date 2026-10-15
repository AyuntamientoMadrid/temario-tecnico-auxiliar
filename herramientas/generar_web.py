"""Genera la web del temario (raíz de este repositorio) a partir de herramientas/datos/.

Entrada:  herramientas/datos/extract/tema-NN.json   (contenido aprobado de cada tema)
          herramientas/datos/casos-test/tema-NN.json (preguntas tipo test de los casos)
          herramientas/plantillas/index.html         (pantallas de la aplicación)
          herramientas/datos/simulacro-practico.json
Salida:   <repo>/index.html
          <repo>/temas/tema-NN.html            (40 páginas)
          <repo>/assets/js/temas.js            (catálogo)
          <repo>/assets/data/preguntas.json    (banco para exámenes y simulacros)
          <repo>/assets/data/simulacro-practico.json

Uso: python3 herramientas/generar_web.py   (requiere beautifulsoup4)
"""
import html
import json
import os
import re
import hashlib
import shutil
import sys

from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ficha_estudio import bloque, horas, medir  # noqa: E402

EXTRACT = os.path.join(HERE, 'datos', 'extract')
REPO = os.path.normpath(os.path.join(HERE, '..'))

# Declaración propia de los procesos selectivos TIC (pedida por el Ayto el 09-10-2026).
ACCESIBILIDAD_URL = 'https://ayuntamientomadrid.github.io/Procesos-selectivos-TIC/accesibilidad.html'
PRIVACIDAD_URL = ('https://www.madrid.es/portales/munimadrid/es/Inicio/Proteccion-de-datos/Proteccion-de-datos/'
                  '?vgnextfmt=default&vgnextoid=2c241e7b0f578010VgnVCM100000dc0ca8c0RCRD&vgnextchannel=251f43db40317010VgnVCM100000dc0ca8c0RCRD')
PROCESOS_URL = 'https://ayuntamientomadrid.github.io/Procesos-selectivos-TIC/'
# URL pública del sitio: cambiar aquí al migrar al dominio del Ayuntamiento (og:url, og:image).
SITE_URL = 'https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/'

# Enunciados literales del programa (BOAM n.º 10.032, de 23 de diciembre de 2025, Anexo).
OFICIAL = {
    1: "La Constitución Española (I): Estructura y contenido. Derechos y deberes fundamentales. Su garantía y suspensión.",
    2: "La Constitución Española (II): La Organización territorial del Estado. Principios generales. La Administración Local. Las Comunidades Autónomas: los Estatutos de Autonomía.",
    3: "El Reglamento Orgánico del Gobierno y de la Administración del Ayuntamiento de Madrid, de 31 de mayo de 2004 (I): Las Áreas de Gobierno y su estructura interna. Órganos superiores de las Áreas de Gobierno; Órganos Centrales directivos. Número y denominación de las actuales Áreas de Gobierno.",
    4: "El Reglamento Orgánico del Gobierno y de la Administración del Ayuntamiento de Madrid, de 31 de mayo de 2004 (II): Los Distritos: Disposiciones Generales. El Concejal Presidente. Estructura administrativa.",
    5: "El personal al servicio de la Administración Pública conforme al texto refundido de la Ley del Estatuto Básico del Empleado Público, aprobado por Real Decreto Legislativo 5/2015, de 30 de octubre: clases de personal. Adquisición y pérdida de la relación de servicio. Situaciones administrativas. Derechos de los empleados públicos. Derecho a la carrera profesional y a la promoción interna. La evaluación del desempeño. Derechos retributivos. Derechos a la jornada de trabajo, permisos y vacaciones. Régimen disciplinario.",
    6: "Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas: derechos de los ciudadanos en sus relaciones con las Administraciones Públicas y Registros. Ley 19/2013, de 9 de diciembre, de transparencia, acceso a la información pública y buen gobierno: derecho de acceso a la información pública. Ordenanza de Transparencia de la Ciudad de Madrid de 27 de julio de 2016: ámbito de aplicación y principios generales.",
    7: "Ley 39/2015, de 1 de octubre del Procedimiento Administrativo Común de las Administraciones Públicas: El procedimiento administrativo: Concepto, naturaleza y principios generales. Fases del procedimiento. Los recursos administrativos: Concepto y clases.",
    8: "Real Decreto Legislativo 2/2004, de 5 de marzo, por el que se aprueba el texto refundido de la Ley Reguladora de las Haciendas Locales: Recursos de las Haciendas Locales. Clasificación: Ingresos de derecho público e ingresos de derecho privado. Especial referencia a las tasas. Contribuciones especiales y precios públicos. Impuestos municipales: concepto y clasificación.",
    9: "Ley 31/1995, de 8 de noviembre de Prevención de Riesgos Laborales: Delegados/as de prevención. Comités de seguridad y salud. Especial referencia a la prevención de riesgos laborales del Acuerdo Convenio en vigor sobre condiciones de trabajo comunes al personal funcionario y laboral del Ayuntamiento de Madrid y de sus Organismos Autónomos. Representación de los empleados públicos.",
    10: "Ley Orgánica 3/2007, de 22 de marzo, para la igualdad efectiva de mujeres y hombres: objeto y ámbito de la ley. El principio de igualdad y la tutela contra la discriminación. Ley 4/2023, de 28 de febrero, para la igualdad real y efectiva de las personas trans y para la garantía de los derechos de las personas LGTBI: objeto, ámbito de aplicación y definiciones. El Plan de Igualdad entre mujeres y hombres del Ayuntamiento de Madrid y sus Organismos Autónomos en vigor: ámbito municipal; estructura; objetivo general; líneas de intervención y objetivos específicos.",
    11: "Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema de información. Características y funciones. Arquitectura de ordenadores. Componentes internos de los equipos microinformáticos.",
    12: "Periféricos: conectividad y administración. Elementos de impresión. Elementos de almacenamiento. Elementos de visualización y digitalización.",
    13: "Tipos abstractos y Estructuras de datos. Organizaciones de ficheros. Algoritmos. Formatos de información y ficheros.",
    14: "Sistemas operativos. Características y elementos constitutivos. Sistemas Windows. Sistemas Unix y Linux. Sistemas operativos para dispositivos móviles.",
    15: "Sistemas de gestión de bases de datos relacionales, orientados a objetos y NoSQL: características y componentes. Administración de bases de datos.",
    16: "Modelo conceptual de datos. Entidades, atributos y relaciones. Reglas de modelización. Diagramas de flujo de datos. Reglas de construcción. Descomposición en niveles. Flujogramas.",
    17: "Diseño de bases de datos. Diseño lógico y físico. El modelo lógico relacional. Normalización.",
    18: "Lenguajes de programación. Representación de tipos de datos. Operadores. Instrucciones condicionales. Bucles y recursividad. Procedimientos, funciones y parámetros. Vectores y registros. Estructura de un programa.",
    19: "Lenguajes de interrogación de bases de datos. Estándar ANSI SQL. Procedimientos almacenados. Eventos y disparadores.",
    20: "Diseño y programación orientada a objetos. Elementos y componentes software: objetos, clases, herencia, métodos, sobrecarga. Ventajas e inconvenientes. Patrones de diseño y lenguaje de modelado unificado (UML).",
    21: "La arquitectura Java EE: Características de funcionamiento. Elementos constitutivos. Productos y herramientas.",
    22: "Arquitectura de sistemas cliente/servidor y multicapas: componentes y operación. Arquitecturas de servicios web y protocolos asociados.",
    23: "Aplicaciones web. Desarrollo web front-end y en servidor, multiplataforma y multidispositivo. Lenguajes: HTML, XML y sus derivaciones. Navegadores y lenguajes de programación web. Lenguajes de script.",
    24: "Desarrollo para dispositivos móviles. Frameworks nativos e híbridos.",
    25: "Accesibilidad, diseño universal y usabilidad. Acceso y usabilidad de las tecnologías, productos y servicios relacionados con la sociedad de la información. Confidencialidad y disponibilidad de la información en puestos de usuario final. Conceptos de seguridad en el desarrollo de los sistemas.",
    26: "Sistemas de almacenamiento y su virtualización. Políticas, sistemas y procedimientos de backup y su recuperación. Backup de sistemas físicos y virtuales.",
    27: "Administración del Sistema operativo y software de base. Funciones y responsabilidades. Actualización, mantenimiento y reparación del sistema operativo.",
    28: "Virtualización de sistemas y virtualización de puestos de usuario.",
    29: "Control remoto de puesto de usuario y gestión de la resolución de incidencias.",
    30: "Administración de redes de área local. Gestión de usuarios. Gestión de dispositivos. Monitorización y control de tráfico.",
    31: "Paradigmas de computación distribuida y Servicios en Cloud. IaaS, PaaS, SaaS. Nubes privadas, públicas e híbridas.",
    32: "Conceptos de seguridad de los sistemas de información. Seguridad física. Seguridad lógica. Amenazas y vulnerabilidades. Técnicas criptográficas y protocolos seguros. Mecanismos de firma digital.",
    33: "Comunicaciones. Medios de transmisión. Modos de comunicación. Equipos terminales y equipos de interconexión y conmutación. Redes de comunicaciones. Redes de conmutación y redes de difusión. Comunicaciones móviles e inalámbricas.",
    34: "El modelo TCP/IP y el modelo de referencia de interconexión de sistemas abiertos (OSI) de ISO. Protocolos TCP/IP.",
    35: "Internet: arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS y SSL/TLS.",
    36: "Seguridad y protección en redes de comunicaciones. Seguridad perimetral. Acceso remoto seguro a redes. Redes privadas virtuales (VPN). Seguridad en el puesto del usuario.",
    37: "Redes locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión.",
    38: "Sistema de radiocomunicación Trans European Trunked Radio o TEerrestrial Trunked RAdio (TETRA).",
    39: "Principios básicos del Esquema Nacional de Seguridad y el Esquema Nacional de Interoperabilidad.",
    40: "Herramientas de trabajo en grupo. Sistemas de videoconferencia. Acondicionamiento de salas y equipos.",
}

# T11 es la plantilla piloto: no tiene cabecera de inicio de la que leer título y subtítulo.
T11_TITULO = 'Informática básica. Representación y comunicación de la información'
T11_SUB = ('Elementos constitutivos de un sistema de información · Arquitectura de ordenadores · '
           'Componentes internos de los equipos microinformáticos')

PESTANAS = [('indice', 'Índice', 'list'), ('contenido', 'Contenido', 'book'), ('diagramas', 'Diagramas', 'layers'),
            ('test', 'Test', 'check-circle'), ('casos', 'Casos', 'briefcase'), ('fuentes', 'Fuentes', 'link')]
# Pestañas que no se muestran (el contenido sigue en la página, oculto). Para volver a enseñarlas, quitarlas de aquí.
# Los casos se abren con el botón «Casos» de la cabecera del tema; el banco de test lo usan el examen y los simulacros.
PESTANAS_OCULTAS = {'test', 'casos'}
MD_A_PESTANA = {'fuentes': ('fuentes', 'Fuentes'), 'diagramas': ('diagramas', 'Diagramas'), 'test': ('test', 'Test'),
                'caso-practico': ('casos', 'Casos'), 'contenido': ('contenido', 'Contenido'), 'indice': ('indice', 'Índice')}

SPRITE = '''<svg style="display:none" aria-hidden="true">
<symbol id="i-home" viewBox="0 0 24 24"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h5v-6h4v6h5V10"/></symbol>
<symbol id="i-book" viewBox="0 0 24 24"><path d="M3 5c2-1 5-1 7 0v14c-2-1-5-1-7 0V5z"/><path d="M21 5c-2-1-5-1-7 0v14c2-1 5-1 7 0V5z"/></symbol>
<symbol id="i-clipboard" viewBox="0 0 24 24"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3a1 1 0 011-1h4a1 1 0 011 1v1"/><path d="M9 11l2 2 4-4"/></symbol>
<symbol id="i-bar" viewBox="0 0 24 24"><path d="M4 20V10"/><path d="M12 20V4"/><path d="M20 20v-7"/></symbol>
<symbol id="i-gauge" viewBox="0 0 24 24"><path d="M4 18a8 8 0 1116 0"/><path d="M12 18l4-6"/></symbol>
<symbol id="i-check-circle" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/></symbol>
<symbol id="i-briefcase" viewBox="0 0 24 24"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 012-2h4a2 2 0 012 2v2"/></symbol>
<symbol id="i-list" viewBox="0 0 24 24"><path d="M8 6h13"/><path d="M8 12h13"/><path d="M8 18h13"/><circle cx="3.5" cy="6" r="1.2"/><circle cx="3.5" cy="12" r="1.2"/><circle cx="3.5" cy="18" r="1.2"/></symbol>
<symbol id="i-layers" viewBox="0 0 24 24"><path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/></symbol>
<symbol id="i-link" viewBox="0 0 24 24"><path d="M10 14a5 5 0 007 0l3-3a5 5 0 00-7-7l-1 1"/><path d="M14 10a5 5 0 00-7 0l-3 3a5 5 0 007 7l1-1"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></symbol>
<symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></symbol>
<symbol id="i-chevron-right" viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></symbol>
<symbol id="i-play" viewBox="0 0 24 24"><path d="M8 5l11 7-11 7V5z"/></symbol>
<symbol id="i-pause" viewBox="0 0 24 24"><path d="M9 5v14M15 5v14"/></symbol>
<symbol id="i-arrow-left" viewBox="0 0 24 24"><path d="M19 12H5"/><path d="M11 6l-6 6 6 6"/></symbol>
<symbol id="i-arrow-right" viewBox="0 0 24 24"><path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></symbol>
<symbol id="i-target" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/></symbol>
<symbol id="i-file-text" viewBox="0 0 24 24"><path d="M6 3h9l3 3v15H6z"/><path d="M9 12h6M9 16h6M9 8h3"/></symbol>
<symbol id="i-refresh" viewBox="0 0 24 24"><path d="M4 4v6h6"/><path d="M20 20v-6h-6"/><path d="M5 15a8 8 0 0014 3M19 9a8 8 0 00-14-3"/></symbol>
<symbol id="i-printer" viewBox="0 0 24 24"><path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M6 14h12v7H6z"/></symbol>
<symbol id="i-info" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 11v6"/><path d="M12 7.5v.5"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/></symbol>
<symbol id="i-trash" viewBox="0 0 24 24"><path d="M4 7h16"/><path d="M10 11v6M14 11v6"/><path d="M6 7l1 13h10l1-13"/><path d="M9 7V4h6v3"/></symbol>
</svg>'''

SITEIMPROVE = '''<script>
/* Siteimprove Analytics (cuenta 6277594 del Ayuntamiento). No se carga en local. */
(function(){var h=location.hostname;if(!h||h==='localhost'||h==='127.0.0.1'||h==='[::1]')return;
var s=document.createElement('script');s.async=true;s.src='https://siteimproveanalytics.com/js/siteanalyze_6277594.js';document.head.appendChild(s);})();
</script>'''


def icon(name, cls=''):
    return f'<svg class="icon {cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def head(title, desc, base, path=''):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Temario Técnico/a Auxiliar TIC · Ayuntamiento de Madrid">
<meta property="og:title" content="{html.escape(title.split(' · ')[0])}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE_URL}{path}">
<meta property="og:image" content="{SITE_URL}assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Temario de Técnico/a Auxiliar TIC del Ayuntamiento de Madrid: 40 temas, test, casos prácticos y simulacros de examen">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/img/favicon.ico" type="image/x-icon">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/app.css?v={VER}">
{SITEIMPROVE}
</head>'''


def header(base, app_href):
    return f'''<a class="skip-link" href="#contenido-principal">Saltar al contenido principal</a>
<header class="banda">
  <div class="banda-inner">
    <button type="button" class="menu-toggle" aria-label="Menú" aria-controls="sidebar" aria-expanded="false">{icon('menu')}</button>
    <img src="{base}assets/img/firma.svg" alt="Ayuntamiento de Madrid" class="banda-logo" width="140" height="38">
    <a class="banda-brand" href="{app_href}">Temario Técnico/a Auxiliar TIC</a>
    <span class="banda-spacer"></span>
    <a class="banda-link" href="{PROCESOS_URL}">Procesos selectivos TIC</a>
  </div>
</header>'''


def footer(base):
    return f'''<footer class="pie">
  <div class="pie-inner">
    <img src="{base}assets/img/firma.svg" alt="Ayuntamiento de Madrid" class="pie-logo" width="140" height="38">
    <div class="pie-text">
      <p>Temario Técnico/a Auxiliar TIC · Ayuntamiento de Madrid</p>
      <ul class="pie-links">
        <li><a href="{ACCESIBILIDAD_URL}" target="_blank" rel="noopener">Declaración de accesibilidad<span class="visually-hidden"> (se abre en una ventana nueva)</span></a></li>
        <li><a href="{PRIVACIDAD_URL}">Protección de datos</a></li>
        <li><a href="mailto:procesosselectivostic@madrid.es" target="_blank" rel="noopener" data-buzon>Buzón de sugerencias<span class="visually-hidden"> (se abre en una ventana nueva)</span></a></li>
      </ul>
    </div>
  </div>
</footer>'''


def nav_global(base, active=None, spa=False):
    items = [('progreso', 'Mi progreso', 'gauge'), ('temario', 'Temario', 'book'), ('test', 'Test', 'clipboard'), ('estadisticas', 'Estadísticas', 'bar')]
    out = '<div class="sb-section">Principal</div>'
    for key, label, ic in items:
        nav = 'stats' if key == 'estadisticas' else key
        cur = ' aria-current="page"' if active == key else ''
        href = f'#/{key}' if spa else f'{base}index.html#/{key}'
        out += f'<a class="sb-link" data-nav="{nav}" href="{href}"{cur}>{icon(ic)} {label}</a>'
    return out


AVISO = f'''<div class="aviso" role="note">{icon('info')}<p><strong>Tu progreso se guarda solo en este navegador.</strong> No hace falta registrarse y no se recoge ningún dato personal. Si cambias de navegador o de dispositivo, o borras los datos de navegación, el progreso no se conserva; puedes imprimir cada tema con tu avance.</p><button type="button">Entendido</button></div>'''


# ── Limpieza de restos de producción en el HTML aprobado ───────────────────
def tab_link(n):
    def repl(m):
        key, label = MD_A_PESTANA[m.group(1)]
        # Con la pestaña Test oculta, la remisión lleva al examen del tema.
        href = f'../index.html#/examen/{n}' if key == 'test' and 'test' in PESTANAS_OCULTAS else f'#{key}'
        return f'la pestaña <a href="{href}">{label}</a>'
    return repl


def limpiar(n, d):
    for k in ('contenido', 'diagramas', 'casos', 'fuentes', 'indiceExtra'):
        v = d.get(k) or ''
        # Pies con versión, changelog o QA de la plantilla de producción.
        v = re.sub(r'<p[^>]*>(?:(?!</p>).)*?(?:changelog\.md|validacion\.md)(?:(?!</p>).)*?</p>', '', v, flags=re.S)
        # «Nota de accesibilidad y de QA» (catálogo de diagramas del T28).
        v = re.sub(r'<h2[^>]*>\s*Nota de accesibilidad y de QA\s*</h2>.*?(?=<h2|$)', '', v, flags=re.S)
        # Frase que remite al documento de validación interno (T34).
        v = v.replace(' Están marcados como tales en el contenido y en el documento de validación, y deben reverificarse antes de cada convocatoria.', '')
        # Remisiones a los ficheros fuente del repositorio → pestañas de la página.
        # Sin tocar los espacios de alrededor (el 08-10 se perdieron en 27 sitios: «enla pestaña», «Diagramas(12…»).
        v = re.sub(r'(?:<code>)?tema-\d+-(fuentes|diagramas|test|caso-practico|contenido|indice)\.md(?:</code>)?', tab_link(n), v)
        v = re.sub(r'^\s*(?:<hr[^>]*>\s*)+', '', v)  # filete suelto al principio de la pestaña
        d[k] = v
    if n == 11:
        d['diagramas'] = d['diagramas'].replace(
            ' El código fuente completo está disponible en el fichero la pestaña <a href="#diagramas">Diagramas</a>.', '')
        d['diagramas'] = re.sub(r'<h3[^>]*>\s*Paleta de colores\s*</h3>.*?(?=<h3|$)', '', d['diagramas'], flags=re.S)
    d['diagramas'] = quitar_columna_formato(d['diagramas'])
    return d


def quitar_columna_formato(v):
    """El índice de diagramas trae una columna «Formato» (680×320…) que es dato de maquetación."""
    m = re.search(r'<table>.*?</table>', v, flags=re.S)
    if not m or 'Formato' not in m.group(0):
        return v
    soup = BeautifulSoup(m.group(0), 'html.parser')
    heads = soup.find_all('th')
    idx = next((i for i, th in enumerate(heads) if th.get_text(strip=True) == 'Formato'), None)
    if idx is None:
        return v
    for tr in soup.find_all('tr'):
        cells = tr.find_all(['th', 'td'], recursive=False)
        if len(cells) > idx:
            cells[idx].decompose()
    return v[:m.start()] + str(soup) + v[m.end():]


# ── Preguntas tipo test añadidas a los casos abiertos (opción B, 09-10-2026) ──
CASOS_TEST = os.path.join(HERE, 'datos', 'casos-test')


def bloque_test(k, n_preg):
    return (f'<div class="caso-test" data-caso="{k}"><h4 class="caso-test-t">Preguntas tipo test sobre este caso</h4>'
            f'<p class="caso-test-sub">{n_preg} preguntas con tres respuestas, como en la parte práctica del examen. Contesta y pulsa «Corregir».</p>'
            f'<div class="caso-qs"></div><div class="caso-test-acc">'
            f'<button type="button" class="btn btn-verde caso-corregir">Corregir</button>'
            f'<span class="caso-res"></span></div></div>')


def anadir_tests_casos(n, casos_html):
    """Inserta, detrás de cada caso abierto, su bloque de preguntas tipo test. Devuelve (html, datos para TEMA.casosTest)."""
    p = os.path.join(CASOS_TEST, f'tema-{n:02d}.json')
    if n == 1 or not os.path.exists(p):
        return casos_html, None
    tests = json.load(open(p, encoding='utf-8'))
    if 2 <= n <= 10:
        partes = re.split(r'(?=<div class="caso-box")', casos_html)
    elif n == 11:
        partes = ['', casos_html]
    else:
        partes = re.split(r'(?=<h2[^>]*>\s*Caso \d)', casos_html)
    cabeza, casos = partes[0], partes[1:]
    assert len(casos) == len(tests), f'T{n}: {len(casos)} casos en la pestaña y {len(tests)} en casos-test'
    out = cabeza
    for k, (h, t) in enumerate(zip(casos, tests)):
        assert t['k'] == k
        m = re.search(r'(\s*<hr[^>]*>\s*)$', h)   # el filete que separa del siguiente caso va después del test
        cuerpo, cola = (h[:m.start()], m.group(1)) if m else (h, '')
        out += cuerpo + bloque_test(k, len(t['preguntas'])) + cola
    return out, [{'preguntas': t['preguntas']} for t in tests]


# ── Página de tema ──────────────────────────────────────────────────────────
def outline(epigrafes):
    out, open_sub = ['<ul class="outline">'], False
    for i, e in enumerate(epigrafes):
        t = html.escape(e['t'])
        item = (f'<div class="ep h{e["lvl"]}"><input type="checkbox" data-ep="{e["id"]}" aria-label="Marcar como leído: {t}">'
                f'<a href="#{e["id"]}" data-ep="{e["id"]}">{t}</a></div>')
        if e['lvl'] == 2:
            if open_sub:
                out.append('</ul></li>'); open_sub = False
            elif i:
                out.append('</li>')
            out.append('<li>' + item)
        else:
            if not open_sub:
                if i == 0:
                    out.append('<li>')
                out.append('<ul>'); open_sub = True
            out.append('<li>' + item + '</li>')
    out.append('</ul></li>' if open_sub else '</li>')
    out.append('</ul>')
    return ''.join(out)


def casos_test_html(casos):
    out = ''
    for k, c in enumerate(casos):
        out += (f'<div class="caso-box" data-caso="{k}"><h3>Caso {k + 1} — {html.escape(c["titulo"])}</h3>'
                f'<div class="caso-scenario">{html.escape(c["escenario"])}</div><div class="caso-qs"></div>'
                f'<div style="display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin-top:6px">'
                f'<button type="button" class="btn btn-verde caso-corregir">Corregir caso</button>'
                f'<span class="caso-res" style="font-weight:700;color:var(--g600)"></span></div></div>')
    return out


def tema_page(t, d, prev_t, next_t):
    n, base = t['n'], '../'
    titulo = t['titulo']
    bloque_txt = 'Bloque I' if t['parte'] == 1 else 'Bloque II'
    counts = {'test': len(d['preguntas']), 'casos': 1 if n == 11 else (len(d['casosData']) if d.get('casosData') else d['plegadas'] or None)}

    tabs = ''.join(
        f'<button type="button" class="tab" role="tab" id="tab-{k}" data-tab="{k}" aria-controls="panel-{k}" aria-selected="false" tabindex="-1">'
        f'{icon(ic, "icon-sm")} {lbl}' + (f' <span class="count">{counts[k]}</span>' if counts.get(k) else '') + '</button>'
        for k, lbl, ic in PESTANAS if k not in PESTANAS_OCULTAS)
    sb_tema = ''.join(f'<a class="sb-link small" data-tab="{k}" href="#{k}">{icon(ic, "icon-sm")} {lbl}</a>' for k, lbl, ic in PESTANAS if k not in PESTANAS_OCULTAS)
    boton_casos = (f'<a class="btn btn-ghost" href="#casos" data-abrir="casos">{icon("briefcase")} Casos ({counts["casos"]})</a>'
                   if 'casos' in PESTANAS_OCULTAS else '')
    volver = ('<p class="panel-volver no-print"><a href="#indice" data-volver>← Volver al índice del tema</a></p>'
              if 'casos' in PESTANAS_OCULTAS else '')
    pager = '<div class="sb-pager">' + (
        f'<a href="tema-{prev_t:02d}.html" aria-label="Tema anterior">← Tema {prev_t}</a>' if prev_t else '') + (
        f'<a href="tema-{next_t:02d}.html" aria-label="Tema siguiente">Tema {next_t} →</a>' if next_t else '') + '</div>'

    ficha = d['ficha'] or ''
    sub = f'<p class="tema-sub">{html.escape(t["sub"])}</p>' if t['sub'] else ''
    ie = re.sub(r'(<table\b.*?</table>)', r'<div class="table-wrap">\1</div>', d['indiceExtra'] or '', flags=re.S)
    extra = f'<div class="contenido" style="margin-top:26px">{ie}</div>' if ie else ''
    casos_test = None
    if d.get('casosData'):
        casos = '<div class="contenido">' + casos_test_html(d['casosData']) + '</div>'
        casos_intro = 'Cada caso plantea un supuesto del Ayuntamiento de Madrid con preguntas tipo test. Contesta y pulsa «Corregir caso».'
    else:
        casos_html, casos_test = anadir_tests_casos(n, d['casos'])
        casos = f'<div class="contenido">{casos_html}</div>'
        casos_intro = ('Supuestos aplicados al Ayuntamiento de Madrid. Intenta resolver cada cuestión antes de desplegar la solución orientativa'
                       + (' y practica después con las preguntas tipo test de cada caso.' if casos_test else '.'))

    desc = f'Tema {n} del temario de Técnico/a Auxiliar TIC del Ayuntamiento de Madrid: {titulo}.'
    tema_js = {'n': n, 'preguntas': d['preguntas']}
    if d.get('casosData'):
        tema_js['casosTest'] = d['casosData']
    elif casos_test:
        tema_js['casosTest'] = casos_test
    tema_json = json.dumps(tema_js, ensure_ascii=False).replace('</', '<\\/')

    return f'''{head(f"Tema {n} — {titulo} · Temario TIC C1 · Ayuntamiento de Madrid", desc, base, f'temas/tema-{n:02d}.html')}
<body data-page="tema" data-base="{base}" data-v="{VER}" data-ocultas="{','.join(sorted(PESTANAS_OCULTAS))}">
{SPRITE}
{header(base, base + 'index.html#/progreso')}
<div class="app">
  <aside class="sidebar" id="sidebar" aria-label="Navegación">
    <nav class="sb-nav">
      {nav_global(base, 'temario')}
      <div class="sb-section">Tema {n} · {bloque_txt}</div>
      <div class="sb-tema">{sb_tema}</div>
      {pager}
    </nav>
  </aside>
  <div class="overlay"></div>
  <main class="main" id="contenido-principal" tabindex="-1">
    <div class="main-header">
      <nav class="breadcrumb" aria-label="Ruta">
        <a href="{base}index.html#/progreso" aria-label="Mi progreso">{icon('home')}</a> <span aria-hidden="true">›</span>
        <a href="{base}index.html#/temario">Temario</a> <span aria-hidden="true">›</span> <span aria-current="page">Tema {n}</span>
      </nav>
    </div>
    <div class="main-body">
      {AVISO}
      <section class="card tema-hero" aria-labelledby="tema-titulo">
        <div class="print-membrete print-only"><img src="{base}assets/img/firma-azul.svg" alt="Ayuntamiento de Madrid" width="178" height="49"><span>Temario Técnico/a Auxiliar TIC</span></div>
        <div class="tema-eyebrow"><span class="badge badge-azul">Tema {n} · {bloque_txt}</span><span class="badge badge-gris">{len(d['preguntas'])} preguntas de test</span></div>
        <h1 id="tema-titulo">{html.escape(titulo)}</h1>
        {sub}
        <div class="tema-oficial"><strong>Enunciado oficial del programa</strong> (BOAM n.º 10.032, de 23 de diciembre de 2025): {html.escape(OFICIAL[n])}</div>
        {ficha}
        <div class="tema-avance no-print"><div class="progress-bar"><div class="progress-fill verde avance-fill" style="width:0"></div></div><span class="tema-avance-txt avance-txt"></span></div>
        <div class="avance-print print-only" hidden></div>
        <div class="tema-acciones">
          <button type="button" class="btn btn-azul" id="imprimir">{icon('printer')} Imprimir / Guardar PDF</button>
          <a class="btn btn-ghost" href="{base}index.html#/examen/{n}">{icon('clock')} Examen de este tema</a>
          {boton_casos}
        </div>
      </section>

      <div class="tabs" role="tablist" aria-label="Partes del tema">{tabs}</div>

      <section class="panel" id="panel-indice" role="tabpanel" aria-labelledby="tab-indice">
        <h2 class="print-only print-title">Índice</h2>
        <div class="panel-card">
          <p class="outline-help no-print">Marca cada epígrafe cuando lo hayas estudiado. Tu avance aparece en «Mi progreso» y en la cabecera al imprimir el tema.</p>
          {outline(d['epigrafes'])}
          {extra}
        </div>
      </section>

      <section class="panel" id="panel-contenido" role="tabpanel" aria-labelledby="tab-contenido">
        <h2 class="print-only print-title">Contenido</h2>
        <div class="panel-card contenido">{d['contenido']}</div>
      </section>

      <section class="panel" id="panel-diagramas" role="tabpanel" aria-labelledby="tab-diagramas">
        <h2 class="print-only print-title">Diagramas</h2>
        <div class="panel-card contenido">{d['diagramas']}</div>
      </section>

      <section class="panel" id="panel-test" role="tabpanel" aria-label="Test del tema">
        <div class="test-bar">
          <div class="kpi">Contestadas<b id="banco-cont">0 / {len(d['preguntas'])}</b></div>
          <div class="kpi">Nota<b id="banco-res">—</b></div>
          <div class="kpi" id="banco-detalle" style="text-transform:none;letter-spacing:0">Cada error resta 1/3 de acierto</div>
          <span class="spacer"></span>
          <button type="button" class="btn btn-verde" id="banco-corregir">{icon('check')} Corregir</button>
          <button type="button" class="btn btn-ghost" id="banco-reiniciar">{icon('refresh')} Reiniciar</button>
        </div>
        <p class="page-sub">Banco completo del tema: {len(d['preguntas'])} preguntas con tres respuestas. Contesta las que quieras y pulsa «Corregir»: verás la nota calculada como en el examen y la explicación de cada pregunta. Para un test corto y cronometrado, usa <a href="{base}index.html#/examen/{n}">el examen de este tema</a>.</p>
        <div id="banco"></div>
      </section>

      <section class="panel" id="panel-casos" role="tabpanel" aria-label="Casos prácticos">
        <h2 class="print-only print-title">Casos prácticos</h2>
        {volver}
        <p class="page-sub no-print">{casos_intro}</p>
        <div class="panel-card">{casos}</div>
      </section>

      <section class="panel" id="panel-fuentes" role="tabpanel" aria-labelledby="tab-fuentes">
        <h2 class="print-only print-title">Fuentes</h2>
        <div class="panel-card contenido">{d['fuentes']}</div>
      </section>
    </div>
  </main>
</div>
{footer(base)}
<script>window.TEMA = {tema_json};</script>
<script src="{base}assets/js/temas.js?v={VER}"></script>
<script src="{base}assets/js/app.js?v={VER}"></script>
</body>
</html>
'''


VER = ''


def version():
    """Huella de CSS, JS y datos: cambia la URL de los recursos en cada publicación (GitHub Pages cachea 10 min)."""
    h = hashlib.sha1()
    for p in [os.path.join(REPO, 'assets', 'css', 'app.css'), os.path.join(REPO, 'assets', 'js', 'app.js'),
              os.path.join(HERE, 'datos', 'simulacro-practico.json')] + sorted(os.path.join(EXTRACT, f) for f in os.listdir(EXTRACT)):
        if os.path.exists(p):
            h.update(open(p, 'rb').read())
    return h.hexdigest()[:10]


def main():
    global VER
    VER = version()
    temas, datos = [], {}
    for n in range(1, 41):
        d = json.load(open(os.path.join(EXTRACT, f'tema-{n:02d}.json'), encoding='utf-8'))
        d = limpiar(n, d)
        if n == 11:
            titulo, sub = T11_TITULO, T11_SUB
        else:
            titulo = re.sub(r'^Tema \d+\s*[—–-]\s*', '', d['titulo']).strip()
            sub = d['subtitulo'] or ''
        temas.append({'n': n, 'parte': 1 if n <= 10 else 2, 'titulo': titulo, 'oficial': OFICIAL[n], 'sub': sub,
                      'nPreg': len(d['preguntas']), 'nEp': len(d['epigrafes'])})
        datos[n] = d

    os.makedirs(os.path.join(REPO, 'temas'), exist_ok=True)
    os.makedirs(os.path.join(REPO, 'assets', 'data'), exist_ok=True)
    for i, t in enumerate(temas):
        page = tema_page(t, datos[t['n']], temas[i - 1]['n'] if i else None, temas[i + 1]['n'] if i < 39 else None)
        with open(os.path.join(REPO, 'temas', f'tema-{t["n"]:02d}.html'), 'w', encoding='utf-8') as f:
            f.write(page)

    with open(os.path.join(REPO, 'assets', 'js', 'temas.js'), 'w', encoding='utf-8') as f:
        f.write('/* Catálogo de los 40 temas (generado por herramientas/generar_web.py) */\nwindow.TEMAS = '
                + json.dumps(temas, ensure_ascii=False, indent=0) + ';\n')
    with open(os.path.join(REPO, 'assets', 'data', 'preguntas.json'), 'w', encoding='utf-8') as f:
        json.dump({str(n): datos[n]['preguntas'] for n in datos}, f, ensure_ascii=False, separators=(',', ':'))
    sp = os.path.join(HERE, 'datos', 'simulacro-practico.json')
    if os.path.exists(sp):
        shutil.copy(sp, os.path.join(REPO, 'assets', 'data', 'simulacro-practico.json'))

    tpl = open(os.path.join(HERE, 'plantillas', 'index.html'), encoding='utf-8').read()
    total = sum(t['nPreg'] for t in temas)
    page = (tpl.replace('{{HEAD}}', head('Temario de Técnico/a Auxiliar TIC · Ayuntamiento de Madrid',
                                         'Temario de los 40 temas de Técnico/a Auxiliar TIC del Ayuntamiento de Madrid, con test, casos prácticos y simulacros de examen.', ''))
            .replace('{{SPRITE}}', SPRITE).replace('{{HEADER}}', header('', '#/inicio'))
            .replace('{{NAV}}', nav_global('', spa=True)).replace('{{AVISO}}', AVISO)
            .replace('{{FOOTER}}', footer('')).replace('{{TOTAL_PREGUNTAS}}', f'{total:,}'.replace(',', '.'))
            .replace('{{PROCESOS_URL}}', PROCESOS_URL).replace('{{VER}}', VER))
    with open(os.path.join(REPO, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'versión {VER}')
    print(f'OK · 40 temas · {total} preguntas · {sum(t["nEp"] for t in temas)} epígrafes')


if __name__ == '__main__':
    main()
