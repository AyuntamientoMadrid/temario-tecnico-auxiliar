"""Genera el PDF de cada tema con la misma impresión que la web (variante δ aprobada).

Sirve el repositorio por HTTP, abre temas/tema-NN.html en Chromium, marca los paneles de
impresión igual que el evento beforeprint de app.js y despliega las soluciones de los casos.
Salida: temario/{administrativo,tecnico}/tema-NN/tema-NN.pdf

Uso: python3 herramientas/generar_pdf.py [N ...]   (requiere playwright + chromium)
"""
import functools
import http.server
import os
import sys
import threading

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..'))
PORT = 8765

PIE = ('<div style="font-size:8px;width:100%;padding:0 14mm;color:#555;display:flex;justify-content:space-between">'
       '<span>Temario TIC C1 · Ayuntamiento de Madrid · Tema {n}</span>'
       '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')


def servir():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=REPO)
    h.log_message = lambda *a, **k: None
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', PORT), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def main(temas):
    srv = servir()
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        for n in temas:
            pg.goto(f'http://127.0.0.1:{PORT}/temas/tema-{n:02d}.html', wait_until='networkidle')
            pg.evaluate("""() => {
              ['indice','contenido','diagramas','casos','fuentes'].forEach((k, i) => {
                const el = document.getElementById('panel-' + k);
                if (el) { el.classList.add('print'); if (i === 0) el.classList.add('first'); }
              });
              document.querySelectorAll('.avance-print').forEach(e => e.hidden = true);
              document.querySelectorAll('details').forEach(d => d.open = true);
            }""")
            pg.emulate_media(media='print')
            bloque = 'administrativo' if n <= 10 else 'tecnico'
            out = os.path.join(REPO, 'temario', bloque, f'tema-{n:02d}', f'tema-{n:02d}.pdf')
            pg.pdf(path=out, format='A4', print_background=True, display_header_footer=True,
                   header_template='<span></span>', footer_template=PIE.format(n=n),
                   margin={'top': '16mm', 'bottom': '18mm', 'left': '14mm', 'right': '14mm'})
            print(f'T{n:02d}: {os.path.getsize(out) // 1024} KB')
        br.close()
    srv.shutdown()


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or range(1, 41))
