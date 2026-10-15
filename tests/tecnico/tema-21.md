# Test del tema 21. La arquitectura Java EE

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-21.html>

## Batería de preguntas

### 1. ¿Qué distingue fundamentalmente a Java EE de escribir una aplicación en Java SE «a pelo»?

- a) El contenedor gestiona el ciclo de vida y presta servicios transversales de forma declarativa (inversión de control)
- b) Java EE usa una sintaxis de lenguaje distinta a Java SE
- c) Java EE no permite usar clases de Java SE

**Respuesta correcta:** a) · **Referencia:** §1.1 [JAKARTA-PLAT]

El desarrollador describe qué necesita el componente; el contenedor lo crea, invoca sus métodos y le inyecta lo necesario.

### 2. En Java EE/Jakarta EE, ¿qué relación existe entre una especificación (p. ej. JAX-RS) y un servidor de aplicaciones como GlassFish o WildFly?

- a) El servidor de aplicaciones define la especificación y las bibliotecas la implementan
- b) La especificación define un contrato normativo; el servidor de aplicaciones es una implementación que debe superar un TCK para certificarse compatible
- c) No existe relación formal entre ambos conceptos

**Respuesta correcta:** b) · **Referencia:** §1.1 [JAKARTA-PLAT]

Es la misma separación especificación/implementación que en el Tema 19 distingue el estándar SQL de sus motores.

### 3. ¿En qué año nace la plataforma, bajo el nombre J2EE 1.2?

- a) 2006
- b) 2017
- c) 1999

**Respuesta correcta:** c) · **Referencia:** §1.2 [GONCALVES, cap. 1]

J2EE 1.2 es la primera versión de la plataforma, impulsada por Sun Microsystems.

### 4. ¿Qué cambio introduce Java EE 5 (2006) respecto a las versiones anteriores de J2EE?

- a) Sustituye buena parte de la configuración XML por anotaciones, simplificando el modelo de programación
- b) Introduce por primera vez el modelo de componentes EJB
- c) Elimina el contenedor de servlets

**Respuesta correcta:** a) · **Referencia:** §1.2 [GONCALVES, cap. 1]

Es uno de los tres hitos de la evolución de la plataforma.

### 5. ¿Cuál fue el motivo declarado por Oracle para transferir Java EE a la Eclipse Foundation en 2017?

- a) Reducir el coste de mantenimiento de la plataforma
- b) Acelerar la evolución de la plataforma fuera del proceso más lento del Java Community Process (JCP)
- c) Eliminar la plataforma por falta de uso

**Respuesta correcta:** b) · **Referencia:** §1.3 [JAKARTA-PLAT]

El proceso de especificación abierto de Eclipse (JESP) sustituye al JCP para esta plataforma.

### 6. ¿Por qué la plataforma se renombró de «Java EE» a «Jakarta EE» tras la transferencia a la Eclipse Foundation?

- a) Por decisión técnica de modernización de marca
- b) Por votación de la comunidad sin motivo legal
- c) Porque Oracle conservó la marca registrada «Java» y no autorizó su uso a la nueva gobernanza

**Respuesta correcta:** c) · **Referencia:** §1.3 [JAKARTA-PLAT]

Es la consecuencia legal directa de la retención de la marca, no una decisión técnica ni de marketing.

### 7. ¿Qué versión de la plataforma introduce el cambio de paquete javax.<em> a jakarta.</em> en todas las APIs?

- a) Jakarta EE 9
- b) Java EE 8
- c) Jakarta EE 11

**Respuesta correcta:** a) · **Referencia:** §1.3 [JAKARTA-PLAT]

Es la llamada «Gran Renombración» (Big Bang Renaming), de 2020.

### 8. El cambio de namespace javax.<em> a jakarta.</em> en Jakarta EE 9 es...

- a) Un cambio puramente cosmético, sin impacto en el código compilado
- b) Una ruptura binaria: el código compilado contra javax.<em> no es compatible en tiempo de ejecución con un contenedor que solo soporte jakarta.</em>
- c) Reversible automáticamente por el servidor de aplicaciones sin recompilar

**Respuesta correcta:** b) · **Referencia:** §1.3 [JAKARTA-PLAT]

* Las aplicaciones existentes requirieron una migración explícita, aunque las APIs se mantuvieron semánticamente casi idénticas.

### 9. En el modelo de seguridad JAAS/Jakarta Security, ¿qué pregunta responde la AUTORIZACIÓN?

- a) ¿Quién eres?
- b) ¿Cuánto tiempo dura tu sesión?
- c) ¿Qué puedes hacer, una vez identificado?

**Respuesta correcta:** c) · **Referencia:** §2.1.1 [JAKARTA-SEC]

La autenticación responde «¿quién eres?»; la autorización, «¿qué puedes hacer?», normalmente basándose en roles.

### 10. En el vocabulario JAAS, ¿qué representa un LoginModule?

- a) Un componente conectable que implementa un mecanismo concreto de autenticación (usuario/contraseña, certificado, LDAP…)
- b) El resultado final de una autenticación exitosa
- c) El registro de auditoría de accesos al sistema

**Respuesta correcta:** a) · **Referencia:** §2.1.1 [JAKARTA-SEC]

Sigue un patrón de complementos (<em>pluggable authentication</em>).

### 11. ¿Cómo se expresa habitualmente la autorización por rol sobre un recurso Jakarta EE (p. ej. un endpoint REST)?

- a) Comprobando el rol manualmente dentro del código de negocio en cada método
- b) De forma declarativa, con la anotación @RolesAllowed, interceptada por el contenedor antes de ejecutar el método
- c) No es posible declarar restricciones de rol a nivel de endpoint

**Respuesta correcta:** b) · **Referencia:** §2.1.1 [JAKARTA-SEC]

Es el contenedor, no el código de negocio, quien verifica el rol.

### 12. ¿Cómo resuelve JNDI la localización de un recurso como un DataSource?

- a) Por el tipo Java de la clase, igual que CDI
- b) Por la dirección IP del servidor de base de datos
- c) Por un nombre lógico jerárquico, independiente de la configuración física del recurso

**Respuesta correcta:** c) · **Referencia:** §2.1.2 [ORACLE-JNDI]

JNDI resuelve por nombre; CDI (§2.4.2), en cambio, resuelve por tipo.

### 13. ¿Qué ventaja principal aporta usar un nombre JNDI lógico (p. ej. jdbc/ExpedientesDS) en lugar de credenciales embebidas en el código?

- a) Permite cambiar de entorno (desarrollo→producción) reconfigurando el servidor, sin recompilar la aplicación
- b) Elimina por completo la necesidad de un pool de conexiones
- c) Sustituye a JPA como mecanismo de persistencia

**Respuesta correcta:** a) · **Referencia:** §2.1.2 [ORACLE-JNDI]

El nombre lógico desacopla el código de la configuración física del recurso.

### 14. En Apache Maven, ¿qué encadena el ciclo de vida estándar de construcción?

- a) Un grafo de tareas con caché incremental, sin fases fijas
- b) Una secuencia de fases fijas: validate → compile → test → package → verify → install → deploy
- c) Un único paso que compila y despliega simultáneamente

**Respuesta correcta:** b) · **Referencia:** §2.1.3 [MAVEN-DOC]

El grafo de tareas con caché incremental es, en cambio, el modelo de Gradle.

### 15. ¿Qué identifica de forma única una dependencia declarada en un pom.xml de Maven?

- a) Solo el nombre del archivo JAR
- b) La ruta absoluta en el disco del desarrollador
- c) La coordenada groupId:artifactId:version

**Respuesta correcta:** c) · **Referencia:** §2.1.3 [MAVEN-DOC]

Esa coordenada se resuelve automáticamente desde un repositorio (Maven Central o uno interno).

### 16. ¿Por qué la dependencia de la propia API Jakarta EE se declara con scope provided en Maven?

- a) Porque el servidor de aplicaciones ya proporciona esa API en tiempo de ejecución; empaquetarla también causaría conflictos de clases duplicadas
- b) Porque esa API no es necesaria para compilar el proyecto
- c) Porque Maven no permite declarar dependencias de la plataforma

**Respuesta correcta:** a) · **Referencia:** §2.1.3 [MAVEN-DOC]

La API se necesita para compilar, pero no para empaquetar dentro del artefacto final.

### 17. ¿Qué distingue a Gradle de Maven en su modelo de construcción?

- a) Gradle no admite gestión de dependencias transitivas
- b) Gradle usa un DSL programable (Groovy/Kotlin) y un motor de ejecución basado en un grafo de tareas con caché incremental
- c) Gradle solo puede usarse en proyectos Android, nunca en Java EE

**Respuesta correcta:** b) · **Referencia:** §2.1.3 [GRADLE-DOC]

Solo re-ejecuta las tareas cuyas entradas han cambiado.

### 18. ¿Qué contiene típicamente un archivo WAR (Web Archive)?

- a) Únicamente EJB de sesión
- b) Un conector JCA a un sistema externo
- c) Un módulo web: servlets, JSF, recursos estáticos y su descriptor de despliegue

**Respuesta correcta:** c) · **Referencia:** §2.1.4 [JAKARTA-SERVLET]

El descriptor <code>web.xml</code> es opcional desde que las anotaciones cubren la mayor parte de la configuración.

### 19. ¿Qué relación de contención es correcta entre los formatos de empaquetado Java EE?

- a) Un EAR puede contener varios WAR y EJB-JAR; un WAR no puede contener un EAR
- b) Un WAR puede contener varios EAR
- c) Un EJB-JAR y un EAR son formatos incompatibles entre sí

**Respuesta correcta:** a) · **Referencia:** §2.1.4 [JAKARTA-PLAT]

Es la jerarquía de empaquetado de la plataforma.

### 20. ¿Qué aísla el classloader hijo asignado a cada módulo dentro de un EAR desplegado?

- a) El acceso a la red del servidor
- b) Las dependencias de cada módulo, evitando colisiones aunque dos módulos usen versiones distintas de una misma biblioteca
- c) Las transacciones JTA de cada módulo

**Respuesta correcta:** b) · **Referencia:** §2.1.4 [JAKARTA-PLAT]

Cada WAR/EJB-JAR obtiene su propio classloader hijo del classloader de la aplicación.

### 21. ¿Qué diferencia fundamental hay entre la compilación JIT de la JVM tradicional y GraalVM Native Image?

- a) Ambas compilan en el mismo momento, solo cambia el formato del ejecutable
- b) JIT compila en tiempo de construcción; Native Image compila en tiempo de ejecución
- c) JIT compila de forma progresiva en tiempo de ejecución; Native Image compila por completo en tiempo de construcción (ahead-of-time)

**Respuesta correcta:** c) · **Referencia:** §2.1.5 [GRAALVM-DOC]

Es la distinción JIT/AOT central de este epígrafe.

### 22. ¿Qué ventaja aporta principalmente un ejecutable generado con GraalVM Native Image frente al arranque de una JVM tradicional?

- a) Arranque en milisegundos y huella de memoria de partida sensiblemente menor
- b) Mejor rendimiento sostenido tras horas de ejecución continua
- c) Elimina la necesidad de declarar reflexión o proxies dinámicos

**Respuesta correcta:** a) · **Referencia:** §2.1.5 [GRAALVM-DOC]

A cambio, un análisis estático más restrictivo: la reflexión y los proxies dinámicos deben declararse explícitamente.

### 23. ¿Cuál es la relación correcta entre GraalVM Native Image y Quarkus?

- a) Son sinónimos exactos del mismo producto
- b) GraalVM Native Image es una tecnología de compilación; Quarkus es un framework que la aprovecha (entre otras estrategias) para ofrecer aplicaciones nativas
- c) Quarkus sustituyó a GraalVM Native Image en 2020

**Respuesta correcta:** b) · **Referencia:** §2.1.5 [QUARKUS-DOC]

Quarkus también puede ejecutarse en modo JVM tradicional sin compilación nativa.

### 24. ¿Por qué Apache Tomcat, por sí solo, no se considera un servidor de aplicaciones Jakarta EE completo?

- a) Porque no puede ejecutar ningún componente Java
- b) Porque no permite desplegar aplicaciones web
- c) Porque implementa solo una parte de la especificación (servlets/JSF) pero le faltan EJB completo, JMS y JTA distribuido nativos

**Respuesta correcta:** c) · **Referencia:** §2.1.6 [WILDFLY-DOC]

TomEE añade esas piezas sobre Tomcat.

### 25. ¿Qué principio rige las dependencias entre las capas de una aplicación Java EE en capas (presentación/negocio/persistencia)?

- a) Cada capa solo depende de la inmediatamente inferior; la dependencia es unidireccional hacia abajo
- b) Cada capa puede invocar directamente a cualquier otra capa sin restricción
- c) La capa de persistencia conoce y depende de la capa de presentación

**Respuesta correcta:** a) · **Referencia:** §2.2 [FOWLER-EAA]

Este aislamiento permite sustituir una capa sin tocar las demás.

### 26. ¿Qué contenedores del servidor de aplicaciones gestionan típicamente, respectivamente, la capa de presentación y la capa de negocio implementada con EJB?

- a) Ambas capas comparten un único contenedor sin distinción
- b) El contenedor web gestiona la presentación (servlets/JSF/JAX-RS); el contenedor EJB gestiona la capa de negocio basada en Enterprise JavaBeans
- c) El contenedor de persistencia gestiona ambas capas

**Respuesta correcta:** b) · **Referencia:** §2.2 [GONCALVES, cap. 2]

Ambos contenedores conviven en el mismo servidor de aplicaciones y comparten servicios transversales.

### 27. ¿Cuántas instancias de un mismo servlet crea, por diseño, el contenedor web?

- a) Una instancia nueva por cada petición HTTP recibida
- b) Una instancia por cada usuario autenticado
- c) Una única instancia, que atiende todas las peticiones concurrentes en hilos distintos

**Respuesta correcta:** c) · **Referencia:** §2.3.1 [JAKARTA-SERVLET]

El contenedor despacha cada petición a un hilo distinto que invoca <code>service()</code>.

### 28. ¿Qué consecuencia práctica tiene que un servlet sea, por diseño, singleton?

- a) No debe guardar estado mutable de una petición en variables de instancia sin sincronización, por riesgo de errores de concurrencia
- b) No puede recibir peticiones POST
- c) Debe reiniciarse tras cada petición

**Respuesta correcta:** a) · **Referencia:** §2.3.1 [JAKARTA-SERVLET]

El estado por petición se guarda en <code>HttpServletRequest</code>; el estado por usuario, en <code>HttpSession</code>.

### 29. ¿Sobre qué componente del contenedor web se construye JavaServer Faces (JSF)?

- a) Sobre un contenedor EJB independiente
- b) Sobre el propio contenedor de servlets, mediante un único servlet especial (FacesServlet) que despacha todas las peticiones JSF
- c) JSF no depende de ningún componente del contenedor web

**Respuesta correcta:** b) · **Referencia:** §2.3.1 [JAKARTA-FACES]

JSF añade un ciclo de vida de petición en seis fases sobre ese modelo base.

### 30. Según la tesis de Roy Fielding (2000), ¿qué es REST?

- a) Un protocolo de mensajería con sobre XML normalizado
- b) Una implementación concreta de JAX-WS
- c) Un estilo arquitectónico que aprovecha las primitivas nativas de HTTP para operar sobre recursos identificados por URI

**Respuesta correcta:** c) · **Referencia:** §2.3.2 [FIELDING2000]

No es un protocolo cerrado, a diferencia de SOAP.

### 31. ¿Qué anotación de JAX-RS identifica la URI base de un recurso REST?

- a) @Path
- b) @WebService
- c) @Entity

**Respuesta correcta:** a) · **Referencia:** §2.3.2 [JAKARTA-REST]

<code>@WebService</code> pertenece a JAX-WS; <code>@Entity</code> pertenece a JPA.

### 32. ¿Qué caracteriza a SOAP frente a REST?

- a) SOAP no exige ningún formato de mensaje concreto
- b) SOAP es un protocolo que exige un sobre XML normalizado, habitualmente descrito por un contrato WSDL formal
- c) SOAP solo puede transportarse sobre FTP, nunca sobre HTTP

**Respuesta correcta:** b) · **Referencia:** §2.3.2 [SOAP12]

SOAP suele transportarse sobre HTTP, aunque no está ligado exclusivamente a él.

### 33. ¿Qué documento describe formalmente el contrato de un servicio SOAP (operaciones, mensajes, tipos, endpoint)?

- a) OpenAPI
- b) UDDI
- c) WSDL

**Respuesta correcta:** c) · **Referencia:** §2.3.3 [WSDL20]

OpenAPI cumple ese papel para REST; UDDI es el registro de descubrimiento, no el contrato.

### 34. ¿Qué papel cumple UDDI en el ecosistema de servicios web SOAP?

- a) Un registro centralizado donde publicar y descubrir servicios, análogo a unas «páginas amarillas» de servicios web
- b) El lenguaje de descripción del contrato de un servicio SOAP
- c) El framework de implementación de servicios REST equivalente a JAX-RS

**Respuesta correcta:** a) · **Referencia:** §2.3.3 [UDDI3]

Tuvo una adopción muy limitada fuera de grandes integraciones corporativas.

### 35. ¿Qué caracteriza a un Stateless Session Bean?

- a) Mantiene una instancia dedicada por cada cliente durante toda la conversación
- b) No mantiene estado conversacional entre invocaciones; el contenedor gestiona un pool de instancias intercambiables
- c) Es la única instancia compartida por toda la aplicación

**Respuesta correcta:** b) · **Referencia:** §2.4.1 [JAKARTA-EJB]

Es la variante más escalable y la más habitual en la capa de negocio.

### 36. ¿Qué tipo de EJB es el adecuado para un asistente web de varios pasos que debe recordar los datos introducidos en pasos anteriores?

- a) Stateless
- b) Singleton
- c) Stateful

**Respuesta correcta:** c) · **Referencia:** §2.4.1 [JAKARTA-EJB]

El contenedor asocia una instancia dedicada a cada cliente durante toda la conversación.

### 37. ¿Qué ocurrió con las Entity Beans, el modelo histórico de persistencia gestionado por el contenedor EJB?

- a) Fueron sustituidas por completo por JPA desde Java EE 5 (2006), por su complejidad y rendimiento deficiente
- b) Siguen siendo el estándar vigente de persistencia en Jakarta EE
- c) Se fusionaron con los Message-Driven Beans

**Respuesta correcta:** a) · **Referencia:** §2.4.1 [JAKARTA-EJB]

Mencionarlas como forma actual de persistencia es un error frecuente.

### 38. ¿Cómo resuelve CDI qué implementación inyectar con @Inject?

- a) Por el nombre JNDI del recurso
- b) Por el tipo Java declarado (con qualifiers para desambiguar si hay varias implementaciones)
- c) Por el orden alfabético de las clases candidatas

**Respuesta correcta:** b) · **Referencia:** §2.4.2 [JAKARTA-CDI]

JNDI, en cambio, resuelve por nombre.

### 39. ¿Cuánto dura la instancia de un bean CDI anotado con @RequestScoped?

- a) Toda la sesión del usuario
- b) Toda la vida de la aplicación
- c) Una única petición HTTP; se crea una nueva instancia en cada petición

**Respuesta correcta:** c) · **Referencia:** §2.4.2 [JAKARTA-CDI]

<code>@SessionScoped</code> dura la sesión; <code>@ApplicationScoped</code>, toda la aplicación.

### 40. ¿A qué patrón de diseño del Tema 20 equivale, en esencia, un bean CDI @ApplicationScoped?

- a) Singleton, gestionado automáticamente por el contenedor en lugar de codificado a mano
- b) Factory Method
- c) Adapter

**Respuesta correcta:** a) · **Referencia:** §2.4.2 [JAKARTA-CDI]

Una única instancia compartida por toda la aplicación.

### 41. ¿Qué tres componentes intercambiables sigue habitualmente un step de Jakarta Batch en el patrón ETL?

- a) Controller, Service, Repository
- b) ItemReader, ItemProcessor, ItemWriter
- c) Producer, Consumer, Broker

**Respuesta correcta:** b) · **Referencia:** §2.4.3 [JAKARTA-BATCH]

Leen, transforman/validan y escriben los elementos, agrupados en fragmentos (chunks).

### 42. ¿En qué momento confirma la transacción el procesamiento por fragmentos (chunk-oriented) de Jakarta Batch?

- a) Solo al finalizar todo el job completo, nunca antes
- b) Nunca; Jakarta Batch no usa transacciones
- c) Por cada fragmento (chunk) procesado, lo que permite reiniciar desde el último fragmento confirmado si el job falla

**Respuesta correcta:** c) · **Referencia:** §2.4.3 [JAKARTA-BATCH]

Un fallo en el fragmento 500 de 1.000 no obliga a reprocesar los 499 anteriores.

### 43. En JMS, ¿qué modelo de mensajería garantiza que cada mensaje lo consuma un único receptor, aunque haya varios consumidores escuchando?

- a) Punto a punto, sobre una Queue
- b) Publicación/suscripción, sobre un Topic
- c) Difusión (broadcast) sin destino definido

**Respuesta correcta:** a) · **Referencia:** §2.5.1 [JAKARTA-MSG]

Varios consumidores se reparten los mensajes, no los duplican.

### 44. ¿Qué modelo JMS es el adecuado para notificar un mismo suceso a varios sistemas interesados de forma independiente?

- a) Punto a punto, sobre una Queue
- b) Publicación/suscripción, sobre un Topic
- c) Solicitud-respuesta síncrona

**Respuesta correcta:** b) · **Referencia:** §2.5.1 [JAKARTA-MSG]

Todos los suscriptores activos en el momento del envío reciben el mensaje.

### 45. ¿Qué defensa estándar frente a la inyección SQL ofrece el uso de PreparedStatement con parámetros en JDBC?

- a) Cifra automáticamente la conexión con la base de datos
- b) Elimina la necesidad de un pool de conexiones
- c) Separa el código SQL fijo, precompilado, de los datos (parámetros), de modo que un valor de entrada no puede alterar la estructura de la sentencia

**Respuesta correcta:** c) · **Referencia:** §2.5.2 [ORACLE-JNDI]

Conecta con el SQL dinámico frente a estático del Tema 19.

### 46. ¿Qué gestiona un DataSource localizado por JNDI en una aplicación Java EE?

- a) Un pool de conexiones físicas ya abiertas y reutilizables, evitando el coste de abrir una conexión TCP nueva en cada operación
- b) La sintaxis JPQL de las consultas
- c) El renderizado de la vista JSF

**Respuesta correcta:** a) · **Referencia:** §2.5.2 [ORACLE-JNDI]

La conexión no se abre directamente con credenciales embebidas en el código.

### 47. ¿Qué protocolo implementa el coordinador de transacciones de JTA para garantizar ACID en transacciones que abarcan varios recursos?

- a) Two-Way Handshake
- b) Commit en dos fases (Two-Phase Commit, 2PC): fase de preparación y fase de confirmación/deshecho
- c) Round-robin de confirmaciones

**Respuesta correcta:** b) · **Referencia:** §2.5.3 [JAKARTA-JTA]

Si algún recurso no está listo, se ordena el rollback a todos.

### 48. ¿Qué diferencia CMT de BMT en la gestión transaccional de un EJB?

- a) CMT solo funciona con bases de datos NoSQL
- b) BMT es el modelo por defecto y el más habitual
- c) En CMT el contenedor gestiona la transacción de forma declarativa (atributos); en BMT el propio componente la controla explícitamente mediante programación

**Respuesta correcta:** c) · **Referencia:** §2.5.3 [JAKARTA-JTA]

CMT es el modelo por defecto, no BMT.

### 49. ¿Qué hace el atributo transaccional REQUIRED (por defecto en CMT) si el método se invoca sin ninguna transacción activa?

- a) Crea una nueva transacción
- b) Lanza una excepción obligatoriamente
- c) Ejecuta el método sin ninguna transacción

**Respuesta correcta:** a) · **Referencia:** §2.5.3 [JAKARTA-JTA]

Si ya existe una transacción activa, <code>REQUIRED</code> se une a ella en lugar de crear una nueva.

### 50. ¿Qué mecanismo de JPA detecta automáticamente los cambios realizados sobre una entidad gestionada, sin invocar explícitamente un UPDATE?

- a) JNDI lookup
- b) El dirty checking del contexto de persistencia del EntityManager
- c) El pool de conexiones JDBC

**Respuesta correcta:** b) · **Referencia:** §2.5.4 [JAKARTA-JPA]

Los cambios se sincronizan con la base de datos al confirmar la transacción.

### 51. ¿Sobre qué opera JPQL, a diferencia de SQL?

- a) Sobre las tablas y columnas físicas de la base de datos
- b) Sobre los ficheros de configuración XML del servidor
- c) Sobre el modelo de entidades y sus atributos Java, no directamente sobre tablas y columnas físicas

**Respuesta correcta:** c) · **Referencia:** §2.5.4 [JAKARTA-JPA]

El proveedor JPA lo traduce internamente a SQL.

### 52. ¿Qué es JCache (JSR 107)?

- a) Una especificación transversal de caché en memoria, aplicable tanto dentro como fuera de Jakarta EE
- b) Un sinónimo del contexto de persistencia de primer nivel de JPA
- c) Un tipo de EJB especializado en almacenamiento temporal

**Respuesta correcta:** a) · **Referencia:** §2.5.5 [JAKARTA-CACHE]

No debe confundirse con el contexto de persistencia de JPA, que es una caché de primer nivel implícita y limitada a la transacción.

### 53. ¿Qué diferencia principal hay entre una herramienta APM y una prueba de carga?

- a) Ambas se ejecutan siempre en el mismo momento del ciclo de vida
- b) El APM monitoriza el sistema en producción de forma continua; la prueba de carga se ejecuta de forma puntual, antes del despliegue
- c) La prueba de carga sustituye por completo al APM en producción

**Respuesta correcta:** b) · **Referencia:** §3.1 [ISO25010]

Son complementarios, no sustitutos.

### 54. ¿Qué papel cumple JUnit en las pruebas de una aplicación Java EE?

- a) Simula miles de usuarios concurrentes contra el sistema
- b) Crea dobles de prueba (mocks) de las dependencias
- c) Ejecuta y organiza las pruebas: aserciones y ciclo de vida (@BeforeEach/@AfterEach)

**Respuesta correcta:** c) · **Referencia:** §3.2 [JUNIT5-DOC]

Simular usuarios concurrentes es tarea de JMeter; crear mocks, de Mockito.

### 55. ¿Qué problema resuelve Mockito al probar la lógica de negocio de un EJB o CDI bean?

- a) Permite simular el comportamiento de sus dependencias reales (otro servicio, un EntityManager) sin ejecutarlas de verdad
- b) Sustituye por completo a JUnit como framework de ejecución de pruebas
- c) Genera automáticamente pruebas de carga con JMeter

**Respuesta correcta:** a) · **Referencia:** §3.2 [MOCKITO-DOC]

Así la prueba se mantiene aislada, rápida y no frágil frente a recursos externos.

### 56. ¿Qué tipo de prueba con JMeter busca encontrar el punto de ruptura del sistema, más allá de la capacidad prevista?

- a) Prueba de resistencia (soak testing)
- b) Prueba de estrés (stress testing)
- c) Prueba unitaria

**Respuesta correcta:** b) · **Referencia:** §3.3 [JMETER-DOC]

La prueba de resistencia usa carga moderada sostenida en el tiempo; la unitaria no es una prueba de carga.

### 57. ¿Cuál es la relación correcta entre Spring Framework y Jakarta EE?

- a) Spring es la implementación de referencia oficial de Jakarta EE
- b) Spring solo puede ejecutarse dentro de un servidor de aplicaciones Jakarta EE completo
- c) Spring es un framework alternativo e independiente, aunque puede interoperar con especificaciones concretas como JPA

**Respuesta correcta:** c) · **Referencia:** §3.4.1 [SPRING-DOC]

Nace en 2003 como respuesta a la complejidad de EJB 2.x.

### 58. ¿Sobre qué estándares se construye explícitamente Quarkus, a diferencia de Spring?

- a) Estándares Jakarta EE/MicroProfile: CDI, JAX-RS, JPA
- b) Un modelo de inyección de dependencias propio, sin relación con CDI
- c) Únicamente sobre JDBC, sin soporte de inyección de dependencias

**Respuesta correcta:** a) · **Referencia:** §3.4.2 [QUARKUS-DOC]

A diferencia de Spring, que es histórica e independiente de la plataforma estándar.

### 59. ¿Qué aporta MicroProfile sobre el subconjunto de especificaciones Jakarta EE que utiliza (CDI, JAX-RS, JSON-P)?

- a) Sustituye por completo a Jakarta EE como plataforma independiente sin relación con ella
- b) Extensiones específicas de microservicios no cubiertas por la plataforma tradicional: tolerancia a fallos, configuración externa, métricas y health checks
- c) Un nuevo lenguaje de programación distinto de Java

**Respuesta correcta:** b) · **Referencia:** §4 [QUARKUS-DOC]

Se apoya en CDI/JAX-RS/JSON-P, no los sustituye.

### 60. ¿Qué relación tienen las tendencias actuales (cloud-native, MicroProfile, programación reactiva) con los fundamentos arquitectónicos de este tema?

- a) Sustituyen por completo el modelo de contenedor y la arquitectura de capas
- b) No tienen ninguna relación con la plataforma Jakarta EE tradicional
- c) Amplían el contexto de despliegue sin sustituir los fundamentos: el modelo de contenedor, la arquitectura de capas y los componentes constitutivos siguen siendo la base

**Respuesta correcta:** c) · **Referencia:** §4 [JAKARTA-PLAT]

Tanto un servidor Jakarta EE tradicional como un microservicio Quarkus en Kubernetes comparten esa misma base conceptual.

## Preguntas sobre los casos prácticos

### Caso 1. API REST segura de consulta y liquidación de tributos

#### 1. En el supuesto planteado, ¿qué anotación expone la clase TributoResource como recurso REST en la ruta /tributos?

- a) @Path("/tributos") sobre la clase.
- b) @Produces("/tributos") sobre la clase.
- c) @WebServlet("/tributos") sobre la clase.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.3.2

En JAX-RS, @Path identifica la URI del recurso; @Produces fija el formato de respuesta y @WebServlet declara un servlet, no un recurso REST.

#### 2. El método consultar debe atender GET /tributos/{id}. ¿Cómo recibe el identificador que viene en la URI?

- a) Con @Consumes(MediaType.APPLICATION_JSON) aplicada al parámetro Long id.
- b) Con @Path("/{id}") en el método y el parámetro anotado con @PathParam("id").
- c) Leyéndolo de la sesión HTTP del usuario, donde lo deja el navegador.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.3.2

La plantilla {id} se declara con @Path en el método y su valor se inyecta en el parámetro anotado con @PathParam("id").

#### 3. ¿Qué anotación indica que consultar devuelve la respuesta en formato JSON?

- a) @Consumes(MediaType.APPLICATION_JSON).
- b) @WebMethod, propia de los servicios web.
- c) @Produces(MediaType.APPLICATION_JSON).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.3.2

@Produces declara el formato de lo que el método devuelve; @Consumes, el del cuerpo que recibe; @WebMethod pertenece a JAX-WS (SOAP).

#### 4. Si el tributo solicitado no existe, ¿qué respuesta debe devolver el recurso REST?

- a) Un 200 OK con el cuerpo vacío, para no generar errores en el cliente.
- b) Un 404 NOT_FOUND, construido con Response.status(Response.Status.NOT_FOUND).
- c) Un 201 CREATED, porque la consulta deja el tributo registrado en el sistema.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.3.2

REST aprovecha los códigos de estado de HTTP: si el recurso buscado no existe, la respuesta es NOT_FOUND (404); 201 corresponde a la creación de un recurso.

#### 5. Solo el rol GESTOR_TRIBUTARIO puede invocar el método liquidar. ¿Cómo se expresa esa restricción?

- a) Con la anotación @RolesAllowed("GESTOR_TRIBUTARIO") sobre el método liquidar.
- b) Con un if al comienzo de liquidar que compruebe a mano el rol del usuario.
- c) Con @Path("/gestor") en el método, para que solo los gestores lo encuentren.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §2.1.1

En Java EE la autorización se expresa de forma declarativa con @RolesAllowed, no comprobando roles a mano dentro del método.

#### 6. Con @RolesAllowed, ¿quién comprueba el rol del usuario y en qué momento?

- a) La base de datos, mediante los permisos GRANT concedidos sobre la tabla TRIBUTO.
- b) El propio método liquidar, una vez ejecutado, antes de devolver la respuesta.
- c) El contenedor, que intercepta la llamada y verifica el rol antes de ejecutar el método.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.1.1

Es el contenedor quien intercepta la llamada y verifica el rol antes de ejecutar el código del método.

#### 7. Un ciudadano identificado en la sede electrónica, sin el rol de gestor, intenta liquidar un tributo y se le deniega. ¿Qué control de seguridad lo ha impedido?

- a) La autorización: se sabe quién es, pero no tiene permiso para esa acción.
- b) La autenticación: el sistema no ha podido verificar quién es el usuario.
- c) La transacción: el atributo REQUIRED rechaza a los usuarios sin rol.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §2.1.1

Autenticación responde a «¿quién eres?» y autorización a «¿qué puedes hacer?»; el ciudadano está autenticado, pero carece del rol que exige la operación.

#### 8. ¿Cómo debe obtener el recurso REST el EJB LiquidacionTributoService para delegar en él la liquidación?

- a) Creándolo con new LiquidacionTributoService() dentro del método liquidar.
- b) Copiando en el recurso el código de cálculo que ya contiene el EJB.
- c) Inyectándolo con @Inject en un atributo y llamando a sus métodos.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §2.4.2

El contenedor crea los componentes y les inyecta lo que necesitan; con @Inject el recurso recibe el EJB de negocio y solo delega en él.

#### 9. ¿Por qué el cálculo de la liquidación no debe programarse dentro del propio recurso REST?

- a) Porque JAX-RS no admite métodos que hagan cálculos con importes decimales.
- b) Porque el recurso pertenece a la capa de presentación, que solo llama a la capa de negocio.
- c) Porque un recurso REST no puede acceder a datos si no es a través de JMS.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §2.2

En la arquitectura de capas la presentación llama a la lógica de negocio, que a su vez usa la persistencia; así se puede sustituir una capa sin tocar las demás.

#### 10. El método liquidar() del EJB debe ejecutarse siempre dentro de una transacción, uniéndose a la existente si la hay. ¿Qué atributo @TransactionAttribute corresponde?

- a) REQUIRED.
- b) REQUIRES_NEW.
- c) SUPPORTS.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §2.5.3

REQUIRED se une a la transacción del llamador y, si no hay ninguna, crea una nueva. REQUIRES_NEW nunca se une y SUPPORTS puede ejecutarse sin transacción.

### Caso 2. Asistente multipaso de alta de expediente

#### 1. En el supuesto planteado, ¿qué tipo de Session Bean debe gestionar el estado del asistente entre los tres pasos?

- a) Stateless.
- b) Singleton.
- c) Stateful.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §2.4.1

Stateful mantiene un estado conversacional propio de cada cliente durante varias invocaciones, como los pasos de un asistente.

#### 2. ¿Por qué un Session Bean Singleton no sirve para este asistente?

- a) Porque es una única instancia para toda la aplicación y mezclaría los datos de usuarios distintos.
- b) Porque un Singleton no puede declarar atributos donde guardar los datos de cada paso.
- c) Porque un Singleton solo se activa cuando llega un mensaje a una cola JMS.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §2.4.1

El Singleton es una única instancia compartida por toda la aplicación: los datos del asistente de un ciudadano quedarían mezclados con los de otros.

#### 3. ¿Y por qué tampoco sirve un Session Bean Stateless?

- a) Porque un bean Stateless no puede acceder a la base de datos para persistir el expediente.
- b) Porque no guarda estado entre invocaciones y cualquier instancia del pool atiende cada llamada.
- c) Porque un bean Stateless es más lento que el Stateful al tramitar los formularios web.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §2.4.1

Stateless no mantiene estado conversacional; sus instancias son intercambiables, así que no recordaría los datos de los pasos anteriores.

#### 4. Si el asistente se implementa en JSF con un bean CDI, ¿qué ámbito es el más adecuado para el flujo de tres pasos?

- a) @ConversationScoped.
- b) @RequestScoped.
- c) @SessionScoped.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §2.4.2

@ConversationScoped vive durante una conversación definida explícitamente por el desarrollador, pensada para flujos multipaso en JSF.

#### 5. ¿Qué ocurriría si el bean del asistente fuera @RequestScoped?

- a) Que los datos del asistente se compartirían con todos los usuarios de la aplicación.
- b) Que los datos se conservarían hasta que el usuario cerrara su sesión en la sede.
- c) Que los datos se perderían entre pasos, porque cada paso es una petición distinta.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §2.4.2

Un bean @RequestScoped vive una única petición HTTP y se crea de nuevo en cada una; al pasar al paso siguiente, lo introducido se habría perdido.

#### 6. ¿Qué inconveniente tendría usar @SessionScoped para el asistente?

- a) Que perdería los datos al pasar de un paso al siguiente del asistente.
- b) Que viviría toda la sesión del usuario, aunque abandone el asistente sin terminar.
- c) Que una única instancia sería compartida por todos los usuarios conectados.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §2.4.2

@SessionScoped dura toda la sesión HTTP del usuario: el estado del asistente sobreviviría más allá del flujo, aunque este se abandone.

#### 7. El bean del asistente declara @Inject private ExpedienteService service. ¿Cómo decide CDI qué objeto inyectar?

- a) Por un nombre JNDI escrito como cadena de texto en la propia anotación.
- b) Por el nombre del atributo, que debe coincidir con el nombre del servicio.
- c) Por el tipo declarado del atributo, ExpedienteService, sin usar nombres.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §2.4.2

CDI resuelve la inyección por el tipo Java declarado; JNDI, en cambio, localiza los recursos por nombre.

#### 8. Si existieran dos implementaciones de ExpedienteService, ¿cómo se indicaría a CDI cuál inyectar?

- a) No hace falta: CDI elige la primera implementación que encuentra por orden alfabético.
- b) Con un qualifier que desambigüe entre las implementaciones de ese mismo tipo.
- c) Solo es posible sustituyendo @Inject por una búsqueda JNDI con InitialContext.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §2.4.2

CDI resuelve por tipo y, si hay varias implementaciones del mismo tipo, se desambigua mediante qualifiers.

#### 9. Al confirmar el alta hay que avisar a dos sistemas municipales independientes sin acoplar el asistente a ninguno. ¿Qué mecanismo de JMS se usa?

- a) Un Topic (publicación/suscripción), que entrega cada mensaje a todos los suscriptores.
- b) Una Queue (punto a punto), que entrega cada mensaje a un único consumidor.
- c) Una llamada REST síncrona a cada sistema desde el método confirmar.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §2.5.1

En un Topic cada mensaje lo reciben todos los suscriptores activos: es el modelo natural para notificar un suceso a varios interesados independientes.

#### 10. ¿Qué componente de negocio consume el mensaje en cada sistema suscrito?

- a) Un Stateful Session Bean que consulta el tema JMS en un bucle de sondeo.
- b) Un servlet cuyo método doGet() recibe el mensaje publicado en el tema.
- c) Un Message-Driven Bean, cuyo onMessage() invoca el contenedor al llegar el mensaje.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §2.4.1 y §2.5.1

El Message-Driven Bean se invoca de forma asíncrona cuando llega un mensaje a la cola o tema al que está suscrito, sin programar un bucle de sondeo.

### Caso 3. Persistencia, transacciones y caché de catálogo

#### 1. En el supuesto planteado, ¿qué anotaciones convierten la clase Tributo en una entidad JPA asociada a la tabla TRIBUTO?

- a) @Stateless y @Table(name = "TRIBUTO").
- b) @Entity y @Table(name = "TRIBUTO").
- c) @Path("/tributo") y @Entity.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §2.5.4

@Entity marca la clase como entidad JPA y @Table fija la tabla a la que se mapea; @Stateless es un EJB y @Path, un recurso REST.

#### 2. ¿Cómo se declara que idTributo es la clave primaria y que su valor lo genera la base de datos?

- a) Con @Id y @JoinColumn(name = "idTributo") sobre el atributo.
- b) Con @ManyToOne sobre el atributo idTributo de la entidad.
- c) Con @Id y @GeneratedValue(strategy = GenerationType.IDENTITY).

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §2.5.4

@Id marca la clave primaria y @GeneratedValue con la estrategia IDENTITY la deja autogenerada (autonumérica).

#### 3. Cada tributo pertenece a un contribuyente y un contribuyente puede tener muchos tributos. ¿Cómo se mapea en la entidad Tributo?

- a) Con @ManyToOne y @JoinColumn(name = "dni_contribuyente") sobre el atributo contribuyente.
- b) Con @Inject sobre el atributo contribuyente, para que el contenedor lo resuelva por tipo.
- c) Con @Table(name = "CONTRIBUYENTE") sobre el atributo contribuyente de la entidad.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §2.5.4

@ManyToOne expresa que muchos tributos apuntan a un contribuyente, y @JoinColumn indica la columna de la clave foránea (dni_contribuyente).

#### 4. ¿Cuál es la consulta JPQL correcta para obtener los tributos de importe superior a un parámetro?

- a) SELECT * FROM TRIBUTO WHERE importe > :minimo
- b) SELECT t FROM Tributo t WHERE t.importe > :minimo
- c) SELECT importe FROM TRIBUTO WHERE importe > ? con PreparedStatement

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §2.5.4

JPQL se escribe sobre la entidad (Tributo) y sus atributos (t.importe), con parámetros con nombre (:minimo); las otras dos opciones son SQL sobre la tabla física.

#### 5. ¿Qué diferencia a JPQL del SQL que se escribe directamente contra la base de datos?

- a) Que JPQL se ejecuta en memoria, sin llegar a consultar la base de datos.
- b) Que JPQL solo funciona con un motor de base de datos concreto.
- c) Que JPQL opera sobre entidades y atributos, y el proveedor lo traduce a SQL.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §2.5.4

JPQL opera sobre el modelo de entidades, no sobre tablas y columnas físicas; el proveedor JPA lo traduce internamente a SQL.

#### 6. La entrada de auditoría debe confirmarse aunque la liquidación acabe haciendo rollback. ¿Qué atributo debe llevar el método registrar de AuditoriaService?

- a) REQUIRES_NEW.
- b) REQUIRED.
- c) MANDATORY.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §2.5.3

REQUIRES_NEW suspende la transacción del llamador y crea siempre una nueva e independiente, que se confirma por su cuenta.

#### 7. Si registrar se dejara con el atributo por defecto REQUIRED y la liquidación hiciera rollback, ¿qué pasaría con la entrada de auditoría?

- a) Se confirmaría igualmente, porque cada método de un EJB tiene su propio COMMIT.
- b) Se desharía también, porque se habría unido a la transacción de la liquidación.
- c) No llegaría a grabarse, porque REQUIRED exige que no exista transacción activa.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §2.5.3

REQUIRED se une a la transacción del llamador: si esa transacción se deshace, se deshace con ella todo lo hecho dentro, auditoría incluida.

#### 8. Durante la liquidación, el servicio recupera un Tributo con em.find() y le cambia el importe. ¿Hace falta lanzar un UPDATE?

- a) No: el contexto de persistencia detecta el cambio y genera el UPDATE al confirmar la transacción.
- b) Sí: hay que invocar siempre em.merge() para que JPA guarde la entidad modificada.
- c) Sí: JPA solo lee entidades y las modificaciones requieren un PreparedStatement.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §2.5.4

Las entidades gestionadas por el EntityManager se vigilan (dirty checking): sus cambios se sincronizan con la base de datos al confirmar la transacción.

#### 9. ¿Por qué el catálogo DISTRITO es un buen candidato para JCache?

- a) Porque cambia en cada petición y conviene tenerlo siempre recalculado en memoria.
- b) Porque JCache sustituye a la base de datos como almacén definitivo del catálogo.
- c) Porque es de solo lectura y cambia muy poco: se evita repetir la misma consulta.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §2.5.5

Una caché evita accesos repetidos a un recurso costoso; un catálogo de solo lectura y poco cambiante es el caso ideal.

#### 10. ¿Qué riesgo introduce cachear DISTRITO y cómo se mitiga?

- a) Que se pierden las propiedades ACID; se mitiga con commit en dos fases.
- b) Servir datos obsoletos; se mitiga con expiración o invalidación explícita.
- c) Que se abre la puerta a la inyección SQL; se mitiga con PreparedStatement.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §2.5.5

Toda caché arriesga servir datos obsoletos (stale) si la fuente cambia; por eso las políticas de expiración y de invalidación explícita son tan importantes como la propia caché.
