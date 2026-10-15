# Tema 34. El modelo TCP/IP y el modelo OSI de ISO. Protocolos TCP/IP

**Bloque:** técnico  
**Enunciado oficial** (BOAM n.º 10.032, de 23 de diciembre de 2025): El modelo TCP/IP y el modelo de referencia de interconexión de sistemas abiertos (OSI) de ISO. Protocolos TCP/IP.

Versión web: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-34.html> · PDF: [tema-34.pdf](tema-34.pdf) · Test: [../../../tests/tecnico/tema-34.md](../../../tests/tecnico/tema-34.md)

## Índice

- 1. Introducción a las arquitecturas de red y la estandarización
  - 1.1. Concepto y necesidad de las arquitecturas por niveles
  - 1.2. Organismos internacionales de estandarización
- 2. El Modelo de Referencia de Interconexión de Sistemas Abiertos (OSI) de ISO
  - 2.1. Origen y principios de diseño del modelo OSI
  - 2.2. Conceptos de capa, servicio, interfaz y protocolo
  - 2.3. Descripción de las capas del modelo OSI
  - 2.4. Unidades de datos de protocolo (PDU) y encapsulamiento
- 3. El Modelo TCP/IP
  - 3.1. Origen y evolución de la arquitectura TCP/IP
  - 3.2. Niveles funcionales del modelo TCP/IP
  - 3.3. Encapsulamiento y demultiplexación de datos
- 4. Comparativa entre el Modelo OSI y el Modelo TCP/IP
  - 4.1. Correspondencia y equivalencia entre capas
  - 4.2. Análisis comparativo: diferencias de diseño y adopción
- 5. Pila de protocolos TCP/IP: capa de acceso a la red
  - 5.1. Funciones de la capa de acceso a la red
  - 5.2. Direccionamiento físico MAC y transmisión de tramas
- 6. Pila de protocolos TCP/IP: capa de red
  - 6.1. Protocolo de Internet versión 4 (IPv4)
  - 6.2. Protocolo de Internet versión 6 (IPv6)
  - 6.3. Protocolos de control y resolución de direcciones (ICMP, ARP y ND)
  - 6.4. Principios de enrutamiento IP
- 7. Pila de protocolos TCP/IP: capa de transporte
  - 7.1. Concepto de puerto y multiplexación de aplicaciones
  - 7.2. Transmission Control Protocol (TCP)
  - 7.3. User Datagram Protocol (UDP)
- 8. Pila de protocolos TCP/IP: capa de aplicación
  - 8.1. Servicios de infraestructura de red (DNS y DHCP)
  - 8.2. Protocolos de servicios web y de transferencia de archivos
  - 8.3. Protocolos de correo electrónico y de gestión de red
- 9. Normativa e integración en la Administración Pública
  - 9.1. Adopción e implantación de IPv6 en el sector público
  - 9.2. Requisitos de red e interconexión en el Esquema Nacional de Seguridad
- Los diez datos que no se pueden fallar

### Conceptos clave para memorizar

| Concepto | Dato clave |
|----|----|
| **Capas del modelo OSI** | **7**: física (1), enlace (2), red (3), transporte (4), sesión (5), presentación (6) y aplicación (7). Norma **ISO/IEC 7498-1:1994**, idéntica a la **Recomendación UIT-T X.200** |
| **Capas del modelo TCP/IP** | **4**: acceso a la red, internet, transporte y aplicación (**RFC 1122**). Algunos autores desdoblan la primera en física y enlace y hablan de **5** |
| **PDU por capa** | Bit (1) · **trama** (2) · **paquete o datagrama** (3) · **segmento** TCP / **datagrama** UDP (4) · **mensaje** o datos (5-7) |
| **Regla del encapsulamiento** | Cada capa trata la PDU de la capa superior como **carga útil opaca** y le añade su propia **cabecera** (y en la capa 2, también una **cola**) |
| **Los tres campos de la demultiplexación** | `EtherType` de la trama → `Protocolo`/`Next Header` de IP → **puerto destino** de TCP o UDP |
| **Dirección MAC** | **48 bits** (6 octetos), notación hexadecimal; los **24 primeros bits** son el **OUI** del fabricante. Difusión = `FF:FF:FF:FF:FF:FF` |
| **Dirección IPv4** | **32 bits**, notación decimal punteada. Cabecera mínima de **20 octetos** y máxima de **60** |
| **Dirección IPv6** | **128 bits**, notación hexadecimal en 8 grupos de 16 bits. Cabecera **fija de 40 octetos** |
| **Direcciones privadas IPv4** | `10.0.0.0/8` · `172.16.0.0/12` · `192.168.0.0/16` (**RFC 1918**). Bucle local `127.0.0.0/8`; enlace local `169.254.0.0/16` |
| **Números de protocolo IP** | **1** = ICMP · **6** = TCP · **17** = UDP · **41** = IPv6 encapsulado · **50** = ESP · **51** = AH · **58** = ICMPv6 |
| **Rangos de puertos (IANA)** | **0-1023** bien conocidos · **1024-49151** registrados · **49152-65535** dinámicos o efímeros |
| **Puertos que hay que saber** | 20/21 FTP · 22 SSH · 23 Telnet · 25 SMTP · 53 DNS · 67/68 DHCP · 80 HTTP · 110 POP3 · 123 NTP · 143 IMAP · 161/162 SNMP · 389 LDAP · 443 HTTPS · 465/587 SMTP seguro · 636 LDAPS · 993 IMAPS · 995 POP3S · 3389 RDP |
| **Saludo de TCP** | **Tres vías**: `SYN` → `SYN+ACK` → `ACK`. Cierre ordenado en **cuatro** (`FIN`, `ACK`, `FIN`, `ACK`) |
| **Cabeceras de transporte** | TCP: **20 octetos** mínimo (60 con opciones) · UDP: **8 octetos** fijos, con solo cuatro campos |
| **MTU de Ethernet** | **1.500 octetos** de carga útil. IPv4 fragmenta en los routers; **IPv6 no fragmenta en tránsito**: usa descubrimiento de MTU de camino |
| **Norma de conexión a SARA** | **NTI de requisitos de conexión a la red de comunicaciones de las AA. PP. españolas** (Resolución de **19 de julio de 2011**), dictada al amparo del **ENI** (RD 4/2010) |
| **Medidas de red del ENS** | `mp.com.1` perímetro seguro · `mp.com.2` confidencialidad · `mp.com.3` integridad y autenticidad · `mp.com.4` **separación de flujos de información en la red** (VLAN en el refuerzo R1) |

## Contenido

### Convenciones del documento

Este tema incluye cuatro tipos de **cajas callout** para facilitar el estudio:

> **Dato clave.** Información de alta densidad memorística: números de puerto, números de protocolo, tamaños de cabecera, siglas y numeración de RFC.

> **Ejercicio resuelto.** Problema resuelto paso a paso: calcular una subred, leer una cabecera, seguir un encapsulamiento, interpretar una traza.

> **Ejemplo de aplicación en el ayto.** Aplicación de la teoría al entorno municipal (red corporativa del IAM, sede electrónica, oficinas de distrito, conexión a la red SARA).

> **Relación con otros temas.** Enlace conceptual a otros temas del temario oficial.

**Cómo leer este tema.** El enunciado oficial encadena **tres preguntas distintas** y conviene no confundirlas. La primera es **conceptual**: por qué las redes se diseñan por capas y qué es un modelo de referencia. La segunda es **comparativa**: dos modelos, uno normativo y otro real, que hay que saber describir por separado y luego enfrentar. Y la tercera es **descriptiva y de dato**: la pila de protocolos TCP/IP, nivel por nivel, con sus cabeceras, sus direcciones y sus números. Un opositor que solo memorice «las siete capas de OSI» y «los cuatro niveles de TCP/IP» tiene cubierta menos de una cuarta parte del tema; el grueso es la tercera, la de los protocolos concretos.

**Fronteras con otros temas, declaradas de entrada.** Este tema es la **columna vertebral del bloque de redes** y por eso limita con cuatro temas a la vez. Se explicita aquí para que el solapamiento del temario oficial no se lea como una omisión:

- El **Tema 33** cubre los **medios de transmisión**, los modos de comunicación y los equipos de conmutación. Aquí la capa física se describe **como capa del modelo**, no como tecnología de transmisión.
- El **Tema 37** cubre las **redes locales**: tipología, técnicas de transmisión, métodos de acceso al medio y dispositivos de interconexión. Aquí Ethernet aparece solo como **ejemplo de capa de acceso a la red** y para explicar la relación entre dirección MAC y dirección IP.
- El **Tema 35** cubre **Internet** y en particular **HTTP, HTTPS y SSL/TLS**. Aquí la capa de aplicación se recorre como **catálogo de protocolos de la pila**, con sus puertos y su transporte, sin desarrollar HTTP ni TLS.
- El **Tema 36** cubre la **seguridad en redes**: seguridad perimetral, acceso remoto y VPN. Aquí la seguridad aparece únicamente en §9.2, y solo en lo que la normativa exige a la **arquitectura de red** de una Administración.
- El **Tema 39** cubre los **principios del ENS y del ENI**. Aquí se citan las medidas concretas del anexo II que se predican de la red, no el esquema en su conjunto.

**Una advertencia de método.** En este tema hay dos tipos de contenido que se estudian de forma distinta. El **mecanismo** —qué hace cada capa, por qué existe el encapsulamiento, por qué TCP necesita tres vías para abrir una conexión— se entiende una vez y ya no se olvida. El **dato** —que ESP es el protocolo IP 50, que la cabecera IPv6 mide 40 octetos, que DHCP usa los puertos 67 y 68— hay que repasarlo periódicamente porque no se deduce de nada. Las cajas naranjas marcan lo segundo. El tema termina con un bloque de **«los diez datos que no se pueden fallar»** pensado para el repaso de última hora.

**Caso de referencia usado en todo el tema** (contexto Ayuntamiento de Madrid, supuesto simplificado): la **red corporativa municipal** que conecta las oficinas de atención a la ciudadanía de los distritos con el centro de proceso de datos del IAM, donde se alojan la sede electrónica y el sistema de tramitación de expedientes, y que a su vez se conecta a **internet** y a la **red SARA** para intercambiar datos con otras Administraciones. Ese único escenario permite instanciar todas las capas: el cable y el conmutador de la oficina (§5), el direccionamiento de la sede y de los puestos (§6), la conexión del navegador con el servidor (§7), la resolución del nombre `sede.madrid.es` y la configuración automática del puesto (§8) y las obligaciones normativas que pesan sobre todo ello (§9).

------------------------------------------------------------------------

### 1. Introducción a las arquitecturas de red y la estandarización

#### 1.1. Concepto y necesidad de las arquitecturas por niveles

Una **red de comunicaciones** resuelve un problema engañosamente sencillo de enunciar: llevar información de un proceso que se ejecuta en un equipo a otro proceso que se ejecuta en otro equipo. Lo que lo hace difícil es la acumulación de problemas independientes que hay que resolver a la vez. Hay que convertir bits en señales y las señales en bits; hay que detectar que la señal ha llegado corrompida; hay que decidir quién transmite cuando el medio es compartido; hay que elegir un camino cuando los equipos no están conectados directamente; hay que evitar que un emisor rápido ahogue a un receptor lento; hay que decidir a cuál de los cincuenta programas que corren en la máquina destino se entregan los datos; y hay que ponerse de acuerdo en cómo se representa lo que se envía.

Resolver todo eso de una vez, en un único programa monolítico, produce un sistema **imposible de mantener, de sustituir por partes y de normalizar**. La solución que adoptó la ingeniería de comunicaciones —y que es, literalmente, el objeto de este tema— es la **arquitectura por niveles** o **estratificación** (*layering*).

**Definición.** Una **arquitectura de red por niveles** organiza la funcionalidad de comunicación en una serie de **capas superpuestas**, cada una de las cuales **presta un servicio a la capa inmediatamente superior** y se apoya en el servicio de la inmediatamente inferior, ocultándole cómo lo consigue \[ISO7498\]. El conjunto de capas y de protocolos se denomina **arquitectura de red**; la lista de protocolos concretos que la realizan, **pila de protocolos** (*protocol stack*).

La idea no es exclusiva de las redes: es el mismo principio de **abstracción por capas** con el que se construyen los sistemas operativos, los sistemas gestores de bases de datos o las arquitecturas multicapa de las aplicaciones. Lo que cambia es que aquí las capas están **distribuidas en máquinas distintas** y deben entenderse entre sí a distancia.

> **Relación con otros temas.** La abstracción por niveles como principio de diseño aparece también en el **Tema 14** (estructura del sistema operativo: núcleo, servicios, interfaz), en el **Tema 22** (arquitecturas cliente/servidor y multicapa) y en el **Tema 20** (encapsulamiento como pilar de la orientación a objetos). Es el mismo concepto aplicado a problemas distintos.

**Los cuatro beneficios de la estratificación** son los que hay que saber enunciar:

1.  **Descomposición del problema.** Cada capa aborda un problema acotado y bien definido. Diseñar el control de errores del enlace y diseñar el encaminamiento son dos tareas separadas.
2.  **Ocultación de la información y sustituibilidad.** La capa superior conoce **qué** hace la inferior, no **cómo** lo hace. Eso permite cambiar la tecnología de una capa —pasar de cable de cobre a fibra, de Ethernet a Wi-Fi— sin tocar ninguna otra. Es la propiedad de la que depende, en la práctica, que internet haya sobrevivido cuarenta años de cambio tecnológico.
3.  **Normalización por partes.** Se pueden publicar normas independientes para cada capa y dejar que compitan varias implantaciones de cada una.
4.  **Interoperabilidad de sistemas heterogéneos.** Dos equipos de fabricantes distintos, con sistemas operativos distintos, se comunican si implementan los mismos protocolos en las capas correspondientes.

También tiene **inconvenientes**, y conviene conocerlos:

- **Sobrecarga por cabeceras.** Cada capa añade su propia información de control. En un paquete pequeño, la proporción de cabecera frente a datos útiles puede ser enorme.
- **Duplicación de funciones.** El control de errores aparece en la capa de enlace, en la de transporte y a veces en la de aplicación. No siempre es redundancia inútil, pero lo parece.
- **Rigidez y pérdida de rendimiento.** Una capa no puede aprovechar información que conoce otra. El caso clásico es un enlace inalámbrico con pérdidas: la capa de transporte interpreta la pérdida como congestión y reduce su velocidad, cuando la causa era una interferencia.
- **Violaciones de capa en la práctica.** Los cortafuegos que inspeccionan hasta la capa de aplicación, o los traductores de direcciones que reescriben puertos de transporte, **rompen deliberadamente** la separación por niveles.

**Los dos principios que rigen la relación entre capas** son la clave conceptual del tema y merecen enunciarse con precisión:

- **Comunicación vertical (real).** Entre capas adyacentes **de la misma máquina**, a través de una **interfaz**. Es la única comunicación que existe físicamente, además del cable de la capa 1.
- **Comunicación horizontal (virtual o entre pares).** Entre la capa *N* de una máquina y la capa *N* de la otra, mediante un **protocolo**. Es una comunicación **lógica**: la capa 4 del origen «habla» con la capa 4 del destino como si estuvieran conectadas, aunque en realidad los datos bajan hasta la capa 1, cruzan el medio y suben de nuevo. Ver **diagrama D1**.

> **Dato clave.** La distinción entre **comunicación vertical real** (interfaz, misma máquina) y **comunicación horizontal virtual** (protocolo, entre pares de la misma capa en máquinas distintas) es la definición central de todo el bloque conceptual. Solo la capa **física** tiene comunicación horizontal real: es la única que transmite bits por un medio.

**Principio de diseño asociado: el reloj de arena.** La arquitectura de internet se representa con frecuencia como un reloj de arena (*hourglass*): muchas tecnologías de red por debajo, muchas aplicaciones por encima y **un único protocolo en el cuello**, IP \[KUROSE\]. Esa estrechez deliberada es lo que garantiza que cualquier aplicación funcione sobre cualquier red: todas las combinaciones pasan por el mismo punto. Es la formulación gráfica del lema clásico *IP sobre todo y todo sobre IP*.

> **Ejemplo de aplicación en el ayto.** Cuando un empleado de la Oficina de Atención a la Ciudadanía del distrito de Chamberí abre en su navegador el expediente de una licencia, la capa de aplicación de su equipo dialoga con la capa de aplicación del servidor del IAM; la de transporte, con la de transporte; la de red, con la de red. Ninguno de esos diálogos existe como cable: el único cable va del equipo al conmutador de la oficina. Que el trayecto sea fibra municipal, un enlace radio o una conexión de respaldo de un operador **no cambia una línea** de la aplicación de expedientes. Esa indiferencia es exactamente el valor de la estratificación.

#### 1.2. Organismos internacionales de estandarización

Un protocolo solo sirve si lo implementan varios fabricantes de la misma manera; de ahí que la normalización sea parte constitutiva de la materia. Conviene distinguir tres familias de organismos, porque es fácil atribuir una norma al organismo equivocado.

**1. Organismos de normalización formal (de iure).** Son organizaciones con procedimiento reglado y con representación estatal:

- **ISO** (Organización Internacional de Normalización), con sede en Ginebra, integrada por los organismos nacionales de normalización —en España, **UNE**—. Junto con **IEC** (Comisión Electrotécnica Internacional) forma el comité conjunto **ISO/IEC JTC 1** para las tecnologías de la información. **Es el organismo que publicó el modelo OSI**, como norma **ISO/IEC 7498-1** \[ISO7498\].
- **UIT** (Unión Internacional de Telecomunicaciones), organismo especializado de Naciones Unidas. Su sector de normalización, **UIT-T** (antes CCITT), publica **Recomendaciones** identificadas por una letra y un número: la serie **X** para redes de datos —**X.200** es el modelo OSI, **X.25**, **X.400**, **X.500**, **X.509**—, la serie **V** para transmisión sobre líneas telefónicas, la serie **G** para transmisión digital, la serie **H** para multimedia —**H.323**, **H.264**—, y la serie **Q** para señalización. El sector **UIT-R** gestiona el espectro radioeléctrico.
- **CEN**, **CENELEC** y **ETSI** en el ámbito europeo. **ETSI** es el responsable de las normas de telecomunicación europeas: **GSM**, **TETRA** o los formatos de firma electrónica.
- **AENOR/UNE** en España, que adopta las normas internacionales como **UNE-EN ISO/IEC**.

**2. Organismos de la comunidad de internet (de facto, por consenso e implantación).** Su legitimidad no procede de los Estados sino de la adopción efectiva:

- **IETF** (*Internet Engineering Task Force*): elabora las especificaciones técnicas de internet. **No tiene miembros ni cuotas**: participa quien quiere, el trabajo se organiza en grupos y las decisiones se toman por **consenso aproximado y código que funciona** (*rough consensus and running code*). Publica los **RFC** (*Request for Comments*).
- **IAB** (*Internet Architecture Board*), supervisión arquitectónica; **IRTF** (*Internet Research Task Force*), investigación a largo plazo; **IESG** (*Internet Engineering Steering Group*), dirección del proceso del IETF; e **ISOC** (*Internet Society*), paraguas jurídico y de financiación.
- **ICANN** (*Internet Corporation for Assigned Names and Numbers*), que coordina el espacio de nombres y de números, y su función operativa **IANA**, que mantiene los registros de números de protocolo, puertos, EtherType y bloques de direcciones. La asignación efectiva de direcciones se delega en **cinco registros regionales (RIR)**: **RIPE NCC** (Europa, Oriente Medio y Asia Central), ARIN (Norteamérica), APNIC (Asia-Pacífico), LACNIC (América Latina y Caribe) y AFRINIC (África) \[IANA\].
- **W3C** (*World Wide Web Consortium*) para las tecnologías de la web, y **WHATWG** para el estándar vivo de HTML.

**3. Asociaciones profesionales y consorcios sectoriales.**

- **IEEE** (*Institute of Electrical and Electronics Engineers*), cuyo **comité 802** normaliza las capas 1 y 2 de las redes de área local y metropolitana. Los grupos de trabajo se identifican con un número: **802.3** Ethernet, **802.11** redes inalámbricas, **802.1Q** VLAN, **802.1X** control de acceso por puerto, **802.15** redes personales (Bluetooth, Zigbee) \[IEEE802\].
- **ANSI** (Estados Unidos), **TIA/EIA** (cableado estructurado y conectores), **ECMA** y consorcios como la *Wi-Fi Alliance*, *USB-IF* o *Bluetooth SIG*, que certifican la conformidad de productos.

> **Dato clave.** Reparto de competencias: **el modelo OSI es de ISO** (norma 7498-1) y de la **UIT-T** (Recomendación X.200), con **texto idéntico**. **El modelo TCP/IP y sus protocolos son del IETF** (RFC). **Las capas 1 y 2 de las redes locales son del IEEE** (serie 802). **Los números —puertos, protocolos, direcciones— los administra IANA**, bajo ICANN. Y **la asignación de direcciones a operadores europeos, RIPE NCC**.

**El proceso de un RFC.** Los RFC se numeran de forma **correlativa y permanente**: una vez publicado, un RFC **nunca se modifica**; si cambia la especificación, se publica un RFC nuevo que **actualiza** (*updates*) o **deja obsoleto** (*obsoletes*) al anterior. Por eso hay que citar siempre el número vigente. El proceso de normalización \[RFC1958\] distingue varios estados:

- **Borrador de internet** (*Internet-Draft*): documento de trabajo, con **caducidad de seis meses**, que **no es un RFC**.
- **Norma propuesta** (*Proposed Standard*): especificación estable, revisada y con consenso; es el nivel en el que se publica hoy la mayoría.
- **Norma de internet** (*Internet Standard*): nivel máximo de madurez, reservado a las especificaciones con implantación amplia y demostrada. Reciben además un número **STD**: **STD 5** (IP e ICMP), **STD 6** (UDP), **STD 7** (TCP), **STD 13** (DNS), **STD 86** (IPv6).
- Categorías no normativas: **Informativo**, **Experimental**, **Histórico** y **Mejor práctica actual** (**BCP**), que es donde viven documentos como la RFC 1918.

> **Dato clave.** **La especificación vigente de TCP es la RFC 9293, de agosto de 2022**, que sustituye a la histórica **RFC 793** de 1981 e integra las correcciones que estaban dispersas en otras seis RFC \[RFC9293\]. Del mismo modo, **la especificación vigente de IPv6 es la RFC 8200 (2017)**, que sustituye a la RFC 2460 \[RFC8200\]. Muchos temarios siguen citando las antiguas: es un error de actualización fácil de detectar.

Ver **diagrama D2**, que reparte los organismos por ámbito y por capa.

------------------------------------------------------------------------

### 2. El Modelo de Referencia de Interconexión de Sistemas Abiertos (OSI) de ISO

#### 2.1. Origen y principios de diseño del modelo OSI

**Contexto histórico.** A finales de los años setenta, las redes de datos eran islas propietarias: **SNA** de IBM, **DECnet** de Digital, **XNS** de Xerox. Cada fabricante tenía su arquitectura y dos equipos de marcas distintas no se comunicaban. En **1977**, ISO abrió los trabajos de un modelo común; el **modelo de referencia OSI** se publicó como norma **ISO 7498 en 1984**, y su **segunda edición**, la vigente, es **ISO/IEC 7498-1:1994**, de 15 de noviembre de 1994, que incorpora de forma explícita el modo de transmisión **no orientado a conexión** \[ISO7498\]. La UIT-T publicó el mismo texto como **Recomendación X.200**, aprobada el **1 de julio de 1994** \[X200\].

La expresión **«sistema abierto»** que da nombre al modelo tiene un significado técnico preciso: es el sistema que **cumple las normas OSI** y que, por tanto, puede comunicarse con cualquier otro que también las cumpla, con independencia de su fabricante. Se opone a **sistema cerrado o propietario**.

**Qué es y qué no es el modelo OSI.** El propio texto de la norma lo advierte: OSI es un **modelo de referencia**, no una especificación de implantación ni un conjunto de protocolos \[ISO7498\]. Su función es **dar un marco común** para situar y coordinar el desarrollo de normas de comunicación. ISO desarrolló después protocolos concretos para cada capa —**X.25**, **TP0-TP4** en transporte, **X.400** para correo, **X.500** para directorio, **CLNP** como protocolo de red— que hoy están, salvo excepciones como X.500 y su derivado LDAP, en desuso.

> **Dato clave.** Hay que separar dos cosas que se confunden con facilidad: **el modelo OSI de siete capas triunfó** y sigue siendo el vocabulario universal con el que se habla de redes (nadie dice «el nivel del conmutador», dice «capa 2»); **la pila de protocolos OSI fracasó** y fue desplazada por TCP/IP. Afirmar que «el modelo OSI está obsoleto» es falso; afirmar que «los protocolos OSI son de uso general», también.

**Los principios de descomposición en capas.** La norma enuncia los criterios que se siguieron para decidir **cuántas capas** debía haber y **dónde** poner las fronteras. Conviene poder citar los principales:

1.  Crear una capa nueva donde se necesite un **nivel de abstracción distinto**.
2.  Que cada capa desempeñe una **función bien definida**.
3.  Elegir las fronteras de modo que se **minimice el flujo de información** a través de las interfaces.
4.  Que la función de cada capa se elija pensando en la posibilidad de **normalizarla internacionalmente**.
5.  Que el número de capas sea **suficiente** para no juntar funciones dispares, pero **no tan grande** que la arquitectura se vuelva inmanejable.
6.  Permitir **modificar una capa por dentro** sin afectar a las demás, mientras se respete la interfaz.
7.  Crear **subcapas** cuando dentro de una capa convivan funciones claramente separables, y poder **puentearlas** cuando no se necesiten.

**El resultado: siete capas.** Numeradas de abajo arriba: **1 física, 2 enlace de datos, 3 red, 4 transporte, 5 sesión, 6 presentación y 7 aplicación**. Las reglas de oro del modelo son dos:

- Una capa **solo se comunica con las adyacentes** dentro de la misma máquina.
- La capa *N* de un sistema **solo dialoga con la capa *N*** del otro, mediante el protocolo de nivel *N*.

> **Dato clave.** Regla mnemotécnica clásica en español para el orden **de abajo arriba** (1→7): *Felipe **E**nvió **R**opa **T**ras **S**er **P**edida **A**yer* — **F**ísica, **E**nlace, **R**ed, **T**ransporte, **S**esión, **P**resentación, **A**plicación. En inglés, de arriba abajo, *All People Seem To Need Data Processing*. **Casi todo OSI se resuelve sabiendo colocar bien el número de capa.**

#### 2.2. Conceptos de capa, servicio, interfaz y protocolo

Esta es la terminología formal del modelo, y es donde están los matices conceptuales más finos. La norma define cada término con precisión \[ISO7498\]:

| Término | Definición | Dónde vive |
|----|----|----|
| **Capa** (*layer*) | Subdivisión de la arquitectura que agrupa funciones homogéneas y presta un servicio a la capa superior | Concepto arquitectónico |
| **Entidad** (*entity*) | Elemento activo de una capa que realiza sus funciones; puede ser un proceso, un módulo software o un circuito. Dos entidades de la misma capa en máquinas distintas son **entidades pares** (*peer entities*) | Dentro de una capa |
| **Servicio** (*service*) | Conjunto de **operaciones que una capa ofrece** a la capa inmediatamente superior. Define **qué** se ofrece, nunca cómo se consigue | Frontera entre capas *N* y *N+1* |
| **Interfaz** (*interface*) | Definición concreta de las **primitivas y parámetros** con los que la capa superior invoca el servicio | Frontera, dentro de la misma máquina |
| **Protocolo** (*protocol*) | Conjunto de **reglas y formatos** que gobiernan el diálogo entre **entidades pares** de la misma capa en máquinas distintas: sintaxis, semántica y temporización | Horizontal, entre máquinas |
| **Punto de acceso al servicio** (**SAP**) | Punto concreto, identificado por una dirección, en el que la capa *N* ofrece su servicio a la capa *N+1*. Una capa puede tener varios SAP | Frontera, con dirección propia |

> **Dato clave.** La distinción **servicio / interfaz / protocolo** es la confusión clásica: el **servicio** es *qué* hace la capa para la de arriba; la **interfaz**, *cómo se le pide*; el **protocolo**, *cómo lo consigue hablando con su par*. Corolario: **se puede cambiar el protocolo de una capa sin cambiar su servicio**, y la capa superior no se entera. Es exactamente lo que ocurrió al pasar de IPv4 a IPv6 en el servicio que la capa de red presta al transporte.

**Las cuatro primitivas de servicio.** El modelo formaliza el diálogo entre capas con cuatro primitivas, que hay que saber nombrar y ordenar:

1.  **Petición** (*request*): la capa superior del **origen** solicita el servicio.
2.  **Indicación** (*indication*): la capa correspondiente del **destino** avisa a su capa superior de que hay una petición.
3.  **Respuesta** (*response*): la capa superior del **destino** contesta.
4.  **Confirmación** (*confirm*): la capa del **origen** informa a su capa superior del resultado.

Un servicio que emplea las cuatro es **confirmado**; el que solo usa petición e indicación, **no confirmado**.

**Los dos modos de servicio.** Distinción capital, porque atraviesa todo el tema:

- **Orientado a conexión** (*connection-oriented*). Tres fases: **establecimiento**, **transferencia** y **liberación**. La conexión mantiene **estado** en ambos extremos, garantiza normalmente la **entrega ordenada** y permite control de flujo y de errores extremo a extremo. Analogía: la llamada telefónica. Ejemplos: **TCP**, X.25, la conexión virtual de Frame Relay.
- **No orientado a conexión** (*connectionless*) o de **datagramas**. Cada unidad de datos viaja **de forma independiente**, con la dirección completa del destino, sin fase previa ni estado compartido. No se garantiza la entrega, ni el orden, ni la ausencia de duplicados. Analogía: la carta postal. Ejemplos: **IP** y **UDP**.

> **Dato clave.** Un servicio orientado a conexión **no implica** un medio dedicado ni un circuito físico: TCP es orientado a conexión y viaja sobre IP, que es de datagramas. La orientación a conexión es una propiedad **lógica**, del estado que mantienen los extremos. Y a la inversa: un servicio de datagramas puede ser **fiable** si alguien, por encima, se ocupa de la fiabilidad.

**Calidad de servicio.** El modelo asocia a cada servicio unos parámetros de calidad —retardo, variación del retardo o fluctuación, tasa de error residual, caudal— que la capa superior puede solicitar y que la inferior puede o no garantizar.

Ver **diagrama D3**, que muestra la anatomía de una capa con sus entidades, su SAP, su interfaz y su protocolo entre pares.

#### 2.3. Descripción de las capas del modelo OSI

Antes del detalle, la panorámica. El modelo divide las siete capas en dos grupos, división que la norma no impone pero que la doctrina emplea de forma unánime:

- **Capas orientadas a la red** o **inferiores** (1 a 3, y en algunas clasificaciones también la 4): se ocupan del **transporte de los datos a través de la red**. Están presentes en **todos los equipos del camino**, incluidos los intermedios.
- **Capas orientadas a la aplicación** o **superiores** (5 a 7, y en algunas clasificaciones desde la 4): se ocupan de **los procesos de usuario**. Solo existen en los **equipos terminales**, no en los equipos intermedios.

> **Dato clave.** Consecuencia de esa división: un **encaminador** implementa hasta la **capa 3**; un **conmutador** clásico, hasta la **capa 2**; un **concentrador** o repetidor, solo la **capa 1**. Un **cortafuegos de nueva generación** o un **balanceador de aplicación** llegan hasta la **capa 7**. La capa de **transporte es de extremo a extremo**: el encaminador del camino **no la interpreta**. Ver el Tema 37 para el detalle de los dispositivos de interconexión.

Ver **diagrama D4**, con las siete capas, su función, su PDU y sus ejemplos de protocolo.

##### 2.3.1. Capas orientadas a la red: física, enlace de datos y red

**Capa 1 — Física.** Se ocupa de la **transmisión de bits sin estructurar** sobre un medio. No entiende de tramas ni de direcciones: su unidad es el **bit**. Sus funciones y especificaciones se agrupan en cuatro características:

- **Mecánicas**: forma y dimensiones del conector, número de patillas (RJ-45, conectores ópticos LC o SC).
- **Eléctricas u ópticas**: niveles de tensión, longitud de onda, potencia, duración de un bit.
- **Funcionales**: significado de cada circuito o hilo.
- **Procedimentales**: secuencia de acciones para establecer y terminar la transmisión.

Aquí se sitúan la **codificación de línea** (NRZ, Manchester, 4B/5B, 8B/10B), la **modulación**, la elección entre transmisión **serie o paralela**, **síncrona o asíncrona**, y los modos **símplex, semidúplex y dúplex**. También pertenecen a esta capa los **medios de transmisión** —par trenzado, coaxial, fibra óptica, radio— y las tasas de transferencia.

> **Relación con otros temas.** Los medios de transmisión, la modulación, la multiplexación y los modos de comunicación son el objeto del **Tema 33**, y las técnicas de transmisión en el ámbito local, del **Tema 37**. Aquí interesan solo como **contenido de la capa 1** del modelo.

**Capa 2 — Enlace de datos.** Convierte un medio de transmisión crudo, con errores, en un **enlace que parece libre de errores** para la capa de red. Su unidad de datos es la **trama** (*frame*). Funciones:

- **Delimitación de tramas** (*framing*): decidir dónde empieza y dónde acaba cada trama en el flujo de bits, mediante contadores, delimitadores con relleno de bits o de octetos, o violaciones de código de línea.
- **Direccionamiento físico**: identificar el equipo dentro del mismo segmento mediante la **dirección MAC**.
- **Detección y, en su caso, corrección de errores**: mediante **CRC** —en Ethernet, el campo **FCS** de 32 bits— o sumas de comprobación. Una trama con error se **descarta**; salvo en protocolos con retransmisión de enlace, no se recupera aquí.
- **Control de flujo** entre dos equipos adyacentes.
- **Control de acceso al medio** cuando el medio es compartido.

La norma **IEEE 802** divide esta capa en **dos subcapas** \[IEEE802\]:

- **LLC** (*Logical Link Control*, **IEEE 802.2**), superior: ofrece a la capa de red un servicio uniforme e independiente de la tecnología, y multiplexa protocolos superiores.
- **MAC** (*Medium Access Control*), inferior: resuelve **quién transmite** en un medio compartido (**CSMA/CD** en Ethernet clásica, **CSMA/CA** en Wi-Fi, paso de testigo en Token Ring) y gestiona el direccionamiento físico.

Protocolos y tecnologías de esta capa: **Ethernet (IEEE 802.3)**, **Wi-Fi (IEEE 802.11)**, **PPP**, **HDLC**, **Frame Relay**, **ATM** —esta última, a caballo entre las capas 2 y 3—.

**Capa 3 — Red.** Es la capa del **encaminamiento**. Su misión es llevar la unidad de datos **desde el origen hasta el destino final**, atravesando tantas redes intermedias como haga falta. Su unidad es el **paquete** o **datagrama**. Funciones:

- **Direccionamiento lógico**, jerárquico e independiente del hardware: la **dirección IP**.
- **Encaminamiento** (*routing*): decidir por qué camino sale cada paquete, con tablas construidas de forma estática o por protocolos de encaminamiento.
- **Reenvío** (*forwarding*): la operación concreta, paquete a paquete, de consultar la tabla y sacarlo por una interfaz.
- **Fragmentación y reensamblado** cuando el paquete no cabe en la MTU del siguiente enlace.
- **Control de congestión** e interconexión de redes heterogéneas (*internetworking*).

> **Dato clave.** **Encaminamiento** (*routing*) y **reenvío** (*forwarding*) no son sinónimos: el primero es el **proceso de construir la tabla de rutas**, el segundo es la **decisión individual** de sacar un paquete por una interfaz consultando esa tabla. El primero es lento y global; el segundo, rapidísimo y local.

La capa de red es también donde se sitúa la distinción entre **circuitos virtuales** —la red mantiene estado por conexión, como en X.25 o ATM— y **datagramas** —la red no mantiene estado, como en IP—.

##### 2.3.2. Capas orientadas a la sesión y al usuario: transporte, sesión, presentación y aplicación

**Capa 4 — Transporte.** Es **la primera capa verdaderamente de extremo a extremo**: su interlocutor no es el siguiente equipo del camino, sino el proceso del otro extremo. Es la capa **frontera** del modelo, la que separa las capas orientadas a la red de las orientadas a la aplicación. Su unidad es el **segmento** (o *TPDU* en la terminología de la norma). Funciones:

- **Direccionamiento de procesos** mediante **puertos** o SAP de transporte, lo que permite **multiplexar** varias comunicaciones sobre una única dirección de red.
- **Segmentación y reensamblado** del flujo de datos de la aplicación.
- **Establecimiento, mantenimiento y liberación de conexiones** extremo a extremo, en el modo orientado a conexión.
- **Entrega fiable**: detección de pérdidas, **retransmisión**, eliminación de duplicados y **entrega ordenada**.
- **Control de flujo** extremo a extremo, para que el emisor no desborde al receptor.
- **Control de congestión**, para que el conjunto de emisores no desborde a la red.

La norma OSI define **cinco clases de protocolo de transporte, de TP0 a TP4**, según la fiabilidad que ofrezca la red subyacente: **TP0** es la más simple, pensada para redes fiables; **TP4** es la más completa, con detección y recuperación de errores, y es **la equivalente funcional de TCP**.

> **Dato clave.** La equivalencia clave: **TP4 de OSI ≡ TCP**, y **CLNP de OSI ≡ IP**. Y el dato de partida: **la capa 4 es la más baja de las que solo existen en los extremos**. Un encaminador intermedio **no tiene capa de transporte** para el tráfico que reenvía.

**Capa 5 — Sesión.** Organiza y sincroniza el **diálogo** entre dos aplicaciones. Es la capa más discutida del modelo porque, en la práctica, sus funciones acabaron absorbidas por las aplicaciones. Funciones:

- **Establecimiento, gestión y cierre de sesiones** entre aplicaciones.
- **Control del diálogo**: decidir de quién es el turno, mediante **gestión de testigo** (*token management*), en comunicaciones semidúplex.
- **Sincronización**: insertar **puntos de comprobación** (*checkpoints*) en transferencias largas, de modo que una interrupción no obligue a repetirlo todo, sino solo desde el último punto.
- **Gestión de actividades** y agrupación de operaciones.

Ejemplos citados habitualmente: **RPC**, **NetBIOS**, **PPTP**, **SIP** o los mecanismos de sesión de **NFS**.

**Capa 6 — Presentación.** Es la única capa que se ocupa de la **sintaxis y la semántica de la información**, no de su transporte. Resuelve el problema de que dos máquinas representen los datos de forma distinta. Funciones:

- **Conversión de la representación**: juegos de caracteres (**ASCII**, **ISO 8859-15**, **Unicode/UTF-8**), representación numérica y **ordenación de octetos** (*big-endian* frente a *little-endian*). La norma distingue la **sintaxis abstracta** —la estructura lógica de los datos— de la **sintaxis de transferencia** —cómo se codifican en el cable—; el ejemplo canónico es **ASN.1** con sus reglas de codificación **BER** y **DER**.
- **Compresión** de los datos.
- **Cifrado y descifrado**.

> **Dato clave.** En el modelo OSI **el cifrado y la compresión son funciones de la capa 6, la de presentación**. En la práctica de la pila TCP/IP, en cambio, **TLS se sitúa entre el transporte y la aplicación** y sus funciones se reparten entre lo que OSI llamaría capas 5 y 6; a veces se le denomina, por eso, «capa 6,5». **Nota**: la arquitectura de seguridad de OSI está en una norma aparte, la **ISO/IEC 7498-2** (UIT-T X.800), que define cinco servicios de seguridad y los reparte por capas \[ISO7498-2\].

**Capa 7 — Aplicación.** Es la capa que **interactúa con los procesos de usuario**. Un error común consiste en identificarla con el programa: la capa 7 **no es el navegador**, es el **protocolo** que el navegador habla (**HTTP**). Contiene los protocolos que prestan servicios directamente utilizables: **HTTP**, **SMTP**, **FTP**, **DNS**, **Telnet**, **SSH**, **SNMP**, **LDAP**, y en la pila OSI **X.400** (correo), **X.500** (directorio), **FTAM** (ficheros) y **VT** (terminal virtual).

> **Ejemplo de aplicación en el ayto.** Trasladado a la red municipal: la **capa 1** es el cable de par trenzado que va del puesto de la oficina de distrito a la roseta; la **capa 2**, la trama Ethernet que llega al conmutador de planta y su VLAN; la **capa 3**, la dirección IP del puesto y la ruta que sigue el paquete hasta el CPD del IAM; la **capa 4**, la conexión TCP con el servidor de expedientes; las **capas 5 y 6**, la sesión autenticada y el cifrado TLS; y la **capa 7**, el diálogo HTTP de la aplicación de tramitación. Las siete capas caben en un solo clic.

#### 2.4. Unidades de datos de protocolo (PDU) y encapsulamiento

Este epígrafe contiene la terminología formal central del modelo. La norma \[ISO7498\] define un vocabulario preciso:

| Sigla | Nombre | Qué es |
|----|----|----|
| **PDU** | *Protocol Data Unit* — unidad de datos de protocolo | La unidad completa que **la capa *N* intercambia con su par**: `PDU(N) = PCI(N) + SDU(N)` |
| **SDU** | *Service Data Unit* — unidad de datos de servicio | Los datos que la capa *N* **recibe de la capa *N+1*** y debe entregar íntegros a su par. Para la capa *N* son **carga útil opaca**: no los interpreta |
| **PCI** | *Protocol Control Information* — información de control de protocolo | La **cabecera** que la capa *N* añade para hablar con su par: direcciones, números de secuencia, sumas de comprobación |
| **IDU** | *Interface Data Unit* — unidad de datos de interfaz | Lo que se pasa realmente **a través de la interfaz** entre dos capas: la SDU más la información de control de interfaz (**ICI**), que es local y no viaja |

**La regla de oro, que hay que saber escribir:** la **PDU de la capa *N*** se convierte en la **SDU de la capa *N−1***.

`PDU(N) = PCI(N) + SDU(N)` y, al bajar de capa, `SDU(N−1) = PDU(N)`

**Encapsulamiento** es el nombre del proceso descendente: cada capa recibe la PDU de la superior, la trata como carga útil y le antepone su cabecera. **Desencapsulamiento** es el proceso inverso en el destino: cada capa retira su cabecera, la interpreta y entrega el resto a la capa superior. Ver **diagrama D5**.

> **Dato clave.** Nombres específicos de la PDU por capa, memorización obligatoria: capa 1 → **bit**; capa 2 → **trama** (*frame*); capa 3 → **paquete** o **datagrama**; capa 4 → **segmento** (TCP) o **datagrama** (UDP); capas 5, 6 y 7 → **datos** o **mensaje**. Ojo con «datagrama»: se usa **tanto en la capa 3** (datagrama IP) **como en la capa 4** (datagrama UDP); el contexto lo desambigua.

La capa 2 tiene una particularidad: es la única que añade información **por delante y por detrás**. Antepone su cabecera —direcciones MAC y tipo— y **añade una cola** con el código de detección de errores (**FCS**) y, en su caso, el delimitador de fin de trama.

> **Ejercicio resuelto.** **Cuánto ocupa realmente un «hola» de cinco letras.** Un puesto de la oficina de distrito envía cinco octetos de datos de aplicación a un servidor del IAM por TCP sobre IPv4 y Ethernet. ¿Cuántos octetos salen por el cable, y qué porcentaje son datos útiles? 1. **Capa 7**: 5 octetos de datos. 2. **Capa 4 (TCP)**: cabecera **mínima de 20 octetos** \[RFC9293\] → segmento de **25**. 3. **Capa 3 (IPv4)**: cabecera **mínima de 20 octetos** \[RFC791\] → paquete de **45**. 4. **Capa 2 (Ethernet II)**: cabecera de **14 octetos** (6 MAC destino + 6 MAC origen + 2 EtherType) y cola **FCS de 4** → 45 + 18 = **63 octetos**. Pero Ethernet exige una **trama mínima de 64 octetos** (sin contar preámbulo), así que se **rellena** (*padding*) hasta 64. 5. **Capa 1**: se añaden **7 octetos de preámbulo + 1 de delimitador de inicio (SFD)** y, entre tramas, un **hueco entre tramas** equivalente a 12 octetos. **Resultado**: por el cable circulan **64 octetos** de trama (72 con preámbulo y delimitador) para transportar **5** de datos útiles: en torno a un **7 %** de eficiencia. Esa es, en cifras, la sobrecarga de la estratificación, y es la razón por la que agrupar datos en menos envíos —el algoritmo de Nagle en TCP, por ejemplo— mejora tanto el rendimiento. **Comprobación**: si en lugar de 5 octetos se enviaran 1.460, el paquete IP mediría 1.500 —justo la **MTU de Ethernet**— y la trama, 1.518. La eficiencia subiría al **96 %**. Es exactamente por eso por lo que **1.460** es el tamaño máximo de segmento (**MSS**) habitual en IPv4 sobre Ethernet: 1.500 − 20 (IP) − 20 (TCP).

------------------------------------------------------------------------

### 3. El Modelo TCP/IP

#### 3.1. Origen y evolución de la arquitectura TCP/IP

**El encargo original.** A finales de los años sesenta, la agencia **ARPA** (después **DARPA**) del Departamento de Defensa estadounidense financió una red experimental de conmutación de paquetes, **ARPANET**, que entró en servicio en **1969** con cuatro nodos universitarios. Su protocolo original, **NCP** (*Network Control Program*), servía para una red homogénea, pero no para interconectar **redes distintas** —una red de radiopaquetes, una red por satélite y una red cableada— que era lo que se quería a continuación.

En **1974**, **Vinton Cerf** y **Robert Kahn** publicaron el artículo que resolvía el problema: un **protocolo de interconexión de redes** que trataba a cada red subyacente como una caja negra y construía sobre todas ellas una **red virtual única**. De ese trabajo salió el **TCP**, que inicialmente hacía a la vez de protocolo de red y de transporte. En **1978** se produjo la decisión de diseño más importante de la arquitectura: **separar TCP en dos protocolos**, dejando en **IP** lo que debía ser común a todo el sistema —direccionamiento y reenvío, sin garantías— y en **TCP** lo que solo interesaba a los extremos —fiabilidad, orden y control de flujo—. Esa separación es la que permite que hoy exista **UDP** al lado de TCP, y la que hace posible ejecutar sobre IP protocolos que no quieren fiabilidad.

**Las fechas clave.** El **1 de enero de 1983** —conocido como *flag day*— ARPANET conmutó definitivamente de NCP a TCP/IP. Ese es el día en que suele fecharse el nacimiento de internet tal como se conoce. La arquitectura quedó documentada de forma normativa en la **RFC 1122** (1989) para los equipos terminales y en la **RFC 1812** (1995) para los encaminadores \[RFC1122\] \[RFC1812\].

**Los objetivos de diseño y su jerarquía.** David Clark dejó escrita la lista, **por orden de prioridad**, y ese orden explica casi todas las decisiones de la arquitectura \[CLARK88\]:

1.  **La comunicación debe sobrevivir a la pérdida de redes o de pasarelas.** Objetivo dominante, de origen militar. De él se derivan dos consecuencias: que el **estado de la conexión reside en los extremos** y no en la red, y que la red pueda reencaminar sin que la conexión se caiga.
2.  **Soportar múltiples tipos de servicio de comunicación** (fiable y ordenado, pero también rápido y sin garantías). De aquí salió la separación TCP/UDP.
3.  **Acomodar una variedad de redes** subyacentes, exigiéndoles lo mínimo.
4.  Permitir la **gestión distribuida** de los recursos.
5.  Ser **eficiente en costes**.
6.  Permitir la **incorporación de nuevos equipos con poco esfuerzo**.
7.  Que los recursos utilizados sean **contabilizables**.

> **Dato clave.** El orden importa: la **supervivencia ante fallos** era el objetivo número uno y la **contabilidad de recursos** el último. Que la facturación y la seguridad quedaran al final de la lista explica buena parte de los problemas actuales de internet.

**El principio extremo a extremo.** Formulado por Saltzer, Reed y Clark en 1984 \[SALTZER\], dice que **una función solo debe implantarse en la red si no puede implantarse correctamente en los extremos**, y que si de todos modos hay que implantarla en los extremos, hacerlo también en la red suele ser una optimización, no un requisito. Es el fundamento de que **IP no garantice nada** —«mejor esfuerzo», *best effort*— y de que la fiabilidad viva en TCP, en los equipos terminales.

La consecuencia arquitectónica es la **red tonta con extremos inteligentes**, opuesta al modelo de la red telefónica clásica —red inteligente con terminales tontos—. Es también lo que permitió que internet incorporara la web, el vídeo o la telefonía IP **sin cambiar la red**.

> **Relación con otros temas.** El principio extremo a extremo tiene una consecuencia directa en el **Tema 36**: si la red no garantiza nada, tampoco protege nada, y la seguridad debe añadirse en capas superiores (TLS) o mediante túneles explícitos (IPsec, VPN). Y en el **Tema 31**: es el mismo argumento que explica por qué la nube pudo construirse sobre internet sin rediseñarla.

**Evolución.** Los hitos que conviene situar: **1983** conmutación a TCP/IP; **1984** aparición del **DNS** \[RFC1034\], que sustituye al fichero `HOSTS.TXT` centralizado; **1989-1991** invención de la **web** en el CERN; **1993** navegador Mosaic y apertura comercial; **1993-1995** introducción de **CIDR** \[RFC950\] ante el agotamiento del direccionamiento por clases; **1998** primera especificación de **IPv6**; **2011-2019** agotamiento sucesivo de los bloques libres de IPv4 en IANA y en los registros regionales —**RIPE NCC** agotó su reserva general en noviembre de 2019 y desde entonces solo asigna bloques `/24` de recuperación \[RIPE\]—; **2017** publicación de la especificación vigente de IPv6, la **RFC 8200**; **2022** publicación de la **RFC 9293**, especificación consolidada de TCP.

#### 3.2. Niveles funcionales del modelo TCP/IP

**Cuántos niveles tiene el modelo TCP/IP.** Es la primera trampa del epígrafe, y hay que saber contestarla con matices:

- La **RFC 1122**, que es la fuente normativa, describe **cuatro capas**: **enlace** (*link layer*), **internet**, **transporte** y **aplicación** \[RFC1122\].
- Buena parte de la doctrina académica desdobla la inferior en **física** y **enlace** y presenta un **modelo híbrido de cinco capas**, más cómodo para enseñar \[TANENBAUM\] \[KUROSE\].
- Algunos textos y muchos manuales de fabricante usan la denominación **«capa de acceso a la red»** (*network access layer*) para la inferior, que es la que emplea el enunciado oficial de este tema.

> **Dato clave.** Si la pregunta cita la RFC 1122, la respuesta es **cuatro capas**. Si habla del «modelo híbrido» o «de cinco capas», se refiere al desdoblamiento didáctico de la inferior. **El enunciado oficial de este tema usa «capa de acceso a la red»**, lo que sitúa el tema en el modelo de cuatro niveles. Nunca son siete: siete son las de OSI.

Descripción de los cuatro niveles, de abajo arriba (ver **diagrama D6**):

**Nivel 1 — Acceso a la red** (*network access* o *link*). Es el nivel que el modelo **deliberadamente no especifica**. Su misión es transmitir el datagrama IP por una red concreta, sea cual sea. La arquitectura solo exige que exista un método para **encapsular un datagrama IP** en el formato de esa red y para **resolver la dirección física** correspondiente a una dirección IP. Por eso puede funcionar sobre Ethernet, Wi-Fi, PPP, MPLS, una línea serie o —según reza la broma canónica de la RFC 1149— sobre palomas mensajeras.

**Nivel 2 — Internet** (*internet layer*). Es el **cuello del reloj de arena**, el único nivel obligatorio y común. Su protocolo es **IP**, en sus versiones **4** y **6**, acompañado de **ICMP**, **IGMP** y, en el caso de IPv4, de **ARP** como protocolo auxiliar. Presta un servicio **no orientado a conexión, no fiable y de mejor esfuerzo**: no garantiza entrega, ni orden, ni ausencia de duplicados, ni integridad de los datos. Sus dos funciones son **direccionar** y **encaminar**.

**Nivel 3 — Transporte.** Presta comunicación **extremo a extremo entre procesos**, identificados por **puertos**. Dos protocolos con filosofías opuestas: **TCP**, orientado a conexión y fiable, y **UDP**, de datagramas y sin garantías. En los últimos años se les ha añadido **SCTP** —orientado a mensajes, con multitrayecto— y, sobre UDP, **QUIC** \[RFC9110\], que implementa en espacio de usuario funciones equivalentes a las de TCP y a las de TLS y es el transporte de **HTTP/3**.

**Nivel 4 — Aplicación.** Reúne, en un solo nivel, lo que OSI reparte entre las capas 5, 6 y 7. Cada protocolo de aplicación resuelve por su cuenta la sesión, la representación de los datos y el servicio: **HTTP**, **SMTP**, **DNS**, **FTP**, **SSH**, **SNMP**, **DHCP**, **NTP**, **LDAP**.

> **Dato clave.** Cuatro afirmaciones sobre la pila TCP/IP que aparecen una y otra vez, y que son **verdaderas**: (1) **IP no es fiable y no está orientado a conexión**; (2) **la fiabilidad, si se quiere, la aporta TCP en los extremos**; (3) **el modelo no especifica el nivel de acceso a la red**, que es competencia de cada tecnología; y (4) **la capa de aplicación de TCP/IP absorbe las capas 5, 6 y 7 de OSI**.

**Terminología de los equipos.** En el vocabulario de la RFC 1122 se distingue entre **host** —equipo terminal, que implementa las cuatro capas— y **pasarela** o **encaminador** —equipo intermedio, que implementa las dos inferiores y reenvía—. Un equipo con varias interfaces de red se denomina **multiconectado** (*multihomed*); si además reenvía tráfico entre ellas, actúa como encaminador.

#### 3.3. Encapsulamiento y demultiplexación de datos

El encapsulamiento en TCP/IP sigue exactamente la regla general vista en §2.4, pero con nombres propios que conviene fijar:

| Nivel | PDU | Cabecera que añade | Direcciones que usa |
|----|----|----|----|
| Aplicación | **Mensaje** / flujo de datos | Propia de cada protocolo | Nombres (URL, dirección de correo) |
| Transporte | **Segmento** (TCP) / **Datagrama** (UDP) | 20 octetos (TCP) / 8 octetos (UDP) | **Puertos** (16 bits) |
| Internet | **Paquete** o **datagrama IP** | 20 octetos (IPv4) / 40 (IPv6) | **Direcciones IP** (32 o 128 bits) |
| Acceso a la red | **Trama** | 14 octetos + 4 de cola (Ethernet II) | **Direcciones MAC** (48 bits) |

**La demultiplexación** es el proceso inverso y es, probablemente, el mecanismo más elegante de la arquitectura. Cuando llega una trama, el receptor tiene que decidir **a quién entregarla** en cada salto hacia arriba, y lo hace con **un campo por nivel**, cada uno situado en la cabecera de la capa que lo lee (ver **diagrama D7**):

1.  **De la capa 2 a la capa 3**: el campo **EtherType** de la trama Ethernet dice qué protocolo de red va dentro. Valores memorizables: **`0x0800` = IPv4**, **`0x0806` = ARP**, **`0x86DD` = IPv6**, `0x8100` = etiqueta VLAN 802.1Q \[IANA\].
2.  **De la capa 3 a la capa 4**: el campo **Protocolo** de IPv4 (o **Siguiente cabecera**, *Next Header*, en IPv6) dice qué protocolo de transporte va dentro. Valores memorizables: **1 = ICMP**, **6 = TCP**, **17 = UDP**, **41 = IPv6 encapsulado**, **50 = ESP**, **51 = AH**, **58 = ICMPv6**, **89 = OSPF** \[IANA\].
3.  **De la capa 4 a la aplicación**: el **puerto de destino** dice a qué proceso se entrega.

> **Dato clave.** Los tres campos de la demultiplexación —**EtherType → Protocolo/Next Header → Puerto destino**— son de memorización obligatoria, junto con al menos estos valores: `0x0800` IPv4, `0x0806` ARP, `0x86DD` IPv6; protocolo **1** ICMP, **6** TCP, **17** UDP, **50** ESP, **51** AH, **58** ICMPv6. **Cuidado con la confusión más frecuente del temario: el número 6 es el número de protocolo de TCP en la cabecera IP, no tiene ninguna relación con IPv6.**

**Identificación de una conexión: la quíntupla.** Un extremo de comunicación queda identificado por el par **(dirección IP, puerto)**, que es lo que clásicamente se llama **socket** o zócalo. Una conexión completa se identifica por la **quíntupla**: **protocolo de transporte, IP origen, puerto origen, IP destino, puerto destino**. Es lo que permite que un servidor web atienda a miles de clientes **por el mismo puerto 443**: cada conexión se distingue por la IP y el puerto de origen del cliente, que son distintos.

> **Ejercicio resuelto.** **Seguir un clic desde la oficina de distrito hasta el servidor del IAM.** Un empleado en `10.20.7.45` abre `https://sede.madrid.es` desde su navegador. Traza completa del encapsulamiento y de la demultiplexación: **Bajada, en el puesto:** 1. El navegador prepara una petición **HTTP**, que TLS cifra. Es la carga útil. 2. La capa de transporte añade una cabecera **TCP** con **puerto origen 51.324** —efímero, del rango dinámico— y **puerto destino 443**. Es un **segmento**. 3. La capa de internet añade una cabecera **IPv4** con **origen 10.20.7.45** y **destino** la dirección pública del servidor, y pone **6** en el campo Protocolo. Es un **paquete**. 4. El puesto compara el destino con su máscara: no está en su subred, luego el paquete va a la **puerta de enlace predeterminada**. Consulta su caché **ARP** para conocer la **MAC del encaminador**, no la del servidor. 5. La capa de acceso a la red construye una **trama Ethernet** con **MAC destino = la del encaminador**, **MAC origen = la del puesto** y **EtherType `0x0800`**. **En el camino:** cada encaminador **desecha la trama entrante y construye una nueva** para el siguiente salto, cambiando las MAC de origen y destino; **decrementa el TTL**; y **no toca** ni las direcciones IP ni el segmento TCP —salvo que haya traducción de direcciones, en cuyo caso sí se reescriben la IP y el puerto de origen—. **Subida, en el servidor:** 6. La capa 2 comprueba el **FCS**, ve `0x0800` y entrega a **IPv4**. 7. IPv4 comprueba que la dirección de destino es suya, ve **Protocolo = 6** y entrega a **TCP**. 8. TCP ve **puerto destino 443** y entrega al proceso del servidor web. **Las dos conclusiones que hay que extraer:** primero, **las direcciones MAC cambian en cada salto y las direcciones IP no cambian nunca** (salvo NAT); segundo, el **TTL solo lo toca la capa 3**, y por eso `traceroute` funciona: envía paquetes con TTL creciente y recoge los mensajes ICMP de «tiempo excedido» que devuelve cada encaminador.

------------------------------------------------------------------------

### 4. Comparativa entre el Modelo OSI y el Modelo TCP/IP

#### 4.1. Correspondencia y equivalencia entre capas

La comparación es central en el tema, y hay que poder trazar la tabla de memoria. La correspondencia **no es exacta**: es una aproximación funcional, porque los dos modelos parten de premisas distintas.

| OSI | N.º | Correspondencia en TCP/IP | Observación |
|----|----|----|----|
| Aplicación | 7 | **Aplicación** | Las tres capas superiores de OSI se **funden** en una sola |
| Presentación | 6 | **Aplicación** | Cada protocolo de aplicación resuelve por su cuenta el formato y el cifrado |
| Sesión | 5 | **Aplicación** | La gestión del diálogo la asume cada protocolo |
| Transporte | 4 | **Transporte** | Correspondencia **casi exacta**: TP4 ≡ TCP; TP0 y el servicio de datagramas ≡ UDP |
| Red | 3 | **Internet** | Correspondencia buena, con un matiz: la capa de red de OSI admite **circuitos virtuales**; la de internet, **solo datagramas** |
| Enlace de datos | 2 | **Acceso a la red** | Las dos capas inferiores de OSI se **funden** en una sola, que el modelo no especifica |
| Física | 1 | **Acceso a la red** | Igual |

> **Dato clave.** Las dos fusiones que hay que saber decir en una frase: **arriba, OSI 5+6+7 = aplicación de TCP/IP**; **abajo, OSI 1+2 = acceso a la red de TCP/IP**. Las **capas 3 y 4 se corresponden una a una**. Y la equivalencia de protocolos: **CLNP ≡ IP**, **TP4 ≡ TCP**, **X.400 ≡ SMTP**, **X.500 ≡ LDAP**, **FTAM ≡ FTP**, **VT ≡ Telnet**.

Ver **diagrama D8**, con la correspondencia y los protocolos de cada nivel.

**Dónde se colocan los protocolos que no encajan.** Es fácil equivocarse:

- **ARP** se sitúa **entre las capas 2 y 3**: usa direcciones de capa 3 pero viaja **directamente en la trama**, con su propio EtherType, sin cabecera IP. La doctrina lo asigna unas veces a la capa 2 y otras a la 3; lo prudente es describirlo como **protocolo auxiliar de la capa de internet que opera sobre la capa de enlace**.
- **ICMP** viaja **encapsulado en IP** (protocolo 1), lo que técnicamente lo pondría por encima de IP, pero su función es **de control de la propia capa de red**, así que se considera de **capa 3**.
- **TLS** se sitúa **entre transporte y aplicación**: por eso se le llama informalmente «capa 6,5». En el modelo de cuatro niveles pertenece a la **capa de aplicación**.
- **MPLS** opera **entre las capas 2 y 3** (de ahí el apodo «capa 2,5»).
- **QUIC** funciona **sobre UDP** pero presta servicios de transporte: es un caso claro de **violación deliberada** de la estratificación por razones de despliegue —era imposible introducir un protocolo de transporte nuevo que atravesara los cortafuegos y los traductores de direcciones existentes—.

#### 4.2. Análisis comparativo: diferencias de diseño y adopción

**Las diferencias de fondo**:

| Criterio | Modelo OSI | Modelo TCP/IP |
|----|----|----|
| **Origen** | Comité internacional (ISO/UIT-T), por consenso institucional | Comunidad técnica (DARPA e IETF), por implantación |
| **Orden de aparición** | **El modelo se diseñó antes que los protocolos** | **Los protocolos existían antes que el modelo**, que los describe *a posteriori* |
| **Número de capas** | 7 | 4 (o 5 en el modelo híbrido didáctico) |
| **Separación servicio / interfaz / protocolo** | **Explícita y rigurosa** | **Difusa**: el modelo no distingue con claridad los tres conceptos |
| **Modos en la capa de red** | Orientado a conexión **y** no orientado a conexión | **Solo** no orientado a conexión (datagramas) |
| **Modos en la capa de transporte** | Solo orientado a conexión en el servicio básico | **Ambos**: TCP orientado a conexión y UDP de datagramas |
| **Neutralidad** | **General**: vale para describir cualquier arquitectura | **Sesgado**: describe bien su propia pila y mal las demás |
| **Complejidad** | Alta; capas 5 y 6 poco utilizadas en la práctica | Baja; pragmática |
| **Adopción real** | El **modelo**, universal como lenguaje; los **protocolos**, marginales | **Total**: es la arquitectura de internet |

> **Dato clave.** La diferencia principal es la de **orden**: en OSI **primero el modelo y después los protocolos**, lo que produjo un modelo neutral pero unos protocolos que llegaron tarde; en TCP/IP **primero los protocolos y después el modelo**, lo que produjo protocolos probados pero un modelo poco general. La segunda es la de **modos**: **OSI admite los dos modos en la capa de red y TCP/IP solo datagramas**; y a la inversa, **TCP/IP admite los dos modos en transporte** mientras que el servicio básico de OSI se pensó orientado a conexión.

**Por qué fracasaron los protocolos OSI.** Tanenbaum lo resume en cuatro causas que conviene poder enunciar \[TANENBAUM\]:

1.  **Mala sincronización** (*bad timing*). Cuando las normas OSI estuvieron listas, TCP/IP ya estaba desplegado en las universidades y era gratuito. Llegar tarde a una batalla de estándares es fatal.
2.  **Mala tecnología**. Siete capas, dos de ellas (sesión y presentación) casi vacías en la práctica y dos (enlace y red) sobrecargadas; especificaciones enormes y de lectura difícil; funciones como el control de errores repetidas en varias capas.
3.  **Malas implantaciones**. Las primeras versiones eran grandes, lentas y difíciles de instalar, frente a una implantación de TCP/IP que venía **incluida y gratis en el Unix de Berkeley**.
4.  **Mala política**. OSI se percibió como un producto de burócratas europeos y de operadores de telecomunicación, frente a una comunidad académica abierta.

**Por qué se impuso TCP/IP.** Las razones simétricas: **estaba disponible antes**, era **gratuito y con código abierto**, funcionaba sobre cualquier red, se **especificaba en documentos cortos y legibles** que cualquiera podía leer, evolucionaba por consenso e implantación, y sus decisiones de diseño —simplicidad en el núcleo, complejidad en los extremos— resultaron ser **exactamente las que permitían crecer**.

> **Dato clave.** También hay que saber la crítica **inversa**, la que se hace a TCP/IP: (1) **no distingue con claridad servicio, interfaz y protocolo**, lo que lo hace mal modelo descriptivo; (2) **no es general**: no sirve para describir arquitecturas distintas de la suya; (3) **no separa la capa física de la de enlace**, que son funciones muy distintas; y (4) el diseño original **descuidó la seguridad y la contabilidad**, que hubo que añadir después.

**El modelo híbrido de cinco capas.** La solución práctica que adopta casi toda la literatura docente y buena parte de los temarios: se usa el **vocabulario de OSI** —hablar de «capa 3» o «dispositivo de capa 2»— y la **estructura de TCP/IP** desdoblando la inferior, con lo que resultan cinco capas: física, enlace, red, transporte y aplicación \[TANENBAUM\]. **No es una norma**: es una convención didáctica útil.

> **Ejemplo de aplicación en el ayto.** La pertinencia práctica de la comparación se ve en cualquier pliego de contratación del IAM. Cuando el pliego exige «conmutadores de **nivel 2** con soporte de 802.1Q» o «cortafuegos de **capa 7** con inspección de aplicaciones», está usando **la numeración de OSI**; cuando exige «soporte de **doble pila IPv4/IPv6**» o «cumplimiento de la **RFC 8200**», está usando **la pila TCP/IP**. Los dos modelos conviven en la misma página: uno es el lenguaje y el otro, la tecnología.

------------------------------------------------------------------------

### 5. Pila de protocolos TCP/IP: capa de acceso a la red

#### 5.1. Funciones de la capa de acceso a la red

**La capa que el modelo no define.** Es la peculiaridad que hay que enunciar primero: la arquitectura TCP/IP **no especifica** esta capa. La RFC 1122 se limita a fijar **qué debe existir** para que IP pueda funcionar encima, y deja el cómo a cada tecnología de red \[RFC1122\]. Esa indefinición deliberada es lo que permite que IP circule hoy sobre tecnologías que no existían cuando se diseñó.

**Los dos requisitos que la arquitectura impone** a cualquier tecnología que quiera transportar IP:

1.  Un **método de encapsulamiento**: cómo se mete un datagrama IP dentro de la unidad de datos de esa red y cómo se indica que lo que va dentro es IP. En Ethernet, el campo **EtherType** con el valor `0x0800` para IPv4 y `0x86DD` para IPv6 \[IANA\].
2.  Un **método de resolución de direcciones**: cómo se averigua la dirección física del siguiente salto a partir de su dirección IP. En IPv4 sobre Ethernet, **ARP** \[RFC826\]; en IPv6, el **descubrimiento de vecinos** \[RFC4861\].

**Funciones que se realizan en esta capa** (equivalentes a las capas 1 y 2 de OSI):

- **Codificación y transmisión de señales** por el medio, y sincronización de bits.
- **Delimitación de tramas** y control de errores mediante **FCS**.
- **Direccionamiento físico** mediante MAC y filtrado por dirección.
- **Control de acceso al medio**, cuando es compartido.
- **Control de flujo** entre equipos adyacentes.

**Tecnologías que ocupan esta capa**: **Ethernet (IEEE 802.3)** en sus distintas velocidades, **Wi-Fi (IEEE 802.11)**, **PPP** y **PPPoE** en accesos de operador, **HDLC**, **Frame Relay** y **ATM** en redes de área extensa heredadas, **MPLS** como capa intermedia de conmutación por etiquetas, y las tecnologías de acceso de operador (fibra **GPON**, redes móviles).

> **Relación con otros temas.** El detalle de estas tecnologías corresponde a otros temas: **Tema 33** para los medios de transmisión y los equipos de conmutación de las redes de comunicaciones; **Tema 37** para la tipología de redes locales, los métodos de acceso al medio y los dispositivos de interconexión; **Tema 38** para TETRA. Aquí solo se describe **el papel de esta capa dentro de la arquitectura**.

**MTU: el parámetro que hay que saber.** La **unidad máxima de transferencia** (*Maximum Transmission Unit*) es el tamaño máximo de carga útil que admite una tecnología de enlace. Determina cuándo la capa de red tiene que fragmentar.

> **Dato clave.** **MTU de Ethernet = 1.500 octetos** de carga útil. Con ella: **MSS típico de TCP sobre IPv4 = 1.460** (1.500 − 20 de IP − 20 de TCP) y **sobre IPv6 = 1.440** (1.500 − 40 − 20). Las tramas gigantes (*jumbo frames*) llegan a **9.000** octetos. **IPv6 exige una MTU mínima de 1.280 octetos** en todo enlace que lo transporte \[RFC8200\]; en IPv4 el mínimo es **68**, y todo equipo debe poder reensamblar al menos **576** octetos.

#### 5.2. Direccionamiento físico MAC y transmisión de tramas

**La dirección MAC.** Es la dirección de la capa de acceso a la red. Datos memorizables:

- **Longitud: 48 bits** = 6 octetos, escritos en **hexadecimal** separados por dos puntos o guiones (`00:1B:44:11:3A:B7`). También se emplea el formato de tres grupos de cuatro dígitos (`001B.4411.3AB7`).
- Se denomina también **dirección física**, **dirección de hardware** o **dirección quemada** (*burned-in address*), porque viene grabada en el adaptador de red, aunque hoy puede modificarse por software.
- **Estructura**: los **24 bits más significativos** son el **OUI** (*Organizationally Unique Identifier*), asignado por el **IEEE** al fabricante; los **24 restantes** los asigna el fabricante a cada tarjeta. La combinación pretende ser **globalmente única**.
- Dos **bits de control** dentro del primer octeto: el bit **I/G** (individual o de grupo) distingue unidifusión de multidifusión, y el bit **U/L** (universal o local) indica si la dirección la administra el IEEE o es local.

> **Dato clave.** **`FF:FF:FF:FF:FF:FF` es la dirección de difusión** (*broadcast*): la trama la procesan todos los equipos del **dominio de difusión**, que coincide con la red local o con la VLAN. Las direcciones **multidifusión** tienen el bit menos significativo del primer octeto a 1; ejemplos: `01:00:5E:xx:xx:xx` para multidifusión IPv4 y `33:33:xx:xx:xx:xx` para multidifusión IPv6.

**Diferencias entre dirección MAC y dirección IP**, en cuadro resumen:

| Criterio | Dirección MAC | Dirección IP |
|----|----|----|
| Capa | Acceso a la red (OSI 2) | Internet (OSI 3) |
| Longitud | 48 bits | 32 bits (v4) / 128 bits (v6) |
| Notación | Hexadecimal | Decimal punteada / hexadecimal con dos puntos |
| Estructura | **Plana** (no jerárquica) | **Jerárquica** (red + equipo) |
| Quién la asigna | El **fabricante**, con OUI del IEEE | El **administrador de la red** o DHCP |
| Ámbito | **El enlace local** | **Global**, extremo a extremo |
| ¿Cambia en el camino? | **Sí, en cada salto** | **No** (salvo traducción de direcciones) |
| ¿Sirve para encaminar? | No: es plana, no agregable | **Sí**: la jerarquía permite agregar rutas |

> **Dato clave.** La razón por la que **no basta con la dirección MAC** y hace falta la IP es que la MAC es **plana**: no se puede agregar. Una tabla de encaminamiento mundial con una entrada por tarjeta de red sería inviable. La dirección IP es **jerárquica** y permite que un encaminador diga «todo lo que empiece por este prefijo, por aquí», que es lo que hace posible internet.

**La trama Ethernet II**, que es el formato con el que viaja prácticamente todo el tráfico IP de una red local (ver **diagrama D9**):

| Campo | Tamaño | Contenido |
|----|----|----|
| Preámbulo | 7 octetos | Patrón `10101010` de sincronización (capa 1, no cuenta como trama) |
| Delimitador de inicio (SFD) | 1 octeto | `10101011` |
| **MAC destino** | **6 octetos** | Dirección física del siguiente salto |
| **MAC origen** | **6 octetos** | Dirección física del emisor |
| **EtherType** | **2 octetos** | Protocolo encapsulado: `0x0800` IPv4, `0x0806` ARP, `0x86DD` IPv6, `0x8100` VLAN |
| **Datos** | **46 a 1.500 octetos** | Carga útil; se rellena si no llega a 46 |
| **FCS** | **4 octetos** | Suma de comprobación **CRC-32** |

> **Dato clave.** **Trama Ethernet: mínimo 64 octetos, máximo 1.518** (sin preámbulo ni delimitador; 1.522 con etiqueta VLAN de 4 octetos). La cabecera son **14 octetos** y la cola, **4**: **18 octetos de sobrecarga**. El mínimo de 64 no es caprichoso: procede del tiempo necesario para detectar una colisión en el Ethernet clásico de medio compartido.

Existe también el formato **IEEE 802.3 con LLC/SNAP**, en el que el campo de dos octetos se interpreta como **longitud** en lugar de como tipo, y el protocolo superior se indica en la cabecera LLC. La regla práctica para distinguirlos: **si el valor es mayor o igual que 1.536 (`0x0600`), es un EtherType; si es menor o igual que 1.500, es una longitud**.

> **Ejemplo de aplicación en el ayto.** En la red de una oficina de distrito, todos los puestos de una misma planta suelen estar en la misma **VLAN**, que es un **dominio de difusión** independiente. Cuando un puesto emite una petición ARP o un descubrimiento DHCP —ambos por difusión—, la trama llega a todos los puestos de esa VLAN **y a ninguno de otra**. Esa contención del tráfico de difusión es, además de una decisión de rendimiento, el fundamento técnico de la medida **`mp.com.4`** del ENS, cuyo refuerzo **R1** exige precisamente implantar los segmentos **mediante VLAN** y segregar como mínimo **usuarios, servicios y administración** \[ENS\]. Ver §9.2.

------------------------------------------------------------------------

### 6. Pila de protocolos TCP/IP: capa de red

#### 6.1. Protocolo de Internet versión 4 (IPv4)

**Naturaleza del protocolo.** IP presta un servicio **no orientado a conexión**, **no fiable** y de **mejor esfuerzo** \[RFC791\]. Esas tres palabras significan, con precisión:

- **No orientado a conexión**: no hay fase de establecimiento; cada datagrama se encamina de forma independiente y dos datagramas de la misma comunicación pueden seguir caminos distintos y llegar desordenados.
- **No fiable**: no hay acuses de recibo ni retransmisiones. Un datagrama puede perderse, duplicarse o llegar corrupto en su carga útil sin que IP haga nada.
- **Mejor esfuerzo**: la red **intenta** entregarlo y solo lo descarta cuando no tiene alternativa; no lo descarta arbitrariamente.

Sus **dos funciones** son **direccionar** y **encaminar**. A ellas se suman la **fragmentación y el reensamblado** y la limitación de la vida del datagrama mediante el **TTL**.

**La cabecera IPv4**, campo a campo (ver **diagrama D10**). Es materia de memorización:

| Campo | Bits | Función |
|----|----|----|
| **Versión** | 4 | Valor **4** |
| **IHL** (longitud de cabecera) | 4 | Longitud **en palabras de 32 bits**: mínimo **5** (= 20 octetos), máximo **15** (= 60) |
| **Tipo de servicio / DSCP + ECN** | 8 | Hoy: **6 bits de DSCP** para calidad de servicio y **2 de ECN** para notificación explícita de congestión \[RFC2474\] |
| **Longitud total** | 16 | Cabecera **más** datos, en octetos. Máximo teórico **65.535** |
| **Identificación** | 16 | Identifica el datagrama original, para reensamblar sus fragmentos |
| **Indicadores** (*flags*) | 3 | Bit 0 reservado; **DF** (*Don't Fragment*); **MF** (*More Fragments*) |
| **Desplazamiento del fragmento** | 13 | Posición del fragmento **en unidades de 8 octetos** |
| **TTL** (tiempo de vida) | 8 | Se **decrementa en uno en cada encaminador**; al llegar a 0 se descarta y se envía un ICMP de tiempo excedido |
| **Protocolo** | 8 | Protocolo encapsulado: **1** ICMP, **6** TCP, **17** UDP, **50** ESP, **51** AH, **89** OSPF |
| **Suma de comprobación de cabecera** | 16 | **Solo de la cabecera**, no de los datos. Se **recalcula en cada salto** porque cambia el TTL |
| **Dirección de origen** | 32 |  |
| **Dirección de destino** | 32 |  |
| **Opciones + relleno** | 0-320 | Poco usadas: registro de ruta, marca de tiempo, encaminamiento desde el origen |

> **Dato clave.** Tres datos clave de esta tabla: (1) la **cabecera IPv4 mide 20 octetos** sin opciones y hasta **60** con ellas; (2) la **suma de comprobación protege únicamente la cabecera**, no los datos —de la carga útil se ocupa el transporte—; y (3) el **TTL no es tiempo, es un contador de saltos**, pese a su nombre.

**Direccionamiento IPv4.** Una dirección son **32 bits**, escritos en **notación decimal punteada** en cuatro octetos (`192.168.1.10`). Toda dirección se divide en **parte de red** y **parte de equipo**, y la frontera la marca la **máscara de subred**.

**Del direccionamiento por clases a CIDR.** Originalmente, la frontera venía dada por los primeros bits de la dirección:

| Clase | Primeros bits | Rango del primer octeto | Máscara por defecto | Redes / equipos |
|----|----|----|----|----|
| **A** | `0` | 1-126 | `255.0.0.0` (**/8**) | 126 redes de 16.777.214 equipos |
| **B** | `10` | 128-191 | `255.255.0.0` (**/16**) | 16.384 redes de 65.534 equipos |
| **C** | `110` | 192-223 | `255.255.255.0` (**/24**) | 2.097.152 redes de 254 equipos |
| **D** | `1110` | 224-239 | — | **Multidifusión** |
| **E** | `1111` | 240-255 | — | **Reservada** / experimental |

Ese esquema derrochaba direcciones —una organización con 300 equipos necesitaba una clase B de 65.534— y en **1993** se sustituyó por el **encaminamiento entre dominios sin clases**, **CIDR** \[RFC950\]. Con CIDR, la máscara se indica con la **notación de prefijo `/n`**, donde *n* es el número de bits de red, y puede tomar **cualquier valor**, no solo 8, 16 o 24. CIDR trajo además la **agregación de rutas** (*supernetting*): un proveedor anuncia un solo prefijo en lugar de cientos.

> **Dato clave.** Direcciones reservadas de memorización obligatoria: **`10.0.0.0/8`, `172.16.0.0/12` y `192.168.0.0/16`** son **privadas** \[RFC1918\]; **`127.0.0.0/8`** es el **bucle local**; **`169.254.0.0/16`** es de **enlace local** (**APIPA**, la que se autoasigna un equipo cuando no encuentra servidor DHCP); **`224.0.0.0/4`** es **multidifusión**; **`0.0.0.0/8`** designa «esta red» y **`0.0.0.0/0`** es la **ruta por defecto**; **`100.64.0.0/10`** se reserva para el NAT de operador. En toda subred, la **primera dirección es la de red** y la **última, la de difusión**: ninguna de las dos se asigna a un equipo.

**Cálculo de subredes.** Las fórmulas, que hay que saber aplicar:

- Número de **direcciones** de una subred `/n`: **2^(32−n)**.
- Número de **equipos direccionables**: **2^(32−n) − 2** (se restan la de red y la de difusión). Excepción: en enlaces punto a punto se usan `/31` sin restar \[RFC950\].
- Número de **subredes** obtenidas al tomar prestados *k* bits: **2^k**.

> **Ejercicio resuelto.** **Dividir la red de un distrito.** Al distrito se le asigna el bloque **`10.20.8.0/22`** y hay que dividirlo en cuatro subredes de igual tamaño: puestos de usuario, telefonía IP, impresión y cámaras. ¿Qué prefijo resulta, cuántos equipos caben en cada una y cuáles son sus rangos? 1. **Bits que hay que tomar prestados**: se necesitan 4 subredes y **2² = 4**, luego se toman **2 bits**. El prefijo pasa de `/22` a **`/24`**. 2. **Direcciones por subred**: 2^(32−24) = **256**. **Equipos direccionables**: 256 − 2 = **254**. 3. **Tamaño del bloque original**: 2^(32−22) = **1.024** direcciones, de `10.20.8.0` a `10.20.11.255`. Cuadra: 4 × 256 = 1.024. 4. **Rangos resultantes**:
>
> | Subred | Prefijo | Dirección de red | Primer equipo | Último equipo | Difusión |
> |----|----|----|----|----|----|
> | Puestos | `10.20.8.0/24` | `10.20.8.0` | `10.20.8.1` | `10.20.8.254` | `10.20.8.255` |
> | Telefonía | `10.20.9.0/24` | `10.20.9.0` | `10.20.9.1` | `10.20.9.254` | `10.20.9.255` |
> | Impresión | `10.20.10.0/24` | `10.20.10.0` | `10.20.10.1` | `10.20.10.254` | `10.20.10.255` |
> | Cámaras | `10.20.11.0/24` | `10.20.11.0` | `10.20.11.1` | `10.20.11.254` | `10.20.11.255` |
>
> 5\. **Comprobación de pertenencia**: ¿está `10.20.9.200` en la subred de telefonía? La máscara `/24` es `255.255.255.0`; la operación **Y lógica** entre la dirección y la máscara da `10.20.9.0`, que es la dirección de red de telefonía. **Sí**. 6. **Refinamiento realista**: si las subredes no necesitan el mismo tamaño —64 cámaras y 500 puestos—, se aplica **máscara de longitud variable (VLSM)**: `/23` para puestos, `/25` para telefonía, `/26` para impresión y `/26` para cámaras, sumando también 1.024 direcciones. VLSM es la técnica que CIDR hace posible y es la que se usa en la práctica.

Ver **diagrama D11**.

**Traducción de direcciones (NAT).** Ante el agotamiento de IPv4 se generalizó la **traducción de direcciones de red** \[RFC3022\]: un encaminador sustituye la dirección privada de origen por su dirección pública y anota la correspondencia en una tabla. En su variante habitual, **NAPT** o **PAT** (*NAT overload*), traduce también el **puerto de origen**, lo que permite que **miles de equipos privados compartan una sola dirección pública**.

Sus consecuencias, como ventajas e inconvenientes:

- **A favor**: ahorra direcciones públicas, oculta la estructura interna y actúa como filtro implícito de conexiones entrantes.
- **En contra**: **rompe el principio extremo a extremo**; impide las conexiones entrantes no solicitadas; complica los protocolos que llevan direcciones dentro de la carga útil (FTP en modo activo, SIP); **dificulta la trazabilidad** y la atribución de responsabilidad, porque muchos usuarios comparten una IP; y obliga a mantener **estado** en un punto de la red.

> **Dato clave.** **NAT no es un mecanismo de seguridad**, aunque se comporte como un filtro. Es un mecanismo de **ahorro de direcciones** cuyo efecto colateral es bloquear conexiones entrantes. Confundir NAT con cortafuegos es un error clásico. Y el matiz normativo: al enmascarar el origen, **NAT compromete la trazabilidad**, que es una de las cinco dimensiones de seguridad del ENS.

#### 6.2. Protocolo de Internet versión 6 (IPv6)

**Por qué existe.** La causa principal es el **agotamiento del espacio de direcciones de IPv4**: 32 bits dan **2³² ≈ 4.294.967.296** direcciones, de las que una parte importante está reservada. IANA agotó su reserva libre en **2011** y los registros regionales fueron agotando la suya después; **RIPE NCC**, el registro europeo, agotó su reserva general en **noviembre de 2019** y desde entonces solo asigna bloques `/24` procedentes de recuperaciones \[RIPE\]. Pero el agotamiento no fue la única razón: también se buscaba **simplificar la cabecera** para acelerar el reenvío, **eliminar la fragmentación en tránsito**, **suprimir la necesidad de NAT** y **facilitar la autoconfiguración**.

**Las cifras.** IPv6 usa **128 bits**, lo que da **2¹²⁸ ≈ 3,4 × 10³⁸** direcciones \[RFC8200\].

**Notación** \[RFC4291\]. Ocho grupos de **16 bits** en hexadecimal separados por dos puntos: `2001:0db8:0000:0000:0000:ff00:0042:8329`. Reglas de abreviatura:

1.  Se **suprimen los ceros a la izquierda** de cada grupo: `2001:db8:0:0:0:ff00:42:8329`.
2.  Se sustituye **una sola** secuencia de grupos nulos consecutivos por **`::`**: `2001:db8::ff00:42:8329`. **El doble dos puntos puede usarse una única vez** en la dirección, porque si no sería ambiguo.
3.  Se escriben en **minúsculas**, y en una URL la dirección va **entre corchetes**: `https://[2001:db8::1]:443/`.

**Tipos de dirección** \[RFC4291\]. IPv6 **elimina la difusión** (*broadcast*) y la sustituye por multidifusión a grupos bien definidos:

| Tipo | Prefijo | Descripción |
|----|----|----|
| **Unidifusión global** | `2000::/3` | Encaminable en internet; equivale a la dirección pública de IPv4 |
| **Enlace local** | `fe80::/10` | Ámbito **del enlace**; se autoconfigura siempre y es imprescindible para el descubrimiento de vecinos |
| **Local única (ULA)** | `fc00::/7`, en la práctica `fd00::/8` | Ámbito interno de la organización; papel análogo al de las direcciones privadas de IPv4 |
| **Multidifusión** | `ff00::/8` | Grupos. `ff02::1` todos los nodos del enlace; `ff02::2` todos los encaminadores del enlace |
| **Anidifusión** (*anycast*) | (del espacio de unidifusión) | La misma dirección en varios nodos; se entrega **al más próximo** según el encaminamiento |
| **Bucle local** | `::1/128` | Equivale a `127.0.0.1` |
| **No especificada** | `::/128` | Origen provisional mientras no hay dirección |
| **Documentación** | `2001:db8::/32` | Reservada para ejemplos y manuales |

> **Dato clave.** **IPv6 no tiene difusión.** Lo que en IPv4 se hacía por difusión, en IPv6 se hace por **multidifusión** a un grupo concreto: `ff02::1` (todos los nodos) o `ff02::2` (todos los encaminadores). Segundo dato: **todo interfaz IPv6 tiene siempre una dirección de enlace local `fe80::`**, además de las que pueda tener; no es opcional.

**Estructura de la dirección global.** Se divide en **prefijo de encaminamiento global** (habitualmente `/48` para una organización), **identificador de subred** (16 bits, que dan 65.536 subredes) e **identificador de interfaz** de **64 bits**. De ahí la regla práctica: **en IPv6, una subred de usuarios es un `/64`**, con independencia de cuántos equipos tenga. El identificador de interfaz puede derivarse de la MAC mediante **EUI-64** —se inserta `FF:FE` en el medio y se invierte el bit U/L— o generarse de forma aleatoria y temporal mediante **extensiones de privacidad**, que es lo habitual hoy para evitar el seguimiento del usuario.

**La cabecera IPv6** (ver **diagrama D12**). Es **fija de 40 octetos** y tiene solo **ocho campos**, frente a los catorce de IPv4:

| Campo | Bits | Función |
|----|----|----|
| **Versión** | 4 | Valor **6** |
| **Clase de tráfico** | 8 | Equivale al DSCP + ECN de IPv4 |
| **Etiqueta de flujo** | 20 | Identifica un flujo para darle un tratamiento homogéneo |
| **Longitud de la carga útil** | 16 | **Solo los datos**, sin contar los 40 octetos de cabecera |
| **Siguiente cabecera** | 8 | Protocolo encapsulado **o** primera cabecera de extensión |
| **Límite de saltos** | 8 | Equivalente al TTL, con nombre honesto |
| **Dirección de origen** | 128 |  |
| **Dirección de destino** | 128 |  |

**Qué desapareció de la cabecera y por qué**:

- **La suma de comprobación de cabecera**: se eliminó porque la capa 2 (FCS) y la capa 4 (suma de comprobación obligatoria en TCP y en UDP sobre IPv6) ya la hacen. Evitar recalcularla en cada salto **acelera el reenvío**.
- **Los campos de fragmentación** (identificación, indicadores, desplazamiento): **los encaminadores no fragmentan en IPv6**. Si un paquete no cabe, el encaminador lo **descarta** y devuelve un ICMPv6 de **«paquete demasiado grande»**; es el origen quien ajusta el tamaño mediante **descubrimiento de la MTU del camino**. Si el origen necesita fragmentar, usa una **cabecera de extensión de fragmentación**.
- **IHL y las opciones**: la cabecera es fija; lo opcional se traslada a **cabeceras de extensión** encadenadas mediante el campo «siguiente cabecera».

Cabeceras de extensión definidas: **salto a salto** (la única que examinan todos los encaminadores), **encaminamiento**, **fragmentación**, **AH**, **ESP**, **opciones de destino**. Su orden recomendado está fijado en la especificación \[RFC8200\].

> **Dato clave.** Comparativa que hay que saber recitar: **IPv4 = 32 bits, cabecera variable de 20 a 60 octetos, 14 campos, con suma de comprobación, fragmenta en los encaminadores, difusión sí. IPv6 = 128 bits, cabecera fija de 40 octetos, 8 campos, sin suma de comprobación, no fragmenta en tránsito, difusión no.** Y el dato contraintuitivo: la cabecera de IPv6 es **más grande** (40 frente a 20) pero **más simple** y de **tamaño fijo**, que es lo que importa para el rendimiento del reenvío.

**Otras mejoras.** **Autoconfiguración sin estado (SLAAC)** \[RFC4861\], que permite a un equipo obtener dirección sin servidor DHCP a partir de los anuncios de encaminador; soporte **nativo** de **IPsec**, previsto desde el diseño —aunque su uso pasó de obligatorio a recomendado—; mejor soporte de multidifusión y de movilidad; y jerarquía de direccionamiento pensada para la **agregación de rutas**, que reduce el tamaño de las tablas.

**Mecanismos de transición** (ver **diagrama D13**). Ni IPv4 ni IPv6 son compatibles entre sí: un equipo solo IPv4 **no puede** hablar con uno solo IPv6. De ahí tres familias de mecanismos \[RFC4213\]:

1.  **Doble pila** (*dual stack*). El equipo ejecuta **las dos pilas simultáneamente** y elige según el destino. Es el **mecanismo recomendado** y el que exige la normativa cuando se planifica la migración. Su inconveniente es que **no ahorra direcciones IPv4**: hay que seguir teniéndolas.
2.  **Túneles**. Se encapsula IPv6 dentro de IPv4 (**número de protocolo 41**) para atravesar una red que solo entiende IPv4. Variantes: túneles configurados manualmente, **6to4**, **6rd**, **Teredo** (sobre UDP, para atravesar NAT) y **ISATAP**. Son mecanismos de transición, y varios de ellos están hoy desaconsejados por motivos de seguridad y de rendimiento.
3.  **Traducción**. Se convierte un protocolo en otro: **NAT64** combinado con **DNS64** permite que un cliente solo IPv6 alcance un servidor solo IPv4 \[RFC4213\]. Es el mecanismo de las redes móviles modernas.

> **Dato clave.** **La estrategia recomendada es la doble pila**; los túneles son un paliativo y la traducción, el recurso cuando ya no se dispone de IPv4. Nota adicional: **la doble pila duplica la superficie de exposición** —hay que aplicar las mismas reglas de filtrado a las dos pilas—, y un fallo típico de seguridad consiste en tener el cortafuegos afinado para IPv4 y abierto para IPv6.

**Estado de la adopción.** En **abril de 2026** la medición de Google alcanzó por primera vez el **50 %** de usuarios accediendo por IPv6, mientras APNIC Labs situaba la capacidad IPv6 global en torno al **42 %** \[APNIC-STATS\]. **Es un dato volátil**: debe reverificarse antes de cada convocatoria y no conviene memorizar la cifra exacta, sino el orden de magnitud y el hecho de que **la coexistencia con IPv4 se prolongará durante años**.

#### 6.3. Protocolos de control y resolución de direcciones (ICMP, ARP y ND)

Los tres protocolos auxiliares sin los cuales la capa de red no funcionaría (ver **diagrama D14**).

**ICMP** (*Internet Control Message Protocol*) \[RFC792\]. Es el protocolo de **notificación de errores y de diagnóstico** de la capa de red. Datos:

- **Número de protocolo IP: 1** (ICMPv6: **58**).
- Viaja **encapsulado en IP**, pero se considera parte de la capa de red.
- **No corrige nada**: solo informa. Un mensaje ICMP de destino inaccesible avisa al origen; no reenvía el paquete perdido.
- Un mensaje ICMP de error transporta la **cabecera IP del paquete que lo provocó más los primeros octetos de su carga**, para que el origen pueda identificar de qué conexión se trata.
- **No se generan mensajes ICMP de error en respuesta a otro mensaje ICMP de error**, ni ante paquetes de difusión o multidifusión: evita tormentas.

Mensajes de memorización obligatoria:

| Tipo | Nombre | Uso |
|----|----|----|
| **0** | Respuesta de eco (*echo reply*) | Respuesta de `ping` |
| **3** | **Destino inaccesible** | Con códigos: 0 red, 1 equipo, 3 **puerto**, 4 **fragmentación necesaria y DF activo** |
| **5** | Redirección | Un encaminador informa de una ruta mejor |
| **8** | Solicitud de eco (*echo request*) | Petición de `ping` |
| **11** | **Tiempo excedido** | TTL agotado; es el que hace funcionar `traceroute` |
| **12** | Problema de parámetro | Cabecera mal formada |

> **Dato clave.** **`ping` usa ICMP tipos 8 y 0**; **`traceroute` se apoya en el tipo 11** (tiempo excedido) enviando paquetes con TTL creciente —en su variante de Unix con datagramas UDP a puertos altos, y en la de Windows (`tracert`) con solicitudes de eco ICMP—. Y un matiz importante: **bloquear todo ICMP en un cortafuegos es una mala práctica**, porque el tipo 3 código 4 es imprescindible para el descubrimiento de la MTU del camino, y sin él aparecen conexiones que se establecen pero se quedan colgadas al transferir datos.

**ARP** (*Address Resolution Protocol*) \[RFC826\]. Resuelve el problema de traducir una **dirección IPv4** en la **dirección MAC** del equipo que la tiene, dentro del **mismo enlace**. Funcionamiento:

1.  El equipo consulta su **caché ARP**. Si la entrada está, termina.
2.  Si no, emite una **petición ARP por difusión** (`FF:FF:FF:FF:FF:FF`): «¿quién tiene la IP `10.20.8.7`? Dígaselo a `10.20.8.45`».
3.  **Solo el propietario** de esa IP responde, con una **respuesta ARP por unidifusión** que contiene su MAC.
4.  Ambos actualizan su caché, con un tiempo de expiración de unos minutos.

Variantes: **ARP gratuito** (*gratuitous ARP*), que un equipo emite al arrancar o al cambiar de dirección, y que sirve para detectar direcciones duplicadas y para actualizar las cachés ajenas; **proxy ARP**, en el que un encaminador responde por otros; y **RARP**, hoy en desuso, sustituido por DHCP.

> **Dato clave.** **ARP es solo de IPv4 y solo dentro del enlace local.** No existe ARP en IPv6: su función la cumple el **descubrimiento de vecinos**. Y el ataque asociado: la **suplantación de ARP** (*ARP spoofing* o envenenamiento de caché) consiste en responder falsamente a una petición para colocarse **en medio** de la comunicación; se combate con **inspección ARP dinámica** en el conmutador y con **802.1X** \[MITRE\].

**Descubrimiento de vecinos (ND)** \[RFC4861\]. En IPv6 sustituye y amplía a ARP, a ICMP de redirección y al descubrimiento de encaminadores. Viaja sobre **ICMPv6** y usa **multidifusión**, no difusión, lo que reduce el ruido en la red. Sus **cinco mensajes**:

| Mensaje | Sigla | Función |
|----|----|----|
| **Solicitud de encaminador** | RS | El equipo pregunta si hay encaminadores en el enlace |
| **Anuncio de encaminador** | RA | El encaminador anuncia su presencia, el **prefijo de red** y los parámetros de configuración |
| **Solicitud de vecino** | NS | Equivale a la petición ARP: pregunta por la MAC de una IPv6 |
| **Anuncio de vecino** | NA | Equivale a la respuesta ARP |
| **Redirección** | — | Informa de un siguiente salto mejor |

Funciones adicionales de ND: **detección de direcciones duplicadas (DAD)**, que un equipo ejecuta antes de usar cualquier dirección; **detección de inaccesibilidad de vecinos (NUD)**; y **autoconfiguración sin estado (SLAAC)**, en la que el equipo construye su dirección combinando el **prefijo anunciado por el encaminador** con su **identificador de interfaz**.

> **Dato clave.** Correspondencias IPv4 → IPv6 que hay que saber: **ARP → solicitud/anuncio de vecino (NS/NA)**; **ICMP → ICMPv6**; **difusión → multidifusión**; **DHCP obligatorio → SLAAC opcional o DHCPv6**; **fragmentación en encaminadores → descubrimiento de MTU del camino**.

#### 6.4. Principios de enrutamiento IP

**Encaminamiento y reenvío, otra vez.** Ya se distinguieron en §2.3.1 y es la base del epígrafe: el **encaminamiento** construye la tabla; el **reenvío** la consulta paquete a paquete.

**El algoritmo de decisión de un equipo terminal.** Cuando un equipo tiene que enviar un paquete, hace **una sola comprobación** (ver **diagrama D15**):

1.  Aplica la operación **Y lógica** entre la dirección de destino y **su propia máscara**.
2.  Si el resultado coincide con **su dirección de red**, el destino está **en su misma subred**: resuelve su MAC por ARP o ND y **le envía la trama directamente**.
3.  Si **no** coincide, el destino está **fuera**: envía la trama a la **MAC de su puerta de enlace predeterminada**, dejando **intacta la dirección IP de destino**.

> **Dato clave.** El punto 3 concentra la idea central de toda la capa de red: **la trama va dirigida al encaminador, pero el paquete va dirigido al destino final**. MAC del siguiente salto, IP del destino. Es la respuesta a la pregunta «¿por qué el paquete lleva dos direcciones de destino distintas?».

**La tabla de encaminamiento.** Cada entrada contiene, como mínimo: **red de destino y máscara**, **siguiente salto** (*next hop*), **interfaz de salida** y **métrica**. Además, en tablas con varias fuentes de rutas, una **distancia administrativa** que decide qué fuente prevalece.

**La regla de decisión: prefijo más largo.** Cuando varias entradas encajan con la dirección de destino, **gana la de prefijo más específico**, es decir, la de máscara más larga \[RFC1812\]. La **ruta por defecto** (`0.0.0.0/0` en IPv4, `::/0` en IPv6) es la de prefijo **más corto** y por eso es la última en aplicarse: es la red de seguridad.

**Clasificación de las rutas por su origen:**

- **Directamente conectadas**: las de las redes a las que el equipo tiene interfaz.
- **Estáticas**: configuradas a mano. Predecibles, sin consumo de recursos y sin adaptación a los fallos. Adecuadas para redes pequeñas o estables y para la ruta por defecto.
- **Dinámicas**: aprendidas mediante un **protocolo de encaminamiento**. Se adaptan solos a los cambios de topología, a cambio de consumir CPU, memoria y ancho de banda, y de exigir configuración de seguridad.

**Protocolos de encaminamiento.** Dos clasificaciones cruzadas:

**Por su ámbito:**

- **Interiores (IGP)**: dentro de un mismo **sistema autónomo**. **RIP**, **OSPF**, **IS-IS**, **EIGRP**.
- **Exteriores (EGP)**: entre sistemas autónomos. **BGP-4** es el único en uso; es el protocolo que **sostiene el encaminamiento global de internet** \[RFC4271\].

**Por su algoritmo:**

- **Vector distancia**: cada encaminador informa a sus vecinos de **las distancias que conoce**; nadie tiene el mapa completo. Sencillo, pero de **convergencia lenta** y expuesto al problema de la **cuenta a infinito**, que se mitiga con horizonte dividido, envenenamiento de ruta y temporizadores. Ejemplo: **RIP**, que usa como métrica el **número de saltos** con un máximo de **15** (16 = inalcanzable).
- **Estado del enlace**: cada encaminador **inunda** la red con el estado de sus enlaces, todos construyen **el mismo mapa completo** y cada uno calcula el camino más corto con el **algoritmo de Dijkstra**. Convergencia rápida y sin bucles, a cambio de más CPU y memoria. Ejemplos: **OSPF** —con su división en **áreas** y el **área 0** como troncal— e **IS-IS**.
- **Vector de camino**: variante de vector distancia en la que se anuncia **el camino completo** de sistemas autónomos, lo que permite detectar bucles. Es el algoritmo de **BGP**.

> **Dato clave.** Datos concretos: **RIP** es vector distancia, métrica de **saltos**, máximo **15**, sobre **UDP/520**. **OSPF** es estado del enlace, métrica de **coste** basada en el ancho de banda, **número de protocolo IP 89**, organizado en **áreas** con **área 0** troncal. **BGP-4** es vector de camino, sobre **TCP/179**, y es el **protocolo exterior** de internet. Y la distinción de vocabulario: un **sistema autónomo (AS)** es un conjunto de redes bajo una misma política de encaminamiento, identificado por un número que asigna el registro regional.

> **Ejemplo de aplicación en el ayto.** En la red municipal conviven las tres clases de ruta. Los puestos de la oficina de distrito tienen una **ruta por defecto** hacia el encaminador de la sede, y nada más: no necesitan saber nada del resto. El encaminador del distrito aprende por un **protocolo interior** las rutas hacia el CPD del IAM y hacia las demás dependencias. Y la conexión con **internet** y con la **red SARA** se resuelve con **rutas específicas** hacia los prefijos de cada una: el tráfico dirigido a otra Administración **no debe salir a internet**, sino entrar por SARA, y eso se implanta precisamente con una ruta de prefijo más específico que la ruta por defecto. Ver §9.2.

------------------------------------------------------------------------

### 7. Pila de protocolos TCP/IP: capa de transporte

#### 7.1. Concepto de puerto y multiplexación de aplicaciones

**El problema que resuelve la capa de transporte.** La dirección IP identifica **una máquina**, no un programa. En un servidor del IAM pueden estar ejecutándose a la vez el servidor web de la sede, el servidor de correo, el de bases de datos y el de administración remota. Cuando llega un paquete a esa dirección IP, alguien tiene que decidir a cuál de ellos se entrega. Ese alguien es la capa de transporte, y el dato que usa es el **puerto**.

**Definición.** Un **puerto** es un identificador numérico de **16 bits** que designa un extremo de comunicación dentro de un equipo. Su rango es, por tanto, de **0 a 65.535**. En la terminología de OSI es el **punto de acceso al servicio de transporte**.

- **Multiplexación**: en el origen, recoger los datos de varios procesos y enviarlos por una única dirección IP, etiquetando cada uno con su puerto.
- **Demultiplexación**: en el destino, repartir lo recibido entre los procesos según el puerto de destino.

**Los tres rangos de IANA**, de memorización obligatoria \[IANA\]:

| Rango | Nombre | Uso |
|----|----|----|
| **0 - 1023** | **Bien conocidos** (*well-known*) | Servicios estándar. En sistemas tipo Unix, **solo un proceso privilegiado puede abrirlos** |
| **1024 - 49151** | **Registrados** | Asignados por IANA a aplicaciones concretas a petición del fabricante |
| **49152 - 65535** | **Dinámicos, privados o efímeros** | Los que el sistema operativo asigna al **cliente** al iniciar una conexión |

> **Dato clave.** La regla clave: **el servidor escucha en un puerto conocido y fijo; el cliente usa un puerto efímero distinto en cada conexión**. Por eso un servidor web atiende a diez mil clientes en el **puerto 443**: cada conexión se identifica por la **quíntupla** completa (protocolo, IP y puerto de origen, IP y puerto de destino), y lo que varía es el extremo del cliente.

**Socket.** El par **(dirección IP, número de puerto)** identifica un extremo. En la programación de red, el *socket* es además la abstracción del sistema operativo —la interfaz de sockets de Berkeley— con la que un programa accede al servicio de transporte: es, literalmente, el **punto de acceso al servicio** de OSI hecho llamada al sistema.

> **Dato clave.** **Los espacios de puertos de TCP y de UDP son independientes.** El puerto TCP 53 y el puerto UDP 53 son dos cosas distintas, y de hecho DNS usa los dos con propósitos diferentes \[RFC1035P\]. Por eso, un servicio TCP en el puerto 80 no impide usar el puerto 80 UDP.

**Los servicios que puede prestar la capa de transporte**, y que distinguen a sus dos protocolos:

1.  **Multiplexación y demultiplexación** por puerto. La presta **siempre**, es la función mínima.
2.  **Detección de errores** en los datos, mediante suma de comprobación sobre la carga útil.
3.  **Transferencia fiable**: acuse de recibo, retransmisión y eliminación de duplicados.
4.  **Entrega ordenada**.
5.  **Control de flujo**: proteger al **receptor**.
6.  **Control de congestión**: proteger a **la red**.

**UDP presta solo las dos primeras. TCP presta las seis.** Esa frase es la síntesis del apartado.

> **Dato clave.** No confundir **control de flujo** con **control de congestión**: el primero evita que el **emisor desborde al receptor** y se implanta con la **ventana anunciada** por el receptor; el segundo evita que el conjunto de emisores **desborde a la red** y se implanta con la **ventana de congestión** que calcula el emisor. TCP usa como ventana efectiva **el mínimo de las dos**.

#### 7.2. Transmission Control Protocol (TCP)

**Caracterización.** TCP presta un servicio **orientado a conexión**, **fiable**, de **flujo de octetos** (*byte stream*), **dúplex** y **punto a punto** \[RFC9293\]. Cada adjetivo tiene consecuencias:

- **Orientado a conexión**: hay establecimiento, transferencia y cierre, y ambos extremos mantienen **estado**.
- **Fiable**: garantiza que los datos llegan **completos, sin duplicados y en orden**, o que la conexión se rompe informando de ello.
- **Flujo de octetos**: TCP **no conserva los límites de mensaje**. Si la aplicación hace tres escrituras de 100 octetos, el receptor puede leer 300 de una vez o 150 y 150. La aplicación debe delimitar sus propios mensajes. Es una diferencia crucial con UDP.
- **Dúplex**: los datos fluyen simultáneamente en ambos sentidos por la misma conexión.
- **Punto a punto**: exactamente dos extremos. **TCP no admite multidifusión ni difusión.**

> **Dato clave.** Dos afirmaciones clave: **TCP no conserva los límites de mensaje** (es un flujo, no una secuencia de mensajes) y **TCP no puede usarse para multidifusión** (es punto a punto por definición). La segunda explica por qué el vídeo multidifusión o la telefonía IP usan **UDP**.

**La cabecera TCP** (ver **diagrama D16**). **Mínimo 20 octetos**, hasta **60** con opciones:

| Campo | Bits | Función |
|----|----|----|
| **Puerto de origen** | 16 |  |
| **Puerto de destino** | 16 |  |
| **Número de secuencia** | 32 | Posición del **primer octeto** de este segmento dentro del flujo |
| **Número de acuse de recibo** | 32 | **Siguiente** octeto que se espera recibir; válido si el indicador ACK está activo |
| **Desplazamiento de datos** | 4 | Longitud de la cabecera en palabras de 32 bits |
| **Reservado** | 4 |  |
| **Indicadores** (*flags*) | 8 | **CWR, ECE, URG, ACK, PSH, RST, SYN, FIN** |
| **Ventana** | 16 | Espacio **disponible en el buffer del receptor**: es el control de flujo |
| **Suma de comprobación** | 16 | **Obligatoria**; cubre cabecera, datos y una **pseudocabecera** con las IP |
| **Puntero de urgencia** | 16 | Válido si URG está activo |
| **Opciones + relleno** | 0-320 | **MSS**, escalado de ventana, **SACK**, marcas de tiempo \[RFC5681\] |

**Los indicadores**, que hay que saber uno a uno:

| Indicador | Significado |
|----|----|
| **SYN** | Sincronizar números de secuencia: **abre** la conexión |
| **ACK** | El campo de acuse de recibo es válido |
| **FIN** | **Cierre ordenado**: «no tengo más datos que enviar» |
| **RST** | **Reinicio abrupto**: aborta la conexión o rechaza una petición a un puerto cerrado |
| **PSH** | Entregar los datos a la aplicación **sin esperar** a llenar el buffer |
| **URG** | Hay datos urgentes; el puntero de urgencia los delimita |
| **ECE / CWR** | Notificación explícita de congestión \[RFC2474\] |

**El saludo de tres vías** (*three-way handshake*), el mecanismo central del tema:

1.  El cliente envía **`SYN`** con su número de secuencia inicial (**ISN**, elegido de forma aleatoria por seguridad \[RFC9293\]).
2.  El servidor responde **`SYN + ACK`**: reconoce el del cliente y envía el suyo.
3.  El cliente responde **`ACK`**. La conexión queda **establecida** (*ESTABLISHED*) y ya puede transferirse.

> **Dato clave.** **¿Por qué tres y no dos?** Porque **cada sentido de la comunicación debe sincronizar su propio número de secuencia y ser reconocido**, y con dos mensajes el servidor no tendría confirmación de que el cliente recibió su número. El tercer mensaje también evita que un `SYN` duplicado y retrasado en la red abra una conexión fantasma. Y el número de secuencia inicial es **aleatorio** para dificultar la suplantación de conexiones.

**El cierre.** TCP cierra **cada sentido por separado**, de ahí que sean **cuatro** segmentos: `FIN` del que termina, `ACK` del otro, `FIN` del otro cuando también termina, y `ACK` final. Entre medias puede haber **cierre parcial** (*half-close*): un extremo ya no envía pero sigue recibiendo. El extremo que cierra primero queda en el estado **TIME-WAIT** durante **2×MSL** (el doble de la vida máxima de un segmento) para absorber segmentos retrasados. Existe además el **cierre abrupto** con `RST`, que descarta lo pendiente.

**Estados principales de la máquina de estados** \[RFC9293\]: `CLOSED`, `LISTEN`, `SYN-SENT`, `SYN-RECEIVED`, `ESTABLISHED`, `FIN-WAIT-1`, `FIN-WAIT-2`, `CLOSE-WAIT`, `CLOSING`, `LAST-ACK`, `TIME-WAIT`.

**Control de flujo: la ventana deslizante.** El receptor anuncia en cada segmento cuántos octetos **puede aceptar** (campo Ventana). El emisor no envía más de esa cantidad sin acuse. Si la ventana llega a cero, el emisor se detiene y sondea periódicamente. Como el campo es de 16 bits —máximo 65.535 octetos, insuficiente en enlaces rápidos—, existe la opción de **escalado de ventana** \[RFC5681\].

**Control de congestión.** Cuatro algoritmos que hay que saber nombrar y ordenar \[RFC5681\]:

1.  **Arranque lento** (*slow start*): la ventana de congestión empieza pequeña y se **duplica** cada tiempo de ida y vuelta hasta alcanzar un umbral. Pese al nombre, el crecimiento es **exponencial**.
2.  **Evitación de congestión**: superado el umbral, el crecimiento pasa a ser **lineal** (un segmento por ciclo).
3.  **Retransmisión rápida**: **tres acuses duplicados** se interpretan como pérdida de un segmento y se retransmite **sin esperar** a que venza el temporizador.
4.  **Recuperación rápida**: tras la retransmisión rápida no se vuelve al arranque lento, sino que se reduce la ventana a la mitad y se continúa en evitación de congestión.

Además, el emisor calcula el **temporizador de retransmisión (RTO)** a partir de una estimación suavizada del tiempo de ida y vuelta y de su variación, y aplica **retroceso exponencial** ante retransmisiones sucesivas.

> **Dato clave.** La secuencia **arranque lento → evitación de congestión → retransmisión rápida → recuperación rápida** hay que saberla en orden, y la trampa está en el nombre: **el arranque lento crece exponencialmente**; lo «lento» es el punto de partida, no el ritmo. La señal de congestión que usa TCP es **la pérdida de paquetes**: interpreta que si algo se pierde, es porque hay una cola llena.

**Otras funciones.** **Acuse acumulativo** —el número de acuse indica el siguiente octeto esperado, y confirma implícitamente todo lo anterior— con la mejora del **acuse selectivo (SACK)**; **acuse retardado**, para agrupar; y el **algoritmo de Nagle**, que agrupa datos pequeños para evitar el «síndrome de la ventana tonta».

> **Relación con otros temas.** La **inundación de SYN** (*SYN flood*) —abrir miles de conexiones a medio establecer para agotar la tabla del servidor— es el ataque clásico contra el saludo de tres vías, y se combate con *cookies* de SYN y limitación de tasa. Se desarrolla en el **Tema 32** (amenazas) y en el **Tema 36** (protección perimetral).

#### 7.3. User Datagram Protocol (UDP)

**Caracterización.** UDP presta un servicio **no orientado a conexión**, **no fiable** y **orientado a mensajes** \[RFC768\]. Es **deliberadamente mínimo**: su especificación ocupa tres páginas frente a las más de noventa de TCP.

**La cabecera UDP**: **ocho octetos fijos**, cuatro campos:

| Campo | Bits | Función |
|----|----|----|
| **Puerto de origen** | 16 | **Opcional** en IPv4: puede ir a cero si no se espera respuesta |
| **Puerto de destino** | 16 |  |
| **Longitud** | 16 | Cabecera **más** datos, mínimo 8 |
| **Suma de comprobación** | 16 | **Opcional en IPv4** (cero = no calculada); **obligatoria en IPv6** |

> **Dato clave.** **La cabecera UDP mide 8 octetos y tiene cuatro campos**; la de TCP, **20 como mínimo**. Y un matiz importante: **la suma de comprobación de UDP es opcional sobre IPv4 pero obligatoria sobre IPv6**, precisamente porque IPv6 eliminó la suya de la cabecera de red.

**Qué NO hace UDP**: no establece conexión, no numera los datagramas, no acusa recibo, no retransmite, no ordena, no controla el flujo y no controla la congestión. **Sí conserva los límites de mensaje**: cada escritura de la aplicación produce exactamente un datagrama, y el receptor lo lee entero o no lo lee.

**Cuándo se elige UDP.** Cuatro situaciones que conviene poder enunciar:

1.  **Aplicaciones en tiempo real** —voz, vídeo, juegos— donde **llegar tarde es peor que no llegar**: retransmitir un fragmento de audio de hace dos segundos no sirve de nada.
2.  **Intercambios de petición y respuesta breves**, en los que abrir y cerrar una conexión costaría más que el propio dato: **DNS**, **NTP**, **SNMP**.
3.  **Difusión y multidifusión**, que TCP no puede hacer: **DHCP**, transmisión de vídeo a un grupo.
4.  Aplicaciones que **implantan su propia fiabilidad** por encima, adaptada a su caso: **QUIC** es el ejemplo contemporáneo.

**Comparativa TCP frente a UDP** (ver **diagrama D17**). Es la tabla que hay que poder escribir de memoria:

| Criterio | **TCP** | **UDP** |
|----|----|----|
| Número de protocolo IP | **6** | **17** |
| Modo | Orientado a conexión | No orientado a conexión |
| Fiabilidad | **Sí**: acuse, retransmisión y orden | **No** |
| Cabecera | **20-60 octetos** | **8 octetos fijos** |
| Unidad | **Segmento**; flujo de octetos | **Datagrama**; conserva límites de mensaje |
| Control de flujo | Sí (ventana deslizante) | No |
| Control de congestión | Sí | No |
| Difusión y multidifusión | **No** | **Sí** |
| Latencia y sobrecarga | Mayores | **Mínimas** |
| Aplicaciones típicas | HTTP, HTTPS, SMTP, FTP, SSH, IMAP, LDAP | DNS, DHCP, SNMP, NTP, TFTP, RTP, voz y vídeo |

> **Ejercicio resuelto.** **Elegir transporte para cuatro servicios municipales.** El IAM va a desplegar cuatro servicios. ¿Qué protocolo de transporte corresponde a cada uno y por qué?
>
> | Servicio | Transporte | Justificación |
> |----|----|----|
> | Presentación de solicitudes en la **sede electrónica** | **TCP** (443) | Un documento no puede llegar incompleto ni desordenado: la fiabilidad es un requisito jurídico, no de rendimiento. Además, TLS **exige** un transporte fiable |
> | **Telefonía IP** de las oficinas de atención | **UDP** (RTP) | La conversación no admite retransmisiones: un paquete de voz que llega tarde ya es inútil. Se prefiere un pequeño corte a un retardo acumulado. La señalización (**SIP**), en cambio, puede ir por TCP |
> | **Monitorización** de los conmutadores de distrito | **UDP** (SNMP, 161/162) | Intercambios muy breves y muy numerosos; perder una lectura de contador no es grave y la siguiente llega en un minuto |
> | **Copia nocturna** de la base de datos de expedientes al CPD de respaldo | **TCP** | Volumen grande donde **cada octeto importa** y donde el control de congestión es una ventaja: aprovecha el ancho de banda disponible sin saturar la red |
>
> **Conclusión que se extrae**: el criterio no es «TCP es mejor». El criterio es **qué prefiere la aplicación cuando algo se pierde**: si prefiere esperar, TCP; si prefiere seguir, UDP.

------------------------------------------------------------------------

### 8. Pila de protocolos TCP/IP: capa de aplicación

Advertencia de alcance: este apartado recorre **el catálogo de protocolos de la pila**, con su puerto, su transporte y su función. **El desarrollo de HTTP, HTTPS y SSL/TLS corresponde al Tema 35**, y aquí se tratan solo en lo imprescindible para situarlos en la arquitectura.

#### 8.1. Servicios de infraestructura de red (DNS y DHCP)

Se llaman así porque **no los usa el usuario directamente**: son los servicios sin los cuales los demás no funcionan.

**DNS (Sistema de Nombres de Dominio)** \[RFC1034\]. Traduce **nombres** en **direcciones IP** —y viceversa—. Es una **base de datos distribuida, jerárquica y con delegación de autoridad**, y es probablemente el sistema distribuido más grande y más antiguo en funcionamiento continuo.

**Estructura del espacio de nombres** (ver **diagrama D18**): un árbol invertido cuya **raíz** se representa por un punto. Bajo ella, los **dominios de primer nivel** (**TLD**): genéricos (`.com`, `.org`, `.net`), de código de país (`.es`, `.fr`) y patrocinados (`.gob.es`). Por debajo, los dominios de segundo nivel (`madrid.es`) y los subdominios (`sede.madrid.es`). Un **nombre de dominio plenamente cualificado (FQDN)** es la ruta completa hasta la raíz.

**Elementos del sistema:**

- **Zona**: porción del árbol administrada como una unidad.
- **Servidor autoritativo**: el que **tiene** los datos de una zona. **Primario o maestro** si mantiene el fichero original, **secundario o esclavo** si obtiene copia por **transferencia de zona**.
- **Servidor recursivo o resolutor**: el que **hace el trabajo** por el cliente, consultando en cadena. Es el que se configura en el puesto.
- **Servidores raíz**: **13 identidades lógicas** (de `a.root-servers.net` a `m.root-servers.net`), replicadas en cientos de instancias físicas mediante **anidifusión**.

**Resolución.** El cliente hace una consulta **recursiva** a su resolutor: «dame la respuesta, no me des pistas». El resolutor hace consultas **iterativas** a la raíz, al TLD y al autoritativo, que le van remitiendo al siguiente. La respuesta se guarda en **caché** durante el tiempo que indica el **TTL** del registro.

**Tipos de registro** de memorización obligatoria:

| Registro | Contenido |
|----|----|
| **A** | Nombre → dirección **IPv4** |
| **AAAA** | Nombre → dirección **IPv6** |
| **CNAME** | Alias: nombre → otro nombre |
| **MX** | Servidor de **correo** de un dominio, con prioridad |
| **NS** | Servidores **autoritativos** de la zona |
| **SOA** | **Inicio de autoridad**: parámetros de la zona (serie, refresco, expiración) |
| **PTR** | Dirección → nombre (**resolución inversa**, bajo `in-addr.arpa` o `ip6.arpa`) |
| **TXT** | Texto libre; soporte de **SPF**, **DKIM** y **DMARC** en el correo |
| **SRV** | Servicio, protocolo, puerto y equipo que lo presta |

> **Dato clave.** **DNS usa el puerto 53 sobre UDP para las consultas ordinarias y sobre TCP cuando la respuesta no cabe o para las transferencias de zona** \[RFC1035P\]. Es el ejemplo canónico de protocolo que emplea los dos transportes. Y los tres datos de refuerzo: **DNSSEC** firma las respuestas para garantizar su autenticidad e integridad —no las cifra—; **DNS sobre HTTPS (DoH)** y **DNS sobre TLS (DoT)** sí cifran la consulta; y el **envenenamiento de la caché** es el ataque clásico contra el sistema.

**DHCP (Protocolo de Configuración Dinámica de Equipos)** \[RFC2131\]. Entrega a un equipo, al arrancar, su **configuración de red completa**: dirección IP, máscara, puerta de enlace predeterminada, servidores DNS, dominio de búsqueda, servidor de hora y, en su caso, servidor de arranque en red.

**El intercambio DORA**, de memorización obligatoria (ver **diagrama D19**):

1.  **DISCOVER**: el cliente, que aún no tiene dirección, emite **por difusión** desde `0.0.0.0` buscando servidores.
2.  **OFFER**: uno o varios servidores **ofrecen** una dirección.
3.  **REQUEST**: el cliente **solicita formalmente** una de las ofertas, también por difusión, para que los demás servidores retiren la suya.
4.  **ACK**: el servidor **confirma** y entrega la concesión con su tiempo de vida.

**La concesión** (*lease*) es temporal. El cliente intenta **renovarla al 50 % del tiempo (T1)** directamente con su servidor, y si no lo consigue, intenta **reenlazar al 87,5 % (T2)** por difusión con cualquier servidor. Si expira sin renovación, debe dejar de usar la dirección.

> **Dato clave.** **DHCP usa UDP: puerto 67 en el servidor y 68 en el cliente.** Como los mensajes iniciales van **por difusión** y la difusión **no atraviesa encaminadores**, en redes con varias subredes hace falta un **agente de retransmisión DHCP** (*DHCP relay*, la función `ip helper-address`) en el encaminador, que reenvía la petición al servidor central por unidifusión. Recordar también **APIPA**: si no hay respuesta, el cliente se autoasigna una dirección `169.254.x.x` de enlace local y solo puede hablar con su propio segmento.

Para IPv6 existe **DHCPv6** \[RFC2131\], sobre los puertos **UDP 546** (cliente) y **547** (servidor), que puede usarse **con estado** —asigna direcciones— o **sin estado** —solo entrega parámetros como el DNS, mientras la dirección se obtiene por SLAAC—.

#### 8.2. Protocolos de servicios web y de transferencia de archivos

**HTTP y HTTPS.** **HTTP** es el protocolo de la web: un protocolo de **petición y respuesta**, **sin estado**, sobre **TCP/80**; **HTTPS** es el mismo protocolo transportado sobre **TLS**, en el **puerto 443** \[RFC9110\]. Las versiones: **HTTP/1.1** sobre TCP, **HTTP/2** sobre TCP con multiplexación de flujos y compresión de cabeceras, y **HTTP/3** sobre **QUIC**, que a su vez va sobre **UDP**.

> **Relación con otros temas.** HTTP, HTTPS y SSL/TLS —versiones, métodos, códigos de estado, saludo TLS, certificados— son el objeto del **Tema 35**, y la criptografía que los sustenta, del **Tema 32**. Aquí basta con saber **situarlos**: capa de aplicación, sobre TCP salvo HTTP/3, puertos 80 y 443.

> **Dato clave.** **HTTP/3 es el primer protocolo web mayoritario que no usa TCP**: se apoya en **QUIC sobre UDP**. Es un dato reciente, y ejemplifica la observación de §4.1 sobre las violaciones deliberadas de la estratificación.

**FTP (Protocolo de Transferencia de Ficheros)** \[RFC959\]. Su particularidad arquitectónica es que usa **dos conexiones TCP separadas**:

- Una **conexión de control**, en el **puerto 21**, que permanece abierta toda la sesión y por la que viajan los comandos.
- Una **conexión de datos**, distinta para cada transferencia.

Dos modos:

- **Activo**: el **servidor** abre la conexión de datos **desde su puerto 20** hacia un puerto que el cliente le indica. Problema: los cortafuegos y los traductores de direcciones del lado del cliente **bloquean esa conexión entrante**.
- **Pasivo**: el **cliente** abre también la conexión de datos, hacia un puerto que el servidor le indica. Es el modo que funciona a través de cortafuegos y el que se usa en la práctica.

Variantes seguras: **FTPS** (FTP sobre TLS) y **SFTP**, que **no es FTP en absoluto** sino un subsistema de **SSH** sobre el **puerto 22**. Y **TFTP**, versión trivial sobre **UDP/69**, sin autenticación, usada para arrancar equipos por red y volcar configuraciones.

> **Dato clave.** **SFTP ≠ FTPS.** SFTP es SSH (puerto 22); FTPS es FTP con TLS (puertos 21/990). Es una confusión frecuente. Y el dato de FTP: **21 control, 20 datos en modo activo**, con el modo **pasivo** como el compatible con cortafuegos.

**Otros protocolos de acceso remoto y de compartición:**

- **SSH** (*Secure Shell*), **TCP/22**: intérprete de órdenes remoto cifrado, transferencia de ficheros (`scp`, `sftp`) y **túneles**. Sustituye a **Telnet** (**TCP/23**), que transmite **en claro**, incluidas las contraseñas, y que **no debe usarse**.
- **RDP** (*Remote Desktop Protocol*), **TCP/3389**: escritorio remoto de Windows.
- **SMB/CIFS**, **TCP/445**: compartición de ficheros e impresoras en entornos Windows. **NFS**, **TCP y UDP/2049**, su equivalente en entornos Unix.
- **LDAP**, **TCP/389**, y **LDAPS**, **TCP/636**: acceso al directorio corporativo de identidades. **Kerberos**, **puerto 88**, para autenticación en dominio.

> **Relación con otros temas.** El control remoto del puesto de usuario y las herramientas de asistencia se desarrollan en el **Tema 29**; la administración de usuarios y de dispositivos en la red local, en el **Tema 30**.

#### 8.3. Protocolos de correo electrónico y de gestión de red

**El correo electrónico** se apoya en **dos familias** de protocolos, y confundirlas es el error más habitual:

- **Para enviar y para transportar entre servidores**: **SMTP** \[RFC5321\], **TCP/25**. Es un protocolo de **empuje** (*push*): el emisor entrega el mensaje al servidor y este lo empuja al siguiente hasta el buzón de destino. Para el **envío desde el cliente** al servidor de su organización, la especificación reserva el **puerto 587** con autenticación obligatoria \[RFC5321\], y el **465** para SMTP sobre TLS implícito.
- **Para consultar el buzón**: **POP3** \[RFC5321\], **TCP/110**, y **IMAP**, **TCP/143**. Son protocolos de **extracción** (*pull*).

**POP3 frente a IMAP**:

| Criterio | **POP3** | **IMAP** |
|----|----|----|
| Puerto (y seguro) | **110** (**995** con TLS) | **143** (**993** con TLS) |
| Modelo | **Descarga y borra**: el mensaje se traslada al equipo | **Sincroniza**: el mensaje **permanece en el servidor** |
| Carpetas en el servidor | No | **Sí**, con gestión completa |
| Varios dispositivos | Mal soportado | **Diseñado para ello** |
| Descarga parcial | No: todo o nada | **Sí**: cabeceras primero, cuerpo a demanda |
| Consumo en el servidor | Bajo | Mayor (almacena todo) |

Complementos del correo que conviene citar: **MIME**, que permite adjuntar contenido no textual y declarar juegos de caracteres; y los tres mecanismos antisuplantación, que se publican como **registros TXT en el DNS**: **SPF** (qué servidores pueden enviar en nombre del dominio), **DKIM** (firma criptográfica del mensaje) y **DMARC** (política y notificación).

> **Dato clave.** Los puertos del correo, en bloque: **25** SMTP entre servidores · **587** envío autenticado del cliente · **465** SMTP sobre TLS · **110** POP3 · **995** POP3S · **143** IMAP · **993** IMAPS. Y la distinción funcional: **SMTP envía, POP3 e IMAP consultan.**

**Gestión de red: SNMP** \[RFC3411\]. Es el protocolo con el que se supervisan y configuran los equipos de red. Elementos:

- **Gestor** (*manager*): la estación de gestión que consulta.
- **Agente**: el proceso que corre en el equipo gestionado.
- **MIB** (*Management Information Base*): la **base de información de gestión**, un árbol jerárquico de variables identificadas por un **OID** (identificador de objeto). La **MIB-II** \[RFC3411\] es el conjunto normalizado básico.

**Operaciones**: `GET`, `GETNEXT`, `GETBULK` (desde la versión 2), `SET` y **`TRAP`** —la notificación **asíncrona** que envía el agente cuando ocurre algo—, con su variante confirmada `INFORM`.

> **Dato clave.** **SNMP usa UDP: puerto 161 para las consultas del gestor y 162 para las trampas que envía el agente.** Y sobre versiones: **SNMPv1 y v2c autentican con una simple «comunidad» que viaja en claro** —`public` y `private` por defecto, un problema de seguridad clásico—; **solo SNMPv3 incorpora autenticación y cifrado** mediante el modelo de seguridad basado en usuario. En una Administración sujeta al ENS, **la versión exigible es la 3**.

**Sincronización horaria: NTP** \[RFC5905\], **UDP/123**. Organiza los servidores en **estratos**: el estrato 0 son las fuentes de referencia (reloj atómico, GPS), el estrato 1 los servidores conectados directamente a ellas, y así sucesivamente. Su importancia no es menor: **sin hora común no hay correlación de registros de actividad, ni validación de certificados, ni sellos de tiempo fiables**, y por eso el ENS lo trata como requisito de la trazabilidad.

> **Relación con otros temas.** La sincronización horaria es requisito de los **registros de actividad** (`op.exp.8` del ENS, ver **Tema 32** y **Tema 39**) y condición de validez de los **sellos de tiempo** de la firma electrónica (**Tema 32**).

**Tabla de puertos de referencia** (ver **diagrama D17**). Los que hay que saber sin dudar:

| Puerto | Transporte | Servicio | Puerto | Transporte | Servicio |
|----|----|----|----|----|----|
| **20/21** | TCP | FTP (datos / control) | **143** | TCP | IMAP |
| **22** | TCP | SSH, SCP, SFTP | **161/162** | UDP | SNMP (consulta / trampa) |
| **23** | TCP | Telnet (**en claro**) | **389** | TCP | LDAP |
| **25** | TCP | SMTP | **443** | TCP | HTTPS |
| **53** | **UDP y TCP** | DNS | **445** | TCP | SMB |
| **67/68** | UDP | DHCP (servidor / cliente) | **465/587** | TCP | SMTP seguro / envío |
| **69** | UDP | TFTP | **636** | TCP | LDAPS |
| **80** | TCP | HTTP | **993/995** | TCP | IMAPS / POP3S |
| **88** | TCP y UDP | Kerberos | **3389** | TCP | RDP |
| **110** | TCP | POP3 | **500/4500** | UDP | IKE / IPsec con NAT |
| **123** | UDP | NTP | **1812/1813** | UDP | RADIUS |

------------------------------------------------------------------------

### 9. Normativa e integración en la Administración Pública

> **Material complementario.** El enunciado oficial de este tema no nombra este apartado. Se mantiene porque sitúa la materia en el Ayuntamiento y en la normativa que le aplica, pero lo exigible es lo que enumera el título del tema.

#### 9.1. Adopción e implantación de IPv6 en el sector público

**Por qué le concierne a una Administración.** El agotamiento de IPv4 no es un problema académico para un ayuntamiento: condiciona el crecimiento de la red municipal, la incorporación de dispositivos —sensores, cámaras, contadores, señalización— y la accesibilidad de los servicios públicos desde redes que ya solo entregan IPv6 a sus usuarios. Además, la Ley 39/2015 configura la relación electrónica como un **derecho de la ciudadanía** (art. 13.a) y como una **obligación** para determinados sujetos (art. 14) \[L39-2015\]: si un ciudadano no puede alcanzar la sede electrónica desde su red, hay un problema jurídico, no solo técnico.

**El instrumento español.** El **Plan de fomento para la incorporación del protocolo IPv6 en España** fue aprobado por **Acuerdo de Consejo de Ministros de 29 de abril de 2011** y publicado mediante la **Orden PRE/1716/2011** \[IPV6-PLAN\]. Es la referencia normativa que hay que citar. Sus **diez líneas de actuación** se agrupan en tres frentes:

- **En la propia Administración**: incorporación de IPv6 en los **portales del Estado**, actualización del **plan de direccionamiento e interconexión de redes** de las Administraciones, **incorporación de IPv6 en la red SARA** y —línea de mayor efecto práctico— **exigencia de soporte de IPv6 como requisito en la contratación pública** de equipamiento y de servicios.
- **En el sector privado**: ayudas a proyectos, colaboración con asociaciones empresariales y un grupo de trabajo con el sector TIC.
- **En la infraestructura común**: funcionamiento pleno de IPv6 en el sistema de nombres del dominio **`.es`**, y jornadas de formación y divulgación.

**Cómo se traduce en decisiones concretas** para un organismo como el IAM:

1.  **Doble pila como estrategia**, no túneles: es el mecanismo recomendado \[RFC4213\] y el único que no degrada el rendimiento ni añade puntos de fallo.
2.  **Cláusula de soporte IPv6 en los pliegos**: todo equipamiento de red, servidor, sistema operativo o servicio contratado debe soportar IPv6 de forma nativa y certificada. Es la línea del Plan con más recorrido, porque **impide seguir comprando el problema**.
3.  **Publicación de los servicios de cara al ciudadano con registro `AAAA`** en el DNS, empezando por la sede electrónica.
4.  **Extensión de las políticas de seguridad a la nueva pila**: reglas de filtrado, registro de actividad y monitorización equivalentes en IPv4 y en IPv6.
5.  **Direccionamiento y documentación**: obtención de un bloque de direcciones a través del registro regional o del proveedor, y diseño del plan de direccionamiento con `/64` por subred.

> **Dato clave.** El instrumento que hay que citar es el **Plan de fomento para la incorporación del protocolo IPv6 en España**, **Acuerdo de Consejo de Ministros de 29 de abril de 2011**, publicado por **Orden PRE/1716/2011**. Sus dos medidas más citadas en el ámbito de las Administraciones son la **incorporación de IPv6 en la red SARA** y su **exigencia como requisito en la contratación pública**.

> **Dato clave.** El riesgo de seguridad específico de la transición: **un equipo con doble pila cuyo cortafuegos solo filtra IPv4 queda efectivamente abierto por IPv6**. Y, en la misma línea, los **túneles automáticos** (6to4, Teredo) pueden **atravesar el perímetro sin ser inspeccionados**, por lo que deben deshabilitarse expresamente si no se usan.

#### 9.2. Requisitos de red e interconexión en el Esquema Nacional de Seguridad

**El encaje legal.** El **artículo 156 de la Ley 40/2015** establece el **Esquema Nacional de Interoperabilidad** (apartado 1) y el **Esquema Nacional de Seguridad** (apartado 2) \[L40-2015\]. De ahí cuelgan el **RD 4/2010 (ENI)** \[ENI\] y el **RD 311/2022 (ENS)** \[ENS\]. Ambos son de **aplicación directa al Ayuntamiento de Madrid y a sus organismos autónomos**, incluido el IAM.

**La red de comunicaciones de las Administraciones: SARA.** El **artículo 13 del ENI** regula la **red de comunicaciones de las Administraciones públicas españolas**, cuya realización es la **red SARA** (Sistemas de Aplicaciones y Redes para las Administraciones), y remite a una norma técnica para los requisitos de conexión. Esa norma es la **NTI de requisitos de conexión a la red de comunicaciones de las Administraciones Públicas españolas**, aprobada por **Resolución de 19 de julio de 2011** \[NTI-RED\].

**Qué exige la NTI de conexión**, verificado contra el texto del BOE (ver **diagrama D20**):

- **Objeto**: establecer las condiciones en las que cualquier órgano de una Administración accede a la red SARA.
- **Tres agentes**: el **órgano gestor** de la red, que administra la conexión y presta soporte permanente; los **proveedores de acceso**, que son las Administraciones que actúan como **punto único de conexión** para los organismos que dependen de ellas; y los **órganos usuarios finales**, que acceden a través de su proveedor de acceso.
- **Área de conexión** con arquitectura de **zona desmilitarizada**, delimitada por un **subsistema de seguridad externo** y otro **interno**. Es decir: no se conecta la red interna a SARA, se conecta una zona intermedia controlada.
- **Servicios básicos** que el área de conexión debe prestar: **DNS**, **correo**, **hora** y **navegación**.
- **Cifrado obligatorio**: todas las comunicaciones que discurren por la red están **cifradas mediante túneles**.
- **Sujeción al plan de direccionamiento e interconexión de redes**, lo que impide que cada organismo elija sus direcciones libremente: hay que **adaptarse al plan común** para evitar solapamientos.
- **Coordinación con el CCN-CERT** en materia de seguridad.

**Las medidas del ENS que se predican de la red.** Del anexo II del RD 311/2022, verificadas literalmente contra el PDF del BOE \[ENS\]:

| Medida | Denominación | Dimensiones | Aplicación |
|----|----|----|----|
| **`mp.com.1`** | **Perímetro seguro** | Todas | **Las tres categorías** |
| **`mp.com.2`** | **Protección de la confidencialidad** | C | BAJO: aplica · MEDIO: +R1 · ALTO: +R1+R2+R3 |
| **`mp.com.3`** | **Protección de la integridad y de la autenticidad** | I, A | BAJO: aplica · MEDIO: +R1+R2 · ALTO: +R1+R2+R3+R4 |
| **`mp.com.4`** | **Separación de flujos de información en la red** | Todas | BÁSICA: **no aplica** · MEDIA: +\[R1 o R2 o R3\] · ALTA: +\[R2 o R3\]+R4 |

Contenido literal de cada una, en lo que interesa a este tema:

- **`mp.com.1`**: *«se dispondrá de un sistema de protección perimetral que separe la red interna del exterior. Todo el tráfico deberá atravesar dicho sistema»*, y *«todos los flujos de información a través del perímetro deben estar autorizados previamente»*. El propio ENS remite a una **Instrucción Técnica de Seguridad de Interconexión de Sistemas de Información** para los requisitos concretos por categoría.
- **`mp.com.2`**: *«se emplearán redes privadas virtuales cifradas cuando la comunicación discurra por redes fuera del propio dominio de seguridad»*. El refuerzo **R1** exige **algoritmos y parámetros autorizados por el CCN** \[CCN-STIC-807\].
- **`mp.com.3`**: exige asegurar la autenticidad del otro extremo y **prevenir ataques activos**, garantizando que, al ser detectados, se registren y activen los procedimientos de respuesta.
- **`mp.com.4`**: *«el tráfico por la red se segregará para que cada equipo solamente tenga acceso a la información que necesita»* y *«si se emplean comunicaciones inalámbricas, será en un segmento separado»*. Sus cuatro refuerzos son escalonados: **R1 segmentación lógica básica mediante VLAN**, con segregación mínima en **usuarios, servicios y administración**; **R2 segmentación lógica avanzada mediante VPN**; **R3 segmentación física** con medios separados; y **R4 puntos de interconexión** controlados y monitorizados.

> **Dato clave.** Los cuatro códigos `mp.com` con su denominación exacta son de memorización obligatoria, y en particular dos matices: **`mp.com.4` NO APLICA en categoría BÁSICA** —es la única del grupo que no se exige siempre—, y su **refuerzo R1 nombra expresamente las VLAN** y la segregación mínima en **usuarios, servicios y administración**. La denominación oficial de **`mp.com.3` es «protección de la integridad y de la autenticidad»**, en ese orden, y la de **`mp.com.4`, «separación de flujos de información en la red»** —no «segregación de redes», que era su nombre en el derogado RD 3/2010—.

**Otras medidas conexas** que conviene citar: **`op.mon.1`** (detección de intrusión) y **`op.mon.2`** (sistema de métricas), que se apoyan en la instrumentación de la red; **`op.exp.8`** (registro de la actividad), que exige una **base de tiempo común** y por tanto sincronización NTP; y **`mp.eq.4`** (otros dispositivos conectados a la red).

> **Ejemplo de aplicación en el ayto.** Traducido a la arquitectura de la red municipal, la normativa dicta el diseño casi punto por punto: la conexión a internet y la conexión a SARA pasan por **áreas de conexión distintas**, cada una con su zona desmilitarizada y su doble subsistema de seguridad (`mp.com.1` y NTI); el tráfico hacia otras Administraciones va **cifrado por túnel** y nunca por internet abierta (`mp.com.2` y NTI); la red de cada dependencia está **segmentada en VLAN** separando como mínimo puestos de usuario, servidores y gestión de los equipos de red (`mp.com.4.r1`); las cámaras y los dispositivos de la ciudad viven en **segmentos propios** (`mp.eq.4`); el direccionamiento sigue el **plan común** para poder interconectar sin solapamientos (NTI); y todos los equipos comparten **hora NTP** para que los registros sean correlacionables (`op.exp.8`).

> **Relación con otros temas.** Los principios generales del ENS y del ENI, sus categorías y su régimen de auditoría corresponden al **Tema 39**. Las medidas de protección perimetral, los cortafuegos, los sistemas de detección de intrusión y las VPN de acceso remoto, al **Tema 36**. La administración diaria de la red municipal —gestión de usuarios y dispositivos, monitorización y control de tráfico—, al **Tema 30**.

------------------------------------------------------------------------

### Los diez datos que no se pueden fallar

Bloque de repaso final. Si el día del examen solo hubiera tiempo para una hoja, sería esta.

1.  **OSI tiene 7 capas** (física, enlace, red, transporte, sesión, presentación, aplicación) y es **norma ISO/IEC 7498-1**, idéntica a la **Recomendación UIT-T X.200**. **TCP/IP tiene 4 niveles** (acceso a la red, internet, transporte, aplicación) según la **RFC 1122**.
2.  **Las fusiones de la comparativa**: OSI 1+2 = acceso a la red; OSI 5+6+7 = aplicación. Las capas **3 y 4 se corresponden una a una**.
3.  **PDU por capa**: bit, **trama**, **paquete/datagrama**, **segmento** (TCP) o **datagrama** (UDP), mensaje. `PDU(N)` se convierte en `SDU(N−1)`.
4.  **Los tres campos de la demultiplexación**: **EtherType** (`0x0800` IPv4, `0x0806` ARP, `0x86DD` IPv6) → **Protocolo/Next Header** (**1** ICMP, **6** TCP, **17** UDP, **50** ESP, **51** AH, **58** ICMPv6) → **puerto de destino**.
5.  **Tamaños de cabecera**: Ethernet **14 + 4** · IPv4 **20-60** · IPv6 **40 fijos** · TCP **20-60** · UDP **8 fijos**. **MTU de Ethernet: 1.500**.
6.  **Direcciones**: MAC **48 bits** (24 de OUI), **plana** y de ámbito local, **cambia en cada salto**. IPv4 **32 bits** e IPv6 **128 bits**, **jerárquicas** y de ámbito global, **no cambian** (salvo NAT).
7.  **IPv6 frente a IPv4**: cabecera **fija de 40 octetos** y **ocho campos**, **sin suma de comprobación**, **no fragmenta en tránsito**, **no tiene difusión** (usa multidifusión: `ff02::1`, `ff02::2`), y **todo interfaz tiene una dirección de enlace local `fe80::`**. Mecanismo de transición recomendado: **doble pila**.
8.  **TCP**: orientado a conexión, fiable, **flujo de octetos**, punto a punto; **saludo de tres vías** `SYN` → `SYN+ACK` → `ACK` y **cierre en cuatro**. **UDP**: sin conexión, sin garantías, **conserva los límites de mensaje**, permite **multidifusión**.
9.  **Puertos**: rangos **0-1023 / 1024-49151 / 49152-65535**. Los imprescindibles: **21/20** FTP · **22** SSH · **23** Telnet · **25** SMTP · **53** DNS (**UDP y TCP**) · **67/68** DHCP · **80** HTTP · **110** POP3 · **123** NTP · **143** IMAP · **161/162** SNMP · **389** LDAP · **443** HTTPS · **993/995** IMAPS/POP3S · **3389** RDP.
10. **Normativa**: conexión a **SARA** por la **NTI de requisitos de conexión** (Resolución de **19 de julio de 2011**, al amparo del **ENI**), con **zona desmilitarizada** y **cifrado obligatorio**; **IPv6** por el **Plan de fomento** (**Acuerdo de Consejo de Ministros de 29 de abril de 2011**, Orden PRE/1716/2011); y las cuatro medidas del ENS: **`mp.com.1`** perímetro seguro, **`mp.com.2`** confidencialidad, **`mp.com.3`** integridad y autenticidad, **`mp.com.4`** separación de flujos de información en la red —**que no aplica en categoría BÁSICA**—.

## Diagramas

### Índice de diagramas

| ID | Título | Sección | Tipo |
|----|----|----|----|
| D1 | Comunicación vertical real y comunicación horizontal virtual | §1.1 | Doble pila + flujos |
| D2 | Quién normaliza qué: organismos por ámbito y por capa | §1.2 | Mapa de competencias |
| D3 | Anatomía de una capa: servicio, interfaz, protocolo y SAP | §2.2 | Esquema conceptual |
| D4 | Las siete capas del modelo OSI: función, PDU y ejemplos | §2.3 | Tabla-pila |
| D5 | Encapsulamiento y desencapsulamiento: PDU, SDU y PCI | §2.4 | Flujo descendente |
| D6 | El modelo TCP/IP: cuatro niveles y sus protocolos | §3.2 | Pila + reloj de arena |
| D7 | Demultiplexación: los tres campos que deciden la entrega | §3.3 | Flujo ascendente |
| D8 | Correspondencia OSI ↔ TCP/IP y diferencias de diseño | §4.1 | Comparativa doble |
| D9 | La trama Ethernet II y la dirección MAC | §5.2 | Estructura de trama |
| D10 | La cabecera IPv4 campo a campo | §6.1 | Mapa de bits |
| D11 | Máscara, CIDR y cálculo de subredes | §6.1 | Algoritmo + ejemplo |
| D12 | La cabecera IPv6 y los tipos de dirección | §6.2 | Mapa de bits + tabla |
| D13 | Los tres mecanismos de transición a IPv6 | §6.2 | Comparativa |
| D14 | ARP, ICMP y ND: quién resuelve qué | §6.3 | Comparativa + flujo |
| D15 | La decisión de reenvío y la tabla de encaminamiento | §6.4 | Árbol de decisión |
| D16 | TCP: cabecera, saludo de tres vías y cierre en cuatro | §7.2 | Estructura + secuencia |
| D17 | TCP frente a UDP y mapa de puertos por servicio | §7.3 · §8 | Comparativa + tabla |
| D18 | DNS: jerarquía de nombres y proceso de resolución | §8.1 | Árbol + secuencia |
| D19 | DHCP: el intercambio DORA y el ciclo de la concesión | §8.1 | Secuencia + línea temporal |
| D20 | Conexión a SARA y medidas de red del ENS | §9.2 | Arquitectura normativa |

------------------------------------------------------------------------

### D1 · Comunicación vertical real y comunicación horizontal virtual

**Sección**: §1.1 — Concepto y necesidad de las arquitecturas por niveles **Propósito**: Fijar la distinción central de todo el bloque conceptual: entre capas de la misma máquina hay **interfaces** y comunicación **real**; entre capas homólogas de máquinas distintas hay **protocolos** y comunicación **virtual**.

![Dos sistemas con cuatro capas cada uno: entre capas adyacentes del mismo sistema la comunicación es vertical y real a través de una interfaz, mientras que entre capas homólogas de sistemas distintos la comunicación es horizontal y virtual mediante un protocolo; solo la capa física transmite bits de forma real por el medio](diagramas/diagrama-01.svg)

------------------------------------------------------------------------

### D2 · Quién normaliza qué: organismos por ámbito y por capa

**Sección**: §1.2 — Organismos internacionales de estandarización **Propósito**: Repartir los organismos entre normalización formal, comunidad de internet y asociaciones profesionales, y asociar cada uno a la parte de la pila que le corresponde.

![Reparto de competencias de normalización: ISO y UIT-T publican el modelo OSI, el IETF publica los RFC de la pila TCP-IP, el IEEE normaliza las capas física y de enlace mediante la serie 802, e IANA bajo ICANN administra los números de puerto, de protocolo y las direcciones a través de los cinco registros regionales](diagramas/diagrama-02.svg)

------------------------------------------------------------------------

### D3 · Anatomía de una capa: servicio, interfaz, protocolo y SAP

**Sección**: §2.2 — Conceptos de capa, servicio, interfaz y protocolo **Propósito**: Separar visualmente los tres conceptos que se confunden con facilidad: qué ofrece la capa (servicio), cómo se le pide (interfaz) y cómo lo consigue (protocolo).

![Anatomía de una capa: el servicio es lo que la capa N ofrece a la capa N más uno, la interfaz es el conjunto de primitivas con las que se le pide a través de un punto de acceso al servicio, y el protocolo es el conjunto de reglas con las que la entidad de la capa N dialoga con su entidad par en el otro sistema](diagramas/diagrama-03.svg)

------------------------------------------------------------------------

### D4 · Las siete capas del modelo OSI: función, PDU y ejemplos

**Sección**: §2.3 — Descripción de las capas del modelo OSI **Propósito**: Reunir en una sola imagen memorizable el número, el nombre, la función, la PDU y los protocolos de ejemplo de cada capa, más la división entre capas de red y capas de aplicación.

![Las siete capas del modelo OSI de arriba abajo: aplicación, presentación y sesión son capas orientadas al usuario y solo existen en los equipos terminales; transporte es la capa frontera y extremo a extremo; red, enlace de datos y física son capas orientadas a la red y están presentes también en los equipos intermedios. Se indica para cada capa su unidad de datos y ejemplos de protocolo](diagramas/diagrama-04.svg)

------------------------------------------------------------------------

### D5 · Encapsulamiento y desencapsulamiento: PDU, SDU y PCI

**Sección**: §2.4 — Unidades de datos de protocolo (PDU) y encapsulamiento **Propósito**: Mostrar cómo crece la unidad de datos al bajar por la pila y fijar la regla de que la PDU de la capa N se convierte en la SDU de la capa N menos uno.

![Proceso de encapsulamiento: los datos de la aplicación reciben una cabecera de transporte formando un segmento, ese segmento recibe una cabecera de red formando un paquete, y ese paquete recibe una cabecera y una cola de enlace formando una trama que se transmite como bits. En el destino el proceso se invierte](diagramas/diagrama-05.svg)

------------------------------------------------------------------------

### D6 · El modelo TCP/IP: cuatro niveles y sus protocolos

**Sección**: §3.2 — Niveles funcionales del modelo TCP/IP **Propósito**: Fijar los cuatro niveles de la RFC 1122 con sus protocolos y representar el principio del reloj de arena: muchas aplicaciones arriba, muchas redes abajo y un único protocolo en el cuello.

![Los cuatro niveles del modelo TCP-IP según la RFC 1122: aplicación con HTTP, DNS, SMTP y otros; transporte con TCP y UDP; internet con IP en sus versiones 4 y 6 más ICMP y ARP; y acceso a la red con Ethernet, Wi-Fi y PPP. El conjunto forma un reloj de arena con IP en el cuello, único protocolo común a todo el sistema](diagramas/diagrama-06.svg)

------------------------------------------------------------------------

### D7 · Demultiplexación: los tres campos que deciden la entrega

**Sección**: §3.3 — Encapsulamiento y demultiplexación de datos **Propósito**: Aislar los tres campos de cabecera que gobiernan la entrega hacia arriba y sus valores memorizables.

![La demultiplexación usa un campo por nivel: el campo EtherType de la trama indica el protocolo de red, con los valores 0x0800 para IPv4, 0x0806 para ARP y 0x86DD para IPv6; el campo Protocolo de IPv4 o Siguiente cabecera de IPv6 indica el protocolo de transporte, con los valores 1 para ICMP, 6 para TCP y 17 para UDP; y el puerto de destino indica el proceso de aplicación](diagramas/diagrama-07.svg)

------------------------------------------------------------------------

### D8 · Correspondencia OSI ↔ TCP/IP y diferencias de diseño

**Sección**: §4.1 — Correspondencia y equivalencia entre capas **Propósito**: Reunir en una imagen la correspondencia capa a capa —con las dos fusiones— y la tabla de diferencias de diseño, que son los dos ejes del apartado.

![Correspondencia entre el modelo OSI y el modelo TCP-IP: las capas de aplicación, presentación y sesión de OSI se funden en la capa de aplicación de TCP-IP; transporte y red se corresponden una a una con transporte e internet; y las capas de enlace de datos y física se funden en la capa de acceso a la red. Se añade una tabla con las diferencias de diseño entre ambos modelos](diagramas/diagrama-08.svg)

------------------------------------------------------------------------

### D9 · La trama Ethernet II y la dirección MAC

**Sección**: §5.2 — Direccionamiento físico MAC y transmisión de tramas **Propósito**: Fijar los campos de la trama con sus tamaños exactos y la estructura interna de la dirección MAC, que son datos de memorización directa.

![Estructura de la trama Ethernet II: preámbulo de 7 octetos y delimitador de 1, dirección MAC de destino de 6 octetos, dirección MAC de origen de 6 octetos, campo EtherType de 2 octetos, datos de 46 a 1500 octetos y secuencia de comprobación de trama de 4 octetos. La dirección MAC tiene 48 bits, de los que los 24 primeros son el identificador único del fabricante](diagramas/diagrama-09.svg)

------------------------------------------------------------------------

### D10 · La cabecera IPv4 campo a campo

**Sección**: §6.1 — Protocolo de Internet versión 4 (IPv4) **Propósito**: Presentar la cabecera en su disposición real de palabras de 32 bits, y destacar los tres campos clave.

![Cabecera IPv4 dispuesta en palabras de 32 bits: primera palabra con versión, longitud de cabecera, tipo de servicio y longitud total; segunda con identificación, indicadores y desplazamiento de fragmento; tercera con tiempo de vida, protocolo y suma de comprobación de la cabecera; cuarta con la dirección de origen; quinta con la dirección de destino; y opciones variables](diagramas/diagrama-10.svg)

------------------------------------------------------------------------

### D11 · Máscara, CIDR y cálculo de subredes

**Sección**: §6.1 — Protocolo de Internet versión 4 (IPv4) **Propósito**: Dar el procedimiento de cálculo y las fórmulas, con un ejemplo trabajado sobre el bloque de un distrito.

![Cálculo de subredes: una dirección de 32 bits se divide en parte de red y parte de equipo según la máscara. Las fórmulas son dos elevado a treinta y dos menos ene para el número de direcciones, menos dos para los equipos direccionables, y dos elevado a ka para el número de subredes al tomar prestados ka bits. Se ilustra con la división del bloque 10.20.8.0 barra 22 en cuatro subredes barra 24](diagramas/diagrama-11.svg)

------------------------------------------------------------------------

### D12 · La cabecera IPv6 y los tipos de dirección

**Sección**: §6.2 — Protocolo de Internet versión 6 (IPv6) **Propósito**: Contraponer la cabecera fija de ocho campos a la de IPv4 y reunir los prefijos de los tipos de dirección, que son datos de memorización directa.

![Cabecera IPv6 fija de 40 octetos con ocho campos: versión, clase de tráfico, etiqueta de flujo, longitud de la carga útil, siguiente cabecera, límite de saltos y las direcciones de origen y destino de 128 bits cada una. Se acompaña de los prefijos de los tipos de dirección: 2000 barra 3 unidifusión global, fe80 barra 10 enlace local, fc00 barra 7 local única y ff00 barra 8 multidifusión](diagramas/diagrama-12.svg)

------------------------------------------------------------------------

### D13 · Los tres mecanismos de transición a IPv6

**Sección**: §6.2 — Protocolo de Internet versión 6 (IPv6) **Propósito**: Separar doble pila, túneles y traducción, indicar cuál es el mecanismo recomendado y señalar el riesgo de seguridad de cada uno.

![Los tres mecanismos de transición a IPv6: doble pila, en la que el equipo ejecuta las dos pilas simultáneamente y es el mecanismo recomendado; túneles, que encapsulan IPv6 dentro de IPv4 usando el número de protocolo 41; y traducción mediante NAT64 y DNS64, que permite a un cliente solo IPv6 alcanzar un servidor solo IPv4](diagramas/diagrama-13.svg)

------------------------------------------------------------------------

### D14 · ARP, ICMP y ND: quién resuelve qué

**Sección**: §6.3 — Protocolos de control y resolución de direcciones (ICMP, ARP y ND) **Propósito**: Separar los tres protocolos auxiliares por función y por versión de IP, y fijar los tipos ICMP y los cinco mensajes de descubrimiento de vecinos.

![Comparación de los protocolos auxiliares de la capa de red: ARP resuelve direcciones IPv4 en direcciones MAC dentro del enlace mediante difusión; ICMP notifica errores y sirve de diagnóstico con el número de protocolo 1; y el descubrimiento de vecinos de IPv6 sustituye a ARP usando ICMPv6 y multidifusión, con cinco mensajes](diagramas/diagrama-14.svg)

------------------------------------------------------------------------

### D15 · La decisión de reenvío y la tabla de encaminamiento

**Sección**: §6.4 — Principios de enrutamiento IP **Propósito**: Reducir el encaminamiento a la única comprobación que hace un equipo terminal y fijar la regla del prefijo más largo y la clasificación de los protocolos de encaminamiento.

![Algoritmo de decisión de reenvío: el equipo aplica la operación Y lógica entre la dirección de destino y su máscara; si el resultado coincide con su dirección de red, el destino está en su misma subred y le envía la trama directamente; si no coincide, envía la trama a la dirección MAC de su puerta de enlace predeterminada dejando intacta la dirección IP de destino. Se acompaña de la regla del prefijo más largo y de la clasificación de los protocolos de encaminamiento](diagramas/diagrama-15.svg)

------------------------------------------------------------------------

### D16 · TCP: cabecera, saludo de tres vías y cierre en cuatro

**Sección**: §7.2 — Transmission Control Protocol (TCP) **Propósito**: Reunir en una imagen la cabecera con sus campos, la secuencia de apertura y la de cierre, que son los tres bloques clave del protocolo.

![Cabecera TCP de 20 octetos mínimo con puertos de origen y destino, número de secuencia, número de acuse de recibo, desplazamiento de datos, indicadores, ventana, suma de comprobación y puntero de urgencia. Secuencia de apertura en tres vías: SYN, SYN más ACK y ACK. Secuencia de cierre en cuatro segmentos: FIN, ACK, FIN y ACK](diagramas/diagrama-16.svg)

------------------------------------------------------------------------

### D17 · TCP frente a UDP y mapa de puertos por servicio

**Sección**: §7.3 — User Datagram Protocol (UDP) · §8 **Propósito**: Enfrentar los dos protocolos de transporte en los criterios clave y adjuntar la tabla de puertos, que es el bloque memorístico más rentable del tema.

![Comparación entre TCP y UDP: TCP es el protocolo 6, orientado a conexión, fiable, con cabecera de 20 a 60 octetos, con control de flujo y de congestión y sin multidifusión; UDP es el protocolo 17, sin conexión, no fiable, con cabecera fija de 8 octetos, sin control de flujo ni de congestión y con multidifusión. Se acompaña de una tabla con los puertos de los servicios más frecuentes](diagramas/diagrama-17.svg)

------------------------------------------------------------------------

### D18 · DNS: jerarquía de nombres y proceso de resolución

**Sección**: §8.1 — Servicios de infraestructura de red (DNS y DHCP) **Propósito**: Mostrar a la vez el árbol de nombres con la delegación y la secuencia de consultas recursiva e iterativa.

![El sistema de nombres de dominio es una base de datos distribuida y jerárquica: bajo la raíz están los dominios de primer nivel, bajo ellos los de segundo nivel y los subdominios. El cliente hace una consulta recursiva a su resolutor, que a su vez hace consultas iterativas a la raíz, al dominio de primer nivel y al servidor autoritativo hasta obtener la respuesta, que guarda en caché](diagramas/diagrama-18.svg)

------------------------------------------------------------------------

### D19 · DHCP: el intercambio DORA y el ciclo de la concesión

**Sección**: §8.1 — Servicios de infraestructura de red (DNS y DHCP) **Propósito**: Fijar los cuatro mensajes, los dos puertos, los umbrales de renovación y el papel del agente de retransmisión.

![Intercambio DHCP en cuatro mensajes: el cliente emite un descubrimiento por difusión, el servidor responde con una oferta, el cliente solicita formalmente una de las ofertas y el servidor confirma con un acuse. La concesión es temporal: se renueva al cincuenta por ciento del tiempo y se reenlaza al ochenta y siete coma cinco por ciento. En redes con varias subredes hace falta un agente de retransmisión](diagramas/diagrama-19.svg)

------------------------------------------------------------------------

### D20 · Conexión a SARA y medidas de red del ENS

**Sección**: §9.2 — Requisitos de red e interconexión en el Esquema Nacional de Seguridad **Propósito**: Traducir la normativa en arquitectura: qué exige la norma técnica de conexión a la red de las Administraciones y qué medidas del anexo II del ENS se predican de la red.

![Arquitectura normativa de la conexión de un ayuntamiento a la red SARA: la red interna municipal se conecta a un área de conexión con arquitectura de zona desmilitarizada delimitada por un subsistema de seguridad interno y otro externo, y desde ahí a la red SARA mediante túneles cifrados. Se acompaña de la tabla de las cuatro medidas de protección de las comunicaciones del anexo dos del Esquema Nacional de Seguridad](diagramas/diagrama-20.svg)

## Casos prácticos

Los tres casos recorren el supuesto de referencia del tema (ver la pestaña Contenido, «Convenciones»): la **red corporativa municipal** que conecta las oficinas de atención a la ciudadanía de los distritos con el centro de proceso de datos del IAM y, desde allí, con internet y con la red SARA. El **Caso 1** trabaja el **direccionamiento y la segmentación** de una oficina nueva (§5, §6 y §9.2); el **Caso 2**, el **diagnóstico de una incidencia** recorriendo la pila capa por capa (§2, §3, §7 y §8); y el **Caso 3**, la **migración a IPv6 y la conexión a SARA** (§6.2 y §9).

------------------------------------------------------------------------

### Caso 1 — Direccionamiento y segmentación de la red de una oficina de distrito

#### Enunciado

El Ayuntamiento abre una nueva **Oficina de Atención a la Ciudadanía** en un distrito. El IAM debe diseñar su red local y conectarla con el centro de proceso de datos municipal. Datos de partida:

- Al distrito se le ha asignado el bloque **`10.30.16.0/22`** del plan de direccionamiento corporativo.
- Habrá **420 puestos de usuario** (previsión a cuatro años), **90 teléfonos IP**, **20 impresoras multifunción** y **40 cámaras** del sistema de videovigilancia.
- Se necesita además una red separada para la **gestión de los equipos de red** (conmutadores, puntos de acceso y el propio encaminador), con no más de 20 dispositivos.
- La oficina tendrá **un único encaminador** de salida hacia la red corporativa.
- Los puestos se configuran mediante **DHCP**; los servidores, las impresoras y las cámaras, con **dirección fija**.
- El sistema de tramitación de expedientes al que accede la oficina ha sido categorizado como de **categoría MEDIA** conforme al Esquema Nacional de Seguridad.

Se pide un informe de diseño previo a la instalación.

#### Cuestiones

**Cuestión 1 — Plan de direccionamiento (3 puntos).** Diseñe el reparto del bloque `10.30.16.0/22` en subredes empleando **máscara de longitud variable**, justificando el prefijo elegido para cada una. Indique para cada subred la **dirección de red**, el **rango asignable** y la **dirección de difusión**.

**Cuestión 2 — Segmentación y normativa (2 puntos).** Justifique la segmentación propuesta desde el punto de vista del **Esquema Nacional de Seguridad**: qué medida la exige, si es exigible a este sistema y qué refuerzo satisface la solución.

**Cuestión 3 — DHCP en una red segmentada (2 puntos).** El servidor DHCP está en el centro de proceso de datos, no en la oficina. Explique **por qué el diseño no funcionaría sin un elemento adicional**, cuál es ese elemento y en qué equipo se configura. Indique además **qué ocurriría** en un puesto si el servicio fallase.

**Cuestión 4 — Recorrido de un paquete (3 puntos).** Un puesto con dirección `10.30.16.50` accede a `https://sede.madrid.es`, alojada en el centro de proceso de datos. Describa **capa por capa** qué direcciones lleva la primera trama que sale del puesto y qué ocurre con esas direcciones en cada salto hasta el servidor.

#### Solución orientativa

- **C1**: (§6.1) El bloque `10.30.16.0/22` contiene **1.024 direcciones**, de `10.30.16.0` a `10.30.19.255`. Con máscara de longitud variable se asigna a cada subred el tamaño mínimo que la cubre, empezando por la mayor:

| Subred | Necesidad | Prefijo | Direcciones | Asignables | Dirección de red | Rango asignable | Difusión |
|----|----|----|----|----|----|----|----|
| **Puestos de usuario** | 420 | **/23** | 512 | **510** | `10.30.16.0` | `10.30.16.1` — `10.30.17.254` | `10.30.17.255` |
| **Telefonía IP** | 90 | **/25** | 128 | **126** | `10.30.18.0` | `10.30.18.1` — `10.30.18.126` | `10.30.18.127` |
| **Cámaras** | 40 | **/26** | 64 | **62** | `10.30.18.128` | `10.30.18.129` — `10.30.18.190` | `10.30.18.191` |
| **Impresión** | 20 | **/27** | 32 | **30** | `10.30.18.192` | `10.30.18.193` — `10.30.18.222` | `10.30.18.223` |
| **Gestión de red** | 20 | **/27** | 32 | **30** | `10.30.18.224` | `10.30.18.225` — `10.30.18.254` | `10.30.18.255` |

**Justificaciones que se valoran**: (a) 420 puestos **no caben en un `/24`**, que solo da 254 asignables, de ahí el `/23`; (b) 90 teléfonos **no caben en un `/26`** (62), de ahí el `/25`; (c) se han asignado los bloques **por orden de tamaño decreciente** y **alineados**, que es lo que evita solapamientos en la máscara de longitud variable; (d) queda **libre todo el `10.30.19.0/24`**, reserva del 25 % del bloque para crecimiento, lo que es una buena práctica exigible en un diseño a cuatro años. Se valora igualmente que se recuerde que **una dirección de cada subred se consume en la interfaz del encaminador**, que actúa como puerta de enlace predeterminada.

- **C2**: (§9.2) La medida que exige la segmentación es **`mp.com.4` — separación de flujos de información en la red** del anexo II del ENS. Es **exigible** a este sistema: `mp.com.4` **no aplica en categoría BÁSICA**, pero **sí en MEDIA**, donde se exige la medida más **uno** de los refuerzos R1, R2 o R3. La solución propuesta —segmentos implantados con **VLAN**— satisface el **refuerzo R1**, que además obliga a segregar como mínimo **usuarios, servicios y administración**; el diseño lo cumple con holgura al separar cinco segmentos, entre ellos una **VLAN de gestión** propia para los equipos de red. Se valora que se cite el requisito `mp.com.4.2`: **si hay comunicaciones inalámbricas, deben ir en un segmento separado**, lo que obligaría a añadir una VLAN más para la red Wi-Fi de la oficina. Y se valora la observación de que la segmentación cumple una **doble función**: acota la propagación de un incidente y contiene el **tráfico de difusión**, ya que cada VLAN es un dominio de difusión independiente.

&nbsp;

- **C3**: (§8.1) El elemento adicional es el **agente de retransmisión DHCP** (*DHCP relay*). La razón: los mensajes **DISCOVER** y **REQUEST** se emiten **por difusión**, y **la difusión no atraviesa los encaminadores**; sin agente, la petición del puesto moriría en su propia VLAN y nunca alcanzaría el servidor central. El agente se configura **en el encaminador** (o en el conmutador de nivel 3) **en la interfaz de cada VLAN que tenga clientes**, e indica la dirección del servidor: el agente recibe la difusión, la convierte en **unidifusión** dirigida al servidor y le añade la información de la subred de origen para que el servidor sepa de qué ámbito debe entregar la dirección.

**Si el servicio fallase**, el puesto no recibiría oferta y acabaría **autoasignándose una dirección de enlace local `169.254.x.x` (APIPA)**, con la que **solo podría comunicarse dentro de su propio segmento**: no tendría puerta de enlace ni servidores DNS, de modo que no alcanzaría la sede electrónica. Se valora que se distinga este caso del de un puesto que **ya tenía concesión**: ese seguiría funcionando hasta que expirase, intentando renovar al **50 %** del tiempo (T1) y reenlazar al **87,5 %** (T2).

- **C4**: (§3.3, §5.2, §6.4) Recorrido de la primera trama:

| Capa | Contenido |
|----|----|
| **Aplicación** | Petición HTTP dentro de un registro TLS. Antes ha habido una consulta **DNS** para resolver `sede.madrid.es` |
| **Transporte** | Cabecera **TCP** con **puerto origen efímero** (rango 49152-65535) y **puerto destino 443** |
| **Internet** | Cabecera **IPv4** con **origen `10.30.16.50`** y **destino** la dirección del servidor de la sede; campo **Protocolo = 6** |
| **Acceso a la red** | Trama Ethernet con **MAC origen = la del puesto**, **MAC destino = la del encaminador de la oficina** y **EtherType `0x0800`** |

El puesto llega a esa decisión aplicando la **operación Y lógica** entre la dirección de destino y su propia máscara: como el resultado no coincide con su dirección de red, el destino está fuera de su subred y la trama debe ir **a la puerta de enlace predeterminada**. Resuelve la **MAC del encaminador** —no la del servidor— mediante **ARP**.

**En cada salto**: el encaminador **descarta la trama entrante y construye una nueva** para el siguiente enlace, con **direcciones MAC nuevas**; **decrementa el TTL en uno**; **recalcula la suma de comprobación de la cabecera IP**, precisamente porque el TTL ha cambiado; y **no modifica** ni las direcciones IP ni la cabecera TCP.

**La conclusión que se valora** es la formulación de la regla: **las direcciones MAC cambian en cada salto y las direcciones IP no cambian en todo el trayecto** (salvo que hubiera traducción de direcciones, que aquí no la hay porque el destino está dentro de la red corporativa). Es también la razón por la que un encaminador **no tiene capa de transporte** para el tráfico que reenvía: no llega a mirar el puerto 443.

#### Criterios de evaluación

| Cuestión | Puntos | Se valora |
|----|----|----|
| C1 | 3 | Prefijos correctos para las cinco subredes (1,5) · rangos y difusión bien calculados (1) · justificación de VLSM, alineación y reserva de crecimiento (0,5) |
| C2 | 2 | Identificar `mp.com.4` y su denominación exacta (0,75) · aplicabilidad en categoría MEDIA y refuerzo R1 con VLAN (0,75) · segregación mínima de usuarios, servicios y administración, y regla del segmento inalámbrico (0,5) |
| C3 | 2 | Agente de retransmisión y razón (la difusión no atraviesa encaminadores) (1) · dónde se configura (0,5) · consecuencia APIPA y matiz de la concesión vigente (0,5) |
| C4 | 3 | Las cuatro capas con sus direcciones correctas (1,5) · MAC del encaminador y no del servidor, con ARP (0,75) · comportamiento en cada salto, incluidos TTL y suma de comprobación (0,75) |

------------------------------------------------------------------------

#### Preguntas tipo test sobre este caso

##### 1. En el supuesto planteado, ¿qué prefijo corresponde a la subred de los 420 puestos de usuario dentro del bloque 10.30.16.0/22?

- a) Un /24, con 254 direcciones asignables.
- b) Un /23, con 510 direcciones asignables.
- c) Un /22, con 1.022 direcciones asignables.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §6.1

420 puestos no caben en un /24; el /23 es el tamaño mínimo que los cubre, y asignar el /22 entero no dejaría sitio a las demás subredes.

##### 2. ¿Qué prefijo corresponde a la subred de los 90 teléfonos IP?

- a) Un /26, con 62 direcciones asignables.
- b) Un /27, con 30 direcciones asignables.
- c) Un /25, con 126 direcciones asignables.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §6.1

Con máscara de longitud variable se asigna a cada subred el tamaño mínimo que la cubre: 90 teléfonos no caben en un /26 y sí en un /25.

##### 3. La subred de las 40 cámaras es 10.30.18.128/26. ¿Cuál es su dirección de difusión?

- a) 10.30.18.191
- b) 10.30.18.255
- c) 10.30.18.127

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §6.1

Un /26 abarca 64 direcciones: de 10.30.18.128 a 10.30.18.191; la última es la de difusión y el rango asignable va de .129 a .190.

##### 4. Asignadas las cinco subredes por orden de tamaño decreciente, ¿qué parte del bloque queda libre?

- a) Nada: el reparto con máscara variable consume siempre el bloque completo.
- b) Todo el 10.30.19.0/24, un 25 % del bloque reservado para el crecimiento.
- c) Solo las direcciones de red y de difusión de cada una de las cinco subredes.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §6.1

Asignar por orden de tamaño decreciente y alineado evita solapamientos y deja libre un /24 completo, buena práctica en un diseño a cuatro años.

##### 5. ¿Es exigible a esta oficina la medida mp.com.4 del ENS, y qué refuerzo satisface la segmentación con VLAN?

- a) Sí: no aplica en BÁSICA pero sí en MEDIA, y las VLAN satisfacen el R1, que exige separar usuarios, servicios y administración.
- b) No: mp.com.4 solo es exigible a los sistemas de categoría ALTA, y la oficina accede a un sistema de categoría MEDIA.
- c) Sí, pero solo su refuerzo R3, que obliga a separar físicamente cada subred con cableado y conmutadores independientes.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §9.2 (mp.com.4)

En categoría MEDIA se exige mp.com.4 más uno de los refuerzos R1, R2 o R3; el diseño, con cinco segmentos y una VLAN de gestión, cumple el R1 con holgura.

##### 6. Si la oficina dispusiera también de red Wi-Fi, ¿qué exigiría el ENS sobre el diseño de segmentos?

- a) Integrar los equipos inalámbricos en la VLAN de puestos, para que hereden sus mismas reglas.
- b) Nada adicional, porque las redes Wi-Fi quedan fuera del ámbito de mp.com.4.
- c) Añadir un segmento separado para las comunicaciones inalámbricas (mp.com.4.2).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §9.2 (mp.com.4.2)

mp.com.4.2 dispone que, si hay comunicaciones inalámbricas, deben ir en un segmento separado, lo que obligaría a añadir una VLAN más.

##### 7. El servidor DHCP está en el CPD. ¿Por qué el diseño no funcionaría sin un agente de retransmisión configurado en el encaminador?

- a) Porque DHCP usa TCP y el encaminador no reenvía conexiones de transporte.
- b) Porque DISCOVER y REQUEST van por difusión, que no atraviesa encaminadores.
- c) Porque el servidor DHCP solo atiende peticiones de su propia subred IP.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §8.1

Sin agente, la petición moriría en su VLAN; el agente, configurado en la interfaz de cada VLAN con clientes, la convierte en unidifusión al servidor y le indica la subred de origen.

##### 8. Si fallase el servicio DHCP, ¿qué le ocurriría a un puesto que arranca sin concesión previa?

- a) Conservaría la última dirección usada por otro equipo y accedería con normalidad a la sede.
- b) Obtendría una dirección del encaminador, que asume el papel de servidor DHCP de respaldo.
- c) Se autoasignaría una dirección 169.254.x.x y solo podría comunicarse dentro de su propio segmento.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §8.1

Sin oferta, el equipo toma una dirección de enlace local (APIPA), sin puerta de enlace ni DNS; un puesto con concesión vigente seguiría funcionando hasta que expirase.

##### 9. El puesto 10.30.16.50 accede a https://sede.madrid.es, alojada en el CPD. ¿Qué direcciones lleva la primera trama que sale del puesto?

- a) MAC destino del encaminador de la oficina e IP destino del servidor de la sede.
- b) MAC destino del servidor de la sede e IP destino del encaminador de la oficina.
- c) MAC e IP de destino del servidor de la sede, obtenidas ambas mediante una consulta DNS.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §5.2, §6.4

Al ver que el destino está fuera de su subred, el puesto envía la trama a la puerta de enlace, cuya MAC resuelve por ARP; la IP de destino es la del servidor.

##### 10. ¿Qué ocurre con las direcciones y cabeceras del paquete en cada encaminador del trayecto, sin traducción de direcciones?

- a) Cambian las direcciones IP y se mantienen las MAC; el TTL y la suma de comprobación no varían.
- b) Cambian las MAC, se decrementa el TTL y se recalcula la suma de comprobación; las IP no cambian.
- c) Se mantienen las direcciones MAC e IP; el encaminador solo modifica el puerto TCP de destino.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §6.4

El encaminador construye una trama nueva para cada enlace, decrementa el TTL y, por eso, recalcula la suma de comprobación de la cabecera IP; no toca las IP ni la cabecera TCP.

### Caso 2 — Diagnóstico de una incidencia de red recorriendo la pila

#### Enunciado

Un lunes por la mañana, el Centro de Atención a Usuarios del IAM recibe avisos de una oficina de distrito. Los síntomas, tal como los describen los usuarios y los primeros datos recogidos por el técnico, son estos:

1.  Desde **un solo puesto**, el navegador muestra el error «no se encuentra el servidor» al abrir `sede.madrid.es`. Desde ese mismo puesto, el comando `ping 10.10.5.20` —la dirección del servidor de la sede— **responde correctamente**.
2.  Desde **todos los puestos de una planta**, cualquier página web tarda en abrirse **más de treinta segundos**, aunque acaba abriéndose. El `ping` al encaminador responde con tiempos normales.
3.  Desde **un tercer puesto**, la aplicación de expedientes se conecta y muestra la pantalla de inicio, pero al **descargar un documento grande** la conexión se queda colgada indefinidamente. El resto de las funciones responden bien.
4.  Un **cuarto puesto** no tiene conectividad alguna y muestra la dirección `169.254.83.12`.

Se pide un informe de diagnóstico.

#### Cuestiones

**Cuestión 1 — Localización por capas (3 puntos).** Para cada uno de los cuatro síntomas, indique **en qué capa del modelo** se sitúa el problema y cuál es la **causa más probable**, justificando por qué los datos del enunciado descartan las demás.

**Cuestión 2 — El valor diagnóstico del modelo (2 puntos).** Explique por qué en el síntoma 1 el hecho de que **el `ping` funcione y el nombre no resuelva** permite localizar el fallo con precisión, y qué principio del modelo por capas se está aplicando.

**Cuestión 3 — El síntoma 3 en detalle (3 puntos).** Explique el mecanismo exacto que produce el síntoma 3: por qué la conexión **se establece** y solo falla al transferir datos grandes. Indique qué protocolo y qué mensaje concreto están implicados y qué debe corregirse.

**Cuestión 4 — Herramientas (2 puntos).** Indique qué **herramienta o comando** emplearía para confirmar cada uno de los cuatro diagnósticos, y qué esperaría observar en cada caso.

#### Solución orientativa

- **C1**: (§2, §6, §7, §8)

| Síntoma | Capa | Causa más probable | Por qué se descartan las demás |
|----|----|----|----|
| **1** — no resuelve el nombre pero el `ping` a la IP responde | **Aplicación** (capa 7) | Fallo de **resolución DNS** en ese puesto: servidor DNS mal configurado, inalcanzable o registro erróneo en la caché local | Que el `ping` a la dirección IP funcione **prueba que las capas 1 a 3 están sanas**: hay cable, hay trama, hay encaminamiento y hay conectividad IP extremo a extremo. El `ping` usa ICMP, que viaja directamente sobre IP sin pasar por la capa de transporte, así que no prueba TCP ni UDP; pero la causa más probable está por encima: la resolución del nombre |
| **2** — lentitud generalizada en una planta | **Enlace o red** (capas 2 y 3) | **Congestión o error físico** en el enlace ascendente de esa planta: puerto negociado a velocidad o dúplex incorrectos, bucle de capa 2, o saturación del enlace | Es **generalizado en una planta y no en otras**, lo que apunta a un elemento común: el conmutador de planta o su enlace. No es de aplicación, porque afecta a **todas** las aplicaciones |
| **3** — se conecta pero se cuelga al transferir | **Red**, con efecto visible en transporte | **Descubrimiento de la MTU del camino roto**: hay un enlace con MTU menor en el trayecto y los mensajes **ICMP tipo 3 código 4** están bloqueados en un cortafuegos | No es DNS, porque el nombre resuelve; no es de encaminamiento general, porque los paquetes pequeños llegan. El patrón «funciona con paquetes pequeños y falla con grandes» es la firma inequívoca de este fallo |
| **4** — dirección `169.254.83.12` | **Aplicación**, con efecto en red | **No hay servicio DHCP alcanzable**: servidor caído, agente de retransmisión mal configurado, ámbito agotado o puerto del conmutador en la VLAN equivocada | La dirección de **enlace local (APIPA)** es autoasignada por el propio equipo y **solo aparece cuando no hay respuesta DHCP**. Es un diagnóstico casi unívoco |

- **C2**: (§1.1, §8.1) El razonamiento es una aplicación directa del **principio de estratificación**: cada capa **presta un servicio a la superior apoyándose en el inferior**, de modo que **si una capa funciona, todas las que están por debajo funcionan también**. El `ping` es un mensaje **ICMP de solicitud de eco**, es decir, un servicio de **capa 3**: que responda demuestra que la trama sale (capa 2), que el medio transmite (capa 1), que el direccionamiento y el encaminamiento son correctos (capa 3) y que el equipo remoto está vivo. Si con todo eso el navegador no encuentra el servidor, **el fallo está necesariamente por encima**, y lo único que hay entre la capa 3 y la petición HTTP en este escenario es la **resolución de nombres**.

Ese es el **valor diagnóstico del modelo por capas**: convierte un problema abierto en una **búsqueda binaria**. Se valora explicitar el método general —**probar de abajo arriba y detenerse en la primera capa que falla**— y señalar que el mismo razonamiento funciona en sentido inverso: si el `ping` **no** hubiera respondido, no tendría sentido investigar el DNS.

- **C3**: (§5.1, §6.1, §6.3) Mecanismo completo:

1.  El puesto abre la conexión TCP con el **saludo de tres vías**, cuyos segmentos son **pequeños**: caben en cualquier enlace. Por eso la aplicación **se conecta y muestra la pantalla de inicio**.
2.  Al descargar el documento, el servidor empieza a enviar segmentos **de tamaño máximo**, que producen paquetes IP de **1.500 octetos**, la MTU de Ethernet, y normalmente con el bit **DF** (*no fragmentar*) activo.
3.  En algún punto del trayecto hay un enlace de **MTU menor** —un túnel, una VPN, un enlace de operador—. El encaminador de ese punto **no puede fragmentar** porque DF está activo, así que **descarta el paquete** y devuelve al servidor un mensaje **ICMP tipo 3, código 4: destino inaccesible, fragmentación necesaria y DF activo**, que además indica la MTU del siguiente enlace.
4.  Si ese mensaje ICMP **está bloqueado** por un cortafuegos intermedio, el servidor **nunca se entera**: sigue reenviando el mismo paquete grande, que se sigue descartando. La conexión queda establecida pero **sin progresar**: es el llamado **agujero negro de la MTU**.

**Qué debe corregirse**: **permitir el paso del ICMP tipo 3 código 4** en todos los cortafuegos del trayecto, que es la solución correcta. Como paliativos cabe **ajustar el MSS** en el encaminador del túnel o **reducir la MTU** de las interfaces implicadas, pero se valora expresamente señalar que **bloquear todo ICMP es una mala práctica** y que este síntoma es su consecuencia más frecuente.

Se valora también la observación de que **en IPv6 el problema es estructural y no ocasional**: como los encaminadores **no fragmentan nunca**, el descubrimiento de la MTU del camino es el **único** mecanismo disponible, y bloquear el ICMPv6 de «paquete demasiado grande» rompe la conectividad de forma sistemática.

- **C4**: (§6.3, §8.1)

| Síntoma | Herramienta | Qué se espera observar |
|----|----|----|
| **1** | `nslookup` o `dig` sobre el nombre, y `ipconfig /all` o `ip addr` para ver el DNS configurado | La consulta falla o devuelve una dirección incorrecta, mientras que la misma consulta contra otro servidor DNS sí resuelve. Confirma que el problema es de resolución y no de conectividad |
| **2** | Contadores de error y de descartes en el puerto del conmutador; `ping` con muchos paquetes para medir la variación del retardo; en su caso, análisis con un analizador de tráfico | Errores de trama o descartes crecientes en el puerto, o retardos muy variables. Una negociación a semidúplex frente a dúplex completo produce colisiones tardías, que aparecen en los contadores |
| **3** | `ping` con tamaño creciente y bit de no fragmentar activo (`ping -f -l` en Windows, `ping -M do -s` en Linux); `traceroute` | El `ping` funciona hasta cierto tamaño y falla a partir de él, sin devolver el mensaje ICMP correspondiente. El umbral revela la MTU real del camino |
| **4** | `ipconfig /release` e `ipconfig /renew`, con captura de tráfico en el puesto; revisión de la VLAN del puerto y del agente de retransmisión | Se observan los **DISCOVER** repetidos sin **OFFER** de respuesta. Si el puesto está en la VLAN equivocada o falta el agente, la petición no llega al servidor |

#### Criterios de evaluación

| Cuestión | Puntos | Se valora |
|----|----|----|
| C1 | 3 | Capa correcta en los cuatro síntomas (1,5) · causa probable bien identificada (1) · descarte razonado de las alternativas (0,5) |
| C2 | 2 | Identificar ICMP y el carácter de capa 3 del `ping` (0,75) · el principio de que si una capa funciona todas las inferiores funcionan (0,75) · el método de prueba de abajo arriba (0,5) |
| C3 | 3 | Mecanismo completo con los cuatro pasos (1,5) · identificar ICMP tipo 3 código 4 por su nombre (0,75) · corrección propuesta y crítica del bloqueo indiscriminado de ICMP (0,75) |
| C4 | 2 | Herramienta pertinente en los cuatro casos (1) · qué se espera observar en cada una (1) |

------------------------------------------------------------------------

#### Preguntas tipo test sobre este caso

##### 1. En el supuesto planteado, un puesto no abre sede.madrid.es («no se encuentra el servidor»), pero el ping a 10.10.5.20 responde. ¿Dónde está el fallo?

- a) En la capa física, por un cable dañado entre el puesto y la roseta.
- b) En la capa de red, por un error de encaminamiento hacia el servidor.
- c) En la capa de aplicación: la resolución DNS de ese puesto.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §8.1

Si el ping a la IP funciona, cable, trama, encaminamiento y conectividad extremo a extremo están sanos; el problema solo puede estar por encima: la resolución del nombre.

##### 2. ¿Qué principio del modelo por capas permite localizar con precisión ese fallo a partir del ping?

- a) Que si una capa funciona, todas las inferiores funcionan: el ping (ICMP, capa 3) prueba las capas 1 a 3.
- b) Que cada capa es independiente de las demás, de modo que el ping no informa sobre ninguna otra capa.
- c) Que el ping es un servicio de capa 7, igual que el navegador, y por eso prueba la misma ruta que este.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §1.1, §8.1

Es el principio de estratificación: cada capa presta servicio a la superior apoyándose en la inferior. Por eso se prueba de abajo arriba y se detiene la búsqueda en la primera capa que falla.

##### 3. Todos los puestos de una planta tardan más de treinta segundos en abrir cualquier página, y las demás plantas van bien. ¿Dónde apunta el diagnóstico?

- a) Al servidor DNS corporativo, porque la lentitud afecta a la navegación web.
- b) Al conmutador de planta o a su enlace ascendente, que es el elemento común.
- c) A la aplicación de expedientes, porque es la más usada en esa planta.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §8.1

Afecta a todas las aplicaciones de una planta y no de otras: apunta a capas 2 y 3 en el elemento común (velocidad o dúplex mal negociados, bucle o saturación del enlace).

##### 4. La aplicación de expedientes se conecta, pero la descarga de un documento grande se cuelga indefinidamente. ¿Cuál es la causa más probable?

- a) El servidor DNS devuelve una dirección distinta para las descargas de documentos grandes.
- b) El ámbito DHCP se ha agotado y el puesto pierde la dirección al empezar la descarga.
- c) Hay un enlace con MTU menor en el camino y se bloquea el ICMP tipo 3 código 4.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestiones 1 y 3 · §6.3

El encaminador del enlace estrecho descarta el paquete grande con DF activo y avisa con ICMP tipo 3 código 4; si un cortafuegos bloquea ese aviso, el servidor nunca reduce el tamaño: es el agujero negro de la MTU.

##### 5. ¿Por qué, en ese mismo puesto, la conexión llega a establecerse y la pantalla de inicio se muestra?

- a) Porque los segmentos del saludo de tres vías son pequeños y caben en cualquier enlace.
- b) Porque la pantalla de inicio se descarga por UDP, que no está sujeto a la MTU del camino.
- c) Porque el saludo inicial se envía sin cabecera IP y no lo examina ningún cortafuegos.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §6.3, §7.2

El fallo solo aparece cuando el servidor envía segmentos de tamaño máximo (paquetes de 1.500 octetos con DF activo); lo pequeño pasa.

##### 6. ¿Qué corrección es la adecuada para ese fallo?

- a) Bloquear todo el tráfico ICMP en los cortafuegos, para cerrar el paso a los paquetes que se pierden.
- b) Permitir el ICMP tipo 3 código 4 en todos los cortafuegos del trayecto; ajustar el MSS solo como paliativo.
- c) Desactivar el control de congestión de TCP en el servidor, para que reenvíe los segmentos más rápido.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §6.3

Es la solución correcta; ajustar el MSS o reducir la MTU son paliativos. Bloquear todo ICMP es una mala práctica y este síntoma es su consecuencia más frecuente.

##### 7. ¿Por qué ese mismo bloqueo de ICMP sería todavía más grave si el tráfico fuera IPv6?

- a) Porque en IPv6 los encaminadores no fragmentan nunca y el descubrimiento de la MTU es el único mecanismo.
- b) Porque IPv6 fragmenta siempre en cada salto, y el ICMP es necesario para volver a montar los fragmentos.
- c) Porque IPv6 no usa ICMP, y cualquier bloqueo afecta a la resolución de nombres a través del DNS.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §6.2, §6.3

En IPv6 el problema es estructural: bloquear el ICMPv6 «paquete demasiado grande» rompe la conectividad de forma sistemática.

##### 8. El cuarto puesto muestra la dirección 169.254.83.12. ¿Qué indica?

- a) Que el puesto tiene una dirección fija mal tecleada por el técnico.
- b) Que el servidor DNS no ha podido resolver el nombre del propio equipo.
- c) Que no ha recibido respuesta de ningún servicio DHCP alcanzable.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §6.1, §8.1

La dirección de enlace local (APIPA) la autoasigna el equipo solo cuando no hay respuesta DHCP: servidor caído, agente mal configurado, ámbito agotado o puerto en la VLAN equivocada.

##### 9. ¿Qué prueba confirma el diagnóstico del puesto cuya descarga grande se cuelga?

- a) Un ipconfig /renew, que debería mostrar mensajes DISCOVER repetidos sin ninguna oferta.
- b) Un ping con tamaño creciente y el bit de no fragmentar activo, que falla a partir de cierto tamaño.
- c) Un nslookup del nombre de la aplicación contra otro servidor DNS distinto del configurado.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §6.3

Con DF activo (ping -f -l en Windows, ping -M do -s en Linux), el ping funciona hasta cierto tamaño y deja de hacerlo sin devolver el ICMP: el umbral revela la MTU real del camino.

##### 10. ¿Qué herramientas confirman el diagnóstico del primer puesto, que no resuelve sede.madrid.es?

- a) Un traceroute hasta 10.10.5.20, que mostrará el salto en que se pierden los paquetes.
- b) Los contadores de errores del puerto del conmutador al que está conectado el puesto.
- c) nslookup o dig sobre el nombre e ipconfig /all para ver el DNS configurado en el puesto.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §8.1

Si la consulta falla o devuelve una dirección incorrecta y la misma consulta contra otro servidor DNS resuelve, queda confirmado que el problema es de resolución y no de conectividad.

### Caso 3 — Migración a IPv6 y conexión de la red municipal a SARA

#### Enunciado

La dirección del IAM encarga un plan para dos actuaciones que van a acometerse en paralelo:

**(A) Publicación de la sede electrónica por IPv6.** Se ha constatado que un número creciente de ciudadanos accede desde redes móviles que entregan **solo IPv6** a sus usuarios. La sede está hoy publicada únicamente sobre IPv4, tras un balanceador. La red interna del IAM es **solo IPv4** y usa direccionamiento privado con traducción de direcciones hacia internet.

**(B) Conexión de un organismo autónomo municipal a la red SARA.** Un organismo autónomo del Ayuntamiento necesita intercambiar datos con la Administración General del Estado y con una comunidad autónoma. Actualmente sale a internet por la misma salida que el resto de la red municipal, sin ninguna separación.

#### Cuestiones

**Cuestión 1 — Estrategia de migración a IPv6 (3 puntos).** Proponga la estrategia técnica para la actuación (A), justificando la elección frente a las alternativas. Indique **qué hay que hacer en el DNS** y qué **orden de despliegue** seguiría.

**Cuestión 2 — Marco normativo de IPv6 en el sector público (2 puntos).** Cite el **instrumento** que ordena la incorporación de IPv6 en las Administraciones españolas y **dos medidas concretas** que contiene y que afectan a este proyecto. Justifique además, con la normativa administrativa general, **por qué esto no es una decisión meramente técnica**.

**Cuestión 3 — Riesgos de seguridad de la transición (2 puntos).** Enumere los **riesgos específicos** que introduce la actuación (A) y las medidas para mitigarlos.

**Cuestión 4 — Conexión a SARA (3 puntos).** Describa la **arquitectura de conexión** exigida por la normativa para la actuación (B): qué norma la regula, qué papel desempeña cada agente, qué elementos debe contener la conexión y qué medidas del Esquema Nacional de Seguridad se predican de ella.

#### Solución orientativa

- **C1**: (§6.2) **Estrategia: doble pila**, que es el mecanismo recomendado con carácter general. Justificación frente a las alternativas: los **túneles** añaden un punto de fallo, degradan el rendimiento y varios de los automáticos están desaconsejados por motivos de seguridad; la **traducción** (NAT64 y DNS64) rompe el principio extremo a extremo y solo se justifica cuando ya no se dispone de direcciones IPv4, que no es el caso. El **inconveniente** de la doble pila —que **no ahorra direcciones IPv4**— es irrelevante aquí, porque el objetivo no es ahorrar direcciones sino **ser alcanzable** desde redes solo IPv6.

**Actuaciones en el DNS**: publicar un registro **`AAAA`** para `sede.madrid.es` con la dirección IPv6 del balanceador, **manteniendo el registro `A`** existente. A partir de ese momento, un cliente con doble pila obtendrá ambos registros y elegirá según su propia preferencia; un cliente solo IPv6 obtendrá el `AAAA` y podrá conectarse; y un cliente solo IPv4 seguirá funcionando exactamente igual. Se valora advertir de que **publicar el `AAAA` antes de que el servicio esté probado provoca caídas de servicio** para los clientes que prefieran IPv6.

**Orden de despliegue** que se valora:

1.  **Obtener direccionamiento IPv6** (bloque del registro regional o del proveedor) y **diseñar el plan de direccionamiento**, con un `/64` por subred.
2.  Habilitar IPv6 **en la infraestructura perimetral**: encaminador de salida, cortafuegos y balanceador, incluido el registro de actividad.
3.  **Replicar en IPv6 todas las reglas de filtrado** ya existentes en IPv4, antes de publicar nada.
4.  **Probar el servicio por IPv6** con clientes controlados, usando la dirección directamente o un nombre de prueba.
5.  **Publicar el registro `AAAA`** con un **tiempo de vida bajo**, para poder revertir con rapidez.
6.  **Monitorizar** el tráfico por ambas pilas y elevar después el tiempo de vida.
7.  Extender progresivamente la doble pila a la red interna, dejando la conversión del centro de proceso de datos y de los puestos para fases posteriores.

- **C2**: (§9.1) El instrumento es el **Plan de fomento para la incorporación del protocolo IPv6 en España**, aprobado por **Acuerdo de Consejo de Ministros de 29 de abril de 2011** y publicado mediante la **Orden PRE/1716/2011**. Dos medidas que afectan directamente a este proyecto:

1.  La **incorporación de IPv6 en los portales y servicios de la Administración**, que es literalmente la actuación (A), junto con la incorporación de IPv6 en la **red SARA**, que enlaza con la actuación (B).
2.  La **exigencia de soporte de IPv6 como requisito en la contratación pública** de equipamiento y de servicios. Es la medida de mayor alcance práctico, porque **impide seguir adquiriendo el problema**: todo equipo de red, servidor o servicio que se contrate debe soportar IPv6 de forma nativa.

Se valora citar también la **actualización del plan de direccionamiento e interconexión de redes** de las Administraciones como tercera medida pertinente.

**Por qué no es una decisión meramente técnica**: el **artículo 13.a de la Ley 39/2015** reconoce a la ciudadanía el **derecho a comunicarse con las Administraciones por medios electrónicos**, y el **artículo 14** impone la **relación electrónica obligatoria** a determinados sujetos —personas jurídicas, entidades sin personalidad, profesionales colegiados y quienes representen a un obligado—. Si un ciudadano **no puede alcanzar la sede electrónica** desde su red, o si un obligado a relacionarse electrónicamente no puede cumplir su obligación, el problema deja de ser de disponibilidad técnica y pasa a afectar al **ejercicio de un derecho** y al **cumplimiento de un deber legal**. Se valora la conclusión: **la accesibilidad por IPv6 es un requisito de servicio público, no una mejora opcional**.

- **C3**: (§6.2, §9.1) Riesgos específicos y mitigación:

| Riesgo | Descripción | Mitigación |
|----|----|----|
| **Asimetría de filtrado** | El cortafuegos está afinado para IPv4 y **abierto o inexistente para IPv6**: la doble pila duplica la superficie de exposición | **Replicar en IPv6 todas las reglas** antes de habilitar la pila, y auditar la equivalencia. Es el riesgo principal |
| **Pila habilitada sin saberlo** | Los sistemas operativos modernos traen **IPv6 activo por defecto**, con dirección de enlace local. Puede haber tráfico IPv6 en la red aunque «no se use» | Inventariar y **monitorizar** también IPv6; si no se va a usar, deshabilitarlo explícitamente y no solo ignorarlo |
| **Túneles automáticos** | Mecanismos como 6to4, Teredo o ISATAP pueden **atravesar el perímetro encapsulados** y escapar a la inspección | **Deshabilitarlos expresamente** y bloquear en el perímetro el protocolo IP **41** y el tráfico de Teredo si no se emplean |
| **Ceguera de la monitorización** | Los sistemas de detección, la correlación de registros y las listas de bloqueo pueden estar construidos solo para direcciones IPv4 | Extender a IPv6 el **registro de actividad** y la detección de intrusión (`op.mon.1`), asegurando la **base de tiempo común** de `op.exp.8` |
| **Privacidad y trazabilidad** | Las **extensiones de privacidad** hacen que la dirección de un puesto cambie con frecuencia, lo que dificulta atribuir una actuación a un equipo | Definir la política de direccionamiento interno (direcciones estables o DHCPv6 con registro) para preservar la **trazabilidad**, que es una dimensión de seguridad del ENS |

- **C4**: (§9.2) **Norma aplicable**: la **Norma Técnica de Interoperabilidad de requisitos de conexión a la red de comunicaciones de las Administraciones Públicas españolas**, aprobada por **Resolución de 19 de julio de 2011**, dictada al amparo del **Esquema Nacional de Interoperabilidad** (Real Decreto 4/2010), que a su vez tiene su fundamento legal en el **artículo 156 de la Ley 40/2015**.

**Los tres agentes** y su papel en este supuesto:

| Agente | Papel |
|----|----|
| **Órgano gestor de la red** | Administra la conexión, presta soporte permanente y gestiona el portal de la red |
| **Proveedor de acceso** | Administración que actúa como **punto único de conexión** para los organismos que dependen de ella. En este supuesto, **el Ayuntamiento de Madrid es el proveedor de acceso** del organismo autónomo |
| **Órgano usuario final** | El organismo autónomo, que **no se conecta por su cuenta** sino a través de su proveedor de acceso |

**Elementos que debe contener la conexión**:

1.  Un **área de conexión** con arquitectura de **zona desmilitarizada**, delimitada por un **subsistema de seguridad externo** y otro **interno**. Es decir: **no se conecta la red interna a SARA**, sino una zona intermedia controlada entre ambas.
2.  Los **servicios básicos** que el área debe prestar: **DNS**, **correo**, **hora** y **navegación**.
3.  **Cifrado obligatorio** de las comunicaciones que discurren por la red, **mediante túneles**.
4.  **Sujeción al plan de direccionamiento e interconexión de redes**, que impide que el organismo elija libremente su direccionamiento y evita solapamientos con otras Administraciones.
5.  **Coordinación con el CCN-CERT** en materia de seguridad.

**Medidas del ENS que se predican de la conexión** (anexo II del Real Decreto 311/2022):

| Medida | Denominación | Cómo se concreta aquí |
|----|----|----|
| **`mp.com.1`** | Perímetro seguro | Los dos subsistemas de seguridad del área de conexión. Todo el tráfico debe atravesarlos y **todos los flujos deben estar autorizados previamente**. Aplica en **las tres categorías** |
| **`mp.com.2`** | Protección de la confidencialidad | **Redes privadas virtuales cifradas** cuando la comunicación discurre fuera del dominio de seguridad propio, con **algoritmos autorizados por el CCN** desde el nivel MEDIO (refuerzo R1) |
| **`mp.com.3`** | Protección de la integridad y de la autenticidad | Autenticación del extremo remoto y prevención de ataques activos, con registro y activación de los procedimientos de respuesta al detectarlos |
| **`mp.com.4`** | Separación de flujos de información en la red | La propia existencia de la zona desmilitarizada, y la segmentación interna. **No aplica en BÁSICA**; en MEDIA exige uno de los refuerzos R1, R2 o R3 |

**La conclusión que se valora** es de encaminamiento y no solo de seguridad: una vez establecida la conexión, el tráfico dirigido a **otras Administraciones debe entrar por SARA y no salir a internet**, y eso se implanta con **rutas específicas** hacia los prefijos de SARA, más específicas que la ruta por defecto hacia internet. Por la **regla del prefijo más largo**, esas rutas ganan. Se valora igualmente señalar que el organismo **no puede mantener su salida actual indiferenciada**: la normativa exige un punto de conexión con arquitectura propia.

#### Criterios de evaluación

| Cuestión | Puntos | Se valora |
|----|----|----|
| C1 | 3 | Elegir doble pila y justificarla frente a túneles y traducción (1) · registro `AAAA` manteniendo el `A` (0,75) · orden de despliegue con el filtrado antes de publicar y el tiempo de vida bajo (1,25) |
| C2 | 2 | Citar el Plan de fomento con su fecha y su norma de publicación (0,75) · dos medidas concretas pertinentes (0,5) · fundamento en los arts. 13.a y 14 de la Ley 39/2015 (0,75) |
| C3 | 2 | Asimetría de filtrado como riesgo principal (0,75) · al menos otros dos riesgos con su mitigación (0,75) · conexión con las medidas del ENS de monitorización y trazabilidad (0,5) |
| C4 | 3 | Norma correcta con su fecha y su encaje en el ENI y el art. 156 de la Ley 40/2015 (0,75) · los tres agentes, identificando al Ayuntamiento como proveedor de acceso (0,75) · zona desmilitarizada, servicios básicos, cifrado y plan de direccionamiento (0,75) · las medidas `mp.com` con su denominación exacta y la conclusión sobre las rutas específicas (0,75) |

#### Preguntas tipo test sobre este caso

##### 1. En el supuesto planteado, ¿qué estrategia técnica conviene para publicar la sede electrónica por IPv6?

- a) Doble pila, porque el objetivo es ser alcanzable desde redes solo IPv6, no ahorrar direcciones IPv4.
- b) Traducción NAT64 y DNS64, porque es el mecanismo recomendado con carácter general por el IETF.
- c) Túneles automáticos como 6to4 o Teredo, porque no exigen modificar la infraestructura perimetral.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §6.2

La doble pila es el mecanismo recomendado; los túneles añaden un punto de fallo y algunos están desaconsejados por seguridad, y la traducción rompe el principio extremo a extremo y solo se justifica sin direcciones IPv4.

##### 2. ¿Qué debe hacerse en el DNS para que la sede sea alcanzable por IPv6?

- a) Sustituir el registro A por un registro AAAA con la dirección IPv6 del balanceador.
- b) Publicar un registro AAAA con la IPv6 del balanceador, manteniendo el registro A.
- c) Publicar un registro PTR con la IPv6 del balanceador y dejar el A sin cambios.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §6.2

Con ambos registros, un cliente solo IPv6 usa el AAAA, uno solo IPv4 sigue igual y uno con doble pila elige según su preferencia.

##### 3. ¿Qué debe hacerse antes de publicar el registro AAAA?

- a) Nada: el AAAA puede publicarse primero y el filtrado IPv6 ajustarse cuando llegue tráfico.
- b) Convertir a doble pila toda la red interna, el CPD y los puestos de las oficinas de distrito.
- c) Replicar en IPv6 las reglas de filtrado y probar el servicio con clientes controlados.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §6.2

Publicar el AAAA antes de probar el servicio provoca caídas para los clientes que prefieren IPv6; después se publica con tiempo de vida bajo, y la red interna se convierte en fases posteriores.

##### 4. ¿Qué instrumento ordena la incorporación de IPv6 en las Administraciones españolas?

- a) El Plan de fomento para la incorporación del protocolo IPv6 en España, de 29 de abril de 2011 (Orden PRE/1716/2011).
- b) La Norma Técnica de Interoperabilidad de conexión a la red SARA, aprobada por Resolución de 19 de julio de 2011.
- c) El Real Decreto 311/2022 del Esquema Nacional de Seguridad, en su medida mp.com.4 de separación de flujos.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §9.1

Fue aprobado por Acuerdo de Consejo de Ministros de 29 de abril de 2011 y publicado mediante la Orden PRE/1716/2011.

##### 5. ¿Qué medida de ese plan tiene mayor alcance práctico para que el Ayuntamiento no siga «adquiriendo el problema»?

- a) La traducción NAT64 obligatoria en todas las sedes electrónicas de la Administración.
- b) La supresión de IPv4 en todas las redes públicas a partir de la fecha de aprobación del plan.
- c) La exigencia de soporte de IPv6 como requisito en la contratación pública de equipos y servicios.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §9.1

Si todo equipo, servidor o servicio que se contrate debe soportar IPv6 de forma nativa, el parque deja de crecer con equipamiento incompatible.

##### 6. ¿Por qué publicar la sede por IPv6 no es una decisión meramente técnica?

- a) Porque la Ley 11/2022 obliga a todos los operadores a ofrecer a sus clientes únicamente conectividad IPv6.
- b) Porque afecta al derecho a relacionarse electrónicamente y a la obligación de ciertos sujetos (arts. 13.a y 14 Ley 39/2015).
- c) Porque el ENS prohíbe publicar solo por IPv4 los servicios electrónicos de los sistemas de categoría MEDIA.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §9.1 (arts. 13.a y 14 Ley 39/2015)

Si un ciudadano no alcanza la sede desde su red, o un obligado no puede cumplir su obligación electrónica, el problema afecta al ejercicio de un derecho y al cumplimiento de un deber legal.

##### 7. ¿Cuál es el riesgo principal de seguridad que introduce la doble pila en la sede?

- a) La asimetría de filtrado: un cortafuegos afinado para IPv4 y abierto o inexistente para IPv6.
- b) El agotamiento de las direcciones IPv4 públicas, que la doble pila consume el doble de rápido.
- c) La pérdida del registro A, que deja la sede inaccesible para los ciudadanos que usan solo IPv4.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §6.2

La doble pila duplica la superficie de exposición: hay que replicar todas las reglas en IPv6 antes de habilitarla y auditar la equivalencia.

##### 8. ¿Cómo se mitiga el riesgo de túneles automáticos como 6to4, Teredo o ISATAP que atraviesan el perímetro sin inspección?

- a) Publicando un registro AAAA con un tiempo de vida bajo, para poder revertir con rapidez.
- b) Deshabilitándolos y bloqueando en el perímetro el protocolo IP 41 y el tráfico de Teredo.
- c) Activando las extensiones de privacidad de IPv6 en todos los puestos de la red interna.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §6.2

Si no se emplean, deben deshabilitarse expresamente y bloquearse en el perímetro, porque pueden encapsular tráfico IPv6 que escapa a la inspección.

##### 9. En la conexión del organismo autónomo a la red SARA, ¿qué papel desempeña el Ayuntamiento de Madrid?

- a) El de órgano usuario final, que se conecta a SARA por su cuenta e independientemente del organismo.
- b) El de órgano gestor de la red, que administra SARA y presta su soporte permanente a todas las AAPP.
- c) El de proveedor de acceso: punto único de conexión para el organismo autónomo que depende de él.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §9.2

Conforme a la Norma Técnica de Interoperabilidad de requisitos de conexión a la red de las AAPP (Resolución de 19 de julio de 2011), el organismo autónomo es usuario final y se conecta a través de su proveedor de acceso.

##### 10. Establecida la conexión a SARA, ¿cómo se garantiza que el tráfico hacia otras Administraciones entre por SARA y no salga a internet?

- a) Con rutas específicas hacia los prefijos de SARA, que ganan a la ruta por defecto por la regla del prefijo más largo.
- b) Con una ruta por defecto hacia SARA, de modo que todo el tráfico del organismo, también el de internet, pase por ella.
- c) Con la misma salida a internet de siempre, porque SARA solo cambia el cifrado y no el encaminamiento del tráfico.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §6.4, §9.2

Cuando varias rutas encajan, se aplica la de prefijo más largo; además, el organismo no puede mantener su salida indiferenciada: la conexión exige un área propia con arquitectura de zona desmilitarizada.

## Fuentes

### Tier 1 — Normas, especificaciones y normativa aplicable

| ID | Referencia |
|----|----|
| `[ISO7498]` | **ISO/IEC 7498-1:1994**. *Information technology — Open Systems Interconnection — Basic Reference Model: The Basic Model*. Segunda edición (15 de noviembre de 1994), que sustituye a la de 1984 e incorpora expresamente el tratamiento del modo **no orientado a conexión**. Define las **siete capas**, los conceptos de entidad, servicio, protocolo, punto de acceso al servicio (**SAP**) y unidad de datos, y los principios de estratificación. |
| `[X200]` | **Recomendación UIT-T X.200 (07/1994)**. *Tecnología de la información — Interconexión de sistemas abiertos — Modelo de referencia básico: el modelo básico*. **Texto idéntico** al de ISO/IEC 7498-1: ISO y UIT-T publicaron el mismo modelo en paralelo. Es la razón por la que el modelo OSI se cita indistintamente como norma ISO o como recomendación de la UIT. |
| `[ISO7498-2]` | **ISO/IEC 7498-2:1989** (UIT-T X.800). *Arquitectura de seguridad OSI*. Define los cinco **servicios de seguridad** (autenticación, control de acceso, confidencialidad, integridad y no repudio) y los **mecanismos** que los realizan, y los sitúa en las capas del modelo. |
| `[ISO7498-3]` | **ISO/IEC 7498-3:1997** (UIT-T X.650). *Denominación y direccionamiento en OSI*. Y **ISO/IEC 7498-4:1989** (UIT-T X.700), *Marco de gestión OSI*. Completan el modelo básico con el direccionamiento y con la gestión de sistemas. |
| `[RFC1122]` | IETF. **[RFC 1122](https://www.rfc-editor.org/rfc/rfc1122)**: *Requirements for Internet Hosts — Communication Layers* (octubre de 1989). Documento que **fija oficialmente los cuatro niveles** de la arquitectura de Internet (enlace, internet, transporte y aplicación) y los requisitos de un equipo terminal. Junto con la **[RFC 1123](https://www.rfc-editor.org/rfc/rfc1123)** (capa de aplicación) constituye el par de normas de referencia para los *hosts*. |
| `[RFC1812]` | IETF. **[RFC 1812](https://www.rfc-editor.org/rfc/rfc1812)**: *Requirements for IP Version 4 Routers* (1995). Equivalente de la [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122) para los **encaminadores**: reglas de reenvío, tratamiento de opciones, TTL y generación de mensajes ICMP. |
| `[RFC791]` | IETF. **[RFC 791](https://www.rfc-editor.org/rfc/rfc791)**: *Internet Protocol* (septiembre de 1981), **STD 5**. Cabecera **IPv4** campo a campo, direccionamiento de 32 bits, fragmentación y reensamblado, y opciones. Actualizado por la [RFC 6864](https://www.rfc-editor.org/rfc/rfc6864) (campo de identificación) y por la [RFC 2474](https://www.rfc-editor.org/rfc/rfc2474) (**DSCP**, que redefine el antiguo campo de tipo de servicio). |
| `[RFC950]` | IETF. **[RFC 950](https://www.rfc-editor.org/rfc/rfc950)**: *Internet Standard Subnetting Procedure* (1985), y **[RFC 1519](https://www.rfc-editor.org/rfc/rfc1519)** / **[RFC 4632](https://www.rfc-editor.org/rfc/rfc4632)**: *Classless Inter-Domain Routing (CIDR)*. Máscara de subred, notación de prefijo `/n`, agregación de rutas y abandono del direccionamiento por clases. |
| `[RFC1918]` | IETF. **[RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)**: *Address Allocation for Private Internets*, **BCP 5**. Reserva de `10.0.0.0/8`, `172.16.0.0/12` y `192.168.0.0/16`. Complementada por la **[RFC 6890](https://www.rfc-editor.org/rfc/rfc6890)** (registro consolidado de direcciones de uso especial), la **[RFC 3927](https://www.rfc-editor.org/rfc/rfc3927)** (enlace local `169.254.0.0/16`) y la **[RFC 6598](https://www.rfc-editor.org/rfc/rfc6598)** (`100.64.0.0/10`, NAT de nivel de operador). |
| `[RFC3022]` | IETF. **[RFC 3022](https://www.rfc-editor.org/rfc/rfc3022)**: *Traditional IP Network Address Translator (NAT)*, y **[RFC 2663](https://www.rfc-editor.org/rfc/rfc2663)** (terminología) y **[RFC 4787](https://www.rfc-editor.org/rfc/rfc4787)** (requisitos de comportamiento para UDP). Traducción de direcciones y de puertos (**NAPT**), sus efectos sobre la conectividad extremo a extremo y su relación con el agotamiento de IPv4. |
| `[RFC8200]` | IETF. **[RFC 8200](https://www.rfc-editor.org/rfc/rfc8200)**: *Internet Protocol, Version 6 (IPv6) Specification* (julio de 2017), **STD 86**. Cabecera fija de **40 octetos**, cabeceras de extensión, prohibición de la fragmentación en tránsito y tratamiento del límite de saltos. Sustituye a la [RFC 2460](https://www.rfc-editor.org/rfc/rfc2460). |
| `[RFC4291]` | IETF. **[RFC 4291](https://www.rfc-editor.org/rfc/rfc4291)**: *IP Version 6 Addressing Architecture*. Notación, tipos de dirección (**unidifusión**, **multidifusión** y **anidifusión** o *anycast*), identificador de interfaz de 64 bits, direcciones de enlace local `fe80::/10`, bucle local `::1`, no especificada `::` y direcciones de multidifusión `ff00::/8`. Complementada por la **[RFC 4193](https://www.rfc-editor.org/rfc/rfc4193)** (direcciones locales únicas `fc00::/7`) y la **[RFC 3849](https://www.rfc-editor.org/rfc/rfc3849)** (prefijo de documentación `2001:db8::/32`). |
| `[RFC4213]` | IETF. **[RFC 4213](https://www.rfc-editor.org/rfc/rfc4213)**: *Basic Transition Mechanisms for IPv6 Hosts and Routers*. **Doble pila** y **túneles configurados**. Con la **[RFC 6144](https://www.rfc-editor.org/rfc/rfc6144)** (marco de traducción IPv4/IPv6), la **[RFC 6146](https://www.rfc-editor.org/rfc/rfc6146)** (**NAT64**) y la **[RFC 6147](https://www.rfc-editor.org/rfc/rfc6147)** (**DNS64**), y la **[RFC 7059](https://www.rfc-editor.org/rfc/rfc7059)** (comparativa de mecanismos de tunelización). |
| `[RFC792]` | IETF. **[RFC 792](https://www.rfc-editor.org/rfc/rfc792)**: *Internet Control Message Protocol* (1981), **STD 5**. Mensajes de error y de consulta de **ICMP** para IPv4: destino inaccesible, tiempo excedido, redirección, eco y respuesta de eco. **Número de protocolo IP 1**. |
| `[RFC4443]` | IETF. **[RFC 4443](https://www.rfc-editor.org/rfc/rfc4443)**: *Internet Control Message Protocol (ICMPv6)*, **STD 89**. **Número de protocolo IP 58**. Añade a los mensajes clásicos el **paquete demasiado grande**, imprescindible porque IPv6 no fragmenta en tránsito, y sirve de soporte al descubrimiento de vecinos. |
| `[RFC826]` | IETF. **[RFC 826](https://www.rfc-editor.org/rfc/rfc826)**: *An Ethernet Address Resolution Protocol* (**ARP**), **STD 37**. Resolución de dirección IPv4 a dirección MAC mediante petición por difusión y respuesta por unidifusión, y funcionamiento de la caché ARP. |
| `[RFC4861]` | IETF. **[RFC 4861](https://www.rfc-editor.org/rfc/rfc4861)**: *Neighbor Discovery for IP version 6* (**ND**), y **[RFC 4862](https://www.rfc-editor.org/rfc/rfc4862)**: *IPv6 Stateless Address Autoconfiguration* (**SLAAC**). Los cinco mensajes de ND (solicitud y anuncio de encaminador, solicitud y anuncio de vecino, y redirección), la detección de direcciones duplicadas (**DAD**) y la autoconfiguración sin servidor. |
| `[RFC9293]` | IETF. **[RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)**: *Transmission Control Protocol (TCP)* (**agosto de 2022**), **STD 7**. **Sustituye a la histórica [RFC 793](https://www.rfc-editor.org/rfc/rfc793)** e incorpora las correcciones dispersas en las [RFC 879](https://www.rfc-editor.org/rfc/rfc879), 2873, 6093, 6429, 6528 y 6691. Cabecera, máquina de estados, saludo de tres vías, control de flujo por ventana deslizante y cierre ordenado. |
| `[RFC5681]` | IETF. **[RFC 5681](https://www.rfc-editor.org/rfc/rfc5681)**: *TCP Congestion Control*. Los cuatro algoritmos clásicos: **arranque lento**, **evitación de congestión**, **retransmisión rápida** y **recuperación rápida**. Con la **[RFC 6298](https://www.rfc-editor.org/rfc/rfc6298)** (cálculo del temporizador de retransmisión), la **[RFC 7323](https://www.rfc-editor.org/rfc/rfc7323)** (escalado de ventana y marcas de tiempo) y la **[RFC 2018](https://www.rfc-editor.org/rfc/rfc2018)** (acuse selectivo, **SACK**). |
| `[RFC768]` | IETF. **[RFC 768](https://www.rfc-editor.org/rfc/rfc768)**: *User Datagram Protocol* (agosto de 1980), **STD 6**. Las **tres páginas** que definen UDP: cabecera de **ocho octetos** con puerto origen, puerto destino, longitud y suma de comprobación. |
| `[RFC1034]` | IETF. **[RFC 1034](https://www.rfc-editor.org/rfc/rfc1034)** y **[RFC 1035](https://www.rfc-editor.org/rfc/rfc1035)**: *Domain Names — Concepts and Facilities* / *Implementation and Specification*, **STD 13**. Espacio de nombres jerárquico, zonas, delegación, servidores autoritativos y recursivos, tipos de registro y formato del mensaje DNS. Con la **[RFC 4033](https://www.rfc-editor.org/rfc/rfc4033)-4035** (**DNSSEC**) y la **[RFC 8484](https://www.rfc-editor.org/rfc/rfc8484)** (**DNS sobre HTTPS**). |
| `[RFC2131]` | IETF. **[RFC 2131](https://www.rfc-editor.org/rfc/rfc2131)**: *Dynamic Host Configuration Protocol* (**DHCP**), y **[RFC 2132](https://www.rfc-editor.org/rfc/rfc2132)** (opciones). Intercambio **DORA**, concesión con tiempo de vida, renovación al 50 % (**T1**) y reenlace al 87,5 % (**T2**). Para IPv6, **[RFC 8415](https://www.rfc-editor.org/rfc/rfc8415)** (**DHCPv6**). |
| `[RFC9110]` | IETF. **[RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)-9114**: *HTTP Semantics*, *HTTP Caching*, *HTTP/1.1*, *HTTP/2* y *HTTP/3*. Semántica de HTTP y sus versiones de transporte; **HTTP/3** se apoya en **QUIC** (**[RFC 9000](https://www.rfc-editor.org/rfc/rfc9000)**) sobre UDP. Desarrollo completo en el **Tema 35**. |
| `[RFC959]` | IETF. **[RFC 959](https://www.rfc-editor.org/rfc/rfc959)**: *File Transfer Protocol* (**FTP**), **STD 9**. Doble conexión de control (**puerto 21**) y de datos (**puerto 20** en modo activo), modos activo y pasivo. Con la **[RFC 4217](https://www.rfc-editor.org/rfc/rfc4217)** (**FTPS**) y la **[RFC 913](https://www.rfc-editor.org/rfc/rfc913)** / **[RFC 1350](https://www.rfc-editor.org/rfc/rfc1350)** (**TFTP**, sobre UDP/69). |
| `[RFC5321]` | IETF. **[RFC 5321](https://www.rfc-editor.org/rfc/rfc5321)**: *Simple Mail Transfer Protocol* (**SMTP**) y **[RFC 5322](https://www.rfc-editor.org/rfc/rfc5322)** (formato del mensaje). Con la **[RFC 1939](https://www.rfc-editor.org/rfc/rfc1939)** (**POP3**), la **[RFC 9051](https://www.rfc-editor.org/rfc/rfc9051)** (**IMAP4rev2**), la **[RFC 8314](https://www.rfc-editor.org/rfc/rfc8314)** (uso obligatorio de TLS: puertos **465** y **993**/**995**) y la **[RFC 6409](https://www.rfc-editor.org/rfc/rfc6409)** (**envío de mensajes en el puerto 587**). |
| `[RFC3411]` | IETF. **[RFC 3411](https://www.rfc-editor.org/rfc/rfc3411)-3418**: *Simple Network Management Protocol version 3* (**SNMPv3**), **STD 62**. Arquitectura, modelo de seguridad basado en usuario (**USM**) y control de acceso por vistas (**VACM**). Con la **[RFC 1157](https://www.rfc-editor.org/rfc/rfc1157)** (SNMPv1) y la **[RFC 1213](https://www.rfc-editor.org/rfc/rfc1213)** (**MIB-II**). Puertos **UDP 161** y **162**. |
| `[RFC5905]` | IETF. **[RFC 5905](https://www.rfc-editor.org/rfc/rfc5905)**: *Network Time Protocol Version 4* (**NTP**). Jerarquía de estratos, algoritmos de selección y disciplina del reloj. **Puerto UDP 123**. |
| `[RFC4271]` | IETF. **[RFC 4271](https://www.rfc-editor.org/rfc/rfc4271)**: *A Border Gateway Protocol 4 (BGP-4)*; **[RFC 2328](https://www.rfc-editor.org/rfc/rfc2328)**: *OSPF Version 2*; **[RFC 5340](https://www.rfc-editor.org/rfc/rfc5340)**: *OSPF for IPv6*; **[RFC 2453](https://www.rfc-editor.org/rfc/rfc2453)**: *RIP Version 2*; **RFC 5340** y **[RFC 7868](https://www.rfc-editor.org/rfc/rfc7868)** (**EIGRP**). Protocolos de encaminamiento interior y exterior, y distinción entre **vector distancia** y **estado del enlace**. |
| `[RFC1035P]` | IETF. **[RFC 1035](https://www.rfc-editor.org/rfc/rfc1035)**, sección 4.2, y **[RFC 7766](https://www.rfc-editor.org/rfc/rfc7766)**. DNS emplea **UDP/53** para las consultas ordinarias y **TCP/53** cuando la respuesta excede el tamaño admitido o para las **transferencias de zona**. Justifica el ejemplo canónico de protocolo que usa los dos transportes. |
| `[RFC2474]` | IETF. **[RFC 2474](https://www.rfc-editor.org/rfc/rfc2474)**: *Definition of the Differentiated Services Field (DS Field) in the IPv4 and IPv6 Headers*, y **[RFC 3168](https://www.rfc-editor.org/rfc/rfc3168)** (**ECN**). Redefinición del octeto de tipo de servicio en **6 bits de DSCP + 2 bits de ECN**. |
| `[IEEE802]` | **IEEE 802.3** (Ethernet), **IEEE 802.1Q** (**VLAN** y etiquetado), **IEEE 802.1D** (puentes y árbol de expansión), **IEEE 802.1X** (control de acceso a la red basado en puerto) e **IEEE 802.11** (redes inalámbricas). El comité **IEEE 802** normaliza las capas 1 y 2 y **divide la capa de enlace en dos subcapas**: **LLC** (802.2) y **MAC**. |
| `[IANA]` | **Internet Assigned Numbers Authority (IANA)**, bajo la **ICANN**. Registros oficiales de **números de protocolo IP**, **puertos y nombres de servicio** (con los tres rangos: bien conocidos, registrados y dinámicos), **EtherType**, tipos de mensaje ICMP y asignación de bloques de direcciones a los **cinco registros regionales (RIR)**, entre ellos **RIPE NCC** para Europa. |
| `[ENS]` | [Real Decreto **311/2022, de 3 de mayo**](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191), por el que se regula el **Esquema Nacional de Seguridad** (BOE núm. 106, de 4 de mayo de 2022). Medidas del anexo II citadas y verificadas literalmente: **`mp.com.1`** perímetro seguro, **`mp.com.2`** protección de la confidencialidad, **`mp.com.3`** protección de la **integridad y de la autenticidad**, **`mp.com.4`** **separación de flujos de información en la red** con sus refuerzos R1 (VLAN), R2 (VPN), R3 (medios físicos separados) y R4 (puntos de interconexión); y `op.mon.1`, `op.mon.2` y `op.exp.8`. Art. 156 de la [Ley 40/2015](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566) como fundamento legal. Desarrollo completo en el **Tema 39**. |
| `[ENI]` | [Real Decreto **4/2010, de 8 de enero**](https://www.boe.es/buscar/act.php?id=BOE-A-2010-1331), por el que se regula el **Esquema Nacional de Interoperabilidad**. Su **artículo 13** regula la **red de comunicaciones de las Administraciones públicas españolas** y remite a la norma técnica que fija los requisitos de conexión. Dictado al amparo del art. 156 de la [Ley 40/2015](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566). |
| `[NTI-RED]` | **Resolución de 19 de julio de 2011**, de la Secretaría de Estado para la Función Pública, por la que se aprueba la **Norma Técnica de Interoperabilidad de requisitos de conexión a la red de comunicaciones de las Administraciones Públicas españolas** ([BOE-A-2011-13173](https://www.boe.es/buscar/act.php?id=BOE-A-2011-13173), de 30 de julio de 2011). Establece las condiciones de acceso a la **red SARA**, los **agentes** (órgano gestor, **proveedores de acceso** y órganos usuarios finales), el **área de conexión** con arquitectura de zona desmilitarizada, los **servicios básicos** que debe prestar (DNS, correo, hora y navegación), el **cifrado obligatorio** de las comunicaciones y la sujeción al **plan de direccionamiento e interconexión de redes**. |
| `[IPV6-PLAN]` | **[Orden PRE/1716/2011](https://www.boe.es/buscar/doc.php?id=BOE-A-2011-10786), de 9 de junio**, por la que se publica el **Acuerdo de Consejo de Ministros de 29 de abril de 2011**, por el que se aprueba el **Plan de fomento para la incorporación del protocolo IPv6 en España**. Diez líneas de actuación; entre ellas, la incorporación de IPv6 en los **portales de la Administración**, la actualización del **plan de direccionamiento e interconexión de redes** administrativas, la **incorporación de IPv6 en la red SARA** y su exigencia como **requisito en la contratación pública** de equipamiento y servicios. |
| `[L39-2015]` | [Ley **39/2015, de 1 de octubre**](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565), del Procedimiento Administrativo Común. Art. **13.a** (derecho a comunicarse con las Administraciones por medios electrónicos), art. **14** (obligación de relación electrónica de determinados sujetos) y art. **16** (registro electrónico). Fundamento del carácter **crítico** de la disponibilidad de la red municipal. |
| `[L40-2015]` | [Ley **40/2015, de 1 de octubre**](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566), de Régimen Jurídico del Sector Público. Art. **155** (transmisión de datos entre Administraciones), art. **156** (Esquema Nacional de Interoperabilidad y Esquema Nacional de Seguridad) y art. **157** (reutilización de sistemas y aplicaciones). Es el **fundamento legal directo** del ENI y del ENS. |

------------------------------------------------------------------------

### Tier 2 — Manuales canónicos y documentación técnica de referencia

| ID | Referencia |
|----|----|
| `[TANENBAUM]` | Tanenbaum, A. S.; Feamster, N.; Wetherall, D. *Computer Networks*, 6.ª ed. Pearson. Manual de referencia universal en la materia. De él proceden la exposición didáctica del modelo híbrido de cinco capas y la crítica clásica al modelo OSI (mala sincronización, mala tecnología, malas implantaciones y mala política). |
| `[KUROSE]` | Kurose, J. F.; Ross, K. W. *Computer Networking: A Top-Down Approach*, 8.ª ed. Pearson. Enfoque descendente, tratamiento del principio del **reloj de arena** y de la ubicación de la complejidad en los extremos. |
| `[STEVENS]` | Stevens, W. R.; Fall, K. R. *TCP/IP Illustrated, Volume 1: The Protocols*, 2.ª ed. Addison-Wesley. Referencia clásica para el detalle de las cabeceras, las máquinas de estados y el comportamiento real observado con analizadores de tráfico. |
| `[COMER]` | Comer, D. E. *Internetworking with TCP/IP, Volume One*, 6.ª ed. Pearson. Exposición canónica del concepto de **red virtual** y de la relación entre direccionamiento lógico y físico. |
| `[SALTZER]` | Saltzer, J. H.; Reed, D. P.; Clark, D. D. *End-to-End Arguments in System Design* (1984). Artículo fundacional del **principio extremo a extremo**, que explica por qué la fiabilidad se sitúa en la capa de transporte de los equipos terminales y no en la red. |
| `[CLARK88]` | Clark, D. D. *The Design Philosophy of the DARPA Internet Protocols* (SIGCOMM, 1988). Enumera y **jerarquiza los objetivos** originales de la arquitectura de Internet, empezando por la supervivencia de la comunicación ante fallos de la red. |
| `[RFC1958]` | IETF. **[RFC 1958](https://www.rfc-editor.org/rfc/rfc1958)**: *Architectural Principles of the Internet*. Formulación breve de los principios de diseño: extremo a extremo, simplicidad, ausencia de estado en la red y evolución por consenso. Con la **[RFC 2026](https://www.rfc-editor.org/rfc/rfc2026)** (proceso de normalización del IETF y niveles de madurez de un documento). |
| `[CCN-STIC-807]` | Centro Criptológico Nacional. **CCN-STIC-807**: *Criptología de empleo en el ENS*, y guías de la serie **500/600** de bastionado de dispositivos de red. Determinan los algoritmos autorizados en los túneles y protocolos seguros exigidos por `mp.com.2` y `mp.com.3`. |
| `[CCN-STIC-811]` | Centro Criptológico Nacional. **CCN-STIC-811**: *Interconexión en el ENS*, y **CCN-STIC-408**: *Seguridad perimetral*. Criterios de conexión entre dominios de seguridad distintos, previstos por el propio `mp.com.1`. |
| `[MITRE]` | MITRE Corporation. **ATT&CK for Enterprise**, tácticas de descubrimiento y de movimiento lateral, y catálogo **CWE**. Citado únicamente para nombrar los ataques que aprovechan debilidades de diseño de los protocolos (suplantación de ARP, envenenamiento de la caché DNS, inundación de SYN). |
| `[RIPE]` | **RIPE NCC**. Registro regional de Internet para Europa, Oriente Medio y Asia Central: asignación de bloques de direcciones y de números de sistema autónomo, y política de **agotamiento de IPv4** (asignaciones limitadas a un `/24` desde noviembre de 2019). |
| `[APNIC-STATS]` | **APNIC Labs / Google IPv6 Statistics**. Medición continua del porcentaje de usuarios que alcanzan los servicios por IPv6. En **abril de 2026** la medición de Google alcanzó por primera vez el **50 %**, mientras APNIC Labs situaba la capacidad IPv6 global en torno al **42 %**; la diferencia se explica por la metodología de ponderación. **Dato volátil: reverificar antes de cada convocatoria.** |
| `[WIRESHARK]` | Fundación Wireshark. Documentación del analizador de protocolos de referencia, y de las utilidades `ping`, `traceroute`/`tracert`, `ipconfig`/`ip`, `nslookup`/`dig`, `netstat`/`ss` y `arp`. Base de los ejercicios de lectura de trazas. |

------------------------------------------------------------------------

### Tier 3 — Contexto administrativo municipal (no citado como contenido técnico)

| ID | Referencia |
|----|----|
| `[BOAM]` | Temario oficial de la convocatoria, **BOAM 10.032**. Enunciado literal del tema 34 y de los temas colindantes 30, 33, 35, 36, 37 y 39, empleado para delimitar fronteras. |
| `[ROGA]` | Reglamento Orgánico del Gobierno y de la Administración del Ayuntamiento de Madrid, de 31 de mayo de 2004, y [Reglamento Orgánico 6/2021](https://www.bocm.es/boletin/CM_Orden_BOCM/2021/06/16/BOCM-20210616-62.PDF) de los Distritos. Estructura de Áreas y de los **21 distritos**, usada como contexto de los casos prácticos. |
| `[IAM]` | Informática del Ayuntamiento de Madrid (**IAM**), organismo autónomo. Prestador de los servicios TIC municipales y responsable de la red corporativa y de su conexión a SARA. Contexto de los casos prácticos. |
| `[TRANSP]` | Portal de transparencia del Ayuntamiento de Madrid y sede electrónica `sede.madrid.es`. Contexto de los ejemplos de servicios municipales accesibles desde internet. |

------------------------------------------------------------------------

### Nota sobre el uso de las fuentes

1.  **Las cifras y los formatos de cabecera proceden siempre de la especificación**, no de manuales ni de resúmenes. Cuando un dato aparece en el contenido —el número de octetos de una cabecera, el número de protocolo IP, un puerto, un tipo de mensaje ICMP— la referencia inline apunta al RFC o a la norma ISO/IEEE que lo fija.
2.  **Los RFC citados están vigentes en su nivel de madurez actual.** Se ha comprobado en particular que la especificación de TCP en vigor es la **[RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)** (2022) y no la [RFC 793](https://www.rfc-editor.org/rfc/rfc793), error frecuente en temarios no actualizados, y que la de IPv6 es la **[RFC 8200](https://www.rfc-editor.org/rfc/rfc8200)** (2017) y no la [RFC 2460](https://www.rfc-editor.org/rfc/rfc2460).
3.  **Lo normativo español se cita del BOE.** Ni el ENS ni el ENI ni la NTI de conexión a SARA se han tomado de fuentes secundarias.
4.  **Los datos de adopción de IPv6 son volátiles por naturaleza.**
