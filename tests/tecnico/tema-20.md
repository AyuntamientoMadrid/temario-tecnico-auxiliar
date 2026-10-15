# Test del tema 20. Diseño y programación orientada a objetos

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-20.html>

## Batería de preguntas

### 1. ¿Qué teorema demuestra que cualquier algoritmo puede expresarse combinando secuencia, selección e iteración, marcando la transición hacia la programación estructurada?

- a) Teorema de Böhm-Jacopini
- b) Teorema de Church-Turing
- c) Teorema de Codd

**Respuesta correcta:** a) · **Referencia:** §1.1 [BOOCH07]

Este teorema (1966) demuestra que cualquier programa puede escribirse con solo tres estructuras de control, fundamento de la programación estructurada que precede históricamente a la POO.

### 2. ¿Qué lenguaje se considera el primero en introducir el concepto de clases y objetos, orientado a la simulación de sistemas?

- a) Smalltalk
- b) Simula 67
- c) C++

**Respuesta correcta:** b) · **Referencia:** §1.1 [BOOCH07]

Dahl y Nygaard lo crearon en 1967 para simular sistemas complejos; introduce por primera vez clases y objetos, raíz histórica del paradigma OO.

### 3. ¿Qué lenguaje populariza el término "orientado a objetos" y el envío de mensajes como mecanismo de interacción entre objetos?

- a) Java
- b) Simula 67
- c) Smalltalk

**Respuesta correcta:** c) · **Referencia:** §1.1 [BOOCH07]

Desarrollado en Xerox PARC en los años 70, consolida el vocabulario y la filosofía de la POO —incluido el envío de mensajes— antes de que C++ y Java la popularizasen en la industria.

### 4. ¿Qué pilar de la POO responde a la pregunta "qué hace un objeto", materializándose en su interfaz pública?

- a) Abstracción
- b) Encapsulamiento
- c) Herencia

**Respuesta correcta:** a) · **Referencia:** §1.2 [MEYER97]

Identifica las características esenciales de una entidad ignorando detalles irrelevantes, y se expresa en el conjunto de operaciones que el objeto ofrece al exterior.

### 5. ¿Qué mecanismo oculta el estado interno de un objeto y restringe el acceso a él a través de una interfaz controlada?

- a) Polimorfismo
- b) Encapsulamiento
- c) Modularidad

**Respuesta correcta:** b) · **Referencia:** §1.2 [MEYER97]

Protege los invariantes del objeto y permite cambiar la implementación interna sin romper el código cliente, siempre que la interfaz pública se mantenga.

### 6. Una clase cuyos atributos y métodos están fuertemente relacionados entre sí, contribuyendo todos a una única responsabilidad, tiene:

- a) Alto acoplamiento
- b) Baja cohesión
- c) Alta cohesión

**Respuesta correcta:** c) · **Referencia:** §1.3 [SOMMERVILLE16]

El objetivo de diseño es alta cohesión combinada con bajo acoplamiento entre clases distintas.

### 7. ¿Qué principio SOLID establece que una clase debe tener una única razón para cambiar?

- a) Single Responsibility
- b) Open/Closed
- c) Liskov Substitution

**Respuesta correcta:** a) · **Referencia:** §1.4 [MARTIN03]

Si una clase acumula más de una responsabilidad, tiene más de una razón para cambiar y debería dividirse.

### 8. El principio de sustitución de Liskov exige que:

- a) Una clase dependa siempre de implementaciones concretas
- b) Un objeto de una subclase pueda sustituir a uno de la superclase sin alterar la corrección del programa
- c) Una interfaz agrupe todos los métodos posibles de un dominio

**Respuesta correcta:** b) · **Referencia:** §1.4 [LISKOV94]

Formulado por Liskov y Wing (1994); si una subclase devuelve valores o lanza excepciones no esperadas por el código que trata con la superclase, se viola LSP.

### 9. La plantilla que define atributos y métodos comunes a un conjunto de entidades se denomina:

- a) Objeto
- b) Instancia
- c) Clase

**Respuesta correcta:** c) · **Referencia:** §2.1 [BOOCH07]

Una clase no ocupa memoria de datos en tiempo de ejecución; es una definición. Un objeto, instancia concreta de una clase, sí.

### 10. ¿Qué mecanismo libera automáticamente la memoria de un objeto en Java cuando ya no existe ninguna referencia alcanzable a él?

- a) El recolector de basura (garbage collector)
- b) El destructor explícito
- c) El operador delete

**Respuesta correcta:** a) · **Referencia:** §2.1 [GOSLING-JLS]

A diferencia de C++, Java gestiona automáticamente la destrucción de objetos; el programador no invoca <code>delete</code>.

### 11. Un atributo declarado como <code>static</code> en Java:

- a) Tiene una copia distinta por cada objeto de la clase
- b) Tiene una única copia compartida por todos los objetos de la clase
- c) Solo existe dentro de un método

**Respuesta correcta:** b) · **Referencia:** §2.2 [GOSLING-JLS]

Se accede sin instancia, con el nombre de la clase (p. ej. <code>Expediente.getTotalAbiertos()</code>).

### 12. El constructor de una clase en Java se caracteriza por:

- a) Ser siempre estático
- b) Ejecutarse solo una vez para toda la clase
- c) Tener el mismo nombre que la clase y no declarar tipo de retorno

**Respuesta correcta:** c) · **Referencia:** §2.2 [GOSLING-JLS]

Se invoca automáticamente al crear un objeto con <code>new</code>, y su responsabilidad es dejarlo en un estado inicial válido.

### 13. Un atributo <code>private</code> de una clase Java es accesible desde:

- a) Únicamente la propia clase
- b) Cualquier clase del mismo paquete
- c) Cualquier subclase, esté o no en el mismo paquete

**Respuesta correcta:** a) · **Referencia:** §2.3 [GOSLING-JLS]

Es el nivel de visibilidad más restrictivo de los cuatro que define Java.

### 14. Un método <code>protected</code> es visible desde:

- a) Solo la propia clase
- b) La propia clase, el mismo paquete y las subclases de otros paquetes
- c) Cualquier clase del programa, sin restricción

**Respuesta correcta:** b) · **Referencia:** §2.3 [GOSLING-JLS]

Es el nivel pensado para que las subclases reutilicen o sobrescriban el miembro, sin exponerlo públicamente.

### 15. Java resuelve el problema del diamante de la herencia múltiple:

- a) Permitiendo herencia múltiple de clases con reglas de precedencia
- b) Obligando a declarar todas las clases como abstractas
- c) Prohibiendo la herencia múltiple de clases, pero permitiendo implementar varias interfaces

**Respuesta correcta:** c) · **Referencia:** §2.4 [GOSLING-JLS; MEYER97]

<code>extends</code> admite una única superclase; <code>implements</code> admite varias interfaces, evitando el conflicto de estado del diamante.

### 16. La relación que modela la herencia entre dos clases se describe habitualmente como:

- a) "es un" (is-a)
- b) "tiene un" (has-a)
- c) "usa un" (uses-a)

**Respuesta correcta:** a) · **Referencia:** §2.4 [BOOCH07]

<code>ExpedienteLicencia</code> <strong>es un</strong> <code>Expediente</code>. La relación "tiene un" (has-a) corresponde a composición o agregación, no a herencia.

### 17. La sobrecarga (overloading) de métodos se resuelve:

- a) En tiempo de ejecución, según la clase real del objeto
- b) En tiempo de compilación, según los tipos de los argumentos de la llamada
- c) De forma aleatoria según el orden de declaración

**Respuesta correcta:** b) · **Referencia:** §2.5 [GOSLING-JLS §8.4]

Es ligadura estática: el compilador decide qué versión del método invocar antes de ejecutar el programa.

### 18. La sobrescritura (overriding) de un método exige que la subclase declare:

- a) Un método con distinto número de parámetros
- b) Un atributo con el mismo nombre que un método heredado
- c) Un método con la misma firma que el de la superclase

**Respuesta correcta:** c) · **Referencia:** §2.5 [GOSLING-JLS §8.4]

Se marca opcionalmente con <code>@Override</code>; si la firma difiere, no hay sobrescritura, sino sobrecarga (o un error si no coincide con ningún método heredado).

### 19. El mecanismo por el cual la JVM decide, en tiempo de ejecución, qué versión de un método invocar según la clase real del objeto se llama:

- a) Ligadura dinámica
- b) Ligadura estática
- c) Sobrecarga

**Respuesta correcta:** a) · **Referencia:** §2.6 [BOOCH07]

También llamada tardía (<em>late binding</em>); es la base técnica del polimorfismo.

### 20. El principio de diseño de GoF "favorece la composición sobre la herencia" advierte principalmente contra:

- a) El uso de interfaces en Java
- b) El uso indiscriminado de herencia para reutilizar código cuando la relación real es "tiene un"
- c) La sobrecarga de constructores

**Respuesta correcta:** b) · **Referencia:** §2.7 [GOF94, cap. 1]

La herencia crea un acoplamiento muy fuerte (problema de la clase base frágil); la composición permite reconfigurar comportamiento en tiempo de ejecución.

### 21. ¿Qué afirmación describe correctamente el coste del software a lo largo de su ciclo de vida?

- a) El coste total del software se concentra siempre en la fase de análisis de requisitos
- b) El mantenimiento del software orientado a objetos es gratuito gracias al encapsulamiento
- c) La mayor parte del coste total del software corresponde históricamente al mantenimiento, no al desarrollo inicial

**Respuesta correcta:** c) · **Referencia:** §3.1 [PRESSMAN14, cap. 20]

Esta es la justificación económica última de perseguir mantenibilidad mediante encapsulamiento y modularidad.

### 22. ¿Qué ventaja de la POO facilita la comunicación entre el equipo técnico y los expertos del dominio de negocio?

- a) La correspondencia directa entre las clases del modelo y las entidades del mundo real del problema
- b) La ausencia de documentación en el código
- c) La eliminación completa de las pruebas unitarias

**Respuesta correcta:** a) · **Referencia:** §3.1 [PRESSMAN14]

Clases como <code>Expediente</code> o <code>Ciudadano</code> reducen la distancia conceptual entre modelo y sistema.

### 23. Cuando un fallo en la implementación interna de una clase no altera su interfaz pública ni sus invariantes, y por tanto no se propaga en cascada, se dice que el sistema logra:

- a) Herencia múltiple
- b) Aislamiento de errores
- c) Sobrecarga de operadores

**Respuesta correcta:** b) · **Referencia:** §3.2 [PRESSMAN14]

Es una consecuencia directa del encapsulamiento y facilita las pruebas unitarias por clase.

### 24. La escalabilidad del equipo de desarrollo en un proyecto OO se ve favorecida principalmente por:

- a) El uso exclusivo de variables globales compartidas
- b) La ausencia de una jerarquía de herencia
- c) La división en clases con responsabilidades delimitadas e interfaces bien definidas

**Respuesta correcta:** c) · **Referencia:** §3.2 [SOMMERVILLE16]

Permite que distintos desarrolladores trabajen en paralelo con interferencia mínima.

### 25. Uno de los principales costes formativos de la POO frente a la programación estructurada básica es:

- a) Una curva de aprendizaje más larga, al exigir dominar simultáneamente abstracción, encapsulamiento, herencia y polimorfismo
- b) La imposibilidad de reutilizar código entre proyectos
- c) La obligación de usar siempre herencia múltiple

**Respuesta correcta:** a) · **Referencia:** §3.3 [PRESSMAN14]

Errores conceptuales tempranos suelen arrastrarse y ser costosos de corregir más adelante.

### 26. Un mal diseño OO inicial puede resultar más rígido de modificar que el equivalente estructurado, sobre todo debido a:

- a) La ausencia total de clases en el sistema
- b) El acoplamiento fuerte que introduce una jerarquía de herencia extensa y profunda
- c) El uso de comentarios en el código fuente

**Respuesta correcta:** b) · **Referencia:** §3.3 [GOF94]

Un cambio en una superclase puede romper subclases: el problema de la clase base frágil.

### 27. El coste en rendimiento de la ligadura dinámica frente a una llamada resuelta en compilación se debe principalmente a:

- a) La necesidad de recompilar el programa en cada ejecución
- b) La ausencia de modificadores de acceso en el lenguaje
- c) Una consulta indirecta a la tabla de métodos de la clase real del objeto en cada invocación

**Respuesta correcta:** c) · **Referencia:** §3.4 [GOSLING-JLS]

Esta indirección es más costosa que una llamada directa resuelta en compilación.

### 28. La creación y destrucción frecuente de muchos objetos de vida corta en Java incrementa la presión sobre:

- a) El recolector de basura (garbage collector)
- b) El compilador estático de tipos
- c) El motor de renderizado gráfico

**Respuesta correcta:** a) · **Referencia:** §3.4 [GOSLING-JLS]

Puede introducir pausas apreciables en sistemas de alto rendimiento o tiempo real.

### 29. Una clase que acumula demasiadas responsabilidades y conoce/controla la mayor parte del sistema, violando el principio de responsabilidad única, se conoce como el anti-patrón:

- a) Factory Method
- b) God Object
- c) Singleton

**Respuesta correcta:** b) · **Referencia:** §3.5 [GOF94]

Concentra un acoplamiento extremo y es contrario al SRP (§1.4).

### 30. ¿Qué disciplina de diseño evita que las ventajas teóricas de la POO se conviertan, en la práctica, en un sistema difícil de mantener?

- a) La eliminación de todas las relaciones de herencia del sistema
- b) La sustitución completa de las clases por funciones globales
- c) La aplicación de SOLID, patrones de diseño y revisión del acoplamiento

**Respuesta correcta:** c) · **Referencia:** §3.5 [MARTIN03]

No es opcional en sistemas OO de tamaño medio o grande.

### 31. Un patrón de diseño es, según GoF:

- a) Una solución general y reutilizable a un problema de diseño OO recurrente, no código listo para copiar
- b) Un fragmento de código que se copia literalmente en cada proyecto
- c) Una regla obligatoria del compilador de Java

**Respuesta correcta:** a) · **Referencia:** §4.1 [GOF94, cap. 1]

Es una plantilla conceptual que se adapta a cada situación concreta.

### 32. ¿Cuántos patrones componen el catálogo original de Gamma, Helm, Johnson y Vlissides (Gang of Four)?

- a) 12
- b) 23
- c) 30

**Respuesta correcta:** b) · **Referencia:** §4.1 [GOF94]

Distribuidos en 5 creacionales, 7 estructurales y 11 de comportamiento.

### 33. Cada patrón GoF documenta, entre otros elementos:

- a) Únicamente el nombre del patrón y su autor
- b) El número de líneas de código que ocupa su implementación
- c) Intención, aplicabilidad, estructura (mini diagrama de clases) y consecuencias

**Respuesta correcta:** c) · **Referencia:** §4.1 [GOF94]

Este formato da a los equipos un vocabulario común de diseño.

### 34. Una solución frecuente en la práctica pero contraproducente a medio o largo plazo, que suele surgir de aplicar un patrón fuera de contexto, se denomina:

- a) Anti-patrón
- b) Patrón estructural
- c) Diagrama de despliegue

**Respuesta correcta:** a) · **Referencia:** §4.2 [GOF94]

Ejemplos: God Object, Spaghetti Code orientado a objetos, Golden Hammer.

### 35. El anti-patrón que consiste en aplicar sistemáticamente un mismo patrón conocido a cualquier problema, por familiaridad del equipo, se llama:

- a) Factory Method
- b) Golden Hammer (martillo de oro)
- c) Composite

**Respuesta correcta:** b) · **Referencia:** §4.2 [GOF94]

Se aplica el patrón conocido aunque no encaje realmente con el problema.

### 36. Usar <code>extends</code> únicamente para reutilizar código de una clase con la que no existe una relación "es un" real es un ejemplo de:

- a) Principio de inversión de dependencias
- b) Patrón Observer
- c) Herencia por conveniencia

**Respuesta correcta:** c) · **Referencia:** §4.2 [GOF94]

Genera jerarquías semánticamente falsas y es uno de los anti-patrones más citados en diseño OO.

### 37. ¿Cuántos patrones creacionales componen el catálogo GoF?

- a) 5
- b) 7
- c) 11

**Respuesta correcta:** a) · **Referencia:** §4.3 [GOF94]

Singleton, Factory Method, Abstract Factory, Builder y Prototype.

### 38. El patrón creacional que garantiza que una clase tenga una única instancia global y proporciona un punto de acceso a ella es:

- a) Builder
- b) Singleton
- c) Prototype

**Respuesta correcta:** b) · **Referencia:** §4.3 [GOF94]

Útil, por ejemplo, para un gestor de configuración cargado una sola vez.

### 39. El patrón que define una interfaz para crear un objeto, dejando que las subclases decidan qué clase concreta instanciar, es:

- a) Adapter
- b) Observer
- c) Factory Method

**Respuesta correcta:** c) · **Referencia:** §4.3 [GOF94]

Desacopla al código cliente de las clases concretas que finalmente se crean.

### 40. ¿Cuántos patrones estructurales componen el catálogo GoF?

- a) 7
- b) 5
- c) 11

**Respuesta correcta:** a) · **Referencia:** §4.4 [GOF94]

Adapter, Bridge, Composite, Decorator, Facade, Flyweight y Proxy.

### 41. El patrón estructural que proporciona una interfaz unificada y simplificada a un conjunto de interfaces de un subsistema complejo es:

- a) Decorator
- b) Facade
- c) Bridge

**Respuesta correcta:** b) · **Referencia:** §4.4 [GOF94]

Oculta la complejidad interna de un subsistema tras un punto de entrada único.

### 42. El patrón de comportamiento que encapsula una familia de algoritmos intercambiables tras una interfaz común, seleccionable en tiempo de ejecución, es:

- a) Visitor
- b) Memento
- c) Strategy

**Respuesta correcta:** c) · **Referencia:** §4.5 [GOF94]

Aplicable, por ejemplo, a los distintos canales de notificación a un ciudadano (§1.4).

### 43. UML surge de la unificación de tres notaciones de modelado OO previas:

- a) El método Booch, la OMT de Rumbaugh y el OOSE de Jacobson
- b) El álgebra relacional, el cálculo relacional y SQL
- c) Los diagramas de flujo de datos, los flujogramas y los pseudocódigos

**Respuesta correcta:** a) · **Referencia:** §5.1 [RUMBAUGH05, prefacio]

Sus autores, «los tres amigos», unieron sus notaciones en Rational Software a partir de 1994.

### 44. ¿Qué organismo adopta y mantiene el estándar UML desde 1997?

- a) ISO (International Organization for Standardization)
- b) OMG (Object Management Group)
- c) W3C (World Wide Web Consortium)

**Respuesta correcta:** b) · **Referencia:** §5.1 [OMG-UML25]

Mantiene desde entonces las sucesivas versiones, hasta la vigente UML 2.5.1 (2017).

### 45. UML debe entenderse principalmente como:

- a) Una metodología de desarrollo obligatoria
- b) Un lenguaje de programación orientado a objetos
- c) Una notación gráfica, sin prescribir un proceso de desarrollo concreto

**Respuesta correcta:** c) · **Referencia:** §5.1 [OMG-UML25]

Puede usarse en metodologías predictivas o ágiles, según las necesidades del proyecto.

### 46. Los estereotipos como <code>«interface»</code> o <code>«actor»</code> son un ejemplo de:

- a) Mecanismo de extensibilidad de UML
- b) Un tipo de diagrama de comportamiento
- c) Un modificador de acceso de Java

**Respuesta correcta:** a) · **Referencia:** §5.2 [OMG-UML25, §7]

Permiten adaptar la notación estándar a necesidades específicas de un dominio sin crear un lenguaje nuevo.

### 47. El diagrama UML más utilizado en la práctica, y con frecuencia el único elaborado por completo en proyectos pequeños, es el:

- a) Diagrama de Despliegue
- b) Diagrama de Clases
- c) Diagrama de Temporización

**Respuesta correcta:** b) · **Referencia:** §5.3 [FOWLER-UML, cap. 5]

Representa clases, atributos, métodos y relaciones con una caja de tres compartimentos.

### 48. En la notación de un diagrama de clases UML, un rombo relleno en el extremo de una relación representa:

- a) Agregación
- b) Asociación simple
- c) Composición

**Respuesta correcta:** c) · **Referencia:** §5.3 [RUMBAUGH05]

El rombo hueco, en cambio, representa agregación (dependencia de ciclo de vida más débil).

### 49. A diferencia del diagrama de clases, el Diagrama de Objetos UML representa:

- a) Una instantánea de instancias concretas en un momento dado, con sus valores de atributo reales
- b) Los nodos de hardware sobre los que se despliega el sistema
- c) La secuencia temporal de mensajes entre objetos

**Respuesta correcta:** a) · **Referencia:** §5.3 [FOWLER-UML]

Útil para ilustrar ejemplos concretos de una relación compleja o depurar un estado del sistema.

### 50. El Diagrama de Clases UML se diferencia del modelo Entidad-Relación (Tema 16) principalmente en que:

- a) El E/R incluye siempre métodos y el diagrama de clases nunca
- b) El diagrama de clases modela datos y comportamiento juntos (con métodos), mientras que el E/R modela datos persistentes para una base de datos relacional
- c) Ambos son exactamente el mismo diagrama con distinto nombre

**Respuesta correcta:** b) · **Referencia:** §5.3 [FOWLER-UML]

Un mismo concepto del dominio puede aparecer en ambos con contenido distinto.

### 51. El diagrama UML que representa la arquitectura física, es decir, los nodos de hardware y sus conexiones de red, es el:

- a) Diagrama de Componentes
- b) Diagrama de Paquetes
- c) Diagrama de Despliegue

**Respuesta correcta:** c) · **Referencia:** §5.4 [OMG-UML25]

(<em>deployment</em>) muestra sobre qué servidores o dispositivos se despliegan los artefactos software.

### 52. ¿Cuántos tipos de diagrama estructural define UML 2.5?

- a) 7
- b) 5
- c) 14

**Respuesta correcta:** a) · **Referencia:** §5.4 [UML-DIAG-TYPES]

Clases, Objetos, Componentes, Despliegue, Paquetes, Estructura Compuesta y Perfiles (más 7 de comportamiento = 14 en total).

### 53. En un Diagrama de Casos de Uso, la relación <code>«include»</code> indica:

- a) Que un actor puede realizar la acción de forma opcional
- b) Que un caso de uso incorpora obligatoriamente la funcionalidad de otro, reutilizada
- c) Que dos actores son en realidad el mismo rol

**Respuesta correcta:** b) · **Referencia:** §5.5 [OMG-UML25]

Frente a <code>«extend»</code>, que representa funcionalidad opcional bajo ciertas condiciones.

### 54. En un Diagrama de Secuencia, el tiempo avanza:

- a) De izquierda a derecha, sobre líneas de vida horizontales
- b) En sentido circular alrededor de los objetos
- c) De arriba abajo, sobre líneas de vida verticales

**Respuesta correcta:** c) · **Referencia:** §5.6 [FOWLER-UML]

Los mensajes se dibujan como flechas horizontales entre líneas de vida, en el orden temporal exacto en que se producen.

### 55. El Diagrama de Comunicación (o de Colaboración) se diferencia del de Secuencia en que:

- a) Organiza a los objetos espacialmente como un grafo, numerando los mensajes para indicar el orden, en lugar de usar la posición vertical
- b) No permite representar el envío de mensajes entre objetos
- c) Solo puede usarse para modelar bases de datos relacionales

**Respuesta correcta:** a) · **Referencia:** §5.6 [OMG-UML25]

Ambos diagramas son semánticamente equivalentes; difieren en el énfasis visual.

### 56. El Diagrama de Máquina de Estados es especialmente útil para modelar:

- a) La arquitectura física de red del sistema
- b) Los distintos estados por los que pasa un objeto a lo largo de su vida y las transiciones entre ellos
- c) La lista de atributos privados de una clase

**Respuesta correcta:** b) · **Referencia:** §5.7 [OMG-UML25]

Heredero del <em>statechart</em> de Harel; el patrón State (§4.5) es su implementación en código.

### 57. Las expresiones lambda e interfaces funcionales incorporadas en Java desde la versión 8 permiten, en muchos casos:

- a) Eliminar por completo la necesidad de usar clases en Java
- b) Sustituir la herencia múltiple de C++ dentro de Java
- c) Sustituir una implementación completa del patrón Strategy por una alternativa más ligera, sin abandonar el modelo de clases y objetos

**Respuesta correcta:** c) · **Referencia:** §6 [GOSLING-JLS]

Reflejan la influencia de la programación funcional sobre los lenguajes OO modernos.

### 58. El Diseño Dirigido por el Dominio (Domain-Driven Design) extiende explícitamente al diseño de servicios distribuidos:

- a) Conceptos de modelado OO como entidades con identidad, objetos de valor inmutables y agregados como unidad de consistencia
- b) La programación no estructurada basada en saltos GOTO
- c) La eliminación de todo vocabulario compartido con el negocio

**Respuesta correcta:** a) · **Referencia:** §6 [BOOCH07]

DDD refuerza, más que sustituye, los fundamentos de la POO clásica.

### 59. La inyección de dependencias, hoy sistematizada como mecanismo de plataforma en los grandes frameworks Java, es una forma sistematizada de:

- a) El problema del diamante de la herencia múltiple
- b) El principio de inversión de dependencias (DIP) y del patrón Factory
- c) El anti-patrón God Object

**Respuesta correcta:** b) · **Referencia:** §6 [MARTIN03; GOF94]

Reduce la necesidad de implementar manualmente Factory Method o Abstract Factory en cada proyecto.

### 60. El modelado ejecutable y la generación de código a partir de diagramas de clases UML, con ida y vuelta entre modelo y código, se conoce como:

- a) Garbage collection
- b) Ligadura estática
- c) Round-trip engineering

**Respuesta correcta:** c) · **Referencia:** §6 [OMG-UML25]

Tendencia actual de las herramientas de modelado, sin renunciar a la semántica formal del estándar OMG.

## Preguntas sobre los casos prácticos

### Caso 1. Diseño de clases para la tramitación de licencias

#### 1. En el supuesto planteado, ¿qué visibilidad deben tener los atributos idExpediente y estado de la clase Expediente para que queden correctamente encapsulados?

- a) public, para que el controlador y las subclases puedan leerlos y modificarlos directamente.
- b) protected, para que cualquier clase de la aplicación pueda consultarlos sin métodos get.
- c) private, de modo que solo se acceda a ellos a través de métodos públicos como getEstado().

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.3

La regla de diseño es exponer el mínimo nivel de visibilidad: atributos casi siempre private, accesibles solo mediante métodos get/set que pueden validar el valor.

#### 2. Desde un método de la subclase ExpedienteLicenciaObra, situada en otro paquete, ¿puede leerse directamente el atributo private estado heredado de Expediente?

- a) No: un atributo private solo es accesible desde su propia clase; la subclase debe usar getEstado().
- b) Sí: las subclases heredan el acceso directo a todos los atributos de la superclase.
- c) Sí: basta con marcar el método de la subclase con la anotación @Override.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.3

Según la tabla de modificadores de Java, private es visible solo en la misma clase: ni desde el mismo paquete ni desde subclases.

#### 3. Expediente solo tiene un constructor, que recibe el identificador. Si en ExpedienteLicenciaObra se omitiera la llamada super(id), ¿qué ocurriría?

- a) El objeto se crearía igualmente, con el identificador y el estado sin inicializar y sin ningún aviso.
- b) Error de compilación: Java intentaría invocar un constructor sin argumentos de Expediente, que no existe.
- c) Java llamaría automáticamente a super(id) usando el identificador recibido por la subclase.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.2

Si la subclase no invoca explícitamente un constructor de la superclase, Java invoca el constructor sin argumentos; si este no existe, se produce un error de compilación.

#### 4. Se registra una licencia de obra con tipoLicencia «ACTIVIDAD». ¿Qué plazo de resolución devuelve calcularPlazoResolucion()?

- a) 30 días, porque solo «OBRA_MAYOR» tiene un plazo distinto.
- b) 90 días, porque toda licencia de obra tiene el plazo largo.
- c) 15 días, porque «ACTIVIDAD» no es una obra propiamente dicha.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2

La regla de la subclase de obra es: 90 días si tipoLicencia es «OBRA_MAYOR» y 30 en el resto de casos, entre ellos «ACTIVIDAD».

#### 5. Una solicitud de terraza declara exactamente 20 metros cuadrados. ¿Qué plazo devuelve calcularPlazoResolucion()?

- a) 30 días, porque a partir de 20 metros cuadrados se aplica el plazo largo.
- b) 90 días, el mismo plazo que se aplica a una licencia de obra mayor.
- c) 15 días, porque la condición es menor o igual a 20 metros cuadrados.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2

La regla de terraza es metrosCuadrados <= 20 → 15 días; solo por encima de 20 se aplican 30 días.

#### 6. ¿Qué aporta la anotación @Override sobre calcularPlazoResolucion() en cada subclase?

- a) Hace que la versión que se ejecuta se decida en tiempo de compilación, no de ejecución.
- b) Hace que el compilador verifique que existe en la superclase un método con la misma firma.
- c) Es obligatoria: sin ella, Java ejecutaría siempre la versión de la superclase Expediente.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.5

@Override es opcional pero recomendada: obliga al compilador a comprobar que realmente se está sobrescribiendo un método de igual firma de la superclase.

#### 7. Las dos versiones de notificar (una con mensaje y otra con mensaje y canal) conviven en Expediente. ¿Qué mecanismo es y cuándo se decide cuál se invoca?

- a) Sobrecarga: mismo nombre y distinta firma; el compilador elige la versión en tiempo de compilación.
- b) Sobrescritura: misma firma y distinta clase; la JVM elige la versión en tiempo de ejecución.
- c) Polimorfismo: misma firma en la misma clase; la versión depende del objeto real que la recibe.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §2.5

La sobrecarga define en la misma clase varios métodos con el mismo nombre y distinta lista de parámetros, y se resuelve por ligadura estática, en compilación.

#### 8. Una lista declarada como List<Expediente> contiene una licencia de obra «OBRA_MAYOR» y una terraza de 12 m². Al recorrerla llamando a calcularPlazoResolucion(), ¿qué se obtiene?

- a) 30 y 30, porque se ejecuta la versión correspondiente al tipo declarado Expediente.
- b) 90 y 15, porque se ejecuta la versión de la clase real de cada objeto (ligadura dinámica).
- c) Un error de compilación, porque el método está declarado como abstracto en Expediente.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.6

Con el polimorfismo, al invocar un método sobrescrito se ejecuta la versión de la clase real del objeto, no la del tipo declarado de la variable.

#### 9. ¿Por qué conviene que calcularPlazoResolucion() sea abstracto en lugar de tener en Expediente una implementación por defecto de 30 días?

- a) Porque los métodos abstractos se resuelven con ligadura estática y son más rápidos de ejecutar.
- b) Porque Java no permite que una clase concreta tenga subclases que sobrescriban sus métodos.
- c) Porque así el compilador exige la implementación en cada subclase y no se devuelve un plazo erróneo en silencio.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 4 · §1.4

Con un valor por defecto, una subclase nueva que olvidara sobrescribir el método devolvería 30 días sin avisar; declararlo abstracto convierte ese olvido en un error de compilación.

#### 10. Urbanismo añade un nuevo tipo de expediente creando otra subclase de Expediente, sin tocar el código que ya trabaja con Expediente. ¿Qué principio SOLID se está respetando?

- a) El principio abierto/cerrado: abierto a extensión y cerrado a modificación.
- b) El principio de responsabilidad única: una sola razón para cambiar.
- c) El principio de segregación de interfaces: interfaces específicas de cliente.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §1.4

Añadir un nuevo tipo de expediente no debería obligar a modificar el código que ya trata con Expediente: basta con crear una nueva subclase. Es el principio abierto/cerrado.

### Caso 2. Aplicación de patrones de diseño al alta de expedientes

#### 1. Para crear el tipo de expediente correcto a partir del código recibido del formulario, sin que el controlador web conozca las clases concretas, ¿qué patrón creacional GoF se aplica?

- a) Factory Method, que delega en una fábrica la decisión de qué clase concreta instanciar.
- b) Singleton, que garantiza una única instancia global del expediente que se va a crear.
- c) Prototype, que crea cada expediente nuevo clonando un expediente ya existente.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §4.3

Factory Method desacopla al código cliente de las clases concretas que se crean; el controlador pide un Expediente y la fábrica decide si es de obra o de terraza.

#### 2. ¿Qué inconveniente tendría instanciar directamente con new cada subclase dentro del controlador web?

- a) Que new es más lento que una fábrica, porque reserva memoria cada vez que se ejecuta.
- b) Que Java no permite instanciar subclases fuera del paquete donde se declara la superclase.
- c) Que acopla el controlador a las clases concretas y obliga a modificarlo al añadir un tipo nuevo.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §4.3

Escribir new ExpedienteLicenciaObra(...) en el cliente lo acopla a las clases concretas; cada tipo nuevo obligaría a tocar el controlador, en contra del principio abierto/cerrado.

#### 3. La fábrica recibe desde el formulario un código de tipo que todavía no está soportado. ¿Cómo debe comportarse el método crear?

- a) Devolver null, para que el controlador decida después qué hacer con la solicitud.
- b) Lanzar una IllegalArgumentException que indique que el tipo de expediente no está soportado.
- c) Crear por defecto una licencia de obra, que es el tipo de expediente más frecuente.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.3

La rama default del switch de la fábrica lanza IllegalArgumentException(«Tipo no soportado…»): el caso no previsto se trata de forma explícita.

#### 4. ¿Qué tipo de retorno debe declarar el método crear de ExpedienteFactory?

- a) Object, para que la fábrica pueda devolver cualquier clase de la aplicación.
- b) ExpedienteLicenciaObra, porque es la primera subclase contemplada en el switch.
- c) Expediente, la superclase abstracta, para que el controlador solo dependa de la abstracción.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §4.3

La fábrica devuelve un Expediente: el código cliente trabaja con la superclase y no sabe qué subclase concreta se ha creado.

#### 5. Para notificar al ciudadano por el canal que haya elegido (correo, SMS o sede electrónica), pudiendo añadirse canales nuevos, ¿qué patrón de comportamiento se aplica?

- a) Strategy, que encapsula algoritmos intercambiables tras una interfaz común.
- b) Observer, que avisa a todos los suscriptores cuando cambia el estado del sujeto.
- c) Singleton, que mantiene un único canal global para todas las notificaciones.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §4.5

Strategy encapsula una familia de algoritmos intercambiables (los canales de notificación) tras una interfaz común, seleccionable en tiempo de ejecución.

#### 6. El código que notifica depende de la interfaz CanalNotificacion y no de clases concretas como el envío por SMTP. ¿Qué principio SOLID se cumple así?

- a) El de sustitución de Liskov.
- b) El de inversión de dependencias.
- c) El de responsabilidad única.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §1.4

El principio de inversión de dependencias pide que los módulos dependan de abstracciones (interfaces), no de implementaciones concretas; depender de una clase EnvioCorreoSMTP lo violaría.

#### 7. El Ayuntamiento añade un cuarto canal: notificación push en la app municipal. ¿Qué cambio exige el diseño propuesto?

- a) Añadir en el código que notifica una nueva rama if para el canal push.
- b) Añadir a la interfaz CanalNotificacion un método enviarPush específico.
- c) Crear una clase NotificacionPush que implemente CanalNotificacion.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §1.4

Con Strategy, el canal nuevo es una implementación más de la interfaz; el código que recibe un CanalNotificacion y llama a enviar(...) no cambia.

#### 8. Se añade además el tipo ExpedienteVadoPermanente. ¿Qué hay que modificar?

- a) Crear la nueva subclase y añadir su case en la fábrica; el controlador que la invoca no cambia.
- b) Modificar el controlador web para que instancie directamente la nueva subclase con new.
- c) Nada: la fábrica detecta y crea automáticamente cualquier subclase nueva de Expediente.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §4.3

Con la fábrica, un tipo nuevo solo afecta a la nueva clase y a ExpedienteFactory; el código cliente que llama a crear(...) permanece igual.

#### 9. ¿A qué familias del catálogo GoF pertenecen los dos patrones aplicados en el supuesto?

- a) Ambos pertenecen a la familia de los patrones estructurales.
- b) Factory Method es creacional y Strategy, de comportamiento.
- c) Factory Method es de comportamiento y Strategy, creacional.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestiones 1 y 3 · §4.3 y §4.5

Los creacionales abstraen la instanciación de objetos (Factory Method); los de comportamiento, cómo colaboran y se reparten responsabilidades los objetos (Strategy).

#### 10. Si en lugar de fábrica y estrategia el controlador web concentrara la creación de todos los tipos de expediente y el envío por todos los canales, ¿en qué anti-patrón se incurriría?

- a) Golden Hammer, por aplicar a todo el mismo patrón conocido.
- b) Herencia por conveniencia, por heredar solo para reutilizar.
- c) God Object, por acumular demasiadas responsabilidades.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §4.2

Una clase que acumula demasiadas responsabilidades y controla la mayor parte del sistema es un God Object: viola el principio de responsabilidad única.

### Caso 3. Modelado UML del flujo de tramitación

#### 1. En el diagrama de clases del módulo de licencias, ¿cuántos compartimentos tiene el rectángulo de la clase Expediente y qué contienen?

- a) Dos: el nombre de la clase y la lista de métodos.
- b) Tres: el nombre de la clase, sus atributos y sus métodos.
- c) Cuatro: nombre, atributos, métodos y relaciones con otras clases.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §5.3

Cada clase se dibuja como un rectángulo con tres compartimentos: nombre, atributos y métodos, estos dos últimos con su visibilidad.

#### 2. ¿Cómo se anota en el diagrama de clases el atributo private idExpediente de tipo String?

- a) - idExpediente : String
- b) # idExpediente : String
- c) + idExpediente : String

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §2.3 y §5.3

En UML la visibilidad se anota con - (private), # (protected), ~ (package) y + (public).

#### 3. ¿Con qué notación se une ExpedienteLicenciaObra a Expediente en el diagrama de clases?

- a) Con un rombo relleno en el extremo de Expediente, que indica composición.
- b) Con una línea discontinua y flecha abierta, que indica una dependencia puntual.
- c) Con una flecha de generalización de punta triangular hueca hacia Expediente.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §5.3

La herencia (generalización) se dibuja con una flecha de punta triangular hueca que apunta a la superclase.

#### 4. Cada expediente guarda una referencia permanente a su canal de notificación preferido. ¿Por qué esa relación NO es una composición?

- a) Porque la composición solo puede unir clases abstractas con sus subclases concretas.
- b) Porque el expediente no controla el ciclo de vida del canal, que existe con independencia de él.
- c) Porque la composición no admite que una clase guarde una referencia a otra como atributo.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §2.8

En la composición el contenedor gestiona el ciclo de vida del contenido (si se destruye uno, se destruye el otro); el canal de notificación sigue existiendo aunque desaparezca el expediente.

#### 5. En el diagrama de casos de uso de «solicitar una licencia de obra», ¿cuál es el actor y cuál el caso de uso principal?

- a) Actor: Ciudadano; caso de uso: «Solicitar licencia de obra».
- b) Actor: PortalWeb; caso de uso: «Crear expediente de obra».
- c) Actor: ExpedienteFactory; caso de uso: «Calcular el plazo».

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §5.5

Los actores son roles externos que interactúan con el sistema, como el ciudadano; el caso de uso es la funcionalidad completa que el sistema le ofrece.

#### 6. «Autenticarse en sede electrónica» es un paso obligatorio de la solicitud y se reutiliza en otras (terraza, vado). ¿Qué relación lo une a «Solicitar licencia de obra»?

- a) «extend», porque amplía la solicitud solo bajo ciertas condiciones.
- b) Generalización, porque la autenticación es un tipo de solicitud.
- c) «include», porque es funcionalidad obligatoria y reutilizada.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §5.5

«include» se usa para funcionalidad obligatoria y reutilizada por varios casos de uso; «extend», para funcionalidad opcional bajo ciertas condiciones.

#### 7. El equipo quiere reflejar también que «Adjuntar plano técnico» solo se añade a la solicitud cuando la licencia es de obra mayor. ¿Qué relación corresponde?

- a) «include», porque el plano forma parte de toda solicitud de licencia.
- b) «extend», porque es funcionalidad opcional que amplía el caso de uso bajo una condición.
- c) Asociación, porque el plano es un actor externo que interactúa con el sistema.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §5.5

«extend» modela funcionalidad opcional que amplía otro caso de uso solo cuando se da una condición, como la obra mayor.

#### 8. En el diagrama de secuencia de la solicitud, ¿cuál es el primer mensaje?

- a) PortalWeb → ExpedienteFactory: crear("OBRA", id, tipoLicencia).
- b) ExpedienteFactory → ExpedienteLicenciaObra: new (mensaje de creación).
- c) Ciudadano → PortalWeb: enviarSolicitud(datosFormulario).

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §5.6

El escenario empieza cuando el ciudadano envía el formulario al portal; después el portal pide a la fábrica que cree el expediente y esta lo instancia.

#### 9. El expediente de obra mayor responde al portal con el plazo de 90 días. ¿Cómo se dibuja ese mensaje en el diagrama de secuencia?

- a) Como un mensaje de retorno, con flecha discontinua hacia la línea de vida de PortalWeb.
- b) Como un rombo relleno sobre la línea de vida del expediente que devuelve el valor.
- c) Como una flecha de punta triangular hueca que sube hacia el primer mensaje enviado.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §5.6

Los mensajes son flechas horizontales entre líneas de vida, en orden temporal de arriba abajo; el retorno se dibuja con flecha discontinua.

#### 10. Para mostrar en qué ubicación física está el servidor que aloja el módulo de licencias, ¿qué diagrama UML se usa y de qué familia es?

- a) El Diagrama de Despliegue, de la familia de comportamiento.
- b) El Diagrama de Despliegue, de la familia estructural.
- c) El Diagrama de Componentes, de la familia estructural.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §5.4

El Diagrama de Despliegue representa la arquitectura física (nodos de hardware y sus conexiones) y es uno de los siete diagramas estructurales; el de Componentes muestra la organización lógica del software.
