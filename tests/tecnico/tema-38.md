# Test del tema 38. El sistema de radiocomunicación TETRA

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-38.html>

## Batería de preguntas

### 1. ¿Cuál es la expansión vigente de las siglas TETRA según el ETSI?

- a) TErrestrial TRunked RAdio
- b) Trans European Trunked Radio
- c) Telephony and Trunked Radio Access

**Respuesta correcta:** a) · **Referencia:** §1.3 [TCCA-GLOBAL]

La denominación original fue <em>Trans European Trunked Radio</em>, coherente con un proyecto concebido para dotar a Europa de un sistema común de radio profesional. Cuando el estándar se difundió fuera de Europa —hoy está desplegado en más de 124 países— el adjetivo «transeuropeo» perdió sentido y el ETSI pasó a expandir el acrónimo como <em>TErrestrial TRunked RAdio</em>. El adjetivo «terrestre» tiene además valor descriptivo: distingue estos sistemas de los móviles por satélite.

### 2. ¿Qué organismo normaliza TETRA?

- a) La APCO estadounidense
- b) El ETSI, Instituto Europeo de Normas de Telecomunicaciones
- c) La Unión Internacional de Telecomunicaciones (UIT)

**Respuesta correcta:** b) · **Referencia:** §1.3 [EN392-1]

TETRA es un estándar abierto del ETSI, con las series EN 300 392 (modo troncalizado), EN 300 396 (modo directo), EN 300 394 (conformidad) y EN 300 395 (códec de voz). La APCO es el organismo que normaliza P25 en Estados Unidos, y la UIT reparte el espectro entre servicios y regiones pero no elabora este estándar.

### 3. En la evolución de la radio móvil privada, ¿a qué generación pertenece TETRA?

- a) A la primera: la radio analógica convencional
- b) A la segunda: el trunking analógico
- c) A la tercera: el trunking digital

**Respuesta correcta:** c) · **Referencia:** §1.1 [UIT-M2014]

La secuencia es: analógica convencional (canal fijo por colectivo) → trunking analógico (MPT-1327) → trunking digital (TETRA, TETRAPOL, P25 y DMR) → banda ancha crítica (MCPTT del 3GPP). Una pregunta habitual pide identificar el sistema analógico de la segunda etapa, que es MPT-1327, no TETRA.

### 4. ¿Qué significa que un sistema de radio sea troncalizado?

- a) Que cada colectivo de usuarios tiene asignada una frecuencia fija en exclusiva
- b) Que la voz se transmite de forma analógica sobre un enlace troncal de alta capacidad
- c) Que los canales forman una bolsa común que el sistema asigna dinámicamente bajo demanda

**Respuesta correcta:** c) · **Referencia:** §1.2 [CNAF]

La asignación la dirige un canal de control dedicado, que recibe la petición, comprueba la identidad y el grupo del solicitante y le asigna un canal de tráfico solo mientras dura la transmisión. La opción A describe precisamente el sistema convencional, que es lo contrario. El CNAF lo denomina «sistemas multicanales de acceso aleatorio de frecuencias con concentración de enlaces».

### 5. ¿Qué diferencia esencial existe entre PMR y PAMR?

- a) La PAMR es la misma tecnología explotada por un operador comercial que vende el servicio a terceros
- b) La PAMR usa exclusivamente tecnología analógica y la PMR, digital
- c) La PAMR opera en VHF y la PMR, en UHF

**Respuesta correcta:** a) · **Referencia:** §1.1 [CNAF]

La distinción es jurídica y de modelo de explotación, no técnica, y tiene consecuencias directas en el título habilitante necesario para usar el espectro. El CNAF español las trata conjuntamente como «sistemas móviles digitales de banda estrecha PMR/PAMR».

### 6. En una estación base TETRA con cuatro portadoras y un intervalo dedicado al canal de control, ¿cuántos canales de tráfico simultáneos hay?

- a) 4
- b) 15
- c) 16

**Respuesta correcta:** b) · **Referencia:** §1.2 [EN392-2]

Cuatro portadoras por cuatro intervalos de tiempo dan 16 canales físicos; descontando el intervalo dedicado al canal de control principal quedan 15 canales de tráfico simultáneos, repartidos dinámicamente entre todos los grupos. La opción C olvida restar el canal de control y la opción A corresponde a un despliegue convencional de cuatro canales rígidos.

### 7. ¿Cuál de las siguientes NO es una ventaja del trunking frente a la radio convencional?

- a) La posibilidad de crear y disolver grupos desde el centro de control sin tocar los terminales
- b) La independencia respecto de la infraestructura, que le permite funcionar aunque caiga el canal de control
- c) La eficiencia espectral, al servir a más usuarios con el mismo número de frecuencias

**Respuesta correcta:** b) · **Referencia:** §1.2 [EN392-2]

Es justamente lo contrario: el trunking introduce dependencia de la infraestructura, porque sin canal de control no hay asignación dinámica. Por eso los sistemas troncalizados serios incorporan modos degradados, como el repliegue local de la estación base y el modo directo entre terminales.

### 8. ¿Qué norma del ETSI hace verificable la interoperabilidad entre equipos TETRA de fabricantes distintos?

- a) La EN 300 392-7, de seguridad
- b) La EN 300 395, del códec de voz
- c) La EN 300 394, de pruebas de conformidad

**Respuesta correcta:** c) · **Referencia:** §1.3 [EN394]

Un estándar abierto define interfaces, pero la promesa de interoperabilidad solo se hace real si existe una forma normalizada de comprobar que un equipo cumple la norma. Esa es la función de la EN 300 394, complementada por las pruebas de interoperabilidad que organiza la industria.

### 9. ¿Cuál de estos rasgos distingue a la radiocomunicación móvil privada de la telefonía celular pública?

- a) El establecimiento de llamada de grupo en menos de 300 milisegundos
- b) El uso de modulaciones digitales de fase
- c) La existencia de un identificador único de abonado

**Respuesta correcta:** a) · **Referencia:** §1.1 [ETR300-1]

Las modulaciones digitales de fase y los identificadores de abonado existen también en la telefonía celular, de modo que no distinguen nada. Lo propio de la PMR es la combinación de comunicación de grupo, inmediatez por debajo de 300 ms, prioridad garantizada por el titular de la red, funcionamiento sin infraestructura y control de la disponibilidad.

### 10. ¿Qué designa la sigla SwMI en el estándar TETRA?

- a) Toda la infraestructura fija de conmutación y gestión de la red
- b) El módulo de identidad de abonado que se inserta en el terminal
- c) El protocolo de señalización entre la estación base y el terminal

**Respuesta correcta:** a) · **Referencia:** §2.1 [EN392-1]

SwMI es <em>Switching and Management Infrastructure</em>. Desde el punto de vista del terminal, la SwMI «es la red»: incluye las estaciones base, los nodos de conmutación, las bases de datos de abonados y grupos, el centro de autenticación y la gestión. El módulo de identidad se normaliza en la EN 300 812.

### 11. ¿Dónde se aplica y dónde se deshace el cifrado de interfaz aire de TETRA?

- a) Entre los dos terminales que participan en la comunicación
- b) Entre el terminal y el nodo de conmutación de la red
- c) Entre el terminal y la estación base, que es donde se descifra

**Respuesta correcta:** c) · **Referencia:** §2.1.1 · §4.3.2 [TTR001-11]

Por eso el cifrado de interfaz aire protege frente a quien escucha el aire, pero no frente al operador de la red ni frente a un compromiso de la infraestructura. La opción A describe el cifrado extremo a extremo, que es una capa distinta y complementaria.

### 12. ¿Qué es el canal de control principal (MCCH) de una célula TETRA?

- a) El canal por el que circula el tráfico de voz de mayor prioridad
- b) El canal permanentemente activo por el que se difunde la información del sistema y se piden recursos
- c) El enlace de transporte entre la estación base y el nodo de conmutación

**Respuesta correcta:** b) · **Referencia:** §2.1.1 [EN392-2]

Se transmite en el intervalo 1 de la portadora principal de la célula. Un terminal recién encendido lo busca para sincronizarse. Sin canal de control no hay troncalización, y de ahí la necesidad de modos degradados como el repliegue local y el modo directo.

### 13. En una llamada de grupo, ¿en qué células ocupa canal de tráfico la red?

- a) En todas las células de la red, para garantizar que nadie se quede fuera
- b) Solo en aquellas donde hay miembros del grupo afiliados
- c) Solo en la célula donde se encuentra quien transmite

**Respuesta correcta:** b) · **Referencia:** §2.1.2 [EN392-1]

Es la razón por la que un sistema TETRA soporta cientos de grupos con pocas portadoras. La opción C impediría que los miembros situados en otras células oyeran la comunicación, y la opción A desperdiciaría capacidad en toda la red.

### 14. ¿Cuál de estas funciones corresponde a la capa de gestión y despacho de una red TETRA?

- a) La asignación dinámica de grupos (DGNA) y la inhabilitación remota de terminales
- b) La modulación π/4-DQPSK y la codificación de canal
- c) El encaminamiento del audio de una llamada hacia las células con afiliados

**Respuesta correcta:** a) · **Referencia:** §2.1.3 [EN392-1]

La modulación y la codificación de canal pertenecen a la capa de radio, y el encaminamiento del audio, a la capa de conmutación. La capa de gestión es la que soporta el trabajo de las personas: gestión de abonados y grupos, consolas de despacho, grabación, supervisión de la red y gestión de claves.

### 15. ¿Cuáles son las clases de potencia normalizadas del terminal TETRA?

- a) 50 W, 25 W, 5 W y 0,5 W
- b) 20 W, 5 W, 2 W y 0,5 W
- c) 30 W, 10 W, 3 W y 1 W

**Respuesta correcta:** c) · **Referencia:** §2.2.1 [EN392-2]

Corresponden a las clases 1, 2, 3 y 4 respectivamente, y existen clases adicionales de menor potencia. En la práctica los portátiles son de 1 y 3 W y los equipos embarcados, de 3 y 10 W. Esa diferencia explica que en el borde de la cobertura llegue el vehículo y no el agente a pie.

### 16. En el esquema de identidades de TETRA, ¿cómo se compone la ITSI?

- a) Por el MCC más el MNC exclusivamente
- b) Por la GSSI más el alias del usuario
- c) Por la MNI más la ISSI, donde la MNI es a su vez el MCC más el MNC

**Respuesta correcta:** c) · **Referencia:** §2.2.1 [EN392-7]

La ITSI es la identidad individual completa del abonado. La ISSI es su parte corta, la que lo identifica dentro de su red. La identidad de grupo es la GTSI, con la GSSI como parte corta. La ESI es la identidad corta cifrada en el aire.

### 17. ¿Qué caracteriza al modo directo (DMO) de TETRA?

- a) Que los terminales se comunican a través de una única estación base, sin pasar por el nodo de conmutación
- b) Que los terminales se comunican entre sí sin ninguna infraestructura de red
- c) Que la red asigna un canal permanente a un grupo para toda la duración del incidente

**Respuesta correcta:** b) · **Referencia:** §2.2.2 [EN396]

Está normalizado en la serie EN 300 396, distinta de la EN 300 392 del modo troncalizado. La opción A describe el repliegue local de una estación base aislada, que sigue siendo modo troncalizado. La capacidad de funcionar sin infraestructura es una de las razones por las que un servicio de emergencia no puede sustituir su radio por telefonía móvil.

### 18. Una dotación trabaja en modo directo en un sótano sin cobertura y el centro de mando necesita oírla y hablar con ella. ¿Qué elemento hay que desplegar?

- a) Un DM-GATE, es decir, una pasarela hacia la red troncalizada
- b) Un DM-REP de tipo 2, para soportar dos llamadas simultáneas
- c) Una estación base adicional en repliegue local

**Respuesta correcta:** a) · **Referencia:** §2.2.3 [EN396]

El DM-REP solo amplía el alcance dentro del modo directo: la dotación se oiría mejor entre sí, pero el centro de mando seguiría sin enterarse de nada. Es la pasarela la que reinyecta la comunicación en la red y devuelve la visibilidad al despacho. El equipo DM-REP/GATE combina ambas funciones.

### 19. ¿Qué tipos de repetidor de modo directo distingue la norma EN 300 396?

- a) Tipo 1A sobre una portadora, tipo 1B sobre un par de portadoras dúplex y tipo 2 con dos llamadas
- b) Tipo A analógico, tipo B digital y tipo C híbrido
- c) Tipo simplex, tipo semidúplex y tipo dúplex completo

**Respuesta correcta:** a) · **Referencia:** §2.2.3 [EN396]

El repetidor de tipo 1 soporta una sola llamada en el interfaz aire, y se subdivide en 1A y 1B según trabaje sobre una portadora o sobre un par separado en dúplex. El de tipo 2 soporta dos llamadas simultáneas.

### 20. ¿Qué interfaz del modelo de referencia de TETRA es la ISI?

- a) La I1
- b) La I3
- c) La I6

**Respuesta correcta:** b) · **Referencia:** §2.3 [ETR300-1]

El modelo define seis puntos de referencia: I1 interfaz aire en modo troncalizado, I2 interfaz de línea, I3 interfaz entre sistemas o ISI, I4 interfaz de equipo periférico o PEI, I5 interfaz de gestión de red e I6 interfaz aire en modo directo. La I1 y la I6 son las dos interfaces aire, y están en normas distintas.

### 21. ¿Para qué sirve la interfaz PEI de TETRA?

- a) Para interconectar dos redes TETRA de titularidad distinta
- b) Para conectar las consolas de despacho a la infraestructura por línea
- c) Para conectar el terminal con un equipo de datos del usuario, como un ordenador embarcado

**Respuesta correcta:** c) · **Referencia:** §2.3.3 [EN392-5]

El PEI, <em>Peripheral Equipment Interface</em>, es la I4 del modelo de referencia y está normalizado en la EN 300 392-5. Se basa en un juego de comandos AT extendidos y es lo que convierte al terminal en un módem de datos. La opción A describe la ISI y la opción B, la interfaz de línea.

### 22. Dos administraciones distintas operan sendas redes TETRA en el mismo territorio y necesitan comunicarse. ¿Cuál es el mecanismo normalizado?

- a) La interfaz PEI de ambas redes
- b) El modo directo con clave estática compartida
- c) La interfaz entre sistemas (ISI), normalizada en la EN 300 392-3

**Respuesta correcta:** c) · **Referencia:** §2.3.2 [EN392-3]

La ISI permite llamadas individuales y de grupo entre abonados de redes distintas, itinerancia y transferencia de mensajes cortos. Conviene saber, además, que su implantación real ha sido desigual y que muchas interconexiones se han resuelto con pasarelas de audio o con acoplamiento de grupos en las consolas de despacho.

### 23. ¿Qué esquema de acceso múltiple emplea TETRA?

- a) FDMA combinado con TDMA: portadoras de 25 kHz divididas en cuatro intervalos
- b) CDMA con códigos ortogonales sobre una banda común
- c) FDMA puro con canalización de 12,5 kHz

**Respuesta correcta:** a) · **Referencia:** §3.2 [EN392-2]

Primero se divide el espectro en portadoras, que es FDMA, y después cada portadora en cuatro intervalos de tiempo, que es TDMA. La opción C describe TETRAPOL, que es de acceso FDMA con canalización de 12,5 kHz. TETRA no emplea CDMA.

### 24. ¿Cuál es la eficiencia espectral de TETRA expresada en anchura de banda por canal de voz?

- a) 12,5 kHz por canal
- b) 6,25 kHz por canal
- c) 25 kHz por canal

**Respuesta correcta:** b) · **Referencia:** §3.2 [UIT-M2014]

Resulta de dividir los 25 kHz de la portadora entre los cuatro canales que sostiene: 25 dividido entre 4 son 6,25 kHz por canal de voz. TETRAPOL, con FDMA y 12,5 kHz por canal, obtiene la mitad de eficiencia; los 25 kHz de la opción C son el ancho de la portadora completa, no el de un canal.

### 25. ¿Cuál es el radio máximo de célula en TETRA Release 1 y a qué se debe?

- a) 35 km, por la potencia máxima permitida al terminal
- b) 58 km, por la estructura temporal de los intervalos TDMA
- c) 120 km, por el límite de propagación en la banda de 400 MHz

**Respuesta correcta:** b) · **Referencia:** §3.2 [EN392-2]

La limitación no es de potencia sino de tiempo: si el terminal está demasiado lejos, su ráfaga llega tan retrasada que invadiría el intervalo siguiente. TETRA Release 2 incorporó mejoras de alcance para superar ese límite en despliegues rurales, marítimos y militares.

### 26. ¿Cuántos bits transporta cada símbolo en la modulación π/4-DQPSK de TETRA?

- a) 1 bit
- b) 4 bits
- c) 2 bits

**Respuesta correcta:** c) · **Referencia:** §3.3 [EN392-2]

La letra Q corresponde a <em>quaternary</em>: cuatro estados de fase posibles, y como 2 elevado a 2 son 4, cada símbolo transporta 2 bits. Con una tasa de 18.000 símbolos por segundo se obtienen 36.000 bits por segundo brutos por portadora. La GMSK de TETRAPOL y de GSM transporta 1 bit por símbolo.

### 27. ¿Qué consigue el desplazamiento de π/4 en la modulación de TETRA?

- a) Que las transiciones entre símbolos no pasen por el origen, evitando que la envolvente caiga a cero
- b) Que la tasa de símbolo se duplique respecto a una QPSK convencional
- c) Que el receptor pueda prescindir de la corrección de errores

**Respuesta correcta:** a) · **Referencia:** §3.3 [EN392-2]

Una señal con variaciones muy bruscas de amplitud obliga a usar amplificadores muy lineales, caros e ineficientes en consumo. Al evitar el paso por el origen se mantiene una relación pico-media moderada, lo que en un terminal alimentado por batería se traduce directamente en más autonomía.

### 28. ¿Cuál es la tasa binaria bruta de una portadora TETRA?

- a) 36 kbit/s
- b) 28,8 kbit/s
- c) 9,6 kbit/s

**Respuesta correcta:** a) · **Referencia:** §3.3 [EN392-2]

Resulta de multiplicar los 18.000 símbolos por segundo por los 2 bits que transporta cada símbolo. Repartidos entre los cuatro intervalos corresponden 9 kbit/s brutos a cada uno, de los que quedan 7,2 kbit/s netos para el usuario tras descontar sincronización, cabeceras y protección de errores. Los 28,8 kbit/s de la opción B son el resultado de agregar los cuatro intervalos netos.

### 29. ¿Qué códec de voz emplea TETRA y con qué tasa neta?

- a) AMR a 12,2 kbit/s
- b) CELP a 8 kbit/s
- c) ACELP a 4,567 kbit/s

**Respuesta correcta:** c) · **Referencia:** §3.3 [EN395]

El códec produce 137 bits por cada trama de voz de 30 milisegundos, lo que da 4.567 bits por segundo. A esos bits se les añade codificación de canal hasta ocupar los 7,2 kbit/s del intervalo: casi el 37 % del caudal se dedica a corregir errores, y es lo que mantiene la voz inteligible en el borde de la cobertura.

### 30. ¿Cuánto dura un intervalo de tiempo en el interfaz aire de TETRA?

- a) 4,615 ms
- b) 14,167 ms
- c) 56,67 ms

**Respuesta correcta:** b) · **Referencia:** §3.4 [EN392-2]

Cuatro intervalos forman una trama de 56,67 ms, que es el valor de la opción C. Dieciocho tramas forman una multitrama de 1,02 s y sesenta multitramas, una hipertrama de 61,2 s. Los 4,615 ms de la opción A corresponden a la trama de GSM.

### 31. ¿Qué trama de cada multitrama TETRA se reserva a señalización?

- a) La primera
- b) La decimoctava
- c) La novena

**Respuesta correcta:** b) · **Referencia:** §3.4 [EN392-2]

La multitrama tiene 18 tramas y la número 18 es la trama de control. Eso permite que la red envíe información a un terminal mientras está en conversación, sin interrumpirla, y hace posible la función de entrada tardía. El usuario dispone, por tanto, de 17 de cada 18 tramas para su tráfico.

### 32. ¿Cuánto dura una hipertrama y qué relevancia tiene?

- a) 61,2 segundos, y su número interviene en la generación del flujo de clave del cifrado de interfaz aire
- b) 1,02 segundos, y delimita el ciclo de asignación de canales de tráfico
- c) 30 segundos, y marca el periodo de renovación de la clave derivada

**Respuesta correcta:** a) · **Referencia:** §3.4 [TETRABURST]

La hipertrama son 60 multitramas de 1,02 segundos. El valor de la opción B es precisamente la duración de una multitrama. Ese papel del tiempo en la generación del flujo de clave es lo que la vulnerabilidad CVE-2022-24401 convirtió en problema, al difundirse el tiempo de red sin autenticar.

### 33. ¿Qué diferencia hay entre la ráfaga descendente y la ascendente en TETRA?

- a) La ascendente lleva más bits útiles que la descendente
- b) La ascendente es continua y la descendente, discontinua
- c) La descendente es continua y da referencia de sincronismo; la ascendente es discontinua

**Respuesta correcta:** c) · **Referencia:** §3.4 [EN392-2]

La estación base transmite sin interrupción, lo que da a los terminales una referencia permanente de temporización, mientras que cada terminal solo transmite en su intervalo. Además, la ráfaga descendente normal lleva 432 bits útiles y la ascendente, 336, de modo que la opción A también es falsa.

### 34. ¿Qué distingue a una llamada de difusión de una llamada de grupo en TETRA?

- a) Que la de difusión llega a más usuarios que la de grupo
- b) Que la de difusión ocupa cuatro intervalos y la de grupo, solo uno
- c) Que la de difusión es unidireccional: los receptores solo escuchan y no pueden responder

**Respuesta correcta:** c) · **Referencia:** §4.1.1 [EN392-9]

En una llamada de grupo cualquiera de los participantes puede tomar la palabra apretando el botón; en una llamada de difusión, no. El número de destinatarios no es lo que las diferencia, y ninguna de las dos ocupa cuatro intervalos por sí misma.

### 35. ¿Qué es la función DGNA en una red TETRA?

- a) Un algoritmo de derivación de claves de grupo a partir de la clave común
- b) La asignación dinámica de grupos, que permite crear y cargar grupos en los terminales por el aire
- c) Un mecanismo de reparto geográfico de las portadoras entre células vecinas

**Respuesta correcta:** b) · **Referencia:** §4.1.1 [EN392-9]

<em>Dynamic Group Number Assignment</em> permite montar en segundos un grupo mixto para una emergencia concreta —policía, bomberos y sanitarios de un mismo incidente— y disolverlo al terminar, todo desde una consola. En radio convencional habría que reprogramar físicamente cada equipo.

### 36. ¿En qué consiste la prioridad con desalojo?

- a) En que una llamada de prioridad suficiente corta una comunicación en curso de prioridad inferior cuando no hay canal libre
- b) En que las llamadas de mayor prioridad se sitúan al principio de la cola de espera
- c) En que el centro de mando puede expulsar a un terminal de la red de forma permanente

**Respuesta correcta:** a) · **Referencia:** §4.1.2 [EN392-9]

La opción B describe el escalón anterior, la prioridad de acceso, que ordena la cola pero no interrumpe a nadie. La opción C describe la inhabilitación remota. La diferencia entre los dos primeros escalones es la que hay entre esperar mejor y echar a otro.

### 37. ¿Cuál es la longitud máxima de datos de usuario de un SDS de tipo 4?

- a) 2.047 bits
- b) 64 bits
- c) 160 caracteres

**Respuesta correcta:** a) · **Referencia:** §4.2.1 [EN392-2]

Los tipos 1, 2 y 3 admiten 16, 32 y 64 bits respectivamente, y el mensaje de estado, 16 bits precodificados. El tipo 4 es el que se usa en la práctica para texto libre, posiciones y aplicaciones, y sobre él se define el SDS-TL, que añade identificación del protocolo de aplicación, acuse de recibo y encadenamiento.

### 38. Los mensajes SDS de una red TETRA viajan por los canales de control. ¿Qué consecuencia tiene esto para el dimensionado?

- a) Ninguna: al no ocupar canal de tráfico, el envío de posiciones es gratuito para la red
- b) Consumen capacidad de señalización, que es finita y compartida con el establecimiento de llamadas
- c) Obligan a reservar una portadora adicional por cada mil terminales

**Respuesta correcta:** b) · **Referencia:** §4.2.1 [EN392-2]

Es el error de diseño más común en despliegues de localización sobre TETRA. Las contramedidas habituales son espaciar el envío cuando el vehículo está parado, emitir por distancia recorrida en lugar de por tiempo, distribuir los envíos para que no coincidan y reservar capacidad de señalización para el establecimiento de llamada, que siempre tiene prioridad.

### 39. ¿Cuál es el caudal máximo de datos de TETRA Release 1 agregando los cuatro intervalos y sin protección de errores?

- a) 7,2 kbit/s
- b) 14,4 kbit/s
- c) 28,8 kbit/s

**Respuesta correcta:** c) · **Referencia:** §4.2.2 [EN392-2]

Cada intervalo aporta 7,2 kbit/s sin protección, 4,8 con protección baja y 2,4 con protección alta. Ese techo permite texto, posiciones, telemetría y consultas breves, pero no vídeo ni cartografía en tiempo real, y es exactamente la razón de ser de TEDS.

### 40. ¿Qué protocolo permite a TETRA transportar tráfico IP en el servicio de datos por paquetes?

- a) CMCE
- b) SDS-TL
- c) SNDCP

**Respuesta correcta:** c) · **Referencia:** §4.2.2 [EN392-2]

El <em>Subnetwork Dependent Convergence Protocol</em> pertenece a la capa 3 del interfaz aire y hace que, desde el punto de vista de la aplicación, el terminal sea un dispositivo IP más. El SDS-TL es la capa de transporte de la mensajería corta, y el CMCE es la entidad de control de llamada en modo circuito.

### 41. ¿Qué característica define a la clave de autenticación K de TETRA?

- a) Que es compartida por el terminal y la red y nunca se transmite por el aire
- b) Que se genera en cada registro y se distribuye cifrada mediante OTAR
- c) Que es común a todos los terminales de un mismo grupo de conversación

**Respuesta correcta:** a) · **Referencia:** §4.3.1 [EN392-7]

La autenticación es de desafío-respuesta con clave simétrica: la red envía un número aleatorio, el terminal calcula la respuesta con K y la red compara. La opción B describe el comportamiento de la clave común CCK, y la opción C, el de la clave de grupo GCK.

### 42. ¿De dónde procede la clave derivada DCK?

- a) De la carga previa en el terminal antes de su puesta en servicio
- b) Del propio proceso de autenticación
- c) De la combinación de la clave de grupo con la clave común

**Respuesta correcta:** b) · **Referencia:** §4.3.1 [TTR001-11]

Autenticar y cifrar están encadenados: de la autenticación se deriva una clave de cifrado propia de ese terminal y esa sesión. Por eso una red que no autentica tiene que conformarse con claves estáticas precargadas, que son las mismas para todos y durante mucho tiempo. La opción C describe la MGCK.

### 43. ¿Qué defensa aporta la autenticación mutua en TETRA?

- a) Impide que se puedan reproducir mensajes cortos capturados previamente
- b) Protege frente a una estación base falsa, porque el terminal verifica también a la red
- c) Garantiza que el operador de la red no pueda escuchar las comunicaciones

**Respuesta correcta:** b) · **Referencia:** §4.3.1 [EN392-7]

Sin autenticación de la red, un atacante puede montar una estación base falsa que atraiga a los terminales de la zona y desde ella degradar la seguridad, capturar tráfico o inyectar mensajes. Que el operador no pueda escuchar es cosa del cifrado extremo a extremo, no de la autenticación.

### 44. ¿Qué caracteriza a la clase de seguridad SC3 del interfaz aire?

- a) Que no aplica cifrado, aunque puede cifrar las identidades mediante ESI
- b) Que cifra con clave estática precargada y no exige autenticación
- c) Que emplea clave derivada y clave común, y exige autenticación

**Respuesta correcta:** c) · **Referencia:** §4.3.2 [TTR001-11]

La opción A describe SC1 y la opción B, SC2, que es además la clase propia del modo directo. SC3 es la configuración recomendada, y admite la variante SC3G cuando se añade cifrado propio por grupo con GCK y MGCK.

### 45. ¿Qué reveló la vulnerabilidad CVE-2022-24402, divulgada en 2023?

- a) Que la clave de 80 bits del algoritmo TEA1 se reduce deliberadamente a unos 32 bits efectivos
- b) Que el algoritmo TEA2 puede descifrarse observando el tiempo de red
- c) Que el cifrado extremo a extremo carece de protección antirrepetición

**Respuesta correcta:** a) · **Referencia:** §4.3.2 [TETRABURST]

Esa reducción permite romper la clave por fuerza bruta en minutos con un ordenador doméstico. La TCCA ha confirmado que fue intencionada y la justifica en el cumplimiento del Acuerdo de Wassenaar de control de exportación. La opción B mezcla la CVE-2022-24401 con otro algoritmo, y la opción C corresponde a la divulgación de 2025.

### 46. ¿A qué algoritmos sustituyen respectivamente TEA5, TEA6 y TEA7 del conjunto TEA set B?

- a) A TEA2, TEA3 y TEA1
- b) A TEA1, TEA2 y TEA3
- c) A TEA3, TEA4 y TEA2

**Respuesta correcta:** a) · **Referencia:** §4.3.2 [TCCA-B]

TEA5 sucede a TEA2 para las redes de emergencia europeas, TEA6 sucede a TEA3 para redes militares y de emergencia extraeuropeas afines, y TEA7 sucede a TEA1 como el único del nuevo conjunto disponible para infraestructuras críticas y uso civil general. El conjunto se liberó en octubre de 2022.

### 47. Según la TCCA, ¿qué longitud de clave tienen TEA5 y TEA6, y qué ocurre con TEA7?

- a) Los tres tienen 80 bits, igual que el conjunto anterior
- b) Los tres tienen 256 bits, sin ninguna restricción
- c) TEA5 y TEA6 tienen 192 bits, y TEA7 conserva una reducción efectiva a 56 bits

**Respuesta correcta:** c) · **Referencia:** §4.3.2 [TCCA-RD]

La reducción de TEA7 responde a las mismas razones de control de exportación que en su día afectaron a TEA1. La lección de fondo, muy citable, es que la debilidad de TEA1 no fue un error de diseño sino una decisión de política de exportación, y que el algoritmo civil del nuevo conjunto sigue arrastrando esa condición.

### 48. Una red TETRA mantiene TEA1 activo «por compatibilidad» junto a algoritmos más fuertes. ¿Qué problema plantea, según la divulgación de 2025?

- a) Ninguno, siempre que los usuarios sensibles tengan configurado un algoritmo distinto
- b) Que soportar TEA1 junto a otros algoritmos permite recuperar también la clave de los demás
- c) Que obliga a reducir el número de grupos de conversación de la red

**Respuesta correcta:** b) · **Referencia:** §4.3.2 [2TETRA]

Es la CVE-2025-52943 de 2TETRA:2BURST, presentada en Black Hat USA el 7 de agosto de 2025. Su consecuencia práctica es directa: no basta con dejar de usar TEA1, hay que dejar de soportarlo, y en un pliego eso se traduce en prohibirlo expresamente y no en desaconsejarlo.

### 49. ¿Sobre qué tecnología está construida la red SIRDEE del Estado español?

- a) Sobre TETRA, en la banda de 380 a 400 MHz
- b) Sobre TETRAPOL, de acceso FDMA y canalización de 12,5 kHz
- c) Sobre DMR, en la banda de 410 a 430 MHz

**Respuesta correcta:** b) · **Referencia:** §5.1 [SIRDEE]

Es la confusión más penalizada del tema. El SIRDEE, en servicio desde el año 2000, se decidió cuando TETRA aún no estaba maduro comercialmente. Las redes autonómicas y municipales, decididas más tarde, sí son en su mayoría TETRA, lo que impide resolver la interoperabilidad entre niveles mediante la ISI.

### 50. ¿Qué reserva la nota UN-28 del CNAF en las subbandas 380-385 y 390-395 MHz?

- a) Redes de servicios de seguridad de las Fuerzas y Cuerpos de Seguridad del Estado y redes de servicios de emergencia
- b) Sistemas digitales de acceso aleatorio de canales para uso civil y profesional
- c) Servicios de banda ancha para protección pública y socorro en catástrofes

**Respuesta correcta:** a) · **Referencia:** §3.1 · §5.2 [CNAF]

Son la excepción a la reserva de la banda 235-399,9 MHz para uso exclusivo del Estado en sistemas del Ministerio de Defensa, y se establecen de conformidad con la Decisión CEPT ECC/DEC(08)05. La opción B corresponde a la nota UN-31, y la opción C, a los bloques de 452-457,5 y 462-467,5 MHz.

### 51. ¿Qué subbandas destina el CNAF a «sistemas digitales de acceso aleatorio de canales (TETRA y otros)» y con qué canalización?

- a) 380-385 y 390-395 MHz, con canalización de 12,5 kHz
- b) 450-470 MHz, con canalización de 6,25 kHz
- c) 410-415,3 y 420-425,3 MHz, con canalización de 25 kHz

**Respuesta correcta:** c) · **Referencia:** §3.1 [CNAF]

Es la nota UN-31, dentro de la subbanda 410-430 MHz reservada a banda estrecha en modalidad dúplex con separación de 10 MHz entre transmisión y recepción. Es la única mención expresa de TETRA en el CNAF español.

### 52. ¿Cuál es el Cuadro Nacional de Atribución de Frecuencias vigente en España?

- a) La Orden ETU/1033/2017, de 25 de octubre
- b) La Orden ETD/1449/2021, de 16 de diciembre
- c) La Orden TDF/732/2026, de 10 de julio

**Respuesta correcta:** c) · **Referencia:** §3.1 · §5.2 [CNAF]

Se publicó en el BOE núm. 173, de 17 de julio de 2026, y deroga la Orden ETD/1449/2021 con efectos de 18 de julio de 2026. Su motivo declarado es incorporar las previsiones de la Conferencia Mundial de Radiocomunicaciones de 2023, en vigor en su mayoría desde el 1 de enero de 2025. Quien estudie con material anterior al verano de 2026 citará una orden derogada.

### 53. Según la Ley 11/2022, ¿qué naturaleza jurídica tiene el espectro radioeléctrico?

- a) Es un bien patrimonial del Estado, susceptible de enajenación
- b) Es un bien de dominio público, cuya titularidad y administración corresponden al Estado
- c) Es un recurso de titularidad compartida entre el Estado y las comunidades autónomas

**Respuesta correcta:** b) · **Referencia:** §5.2 [LGTel]

Lo establece el artículo 85.1 de la Ley 11/2022, General de Telecomunicaciones. De ahí se deduce que nadie es propietario de una frecuencia, que su uso requiere título habilitante estatal y que ese título está sujeto a condiciones, tiene plazo y puede modificarse o revocarse.

### 54. Un ayuntamiento explota una red TETRA propia para sus servicios de emergencia. ¿Qué título habilitante ampara su uso del espectro?

- a) Una afectación demanial, conforme al artículo 88.5.b) de la Ley 11/2022
- b) Una autorización individual de uso privativo para autoprestación
- c) Una concesión administrativa, previa inscripción como operador de comunicaciones electrónicas

**Respuesta correcta:** a) · **Referencia:** §5.2 [LGTel]

El precepto otorga el uso privativo para autoprestación mediante autorización individual «salvo en el caso de Administraciones públicas, que requerirán de afectación demanial». La concesión de la opción C exigiría además ostentar la condición de operador de comunicaciones electrónicas, según el artículo 88.6, que no es el caso de un ayuntamiento que se autopresta el servicio.

### 55. ¿Cuál es la duración general de los derechos de uso privativo del dominio público radioeléctrico sin limitación de número?

- a) Hasta el 31 de diciembre del año natural en que cumplan su quinto año de vigencia, renovables por periodos de cinco años
- b) Veinte años, prorrogables una sola vez
- c) Diez años improrrogables

**Respuesta correcta:** a) · **Referencia:** §5.2 [LGTel]

Lo fija el artículo 94.1 de la Ley 11/2022. La duración mínima de veinte años de la opción B corresponde a los derechos de uso privativo con limitación de número, que son los que se otorgan por licitación, como los de la telefonía móvil.

### 56. Según el artículo 4.1 de la Ley 11/2022, ¿qué servicios de telecomunicaciones tienen la consideración de servicio público?

- a) Todos los servicios disponibles al público, por su condición de servicios de interés general
- b) Solo los de seguridad nacional, defensa nacional, seguridad pública, seguridad vial y protección civil
- c) Únicamente los incluidos en el servicio universal

**Respuesta correcta:** b) · **Referencia:** §5.2 [LGTel]

El precepto dice literalmente que «sólo tienen la consideración de servicio público los servicios regulados en este artículo», y el artículo se titula precisamente así. Es la excepción a la regla general del artículo 2, que declara las telecomunicaciones servicios de interés general prestados en régimen de libre competencia.

### 57. ¿Qué exige la medida mp.com.4.2 del Esquema Nacional de Seguridad?

- a) Que todas las comunicaciones se cifren con algoritmos aprobados por el Centro Criptológico Nacional
- b) Que se realicen pruebas periódicas del plan de continuidad del servicio
- c) Que, si se emplean comunicaciones inalámbricas, sea en un segmento separado

**Respuesta correcta:** c) · **Referencia:** §5.2 [ENS]

Pertenece a la medida mp.com.4, «separación de flujos de información en la red», que no aplica en categoría BÁSICA y cuyos refuerzos son R1 con VLAN, R2 con VPN, R3 con medios físicos separados y R4 en los puntos de interconexión. Es el precepto que se cita cuando alguien propone conectar la red radio al segmento ofimático general.

### 58. ¿Cuál de estos NO es un modo degradado propio de un sistema TETRA?

- a) El repliegue local de la estación base, que sigue troncalizando en su célula
- b) El paso de la clase de seguridad SC3 a la SC2 al perder el enlace con el centro de autenticación
- c) La conmutación automática de los terminales a la red de telefonía móvil comercial

**Respuesta correcta:** c) · **Referencia:** §5.3 [TTR001-11]

No es un modo previsto por el estándar: los terminales híbridos que combinan TETRA y banda ancha son una solución de producto, no un modo degradado normalizado. Los tres modos degradados propios son el repliegue local, el modo directo y el repliegue de clase de seguridad.

### 59. ¿Qué introduce TEDS respecto de TETRA Release 1?

- a) Anchos de canal de 25, 50, 100 y 150 kHz y modulaciones de orden superior con adaptación al enlace
- b) La sustitución del acceso TDMA por acceso ortogonal por división de frecuencia
- c) La incorporación del modo directo y de los repetidores de modo directo

**Respuesta correcta:** a) · **Referencia:** §5.4 [TR102580]

Las modulaciones añadidas son π/8-D8PSK, 4-QAM, 16-QAM y 64-QAM, y el sistema elige entre ellas según la calidad de la señal, reservando el 4-QAM para el borde de la cobertura. TEDS es una mejora dentro de TETRA, no una tecnología distinta. El modo directo de la opción C existe desde la Release 1.

### 60. ¿En qué versión del 3GPP se normalizó el servicio MCPTT de voz de misión crítica?

- a) En la Release 8, junto con la introducción de LTE
- b) En la Release 13, culminada en 2016
- c) En la Release 17, junto con las primeras funciones de 5G avanzado

**Respuesta correcta:** b) · **Referencia:** §5.4 [3GPP-MC]

La especificación de requisitos es la TS 22.179. MCVideo y MCData llegaron en la Release 14. Los habilitadores previos del propio 3GPP fueron GCSE para las comunicaciones de grupo, eMBMS para la difusión eficiente y ProSe para la comunicación de proximidad, que aspira a replicar el modo directo de TETRA.

## Preguntas sobre los casos prácticos

### Caso 1. Incidente en un aparcamiento subterráneo del distrito de Salamanca

#### 1. En el supuesto planteado, la cobertura de la red municipal en el nivel −3 del aparcamiento es nula. ¿En qué modo deben trabajar las dotaciones que descienden a ese nivel?

- a) En modo troncalizado (TMO), porque la cobertura marginal del nivel −1 basta para llegar al −3.
- b) En modo directo (DMO), porque no hay cobertura de red; se oirán entre ellas, pero el CISEM no.
- c) En modo troncalizado con prioridad con desalojo, que amplía la cobertura de la célula al subsuelo.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.2.2

El modo directo funciona sin infraestructura: los terminales se comunican entre sí. La contrapartida es que la comunicación no llega a la red y, por tanto, el CISEM no la oye.

#### 2. ¿En qué modo deben trabajar el mando del incidente, la Policía Municipal en superficie y el CISEM?

- a) En modo troncalizado (TMO), que es donde hay despacho, grabación y visión de posiciones.
- b) En modo directo (DMO), para no consumir canales en una red del centro que está saturada.
- c) En modo directo a través de un DM-REP, que permite al CISEM grabar las comunicaciones.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.2.2

Quien tiene cobertura debe trabajar en TMO: la red aporta el despacho desde el centro, la grabación y la localización. El DM-REP no conecta con la red.

#### 3. ¿Qué función debe configurarse en el vehículo de mando estacionado en la rampa para que el CISEM no pierda a las dotaciones del nivel −3?

- a) DM-REP (repetidor), que retransmite el modo directo con más potencia hasta la consola del CISEM.
- b) Repliegue local de la estación base, que enlaza el modo directo con el núcleo de la red troncalizada.
- c) DM-GATE (pasarela), que recibe en modo directo y reinyecta la comunicación en la red troncalizada.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.2.3

La pasarela DM-GATE une el modo directo con la red troncalizada y devuelve al CISEM la audición, la posibilidad de hablar con el interior y la grabación.

#### 4. Si en la rampa se desplegara únicamente un DM-REP, ¿qué ocurriría?

- a) Las dotaciones se oirían más lejos entre sí, pero el CISEM seguiría sin enterarse de nada.
- b) El CISEM oiría a las dotaciones del nivel −3, pero no podría hablar con ellas ni grabarlas.
- c) Las dotaciones volverían automáticamente a TMO al quedar dentro del alcance del repetidor.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.2.3

El repetidor de modo directo amplía el alcance dentro del modo directo sin tocar la red: lo que entra en DMO sale en DMO. Solo la pasarela conecta con la red.

#### 5. ¿Por qué conviene que la pasarela sea el equipo embarcado del vehículo y no el portátil de un agente?

- a) Porque los portátiles de 1 W no admiten el modo directo, exclusivo de los embarcados.
- b) Porque el equipo embarcado de 10 W tiene bastante más alcance que el portátil de 1 W.
- c) Porque solo los equipos de 10 W pueden afiliarse a grupos creados desde la consola.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.2.3

Los equipos embarcados de gama profesional pueden actuar como DM-REP o DM-GATE, y su mayor potencia les da más alcance, lo que convierte al vehículo en el nodo de la intervención.

#### 6. ¿Qué función ha usado el operador del CISEM para crear el grupo INC-0340-SALAMANCA y cargarlo en los terminales de las unidades?

- a) La DGNA, que asigna al grupo una frecuencia física exclusiva programada en cada terminal.
- b) La ISI, que reprograma el grupo en cada terminal a través de su interfaz de datos PEI.
- c) La DGNA, que crea el grupo como entidad lógica y lo carga por el aire en los terminales.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §4.1.1

La asignación dinámica de grupos crea el grupo y lo carga desde la consola sin tocar los equipos. En TETRA el grupo es una entidad lógica (GSSI), no una frecuencia; en radio convencional habría que reprogramar equipo por equipo.

#### 7. Un terminal se afilia a INC-0340-SALAMANCA cuando la conversación del grupo ya ha empezado. ¿Qué ocurre?

- a) Debe esperar a que termine la conversación, porque la red solo avisa a los terminales al iniciarse cada llamada.
- b) Se incorpora a ella por la entrada tardía, posible porque la trama 18 de cada multitrama se reserva a señalización.
- c) Se incorpora gracias a la hipertrama, que repite la llamada de grupo completa cada 61,2 segundos de duración.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §4.1.1

La trama de control (la 18.ª de cada multitrama) permite a la red avisar a un terminal sin interrumpir el tráfico; por eso quien se afilia con la llamada iniciada se incorpora a ella.

#### 8. Con la red del centro saturada por otro operativo y sin ningún canal libre, ¿qué escalón de prioridad permite que una llamada del incidente corte otra de prioridad inferior?

- a) La prioridad de acceso, que ordena la cola de espera.
- b) La entrada tardía, que libera el canal más antiguo.
- c) La prioridad con desalojo (pre-emptive priority).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §4.1.2

La prioridad de acceso solo ordena la cola sin cortar a nadie; la prioridad con desalojo corta una comunicación en curso de prioridad inferior cuando no hay canal libre. Por encima está la llamada de emergencia.

#### 9. Un bombero del nivel −1 pulsa el botón de emergencia de su terminal. ¿Qué se produce?

- a) Establecimiento inmediato con máxima prioridad y desalojo, alarma con su identidad en el CISEM y canal de voz abierto sin pulsar el PTT.
- b) Envío de un mensaje de estado al CISEM, que lo encola por prioridad de acceso sin cortar ninguna de las llamadas en curso.
- c) Paso automático del terminal a modo directo, para que las dotaciones cercanas le oigan sin depender de la red.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §4.1.2

La llamada de emergencia es el nivel máximo: entra con desalojo en el grupo de emergencia, alerta a la consola con la identidad y, si se envía, la posición, y abre un canal de voz para que el centro oiga lo que ocurre aunque el agente esté incapacitado.

#### 10. La estación base que cubre la zona tiene 3 portadoras y dedica un intervalo al canal de control. ¿Cuántas conversaciones simultáneas admite esa célula?

- a) 12: el intervalo de control también cursa voz cuando la célula se satura.
- b) 11: 3 portadoras × 4 intervalos son 12 canales físicos, menos 1 de control.
- c) 9: cada portadora reserva un intervalo a señalización, y quedan 3 × 3.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §1.2 · §3.4

Cada portadora de 25 kHz se divide en 4 intervalos TDMA: 12 canales físicos. Solo uno se dedica al canal de control principal, de modo que quedan 11 para tráfico.

### Caso 2. Informe de seguridad sobre una oferta de renovación de terminales

#### 1. La oferta propone configurar TEA1 «por ser el de exportación libre». ¿Por qué es inaceptable?

- a) Porque su clave de 80 bits se reduce deliberadamente a unos 32 bits efectivos y se rompe en minutos (CVE-2022-24402).
- b) Porque su clave de 128 bits es incompatible con los terminales de exportación libre del parque municipal actual.
- c) Porque es un algoritmo sin clave que solo cifra la señalización y deja la voz del interfaz aire en claro.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §4.3.2

La clave de 80 bits de TEA1 se comprime a unos 32 bits efectivos, lo que permite romperla por fuerza bruta en minutos con un ordenador doméstico. La TCCA ha confirmado que la reducción fue intencionada (Acuerdo de Wassenaar).

#### 2. La oferta deja además TEA2 activo «por compatibilidad». ¿Mejora eso la seguridad de la red si TEA1 sigue soportado?

- a) Sí: los terminales negocian siempre el algoritmo más fuerte disponible, de modo que TEA1 nunca llegaría a usarse.
- b) Sí: TEA2 no tiene ninguna relación con TEA1, y basta con reservarlo para los grupos de conversación sensibles.
- c) No: en redes multicifrado, soportar TEA1 permite recuperar también la clave de los demás algoritmos (CVE-2025-52943).

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §4.3.2

La divulgación de agosto de 2025 demostró que admitir TEA1 junto a otros algoritmos compromete también a estos. No basta con dejar de usar TEA1: hay que dejar de soportarlo.

#### 3. ¿Qué exigencia concreta sobre algoritmos debe incorporarse al pliego de los 1.200 terminales?

- a) Desaconsejar TEA1 y exigir que los terminales lo conserven solo como algoritmo de reserva ante fallos.
- b) Prohibir expresamente TEA1 y exigir capacidad de migración a TEA set B (TEA5, TEA6 y TEA7) y a TAA2.
- c) Exigir TEA7 en sustitución de TEA2, por ser el algoritmo civil de 192 bits del TEA set B de la TCCA.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §4.3.2

TEA1 debe prohibirse, no desaconsejarse. En el TEA set B, TEA5 sustituye a TEA2, TEA6 a TEA3 y TEA7 a TEA1; TEA5 y TEA6 usan claves de 192 bits y TEA7 conserva una reducción efectiva a 56 bits.

#### 4. La red operaría en clase SC2 «para evitar la carga del centro de autenticación». ¿Qué clase debe exigirse?

- a) SC1, que evita la carga del centro de autenticación sin renunciar al cifrado del interfaz aire.
- b) SC2 con una clave estática más larga, que da la misma protección que SC3 sin autenticar.
- c) SC3, con clave derivada (DCK) y clave común (CCK), que exige autenticación, preferiblemente mutua.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §4.3.1

SC2 cifra con una clave estática precargada, la misma para todos y durante mucho tiempo; SC1 no cifra. SC3 usa una clave distinta por terminal que se renueva, y la autenticación mutua protege frente a una estación base falsa.

#### 5. ¿Por qué una red TETRA que no autentica queda condenada a la clave estática?

- a) Porque la DCK se deriva del propio proceso de autenticación: sin autenticación no hay clave derivada.
- b) Porque la DCK se distribuye cifrada con la SCK, que solo existe en las redes que no autentican.
- c) Porque la clave K viaja por el aire durante la autenticación y sin ella no se puede generar la CCK.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §4.3.1

Autenticar y cifrar están encadenados: del proceso de autenticación se deriva la DCK, propia de cada terminal y sesión. La clave K nunca se transmite por el aire.

#### 6. La oferta no incluye distribución de claves por el aire: se renovarían recogiendo los terminales en el almacén una vez al año. ¿Qué debe exigirse?

- a) Una renovación semestral en el almacén, que es la periodicidad mínima que fija el ENS para las claves.
- b) OTAR y un procedimiento de inhabilitación remota (stun y kill) para terminales perdidos o robados.
- c) Claves estáticas de mayor longitud, que no necesitan renovarse durante la vida útil de los terminales.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.3.1

Recoger 1.200 terminales impide reaccionar ante un compromiso de clave o la baja de un usuario. OTAR permite renovar las claves de miles de terminales sin recogerlos.

#### 7. El fabricante alega que «el cifrado de interfaz aire ya protege la comunicación de punta a punta». ¿Qué debe responderse?

- a) Que es falso: ese cifrado se descifra en la estación base y desde ahí la comunicación circula en claro por la infraestructura.
- b) Que es cierto: el cifrado de interfaz aire acompaña a la comunicación hasta que la descifra el terminal receptor.
- c) Que es cierto si la red trabaja en SC3, porque esa clase extiende el cifrado hasta la consola del centro de despacho.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §4.3.2 · §4.3.3

El cifrado de interfaz aire protege el tramo terminal ↔ estación base. El cifrado extremo a extremo cifra en el terminal emisor y descifra en el receptor; son complementarios, no alternativos.

#### 8. ¿Frente a quién NO protege el cifrado de interfaz aire de la red municipal?

- a) Frente a quien escuche con un receptor el tramo radio entre el terminal y la estación base.
- b) Frente al operador de la red y al personal con acceso a los equipos o a las grabaciones.
- c) Frente a quien capte por radio la señalización que intercambian el terminal y la red.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §4.3.3

Como se descifra en la estación base, no protege frente a quien accede a la infraestructura: el operador, el personal técnico, las grabaciones o un compromiso de los enlaces de transporte. Sí protege el tramo radio.

#### 9. Si finalmente se implanta cifrado extremo a extremo, ¿qué debe exigir el pliego?

- a) Basta exigir «cifrado extremo a extremo», porque el ETSI impone un único algoritmo común a todos los fabricantes.
- b) Basta exigir AES-128, que garantiza por sí solo 128 bits de entropía efectiva en cualquier implementación.
- c) Algoritmo y longitud de clave nombrados, protección frente a repetición, autenticación del contenido y derecho de auditoría.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §4.3.3

El ETSI no impone algoritmo de cifrado extremo a extremo. La CVE-2025-52941 halló una variante de AES-128 con entropía efectiva de 56 bits, y otras CVE de 2025 describen repetición e inyección de voz.

#### 10. Se propone conectar las consolas de despacho al segmento de la ofimática municipal. ¿Qué medida del ENS lo impide y qué exige en categoría MEDIA?

- a) mp.com.4, separación de flujos de información en la red, que en MEDIA exige [R1 o R2 o R3].
- b) mp.com.4, separación de flujos de información en la red, que en MEDIA todavía no se aplica.
- c) op.exp.10, protección de claves criptográficas, que exige que las consolas estén en otro edificio.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §5.2 · mp.com.4 ENS

mp.com.4 obliga a segregar el tráfico; en MEDIA exige uno de los refuerzos (segmentación lógica con VLAN, VPN o medios físicos separados), y en BÁSICA no aplicaría.

### Caso 3. Renovación del título habilitante y decisión de evolución

#### 1. Un informe interno afirma que el Ayuntamiento tiene concedidas las frecuencias «a perpetuidad por su condición de Administración pública». ¿Cuál es el punto de partida para corregirlo?

- a) El espectro es dominio público municipal dentro del término del Ayuntamiento, aunque su uso esté sujeto a inscripción registral.
- b) Las frecuencias solo se conceden a perpetuidad a la Administración General del Estado, y no a las entidades locales.
- c) El espectro es dominio público cuya titularidad corresponde al Estado: el Ayuntamiento solo tiene un derecho de uso con título habilitante.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §5.2 · art. 85.1 Ley 11/2022

Conforme al artículo 85.1 de la Ley 11/2022, el espectro radioeléctrico es un bien de dominio público cuya titularidad y administración corresponden al Estado.

#### 2. ¿Qué modalidad de uso del espectro corresponde a la red de radio municipal?

- a) Uso común, como el de las redes Wi-Fi abiertas.
- b) Uso privativo en régimen de autoprestación.
- c) Uso especial, por ser el titular una Administración.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §5.2 · art. 88.1 Ley 11/2022

El uso privativo es la explotación en exclusiva o por un número limitado de usuarios de determinadas frecuencias en un mismo ámbito físico (art. 88.1); la red municipal la explota el propio Ayuntamiento para sus servicios, es decir, en autoprestación.

#### 3. Para la renovación, alguien propone solicitar una concesión. ¿Es correcto?

- a) No: la concesión exige ser operador (art. 88.6); a una Administración en autoprestación le corresponde la afectación demanial.
- b) Sí: la concesión demanial es el título propio de las Administraciones públicas para el uso privativo del espectro.
- c) No: lo que procede es una autorización individual, como a cualquier otro usuario en régimen de autoprestación.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §5.2 · art. 88.5.b) Ley 11/2022

Conforme al artículo 88.5.b) de la Ley 11/2022, el uso privativo para autoprestación se otorga por autorización individual «salvo en el caso de Administraciones públicas, que requerirán de afectación demanial».

#### 4. ¿Qué duración tiene el derecho de uso privativo que se renueva?

- a) Indefinida, mientras el Ayuntamiento siga pagando la tasa por reserva del dominio público radioeléctrico.
- b) Hasta el 31 de diciembre del año en que cumpla su quinto año de vigencia, renovable por periodos de cinco años.
- c) Diez años improrrogables, tras los cuales hay que solicitar un título habilitante completamente nuevo.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §5.2 · art. 94.1 Ley 11/2022

El artículo 94.1 de la Ley 11/2022 fija la duración de los derechos de uso privativo sin limitación de número: hasta el 31 de diciembre del año natural en que cumplan su quinto año de vigencia, renovables por periodos de cinco años.

#### 5. Se propone dar servicio a limpieza viaria y a parques y jardines «en la banda de emergencias, que es la nuestra». ¿Es posible?

- a) Sí: la banda de emergencias corresponde al Ayuntamiento por su condición de Administración pública titular de la red.
- b) Sí, siempre que limpieza y parques usen grupos de conversación distintos de los de Policía Municipal y Bomberos.
- c) No: la nota UN-28 reserva 380-385 / 390-395 MHz a redes de seguridad del Estado y de emergencias, y esos servicios no lo son.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §3.1 · nota UN-28 CNAF

La banda la determina el servicio que se presta, no la condición del solicitante. La nota UN-28 reserva esas subbandas a redes de seguridad de las Fuerzas y Cuerpos de Seguridad del Estado y a redes de servicios de emergencia.

#### 6. ¿Qué banda correspondería a la red de limpieza viaria y de parques y jardines?

- a) 410-415,3 / 420-425,3 MHz (nota UN-31), con canalización de 25 kHz y separación dúplex de 10 MHz.
- b) 698-703 / 753-758 MHz, el bloque PPDR de banda ancha reservado al ámbito autonómico y local.
- c) 380-385 / 390-395 MHz, con canalización de 12,5 kHz para los servicios que no son de emergencia.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §3.1 · nota UN-31 CNAF

La nota UN-31 destina esas subbandas a «sistemas digitales de acceso aleatorio de canales (TETRA y otros)». El bloque de 698-703 / 753-758 MHz es para banda ancha PPDR, no para servicios municipales generales.

#### 7. Un proveedor propone sustituir la red TETRA por teléfonos comerciales con una aplicación de push-to-talk. ¿Cuál de estos argumentos rebate correctamente la propuesta?

- a) TETRA ofrece mucho más caudal de datos que las redes móviles comerciales de banda ancha para vídeo y cartografía.
- b) La telefonía móvil comercial no admite ningún tipo de comunicación de grupo entre varios usuarios a la vez.
- c) En una red comercial el Ayuntamiento no decide a quién se desaloja, y un móvil no se comunica con otro si cae la red.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §5.1 · §5.3

TETRA ofrece prioridad y desalojo gobernados por el titular de la red y modo directo sin infraestructura. Su punto débil es el caudal (28,8 kbit/s en Release 1), y la telefonía comercial sí tiene grupos, aunque de establecimiento lento.

#### 8. ¿Qué tiempo de establecimiento de llamada de grupo ofrece TETRA, frente a la telefonía comercial?

- a) Por debajo de 300 ms, frente a segundos.
- b) Por debajo de 3 s, frente a varios minutos.
- c) Por debajo de 30 ms, frente a unos 300 ms.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §5.1

El establecimiento de la llamada de grupo por debajo de 300 ms es uno de los rasgos que distinguen la radiocomunicación móvil privada de la telefonía celular pública.

#### 9. Durante el apagón del 28 de abril de 2025 la red municipal de radio siguió operativa. ¿Qué lección de fondo debe extraerse?

- a) Que la red TETRA no depende de la energía eléctrica, porque sus terminales portátiles funcionan con batería.
- b) Que un servicio crítico solo es resiliente si lo son todas sus dependencias, empezando por la energía (mp.if.4 ENS).
- c) Que la telefonía comercial es igual de resiliente si se contratan tarifas con prioridad para emergencias.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §5.3 · mp.if.4 ENS

La red siguió operativa gracias al respaldo energético de los emplazamientos (baterías en los repetidores). Cada emplazamiento debe tener baterías para varias horas y, en los principales, grupo electrógeno, con respaldo en mp.if.4.

#### 10. ¿Qué vía de evolución es defendible y qué espectro tiene reservado el CNAF para las redes locales?

- a) Sustitución inmediata de TETRA por MCPTT, con el bloque de 733-736 / 788-791 MHz reservado al ámbito local.
- b) Sustitución de TETRA por TEDS, que no necesita más espectro por canal y libera la banda TETRA del Ayuntamiento.
- c) Coexistencia: TETRA para la voz crítica y banda ancha (MCPTT, Release 13) para el caudal, con 698-703 / 753-758 MHz.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §5.4

El modelo es de coexistencia por fases. El CNAF reserva 733-736 / 788-791 MHz al sistema PPDR nacional y 698-703 / 753-758 MHz a las redes autonómicas y locales. TEDS amplía TETRA, pero exige más espectro por canal.
