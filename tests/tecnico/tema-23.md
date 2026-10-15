# Test del tema 23. Aplicaciones web

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-23.html>

## Batería de preguntas

### 1. ¿Qué distingue fundamentalmente a una aplicación web de una página web estática?

- a) Procesa datos, mantiene estado y reacciona a la interacción del usuario
- b) Únicamente que usa HTML5 en lugar de versiones anteriores de HTML
- c) Que requiere instalación de software específico en el equipo del usuario

**Respuesta correcta:** a) · **Referencia:** §1.1 [WHATWG-HTML]

Una página estática es de solo lectura; una aplicación web añade procesamiento, estado e interacción, con lógica ejecutada en el servidor y/o en el cliente.

### 2. ¿Qué marca la transición de la Web 1.0 a la Web 2.0?

- a) La sustitución completa de HTML por XML
- b) La adopción de AJAX para actualizar contenido sin recargar la página completa
- c) La generalización de HTTPS frente a HTTP

**Respuesta correcta:** b) · **Referencia:** §1.1 [WHATWG-HTML]

La Web 2.0 se caracteriza por la interactividad y el contenido generado por el usuario, posible gracias a peticiones asíncronas que evitan recargar la página entera.

### 3. ¿Cuál es una ventaja de las aplicaciones web frente a las de escritorio?

- a) Mejor acceso directo al hardware del dispositivo
- b) Menor dependencia de la conectividad de red
- c) No requieren instalación ni actualización manual por parte del usuario

**Respuesta correcta:** c) · **Referencia:** §1.2 [WHATWG-HTML]

El servidor sirve siempre la última versión; el usuario no gestiona parches ni instaladores distintos por sistema operativo.

### 4. En el modelo cliente-servidor, ¿qué papel desempeña el cliente?

- a) Inicia la comunicación solicitando un recurso o una acción
- b) Permanece a la escucha, procesando peticiones entrantes
- c) Ambos roles son intercambiables en cada petición HTTP

**Respuesta correcta:** a) · **Referencia:** §1.3.1 [FIELDING2000]

El servidor es quien permanece a la escucha y responde; el cliente (típicamente el navegador) es quien inicia cada petición.

### 5. ¿Qué significa que HTTP sea un protocolo «sin estado» (stateless)?

- a) No puede usarse para transmitir datos binarios
- b) Cada petición se procesa de forma independiente, sin memoria de peticiones anteriores
- c) Solo puede establecerse una conexión TCP por servidor

**Respuesta correcta:** b) · **Referencia:** §1.3.1 [RFC9110]

Toda «sesión» percibida por el usuario se construye con mecanismos añadidos (cookies, tokens), no es una propiedad nativa de HTTP.

### 6. ¿Cuál de las siguientes afirmaciones es correcta?

- a) La Web es uno de los servicios que se ejecutan sobre la infraestructura de Internet
- b) Internet y la Web son sinónimos exactos
- c) La Web es la infraestructura y HTTP uno de sus servicios

**Respuesta correcta:** a) · **Referencia:** §2.1 [WHATWG-HTML]

Internet es la red (TCP/IP); la Web, el correo o el FTP son servicios distintos que corren sobre esa red.

### 7. ¿Cuál es la relación correcta entre URI y URL?

- a) Toda URL es un URI, pero no todo URI es una URL
- b) Todo URI es una URL, pero no toda URL es un URI
- c) Son términos completamente independientes, sin relación de inclusión

**Respuesta correcta:** a) · **Referencia:** §2.2 [RFC3986]

URI identifica un recurso (puede ser solo un nombre, como un URN); URL además indica cómo localizarlo.

### 8. En la URL <code>https://sede.madrid.es/portal/cita?ano=2026</code>, ¿qué parte es <code>ano=2026</code>?

- a) El fragmento
- b) La ruta (path)
- c) La query string (cadena de consulta)

**Respuesta correcta:** c) · **Referencia:** §2.2 [RFC3986]

Los parámetros clave-valor tras el símbolo <code>?</code> forman la query string; el fragmento, si existiera, iría tras <code>#</code> y no se envía al servidor.

### 9. ¿Qué método HTTP es el adecuado para reemplazar por completo un recurso existente de forma idempotente?

- a) POST
- b) PATCH
- c) PUT

**Respuesta correcta:** c) · **Referencia:** §2.3.1 [RFC9110]

PUT reemplaza el recurso completo y es idempotente (repetirlo dos veces deja el mismo resultado); POST no es idempotente y PATCH modifica solo parcialmente.

### 10. Un ciudadano autenticado en la sede electrónica intenta consultar un expediente que no le pertenece. ¿Qué código de estado HTTP es el correcto?

- a) 403 Forbidden
- b) 401 Unauthorized
- c) 500 Internal Server Error

**Respuesta correcta:** a) · **Referencia:** §2.3.1 [RFC9110]

El servidor sabe quién es (está autenticado), pero no tiene autorización sobre ese recurso concreto; 401 correspondería a no estar autenticado.

### 11. ¿Qué protocolo introdujo QUIC como sustituto de TCP en el transporte?

- a) HTTP/1.1
- b) HTTP/2
- c) HTTP/3

**Respuesta correcta:** c) · **Referencia:** §2.3 [RFC9114]

HTTP/3 se apoya en QUIC (sobre UDP), eliminando el bloqueo de cabeza de línea a nivel de transporte que persistía en HTTP/2 pese a su multiplexación sobre una única conexión TCP.

### 12. ¿Cuál es la responsabilidad de CSS en el front-end?

- a) La estructura semántica del documento
- b) La presentación: color, tipografía y disposición espacial
- c) La lógica de comportamiento e interactividad

**Respuesta correcta:** b) · **Referencia:** §3.2.1 [W3C-CSS]

HTML aporta estructura y JavaScript comportamiento; CSS es responsable exclusivamente de la presentación.

### 13. ¿Qué metaetiqueta es imprescindible para que las media queries funcionen correctamente en un dispositivo móvil?

- a) <code>&lt;meta name="description"&gt;</code>
- b) <code>&lt;meta charset="UTF-8"&gt;</code>
- c) <code>&lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;</code>

**Respuesta correcta:** c) · **Referencia:** §3.3.1 [MDN-CSS]

Sin ella, el navegador móvil simula una anchura de escritorio y luego reduce la página, invalidando las media queries basadas en el ancho real de pantalla.

### 14. ¿Cuál de los siguientes es uno de los cuatro principios WCAG (POUR)?

- a) Operable
- b) Portable
- c) Optimizado

**Respuesta correcta:** a) · **Referencia:** §3.3.2 [WCAG22]

Los cuatro principios son Perceptible, Operable, Comprensible y Robusto; «Operable» exige que la interfaz pueda manejarse, por ejemplo, íntegramente por teclado.

### 15. Según el RD 1112/2018, ¿qué nivel de las WCAG deben cumplir los sitios web del sector público en España?

- a) Nivel A
- b) Nivel AAA
- c) Nivel AA

**Respuesta correcta:** c) · **Referencia:** §3.3.3 [RD1112-2018]

El Real Decreto exige el nivel AA (o superior) de las WCAG, más el requisito adicional de publicar una declaración de accesibilidad revisable.

### 16. ¿Qué diferencia principal existe entre <code>localStorage</code> y <code>sessionStorage</code>?

- a) <code>localStorage</code> se envía automáticamente en cada petición HTTP y <code>sessionStorage</code> no
- b) <code>sessionStorage</code> desaparece al cerrar la pestaña; <code>localStorage</code> persiste indefinidamente hasta borrado explícito
- c) <code>sessionStorage</code> tiene mayor capacidad de almacenamiento que <code>localStorage</code>

**Respuesta correcta:** b) · **Referencia:** §3.4 [MDN-JS]

Ambos comparten la misma API (<code>setItem</code>/<code>getItem</code>), pero difieren en el ciclo de vida de los datos; ninguno de los dos se envía automáticamente al servidor, a diferencia de las cookies.

### 17. ¿Cuál es el objetivo del Responsive Web Design (RWD)?

- a) Servir versiones de código HTML completamente distintas según el dispositivo detectado
- b) Sustituir HTML por una aplicación nativa instalada en el dispositivo
- c) Que una única base de código HTML/CSS se reorganice según el tamaño de pantalla mediante media queries

**Respuesta correcta:** c) · **Referencia:** §3.3.1 [MDN-CSS]

Frente al diseño adaptativo (varias maquetaciones fijas predefinidas), el RWD usa una única maquetación fluida.

### 18. ¿Qué separa el patrón <code>addEventListener</code> frente a asignar un manejador con el atributo <code>onclick</code>?

- a) <code>addEventListener</code> permite registrar varios manejadores para el mismo evento sin sobrescribirse
- b) <code>onclick</code> es más moderno y sustituye completamente a <code>addEventListener</code>
- c) <code>addEventListener</code> solo funciona con eventos de teclado, no de ratón

**Respuesta correcta:** a) · **Referencia:** §3.2.1 [MDN-JS]

Además, separa mejor el comportamiento (JS) de la estructura (HTML), reforzando el principio de separación de responsabilidades.

### 19. ¿Qué mecanismo de caché evita repetir peticiones HTTP de recursos que no han cambiado?

- a) <code>sessionStorage</code>
- b) IndexedDB
- c) Cabeceras <code>Cache-Control</code> y validadores como <code>ETag</code>

**Respuesta correcta:** c) · **Referencia:** §3.4 [MDN-HTTP]

La caché HTTP gobernada por estas cabeceras mejora el rendimiento percibido y es la base sobre la que se construye el funcionamiento offline de una PWA mediante la Cache API.

### 20. ¿De qué lenguaje deriva HTML originalmente?

- a) De XML
- b) De SGML
- c) De ECMAScript

**Respuesta correcta:** b) · **Referencia:** §4.1 [WHATWG-HTML]

HTML fue creado por Tim Berners-Lee en 1991 como un lenguaje de marcado derivado de SGML (Standard Generalized Markup Language).

### 21. Desde 2019, ¿cuál es la única fuente normativa de referencia de HTML?

- a) El WHATWG Living Standard
- b) La recomendación HTML5.2 del W3C
- c) La especificación XHTML 1.1

**Respuesta correcta:** a) · **Referencia:** §4.1 [WHATWG-HTML]

El W3C y el WHATWG acordaron en 2019 que el Living Standard, en evolución continua, sustituye al antiguo modelo de recomendaciones numeradas fijas.

### 22. ¿Dónde deben declararse los metadatos de un documento HTML, como el <code>&lt;title&gt;</code> o el <code>&lt;meta charset&gt;</code>?

- a) Dentro de <code>&lt;head&gt;</code>
- b) Dentro de <code>&lt;body&gt;</code>, al principio del documento
- c) En un fichero externo enlazado con <code>&lt;link rel="metadata"&gt;</code>

**Respuesta correcta:** a) · **Referencia:** §4.2.1 [WHATWG-HTML]

Los metadatos no se muestran en el cuerpo visible de la página y residen exclusivamente en <code>&lt;head&gt;</code>.

### 23. ¿Cuál de las siguientes es una etiqueta semántica introducida por HTML5 para el contenido principal, único por página?

- a) <code>&lt;div id="main"&gt;</code>
- b) <code>&lt;content&gt;</code>
- c) <code>&lt;main&gt;</code>

**Respuesta correcta:** c) · **Referencia:** §4.3.1 [WHATWG-HTML]

Frente al uso indiscriminado de <code>&lt;div&gt;</code> genéricos, HTML5 introduce <code>&lt;main&gt;</code> para describir explícitamente el contenido principal, único por página.

### 24. ¿Qué ventaja aportan principalmente las etiquetas semánticas de HTML5?

- a) Cambian automáticamente la apariencia visual por defecto de la página
- b) Mejoran la accesibilidad y el SEO al describir la estructura a máquinas, no solo a humanos
- c) Sustituyen por completo la necesidad de escribir CSS

**Respuesta correcta:** b) · **Referencia:** §4.3.1 [WHATWG-HTML]

No cambian la apariencia por defecto (siguen pudiendo estilizarse como cualquier <code>&lt;div&gt;</code>), pero sí el significado que transmiten a lectores de pantalla y buscadores.

### 25. ¿Qué atributo HTML5 permite validar en el navegador, sin JavaScript, que un campo cumple una expresión regular?

- a) <code>required</code>
- b) <code>validate</code>
- c) <code>pattern</code>

**Respuesta correcta:** c) · **Referencia:** §4.3.2 [WHATWG-HTML]

El atributo <code>pattern</code> acepta una expresión regular que el navegador valida de forma nativa; <code>required</code> solo exige que el campo no esté vacío, sin comprobar su formato.

### 26. ¿Cuál es la diferencia esencial entre HTML y XML?

- a) XML no puede representar texto, solo datos binarios
- b) HTML tiene un vocabulario fijo de etiquetas; XML permite definir vocabularios propios
- c) HTML es más estricto sintácticamente que XML

**Respuesta correcta:** b) · **Referencia:** §5.1 [XML10]

XML es un metalenguaje: no define ninguna etiqueta propia, a diferencia del conjunto predeterminado de HTML.

### 27. ¿Qué diferencia «bien formado» de «válido» en un documento XML?

- a) Son sinónimos exactos, no hay diferencia
- b) Bien formado cumple la sintaxis general de XML; válido además cumple una gramática concreta (DTD/XSD)
- c) Válido se refiere solo a la codificación de caracteres del documento

**Respuesta correcta:** b) · **Referencia:** §5.3 [XML10; XMLSCHEMA]

Un documento puede estar sintácticamente bien formado y aun así no respetar la estructura de datos esperada por una aplicación concreta.

### 28. ¿Qué mecanismo de validación XML está escrito en el propio XML y admite tipos de datos ricos (fecha, entero, patrones)?

- a) XML Schema (XSD)
- b) DTD
- c) XHTML

**Respuesta correcta:** a) · **Referencia:** §5.3.1 [XMLSCHEMA]

DTD, heredado de SGML, tiene sintaxis propia distinta de XML y tipos muy básicos; XSD es XML válido en sí mismo y admite restricciones de tipo, rango y cardinalidad.

### 29. ¿Qué elemento evita colisiones cuando dos vocabularios XML definen una etiqueta con el mismo nombre pero significado distinto?

- a) El atributo <code>xmlns</code> (espacio de nombres)
- b) La declaración <code>&lt;!DOCTYPE&gt;</code>
- c) El atributo <code>encoding</code> de la cabecera XML

**Respuesta correcta:** a) · **Referencia:** §5.2.1 [XML-NAMESPACES]

El espacio de nombres, junto a su prefijo, asocia cada elemento a su vocabulario declarado, evitando ambigüedad entre etiquetas homónimas de significado distinto.

### 30. ¿Qué tecnología derivada de XML se usa para transformar un documento XML en otro formato mediante plantillas declarativas?

- a) XHTML
- b) SVG
- c) XSLT

**Respuesta correcta:** c) · **Referencia:** §5.4 [XSLT30]

XSL/XSLT es un lenguaje declarativo escrito en XML que transforma un documento XML en otro (otro XML, HTML o texto) mediante coincidencia de patrones.

### 31. ¿Qué caracteriza al formato SVG frente a un mapa de bits como PNG o JPEG?

- a) Es un formato binario propietario
- b) Describe las formas de manera vectorial en XML, por lo que escala sin perder calidad
- c) Solo puede mostrarse mediante un plugin del navegador

**Respuesta correcta:** b) · **Referencia:** §5.4 [SVG11]

SVG es un formato de gráficos vectoriales descrito íntegramente en XML, manipulable con CSS y JavaScript como cualquier otro nodo del DOM.

### 32. ¿Cuál de los siguientes pares motor de renderizado/navegador es correcto?

- a) Gecko / Safari
- b) WebKit / Firefox
- c) Blink / Chrome

**Respuesta correcta:** c) · **Referencia:** §6.2 [CHROMIUM-BLINK]

Chrome, Edge, Opera y Brave se basan en Chromium/Blink; Firefox usa Gecko; Safari usa WebKit.

### 33. ¿Cuál es el orden correcto del pipeline de renderizado de un navegador?

- a) Layout → parsing → paint → estilo → composición
- b) Parsing → estilo → layout → paint → composición
- c) Paint → parsing → composición → estilo → layout

**Respuesta correcta:** b) · **Referencia:** §6.2 [CHROMIUM-BLINK]

El motor primero construye DOM y CSSOM (parsing), los combina (estilo), calcula posiciones (layout), pinta píxeles (paint) y finalmente ensambla capas con la GPU (composición).

### 34. ¿Qué es el DOM?

- a) Un lenguaje de programación equivalente a JavaScript
- b) Una representación en árbol del documento, accesible mediante una API independiente del lenguaje
- c) El motor de renderizado del navegador

**Respuesta correcta:** b) · **Referencia:** §6.3 [W3C-DOM4]

El DOM es una interfaz (API), no un lenguaje: JavaScript la usa habitualmente, pero no es exclusiva de él.

### 35. ¿Por qué JavaScript se describe como un lenguaje «de un solo hilo» en el navegador?

- a) Porque solo puede ejecutar una pieza de código a la vez, gestionando la asincronía mediante el bucle de eventos
- b) Porque solo puede ejecutarse en servidores de un único núcleo
- c) Porque no admite funciones recursivas

**Respuesta correcta:** a) · **Referencia:** §6.2 [V8-DOC]

La sensación de paralelismo en operaciones de red se logra mediante el bucle de eventos y una cola de tareas, no mediante hilos reales concurrentes.

### 36. ¿Qué práctica consiste en construir primero una experiencia funcional básica y añadir capacidades avanzadas solo donde el navegador las soporte?

- a) Compilación <em>just-in-time</em>
- b) Mejora progresiva (<em>progressive enhancement</em>)
- c) Renderizado del lado del servidor

**Respuesta correcta:** b) · **Referencia:** §6.4

Esta práctica, junto a la comprobación previa de compatibilidad de cada API, mitiga las diferencias de implementación entre motores de navegador.

### 37. ¿Qué caracteriza a un lenguaje de script frente a un lenguaje compilado por adelantado?

- a) Está diseñado para automatizar tareas dentro de un entorno anfitrión, habitualmente interpretado o compilado JIT
- b) No puede ejecutar bucles ni condicionales
- c) Solo puede ejecutarse en el servidor, nunca en el navegador

**Respuesta correcta:** a) · **Referencia:** §7.1 [ECMA262]

JavaScript es el lenguaje de script más relevante del contexto web, tanto en cliente como, con Node.js, en servidor.

### 38. ¿Qué nombre real recibe hoy, en la práctica, el formato de intercambio de datos usado en la técnica AJAX, pese a lo que sugiere su nombre histórico?

- a) XML, tal como indica el propio nombre AJAX
- b) JSON
- c) YAML

**Respuesta correcta:** b) · **Referencia:** §7.2.2 [MDN-JS]

El nombre AJAX es histórico (2005, usaba XML); hoy la práctica casi universal es JSON, más ligero y nativo del propio lenguaje JavaScript.

### 39. ¿Qué objeto devuelve la API <code>fetch</code> para representar un valor que estará disponible en el futuro?

- a) Un <code>Callback</code>
- b) Un <code>Thread</code>
- c) Una <code>Promise</code>

**Respuesta correcta:** c) · **Referencia:** §7.2.2 [MDN-JS]

La promesa permite encadenar el manejo del resultado de una petición de red sin bloquear el hilo único de ejecución de JavaScript.

### 40. ¿Cuál de los siguientes lenguajes se embebe directamente dentro del flujo HTML, ejecutándose típicamente por petición en el servidor?

- a) Java
- b) Python
- c) PHP

**Respuesta correcta:** c) · **Referencia:** §7.3 [PHP-DOC]

PHP fue diseñado específicamente para la web desde 1994 y se embebe directamente en el HTML, con una ejecución típica sin estado persistente entre peticiones salvo mecanismos explícitos.

### 41. ¿Qué entorno de ejecución permite usar JavaScript también en el lado servidor, empleando el motor V8 fuera del navegador?

- a) Django
- b) Node.js
- c) Jakarta EE

**Respuesta correcta:** b) · **Referencia:** §7.3 [NODE-DOC]

Node.js emplea V8 con un modelo de E/S no bloqueante, adecuado para aplicaciones con muchas conexiones concurrentes de corta duración.

### 42. ¿Qué distingue a un framework de una biblioteca?

- a) Un framework impone la estructura y el flujo de control (inversión de control); una biblioteca es invocada por el propio código del desarrollador
- b) Una biblioteca siempre es de pago y un framework siempre es gratuito
- c) No existe diferencia real entre ambos términos

**Respuesta correcta:** a) · **Referencia:** §7.4 [REACT-DOC]

Es el mismo principio de inversión de control estudiado en el Tema 21 para los contenedores Java EE.

### 43. ¿En qué especificación de plataforma, desarrollada en profundidad en otro tema del temario, se apoya principalmente Java como lenguaje de servidor en el ámbito web?

- a) Jakarta EE (Tema 21)
- b) ECMAScript
- c) WSGI

**Respuesta correcta:** a) · **Referencia:** §7.3 [JAKARTA-PLAT]

El Tema 21 desarrolla en profundidad Servlets, JSF, EJB, CDI y JPA como plataforma Java de servidor; este tema sitúa Java como una de las opciones de lenguaje de servidor junto a PHP y Python.

### 44. ¿Cuál es la responsabilidad principal del back-end de una aplicación web?

- a) Aplicar estilos CSS al contenido
- b) Ejecutar la lógica que no debe o no puede correr en el navegador del cliente: datos persistentes, reglas de negocio y autenticación
- c) Interpretar el HTML recibido del servidor

**Respuesta correcta:** b) · **Referencia:** §8.1

El back-end concentra todo aquello que requiere confianza o recursos que el cliente no puede garantizar.

### 45. ¿Qué enfoque de generación de contenidos construye el HTML completo en el servidor antes de enviarlo al navegador?

- a) <em>Client-Side Rendering</em> (CSR)
- b) <em>Server-Side Rendering</em> (SSR)
- c) <em>Progressive Web App</em> (PWA)

**Respuesta correcta:** b) · **Referencia:** §8.2

Es el modelo clásico (PHP, JSP/JSF de Java EE); en CSR, en cambio, es el JavaScript del cliente el que construye el contenido visible.

### 46. ¿Cuál es la forma recomendada de evitar la inyección SQL al acceder a la base de datos desde el back-end?

- a) Validar el formato del campo únicamente en JavaScript, en el front-end
- b) Concatenar directamente la entrada del usuario en la cadena SQL
- c) Usar consultas parametrizadas (o un ORM), donde el dato del usuario se trata siempre como un valor

**Respuesta correcta:** c) · **Referencia:** §8.3 [OWASP-TOP10]

El motor de base de datos recibe el dato siempre como valor, nunca como parte de la sintaxis del comando, sea cual sea su contenido.

### 47. ¿Cuál es la diferencia entre autenticación y autorización?

- a) Son sinónimos y se usan indistintamente
- b) Autorización verifica quién es el usuario; autenticación determina qué puede hacer
- c) Autenticación verifica quién es el usuario; autorización determina qué puede hacer ese usuario ya identificado

**Respuesta correcta:** c) · **Referencia:** §8.4

Confundir ambos conceptos explica por qué el código 401 (fallo de autenticación) se confunde a menudo con un fallo de permisos, que en realidad corresponde a 403.

### 48. ¿Qué atributo de una cookie impide que JavaScript pueda leerla desde el DOM, mitigando su robo mediante XSS?

- a) <code>Secure</code>
- b) <code>SameSite</code>
- c) <code>HttpOnly</code>

**Respuesta correcta:** c) · **Referencia:** §8.4

<code>Secure</code> restringe el envío a HTTPS y <code>SameSite</code> restringe el envío entre dominios distintos (mitigando CSRF); <code>HttpOnly</code> es el que impide la lectura por script.

### 49. ¿Qué estilo arquitectónico trata cada entidad de negocio como un recurso identificado por una URL, manipulado con los métodos HTTP estándar?

- a) SOAP
- b) REST
- c) RPC clásico

**Respuesta correcta:** b) · **Referencia:** §8.5 [FIELDING2000]

Formulado por Fielding en el año 2000, REST domina el desarrollo de APIs nuevas por su simplicidad y su alineamiento natural con HTTP, frente al sobre XML y el contrato WSDL de SOAP.

### 50. ¿Qué alternativa a la cookie de sesión con estado en el servidor incluye la identidad y los permisos firmados digitalmente, sin necesitar un almacén de sesiones?

- a) Un token autocontenido como JWT
- b) Un <code>localStorage</code> sin cifrar
- c) Un identificador incremental en la URL

**Respuesta correcta:** a) · **Referencia:** §8.4

A cambio, revocar un token individual antes de su expiración resulta más difícil que invalidar una entrada en un almacén de sesiones del servidor.

### 51. ¿Por qué una aplicación web es multiplataforma por construcción?

- a) Porque el mismo HTML/CSS/JS se ejecuta en cualquier sistema operativo con un navegador compatible, sin recompilar
- b) Porque siempre requiere una API nativa distinta por sistema operativo
- c) Porque XML sustituye a HTML en los dispositivos móviles

**Respuesta correcta:** a) · **Referencia:** §9.1

Es la misma ventaja frente a las aplicaciones de escritorio descrita al inicio del tema, aplicada ahora a la variedad de plataformas y dispositivos.

### 52. ¿Qué diferencia al diseño adaptativo del diseño responsivo?

- a) El adaptativo usa varias maquetaciones fijas predefinidas; el responsivo usa una única maquetación fluida y continua
- b) Son exactamente la misma técnica con nombres distintos
- c) El responsivo solo funciona en dispositivos móviles, nunca en escritorio

**Respuesta correcta:** a) · **Referencia:** §9.2

En la práctica, muchas aplicaciones combinan ambas ideas en distintos puntos de ruptura.

### 53. ¿Cuáles son los tres pilares técnicos de una Progressive Web App (PWA)?

- a) HTML, CSS y JavaScript
- b) Service Worker, Web App Manifest y servicio obligatorio por HTTPS
- c) DTD, XML Schema y XSLT

**Respuesta correcta:** b) · **Referencia:** §9.3 [MDN-PWA]

El Service Worker gestiona la caché y el funcionamiento offline; el Manifest permite instalar la aplicación; HTTPS es requisito de seguridad para registrar el Service Worker.

### 54. ¿Por qué el Service Worker puede seguir funcionando aunque la pestaña de la aplicación esté cerrada?

- a) Porque se ejecuta en un hilo separado de la página y no tiene acceso directo al DOM
- b) Porque forma parte del propio DOM y se mantiene en memoria indefinidamente
- c) Porque sustituye por completo al navegador como proceso del sistema operativo

**Respuesta correcta:** a) · **Referencia:** §9.3 [SERVICE-WORKERS]

Esta separación, y la comunicación por paso de mensajes con la página, es lo que permite servir contenido cacheado o recibir notificaciones push sin que la pestaña esté abierta.

### 55. ¿Qué fichero describe metadatos como el nombre, los iconos y el color de tema de una PWA, para que el navegador ofrezca instalarla?

- a) <code>robots.txt</code>
- b) <code>sw.js</code>
- c) <code>manifest.json</code> (Web App Manifest)

**Respuesta correcta:** c) · **Referencia:** §9.3 [WEB-APP-MANIFEST]

El <code>sw.js</code> es el propio script del Service Worker, responsable de interceptar peticiones de red, no de describir metadatos de instalación.

### 56. Según el OWASP Top 10:2021, ¿qué riesgo ocupa el primer puesto por su frecuencia e impacto directo sobre la confidencialidad de datos de terceros?

- a) Configuración de seguridad incorrecta
- b) Uso de componentes con vulnerabilidades conocidas
- c) Control de acceso roto

**Respuesta correcta:** c) · **Referencia:** §10.2.1 [OWASP-TOP10]

Ocurre cuando la aplicación no verifica en el servidor que el usuario autenticado tiene permiso sobre el recurso concreto que solicita, dando lugar a ataques como el IDOR.

### 57. ¿Cómo se mitiga la inyección SQL de forma efectiva?

- a) Confiando en la validación del formulario en el front-end
- b) Escapando solo los caracteres <code>&lt;</code> y <code>&gt;</code> de la entrada del usuario
- c) Con consultas parametrizadas en el back-end, donde el dato del usuario nunca forma parte de la sintaxis del comando

**Respuesta correcta:** c) · **Referencia:** §10.2.1 [OWASP-TOP10]

La validación de front-end puede eludirse enviando la petición directamente al servidor, sin pasar por el formulario ni por el JavaScript de la página.

### 58. ¿Qué diferencia esencial existe entre XSS y CSRF?

- a) XSS explota la confianza del usuario en el sitio; CSRF explota la confianza del sitio en el navegador ya autenticado del usuario
- b) Son exactamente el mismo ataque con nombres distintos
- c) XSS solo afecta a aplicaciones móviles, nunca a aplicaciones web de escritorio

**Respuesta correcta:** a) · **Referencia:** §10.2.2 [OWASP-TOP10]

XSS ejecuta script inyectado como si fuera del propio dominio; CSRF envía una petición no deseada aprovechando que el navegador adjunta automáticamente la cookie de sesión válida.

### 59. ¿Qué atributo de cookie impide que el navegador la adjunte en peticiones originadas desde un dominio distinto, mitigando CSRF?

- a) <code>HttpOnly</code>
- b) <code>SameSite</code>
- c) <code>Max-Age</code>

**Respuesta correcta:** b) · **Referencia:** §10.3.2 [OWASP-TOP10]

Junto con un token CSRF único por sesión o formulario, <code>SameSite=Strict</code> o <code>Lax</code> es la mitigación estándar frente a peticiones falsificadas entre sitios.

### 60. Un formulario valida el DNI con una expresión regular únicamente en JavaScript, en el navegador. ¿Es esto seguridad suficiente?

- a) Sí, porque el navegador garantiza que ningún dato inválido llegará nunca al servidor
- b) No, porque un atacante puede enviar la petición HTTP directamente al servidor, sin pasar por el formulario ni por el JavaScript de la página
- c) Sí, siempre que el campo tenga también el atributo <code>required</code>

**Respuesta correcta:** b) · **Referencia:** §10.3.1 [OWASP-TOP10]

La validación de cliente mejora la experiencia de uso, pero la validación de seguridad real debe repetirse siempre en el servidor, el único punto de confianza.

## Preguntas sobre los casos prácticos

### Caso 1. Formulario de cita previa: HTML5, RWD y accesibilidad

#### 1. En el supuesto planteado, el campo de DNI/NIE debe exigir 8 dígitos seguidos de una letra mediante validación nativa de HTML5, sin JavaScript. ¿Qué atributo se usa?

- a) type="email", que obliga al navegador a comprobar el formato del dato.
- b) maxlength="9", que limita el campo a nueve caracteres en total.
- c) pattern="[0-9]{8}[A-Za-z]", con la expresión regular del formato.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §4.3.2

El atributo pattern aplica una expresión regular como validación nativa del navegador; maxlength solo limita la longitud y type="email" valida direcciones de correo.

#### 2. ¿Qué atributo marca el campo de DNI/NIE como obligatorio, también sin JavaScript?

- a) El atributo placeholder="Obligatorio".
- b) El atributo required.
- c) El atributo min="1".

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §4.3.2

HTML5 incorporó atributos de validación nativa como required (obligatoriedad), pattern o min/max; el placeholder es solo un texto de ayuda.

#### 3. Con pattern y required ya puestos, ¿basta esa validación del formulario como medida de seguridad?

- a) No: mejora la experiencia de uso, pero un atacante puede enviar la petición directamente al servidor.
- b) Sí: el navegador rechaza cualquier petición que no haya pasado la validación del formulario.
- c) Sí, siempre que el formulario envíe los datos con el método POST en lugar de con GET.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §10.3.1

La validación del front-end puede eludirse enviando peticiones HTTP sin pasar por el formulario; toda entrada debe validarse siempre también en el servidor.

#### 4. ¿Qué etiqueta es imprescindible en el <head> para que el formulario se muestre adaptado en un móvil?

- a) <meta charset="UTF-8">
- b) <meta name="viewport" content="width=device-width, initial-scale=1.0">
- c) <meta name="description" content="Cita previa en la sede electrónica">

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §3.3.1

La metaetiqueta viewport hace que el navegador móvil use el ancho real del dispositivo; charset fija la codificación y description la usan los buscadores.

#### 5. ¿Qué ocurre en el móvil del ciudadano si se omite esa metaetiqueta?

- a) El navegador no muestra la página y avisa de que no está adaptada al dispositivo.
- b) Las media queries se aplican igual, pero el texto aparece con un tamaño mayor.
- c) Se renderiza a un ancho de escritorio simulado (unos 980 px) y luego se reduce.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §3.3.1

Sin viewport, el navegador móvil simula un ancho de escritorio y reduce la página, lo que deja sin efecto las media queries basadas en el ancho real de la pantalla.

#### 6. El formulario se maqueta con Flexbox en fila. ¿Qué media query lo pasa a columna por debajo de 600 px de ancho?

- a) @media (max-width: 600px) { .formulario-cita { flex-direction: column; } }
- b) @media (min-width: 600px) { .formulario-cita { flex-direction: column; } }
- c) @media (max-width: 600px) { .formulario-cita { flex-direction: row; } }

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §3.3.1

La condición max-width: 600px se cumple en anchos de hasta 600 px y, dentro de ella, flex-direction: column apila los elementos; min-width haría lo contrario.

#### 7. ¿A qué responde la condición de esa media query?

- a) Al sistema operativo del dispositivo, móvil o de escritorio, que el servidor detecta.
- b) A la resolución de las imágenes del formulario, indicada mediante el atributo srcset.
- c) Al ancho de la ventana gráfica (viewport) del navegador en el que se muestra la página.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §3.3.1

Las media queries son reglas CSS condicionadas al ancho de la ventana gráfica, que reorganizan la disposición en puntos de ruptura.

#### 8. Un campo de búsqueda no tiene <label> visible, solo un icono. ¿Cómo se etiqueta para que el lector de pantalla anuncie su propósito?

- a) Con el atributo aria-label, por ejemplo aria-label="Buscar trámite".
- b) No hace falta: el lector de pantalla describe el icono de forma automática.
- c) Con un comentario HTML junto al campo que explique para qué sirve.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §3.3.2 (principio Perceptible) y técnica ARIA14 del W3C

aria-label da al campo un nombre accesible que el lector de pantalla anuncia aunque no haya texto visible; un comentario HTML no llega al usuario.

#### 9. Otra opción es mantener un <label> pero ocultarlo visualmente. ¿Por qué NO debe ocultarse con display:none?

- a) Porque display:none está prohibido dentro de los formularios de HTML5.
- b) Porque display:none también lo oculta a las tecnologías de apoyo.
- c) Porque display:none borra el valor que el ciudadano haya escrito.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 (solución orientativa)

Un elemento con display:none desaparece también para los lectores de pantalla; la etiqueta debe sacarse del flujo visual con una clase que la mantenga accesible.

#### 10. Para las personas que navegan solo con teclado, ¿qué principio POUR de las WCAG exige que todo el formulario pueda manejarse sin ratón?

- a) Perceptible.
- b) Comprensible.
- c) Operable.

**Respuesta correcta:** c) · **Referencia:** Caso 1, enunciado · §3.3.2

Operable significa que los componentes de la interfaz deben poder manejarse; por ejemplo, que toda la funcionalidad sea accesible por teclado y no solo con ratón.

### Caso 2. API REST de consulta de expedientes con sesión segura

#### 1. En el supuesto planteado, ¿qué método HTTP y qué ruta corresponden, en estilo REST, a «obtener el expediente número 1234»?

- a) POST /api/expedientes/1234
- b) GET /api/expedientes/1234
- c) PUT /api/expedientes/1234

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §8.5

En REST cada expediente es un recurso identificado en la ruta y se obtiene con GET; PUT lo reemplazaría y POST se usa para crear.

#### 2. ¿Por qué el método adecuado para esa consulta es GET?

- a) Porque es una operación de lectura, idempotente y sin efectos secundarios.
- b) Porque GET cifra los parámetros de la URL antes de enviarlos al servidor.
- c) Porque GET crea el recurso en el servidor si todavía no existía.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §2.3.1

GET obtiene una representación del recurso; según la tabla de métodos, es idempotente y seguro (sin efectos secundarios).

#### 3. ¿Cómo debe escribir el back-end la consulta que recupera el expediente por su identificador?

- a) Concatenando el identificador en la cadena SQL, tras validarlo antes con JavaScript.
- b) "SELECT * FROM expediente WHERE id = '" + id_expediente + "'"
- c) cursor.execute("SELECT * FROM expediente WHERE id = %s", (id_expediente,))

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §8.3 y §10.2.1

La consulta parametrizada evita la inyección SQL; concatenar el dato en la cadena es lo vulnerable, y la validación en JavaScript puede eludirse.

#### 4. ¿Por qué la consulta parametrizada protege frente a la inyección SQL?

- a) Porque el motor recibe el dato siempre como un valor, nunca como parte de la sintaxis.
- b) Porque cifra el identificador del expediente antes de enviarlo a la base de datos.
- c) Porque solo admite identificadores numéricos y rechaza cualquier otro carácter.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §10.2.1

En la consulta parametrizada el dato del usuario se trata como un valor, sea cual sea su contenido, y no puede alterar la estructura del comando.

#### 5. Un ciudadano autenticado cambia en la URL el número de su expediente por otro y obtiene un expediente ajeno. ¿Qué vulnerabilidad es?

- a) Un XSS reflejado, porque el dato viaja en la propia URL de la petición.
- b) Un IDOR, una variante del control de acceso roto.
- c) Un CSRF, porque la petición lleva la cookie de sesión válida.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §10.2.1

Cambiar el identificador en la URL para acceder al recurso de otro ciudadano es un IDOR (Insecure Direct Object Reference), variante del control de acceso roto.

#### 6. Para no ser vulnerable a ese IDOR, ¿qué comprobación debe hacer el servidor antes de devolver el expediente?

- a) Que el usuario está autenticado, lo que basta para servir cualquier expediente.
- b) Que el identificador recibido tiene un formato numérico válido y existe.
- c) Que el expediente pertenece al ciudadano autenticado o que su rol tiene permiso.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §8.4 y §10.2.1

La autenticación dice quién es el usuario; la autorización decide si puede acceder a ese recurso concreto, y debe verificarse en el servidor.

#### 7. Si el expediente pertenece a otro ciudadano, ¿qué código de estado debe devolver la API?

- a) 401 Unauthorized.
- b) 403 Forbidden.
- c) 400 Bad Request.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §2.3.1 y §8.4

403 Forbidden indica un fallo de autorización: el servidor sabe quién es el usuario, pero no tiene permiso. 401 indica un fallo de autenticación.

#### 8. ¿Qué atributo de la cookie de sesión mitiga su robo mediante XSS?

- a) SameSite, que impide enviarla desde otro dominio.
- b) Secure, que impide enviarla por HTTP sin cifrar.
- c) HttpOnly, que impide que JavaScript la lea.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §8.4

Con HttpOnly, JavaScript no puede leer la cookie desde el DOM, de modo que un script inyectado no puede robarla directamente.

#### 9. ¿Qué atributo de la cookie de sesión mitiga el uso indebido por CSRF?

- a) El atributo SameSite=Strict o Lax.
- b) El atributo HttpOnly.
- c) El atributo Max-Age=3600.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §8.4 y §10.2.2

SameSite restringe el envío de la cookie en peticiones originadas desde otro dominio, que es justo lo que aprovecha un ataque CSRF.

#### 10. ¿Qué aporta el atributo Secure en la cookie de sesión?

- a) Impide que JavaScript pueda leer la cookie desde el DOM.
- b) Hace que la cookie solo se envíe por HTTPS, nunca por HTTP.
- c) Impide que la cookie se adjunte a peticiones de otro dominio.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §8.4

Secure garantiza que la cookie solo viaja sobre HTTPS, nunca en texto plano por HTTP.

### Caso 3. Conversión a PWA y mitigación de XSS en un formulario de contacto

#### 1. En el supuesto planteado, ¿qué código, ejecutado desde la página principal, registra el Service Worker ubicado en /sw.js?

- a) if ('serviceWorker' in navigator) { navigator.serviceWorker.register('/sw.js'); }
- b) window.open('/sw.js'); al terminar de cargar la página principal
- c) <script src="/sw.js"></script> incluido en el <head> de la página

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §9.3

El Service Worker se registra con navigator.serviceWorker.register(); cargar el fichero como un script normal lo ejecutaría en la página, no como Service Worker.

#### 2. ¿Para qué sirve la comprobación 'serviceWorker' in navigator antes del registro?

- a) Para verificar que la página se está sirviendo por HTTPS.
- b) Para confirmar que el ciudadano ya ha iniciado sesión.
- c) Para comprobar que el navegador admite esa API (mejora progresiva).

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §6.4 y §9.3

El registro se condiciona a que el navegador soporte la API: si no la tiene, la página sigue funcionando sin capacidad offline, como pide la mejora progresiva.

#### 3. ¿Bajo qué condición de protocolo puede registrarse el Service Worker en producción?

- a) Con cualquier protocolo, siempre que sw.js esté en la raíz.
- b) Solo si la sede electrónica se sirve por HTTPS.
- c) Solo si el servidor web utiliza la versión HTTP/3.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §9.3

Servir la aplicación por HTTPS es requisito obligatorio para registrar un Service Worker; es uno de los tres pilares de una PWA.

#### 4. ¿Por qué HTTPS es un requisito de seguridad y no una simple recomendación para el Service Worker?

- a) Porque HTTPS acelera la carga del Service Worker y de la caché sin conexión.
- b) Porque el Service Worker guarda las contraseñas del ciudadano en la caché.
- c) Porque el Service Worker controla el tráfico de red y, sin cifrar, quedaría expuesto.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §9.3

El Service Worker puede interceptar y modificar peticiones y respuestas; permitirlo sobre HTTP expondría ese control a quien intercepte la red.

#### 5. ¿Qué propiedades del fichero manifest.json son necesarias para que el navegador ofrezca «instalar» la sede electrónica?

- a) name (o short_name) y start_url, junto con al menos un icono en icons.
- b) HttpOnly y SameSite, que protegen la sesión de la aplicación instalada.
- c) Cache-Control y ETag, que controlan la caché de la aplicación instalada.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §9.3

El Web App Manifest es un JSON con los metadatos de la aplicación (nombre, iconos, URL de inicio…); HttpOnly, SameSite, Cache-Control y ETag son atributos de cookie y cabeceras HTTP.

#### 6. Un ciudadano consultó ayer el estado de su trámite y hoy quiere verlo en el metro, sin conexión. ¿Qué pieza de la PWA lo hace posible?

- a) El fichero manifest.json, que guarda una copia del último estado consultado.
- b) El Service Worker, que sirve desde la caché el contenido ya consultado.
- c) La cookie de sesión, que almacena el estado del trámite en el navegador.

**Respuesta correcta:** b) · **Referencia:** Caso 3, enunciado · §9.3

El Service Worker intercepta las peticiones y sirve contenido desde la caché cuando no hay conexión; obtener un estado más reciente exigirá conectividad.

#### 7. El formulario de contacto muestra el último mensaje con elemento.innerHTML = ultimoMensaje. ¿Por qué es vulnerable a XSS?

- a) Porque innerHTML interpreta la cadena como HTML y ejecutaría el código de un atributo de evento inyectado (p. ej. onerror) en el dominio de la sede.
- b) Porque innerHTML envía el mensaje al servidor sin cifrar, y un atacante puede leerlo por el camino.
- c) Porque innerHTML no admite caracteres con tilde y deja el mensaje del ciudadano sin escapar.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §10.2.2

Insertar contenido no confiable como HTML sin escapar permite ejecutar JavaScript arbitrario (p. ej. con <img src=x onerror=…>) en el contexto del propio dominio de confianza; es un XSS basado en DOM porque la inserción la hace el JavaScript del cliente.

#### 8. Si el mensaje es texto plano, ¿cuál es la corrección adecuada?

- a) Mantener innerHTML y marcar la cookie de sesión como HttpOnly.
- b) Usar elemento.textContent = ultimoMensaje en lugar de innerHTML.
- c) Limitar con JavaScript la longitud máxima del mensaje del ciudadano.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §10.2.2

textContent inserta el contenido como texto, sin interpretarlo como HTML. HttpOnly no evita el XSS: solo limita su impacto sobre la cookie.

#### 9. Si hubiera que insertar marcado en lugar de texto plano, ¿cómo se protege la página?

- a) Insertando el mensaje con innerHTML tal como lo escribió el ciudadano.
- b) Desactivando el Service Worker mientras se muestra el mensaje en pantalla.
- c) Escapando los caracteres especiales (<, >, &) antes de insertarlo, con una CSP de refuerzo.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §10.2.2

La mitigación principal del XSS es escapar toda salida con datos no controlados por el desarrollador, reforzada con la cabecera Content-Security-Policy.

#### 10. ¿Qué añade la cabecera Content-Security-Policy como refuerzo frente al XSS?

- a) Restringe desde qué orígenes puede cargarse y ejecutarse script en la página.
- b) Cifra la cookie de sesión para que un script no pueda descifrarla.
- c) Obliga al navegador a usar HTTPS en todas las visitas futuras.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §10.2.2 y §10.3.1

CSP limita qué script puede ejecutarse en la página; forzar HTTPS en visitas futuras es la función de otra cabecera, Strict-Transport-Security.
