"""Exporta el temario y las baterías de test de la entrega a Markdown y JSON.

Entrada:  herramientas/datos/extract/tema-NN.json      (versión aprobada, la misma que pinta la web)
          herramientas/datos/casos-test/tema-NN.json   (preguntas tipo test de los casos)
          herramientas/datos/simulacro-practico.json
Salida:   temario/{administrativo,tecnico}/tema-NN/tema-NN.md (+ diagramas/*.svg)
          tests/{administrativo,tecnico}/tema-NN.{json,md}
          tests/simulacro-practico.{json,md}

La limpieza es la de generar_web.py (limpiar), así que el Markdown
dice lo mismo que la web. Requiere pandoc.

Uso: python3 herramientas/exportar_md.py
"""
import json
import os
import re
import shutil
import subprocess
import sys

from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.join(HERE, 'datos')
sys.path.insert(0, HERE)
import generar_web as b  # noqa: E402

REPO = os.path.normpath(os.path.join(HERE, '..'))
LETRAS = 'abc'


def bloque(n):
    return 'administrativo' if n <= 10 else 'tecnico'


def a_md(html_txt, shift=0):
    args = ['pandoc', '-f', 'html', '-t', 'gfm-raw_html+pipe_tables', '--wrap=none']
    if shift:
        args.append(f'--shift-heading-level-by={shift}')
    out = subprocess.run(args, input=html_txt, capture_output=True, text=True, check=True).stdout
    return re.sub(r'\n{3,}', '\n\n', out).strip() + '\n'


def limpiar_html(h, dir_diag, pref, contador):
    """Quita los controles de la web y saca los SVG a ficheros enlazados como imagen."""
    soup = BeautifulSoup(h, 'html.parser')
    for sel in ('.leido-wrap', '.ep-done-mark', 'button', 'input', '.no-print'):
        for el in soup.select(sel):
            el.decompose()
    for svg in soup.find_all('svg'):
        if svg.find('use') and not svg.find(['rect', 'path', 'text', 'line']):
            svg.decompose()   # icono de la interfaz
            continue
        contador[0] += 1
        nombre = f'{pref}-{contador[0]:02d}.svg'
        if not svg.get('xmlns'):
            svg['xmlns'] = 'http://www.w3.org/2000/svg'
        os.makedirs(dir_diag, exist_ok=True)
        with open(os.path.join(dir_diag, nombre), 'w', encoding='utf-8') as f:
            f.write(str(svg))
        img = soup.new_tag('img', src=f'diagramas/{nombre}', alt=svg.get('aria-label') or 'Diagrama')
        svg.replace_with(img)
    # Las remisiones a pestañas de la web no tienen destino en el Markdown.
    for a in soup.find_all('a'):
        if (a.get('href') or '').startswith('#'):
            a.unwrap()
    # La solución orientativa va plegada en la web; en el Markdown se muestra entera.
    for det in soup.find_all('details'):
        s = det.find('summary')
        if s:
            s.decompose()   # «Ver solución orientativa»: etiqueta del botón
        det.unwrap()
    # Cajas «Dato clave», «Ejemplo»… → cita con la etiqueta en negrita.
    for c in soup.select('div.callout'):
        k = c.select_one('.kicker')
        if k:
            k.name = 'strong'
            k.string = k.get_text(strip=True).capitalize() + '.'
            k.insert_after(' ')
            del k['class']
        c.name = 'blockquote'
        del c['class']
    return str(soup)


def pregunta_json(i, p):
    return {
        'numero': i,
        'pregunta': p['q'],
        'opciones': {LETRAS[k]: o for k, o in enumerate(p['o'])},
        'correcta': LETRAS[p['c']],
        'referencia': p.get('r') or '',
        'explicacion': p.get('e') or '',
    }


def pregunta_md(i, p, nivel='###'):
    out = [f'{nivel} {i}. {p["q"]}', '']
    out += [f'- {LETRAS[k]}) {o}' for k, o in enumerate(p['o'])]
    out.append('')
    linea = f'**Respuesta correcta:** {LETRAS[p["c"]]})'
    if p.get('r'):
        linea += f' · **Referencia:** {p["r"]}'
    out.append(linea)
    if p.get('e'):
        out += ['', p['e']]
    out.append('')
    return '\n'.join(out)


def partir_casos(n, casos_html):
    """Mismo corte que build_v3.anadir_tests_casos."""
    if 2 <= n <= 10:
        partes = re.split(r'(?=<div class="caso-box")', casos_html)
    elif n == 11:
        partes = ['', casos_html]
    else:
        partes = re.split(r'(?=<h2[^>]*>\s*Caso \d)', casos_html)
    return partes[0], partes[1:]


def exportar_tema(n):
    d = json.load(open(os.path.join(V3, 'extract', f'tema-{n:02d}.json'), encoding='utf-8'))
    d = b.limpiar(n, d)
    titulo = b.T11_TITULO if n == 11 else re.sub(r'^Tema \d+\s*[—–-]\s*', '', d['titulo']).strip()
    dir_t = os.path.join(REPO, 'temario', bloque(n), f'tema-{n:02d}')
    dir_diag = os.path.join(dir_t, 'diagramas')
    shutil.rmtree(dir_diag, ignore_errors=True)   # el PDF del tema (generar_pdf) se conserva
    os.makedirs(dir_t, exist_ok=True)

    casos_test = None
    p = os.path.join(V3, 'casos-test', f'tema-{n:02d}.json')
    if n != 1 and os.path.exists(p):
        casos_test = json.load(open(p, encoding='utf-8'))

    md = [f'# Tema {n}. {titulo}', '',
          f'**Bloque:** {"administrativo" if n <= 10 else "técnico"}  ',
          f'**Enunciado oficial** (BOAM n.º 10.032, de 23 de diciembre de 2025): {b.OFICIAL[n]}', '',
          f'Versión web: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-{n:02d}.html> · '
          f'PDF: [tema-{n:02d}.pdf](tema-{n:02d}.pdf) · Test: [../../../tests/{bloque(n)}/tema-{n:02d}.md](../../../tests/{bloque(n)}/tema-{n:02d}.md)', '']

    md += ['## Índice', '']
    for e in d['epigrafes']:
        md.append(('  ' if e['lvl'] > 2 else '') + f'- {e["t"]}')
    md.append('')
    if d.get('indiceExtra'):
        md += [a_md(limpiar_html(d['indiceExtra'], dir_diag, 'indice', [0]), shift=1), '']

    md += ['## Contenido', '', a_md(limpiar_html(d['contenido'], dir_diag, 'contenido', [0]), shift=1), '']
    if d.get('diagramas'):
        md += ['## Diagramas', '', a_md(limpiar_html(d['diagramas'], dir_diag, 'diagrama', [0]), shift=1), '']

    md += ['## Casos prácticos', '']
    if n == 1:
        for k, c in enumerate(d['casosData']):
            md += [f'### Caso {k + 1}. {c["titulo"]}', '', c['escenario'], '']
            md += [pregunta_md(i, q, '####') for i, q in enumerate(c['preguntas'], 1)]
    else:
        cabeza, casos = partir_casos(n, d['casos'] or '')
        if cabeza.strip():
            md += [a_md(limpiar_html(cabeza, dir_diag, 'caso', [0]), shift=1)]
        for k, h in enumerate(casos):
            md.append(a_md(limpiar_html(h, dir_diag, f'caso{k + 1}', [0]), shift=1))
            if casos_test:
                md += ['#### Preguntas tipo test sobre este caso', '']
                md += [pregunta_md(i, q, '#####') for i, q in enumerate(casos_test[k]['preguntas'], 1)]
    md.append('')

    if d.get('fuentes'):
        md += ['## Fuentes', '', a_md(limpiar_html(d['fuentes'], dir_diag, 'fuente', [0]), shift=1)]

    with open(os.path.join(dir_t, f'tema-{n:02d}.md'), 'w', encoding='utf-8') as f:
        f.write(re.sub(r'\n{3,}', '\n\n', '\n'.join(md)))

    # Batería de test del tema (+ preguntas de los casos).
    dir_test = os.path.join(REPO, 'tests', bloque(n))
    os.makedirs(dir_test, exist_ok=True)
    pregs = d['preguntas']
    if n == 1:
        casos_q = [{'caso': k + 1, 'titulo': c['titulo'], 'preguntas': c['preguntas']} for k, c in enumerate(d['casosData'])]
    else:
        titulos = [re.sub(r'^Caso \d+\s*[—.:-]\s*', '', BeautifulSoup(h, 'html.parser').find(['h2', 'h3']).get_text(' ', strip=True))
                   if BeautifulSoup(h, 'html.parser').find(['h2', 'h3']) else f'Caso {k + 1}'
                   for k, h in enumerate(partir_casos(n, d['casos'] or '')[1])]
        casos_q = [{'caso': k + 1, 'titulo': titulos[k] if k < len(titulos) else '', 'preguntas': c['preguntas']}
                   for k, c in enumerate(casos_test or [])]
    doc = {
        'tema': n, 'bloque': bloque(n), 'titulo': titulo, 'enunciado_oficial': b.OFICIAL[n],
        'calificacion': '+1 acierto, -1/3 error, 0 en blanco (BOAM 10.032, base 5.2)',
        'preguntas': [pregunta_json(i, q) for i, q in enumerate(pregs, 1)],
        'casos': [{'caso': c['caso'], 'titulo': c['titulo'],
                   'preguntas': [pregunta_json(i, q) for i, q in enumerate(c['preguntas'], 1)]} for c in casos_q],
    }
    with open(os.path.join(dir_test, f'tema-{n:02d}.json'), 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    tmd = [f'# Test del tema {n}. {titulo}', '',
           f'{len(pregs)} preguntas con tres opciones y una sola correcta. Calificación como en el examen: '
           '+1 por acierto, −1/3 por error, 0 en blanco.', '',
           f'Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-{n:02d}.html>', '',
           '## Batería de preguntas', '']
    tmd += [pregunta_md(i, q) for i, q in enumerate(pregs, 1)]
    if casos_q:
        tmd += ['## Preguntas sobre los casos prácticos', '']
        for c in casos_q:
            tmd += [f'### Caso {c["caso"]}. {c["titulo"]}', '']
            tmd += [pregunta_md(i, q, '####') for i, q in enumerate(c['preguntas'], 1)]
    with open(os.path.join(dir_test, f'tema-{n:02d}.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(tmd))
    return len(pregs), sum(len(c['preguntas']) for c in casos_q), len(casos_q)


def exportar_simulacro():
    s = json.load(open(os.path.join(V3, 'simulacro-practico.json'), encoding='utf-8'))
    dir_test = os.path.join(REPO, 'tests')
    shutil.copy(os.path.join(V3, 'simulacro-practico.json'), os.path.join(dir_test, 'simulacro-practico.json'))
    enun = s['enunciado'] if isinstance(s['enunciado'], list) else [s['enunciado']]
    md = [f'# Simulacro práctico. {s["titulo"].replace("Caso práctico: ", "")}', '',
          'Supuesto y 30 preguntas tipo test, con el formato de la parte práctica del examen (Grupo II).', '',
          '## Supuesto', ''] + [p + '\n' for p in enun] + ['## Preguntas', '']
    md += [pregunta_md(i, q) for i, q in enumerate(s['preguntas'], 1)]
    with open(os.path.join(dir_test, 'simulacro-practico.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    return len(s['preguntas'])


def main():
    shutil.rmtree(os.path.join(REPO, 'tests'), ignore_errors=True)
    tot = [0, 0, 0]
    for n in range(1, 41):
        r = exportar_tema(n)
        tot = [a + c for a, c in zip(tot, r)]
        print(f'T{n:02d}: {r[0]} preguntas · {r[2]} casos · {r[1]} preguntas de casos')
    sim = exportar_simulacro()
    print(f'TOTAL: {tot[0]} preguntas · {tot[2]} casos · {tot[1]} preguntas de casos · simulacro práctico {sim}')


if __name__ == '__main__':
    main()
