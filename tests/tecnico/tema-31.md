# Test del tema 31. Paradigmas de computación distribuida y Servicios en Cloud

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-31.html>

## Batería de preguntas

### 1. ¿Cuáles son las dos ausencias que definen técnicamente a un sistema distribuido?

- a) La ausencia de red de comunicaciones y la ausencia de sistema operativo común
- b) La ausencia de memoria compartida y la ausencia de un reloj global
- c) La ausencia de virtualización y la ausencia de un servidor central

**Respuesta correcta:** b) · **Referencia:** §1.1.1 [TANENBAUM]

De ambas se deriva que el único mecanismo de coordinación posible sea el paso de mensajes, y con él la imposibilidad de distinguir con certeza un nodo caído de un nodo lento.

### 2. ¿Cuántas transparencias de distribución define el modelo de referencia RM-ODP?

- a) Ocho: acceso, ubicación, migración, reubicación, replicación, concurrencia, fallo y persistencia
- b) Cinco: acceso, ubicación, replicación, fallo y persistencia
- c) Doce, agrupadas en cuatro bloques de tres

**Respuesta correcta:** a) · **Referencia:** §1.1.1 [RMODP]

El objetivo de todas ellas es ocultar al usuario que el sistema está repartido, aunque la transparencia total no es un objetivo deseable en sí mismo.

### 3. La transparencia que oculta que un recurso se está moviendo de ubicación mientras se está utilizando se denomina:

- a) De migración
- b) De replicación
- c) De reubicación

**Respuesta correcta:** c) · **Referencia:** §1.1.1 [RMODP]

La transparencia de migración oculta que el recurso se ha movido; la de reubicación, que se mueve durante el uso sin interrumpirlo. Es la distinción que más se falla de las ocho.

### 4. ¿Cuál de las siguientes NO es una de las ocho falacias de la computación distribuida?

- a) El almacenamiento es infinito
- b) El coste de transporte es cero
- c) La red es homogénea

**Respuesta correcta:** a) · **Referencia:** §1.1.2 [DEUTSCH]

Las ocho falacias son: la red es fiable, la latencia es cero, el ancho de banda es infinito, la red es segura, la topología no cambia, hay un único administrador, el coste de transporte es cero y la red es homogénea.

### 5. Las tarifas de salida de datos que cobran los proveedores de nube pública son la materialización económica de una de las falacias. ¿De cuál?

- a) La red es fiable
- b) El ancho de banda es infinito
- c) El coste de transporte es cero

**Respuesta correcta:** c) · **Referencia:** §1.1.2 [DEUTSCH] [DATAACT]

Es la séptima falacia. Serializar y mover datos consume procesador y, en la nube pública, se factura por gigabyte, lo que penaliza precisamente la extracción masiva de información.

### 6. En una arquitectura multicapa estricta, ¿cuál es la regla que la define?

- a) Que exista siempre un servidor de aplicaciones intermedio
- b) Que cada capa solo se comunique con la capa contigua
- c) Que la lógica de negocio resida en el cliente

**Respuesta correcta:** b) · **Referencia:** §1.2.1 [TANENBAUM]

Si la capa de presentación ataca directamente a la base de datos, hay tres capas dibujadas pero dos de verdad, y se pierden las ventajas de seguridad y de mantenimiento del modelo.

### 7. ¿Cuál es la diferencia esencial entre una arquitectura SOA clásica y una arquitectura de microservicios?

- a) En SOA la lógica de integración vive en el bus y los datos suelen compartirse; en microservicios el canal es ligero y cada servicio posee su propia base de datos
- b) En SOA los servicios son pequeños y en microservicios son grandes
- c) SOA usa exclusivamente REST y los microservicios exclusivamente SOAP

**Respuesta correcta:** a) · **Referencia:** §1.2.2 [FOWLER]

El corte no está en el tamaño, sino en dónde vive la lógica de integración y quién es dueño de los datos.

### 8. El principio de los microservicios que se enuncia como «tuberías tontas y extremos listos» significa que:

- a) Los mensajes deben ir siempre sin cifrar para reducir la latencia
- b) Cada servicio debe delegar su lógica en el orquestador central
- c) La lógica reside en los servicios y el canal de comunicación no la contiene

**Respuesta correcta:** c) · **Referencia:** §1.2.2 [FOWLER]

Es la reacción directa al bus de servicios empresarial de la SOA clásica, que acumulaba lógica de negocio y se convertía en punto único de fallo y cuello de botella organizativo.

### 9. En una red entre pares (P2P), ¿qué mecanismo permite localizar un recurso sin índice central y sin inundar la red de consultas?

- a) El bus de servicios empresarial
- b) La tabla hash distribuida (DHT)
- c) El registro UDDI

**Respuesta correcta:** b) · **Referencia:** §1.2.3 [DHT]

La clave del recurso determina matemáticamente qué nodo es responsable de él, de modo que la búsqueda converge en un número de saltos del orden del logaritmo del número de nodos.

### 10. En una arquitectura dirigida por eventos, ¿cuál es la diferencia entre un comando y un evento?

- a) El comando se dirige a un destinatario concreto y espera que se ejecute; el evento es un hecho ya ocurrido, no va dirigido a nadie en particular y no espera nada
- b) El comando es asíncrono y el evento es siempre síncrono
- c) El comando lo emite el intermediario y el evento lo emite el consumidor

**Respuesta correcta:** a) · **Referencia:** §1.2.3 [TANENBAUM]

Confundirlos es el error de diseño más frecuente en arquitecturas dirigidas por eventos.

### 11. ¿Cuál de los siguientes métodos HTTP NO es idempotente?

- a) PUT
- b) DELETE
- c) POST

**Respuesta correcta:** c) · **Referencia:** §1.3.1 [RFC7231]

Dos peticiones POST idénticas crean dos recursos. Por eso, cuando una creación puede reintentarse tras un tiempo de espera, se envía una clave de idempotencia que permite al servidor detectar el reintento.

### 12. La garantía de entrega de mensajes más habitual en sistemas asíncronos es «al menos una vez». ¿Qué obligación impone al consumidor?

- a) Confirmar la recepción antes de procesar el mensaje
- b) Ser idempotente, de modo que procesar dos veces el mismo mensaje no produzca dos altas
- c) Ordenar los mensajes por marca de tiempo antes de procesarlos

**Respuesta correcta:** b) · **Referencia:** §1.3.2 [AMQP]

La garantía «al menos una vez» no pierde mensajes, pero puede duplicarlos; el mecanismo habitual de protección es una clave de desduplicación almacenada por el consumidor.

### 13. Según el enunciado correcto del teorema CAP, ¿qué elección se plantea?

- a) Cuando se produce una partición de red, hay que elegir entre consistencia y disponibilidad
- b) Hay que elegir dos de las tres propiedades en cualquier circunstancia
- c) Hay que elegir entre consistencia y tolerancia a particiones, siendo la disponibilidad siempre obligatoria

**Respuesta correcta:** a) · **Referencia:** §1.3.3 [BREWER]

En un sistema distribuido real las particiones ocurren, de modo que la tolerancia a particiones no es opcional. Cuando no hay partición, se pueden tener consistencia y disponibilidad a la vez.

### 14. Los algoritmos de consenso como Paxos o Raft exigen quórum de mayoría. ¿Qué consecuencia práctica tiene sobre el número de nodos del despliegue?

- a) Que conviene desplegar un número par de nodos para repartir la carga
- b) Que se despliega un número impar de nodos, porque añadir un cuarto a un grupo de tres no aumenta la tolerancia a fallos
- c) Que basta con dos nodos si ambos están en zonas de disponibilidad distintas

**Respuesta correcta:** b) · **Referencia:** §1.3.3 [BREWER]

Con N nodos se toleran (N-1)/2 caídas: con tres nodos, una; con cinco, dos.

### 15. El modelo BASE, característico de muchos sistemas distribuidos NoSQL, se caracteriza frente a ACID por:

- a) Garantizar atomicidad y aislamiento a costa de la disponibilidad
- b) Exigir bloqueo pesimista en todas las operaciones de escritura
- c) Priorizar la disponibilidad y admitir consistencia eventual

**Respuesta correcta:** c) · **Referencia:** §1.3.3 [DYNAMO]

BASE responde a las iniciales de básicamente disponible, estado blando y consistencia eventual, y está pensado para escalar horizontalmente, a diferencia de ACID.

### 16. ¿Cuántas características esenciales, modelos de servicio y modelos de despliegue define el NIST en la SP 800-145?

- a) Cinco características, tres modelos de servicio y cuatro modelos de despliegue
- b) Seis características, cuatro modelos de servicio y tres modelos de despliegue
- c) Cuatro características, tres modelos de servicio y tres modelos de despliegue

**Respuesta correcta:** a) · **Referencia:** §2.1.1 [NIST145]

Es la cifra que hay que llevar grabada: 5-3-4. La definición se publicó en septiembre de 2011 y no ha sido sustituida.

### 17. Un centro de datos municipal está completamente virtualizado, pero para crear una máquina hay que abrir un tique y esperar a que un técnico la cree a mano. ¿Es una nube privada según el NIST?

- a) Sí, porque la infraestructura es de uso exclusivo de una organización
- b) No, porque falta el autoservicio bajo demanda y la medición del consumo, y sin todas las características esenciales no es nube
- c) Sí, siempre que exista un hipervisor de tipo 1

**Respuesta correcta:** b) · **Referencia:** §2.1.1 [NIST145]

Las cinco características del NIST son acumulativas y necesarias. Un centro de datos virtualizado sin autoservicio ni medición es virtualización, no nube: la virtualización es un habilitador, no un sinónimo.

### 18. ¿Qué característica añade la norma ISO/IEC 17788, equivalente a la Recomendación ITU-T Y.3500, respecto de las cinco del NIST?

- a) La portabilidad de aplicaciones
- b) La interoperabilidad semántica
- c) La multitenencia

**Respuesta correcta:** c) · **Referencia:** §2.1.2 [ISO17788]

ISO la hace explícita como sexta característica clave, mientras que el NIST la considera implícita dentro de la agrupación de recursos.

### 19. Los cinco actores de la arquitectura de referencia del NIST (SP 500-292) son:

- a) Consumidor, proveedor, desarrollador, integrador y auditor
- b) Consumidor, proveedor, intermediario, portador y auditor
- c) Cliente, encargado, subencargado, responsable y autoridad de control

**Respuesta correcta:** b) · **Referencia:** §2.1.2 [NIST292]

El portador aporta la conectividad y el auditor la evaluación independiente; son los dos que se olvidan con más frecuencia. El intermediario puede ser de intermediación, de agregación o de arbitraje.

### 20. ¿Cuál es la diferencia principal entre la computación en malla (grid) y la computación en la nube?

- a) La malla federa recursos de varias organizaciones con motivación colaborativa y aprovisionamiento planificado; la nube es normalmente de un proveedor, con pago por uso y aprovisionamiento bajo demanda
- b) La malla utiliza virtualización y la nube no
- c) La malla es siempre pública y la nube es siempre privada

**Respuesta correcta:** a) · **Referencia:** §2.2 [NIST145]

La nube heredó de la malla la idea de federación, pero cambió el modelo económico y el tiempo de aprovisionamiento.

### 21. ¿Cuál es la diferencia esencial entre una máquina virtual y un contenedor?

- a) La máquina virtual comparte el núcleo del anfitrión y el contenedor no
- b) El contenedor solo puede ejecutar aplicaciones escritas en lenguajes interpretados
- c) La máquina virtual virtualiza el hardware y lleva su propio sistema operativo; el contenedor virtualiza el sistema operativo y comparte el núcleo del anfitrión

**Respuesta correcta:** c) · **Referencia:** §2.3.1 [OCI]

De ahí que el contenedor arranque en segundos y ofrezca mucha más densidad, pero con un aislamiento menor.

### 22. ¿Qué organización define las especificaciones abiertas de imagen, ejecución y distribución de contenedores que sustentan su portabilidad entre nubes?

- a) La Open Container Initiative (OCI)
- b) El Instituto Nacional de Estándares y Tecnología (NIST)
- c) La Unión Internacional de Telecomunicaciones (UIT)

**Respuesta correcta:** a) · **Referencia:** §2.3.1 [OCI]

Gracias a esa normalización, una imagen construida en un entorno se ejecuta igual en otro, lo que convierte a los contenedores en el mecanismo de portabilidad entre nubes más eficaz disponible.

### 23. En infraestructura como código, ¿qué significa que una descripción sea idempotente?

- a) Que puede escribirse en cualquier lenguaje de programación
- b) Que aplicarla varias veces deja el sistema en el mismo estado que aplicarla una sola vez
- c) Que solo puede aplicarse una vez y después queda bloqueada

**Respuesta correcta:** b) · **Referencia:** §2.3.2 [TERRAFORM]

Es lo que diferencia una herramienta declarativa de un guion imperativo, que al ejecutarse dos veces puede duplicar recursos o fallar.

### 24. El modelo declarativo de un orquestador de contenedores consiste en que:

- a) El operador ejecuta órdenes secuenciales de creación y destrucción de recursos
- b) El orquestador ejecuta un guion al arrancar y no vuelve a intervenir
- c) El operador describe el estado deseado y un bucle de control trabaja para que el estado real coincida con él

**Respuesta correcta:** c) · **Referencia:** §2.3.2 [K8S]

Ese cambio de mentalidad, de dar órdenes a declarar objetivos, es el que hace posible la autorreparación de instancias que dejan de responder.

### 25. Una unidad mantiene veinte instancias encendidas las veinticuatro horas del año en la nube pública porque «así no hay sorpresas». ¿Qué está ocurriendo?

- a) Está pagando el precio de la nube sin ejercer la elasticidad, lo que puede salir más caro que comprar los servidores
- b) Está aplicando correctamente el principio de alta disponibilidad
- c) Está aprovechando el descuento por instancias de capacidad sobrante

**Respuesta correcta:** a) · **Referencia:** §2.4 [FINOPS]

El ahorro no lo produce la nube, sino la elasticidad efectivamente ejercida: una instancia encendida permanentemente no es elástica.

### 26. ¿Cuál es la causa dominante de los incidentes de seguridad en nube pública?

- a) La vulneración del hipervisor del proveedor
- b) La configuración incorrecta por parte del cliente
- c) El fallo del aislamiento entre inquilinos

**Respuesta correcta:** b) · **Referencia:** §2.4, §4.1.1 [NIST144]

Almacenamiento de objetos expuesto públicamente, credenciales incrustadas en el código y permisos excesivos concentran la mayor parte de los incidentes reales publicados.

### 27. Según la definición del NIST, en el modelo IaaS el consumidor:

- a) No controla el sistema operativo, que gestiona el proveedor
- b) Controla la infraestructura de nube subyacente, incluidos los servidores físicos
- c) No gestiona la infraestructura subyacente, pero sí controla los sistemas operativos, el almacenamiento y las aplicaciones desplegadas

**Respuesta correcta:** c) · **Referencia:** §3.1.1 [NIST145]

Puede además tener un control limitado de componentes de red seleccionados, como los cortafuegos de anfitrión.

### 28. Un servicio municipal debe conservar durante años la documentación que la ciudadanía adjunta a sus solicitudes: ficheros que se escriben una vez, se leen pocas y crecen sin límite previsible. ¿Qué tipo de almacenamiento es el adecuado?

- a) Almacenamiento de bloques conectado a cada instancia
- b) Almacenamiento de objetos, accesible por HTTP y con clases de acceso según la frecuencia de uso
- c) Almacenamiento de ficheros compartido por NFS entre todas las instancias

**Respuesta correcta:** b) · **Referencia:** §3.1.1 [CSP]

Es prácticamente ilimitado, barato y muy durable. Su limitación es que un objeto no se modifica parcialmente, sino que se sustituye entero, y que su latencia es mayor.

### 29. ¿Qué distingue la elasticidad de la escalabilidad?

- a) Que la elasticidad exige automatismo, rapidez y bidireccionalidad, es decir, también decrecer
- b) Que la escalabilidad solo se aplica al almacenamiento y la elasticidad al cómputo
- c) Que la escalabilidad es una característica esencial del NIST y la elasticidad no

**Respuesta correcta:** a) · **Referencia:** §3.1.2 [NIST145]

Un sistema puede ser escalable —se le pueden añadir servidores— y nada elástico, si hacerlo requiere intervención manual y semanas de plazo.

### 30. Para que el escalado horizontal funcione, ¿qué condición debe cumplir la aplicación?

- a) Debe ejecutarse sobre un hipervisor de tipo 1
- b) Debe estar escrita en un lenguaje compilado
- c) Debe ser sin estado, de modo que la sesión del usuario no viva en la memoria de una instancia concreta

**Respuesta correcta:** c) · **Referencia:** §3.1.2 [12FACTOR]

Si la sesión reside en la memoria local, no se pueden añadir ni retirar instancias sin romper sesiones de usuario en curso.

### 31. Ante una carga con una base estable conocida y picos puntuales, la combinación de facturación más eficiente es:

- a) Cubrir la base con instancias reservadas y el pico con instancias bajo demanda
- b) Cubrir todo con instancias de capacidad sobrante para maximizar el descuento
- c) Cubrir todo con instancias reservadas a tres años

**Respuesta correcta:** a) · **Referencia:** §3.1.2 [FINOPS]

Las instancias de capacidad sobrante pueden ser retiradas por el proveedor con poco aviso, por lo que solo son adecuadas para procesos por lotes tolerantes a la interrupción.

### 32. Según la definición del NIST, en el modelo PaaS el consumidor no gestiona ni controla:

- a) Las aplicaciones que él mismo despliega
- b) Los ajustes de configuración del entorno de alojamiento
- c) La red, los servidores, los sistemas operativos ni el almacenamiento

**Respuesta correcta:** c) · **Referencia:** §3.2.1 [NIST145]

Sí controla, en cambio, las aplicaciones desplegadas y, posiblemente, los ajustes de configuración del entorno de alojamiento.

### 33. ¿Cuál es la frontera exacta que separa IaaS de PaaS?

- a) La virtualización: en PaaS la pone el proveedor y en IaaS el cliente
- b) El sistema operativo: en IaaS lo administra el cliente y en PaaS lo administra el proveedor
- c) Los datos: en PaaS pasan a ser responsabilidad del proveedor

**Respuesta correcta:** b) · **Referencia:** §3, §3.2.1 [NIST145] [CCN823]

La virtualización marca la frontera entre el modelo local y IaaS. Los datos y las identidades no cambian de dueño en ningún modelo: son siempre del cliente.

### 34. El término «sin servidor» (serverless) significa que:

- a) El cliente no ve, no dimensiona ni paga los servidores cuando no se usan, aunque los servidores siguen existiendo
- b) La aplicación se ejecuta directamente en el navegador del usuario, sin ningún servidor implicado
- c) El proveedor entrega servidores físicos sin hipervisor

**Respuesta correcta:** a) · **Referencia:** §3.2.1 [CSP]

Se factura por número de invocaciones y tiempo de ejecución, y su contrapartida técnica es el arranque en frío tras un periodo de inactividad.

### 35. Al contratar una base de datos gestionada, ¿qué sigue siendo responsabilidad del cliente?

- a) Aplicar los parches del motor de base de datos y sustituir los discos averiados
- b) El esquema, las consultas, los índices, los datos y la política de retención y restauración
- c) La replicación entre zonas de disponibilidad y la programación de las copias

**Respuesta correcta:** b) · **Referencia:** §3.2.2 [CCN823]

El servicio hace copias, pero no impide que el cliente borre una tabla: la recuperación ante un error propio exige haber definido la retención y haber probado la restauración.

### 36. ¿Cuál es la consecuencia menos intuitiva y más relevante del modelo SaaS para una Administración?

- a) Que los datos se cifran obligatoriamente en origen
- b) Que el proveedor asume la responsabilidad jurídica sobre los datos personales
- c) Que el cliente pierde el control del calendario de versiones, porque el proveedor actualiza para todos a la vez

**Respuesta correcta:** c) · **Referencia:** §3.3.1 [SAAS-SUITES]

Por eso los contratos deben incluir preaviso de cambios funcionales, entornos de prueba y compromisos de compatibilidad de las integraciones.

### 37. En un producto SaaS, la adaptación a las necesidades de una organización cliente se realiza normalmente:

- a) Por configuración y por extensión mediante API o complementos, no por modificación del código
- b) Por modificación del código fuente del producto para ese cliente concreto
- c) Por sustitución de la base de datos del producto por una propia

**Respuesta correcta:** a) · **Referencia:** §3.3.1 [SAAS-SUITES]

El código es común a todos los inquilinos. Cuando el producto no contempla un comportamiento exigido, las salidas son adaptar el procedimiento, pagar un desarrollo que el fabricante incorpore al producto estándar o construir una capa propia alrededor.

### 38. En un modelo de multitenencia agrupado (pooled), ¿de qué depende enteramente el aislamiento entre organizaciones?

- a) Del hipervisor del proveedor
- b) Del cifrado del canal de comunicaciones
- c) Del software, ya que basta con que una consulta olvide filtrar por el identificador de inquilino para exponer datos de otra organización

**Respuesta correcta:** c) · **Referencia:** §3.3.2 [ISO17788]

Por eso el filtrado se aplica en la capa de acceso a datos o mediante seguridad a nivel de fila, y no se confía en que cada consulta lo recuerde.

### 39. Una herramienta en modo SaaS para 3.000 empleados de los que solo 400 la usan a diario. ¿Qué modalidad de licenciamiento ajusta mejor el coste al uso real?

- a) Por usuario nombrado, dando de alta a los 3.000
- b) Por usuario concurrente o por transacción realizada
- c) Por niveles de funcionalidad, contratando el nivel superior para todos

**Respuesta correcta:** b) · **Referencia:** §3.3.2 [LCSP]

La elección del modelo de licencia puede mover el precio del contrato en un factor de cinco sin cambiar ni una línea del pliego técnico.

### 40. Respecto de las denominaciones XaaS (FaaS, CaaS, DBaaS, DaaS…), es correcto afirmar que:

- a) No son categorías del NIST, que reconoce únicamente tres modelos de servicio, y algunas siglas son ambiguas, como CaaS y DaaS
- b) Sustituyen a los tres modelos clásicos desde la revisión de la SP 800-145
- c) Son las siete categorías de servicio que define en exclusiva la norma ISO/IEC 17789

**Respuesta correcta:** a) · **Referencia:** §3.4 [NIST145] [ISO17788]

CaaS puede significar contenedores o comunicaciones, y DaaS escritorio o datos: en una respuesta escrita conviene desarrollar siempre la sigla.

### 41. Respecto de la nube privada, según la definición del NIST:

- a) Debe estar necesariamente en las instalaciones de la organización que la usa
- b) Puede ser propiedad de un tercero, estar operada por un tercero y ubicarse fuera de las instalaciones; lo que la define es que su uso está reservado a una sola organización
- c) Solo puede ofrecer el modelo de servicio IaaS

**Respuesta correcta:** b) · **Referencia:** §4.2.1 [NIST145]

Es el error más frecuente al estudiar los modelos de despliegue: privada no significa «en casa».

### 42. Dentro de la organización geográfica de una nube pública, ¿qué es una zona de disponibilidad?

- a) El área geográfica completa en la que el proveedor ofrece servicio
- b) Un segmento lógico de red aislado dentro de la red virtual del cliente
- c) Un centro de datos independiente en energía, refrigeración y red, unido a los demás de su región por enlaces de baja latencia

**Respuesta correcta:** c) · **Referencia:** §1.3.3, §4.1 [CSP]

Repartir réplicas entre zonas protege frente a la caída de un edificio; repartirlas entre regiones protege frente a una catástrofe territorial, a costa de latencia y de posibles restricciones jurídicas.

### 43. En el modelo de responsabilidad compartida, ¿qué conserva siempre el cliente, sea cual sea el modelo de servicio?

- a) Los datos y su clasificación, la gestión de identidades y accesos, y la configuración de los servicios contratados
- b) El sistema operativo, el middleware y el hipervisor
- c) La red troncal, el hardware y el aislamiento entre inquilinos

**Respuesta correcta:** a) · **Referencia:** §4.1.1 [CCN823]

La línea que separa las responsabilidades se desplaza con el modelo de servicio, pero estas tres nunca cambian de dueño.

### 44. Un almacén de objetos con documentación ciudadana queda accesible públicamente por una política de acceso mal fijada por el personal del Ayuntamiento. ¿Quién ha incumplido?

- a) El proveedor, por no impedir configuraciones inseguras
- b) El Ayuntamiento, porque la configuración de los servicios es responsabilidad del cliente, y estaría además ante una brecha de datos personales notificable en 72 horas
- c) Ninguno de los dos, al tratarse de un riesgo inherente a la nube pública

**Respuesta correcta:** b) · **Referencia:** §4.1.1 [RGPD] [CCN823]

Es el ejemplo que mejor explica por qué el reparto de responsabilidades debe constar en el pliego y no darse por supuesto.

### 45. Una nube privada virtual (VPC) contratada dentro de un proveedor de nube pública:

- a) Convierte el despliegue en una nube privada según el NIST
- b) Equivale a una nube comunitaria si la usan varias Administraciones
- c) Sigue siendo un despliegue en nube pública, porque el hardware continúa siendo compartido y el aislamiento es solo lógico

**Respuesta correcta:** c) · **Referencia:** §4.2.1 [NIST145]

La palabra clave del NIST para «privada» es el uso exclusivo de la infraestructura por una sola organización, no el aislamiento lógico de la red.

### 46. Según el NIST, en una nube híbrida las infraestructuras que se combinan:

- a) Se fusionan en una única infraestructura gestionada por el proveedor principal
- b) Permanecen como entidades separadas y distintas, unidas por una tecnología que permite la portabilidad de datos y aplicaciones
- c) Deben ser necesariamente una privada y una comunitaria

**Respuesta correcta:** b) · **Referencia:** §4.3.1 [NIST145]

La definición es exigente: no basta con tener cosas en dos sitios, hace falta un mecanismo real de portabilidad.

### 47. El patrón híbrido consistente en atender la carga base en la nube privada y desbordar el pico a la nube pública se denomina:

- a) Desbordamiento a la nube (cloud bursting)
- b) Reparto por sensibilidad
- c) Modernización progresiva

**Respuesta correcta:** a) · **Referencia:** §4.3.1 [NIST145]

Es el patrón adecuado para campañas, matrículas y plazos de presentación, donde la demanda se concentra en unas horas concretas del año.

### 48. ¿Qué distingue la interoperabilidad de la portabilidad según la norma ISO/IEC 19941?

- a) La interoperabilidad se refiere a los datos y la portabilidad a las personas usuarias
- b) Son términos sinónimos en el ámbito de la computación en la nube
- c) Interoperar es intercambiar información y usarla estando cada sistema en su sitio; portar es mover datos o aplicaciones de un entorno a otro

**Respuesta correcta:** c) · **Referencia:** §4.3.1 [ISO19941]

Un sistema puede ser perfectamente interoperable y absolutamente imposible de portar: esa es justamente la situación que produce la dependencia del proveedor.

### 49. La nube comunitaria se define como infraestructura aprovisionada para:

- a) El público general, con acceso abierto y pago por uso
- b) El uso exclusivo de una comunidad específica de organizaciones que comparten intereses, misión, requisitos de seguridad o cumplimiento
- c) Un consorcio de proveedores privados que reparten entre sí la capacidad sobrante

**Respuesta correcta:** b) · **Referencia:** §4.4 [NIST145]

Es el modelo naturalmente adecuado al sector público y comparte la lógica de los servicios compartidos de la Administración; su dificultad principal es de gobernanza.

### 50. ¿En qué se diferencian una estrategia multicloud y un despliegue de nube híbrida?

- a) Multicloud es usar varios proveedores del mismo tipo, normalmente varias nubes públicas; híbrida es combinar modelos de despliegue distintos unidos por portabilidad
- b) Multicloud es un modelo de despliegue del NIST e híbrida no
- c) Multicloud exige que la misma carga se ejecute simultáneamente en todos los proveedores

**Respuesta correcta:** a) · **Referencia:** §4.4 [NIST145] [ESTRATEGIA-CLOUD]

Ambas pueden darse a la vez: una entidad con nube privada propia y servicios en dos proveedores públicos es híbrida y multicloud simultáneamente.

### 51. ¿Qué precepto obliga a que una empresa privada que presta servicios en la nube a una entidad del sector público cumpla el Esquema Nacional de Seguridad?

- a) El artículo 31 del Real Decreto 311/2022
- b) El artículo 40 del Real Decreto 311/2022
- c) El artículo 2.3 del Real Decreto 311/2022

**Respuesta correcta:** c) · **Referencia:** §5.1.1 [ENS]

Extiende el ENS a los sistemas de información de las entidades del sector privado que, en virtud de una relación contractual, presten servicios o provean soluciones al sector público para el ejercicio de sus competencias y potestades administrativas, incluida la obligación de contar con política de seguridad.

### 52. Las categorías de seguridad del ENS y su determinación son:

- a) BÁSICA, MEDIA y ALTA, correspondiendo al sistema la categoría de la dimensión más exigente entre disponibilidad, integridad, confidencialidad, autenticidad y trazabilidad
- b) BAJA, MEDIA y CRÍTICA, correspondiendo al sistema la media aritmética de las dimensiones
- c) BÁSICA y ALTA únicamente, según haya o no datos personales

**Respuesta correcta:** a) · **Referencia:** §5.1.1 [ENS]

Las categorías están en el artículo 40 y las cinco dimensiones, en el Anexo I. Esta valoración es el primer paso de cualquier proyecto de nube.

### 53. En el Anexo II del ENS, ¿qué grupo de medidas del marco operacional se refiere específicamente a los servicios en la nube?

- a) mp.info
- b) op.nub
- c) org.pro

**Respuesta correcta:** b) · **Referencia:** §5.1.1 [ENS]

El grupo op.nub, con la medida op.nub.1 de protección de los servicios en la nube, es una novedad del Real Decreto 311/2022, igual que op.ext.3 (protección de la cadena de suministro) y op.ext.4 (interconexión de sistemas).

### 54. Respecto de la auditoría y la conformidad con el ENS:

- a) Todos los sistemas requieren certificación por entidad acreditada, con periodicidad anual
- b) La auditoría es voluntaria salvo que se traten datos personales
- c) La auditoría regular ordinaria se realiza al menos cada dos años, y los sistemas de categoría BÁSICA solo requieren autoevaluación para declarar la conformidad

**Respuesta correcta:** c) · **Referencia:** §5.1.1 [ENS]

Los de categoría MEDIA y ALTA requieren auditoría de certificación por entidad acreditada. La auditoría se regula en el artículo 31 y los procedimientos de conformidad en el artículo 38.

### 55. ¿Cuál es la guía del Centro Criptológico Nacional específicamente dedicada a la utilización de servicios en la nube?

- a) La CCN-STIC 823
- b) La CCN-STIC 105
- c) La CCN-STIC 817

**Respuesta correcta:** a) · **Referencia:** §5.1.1 [CCN823] [CCN105]

Identifica las medidas y requisitos exigibles al proveedor y, sobre todo, cómo se reparten las responsabilidades entre cliente y proveedor según el modelo de servicio. La 105 publica el catálogo CPSTIC de productos y servicios y la 817 trata la gestión de ciberincidentes.

### 56. Cuando una Administración contrata un servicio en la nube que trata datos personales, el proveedor tiene la condición de:

- a) Corresponsable del tratamiento, junto con la Administración
- b) Encargado del tratamiento, conforme al artículo 28 del RGPD, siguiendo instrucciones documentadas del responsable
- c) Tercero receptor de una cesión de datos, que requiere consentimiento de las personas afectadas

**Respuesta correcta:** b) · **Referencia:** §5.1.2 [RGPD]

El contrato debe prohibir la subcontratación sin autorización y obligar a devolver o suprimir los datos, incluidas las copias, al finalizar la prestación. La Administración sigue siendo responsable del tratamiento.

### 57. El personal de soporte de un proveedor, establecido en un tercer país, accede en remoto a datos alojados en servidores situados en la Unión Europea. Desde el punto de vista del RGPD, esto es:

- a) Un tratamiento interno que no requiere garantías adicionales, al no salir los datos de la Unión
- b) Una comunicación de datos sometida únicamente al deber de confidencialidad
- c) Una transferencia internacional de datos, sujeta al capítulo V del RGPD

**Respuesta correcta:** c) · **Referencia:** §5.1.2 [SCHREMSII] [RGPD]

El acceso remoto desde un tercer país es transferencia aunque los servidores estén en la Unión. Tras la sentencia Schrems II hay que evaluar el marco jurídico del país de destino y adoptar medidas complementarias, siendo el cifrado con claves gestionadas exclusivamente por la Administración la más eficaz.

### 58. Conforme al Reglamento (UE) 2023/2854 (Reglamento de Datos), ¿desde qué fecha no podrán los proveedores imponer tarifas de cambio a sus clientes?

- a) Desde el 11 de enero de 2024
- b) Desde el 12 de enero de 2027
- c) Desde el 10 de julio de 2023

**Respuesta correcta:** b) · **Referencia:** §5.1.2 [DATAACT]

Lo establece el artículo 29, dentro del capítulo VI (artículos 23 a 31) sobre cambio entre servicios de tratamiento de datos. Durante el periodo transitorio solo pueden repercutirse costes reducidos directamente vinculados al proceso de cambio.

### 59. La Estrategia de servicios en la nube híbrida para las Administraciones Públicas, de diciembre de 2022, se estructura en:

- a) Siete pilares y diecinueve iniciativas, con el principio de «nube híbrida primero»
- b) Tres ejes y doce medidas, con el principio de «cloud first»
- c) Cinco objetivos y veinte acciones, con el principio de «nube pública por defecto»

**Respuesta correcta:** a) · **Referencia:** §5.2.1 [ESTRATEGIA-CLOUD]

El principio español no es «cloud first» sin matices: prioriza el aprovisionamiento en la nube frente a las soluciones tradicionales, pero en un modelo híbrido que combina la nube privada de la Administración con proveedores externos.

### 60. ¿Qué es NubeSARA?

- a) La red de interconexión de las Administraciones Públicas españolas
- b) El catálogo de productos y servicios de seguridad cualificados por el Centro Criptológico Nacional
- c) La solución de nube privada de la Administración General del Estado, desplegada por la Secretaría General de Administración Digital en 2015, con catálogo de servicios IaaS y PaaS con costes y acuerdos de nivel de servicio

**Respuesta correcta:** c) · **Referencia:** §5.2.2 [ESTRATEGIA-CLOUD]

No debe confundirse la red SARA, que es la red de interconexión, con NubeSARA, que es la nube desplegada sobre ella y que evoluciona hacia una «tienda» de soluciones para todas las Administraciones.

## Preguntas sobre los casos prácticos

### Caso 1. Diseño distribuido y elección del modelo de servicio

#### 1. En el supuesto planteado, el equipo descompone el portal en tres servicios: validación de empadronamiento, gestión de solicitudes y notificación. ¿Qué criterio justifica esa descomposición?

- a) Separar las piezas que tienen ritmos de cambio y de carga distintos, dimensionando el número de servicios al equipo disponible.
- b) Hacer los servicios lo más pequeños posible, porque cuantos más microservicios haya, más fácil resulta operar el sistema.
- c) Crear un servicio por cada tabla de la base de datos, porque así cada uno queda aislado de los cambios de los demás.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §1.2.2

La validación se dispara el día de la apertura, la notificación semanas después y la gestión de solicitudes soporta el estado; con tres personas y dos meses, más servicios trasladarían la complejidad a la operación.

#### 2. ¿Cómo debe comunicarse el portal con el registro electrónico, que admite 5 asientos por segundo, si se esperan 40.000 solicitudes en la primera hora?

- a) De forma síncrona, porque el registro absorbe 40.000 asientos por hora con 5 por segundo.
- b) De forma asíncrona, con una cola, porque el registro solo absorbe 18.000 asientos por hora.
- c) De forma síncrona con reintentos, porque los reintentos del usuario reparten la carga en el tiempo.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §1.3.2

5 asientos por segundo son 18.000 por hora: una llamada síncrona daría errores de tiempo de espera y los reintentos multiplicarían la carga. La cola absorbe el pico.

#### 3. ¿Cuántas solicitudes quedarán acumuladas en la cola al acabar la primera hora y cuánto tardarán aproximadamente en drenarse una vez cese el pico?

- a) Unas 18.000, que se drenan en unos 60 minutos.
- b) Unas 40.000, que se drenan en unos 133 minutos.
- c) Unas 22.000, que se drenan en unos 73 minutos.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §1.3.2

Entran 40.000 y salen 18.000, de modo que quedan 22.000; a 5 por segundo son 4.400 segundos, unos 73 minutos.

#### 4. Con el registro asíncrono, una solicitud presentada a las 9:05 puede no asentarse hasta pasadas las 10:00. ¿Qué fecha y hora de presentación se le reconoce?

- a) La del asiento en el registro electrónico, que es la única con valor jurídico de presentación.
- b) La de la solicitud, acreditada por el justificante con número de referencia y marca de tiempo.
- c) La del envío de la notificación de acuse de recibo, cuando el solicitante la recibe en su correo.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §1.3.2

La cola no compromete la garantía jurídica: el justificante con marca de tiempo acredita el momento de presentación, aunque el asiento se practique después.

#### 5. La cola hacia el registro ofrece la garantía de entrega «al menos una vez». ¿Qué debe cumplir el consumidor que practica los asientos?

- a) Ser idempotente mediante una clave de desduplicación, para que un reintento no genere dos asientos.
- b) Confirmar cada mensaje antes de procesarlo, para que la cola no vuelva a entregarlo en ningún caso.
- c) Procesar los mensajes en paralelo sin control, porque la cola ya garantiza que no habrá duplicados.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §1.3.2

«Al menos una vez» significa que un mensaje puede llegar repetido; procesarlo dos veces debe producir el mismo efecto que una, y la clave de desduplicación lo asegura.

#### 6. ¿Cómo debe resolverse la consulta del portal al padrón para validar el empadronamiento?

- a) De forma asíncrona por evento, enviando el resultado por correo al solicitante horas después de presentar la solicitud.
- b) De forma síncrona sin límite, consultando el padrón cada vez que el solicitante rellena un campo del formulario.
- c) De forma síncrona pero acotada y cacheada: tiempo de espera corto, reintento limitado y una consulta por solicitud.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §1.3.1

La validación debe resolverse en la misma pantalla, pero sin trasladar el pico al padrón: espera corta, reintento limitado, caché y una sola consulta por solicitud, no una por campo.

#### 7. ¿Qué modelo de servicio es el adecuado para la validación de empadronamiento?

- a) PaaS con caché, y no FaaS, porque el arranque en frío arruinaría la experiencia justo en el pico.
- b) FaaS, porque es una tarea corta, sin estado y disparada por evento, igual que la notificación.
- c) SaaS, porque la validación del padrón es un producto comercial que no requiere desarrollo propio.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §3.2

La función bajo demanda encaja con la notificación, que nadie espera; la validación se hace con el usuario delante y en el momento de mayor carga, por lo que no puede sufrir arranques en frío.

#### 8. Si para la capa web del portal se eligiera IaaS en lugar de PaaS, ¿qué trabajo adicional asumiría el equipo?

- a) El mantenimiento del hardware físico y de la red del centro de datos del proveedor.
- b) Ninguno, porque en IaaS el proveedor administra también el sistema operativo y el código.
- c) El parcheado y el endurecimiento del sistema operativo de todas las instancias del pico.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §3.1, §3.2

La frontera entre IaaS y PaaS es el sistema operativo: en PaaS lo administra el proveedor; en IaaS, el cliente. El hardware sigue siendo del proveedor en ambos casos.

#### 9. ¿Dónde deben guardarse los documentos escaneados que adjuntan los solicitantes?

- a) En discos de bloques de las instancias web, redimensionándolos a medida que crezca el volumen.
- b) En almacenamiento de objetos, con clase de acceso esporádico o de archivo pasados unos meses.
- c) En la memoria de las instancias del portal, para servirlos con la máxima rapidez posible.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §3.1.1

Se escriben una vez, se leen pocas, deben conservarse años y crecen sin límite previsible: el almacenamiento de objetos es más barato y durable que redimensionar discos.

#### 10. La capa web guarda la sesión del solicitante y los ficheros temporales en la memoria y el disco local de cada instancia. ¿Qué consecuencia tiene?

- a) Ninguna, porque el escalado vertical añade instancias de forma automática sin afectar a las sesiones en curso.
- b) Que el portal será más rápido en el pico, porque cada instancia sirve a sus usuarios desde su propio disco local.
- c) Que no se pueden añadir ni retirar instancias sin romper sesiones: deben ir a una caché o almacén compartido.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 4 · §3.1.2

Para escalar horizontalmente la aplicación debe ser sin estado: la sesión no puede vivir en una instancia concreta que puede retirarse.

### Caso 2. Modelo de despliegue: nube híbrida para el portal de ayudas

#### 1. En el supuesto planteado, la plataforma de virtualización municipal ofrece autoservicio por portal y medición del consumo por unidad. ¿Qué característica falta verificar para calificarla de nube privada según el NIST?

- a) La multitenencia, que el NIST exige como sexta característica esencial de la nube.
- b) La elasticidad: que aprovisionar y liberar sea automático y rápido, sin tique ni técnico.
- c) La ubicación en el centro de datos propio, porque una nube privada no puede estar fuera.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §2.1.1

Acceso por red y agrupación de recursos se dan por definición; si crear una máquina exige abrir un tique y esperar a un técnico, es virtualización, no nube.

#### 2. Aun calificada como nube privada, ¿qué límite tiene la elasticidad de la plataforma municipal?

- a) Está acotada por la capacidad instalada: las 40 máquinas virtuales adicionales son su techo físico.
- b) Ninguno, porque una nube privada ofrece la misma capacidad percibida como ilimitada que la pública.
- c) Solo puede crecer y nunca decrecer, porque las máquinas creadas ya no pueden liberarse después.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §4.2.1

A diferencia de la capacidad percibida como ilimitada de la nube pública, la nube privada solo puede crecer hasta lo que tiene instalado.

#### 3. ¿Dónde debe desplegarse la base de datos de solicitudes y con qué patrón híbrido?

- a) En la nube pública, con desbordamiento, porque es la pieza que recibe la avalancha.
- b) En la nube pública, con desarrollo y pruebas, porque así se abarata su mantenimiento.
- c) En la nube privada, con reparto por sensibilidad, porque contiene datos de salud.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §4.3.1

Los datos más sensibles se quedan donde la organización los controla; el desbordamiento a la pública se reserva para la capa que recibe el pico.

#### 4. ¿Qué componentes van a la nube pública con el patrón de desbordamiento?

- a) La capa web del portal con su CDN y la función de notificación.
- b) El padrón municipal y el registro electrónico, por su volumen.
- c) La base de datos de solicitudes y los documentos con datos de salud.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §4.3.1

Son las piezas que reciben la avalancha y las que mejor aprovechan la elasticidad pública; el padrón y el registro no se mueven por ser sistemas críticos con muchas integraciones internas.

#### 5. ¿Qué condiciones técnicas deben cumplirse para que la unión entre la nube privada y la pública funcione?

- a) Mismo fabricante de hipervisor en ambos lados, rangos de direcciones idénticos y una consola de gestión en cada nube.
- b) Conectividad suficiente y no única, identidad federada, direccionamiento sin solapamientos y observabilidad unificada.
- c) Un único enlace de 1 Gbps, cuentas de usuario distintas en cada nube y registros de actividad separados por proveedor.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.3.1

Las mismas cuentas y roles deben valer a ambos lados, los rangos no pueden solaparse y un incidente que atraviesa dos nubes es indiagnosticable con dos consolas separadas.

#### 6. ¿Qué elemento evita que el pico de solicitudes en la capa pública se propague al padrón y al registro de la nube privada?

- a) Una segunda conexión de 1 Gbps a internet, para que el tráfico del pico llegue antes a la nube privada.
- b) La replicación del padrón en la nube pública, para que las consultas no tengan que cruzar el enlace.
- c) Una cola de amortiguación en el sentido pública → privada, con limitación de tasa y caché de validaciones.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestiones 2 y 4 · §4.3.1

La cola desacopla los dos lados: el portal puede recibir la avalancha mientras los sistemas internos procesan a su ritmo.

#### 7. El sistema de solicitudes es de categoría ALTA en confidencialidad. ¿Qué consecuencia tiene sobre la elección del proveedor?

- a) Ninguna, porque la categoría ALTA solo obliga a cifrar los datos, sea cual sea la jurisdicción a la que esté sometido el proveedor.
- b) Que sus datos solo pueden manejarlos empresas sometidas en exclusiva a la jurisdicción comunitaria, o quedarse en la nube privada.
- c) Que basta con que los servidores estén en la Unión Europea, aunque la matriz del proveedor esté sometida a un tercer país.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §5.1.2

Es el criterio del pilar de soberanía del dato de la Estrategia de servicios en la nube híbrida para las Administraciones Públicas.

#### 8. Al haber datos de salud en la documentación adjunta, ¿qué procede antes del tratamiento?

- a) Una evaluación de impacto previa (art. 35 RGPD), con intervención del delegado de protección de datos.
- b) Una autoevaluación de conformidad con el ENS, que sustituye a cualquier análisis de protección de datos.
- c) La publicación de los datos anonimizados en el portal de transparencia, antes de abrir la convocatoria.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §5.1.2

Los datos de salud son categoría especial (art. 9 RGPD); su tratamiento exige evaluación de impacto previa, y el proveedor será encargado del tratamiento (art. 28 RGPD).

#### 9. Servir los documentos desde la nube pública puede generar un tráfico de salida no previsto. ¿Qué tipo de riesgo es y qué medida lo mitiga?

- a) De disponibilidad: duplicar el enlace con otro operador y degradar el portal si cae.
- b) De seguridad: aplicar mínimo privilegio y un gestor de secretos en la nube pública.
- c) De coste: estimar antes el volumen, usar CDN y caché, y fijar alertas de consumo.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §2.4, §4.1.1

En la nube pública se paga el tráfico de salida; si no se estima y vigila, la factura se dispara.

#### 10. El enlace entre ambas nubes es punto único de fallo. ¿Qué medida corresponde a este riesgo de disponibilidad?

- a) Redundar el enlace por rutas y operadores distintos y prever una degradación controlada del portal si cae.
- b) Contratar instancias reservadas en la nube pública para cubrir la base de carga durante los veinte días.
- c) Empaquetar las aplicaciones en contenedores conformes con la OCI y mantener un plan de reversión probado.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §4.3.1

Si toda la comunicación depende de un único enlace, su caída corta la unión; las instancias reservadas son una medida de coste y la portabilidad OCI, de dependencia del proveedor.

### Caso 3. Contratación, cumplimiento y salida del proveedor

#### 1. En el supuesto planteado, un licitador alega que «el ENS obliga a la Administración, no a las empresas». ¿Qué precepto la refuta?

- a) Ninguno: la alegación es correcta y el ENS solo puede exigirse a las Administraciones Públicas y a sus organismos dependientes.
- b) El artículo 28 del RGPD, que obliga a todo encargado del tratamiento a certificarse en el Esquema Nacional de Seguridad.
- c) El artículo 2.3 del Real Decreto 311/2022, que extiende el ENS a las entidades privadas que prestan servicios al sector público.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §5.1.1 (art. 2.3 RD 311/2022)

El ENS se aplica a los sistemas de las entidades del sector privado que, en virtud de una relación contractual, prestan servicios o proveen soluciones a entidades del sector público, incluida la obligación de tener política de seguridad.

#### 2. Si el sistema al que se presta el servicio es de categoría MEDIA o ALTA, ¿cómo debe acreditar el adjudicatario su conformidad con el ENS?

- a) Mediante una certificación emitida por una entidad de certificación acreditada.
- b) Mediante una declaración responsable basada en una autoevaluación propia.
- c) Mediante su inclusión en el CPSTIC, que sustituye a cualquier otra acreditación.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §5.1.1 (arts. 31 y 38 RD 311/2022)

La declaración basada en autoevaluación solo vale para la categoría BÁSICA; las categorías MEDIA y ALTA exigen certificación. El CPSTIC es una comprobación aconsejable adicional.

#### 3. El licitador del servicio SaaS aloja los datos en la Unión Europea, pero su matriz está sujeta a la legislación de un tercer país. ¿Qué debe comprobarse en primer lugar?

- a) Nada más, porque el alojamiento de los servidores en la Unión Europea resuelve por sí solo cualquier riesgo de transferencia.
- b) Si hay acceso a los datos desde el tercer país (soporte, administración, copias), porque es una transferencia internacional.
- c) Solo el precio ofertado, porque la legislación aplicable a la matriz del licitador no afecta al contrato del Ayuntamiento.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §5.1.2 (arts. 44-50 RGPD)

Que los servidores estén en la Unión no basta: el acceso remoto desde un tercer país es una transferencia internacional sometida al capítulo V del RGPD.

#### 4. Si ese tercer país es Estados Unidos y el proveedor carece de la certificación del Marco de Privacidad de Datos UE-EE. UU., ¿en qué puede apoyarse la transferencia?

- a) En la decisión de adecuación de 10 de julio de 2023, que ampara a cualquier empresa estadounidense.
- b) En el simple consentimiento del Ayuntamiento como responsable, sin necesidad de ninguna otra garantía.
- c) En cláusulas contractuales tipo, con la evaluación del marco jurídico del país de destino que exige Schrems II.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §5.1.2

La decisión de adecuación solo ampara a las empresas certificadas en el Marco; sin certificación, caben cláusulas contractuales tipo acompañadas de la evaluación del país de destino.

#### 5. ¿Qué posición jurídica ocupan el proveedor y el Ayuntamiento respecto de los datos personales del servicio?

- a) El proveedor pasa a ser responsable del tratamiento y el Ayuntamiento queda liberado de responsabilidad.
- b) El proveedor es encargado del tratamiento (art. 28 RGPD) y el Ayuntamiento sigue siendo responsable.
- c) Ambos son corresponsables a partes iguales, y el Ayuntamiento responde solo de la mitad de los datos.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §5.1.2

La responsabilidad se delega operativamente, pero no se externaliza: el Ayuntamiento sigue respondiendo como responsable del tratamiento.

#### 6. ¿Qué medida complementaria reduce de forma efectiva el riesgo de acceso desde el tercer país?

- a) Cifrar los datos con claves gestionadas exclusivamente por el Ayuntamiento.
- b) Cifrar los datos con claves gestionadas por la matriz del proveedor.
- c) Ampliar la lista de subencargados sin preaviso ni derecho de oposición.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §5.1.2

Si las claves solo las tiene el Ayuntamiento, el proveedor no puede entregar datos legibles; se completa con seudonimización, minimización y restricción geográfica del soporte.

#### 7. Al terminar el contrato, ¿qué debe ocurrir con los datos según el pliego?

- a) Conservarlos el proveedor durante cinco años, por si el Ayuntamiento necesitara consultarlos más tarde.
- b) Devolverlos o suprimirlos, a elección del responsable, incluidas las copias y con certificado de borrado.
- c) Suprimirlos el proveedor cuando estime oportuno, sin necesidad de acreditar el borrado al Ayuntamiento.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §5.1.2 (art. 28.3.g RGPD)

Es una obligación del encargado del tratamiento: al finalizar la prestación, devolver o suprimir los datos según elija el responsable.

#### 8. ¿Por qué debe exigirse en el pliego una prueba de reversión durante la vigencia del contrato?

- a) Porque el Reglamento de Datos obliga a cambiar de proveedor al menos una vez durante el contrato.
- b) Porque así el proveedor puede cobrar la tarifa de cambio antes de que dejen de estar permitidas.
- c) Porque es la única forma de comprobar que la salida funciona: un plan no probado no es un plan.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §2.4, §4.3.1

La reversión debe ensayarse al menos una vez mientras el contrato está vigente, junto con formatos abiertos, derecho de extracción y periodo de solapamiento.

#### 9. El contrato, de dos años prorrogable, seguirá vigente después del 12 de enero de 2027. ¿Qué podrá repercutir el proveedor a partir de esa fecha si el Ayuntamiento decide cambiar de proveedor?

- a) Ninguna tarifa de cambio, porque el Reglamento (UE) 2023/2854 las prohíbe por completo.
- b) Costes reducidos directamente vinculados al proceso de cambio, como hasta entonces.
- c) La tarifa de cambio que haya fijado libremente en su catálogo de precios vigente.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §5.1.2 (art. 29 Reglamento (UE) 2023/2854)

El Reglamento de Datos retira progresivamente las tarifas de cambio: hasta el 12 de enero de 2027 solo caben costes reducidos vinculados al cambio, y desde esa fecha quedan prohibidas.

#### 10. Para controlar el gasto del servicio de pago por uso, ¿qué mecanismo permite imputar el consumo a cada proyecto y unidad responsable?

- a) La contratación de instancias reservadas, que convierte todo el consumo en un precio fijo e indiviso.
- b) El etiquetado obligatorio de todos los recursos por proyecto y unidad, posible porque el servicio es medido.
- c) Un crédito fijo cerrado al inicio del contrato, que hace innecesario medir el consumo de cada unidad.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §2.4, §3.3.2

El crédito corresponde a un consumo estimado; el etiquetado lo hace imputable, junto con presupuestos y alertas con umbrales y cuotas por servicio. Las reservas solo reducen la parte variable.
