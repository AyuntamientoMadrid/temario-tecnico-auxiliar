# Test del tema 35. Internet: arquitectura de red

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-35.html>

## Batería de preguntas

### 1. ¿Qué fecha se cita convencionalmente como el nacimiento de Internet tal como se entiende hoy?

- a) El 29 de octubre de 1969, cuando ARPANET conectó sus primeros nodos
- b) El 1 de enero de 1983, cuando ARPANET abandonó NCP y adoptó TCP/IP
- c) El 6 de agosto de 1991, cuando Berners-Lee publicó el proyecto de la World Wide Web

**Respuesta correcta:** b) · **Referencia:** §1.1.1 [RFC801]

Ese cambio obligatorio en una única fecha (<em>flag day</em>) es lo que crea una familia de protocolos común capaz de unir redes heterogéneas. 1969 es el nacimiento de <strong>ARPANET</strong>, que funcionaba con NCP, y 1991 es la publicación de la <strong>Web</strong>, un servicio posterior.

### 2. Señale la afirmación correcta sobre la relación entre Internet y la World Wide Web.

- a) La Web es uno de los servicios que se ejecutan sobre Internet, junto al correo, el DNS o el acceso remoto
- b) Internet y la Web son denominaciones equivalentes del mismo sistema
- c) Internet es el conjunto de páginas enlazadas y la Web es la infraestructura de comunicación

**Respuesta correcta:** a) · **Referencia:** §1.1.1 [FNC]

Internet es la <strong>infraestructura</strong> (la red de redes con TCP/IP) y la Web es <strong>un servicio</strong> que apareció casi veinte años después. La opción C invierte exactamente los términos.

### 3. ¿Cuál fue el objetivo declarado del proyecto ARPANET?

- a) Garantizar las comunicaciones militares ante un ataque nuclear
- b) Ofrecer un servicio comercial de intercambio de mensajes entre universidades
- c) Compartir recursos de computación escasos y caros entre centros de investigación

**Respuesta correcta:** c) · **Referencia:** §1.1.1 [LEINER]

La resistencia a fallos era una propiedad deseable de la conmutación de paquetes, no la finalidad del proyecto; los propios protagonistas han desmentido por escrito el mito nuclear. El uso comercial no llegó hasta la privatización de NSFNET, en 1995.

### 4. En 1978 se produjo una decisión de diseño determinante para la arquitectura actual. ¿Cuál?

- a) La sustitución de los IMP por encaminadores comerciales
- b) La creación del sistema de nombres de dominio
- c) La separación del protocolo TCP en dos: IP para el direccionamiento y TCP para la fiabilidad

**Respuesta correcta:** c) · **Referencia:** §1.1.1 [CERF-KAHN]

Esa división permitió que sobre IP pudieran construirse transportes distintos, y es la razón de que exista <strong>UDP</strong>. El DNS llegó en 1983-1987.

### 5. ¿Qué tres invenciones combinó la propuesta original de la World Wide Web?

- a) HTML, URI/URL y HTTP
- b) HTML, TCP/IP y DNS
- c) XML, FTP y SMTP

**Respuesta correcta:** a) · **Referencia:** §1.1.2 [W3C]

Un lenguaje de marcado con enlaces, un identificador global de recursos y un protocolo de transferencia. TCP/IP y el DNS son <strong>anteriores</strong> a la Web y pertenecen a la infraestructura, no a la propuesta de Berners-Lee.

### 6. En la clasificación habitual de la evolución de la Web, ¿qué caracteriza a la Web 3.0 en el sentido que le dio el W3C?

- a) La descentralización mediante cadenas de bloques y contratos inteligentes
- b) La Web Semántica: datos con significado procesable por máquinas mediante RDF, OWL y SPARQL
- c) La generación de contenidos por los propios usuarios en redes sociales y wikis

**Respuesta correcta:** b) · **Referencia:** §1.1.2 [W3C]

La opción A describe la llamada <strong>Web3</strong>, que es una acepción distinta y posterior; la C describe la <strong>Web 2.0</strong>. Distinguir Web 3.0 de Web3 es una trampa habitual.

### 7. ¿Qué organismo gestiona la asignación de bloques de direcciones IP y de números de sistema autónomo a los registros regionales?

- a) La función IANA, ejercida desde 2016 por PTI, filial de ICANN
- b) El IETF, a través de sus grupos de trabajo
- c) La Internet Society (ISOC)

**Respuesta correcta:** a) · **Referencia:** §1.2.1 [ICANN]

La cadena es <strong>IANA → RIR → LIR (operador) → usuario final</strong>. El IETF escribe los estándares y la ISOC es el paraguas institucional; ninguno reparte direcciones.

### 8. ¿A qué registro regional de Internet pertenece España?

- a) ARIN
- b) APNIC
- c) RIPE NCC

**Respuesta correcta:** c) · **Referencia:** §1.2.1 [RIPE]

Cubre Europa, Oriente Medio y Asia Central, con sede en los Países Bajos. ARIN cubre Norteamérica y APNIC la región Asia-Pacífico.

### 9. Señale la afirmación correcta sobre el reparto de competencias entre organismos.

- a) El W3C es el organismo que estandariza el protocolo HTTP
- b) El IETF estandariza HTTP y TLS, mientras que el W3C estandariza HTML y CSS
- c) El Foro de Gobernanza de Internet (IGF) adopta decisiones vinculantes sobre la raíz del DNS

**Respuesta correcta:** b) · **Referencia:** §1.2.1 [IETF]

Aunque HTTP sea «el protocolo de la Web», es un estándar <strong>del IETF</strong>. Y el IGF es un foro <strong>de diálogo</strong> auspiciado por la ONU, sin capacidad normativa.

### 10. Un documento se publica como Internet-Draft del IETF. ¿Qué consecuencia tiene ese estado?

- a) No es un estándar y caduca a los seis meses si no se actualiza, por lo que no puede citarse como referencia normativa
- b) Es un estándar provisional de obligado cumplimiento durante seis meses
- c) Equivale a un RFC de categoría <em>Informational</em> con número asignado

**Respuesta correcta:** a) · **Referencia:** §1.2.2 [RFC-ED]

Solo al final del proceso —adopción por el grupo de trabajo, última llamada y aprobación del IESG— se publica como <strong>RFC</strong> con número definitivo.

### 11. ¿Qué ocurre cuando el IETF necesita corregir el contenido de un RFC ya publicado?

- a) Se publica una nueva revisión con el mismo número y una letra de versión
- b) El RFC Editor edita el documento original y anota la fecha del cambio
- c) Se publica un RFC nuevo que obsoleta o actualiza al anterior, porque el publicado es inmutable

**Respuesta correcta:** c) · **Referencia:** §1.2.2 [RFC-ED]

Es la regla básica de la serie. Por eso HTTP/1.1, especificado en el RFC 2616, pasó por los RFC 723x y hoy está en los <strong>RFC 9110-9112</strong>.

### 12. El modelo TCP/IP y el modelo OSI se corresponden de la siguiente manera:

- a) Ambos tienen siete capas con distinta denominación
- b) La capa de aplicación de TCP/IP equivale a las capas de aplicación, presentación y sesión de OSI
- c) La capa de acceso a red de TCP/IP equivale únicamente a la capa física de OSI

**Respuesta correcta:** b) · **Referencia:** §2.1.1 [RFC1122]

TCP/IP tiene <strong>cuatro</strong> capas frente a las <strong>siete</strong> de OSI, y su capa de acceso a red absorbe <strong>dos</strong>: enlace de datos y física.

### 13. ¿Cuál es la unidad de datos (PDU) propia de la capa de internet o de red?

- a) El paquete o datagrama IP
- b) La trama
- c) El segmento

**Respuesta correcta:** a) · **Referencia:** §2.1.1 [RFC1122]

La <strong>trama</strong> es la PDU de la capa de enlace y el <strong>segmento</strong> la de TCP (la de UDP se denomina datagrama). En la capa de aplicación se habla de mensaje.

### 14. Durante el encaminamiento de un paquete a través de varios encaminadores:

- a) Cambian las direcciones IP de origen y destino, y se conservan las direcciones MAC
- b) Se conservan tanto las direcciones IP como las MAC hasta el destino final
- c) Cambian las direcciones MAC en cada salto y se conservan las direcciones IP de extremo a extremo

**Respuesta correcta:** c) · **Referencia:** §2.1.2 [RFC1122]

Las direcciones MAC son locales a cada enlace. La única excepción a la conservación de las IP es la presencia de un <strong>NAT</strong>, cuya función es precisamente reescribirlas.

### 15. Respecto de la fragmentación de paquetes, IPv6 se diferencia de IPv4 en que:

- a) Elimina por completo la posibilidad de fragmentar
- b) Solo el nodo origen puede fragmentar; los encaminadores intermedios no lo hacen
- c) Fragmenta siempre en el encaminador de salida de la red local

**Respuesta correcta:** b) · **Referencia:** §2.1.2 [RFC8200]

El origen descubre la MTU del camino con <em>Path MTU Discovery</em>, y si un paquete no cabe se genera un mensaje ICMPv6 de «paquete demasiado grande». La fragmentación no desaparece: cambia de responsable.

### 16. ¿Qué es un sistema autónomo (AS)?

- a) Un conjunto de redes bajo una misma administración que presenta hacia el exterior una política de encaminamiento única
- b) Un encaminador capaz de funcionar sin configuración manual
- c) Una red local aislada de Internet por un cortafuegos

**Respuesta correcta:** a) · **Referencia:** §2.2.1 [RFC4271]

Se identifica con un <strong>ASN</strong> de 32 bits asignado por la IANA a través de los RIR, y se relaciona con los demás mediante <strong>BGP</strong>.

### 17. Señale la afirmación correcta sobre BGP.

- a) Es un protocolo de encaminamiento interior que optimiza el número de saltos
- b) Es el único protocolo de encaminamiento exterior de Internet, funciona sobre TCP/179 y decide por política
- c) Es un protocolo de estado de enlace que sustituye a OSPF dentro del sistema autónomo

**Respuesta correcta:** b) · **Referencia:** §2.2.1 [RFC4271]

BGP-4 es un protocolo de <strong>vector de caminos</strong>. RIP, OSPF, IS-IS y EIGRP son protocolos <strong>interiores</strong> (IGP) y sí optimizan métricas técnicas.

### 18. ¿Qué diferencia el tránsito del <em>peering</em> entre operadores?

- a) El tránsito es gratuito y el <em>peering</em> se factura por volumen intercambiado
- b) Ambos dan acceso a la totalidad de Internet, y solo se diferencian en la tecnología del enlace
- c) El tránsito se paga y da acceso a todo Internet; el <em>peering</em> suele ser gratuito y solo alcanza al otro AS y a sus clientes

**Respuesta correcta:** c) · **Referencia:** §2.2.1 [ESPANIX]

Los puntos neutros (<strong>IXP</strong>), como ESPANIX o DE-CIX Madrid, son la infraestructura donde el <em>peering</em> se realiza de forma masiva, con el efecto de reducir costes y latencia.

### 19. ¿Qué son las direcciones del rango 100.64.0.0/10 definido en el RFC 6598?

- a) El espacio compartido reservado para el NAT a gran escala del operador (CGNAT)
- b) Un tercer rango de direcciones privadas de uso interno, equivalente a las del RFC 1918
- c) El rango asignado a los servidores raíz del DNS

**Respuesta correcta:** a) · **Referencia:** §2.2.2 [RFC6598]

Su consecuencia práctica más relevante es que <strong>varios abonados comparten una misma IP pública</strong>, de modo que para identificar a un usuario ya no basta con la dirección y la hora: hace falta también el <strong>puerto de origen</strong>.

### 20. Señale la afirmación correcta sobre IPv6.

- a) Utiliza direcciones de 64 bits y mantiene la difusión (<em>broadcast</em>) de IPv4
- b) Utiliza direcciones de 128 bits, tiene cabecera fija de 40 bytes y sustituye la difusión por multidifusión y anycast
- c) Utiliza direcciones de 128 bits y conserva la suma de control de la cabecera para mayor fiabilidad

**Respuesta correcta:** b) · **Referencia:** §2.2.2 [RFC8200]

Además <strong>elimina la suma de control</strong> de la cabecera —se delega en las capas superior e inferior— y sustituye ARP por el protocolo de descubrimiento de vecinos (<strong>NDP</strong>).

### 21. Una organización necesita que sus equipos, que solo hablan IPv6, accedan a servicios que solo están publicados en IPv4. ¿Qué mecanismo procede?

- a) Ninguno: basta con activar IPv6 en el encaminador, porque ambos protocolos son compatibles
- b) Un túnel 6in4 entre los dos extremos
- c) Una traducción con NAT64 y DNS64

**Respuesta correcta:** c) · **Referencia:** §2.2.2 [RFC6146]

Los túneles sirven para transportar <strong>IPv6 a través de</strong> una zona IPv4, no para que un nodo solo-IPv6 hable con uno solo-IPv4. Y la opción A es falsa: los dos protocolos son <strong>incompatibles</strong>, y siempre hace falta doble pila, túnel o traducción.

### 22. En la resolución de un nombre de dominio, ¿qué tipo de consulta lanza el cliente a su resolutor?

- a) Una consulta recursiva: el resolutor asume el trabajo de obtener la respuesta final
- b) Una consulta iterativa, que el cliente repite contra la raíz, el TLD y el servidor autoritativo
- c) Una transferencia de zona, que le entrega los registros del dominio

**Respuesta correcta:** a) · **Referencia:** §2.2.3 [RFC1034]

Las <strong>iterativas</strong> son las que hace el propio resolutor contra los servidores autoritativos. La transferencia de zona (AXFR) es una operación entre servidores, que además debe estar restringida.

### 23. ¿Por qué existen exactamente trece identidades de servidor raíz del DNS?

- a) Porque son las trece organizaciones autorizadas por la ONU para operar la raíz
- b) Por una limitación histórica: la lista completa debía caber en un único datagrama UDP de 512 bytes
- c) Porque el protocolo DNS reserva cuatro bits para identificarlos

**Respuesta correcta:** b) · **Referencia:** §2.2.3 [ICANN]

La restricción se superó con <strong>EDNS0</strong>, pero el número se mantiene por compatibilidad. Lo que sí crece es el número de <strong>instancias físicas</strong>: más de 2.000 en 2026, gracias a <strong>anycast</strong>.

### 24. ¿Qué registro DNS indica qué autoridades de certificación pueden emitir certificados para un dominio?

- a) El registro TXT
- b) El registro SRV
- c) El registro CAA

**Respuesta correcta:** c) · **Referencia:** §2.2.3 [RFC8659]

Es una medida barata y muy eficaz para una organización pública: impide que una AC distinta de la contratada emita un certificado válido para el dominio municipal. El registro TXT da soporte a SPF, DKIM y DMARC, y el SRV publica servicio, protocolo y puerto.

### 25. Señale la afirmación correcta sobre DNSSEC.

- a) Firma digitalmente las respuestas y aporta autenticidad e integridad, pero no confidencialidad
- b) Cifra las consultas DNS entre el cliente y el resolutor, impidiendo que un tercero sepa qué sitios se visitan
- c) Sustituye a DNS sobre TLS y a DNS sobre HTTPS, que quedan obsoletos donde se implanta

**Respuesta correcta:** a) · **Referencia:** §2.2.3 [RFC4033]

El cifrado del transporte lo aportan <strong>DoT</strong> (TCP/853) y <strong>DoH</strong> (HTTPS/443), que en cambio <strong>no</strong> garantizan la autenticidad del dato de la zona. Son mecanismos <strong>complementarios</strong>.

### 26. El DNS emplea el puerto 53. ¿En qué casos utiliza TCP en lugar de UDP?

- a) Nunca: el DNS es un protocolo exclusivamente UDP
- b) Solo cuando el cliente lo solicita expresamente en la configuración del sistema
- c) Cuando la respuesta excede el tamaño admisible y, siempre, en las transferencias de zona

**Respuesta correcta:** c) · **Referencia:** §2.2.3 [RFC1035]

La respuesta truncada se marca con el bit <strong>TC</strong> y el cliente reintenta por TCP. Las transferencias <strong>AXFR</strong> e <strong>IXFR</strong> van siempre por TCP y deben restringirse: una AXFR abierta entrega el mapa completo de la organización.

### 27. ¿Qué protocolo se utiliza para enviar un mensaje de correo electrónico desde el cliente hacia el servidor y entre servidores?

- a) IMAP
- b) SMTP
- c) POP3

**Respuesta correcta:** b) · **Referencia:** §3.1.1 [RFC5321]

Es el protocolo de <strong>envío y tránsito</strong>. POP3 e IMAP son protocolos de <strong>acceso al buzón</strong>: sirven para recoger, no para enviar. Un cliente de correo necesita configurados los dos tipos: uno de salida y uno de entrada.

### 28. Un empleado municipal consulta el correo desde el ordenador de la oficina y desde el móvil, y necesita ver en ambos el mismo estado de las carpetas. ¿Qué protocolo de acceso procede?

- a) IMAP, porque mantiene los mensajes en el servidor y sincroniza carpetas y estado
- b) POP3, porque descarga los mensajes y libera espacio en el servidor
- c) SMTP con autenticación, configurado en los dos dispositivos

**Respuesta correcta:** a) · **Referencia:** §3.1.1 [RFC9051]

POP3, en su comportamiento por defecto, <strong>descarga y borra</strong>, de modo que cada dispositivo acabaría con una copia distinta. SMTP no sirve para consultar el buzón.

### 29. ¿Qué puerto se emplea para el envío de correo desde el cliente al servidor (<em>submission</em>) con STARTTLS?

- a) El 25
- b) El 993
- c) El 587

**Respuesta correcta:** c) · **Referencia:** §3.1.1 [RFC8314]

El <strong>25</strong> queda para el tránsito entre servidores y el <strong>465</strong> para el envío con TLS implícito. El <strong>993</strong> es IMAP sobre TLS, que es acceso al buzón, no envío.

### 30. Señale la afirmación correcta sobre SPF, DKIM y DMARC.

- a) Los tres cifran el contenido del mensaje de extremo a extremo
- b) SPF autoriza servidores emisores, DKIM firma criptográficamente el mensaje y DMARC exige el alineamiento y fija la política ante el fallo
- c) DKIM sustituye a SPF, que quedó obsoleto tras la publicación del RFC 9989

**Respuesta correcta:** b) · **Referencia:** §3.1.1 [RFC9989]

Los tres se publican como registros <strong>TXT en el DNS</strong> y ninguno cifra el contenido: para eso están S/MIME o PGP. DMARC fue reeditado en mayo de 2026 por los RFC 9989, 9990 y 9991, sin que ello afecte a la vigencia de SPF.

### 31. En una transferencia FTP en modo activo:

- a) El servidor abre la conexión de datos hacia el cliente desde su puerto 20, lo que suele bloquear el cortafuegos del cliente
- b) El cliente abre las dos conexiones, la de control y la de datos
- c) Se emplea una única conexión TCP para control y datos

**Respuesta correcta:** a) · **Referencia:** §3.1.2 [RFC959]

Por eso el modo habitual hoy es el <strong>pasivo</strong> (comando <code>PASV</code>), en el que es el cliente quien abre ambas conexiones. FTP usa siempre <strong>dos</strong> canales: control en el 21 y datos.

### 32. Señale la afirmación correcta sobre SFTP y FTPS.

- a) Son dos nombres del mismo protocolo: FTP con cifrado TLS
- b) SFTP es un subsistema de SSH que usa el puerto 22, mientras que FTPS es FTP envuelto en TLS
- c) SFTP es FTP sobre TLS en el puerto 990 y FTPS es una extensión de SSH

**Respuesta correcta:** b) · **Referencia:** §3.1.2 [RFC4251]

Es la confusión más frecuente del epígrafe: <strong>SFTP no tiene ninguna relación con FTP</strong> pese al nombre, y por eso funciona con un solo canal y sin los problemas de cortafuegos del modo activo.

### 33. ¿Cuál de estas capas NO forma parte de la arquitectura del protocolo SSH?

- a) La capa de transporte, que cifra y autentica al servidor
- b) La capa de conexión, que multiplexa canales
- c) La capa de presentación, que negocia la codificación de los datos

**Respuesta correcta:** c) · **Referencia:** §3.2.1 [RFC4251]

SSH se estructura en <strong>tres</strong> capas: transporte, autenticación de usuario y conexión. La «capa de presentación» pertenece al modelo OSI, no a SSH.

### 34. Al conectarse por primera vez a un servidor SSH, el cliente muestra la huella de la clave del servidor y pide confirmación. ¿Qué modelo de confianza aplica y qué implica un cambio posterior de esa huella?

- a) Confianza en el primer uso: si la huella cambia después, el cliente aborta la conexión porque puede haber un ataque de intermediario
- b) Confianza en una autoridad de certificación: si la huella cambia, basta con aceptar el nuevo certificado
- c) Confianza delegada en el servidor DNS: el cambio de huella indica que se ha actualizado el registro A

**Respuesta correcta:** a) · **Referencia:** §3.2.1 [RFC4251]

La huella se guarda en <code>known_hosts</code>. El aviso puede deberse a una reinstalación legítima del servidor, pero <strong>nunca debe ignorarse sin comprobarlo</strong>.

### 35. El intercambio DHCP se resume en el acrónimo DORA. ¿Cuál es su secuencia correcta?

- a) Discover, Offer, Renew, Acknowledge
- b) Discover, Offer, Request, Acknowledge
- c) Demand, Offer, Request, Assign

**Respuesta correcta:** b) · **Referencia:** §3.2.2 [RFC2131]

El cliente descubre en difusión, uno o varios servidores ofrecen, el cliente solicita formalmente una oferta —también en difusión, para que los demás retiren la suya— y el servidor confirma la concesión. La renovación posterior se intenta al <strong>50 %</strong> de la concesión.

### 36. ¿Qué puertos utiliza DHCP en IPv4?

- a) TCP 67 en el cliente y TCP 68 en el servidor
- b) UDP 546 en el servidor y UDP 547 en el cliente
- c) UDP 67 en el servidor y UDP 68 en el cliente

**Respuesta correcta:** c) · **Referencia:** §3.2.2 [RFC2131]

Los puertos <strong>546 y 547</strong> corresponden a <strong>DHCPv6</strong> (547 servidor y 546 cliente), reeditado en enero de 2026 por el RFC 9915, que es además <strong>STD 102</strong>.

### 37. En una red IPv6 en la que se exige poder determinar qué equipo tenía cada dirección en cada momento, ¿qué opción de configuración es la adecuada?

- a) DHCPv6 con estado, porque mantiene un registro central de las concesiones
- b) SLAAC, porque cada equipo se construye su dirección a partir del prefijo anunciado
- c) Es indiferente: ambas mantienen registro de las direcciones asignadas

**Respuesta correcta:** a) · **Referencia:** §3.2.2 [RFC9915]

<strong>SLAAC</strong> es <em>sin estado</em>: el encaminador anuncia el prefijo y no lleva registro de quién toma qué dirección, lo que dificulta la <strong>trazabilidad</strong> exigida por el ENS. Si se usa SLAAC, hay que complementarlo vigilando la tabla de vecinos.

### 38. ¿Cuál es la especificación vigente del protocolo HTTP?

- a) El RFC 2616, de 1999
- b) La serie RFC 7230 a 7235, de 2014
- c) La serie RFC 9110 a 9114, de junio de 2022

**Respuesta correcta:** c) · **Referencia:** §4.1.1 [RFC9110]

El RFC 2616 fue sustituido por la serie 723x y esta por la actual, que además <strong>separa la semántica de la sintaxis</strong> de cada versión: RFC 9110 (semántica, STD 97), 9111 (caché), 9112 (HTTP/1.1), 9113 (HTTP/2) y 9114 (HTTP/3).

### 39. Que HTTP sea un protocolo «sin estado» significa que:

- a) Cierra la conexión TCP después de cada recurso transferido
- b) El servidor no recuerda por sí mismo nada de las peticiones anteriores: cada una se interpreta de forma independiente
- c) No admite autenticación de usuarios

**Respuesta correcta:** b) · **Referencia:** §4.1.1 [RFC9110]

No hay que confundirlo con «sin conexión»: desde <strong>HTTP/1.1</strong> las conexiones son <strong>persistentes</strong> por defecto, y aun así el protocolo sigue siendo sin estado. El estado de la aplicación se construye con cookies, sesiones o tokens.

### 40. ¿Qué aportó HTTP/1.1 respecto de HTTP/1.0?

- a) Conexiones persistentes por defecto y la cabecera Host obligatoria, que hace posible el alojamiento virtual
- b) La codificación binaria de los mensajes y la multiplexación de corrientes
- c) El transporte sobre QUIC y el cifrado obligatorio

**Respuesta correcta:** a) · **Referencia:** §4.1.2 [RFC9112]

La codificación binaria y la multiplexación llegaron con <strong>HTTP/2</strong>, y el transporte sobre QUIC con <strong>HTTP/3</strong>.

### 41. HTTP/2 introdujo la multiplexación de corrientes sobre una única conexión. ¿Qué problema NO llegó a resolver?

- a) La compresión de las cabeceras repetidas
- b) El bloqueo de cabecera de línea en el transporte: la pérdida de un segmento TCP detiene todas las corrientes
- c) La necesidad de abrir varias conexiones por dominio para descargar recursos en paralelo

**Respuesta correcta:** b) · **Referencia:** §4.1.2 [RFC9113]

HTTP/2 sí resolvió el bloqueo <strong>en la capa de aplicación</strong> y sí comprimió cabeceras con <strong>HPACK</strong>. El bloqueo del transporte solo desaparece con <strong>HTTP/3</strong>, porque QUIC gestiona cada corriente de forma independiente.

### 42. HTTP/3 se apoya en QUIC. Señale la afirmación correcta.

- a) QUIC es una variante de TCP optimizada para la web, definida en el RFC 9114
- b) HTTP/3 puede funcionar en claro sobre UDP si el servidor así lo configura
- c) QUIC se ejecuta sobre UDP, integra TLS 1.3 en su propio establecimiento y por eso HTTP/3 va siempre cifrado

**Respuesta correcta:** c) · **Referencia:** §4.1.2 [RFC9000]

QUIC está definido en el <strong>RFC 9000</strong> (el 9114 es HTTP/3) y reimplementa en espacio de usuario la fiabilidad que TCP ofrece en el núcleo. <strong>No existe un HTTP/3 en claro</strong>.

### 43. ¿Qué ventaja aporta QUIC a un usuario que pasa de la red Wi-Fi a la red móvil en mitad de una descarga?

- a) La migración de conexión: como esta se identifica por un identificador propio y no por la cuádrupla IP y puerto, la sesión se conserva
- b) La retransmisión selectiva, que recupera los paquetes perdidos durante el cambio de red
- c) Ninguna: el cambio de red obliga siempre a reiniciar la conexión

**Respuesta correcta:** a) · **Referencia:** §4.1.2 [RFC9000]

Es una de las dos ventajas más citadas de QUIC, junto con el <strong>0-RTT</strong> en la reanudación, que solo debe emplearse con peticiones idempotentes por el riesgo de repetición.

### 44. Señale la afirmación correcta sobre los métodos HTTP.

- a) POST es idempotente porque siempre produce el mismo recurso
- b) GET, HEAD, OPTIONS y TRACE son seguros e idempotentes; PUT y DELETE son idempotentes pero no seguros
- c) DELETE no es idempotente, porque al repetirlo el servidor devuelve un código de error distinto

**Respuesta correcta:** b) · **Referencia:** §4.2.1 [RFC9110]

<strong>Seguro</strong> significa que no pretende modificar el estado del servidor; <strong>idempotente</strong>, que repetir la petición produce el mismo efecto. La opción C confunde el <strong>código de respuesta</strong> con el <strong>efecto</strong>, que es lo que define la idempotencia. <code>POST</code> y <code>PATCH</code> no son ni seguros ni idempotentes.

### 45. Una aplicación devuelve 401 en lugar de 403. ¿Qué está indicando?

- a) Que el recurso solicitado no existe en el servidor
- b) Que el usuario está autenticado pero carece de permisos sobre el recurso
- c) Que el usuario no está autenticado o sus credenciales no son válidas

**Respuesta correcta:** c) · **Referencia:** §4.2.1 [RFC9110]

El <strong>403 Forbidden</strong> es el caso contrario: identidad acreditada pero <strong>sin autorización</strong>, de modo que volver a identificarse no serviría de nada. El «no existe» es el <strong>404</strong>.

### 46. Un formulario de la sede electrónica envía datos personales. ¿Qué afirmación es correcta?

- a) Con POST los datos viajan en el cuerpo y no quedan escritos en la URL, pero solo HTTPS garantiza su confidencialidad
- b) POST cifra el contenido del formulario, por lo que no es necesario HTTPS
- c) Con GET los datos viajan cifrados en la cadena de consulta

**Respuesta correcta:** a) · **Referencia:** §4.2.1 [RFC9110]

<strong>POST no cifra nada</strong>. La cadena de consulta de un <code>GET</code> queda registrada en los <em>logs</em> del servidor y de los intermediarios, y en el historial del navegador: por eso nunca deben ponerse datos sensibles en la URL.

### 47. ¿Qué atributo de una cookie impide que sea accesible desde JavaScript y, con ello, mitiga su robo mediante secuencias de órdenes en sitios cruzados?

- a) Secure
- b) SameSite
- c) HttpOnly

**Respuesta correcta:** c) · **Referencia:** §4.2.2 [RFC6265]

<strong>Secure</strong> limita el envío a conexiones HTTPS —protege frente a la interceptación en red— y <strong>SameSite</strong> controla el envío en peticiones de origen cruzado, mitigando la falsificación de petición (<strong>CSRF</strong>). Los tres protegen frente a amenazas distintas y deben combinarse.

### 48. Una página de la sede muestra datos personales del ciudadano y se accede desde un puesto compartido. ¿Qué directiva de caché procede?

- a) Cache-Control: no-cache, porque prohíbe almacenar la respuesta
- b) Cache-Control: no-store, junto con private, porque prohíbe almacenar la respuesta en cualquier caché
- c) Cache-Control: max-age=0, porque equivale a no guardar nada

**Respuesta correcta:** b) · **Referencia:** §4.2.2 [RFC9111]

La trampa está en <code>no-cache</code>, que <strong>sí permite almacenar</strong> la respuesta y solo obliga a <strong>revalidarla</strong> antes de reutilizarla.

### 49. ¿Cuál es la situación de SSL y de las distintas versiones de TLS en 2026?

- a) SSL 2.0 y 3.0 están prohibidos, TLS 1.0 y 1.1 se declararon obsoletos por el RFC 8996, y siguen vigentes TLS 1.2 y TLS 1.3
- b) SSL 3.0 sigue admitiéndose por compatibilidad con navegadores antiguos
- c) Solo TLS 1.3 está admitido; TLS 1.2 quedó prohibido al publicarse el RFC 9846

**Respuesta correcta:** a) · **Referencia:** §5.1.1 [RFC9846]

El <strong>RFC 9846</strong> (julio de 2026) reedita TLS 1.3 y obsoleta las especificaciones anteriores, incluida la del RFC 5246, pero <strong>no prohíbe TLS 1.2</strong>: unifica la especificación y añade requisitos para sus implementaciones.

### 50. ¿Cuál es el subprotocolo de TLS que encapsula a todos los demás?

- a) El protocolo Handshake, porque es el primero en ejecutarse
- b) El protocolo Alert, porque puede interrumpir la sesión en cualquier momento
- c) El protocolo Record, porque fragmenta, cifra y protege la integridad de todo lo que transportan los demás

**Respuesta correcta:** c) · **Referencia:** §5.1.1 [RFC9846]

El <strong>Handshake</strong> es el que negocia los algoritmos, autentica mediante certificado y acuerda las claves, pero viaja <strong>dentro</strong> del Record, igual que Alert, Change Cipher Spec y los datos de aplicación.

### 51. Señale la afirmación correcta sobre TLS 1.3.

- a) Mantiene el intercambio de claves RSA estático por motivos de compatibilidad
- b) Exige confidencialidad directa, admite solo cifrado autenticado AEAD y completa el saludo en una vuelta (1-RTT)
- c) Elimina por completo el uso de RSA, que ya no puede emplearse ni para firmar

**Respuesta correcta:** b) · **Referencia:** §5.1.1 [RFC9846]

La trampa está en la opción C: TLS 1.3 elimina RSA <strong>como método de intercambio de claves</strong>, pero RSA <strong>sigue admitido para la firma</strong> del certificado. También suprime la renegociación y la compresión.

### 52. ¿Qué consecuencia tiene que TLS 1.3 imponga la confidencialidad directa (<em>forward secrecy</em>)?

- a) Que comprometer en el futuro la clave privada del servidor no permite descifrar el tráfico capturado en el pasado
- b) Que el servidor puede descifrar en cualquier momento las sesiones antiguas para auditarlas
- c) Que ya no es necesario el certificado del servidor, porque las claves se generan en el cliente

**Respuesta correcta:** a) · **Referencia:** §5.1.1 [RFC9846]

Se consigue porque el acuerdo de claves es <strong>Diffie-Hellman efímero</strong> (ECDHE o DHE) y el material de sesión no se deriva de la clave del certificado. El certificado sigue siendo imprescindible para <strong>autenticar</strong> al servidor.

### 53. Al validar el certificado de un servidor, ¿qué extensión determina hoy si el nombre solicitado corresponde a ese certificado?

- a) El campo CN del sujeto
- b) La extensión keyUsage
- c) La extensión subjectAltName (SAN)

**Respuesta correcta:** c) · **Referencia:** §5.1.2 [RFC5280]

Es la única que miran los navegadores modernos, y la que permite incluir <strong>varios nombres</strong> en un mismo certificado. La validación comprueba además la firma de la AC, la vigencia, las restricciones básicas y la revocación.

### 54. Respecto de la duración de los certificados TLS públicos, según el calendario aprobado por el CA/Browser Forum:

- a) El máximo se mantiene en 398 días hasta 2030
- b) El máximo es de 200 días desde el 15 de marzo de 2026, de 100 días desde 2027 y de 47 días desde 2029
- c) La duración la fija libremente cada autoridad de certificación

**Respuesta correcta:** b) · **Referencia:** §5.1.2 [CABF]

Es el acuerdo <strong>SC-081v3</strong>, aprobado en abril de 2025. Su consecuencia organizativa es que la renovación manual deja de ser viable y hay que implantar <strong>renovación automatizada</strong> e inventario de certificados.

### 55. Señale la afirmación correcta sobre los mecanismos de revocación de certificados.

- a) La CRL es una lista firmada de certificados revocados que puede estar desactualizada, mientras que OCSP consulta el estado en línea de un certificado concreto
- b) OCSP sustituyó a las CRL, que ya no se emplean desde 2020
- c) El grapado OCSP obliga al navegador a consultar directamente a la autoridad de certificación en cada conexión

**Respuesta correcta:** a) · **Referencia:** §5.1.2 [RFC6960]

El <strong>grapado</strong> hace justo lo contrario de lo que dice la opción C: es <strong>el servidor</strong> quien adjunta una respuesta OCSP reciente, evitando la consulta del navegador y el problema de privacidad que llevó a Let's Encrypt a apagar su servicio OCSP en agosto de 2025.

### 56. ¿Qué es exactamente HTTPS?

- a) Un protocolo distinto de HTTP, con métodos y códigos de estado propios
- b) HTTP transportado dentro de una sesión TLS, normalmente en el puerto 443, con la misma semántica que HTTP
- c) Una extensión de TLS que sustituye a HTTP en las sedes electrónicas

**Respuesta correcta:** b) · **Referencia:** §5.2.1 [RFC9110]

Los métodos, los códigos y las cabeceras son idénticos. El orden de las capas es <strong>TCP → TLS → HTTP</strong>; en HTTP/3, <strong>UDP → QUIC (con TLS 1.3 integrado) → HTTP/3</strong>.

### 57. Un ciudadano accede por HTTPS a la sede electrónica. ¿Qué información sigue siendo visible para quien observe la red?

- a) El contenido del formulario que envía y las cookies de sesión
- b) La ruta y la cadena de consulta de la URL solicitada
- c) La dirección IP del servidor y, salvo que se emplee ECH, el nombre del sitio en la extensión SNI del saludo

**Respuesta correcta:** c) · **Referencia:** §5.2.1 [RFC8446]

El cuerpo, las cabeceras, las cookies y la ruta <strong>sí van cifrados</strong>. El SNI viaja en claro porque el servidor todavía no sabe qué certificado debe presentar; <strong>ECH</strong> es la solución en despliegue.

### 58. Una sede electrónica redirige con un 301 todo el tráfico HTTP hacia HTTPS. ¿Es suficiente?

- a) No: la primera petición aún viaja en claro y puede interceptarse, por lo que debe añadirse HSTS y, si es posible, la precarga
- b) Sí: la redirección permanente garantiza que ninguna petición viaje sin cifrar
- c) No, porque el código correcto para redirigir a HTTPS es el 403

**Respuesta correcta:** a) · **Referencia:** §5.2.1 [RFC6797]

<strong>HSTS</strong> (RFC 6797) obliga al navegador a usar siempre HTTPS con ese dominio, y la <strong>precarga</strong> aplica la protección <strong>desde la primera visita</strong>, eliminando el único momento de riesgo.

### 59. ¿Qué medida del anexo II del Esquema Nacional de Seguridad se refiere específicamente a la protección de servicios y aplicaciones web?

- a) <code>mp.com.1</code>, perímetro seguro
- b) <code>mp.s.2</code>, protección de servicios y aplicaciones web
- c) <code>op.exp.10</code>, protección de claves criptográficas

**Respuesta correcta:** b) · **Referencia:** §6.1.1 [ENS]

Es exigible en las <strong>tres categorías</strong> y obliga ya en la BÁSICA a realizar auditorías <strong>[R1 o R2]</strong> —de caja negra o de caja blanca—, además de prevenir el escalado de privilegios y los ataques de secuencias de órdenes en sitios cruzados. En categoría ALTA se exigen <code>+R2 +R3</code>.

### 60. Conforme al artículo 38 de la Ley 40/2015, la sede electrónica se caracteriza porque:

- a) Puede ser gestionada por cualquier entidad privada en nombre de la Administración
- b) Es equivalente al portal de internet regulado en el artículo 39
- c) Su titularidad, gestión y administración corresponden a una Administración Pública u organismo público, y sus comunicaciones se realizan mediante certificados de sede electrónica

**Respuesta correcta:** c) · **Referencia:** §6.1.1 [L40-2015]

Además está sujeta a los principios de transparencia, publicidad, responsabilidad, calidad, seguridad, disponibilidad, accesibilidad, neutralidad e interoperabilidad. El <strong>portal de internet</strong> del art. 39 no tiene ese régimen reforzado.

## Preguntas sobre los casos prácticos

### Caso 1. Publicación de un nuevo trámite en la sede electrónica

#### 1. En el supuesto planteado, el nombre ayudas.sede.madrid.es se resolverá desde un único servidor DNS autoritativo alojado en el CPD del IAM. ¿Qué riesgo introduce y qué debe proponerse?

- a) Es un punto único de fallo; procede añadir un segundo autoritativo en el mismo CPD y en la misma red.
- b) Es un riesgo menor, porque los resolutores guardan la zona en caché de forma indefinida y siempre la sirven.
- c) Es un punto único de fallo; procede contar con al menos dos autoritativos en redes y emplazamientos distintos.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.2.3

Si el DNS autoritativo cae, ningún servidor deja de funcionar, pero nadie los encuentra: el efecto es el de una caída total. La redundancia exige servidores en redes y emplazamientos distintos (primario y secundarios por transferencia de zona).

#### 2. Para proteger la zona madrid.es frente a la suplantación de respuestas y el envenenamiento de caché, ¿qué medida debe incluir el informe?

- a) Activar DNS sobre TLS (DoT) en el autoritativo, que firma las respuestas y acredita su origen.
- b) Firmar la zona con DNSSEC, que aporta autenticidad e integridad a las respuestas del DNS.
- c) Publicar un registro CAA, que cifra las respuestas que el autoritativo envía a los resolutores.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.2.3

DNSSEC firma digitalmente las respuestas: aporta autenticidad e integridad, no confidencialidad. DoT cifra el canal pero no firma el dato, y CAA solo declara qué autoridades de certificación pueden emitir certificados.

#### 3. Sobre la decisión de publicar el trámite solo en IPv4, ¿qué debe proponer el informe técnico?

- a) Publicarlo en doble pila IPv4/IPv6 y duplicar las reglas del cortafuegos en ambos protocolos.
- b) Mantener solo IPv4, porque con una adopción de IPv6 en torno al 10 % la doble pila no aporta nada.
- c) Publicarlo en doble pila, con las reglas del cortafuegos de IPv4, que se aplican también a IPv6.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.2.2

La doble pila no perjudica a los usuarios IPv4 y evita penalizar a los que acceden desde redes móviles con CGNAT; pero una regla de cortafuegos que solo cubre IPv4 deja abierta la puerta IPv6, por lo que hay que duplicarlas.

#### 4. El puerto 80 se mantiene abierto únicamente para redirigir con un 301 a HTTPS. ¿Qué falta para impedir que un intermediario degrade la conexión del ciudadano (SSL stripping)?

- a) Sustituir el 301 por una redirección 302, que el navegador no almacena y repite en cada visita.
- b) Añadir HSTS con includeSubDomains y, si el dominio lo permite, solicitar la precarga.
- c) Activar el grapado OCSP, que comprueba el certificado antes de la primera petición por HTTP.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §5.2.1

La redirección es necesaria pero insuficiente: la primera petición viaja en claro y puede interceptarse. HSTS obliga al navegador a usar siempre HTTPS con el dominio, y la precarga aplica la protección desde la primera visita.

#### 5. ¿Qué versiones del protocolo debe admitir en 2026 el servidor que publica el nuevo trámite?

- a) Solo TLS 1.3, porque TLS 1.2 se declaró obsoleto por el RFC 8996 junto con TLS 1.0 y TLS 1.1.
- b) De TLS 1.0 a TLS 1.3, porque TLS 1.0 y 1.1 siguen vigentes para no dejar fuera a equipos antiguos.
- c) TLS 1.2 y TLS 1.3, con preferencia por 1.3, deshabilitando SSL 2.0 y 3.0 y TLS 1.0 y 1.1.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §5.1.1

SSL 2.0 y 3.0 están prohibidos (RFC 6176 y 7568) y TLS 1.0 y 1.1 son obsoletos (RFC 8996); siguen vigentes TLS 1.2 y TLS 1.3.

#### 6. El equipo de proyecto quiere contratar un certificado de un año con renovación manual anotada en la agenda del responsable. ¿Cómo debe valorarse?

- a) No es viable: desde el 15 de marzo de 2026 el máximo es de 200 días, y hay que automatizar la renovación (ACME).
- b) Es viable, porque el límite de 200 días del CA/Browser Forum no se aplicará a los certificados hasta 2027.
- c) No es viable: desde marzo de 2026 el máximo es de 47 días, por lo que habría que renovarlo cada mes y medio.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §5.1.2

El CA/Browser Forum fija un máximo de 200 días desde el 15 de marzo de 2026, que bajará a 100 días en 2027 y a 47 en 2029. Con plazos tan cortos la renovación manual deja de ser sostenible: renovación automatizada, inventario con responsable y alertas.

#### 7. La aplicación guarda la sesión en una cookie sin atributos. ¿Qué atributos mitigan, respectivamente, la interceptación en tránsito, el robo por XSS y la falsificación de petición en sitios cruzados (CSRF)?

- a) HttpOnly, Secure y SameSite=None.
- b) Secure, SameSite=Strict y HttpOnly.
- c) Secure, HttpOnly y SameSite=Lax o Strict.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §4.2.2

Secure impide que la cookie viaje por HTTP; HttpOnly la hace inaccesible desde JavaScript, lo que mitiga el robo por XSS; y SameSite controla su envío en peticiones de origen cruzado, lo que mitiga el CSRF.

#### 8. Un desarrollador propone devolver las páginas con datos del solicitante con Cache-Control: no-cache, para que no queden en el navegador de un puesto compartido. ¿Es adecuado?

- a) No: no-cache permite almacenar la respuesta y solo obliga a revalidarla; procede no-store, private.
- b) Sí: no-cache prohíbe almacenar la respuesta en cualquier caché, incluida la del navegador del puesto.
- c) No: no-cache solo afecta a las cachés intermedias; procede public, que limita la copia al navegador.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §4.2.2

no-cache sí permite almacenar la respuesta, aunque obliga a revalidarla antes de reutilizarla; no-store prohíbe almacenarla en cualquier caché, y private excluye las cachés compartidas.

#### 9. El sistema está categorizado MEDIA conforme al ENS. ¿Qué exige el ENS para el cifrado del canal de este servicio?

- a) La medida mp.com.2 solo en categoría ALTA; en MEDIA basta con cualquier algoritmo de TLS.
- b) La medida mp.com.2 con su refuerzo R1: algoritmos y parámetros autorizados por el CCN.
- c) La medida mp.info.3, que en nivel MEDIO exige firmar electrónicamente cada respuesta.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §6.1.1 · mp.com.2 ENS

mp.com.2 (protección de la confidencialidad) se aplica desde nivel BAJO y, desde nivel MEDIO, añade el refuerzo R1: algoritmos y parámetros autorizados por el CCN.

#### 10. ¿Qué precepto legal ampara la exigencia de que el nuevo trámite se sirva con certificado de sede y comunicación segura?

- a) El artículo 32 del RGPD, que regula los certificados de sede electrónica.
- b) El Real Decreto 1112/2018, que regula la sede electrónica y sus certificados.
- c) El artículo 38 de la Ley 40/2015, desarrollado por el Real Decreto 203/2021.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 4 · art. 38 Ley 40/2015

Conforme al artículo 38 de la Ley 40/2015, las comunicaciones de la sede se realizan mediante certificados de sede electrónica; el RD 203/2021 lo desarrolla. El art. 32 del RGPD trata la seguridad del tratamiento y el RD 1112/2018, la accesibilidad.

### Caso 2. Diagnóstico por capas de una incidencia en una oficina de distrito

#### 1. En el aviso 1, ping 8.8.8.8 responde y ping sede.madrid.es devuelve «host desconocido». ¿Dónde está el problema?

- a) En la capa de enlace, porque el puesto no obtiene la dirección MAC de la pasarela.
- b) En la resolución de nombres (DNS), servicio de la capa de aplicación; la red funciona.
- c) En la capa de transporte, porque el cortafuegos bloquea el puerto 443 de la sede.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §2.1.2

Si el ping a una dirección IP externa funciona, las capas física, de enlace y de internet están operativas. Lo que falla es traducir el nombre, que es un servicio de la capa de aplicación.

#### 2. Para confirmar si el fallo del aviso 1 está en el resolutor de la organización, ¿qué comprobación procede?

- a) nslookup sede.madrid.es contra el DNS corporativo y después contra uno externo, comparando los resultados.
- b) Repetir ping 8.8.8.8 con paquetes de mayor tamaño, para descartar un problema de fragmentación.
- c) Borrar las cookies del navegador, para descartar que la sesión de la sede haya caducado en el puesto.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §2.2.3

Si la resolución solo falla contra el DNS corporativo y funciona contra uno externo, el problema está en el resolutor que usa el puesto, no en la sede. Que la sede abra desde el móvil con el DNS del operador apunta en la misma dirección.

#### 3. Teniendo en cuenta que esa mañana un proveedor conectó un portátil a una toma de la zona de público, ¿cuál es la causa más probable del aviso 1?

- a) Un conflicto de direcciones MAC entre el portátil y el puesto, que impide resolver nombres en la red.
- b) Un bucle de conmutación causado por el portátil, que ha saturado la red de tramas de difusión.
- c) Un servidor DHCP no autorizado en el portátil, que ha entregado a los puestos un DNS y una pasarela falsos.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §3.2.2

DHCP no autentica: un servidor no autorizado conectado a una toma de red puede repartir configuraciones falsas, rompiendo la resolución y convirtiéndose en intermediario de todo el tráfico. Un bucle saturaría la red y fallaría también el ping a la IP.

#### 4. En el aviso 2, al enviar el formulario el navegador muestra «502 Bad Gateway». ¿Quién emite ese código y qué significa?

- a) Un intermediario (proxy inverso o balanceador), porque el servidor de origen le devolvió una respuesta inválida.
- b) La aplicación de origen, ante un error genérico no controlado que se ha producido dentro del propio servidor.
- c) El navegador del puesto, porque no ha podido validar la respuesta cifrada recibida del servidor de la sede.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §4.2.1

El 502 lo emite un intermediario cuando el origen le devuelve una respuesta inválida. El error genérico de la propia aplicación es el 500.

#### 5. Si en lugar de «503 Service Unavailable» los usuarios hubieran recibido «504 Gateway Timeout», ¿qué indicaría?

- a) Que el servicio está en mantenimiento y puede indicarse cuándo reintentar con Retry-After.
- b) Que el intermediario no recibió a tiempo la respuesta del servidor de origen.
- c) Que el usuario está autenticado pero no tiene permiso para enviar ese formulario.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.2.1

El 504 lo emite un intermediario cuando el origen no responde a tiempo. La indisponibilidad temporal con Retry-After corresponde al 503, y la falta de permiso de un usuario autenticado, al 403.

#### 6. Ante la secuencia de 502 y, poco después, 503 generalizado, ¿cómo debe actuar el Centro de Atención a Usuarios?

- a) Reinstalar el navegador de los puestos afectados, porque los códigos 5xx señalan un error del cliente.
- b) Revisar el DNS de cada puesto de la oficina, porque el 503 indica que el nombre no se ha resuelto.
- c) Escalarlo al equipo de la aplicación, porque los códigos 5xx señalan un problema del lado del servidor.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §4.2.1

La familia 5xx es responsabilidad del servidor, y la 4xx del cliente. La secuencia apunta a que la aplicación de origen ha dejado de responder bien, así que no procede intervenir en la oficina.

#### 7. En el aviso 3, el empleado ha entrado en el servicio interno escribiendo su dirección IP en lugar del nombre. ¿Por qué puede aparecer el aviso de certificado no válido?

- a) Porque TLS no puede negociarse cuando se accede a un servidor por su dirección IP en lugar del nombre.
- b) Porque la IP no figura en la extensión subjectAltName, que es donde el navegador comprueba el nombre.
- c) Porque al usar la IP el navegador deja de consultar las AC raíz de su almacén de confianza.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §5.1.2

El navegador comprueba que el nombre solicitado figure en la extensión subjectAltName (SAN). Si se accede por la IP o por un alias que no está en el SAN, la validación falla.

#### 8. El empleado pregunta si puede «darle a continuar» para entrar en el servicio interno. ¿Qué debe responderse?

- a) Que sí: al ser un servicio interno, el tráfico no sale de la red municipal y el aviso no supone riesgo.
- b) Que sí, siempre que al terminar borre el historial y las cookies del navegador del puesto de trabajo.
- c) Que no: aceptar el aviso anula la garantía de TLS de saber con quién se habla, y hay que corregir la causa.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §5.1.2

Aceptar el aviso anula precisamente lo que aporta TLS: la certeza de hablar con quien se cree. Acostumbrar al usuario a aceptar avisos es la puerta de entrada de los ataques de intermediario.

#### 9. Para que un equipo conectado a una toma de público no vuelva a repartir configuraciones de red, ¿qué medida debe activarse en el conmutador de planta?

- a) DHCP snooping, que solo admite respuestas DHCP por los puertos de confianza, junto con RA Guard para IPv6.
- b) DHCPv6 sin estado en los puestos, que impide que cualquier equipo ajeno reparta direcciones en la red.
- c) Concesiones DHCP de pocos minutos, para que la configuración falsa caduque antes de causar daños.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §3.2.2

DHCP snooping admite respuestas DHCP solo por los puertos declarados de confianza, y RA Guard cubre el equivalente IPv6 (anuncios de encaminador falsos). Se completa con 802.1X, tomas no usadas deshabilitadas y VLAN separada.

#### 10. ¿Qué medida del ENS respalda llevar los equipos ajenos al Ayuntamiento y la zona de público a una VLAN separada?

- a) mp.com.3, protección de la integridad y de la autenticidad.
- b) mp.com.4, separación de flujos de información en la red.
- c) mp.s.4, protección frente a la denegación de servicio.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §6.1.1 · mp.com.4 ENS

mp.com.4 exige segregar el tráfico, con refuerzos por VLAN o redes separadas y un segmento propio para las comunicaciones inalámbricas.

### Caso 3. Correo suplantado y envío de un fichero con datos personales

#### 1. En el asunto A, el correo fraudulento muestra como remitente tesoreria@madrid.es sin haber salido de los servidores municipales. ¿Cuál es la raíz del problema?

- a) Que SMTP no autentica la cabecera From, que es la que ve el destinatario.
- b) Que el atacante ha obtenido la clave privada DKIM del dominio municipal.
- c) Que SPF publica el From visible y permite que cualquier servidor lo use.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §3.1.1

SMTP no autentica la cabecera From, de modo que cualquiera puede escribir en ella lo que quiera. SPF, DKIM y DMARC existen para tapar ese agujero; aquí, además, no hay DKIM configurado.

#### 2. El dominio tiene un registro SPF terminado en ~all. ¿Qué comprueba SPF y por qué no ha bastado?

- a) Comprueba el From visible; con ~all el receptor debía rechazar el mensaje, pero ignoró la política.
- b) Comprueba la firma del cuerpo del mensaje; con ~all se acepta el correo aunque la firma no cuadre.
- c) Comprueba la envuelta (MAIL FROM); con ~all el fallo es blando y, además, no protege el From visible.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §3.1.1

SPF publica qué servidores pueden enviar con el dominio y se comprueba contra la envuelta, no contra el From visible. Con ~all el receptor puede aceptar el mensaje marcándolo.

#### 3. El registro DMARC del dominio tiene la política p=none. ¿Qué efecto tiene?

- a) Pide al receptor que rechace los mensajes no alineados, salvo los que lleguen firmados.
- b) Solo observa e informa: no pide al receptor ninguna acción ante el fallo de alineamiento.
- c) Pide al receptor que envíe a cuarentena los mensajes con SPF terminado en ~all.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §3.1.1

DMARC exige el alineamiento entre el From visible y lo validado por SPF o DKIM, y fija la política ante el fallo (none, quarantine, reject). Con p=none no dice al receptor qué hacer.

#### 4. El dominio no tiene DKIM configurado. ¿Qué aportaría ese mecanismo?

- a) El cifrado del mensaje de extremo a extremo entre el servidor municipal y el destinatario.
- b) La lista de direcciones IP autorizadas para enviar correo en nombre de madrid.es.
- c) Una firma criptográfica de cabeceras y cuerpo, con la clave pública publicada en el DNS.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §3.1.1

DKIM firma criptográficamente cabeceras y cuerpo con una clave cuya pública se publica en el DNS, bajo un selector. La lista de servidores autorizados es SPF, y DKIM no cifra el mensaje.

#### 5. Para corregir la configuración del correo sin bloquear mensajes legítimos, ¿qué debe hacerse en primer lugar?

- a) Inventariar todos los emisores legítimos del dominio, incluidas plataformas de notificación y de boletines.
- b) Pasar DMARC directamente a p=reject, para cortar cuanto antes la campaña de suplantación en curso.
- c) Endurecer SPF a -all, porque es el cambio con menos riesgo de bloquear el correo legítimo del dominio.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §3.1.1

Endurecer la política antes de tener DKIM y el inventario de emisores es la causa más frecuente de que se pierda correo legítimo. El orden es: inventario, DKIM, SPF -all y DMARC progresivo.

#### 6. Una vez desplegado DKIM y endurecido SPF, ¿cómo debe evolucionar la política DMARC?

- a) De p=reject a p=quarantine, relajándola en cuanto lleguen quejas por correo legítimo bloqueado.
- b) De p=none con informes agregados a p=quarantine con porcentaje creciente y, al final, a p=reject.
- c) De p=none directamente a p=reject en cuanto se publique el SPF con -all, sin fases intermedias.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §3.1.1

El escalado es progresivo: unas semanas en p=none recibiendo informes agregados, después p=quarantine con porcentaje creciente y, como objetivo, p=reject.

#### 7. En el asunto B, el proveedor propone publicar el fichero en un FTP anónimo accesible desde internet. ¿Por qué debe rechazarse?

- a) Porque no autentica a quien accede, y FTP transmite las credenciales y los datos en claro.
- b) Porque FTP solo admite ficheros de texto y el de los solicitantes contiene datos binarios.
- c) Porque el FTP anónimo cifra el fichero con una clave pública que cualquiera puede obtener.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §3.1.2

Un FTP anónimo no autentica a quien accede y FTP transmite credenciales y datos en claro: un fichero con datos personales expuesto así es una violación de seguridad en potencia.

#### 8. Como alternativa, el proveedor ofrece «FTP seguro» y duda entre SFTP y FTPS. ¿Qué opción es preferible y por qué?

- a) FTPS, que es la variante de SFTP que añade TLS a SSH y evita así tener que abrir el puerto 22.
- b) SFTP, subsistema de SSH que usa un solo canal en el puerto 22 y admite autenticación por par de claves.
- c) FTPS, porque usa un único canal cifrado y evita los problemas de cortafuegos del modo activo.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §3.1.2

FTPS es FTP envuelto en TLS y conserva sus dos canales, con los problemas de cortafuegos del modo activo. SFTP no tiene relación con FTP: es SSH, con un solo canal en el puerto 22 y autenticación por clave.

#### 9. ¿Qué medida del ENS respalda la protección del correo electrónico municipal y la actuación frente al correo no solicitado, y en qué categorías es exigible?

- a) mp.s.1, protección del correo electrónico, exigible solo desde categoría MEDIA.
- b) mp.com.4, separación de flujos de información, exigible solo en categoría ALTA.
- c) mp.s.1, protección del correo electrónico, exigible en las tres categorías.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §6.1.1 · mp.s.1 ENS

mp.s.1 protege la información y los datos de encaminamiento del correo y actúa frente a correo no solicitado, código dañino y código móvil, con normativa de uso y concienciación; se exige en las tres categorías.

#### 10. Si el fichero de los solicitantes llegara a exfiltrarse, ¿qué preceptos regulan la notificación de esa violación de seguridad?

- a) Los artículos 33 y 34 del RGPD, con notificación en el plazo de 72 horas.
- b) El artículo 38 de la Ley 40/2015, con notificación en el plazo de 24 horas.
- c) El artículo 32 del RGPD, con notificación en el plazo de diez días hábiles.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · arts. 33 y 34 RGPD

Conforme a los artículos 33 y 34 del RGPD, la violación de seguridad de datos personales se notifica en 72 horas. El artículo 32 regula la seguridad del tratamiento y el 38 de la Ley 40/2015, la sede electrónica.
