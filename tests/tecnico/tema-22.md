# Test del tema 22. Arquitectura de sistemas cliente/servidor y multicapas

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-22.html>

## Batería de preguntas

### 1. ¿Qué distingue a la "arquitectura de sistemas" de la "arquitectura de red"?

- a) La arquitectura de sistemas organiza componentes software y sus relaciones; la de red es la topología física/lógica de los dispositivos de comunicaciones
- b) Son sinónimos exactos, usados indistintamente en toda la literatura técnica
- c) La arquitectura de red incluye siempre a la de sistemas como subconjunto

**Respuesta correcta:** a) · **Referencia:** §1.1 [FOWLER-PEAA]

Son nociones relacionadas pero independientes: una misma arquitectura de sistemas puede desplegarse sobre topologías de red distintas.

### 2. ¿Qué avance tecnológico hizo posible la transición del modelo centralizado (mainframe) al modelo cliente/servidor?

- a) La sustitución de las terminales tontas por impresoras de red
- b) La popularización del PC y de las redes de área local (LAN) a finales de los 80
- c) La invención del protocolo HTTP en 1991

**Respuesta correcta:** b) · **Referencia:** §1.2.2 [GARTNER-3TIER]

Permitió repartir la lógica y la interfaz entre puestos de usuario, mientras los recursos compartidos seguían en servidores especializados.

### 3. ¿Cuál de los siguientes es un "atributo de calidad" (requisito no funcional) que persigue una arquitectura de sistemas?

- a) El número de líneas de código del proyecto
- b) El lenguaje de programación elegido por el equipo
- c) La escalabilidad, entendida como capacidad de crecer en carga sin rediseñar

**Respuesta correcta:** c) · **Referencia:** §1.1 [FOWLER-PEAA]

Junto con disponibilidad, mantenibilidad, seguridad, rendimiento e interoperabilidad, son los atributos que determinan si una arquitectura es adecuada para un contexto dado.

### 4. Ordenando cronológicamente la evolución de los modelos arquitectónicos, ¿qué secuencia es correcta?

- a) Centralizado → cliente/servidor → 3/n-capas → SOA → microservicios/contenedores/nube
- b) SOA → microservicios → cliente/servidor → centralizado
- c) Microservicios → 3-capas → SOA → cliente/servidor

**Respuesta correcta:** a) · **Referencia:** §1.2.3

Cada oleada resuelve limitaciones de la anterior, sin eliminar por completo a las precedentes (SOAP sigue en uso, por ejemplo).

### 5. ¿Qué relación existe entre este Tema 22 y el Tema 31 del temario?

- a) Son temas idénticos que se repiten por error en el temario oficial
- b) El Tema 31 desarrolla en profundidad IaaS/PaaS/SaaS y los modelos de despliegue de nube que el Tema 22 solo sitúa como cierre de la evolución arquitectónica
- c) El Tema 31 trata exclusivamente de seguridad y no tiene relación con este tema

**Respuesta correcta:** b) · **Referencia:** §1.2.3 [RELACIÓN CON OTROS TEMAS]

Este tema sienta las bases arquitectónicas (cliente/servidor, capas, servicios) sobre las que se apoya la infraestructura de provisión que trata el Tema 31.

### 6. En la relación cliente/servidor, ¿qué característica define el patrón de interacción "petición-respuesta"?

- a) El servidor inicia siempre la comunicación hacia el cliente
- b) Cliente y servidor envían mensajes de forma simultánea sin orden definido
- c) El cliente inicia la comunicación solicitando un servicio; el servidor responde, sin iniciativa propia hacia el cliente en el modelo clásico

**Respuesta correcta:** c) · **Referencia:** §2.1 [FOWLER-PEAA]

Es una relación asimétrica: el cliente conoce (o localiza) al servidor, no al revés.

### 7. ¿Qué caracteriza a un "cliente ligero" (thin client) frente a un "cliente pesado"?

- a) Concentra en el servidor casi toda la lógica de negocio; el cliente solo renderiza — el navegador web es el ejemplo paradigmático
- b) Mantiene siempre una copia local completa de la base de datos
- c) No puede comunicarse con ningún servidor remoto

**Respuesta correcta:** a) · **Referencia:** §2.2.1 [FOWLER-PEAA]

El cliente pesado, en cambio, ejecuta lógica de negocio local y complica el despliegue.

### 8. ¿Cuál fue el motor histórico que impulsó la migración de aplicaciones de escritorio (cliente pesado) hacia aplicaciones web (cliente ligero)?

- a) La desaparición de los sistemas operativos de escritorio
- b) El problema de despliegue del cliente pesado: instalar y actualizar software en cada puesto tiene un coste de mantenimiento alto
- c) La obligación legal de usar exclusivamente HTML

**Respuesta correcta:** b) · **Referencia:** §2.2.1 [DATO CLAVE]

Un cliente ligero centraliza la actualización en el servidor, transparente al usuario final.

### 9. ¿Qué responsabilidad es propia del servidor y no tiene equivalente directo en el cliente clásico?

- a) La renderización de la interfaz de usuario
- b) La validación del formato de un correo electrónico introducido en un formulario
- c) La gestión de recursos compartidos y el control de concurrencia ante accesos simultáneos de varios clientes

**Respuesta correcta:** c) · **Referencia:** §2.2.2

Exige mecanismos como bloqueos, control de concurrencia optimista o transacciones para evitar que accesos simultáneos corrompan el recurso.

### 10. ¿Qué diferencia al escalado "vertical" del escalado "horizontal"?

- a) El vertical añade más CPU/memoria a una misma máquina (con límite físico); el horizontal añade más máquinas/instancias en paralelo, sin techo físico
- b) Son términos sinónimos usados indistintamente
- c) El horizontal solo es aplicable a bases de datos, nunca a servidores de aplicaciones

**Respuesta correcta:** a) · **Referencia:** §2.2.2 [DATO CLAVE]

Las arquitecturas modernas priorizan el horizontal porque además aporta tolerancia a fallos.

### 11. ¿Qué es el "middleware" en una arquitectura cliente/servidor?

- a) Un sinónimo de "servidor de base de datos"
- b) Software intermedio que oculta la complejidad de la comunicación distribuida, ofreciendo una interfaz de más alto nivel (p. ej. ODBC/JDBC, MOM, ORB)
- c) El conjunto de cables y conmutadores de la red física

**Respuesta correcta:** b) · **Referencia:** §2.2.3 [FOWLER-PEAA]

Sin él, cada aplicación tendría que resolver por sí misma la serialización, la localización de servicios o la tolerancia a fallos de red.

### 12. ¿Qué tipo de middleware es la base técnica de la arquitectura orientada a eventos (EDA, §7.2)?

- a) El middleware de acceso a datos (ODBC/JDBC)
- b) El middleware transaccional de commit en dos fases
- c) El middleware orientado a mensajes (MOM), como JMS, RabbitMQ o Kafka

**Respuesta correcta:** c) · **Referencia:** §2.2.3 [RELACIÓN CON OTROS TEMAS]

Permite el envío de mensajes/eventos asíncronos entre aplicaciones sin acoplamiento directo emisor-receptor.

### 13. El Tema 34 del temario desarrolla en profundidad...

- a) El modelo TCP/IP y el modelo OSI: la infraestructura de comunicaciones sobre la que se apoyan, sin necesidad de conocerla en detalle, los protocolos de aplicación de este Tema 22
- b) Los procedimientos almacenados y disparadores de bases de datos relacionales
- c) El diseño de interfaces de usuario accesibles

**Respuesta correcta:** a) · **Referencia:** §2.2.4 [RELACIÓN CON OTROS TEMAS]

Este tema se sitúa deliberadamente en el nivel de aplicación de la pila de protocolos.

### 14. En días de campaña de renovación del Padrón, con picos de tráfico en la Sede Electrónica, ¿qué estrategia de escalado permite añadir capacidad solo durante el pico y retirarla después?

- a) El escalado vertical exclusivamente
- b) El escalado horizontal, añadiendo instancias temporales del servidor de aplicaciones detrás de un balanceador de carga
- c) Reducir el número de campos del formulario de solicitud

**Respuesta correcta:** b) · **Referencia:** §2.2.2 [EJEMPLO DE APLICACIÓN EN EL AYTO]

El escalado vertical exigiría sobredimensionar permanentemente el hardware, con coste ocioso el resto del año.

### 15. En la arquitectura de dos capas (2-Tier), ¿dónde reside la lógica de negocio?

- a) Exclusivamente en un servidor de aplicaciones intermedio
- b) Nunca en el cliente, siempre en un tercer nivel
- c) De forma ambigua, repartida entre el cliente y el servidor de datos (procedimientos almacenados y disparadores)

**Respuesta correcta:** c) · **Referencia:** §3.1 [DATO CLAVE]

Esta ambigüedad es precisamente lo que resuelve el modelo de 3 capas al introducir un lugar único y claro para la lógica de negocio.

### 16. ¿Qué tema del temario desarrolla en detalle los procedimientos almacenados y disparadores que en 2-Tier concentran lógica en el servidor de datos?

- a) El Tema 19 (lenguajes de interrogación de bases de datos, ANSI SQL, procedimientos almacenados y disparadores)
- b) El Tema 24 (desarrollo para dispositivos móviles)
- c) El Tema 33 (comunicaciones y medios de transmisión)

**Respuesta correcta:** a) · **Referencia:** §3.1 [RELACIÓN CON OTROS TEMAS]

Es una referencia cruzada explícita señalada en el §3.1 de este tema.

### 17. ¿Cuál es la ventaja arquitectónica central de introducir el servidor de aplicaciones en el modelo de 3 capas?

- a) Eliminar por completo la necesidad de una base de datos
- b) El desacoplamiento: el cliente ya no conoce el esquema de datos, solo el contrato que expone la capa de negocio
- c) Reducir a la mitad el número de líneas de código del cliente

**Respuesta correcta:** b) · **Referencia:** §3.2 [DATO CLAVE]

Cambiar el modelo de datos, o incluso el motor de base de datos, no debería requerir tocar el cliente.

### 18. Además del desacoplamiento, ¿qué mejora de rendimiento aporta el servidor de aplicaciones frente a que cada cliente se conecte directamente al SGBD (como en 2-Tier)?

- a) Elimina por completo la necesidad de autenticación
- b) Convierte automáticamente el SGBD relacional en NoSQL
- c) Puede agrupar y reutilizar conexiones a la base de datos mediante un pool de conexiones, en lugar de que cada cliente mantenga la suya propia

**Respuesta correcta:** c) · **Referencia:** §3.2

El número de conexiones concurrentes al SGBD es un recurso finito, y esto mejora sustancialmente la escalabilidad.

### 19. ¿Qué distingue una "capa lógica" (layer) de un "nivel físico" (tier)?

- a) La capa lógica es una agrupación de responsabilidades en el diseño (presentación, negocio, datos); el nivel físico es la máquina o proceso donde se despliega — no siempre coinciden en número
- b) Son sinónimos exactos y siempre coinciden en número
- c) El nivel físico siempre es menor en número que las capas lógicas

**Respuesta correcta:** a) · **Referencia:** §3.3 [DATO CLAVE]

Una aplicación con 3 capas lógicas puede desplegarse en 5 o más niveles físicos en producción.

### 20. En producción, la Sede Electrónica del Ayuntamiento reparte peticiones entre varias instancias del servidor de aplicaciones mediante un balanceador, y usa una capa de caché para el callejero antes de llegar al clúster de base de datos. ¿Cuántas capas lógicas y niveles físicos hay, respectivamente?

- a) 3 capas lógicas y exactamente 3 niveles físicos
- b) 3 capas lógicas y bastantes más de 3 niveles físicos
- c) 1 capa lógica y 1 nivel físico

**Respuesta correcta:** b) · **Referencia:** §3.3 [EJEMPLO DE APLICACIÓN EN EL AYTO]

Presentación, negocio y datos son las 3 capas lógicas clásicas, desplegadas sobre balanceador, varias instancias de aplicación, caché y clúster de datos.

### 21. Comparando 2-Tier, 3-Tier y n-Tier, ¿qué modelo ofrece mayor escalabilidad y mayor complejidad operativa simultáneamente?

- a) 2-Tier
- b) Ninguno de los tres modelos es más complejo que otro
- c) n-Tier, al permitir escalado horizontal en cada nivel a costa de mayor complejidad de operación

**Respuesta correcta:** c) · **Referencia:** §3.4

2-Tier tiene escalabilidad limitada y baja complejidad; n-Tier invierte ese equilibrio.

### 22. ¿Qué caso de uso típico corresponde mejor a una arquitectura de 2-Tier?

- a) Aplicaciones departamentales pequeñas o herramientas internas con pocos usuarios concurrentes en red local
- b) Sistemas de alta disponibilidad e integración masiva con terceros
- c) APIs públicas consumidas por millones de usuarios simultáneos

**Respuesta correcta:** a) · **Referencia:** §3.4

Es donde su sencillez conceptual y buen rendimiento en LAN compensan sus limitaciones de escalabilidad.

### 23. ¿Cuáles son las dos reglas estructurales de la arquitectura multicapa?

- a) Máxima velocidad de red y mínimo número de servidores
- b) Encapsulación (cada capa oculta su implementación tras una interfaz) y dependencia unidireccional (de arriba hacia abajo)
- c) Uso obligatorio de XML y prohibición de JSON

**Respuesta correcta:** b) · **Referencia:** §4.1 [DATO CLAVE]

Permiten sustituir una capa sin afectar a las demás, siempre que el contrato entre capas se respete.

### 24. ¿Cuál es la responsabilidad exclusiva de la capa de presentación?

- a) Calcular la liquidación de una tasa municipal
- b) Almacenar de forma duradera el estado de la aplicación
- c) La interacción con el usuario: recoger entrada, mostrar resultados y validar el formato superficial de los datos, sin lógica de negocio

**Respuesta correcta:** c) · **Referencia:** §4.2

Su única responsabilidad es traducir entre el modelo interno y lo que percibe el usuario.

### 25. Un ciudadano presenta una solicitud de licencia de obra. ¿Qué capa decide si la documentación aportada cumple los requisitos normativos para admitir a trámite la solicitud?

- a) La capa de lógica de negocio, porque esa decisión depende de la normativa urbanística vigente, no de la tecnología de la interfaz
- b) La capa de presentación, mediante validación de formato de campos
- c) La capa de acceso a datos, al ejecutar la consulta SQL

**Respuesta correcta:** a) · **Referencia:** §4.3 [EJERCICIO RESUELTO]

La capa de presentación solo puede hacer validaciones superficiales (campo obligatorio, tamaño de fichero).

### 26. ¿Qué responsabilidad tiene la capa de acceso a datos frente a la capa de negocio?

- a) Decidir si un usuario tiene permiso para realizar una acción de negocio
- b) Leer/escribir el estado persistente y traducir entre el modelo de la capa de negocio y el modelo de almacenamiento, sin exponer el esquema interno
- c) Renderizar la interfaz gráfica del usuario final

**Respuesta correcta:** b) · **Referencia:** §4.4 [RELACIÓN CON OTROS TEMAS]

El diseño concreto de esta capa es objeto de los Temas 15, 16 y 17.

### 27. En el flujo de procesamiento de una petición en arquitectura multicapa, ¿en qué sentido viaja la petición y en qué sentido la respuesta?

- a) Ambas viajan siempre de abajo hacia arriba
- b) La petición salta directamente de presentación a datos, sin pasar por negocio
- c) La petición viaja de arriba hacia abajo (presentación→negocio→datos); la respuesta, de abajo hacia arriba, por el mismo camino en sentido inverso

**Respuesta correcta:** c) · **Referencia:** §4.5

En ningún punto la capa de datos invoca directamente a la de presentación.

### 28. ¿Cuál de las siguientes situaciones constituye una violación de la regla de dependencia unidireccional en arquitectura multicapa?

- a) La capa de acceso a datos invoca directamente a la capa de presentación para notificar un cambio
- b) La capa de presentación llama a la capa de negocio
- c) La capa de negocio llama a la capa de acceso a datos

**Respuesta correcta:** a) · **Referencia:** §4.1 [DATO CLAVE]

Es el antipatrón más habitual: las dependencias deben fluir siempre en una única dirección.

### 29. ¿Qué beneficio en escalabilidad aporta el desacoplamiento entre capas de una arquitectura multicapa?

- a) Obliga a escalar siempre las tres capas a la vez, en la misma proporción
- b) Se puede escalar de forma independiente la capa que más lo necesite, sin tocar las demás
- c) Elimina por completo la necesidad de un servidor de base de datos

**Respuesta correcta:** b) · **Referencia:** §4.6

Si el cuello de botella está en presentación, se añaden instancias de esa capa sin tocar la de datos, y viceversa.

### 30. ¿Por qué no se debe confiar en la validación del lado cliente como mecanismo de seguridad?

- a) Porque el navegador nunca ejecuta JavaScript
- b) Porque HTTPS lo impide técnicamente
- c) Porque un cliente ligero es manipulable por el propio usuario (herramientas de desarrollador, peticiones directas a la API); la validación autoritativa debe repetirse siempre en el servidor

**Respuesta correcta:** c) · **Referencia:** §4.6 [DATO CLAVE]

Centralizar la seguridad en la capa de negocio evita que dependa de un cliente que el usuario controla.

### 31. ¿Qué es un "servicio", en sentido arquitectónico?

- a) Una unidad de funcionalidad autocontenida, con interfaz explícita y débilmente acoplada, que puede ser descubierta e invocada por distintos consumidores
- b) Un sinónimo exacto de "clase Java"
- c) Un fichero de configuración XML sin comportamiento

**Respuesta correcta:** a) · **Referencia:** §5.1 [ERL-SOA]

La motivación de fondo es la reutilización funcional: exponer la lógica una vez, en lugar de duplicarla en cada aplicación.

### 32. ¿Qué es SOA (Service-Oriented Architecture)?

- a) Un protocolo de red concreto equivalente a HTTP
- b) Un estilo arquitectónico que estructura un sistema como un conjunto de servicios débilmente acoplados que se comunican mediante contratos explícitos
- c) Una marca comercial de un fabricante de software

**Respuesta correcta:** b) · **Referencia:** §5.2 [DATO CLAVE]

No es una tecnología concreta; los servicios web son su implementación más habitual, pero no la única.

### 33. ¿Cuál de los siguientes NO es uno de los principios de diseño de SOA?

- a) Bajo acoplamiento
- b) Contrato explícito
- c) Dependencia obligatoria de un único lenguaje de programación para todos los servicios

**Respuesta correcta:** c) · **Referencia:** §5.2 [ERL-SOA]

SOA persigue justamente lo contrario: interoperabilidad entre servicios implementados en tecnologías distintas, gracias a la abstracción del contrato.

### 34. ¿Qué diferencia principal se señala entre SOA "clásico" y los microservicios (§7.1)?

- a) SOA tiende a compartir infraestructura común (bus de servicios empresarial, ESB); los microservicios enfatizan la autonomía total, incluida a menudo la de los datos
- b) Los microservicios no usan nunca HTTP
- c) SOA es posterior cronológicamente a los microservicios

**Respuesta correcta:** a) · **Referencia:** §5.2 [RELACIÓN CON OTROS TEMAS]

Los microservicios se presentan como una evolución o reinterpretación radical de los principios SOA.

### 35. ¿Qué garantiza a un servicio web su "interoperabilidad" entre sistemas de tecnologías distintas?

- a) Que todos los sistemas involucrados usen la misma base de datos física
- b) El uso de protocolos y formatos estándar y abiertos (HTTP, XML/JSON), independientes de un lenguaje o fabricante concreto
- c) Que el servicio se ejecute exclusivamente en la nube

**Respuesta correcta:** b) · **Referencia:** §5.3 [W3C-SOAP]

Un cliente Java puede así invocar un servicio implementado en Python sin conflicto.

### 36. ¿Cuál de las siguientes NO es una característica definitoria de un servicio web?

- a) Interoperabilidad
- b) Uso de protocolos y formatos estándar
- c) Acoplamiento fuerte obligatorio entre consumidor e implementación interna del proveedor

**Respuesta correcta:** c) · **Referencia:** §5.3

Es justo lo contrario: un servicio web se caracteriza por el débil acoplamiento — el consumidor solo conoce el contrato público, no la implementación.

### 37. ¿Qué estructura formal define la especificación de un mensaje SOAP?

- a) Un "sobre" (envelope) en XML, con cabecera (metadatos) y cuerpo (datos de la operación)
- b) Un objeto JSON con una única clave "data"
- c) Un fichero binario propietario sin especificación pública

**Respuesta correcta:** a) · **Referencia:** §5.4.1 [W3C-SOAP]

La cabecera puede transportar extensiones WS-* (seguridad, transacciones); el cuerpo, la operación invocada.

### 38. ¿Cómo describe REST los recursos que expone un servicio, frente al modelo de "operaciones nombradas" de SOAP?

- a) Mediante procedimientos remotos con nombres arbitrarios sin relación con HTTP
- b) Mediante URIs que identifican recursos, manipulados con los verbos estándar de HTTP
- c) Mediante ficheros WSDL obligatorios

**Respuesta correcta:** b) · **Referencia:** §5.4.2 [FIELDING]

REST no es un protocolo de mensajería como SOAP, sino un estilo arquitectónico que aprovecha las capacidades ya existentes de HTTP.

### 39. En el caso de referencia, el sistema de Tributos, heredado, expone su lógica de liquidación mediante SOAP con WSDL formal, mientras que la nueva capa de negocio de la Sede expone hacia el navegador una API REST en JSON. ¿Qué principio arquitectónico ilustra esta convivencia?

- a) Que REST siempre sustituye a SOAP en cualquier escenario
- b) Que SOAP y REST son técnicamente idénticos y solo cambia el nombre
- c) Que ambos estilos conviven en la misma arquitectura, cada uno donde mejor encaja: SOAP en integración estable y crítica, REST en clientes web/móviles modernos

**Respuesta correcta:** c) · **Referencia:** §5.4.2 [EJEMPLO DE APLICACIÓN EN EL AYTO]

SOAP no está "muerto"; sigue siendo el estándar de facto en integraciones que requieren garantías formales fuertes.

### 40. ¿Qué elementos componen una petición/respuesta HTTP?

- a) Método (verbo), cabeceras, cuerpo y, en la respuesta, un código de estado de tres dígitos
- b) Únicamente una URL, sin ningún otro dato
- c) Un certificado X.509 obligatorio en toda petición, incluso sin HTTPS

**Respuesta correcta:** a) · **Referencia:** §6.1 [RFC9110]

HTTP es el protocolo de aplicación que sirve de transporte a la inmensa mayoría de los servicios web.

### 41. ¿Qué diferencia hay entre los códigos de estado HTTP 401 y 403?

- a) 401 significa "recurso no encontrado" y 403 significa "error del servidor"
- b) 401 (Unauthorized) indica que el cliente no está autenticado o su autenticación no es válida; 403 (Forbidden) indica que está autenticado pero no tiene permiso para esa acción
- c) Ambos códigos son sinónimos exactos y pueden usarse indistintamente

**Respuesta correcta:** b) · **Referencia:** §6.1 [DATO CLAVE]

Es una de las confusiones más explotadas en preguntas tipo test de este bloque.

### 42. ¿Qué garantías aporta TLS a una conexión HTTPS?

- a) Ninguna: HTTPS es idéntico a HTTP salvo por el puerto usado
- b) Solo velocidad de transferencia, sin relación con la seguridad
- c) Confidencialidad (cifrado del contenido), integridad (detección de alteraciones) y autenticación del servidor mediante certificado X.509

**Respuesta correcta:** c) · **Referencia:** §6.1 [RFC9846]

HTTPS no es un protocolo distinto de HTTP, sino HTTP transportado sobre una conexión cifrada con TLS.

### 43. ¿Qué mejora introduce fundamentalmente HTTP/2 respecto a HTTP/1.1?

- a) La multiplexación: varias peticiones y respuestas viajan intercaladas sobre una única conexión TCP, eliminando el bloqueo de cabecera de línea a nivel de aplicación
- b) Cambia por completo la semántica de los verbos HTTP (GET, POST dejan de existir)
- c) Elimina la necesidad de usar códigos de estado

**Respuesta correcta:** a) · **Referencia:** §6.1 [RFC9113]

Los verbos, cabeceras y códigos de estado son los mismos en HTTP/1.1, /2 y /3.

### 44. ¿Qué es OAuth 2.0?

- a) Un formato de token JSON firmado
- b) Un framework de autorización delegada que permite a una aplicación acceder a un recurso en nombre del usuario sin conocer sus credenciales
- c) Un algoritmo de cifrado simétrico

**Respuesta correcta:** b) · **Referencia:** §6.2 [RFC6749]

Distingue los roles resource owner, client, authorization server y resource server.

### 45. En el flujo de OAuth 2.0, ¿qué rol emite el token de acceso al cliente?

- a) El propio resource owner (usuario)
- b) El resource server directamente, sin intermediarios
- c) El authorization server, tras verificar la autorización concedida por el resource owner

**Respuesta correcta:** c) · **Referencia:** §6.2 [RFC6749]

El cliente presenta después ese token al resource server para acceder al recurso protegido.

### 46. ¿Qué es un JWT (JSON Web Token)?

- a) Un formato de token autocontenido, compuesto por header.payload.signature en Base64URL, cuyas reclamaciones (claims) van firmadas
- b) Un protocolo de autorización alternativo a OAuth 2.0
- c) Un tipo de certificado digital X.509

**Respuesta correcta:** a) · **Referencia:** §6.2 [RFC7519]

Es autocontenido: permite verificar su validez sin consultar una base de datos central en cada petición.

### 47. ¿Cuál es la relación correcta entre OAuth 2.0 y JWT?

- a) Son sinónimos: implementar JWT equivale a implementar OAuth 2.0
- b) OAuth 2.0 es un framework de autorización (cómo se obtiene un token de forma segura); JWT es, con frecuencia, el formato concreto que adopta ese token
- c) JWT sustituyó por completo a OAuth 2.0 desde 2020

**Respuesta correcta:** b) · **Referencia:** §6.2 [DATO CLAVE]

Confundir "usar JWT" con "implementar OAuth 2.0" es un error frecuente.

### 48. ¿Qué diferencia principal existe entre XML y JSON como formatos de intercambio de datos?

- a) JSON solo puede transportar números, nunca texto
- b) XML no permite anidar estructuras, JSON sí
- c) XML es más verboso pero soporta espacios de nombres y validación robusta (XSD); JSON es más ligero y de mapeo más natural a estructuras de programación

**Respuesta correcta:** c) · **Referencia:** §6.3 [W3C-XML; RFC8259]

XML domina en SOAP y estándares de Administración; JSON domina en APIs REST modernas.

### 49. ¿Qué es el Esquema Nacional de Interoperabilidad (ENI) en relación con XML y JSON?

- a) Un catálogo de estándares abiertos —entre ellos XML y JSON— de uso obligatorio en los sistemas de información de las Administraciones Públicas españolas
- b) Un protocolo de cifrado exclusivo del Ayuntamiento de Madrid
- c) Una versión obsoleta de XML sin uso actual

**Respuesta correcta:** a) · **Referencia:** §6.3 [ENI]

Garantiza el intercambio de información entre organismos.

### 50. ¿Qué describe formalmente el documento WSDL de un servicio SOAP?

- a) La contraseña de acceso al servidor
- b) Las operaciones que ofrece el servicio, los mensajes que espera y devuelve cada una, los tipos de datos y el endpoint de red
- c) El diseño gráfico de la interfaz de usuario

**Respuesta correcta:** b) · **Referencia:** §6.4 [W3C-WSDL]

Es el contrato formal que hace posible que un consumidor genere automáticamente el código cliente.

### 51. ¿Cuál es la situación actual de UDDI como registro de descubrimiento de servicios?

- a) Es el estándar dominante en todas las nuevas APIs REST
- b) Sustituyó completamente a WSDL desde 2015
- c) Está en desuso en la práctica: su función de catálogo descubrible ha sido sustituida por catálogos de API modernos (OpenAPI/Swagger)

**Respuesta correcta:** c) · **Referencia:** §6.4 [DATO CLAVE]

La promesa de un registro público universal de servicios nunca llegó a adoptarse a gran escala.

### 52. ¿Qué es RPC (Remote Procedure Call)?

- a) Un paradigma de comunicación en el que se invoca un procedimiento en otro espacio de direcciones como si fuera una llamada local, ocultando serialización y transporte
- b) La implementación específica de Java para invocar objetos remotos
- c) Un formato de fichero de configuración

**Respuesta correcta:** a) · **Referencia:** §6.5 [RFC5531]

Es el paradigma conceptual subyacente al modelo de "operaciones" de SOAP.

### 53. ¿Qué relación existe entre RPC y RMI?

- a) RMI es el paradigma general; RPC es su implementación específica en Java
- b) RPC es el paradigma general de invocación remota; RMI es su implementación nativa en la plataforma Java, con stubs y skeletons
- c) No tienen ninguna relación conceptual entre sí

**Respuesta correcta:** b) · **Referencia:** §6.5 [DATO CLAVE]

RMI está limitado a comunicación entre extremos Java, a diferencia de SOAP, neutral respecto al lenguaje.

### 54. ¿Qué son los microservicios?

- a) Un sinónimo exacto e intercambiable de "servicio web SOAP"
- b) Un componente único y monolítico que concentra toda la lógica de una aplicación
- c) Un estilo arquitectónico que estructura una aplicación como servicios pequeños, autónomos y desplegables de forma independiente, organizados en torno a una capacidad de negocio

**Respuesta correcta:** c) · **Referencia:** §7.1 [NEWMAN]

Se comunican mediante mecanismos ligeros, típicamente APIs REST o mensajería asíncrona.

### 55. ¿Qué "coste" arquitectónico se asume habitualmente al adoptar microservicios frente a un monolito?

- a) Mayor complejidad operacional (observabilidad, despliegue, red entre servicios) y, con frecuencia, renuncia a la consistencia transaccional fuerte en favor de la consistencia eventual
- b) Ninguno: los microservicios son estrictamente superiores en todos los aspectos
- c) La imposibilidad técnica de escalar de forma independiente cada servicio

**Respuesta correcta:** a) · **Referencia:** §7.1 [DATO CLAVE]

No son "gratis": a cambio de flexibilidad, hay que monitorizar y versionar muchos más componentes.

### 56. ¿En qué consiste el desacoplamiento que aporta la arquitectura orientada a eventos (EDA)?

- a) Obliga a que emisor y receptor se ejecuten siempre en el mismo proceso
- b) Desacopla emisor y receptor en el espacio (no conocen su dirección de red mutua) y en el tiempo (el consumidor no necesita estar disponible en el instante exacto de la publicación)
- c) Elimina por completo la necesidad de cualquier tipo de middleware

**Respuesta correcta:** b) · **Referencia:** §7.2 [EDA-FOWLER]

El productor publica un evento en un canal sin conocer quién, si alguien, lo va a consumir.

### 57. En el caso de referencia, cuando un expediente cambia a estado "resuelto", ¿qué ventaja aporta que notificaciones y estadísticas se suscriban al evento correspondiente en lugar de que la capa de negocio los invoque directamente?

- a) Ninguna: es equivalente a invocarlos directamente
- b) Que el evento solo pueda ser consumido por un único sistema como máximo
- c) Que un tercer sistema interesado pueda darse de alta como nuevo suscriptor sin modificar en absoluto la capa de negocio que publica el evento

**Respuesta correcta:** c) · **Referencia:** §7.2 [EJEMPLO DE APLICACIÓN EN EL AYTO]

Es la ventaja central del desacoplamiento productor-consumidor propio de EDA.

### 58. ¿Qué distingue a un contenedor de una máquina virtual tradicional?

- a) El contenedor virtualiza a nivel de sistema operativo (namespaces/cgroups), compartiendo el núcleo con el host; la máquina virtual virtualiza el hardware completo mediante un hipervisor
- b) Son términos sinónimos y completamente intercambiables
- c) El contenedor requiere siempre más tiempo de arranque que una máquina virtual

**Respuesta correcta:** a) · **Referencia:** §7.3 [K8S-DOCS]

Por eso un contenedor arranca en segundos, frente a los minutos de una máquina virtual.

### 59. ¿Qué automatiza la orquestación de contenedores (p. ej. Kubernetes)?

- a) La escritura del código fuente de la aplicación
- b) El arranque, reinicio ante fallo, balanceo de carga y escalado horizontal de un gran número de contenedores desplegados
- c) El diseño del modelo entidad-relación de la base de datos

**Respuesta correcta:** b) · **Referencia:** §7.3 [K8S-DOCS]

Gestionar manualmente decenas o cientos de contenedores deja de ser viable sin esta automatización.

### 60. Según la definición de referencia del NIST, ¿qué caracteriza a la computación en la nube?

- a) La obligación de comprar hardware físico dedicado para cada aplicación
- b) Un modelo exclusivo para aplicaciones sin ningún requisito de disponibilidad
- c) El acceso bajo demanda, a través de la red, a un conjunto compartido de recursos de cómputo configurables, que pueden aprovisionarse y liberarse rápidamente con un esfuerzo mínimo de gestión

**Respuesta correcta:** c) · **Referencia:** §7.4 [NIST800145]

Sus modelos de servicio (IaaS/PaaS/SaaS) y de despliegue se desarrollan en profundidad en el Tema 31.

## Preguntas sobre los casos prácticos

### Caso 1. Diseño n-capas y API REST de la Sede Electrónica

#### 1. En el supuesto planteado, la aplicación de escritorio actual se conecta directamente a la base de datos de expedientes. ¿Cuál es el principal problema de ese modelo de 2 capas?

- a) Que el cliente es un navegador sin lógica propia, incapaz de mostrar los expedientes.
- b) Que el cliente queda acoplado al esquema de datos y cada uno mantiene su propia conexión al SGBD.
- c) Que la base de datos no puede albergar procedimientos almacenados ni disparadores.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §3.1

En 2 capas cualquier cambio en el modelo de datos obliga a tocar el cliente, y la escalabilidad es limitada porque cada cliente mantiene una conexión directa al SGBD, un recurso finito.

#### 2. ¿Cuál es la ventaja arquitectónica central de pasar a un modelo de 3 capas en la nueva Sede Electrónica?

- a) Que se suprime la base de datos y los expedientes pasan a guardarse en el servidor web.
- b) Que la lógica de negocio se traslada al navegador del ciudadano, que la ejecuta localmente.
- c) El desacoplamiento: el cliente ya no conoce el esquema de datos, solo el contrato de la capa de negocio.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §3.2

Con 3 capas, cambiar el modelo de datos o incluso el motor de base de datos no debería requerir tocar el cliente, que solo conoce la interfaz del servidor de aplicaciones.

#### 3. Además del desacoplamiento, ¿qué mejora de escalabilidad aporta el servidor de aplicaciones frente a la conexión directa de cada cliente al SGBD?

- a) Agrupa y reutiliza las conexiones a la base de datos mediante un pool de conexiones.
- b) Guarda en cada puesto una copia local de los datos para trabajar sin conexión.
- c) Elimina el uso de la red, porque cliente y base de datos pasan a la misma máquina.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §3.2

El servidor de aplicaciones puede agrupar y reutilizar conexiones al SGBD mediante un pool, en lugar de que cada cliente mantenga la suya propia.

#### 4. Ante los picos de tráfico de las campañas de plazos fiscales, ¿qué estrategia de escalado conviene para el nuevo servidor de aplicaciones?

- a) Escalado vertical: dotar al servidor, de forma permanente, de más CPU y más memoria.
- b) Sustituir el servidor de base de datos por otro de mayor capacidad antes de cada campaña.
- c) Escalado horizontal: añadir instancias temporales tras un balanceador y retirarlas después.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.2.2

El escalado horizontal añade instancias en paralelo coordinadas por un balanceador; permite crecer solo durante el pico y retirar la capacidad cuando ya no hace falta.

#### 5. ¿Por qué no basta con la estrategia que permitía el modelo antiguo, el escalado vertical?

- a) Porque el escalado vertical exige instalar un balanceador de carga delante del servidor.
- b) Porque tiene un límite físico y obliga a sobredimensionar el hardware con coste ocioso el resto del año.
- c) Porque el escalado vertical solo se aplica a los puestos cliente, no a los servidores.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.2.2

Añadir CPU y memoria a una misma máquina tiene un techo físico y de coste; para cubrir los picos habría que mantener el hardware sobredimensionado todo el año.

#### 6. ¿Cómo se diseña, en una API REST, la consulta del expediente EXP-2026-004821?

- a) GET /api/expedientes/EXP-2026-004821
- b) POST /api/consultarExpediente, con el número en el cuerpo
- c) PUT /api/expedientes/EXP-2026-004821

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §6.6

En REST el expediente es un recurso identificado por su URI y se lee con GET; un único endpoint con POST para todo es el estilo RPC del nivel 0.

#### 7. Desde el panel del gestor hay que marcar ese expediente como «revisado», cambiando solo su estado. ¿Qué petición corresponde?

- a) PUT /api/expedientes/EXP-2026-004821, enviando solo el campo estado.
- b) PATCH /api/expedientes/EXP-2026-004821 con el cuerpo {"estado": "revisado"}.
- c) POST /api/expedientes con el cuerpo {"estado": "revisado"}.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §6.6

PATCH es la actualización parcial de un recurso; PUT es un reemplazo completo y POST crea un recurso nuevo.

#### 8. Este diseño usa recursos identificados por URI, verbos HTTP y códigos de estado, pero sin hipermedia. ¿Qué nivel del modelo de madurez de Richardson alcanza?

- a) El nivel 2.
- b) El nivel 3.
- c) El nivel 0.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §6.6

El nivel 2 usa correctamente los verbos HTTP y los códigos de estado; es el nivel de la inmensa mayoría de las APIs REST reales.

#### 9. ¿Qué le falta a ese diseño para alcanzar el nivel 3 del modelo de Richardson?

- a) Devolver los datos en XML en lugar de JSON, con un esquema formal.
- b) Usar un único verbo HTTP para todas las operaciones sobre el recurso.
- c) Incluir en las respuestas enlaces a las acciones disponibles (HATEOAS).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §6.6

El nivel 3 añade HATEOAS: las respuestas incluyen enlaces a las acciones y recursos relacionados, para que el cliente navegue la API dinámicamente.

#### 10. ¿Dónde debe comprobarse que el ciudadano autenticado es el titular del expediente que consulta?

- a) En el cliente web, con JavaScript, antes de enviar la petición a la API.
- b) En la capa de lógica de negocio del servidor, porque el cliente es manipulable.
- c) En la capa de presentación, validando el formato del número de expediente.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §4.3 y §4.6

Es una regla de negocio y de seguridad, no de formato; el navegador es manipulable por el usuario, así que la comprobación autoritativa debe hacerse siempre en el servidor.

### Caso 2. Integración de un servicio SOAP heredado en la nueva arquitectura orientada a servicios

#### 1. En el supuesto planteado, ¿conviene sustituir el servicio SOAP de Tributos por uno REST antes de integrarlo?

- a) No: SOAP sigue vigente en integraciones con garantías formales; se envuelve, no se sustituye.
- b) Sí: SOAP es un protocolo obsoleto que ya no se usa en integraciones de la Administración.
- c) Sí: SOAP y REST no pueden convivir dentro de una misma arquitectura de sistemas.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §5.4.1

SOAP no está «muerto»: es habitual en sistemas heredados de la Administración que exigen garantías formales. Reescribirlo añadiría riesgo y coste sin beneficio funcional.

#### 2. ¿Qué ecosistema de extensiones da a SOAP garantías como la seguridad a nivel de mensaje o las transacciones distribuidas?

- a) OpenAPI (Swagger), que describe el contrato del servicio en JSON o YAML.
- b) WS-*: WS-Security, WS-ReliableMessaging o WS-AtomicTransaction.
- c) HATEOAS, que añade enlaces a las acciones disponibles en cada respuesta.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §5.4.1

Las extensiones WS-* (seguridad, entrega garantizada, transacciones distribuidas) hacen a SOAP especialmente robusto en escenarios empresariales exigentes.

#### 3. ¿Qué documento describe formalmente las operaciones, los mensajes, los tipos y el endpoint del servicio SOAP de Tributos?

- a) El registro UDDI de servicios.
- b) La especificación OpenAPI.
- c) El documento WSDL del servicio.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §6.4

El WSDL es el documento XML que describe el contrato de un servicio SOAP: operaciones, mensajes de entrada y salida, tipos de datos y dirección de red.

#### 4. ¿Qué papel tendría un registro UDDI en esta integración?

- a) Es imprescindible: ningún servicio SOAP puede invocarse sin consultar antes un registro UDDI.
- b) Serviría para publicar y descubrir el WSDL, pero está en desuso y aquí el WSDL ya se conoce.
- c) Traduciría automáticamente los mensajes SOAP del sistema de Tributos a JSON para la API.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §6.4

UDDI es un registro para publicar y descubrir servicios («páginas amarillas»), hoy en desuso; el equipo conoce directamente el WSDL del sistema de Tributos.

#### 5. En el WSDL de Tributos aparece ConsultarImportePendiente dentro de wsdl:portType, con wsdl:input y wsdl:output. ¿Qué representa?

- a) Una operación del servicio, con su mensaje de entrada y su mensaje de salida.
- b) Un recurso REST identificado por URI que se consulta con el verbo GET.
- c) Una reclamación (claim) firmada dentro del token del ciudadano.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §6.4

SOAP sigue un modelo de operaciones nombradas; el WSDL declara cada operación con los mensajes que espera y devuelve.

#### 6. ¿Cómo actúa la capa de negocio de la Sede como intermediaria entre el ciudadano y el servicio SOAP de Tributos?

- a) Redirige el navegador del ciudadano al endpoint SOAP para que lo invoque directamente.
- b) Invoca el servicio SOAP y devuelve al ciudadano el mensaje XML tal como lo recibe.
- c) Recibe la petición REST, construye el mensaje SOAP, invoca el servicio y traduce el XML a JSON.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §5.4.2

La capa de negocio traduce entre estilos: el ciudadano solo ve JSON sobre REST y nunca XML ni SOAP, lo que permite que ambos estilos convivan.

#### 7. ¿Qué estructura debe tener el mensaje que la capa de negocio construye para invocar el servicio de Tributos?

- a) Un sobre (Envelope) XML con una cabecera (Header) y un cuerpo (Body).
- b) Un token de tres partes separadas por puntos: header.payload.signature.
- c) Un objeto JSON de pares clave-valor enviado con el verbo PATCH.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §5.4.1

Un mensaje SOAP tiene la estructura formal de un sobre XML: cabecera con metadatos (seguridad, transacción) y cuerpo con los datos de la operación.

#### 8. El nuevo endpoint REST de consulta de tributos debe exigir que el ciudadano esté autenticado. ¿Qué estándar y qué formato de token se usan?

- a) WS-Security, con el token incluido en la cabecera del sobre SOAP.
- b) UDDI, con un token publicado en el registro de servicios.
- c) OAuth 2.0, con un token de acceso en formato JWT.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §6.2

Para APIs REST, la seguridad se resuelve con OAuth 2.0 y JWT; WS-Security es la seguridad a nivel de mensaje propia de SOAP.

#### 9. ¿Qué relación hay entre OAuth 2.0 y JWT en esa solución?

- a) Son sinónimos: dos nombres del mismo protocolo de autenticación.
- b) OAuth 2.0 define cómo obtener el token; JWT es el formato del token.
- c) JWT es el protocolo de autorización y OAuth 2.0, el formato del token.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §6.2

OAuth 2.0 es un framework de autorización delegada; JWT es un formato de token. No son alternativas ni sinónimos.

#### 10. ¿Qué permite a la API de tributos comprobar que el JWT es válido sin consultar al emisor en cada petición?

- a) La firma (signature), que permite verificar que el token no se ha alterado.
- b) La contraseña del ciudadano, que viaja cifrada dentro del payload del token.
- c) La publicación del token en un registro UDDI consultable por todos los servicios.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §6.2

El JWT es autocontenido: su firma permite verificar que no ha sido alterado sin consultar una base de datos central. OAuth 2.0 evita, además, que la aplicación conozca la contraseña.

### Caso 3. Evolución del módulo de notificaciones hacia microservicios, eventos y contenedores

#### 1. En el supuesto planteado, ¿qué estilo arquitectónico permite que cualquier número de sistemas reaccione al cambio de estado sin modificar la capa de negocio?

- a) Una arquitectura de 2 capas, con la lógica en procedimientos almacenados.
- b) Llamadas RPC síncronas desde la capa de negocio a cada sistema interesado.
- c) Una arquitectura orientada a eventos (EDA), con publicación y suscripción.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §7.2

En EDA el productor publica el evento en un canal sin saber quién lo consumirá, y los sistemas interesados se suscriben a ese canal.

#### 2. ¿Qué papel juega el middleware en esa solución?

- a) El middleware orientado a mensajes entrega el evento a los suscriptores, desacoplándolos en espacio y tiempo.
- b) Un middleware orientado a objetos (ORB) invoca de forma síncrona los métodos de cada sistema.
- c) Un middleware de acceso a datos traduce el evento al dialecto SQL de cada base de datos.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §2.2.3 y §7.2

El middleware orientado a mensajes (MOM) es la base técnica de EDA: gestiona la entrega del evento a todos los suscriptores.

#### 3. Si en el futuro se añade un sistema de auditoría interesado en el cambio de estado, ¿qué hay que hacer?

- a) Modificar la capa de negocio para que también llame al sistema de auditoría.
- b) Solo dar de alta una nueva suscripción al evento; la capa de negocio no cambia.
- c) Reconfigurar el productor del evento con la dirección de red del nuevo sistema.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §7.2

Como el productor no conoce a los consumidores, un tercer sistema interesado se incorpora como nuevo suscriptor sin tocar la capa de negocio.

#### 4. Se dice que la comunicación por eventos desacopla emisor y receptor «en el tiempo». ¿Qué significa?

- a) Que el consumidor no tiene que estar disponible al publicarse el evento: el broker lo retiene.
- b) Que el productor conoce de antemano la dirección de red de cada uno de los consumidores.
- c) Que los eventos se procesan de forma síncrona, en el mismo instante en que se publican.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §7.2

El desacoplamiento en el tiempo implica que el broker puede retener el mensaje hasta que el consumidor esté listo; en el espacio, que el productor solo conoce el canal.

#### 5. ¿Qué ventaja aporta extraer el módulo de notificaciones como microservicio con su propia base de datos?

- a) Que desaparece la complejidad operativa de desplegar y monitorizar la aplicación.
- b) Que se garantiza la consistencia ACID entre expedientes y notificaciones.
- c) Que puede desplegarse y escalarse de forma independiente del resto de la aplicación.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §7.1

Los microservicios son desplegables de forma independiente y permiten escalar selectivamente, servicio a servicio, según su propio patrón de carga.

#### 6. ¿Qué inconveniente tiene esa extracción frente a mantener el módulo dentro del monolito?

- a) Que el microservicio ya no podrá comunicarse mediante APIs REST con el resto.
- b) Más complejidad operativa y la renuncia a la consistencia transaccional fuerte.
- c) Que el microservicio deberá compartir obligatoriamente la base de datos del monolito.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §7.1

Los microservicios no son gratis: hay que monitorizar, desplegar y versionar más componentes, y se pasa a menudo de consistencia fuerte a consistencia eventual.

#### 7. ¿Qué tecnología de empaquetado se recomienda para desplegar el microservicio de notificaciones de forma ligera y reproducible?

- a) Una máquina virtual completa por servicio, que virtualiza el hardware mediante un hipervisor.
- b) Una aplicación de escritorio instalada en cada puesto que vaya a enviar notificaciones.
- c) Contenedores (por ejemplo, Docker), que virtualizan a nivel del sistema operativo.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §7.3

El contenedor comparte el núcleo del sistema operativo, arranca en segundos y es mucho más ligero que una máquina virtual, que virtualiza el hardware completo.

#### 8. ¿Qué mecanismo automatiza el arranque, el reinicio ante fallo y el escalado de ese microservicio sin intervención manual?

- a) Scripts que el técnico de sistemas ejecuta a mano cuando detecta un pico de carga.
- b) Un orquestador como Kubernetes, que mantiene las réplicas y escala horizontalmente.
- c) Un registro UDDI que publica y descubre las instancias disponibles del servicio.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §7.3

La orquestación de contenedores define de forma declarativa cuántas réplicas deben ejecutarse, reinicia las que fallan, balancea la carga y escala añadiendo o quitando réplicas.

#### 9. Con dos servicios y dos bases de datos comunicados por eventos asíncronos, ¿qué tipo de consistencia debe asumir el equipo?

- a) Consistencia eventual: los datos pueden estar desincronizados un tiempo y acaban convergiendo.
- b) Consistencia fuerte (ACID), garantizada por el broker de mensajería en cada entrega.
- c) Consistencia inmediata, porque el evento se publica dentro de la misma transacción.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §7.1

El expediente puede haber cambiado ya de estado sin que la notificación se haya enviado todavía; se asume que ambos estados acabarán convergiendo.

#### 10. ¿Por qué ya no es realista exigir consistencia transaccional fuerte entre expedientes y notificaciones?

- a) Porque la arquitectura orientada a eventos prohíbe que los servicios usen bases de datos.
- b) Porque el formato JSON de los eventos no admite operaciones transaccionales.
- c) Porque son dos bases de datos en servicios distintos, sin una transacción única que las abarque.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §7.1

Abarcar ambas bases de datos exigiría un coordinador de transacciones distribuidas, precisamente lo que el diseño de microservicios busca evitar.
