# Test del tema 16. Modelo conceptual de datos

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-16.html>

## Batería de preguntas

### 1. Un modelo de datos conceptual se caracteriza por:

- a) Ser independiente del SGBD y estar próximo a la visión del usuario
- b) Describir cómo se almacenan físicamente los datos en disco
- c) Depender del producto concreto de base de datos elegido

**Respuesta correcta:** a) · **Referencia:** §1.1 [ELMASRI]

El modelo conceptual (E-R) es independiente de la tecnología; el lógico depende del tipo de SGBD y el físico, del producto y el soporte.

### 2. En la arquitectura ANSI/SPARC, ¿cuántos esquemas de cada tipo existen?

- a) Uno externo, varios conceptuales y uno interno
- b) Uno de cada tipo
- c) Varios externos, uno conceptual y uno interno

**Respuesta correcta:** c) · **Referencia:** §1.2 [ANSI-SPARC]

Puede haber muchas vistas (esquemas externos), pero el esquema conceptual y el interno son únicos.

### 3. El nivel conceptual de la arquitectura ANSI/SPARC contiene:

- a) Las rutas de acceso, índices y la ubicación física de los datos
- b) Las vistas particulares de cada grupo de usuarios
- c) La estructura global de la base de datos: entidades, atributos, relaciones y restricciones

**Respuesta correcta:** c) · **Referencia:** §1.2 [ANSI-SPARC]

El nivel conceptual describe toda la base de datos para la comunidad de usuarios, sin detalles de almacenamiento.

### 4. La independencia física de datos permite:

- a) Cambiar el esquema conceptual sin alterar las vistas
- b) Cambiar las vistas sin alterar las aplicaciones
- c) Cambiar el almacenamiento interno sin alterar el esquema conceptual

**Respuesta correcta:** c) · **Referencia:** §1.3 [DATE]

La independencia física aísla el nivel conceptual de los cambios en el nivel interno (índices, ficheros).

### 5. ¿Cuál de estas afirmaciones sobre la independencia de datos es correcta?

- a) La independencia lógica es la más difícil de lograr
- b) La independencia física es la más difícil de lograr
- c) Ambas son igual de sencillas de conseguir

**Respuesta correcta:** a) · **Referencia:** §1.3 [DATE]

La independencia lógica es más difícil porque las vistas dependen directamente del esquema conceptual.

### 6. El "universo del discurso" o dominio en el modelado de datos es:

- a) El conjunto de SGBD disponibles en el mercado
- b) La parcela de la realidad que se quiere representar
- c) El lenguaje de programación elegido para la implementación

**Respuesta correcta:** b) · **Referencia:** §1.4 [METRICA3]

El modelo de dominio captura los conceptos del negocio antes de pensar en la solución informática.

### 7. El modelado dinámico de un sistema de información se ocupa de:

- a) Cómo cambia de estado el sistema ante los eventos
- b) La estructura de los datos y sus relaciones
- c) Las transformaciones que sufren los datos al fluir entre procesos

**Respuesta correcta:** a) · **Referencia:** §1.5 [RUMBAUGH]

El modelado dinámico (DTE) describe el comportamiento; el estático, los datos (E-R); el funcional, los procesos (DFD).

### 8. La técnica clásica del modelado funcional es:

- a) El modelo entidad-relación (E-R)
- b) El diagrama de flujo de datos (DFD)
- c) El diagrama de transición de estados (DTE)

**Respuesta correcta:** b) · **Referencia:** §1.5 [YOURDON]

El DFD modela la vista funcional (procesos); el E-R, la estática (datos); el DTE, la dinámica (comportamiento).

### 9. Un dato se convierte en información cuando:

- a) Se almacena en un fichero binario
- b) Se procesa y se interpreta dándole significado en un contexto
- c) Se representa en código ASCII

**Respuesta correcta:** b) · **Referencia:** §1.1 [METRICA3]

El dato es la representación simbólica; la información es el dato procesado e interpretado.

### 10. El modelo lógico de datos más extendido es:

- a) El modelo relacional
- b) El modelo jerárquico
- c) El modelo en red (CODASYL)

**Respuesta correcta:** a) · **Referencia:** §1.1 [CODD]

El modelo relacional de Codd (tablas) es el dominante en el nivel lógico; el conceptual usa E-R.

### 11. El modelo Entidad-Relación fue propuesto por:

- a) Peter Chen en 1976
- b) Edgar F. Codd en 1970
- c) Tom DeMarco en 1979

**Respuesta correcta:** a) · **Referencia:** §2.1 [CHEN]

Chen propuso el E-R como vista unificada de los datos. Codd (1970) propuso el modelo relacional; DeMarco (1979), el DFD.

### 12. En notación de Chen, una entidad se representa mediante:

- a) Un rombo
- b) Un rectángulo
- c) Una elipse

**Respuesta correcta:** b) · **Referencia:** §2.2 [CHEN]

En Chen: entidad = rectángulo; relación = rombo; atributo = elipse.

### 13. La diferencia entre un tipo de entidad y una ocurrencia es que:

- a) El tipo es la plantilla o categoría; la ocurrencia es un ejemplar concreto
- b) Son sinónimos
- c) La ocurrencia se dibuja en el diagrama y el tipo no

**Respuesta correcta:** a) · **Referencia:** §2.2 [ELMASRI]

El tipo `HABITANTE` se dibuja; las ocurrencias (cada habitante) pueblan la base de datos y no se dibujan.

### 14. Una entidad débil se caracteriza porque:

- a) No puede identificarse solo con sus atributos y depende de una entidad fuerte
- b) Tiene pocos atributos
- c) No participa en ninguna relación

**Respuesta correcta:** a) · **Referencia:** §2.2 [ELMASRI]

La entidad débil necesita la clave de la entidad fuerte más un discriminante (clave parcial). Se dibuja con rectángulo doble.

### 15. En notación de Chen, un atributo identificador (clave) se representa:

- a) Con una elipse doble
- b) Con una elipse de línea discontinua
- c) Con la elipse subrayada

**Respuesta correcta:** c) · **Referencia:** §2.3 [CHEN]

El identificador se subraya; la elipse doble es multivaluado y la discontinua, derivado.

### 16. Un atributo multivaluado se representa en notación de Chen con:

- a) Una elipse de línea discontinua
- b) Un rombo
- c) Una elipse doble

**Respuesta correcta:** c) · **Referencia:** §2.3 [CHEN]

El multivaluado (p. ej. varios teléfonos) se dibuja con elipse doble; el derivado, con elipse discontinua.

### 17. El atributo "edad", obtenido a partir de la fecha de nacimiento, es un atributo:

- a) Compuesto
- b) Multivaluado
- c) Derivado (calculado)

**Respuesta correcta:** c) · **Referencia:** §2.3 [ELMASRI]

Un atributo derivado se calcula a partir de otros; no se almacena. Se dibuja con elipse discontinua.

### 18. Un atributo compuesto es aquel que:

- a) Toma varios valores para una misma ocurrencia
- b) Se descompone en partes con significado propio
- c) Se calcula a partir de otros atributos

**Respuesta correcta:** b) · **Referencia:** §2.3 [ELMASRI]

Ejemplo: `domicilio` = (vía, número, planta, puerta, CP). El que toma varios valores es multivaluado; el calculado, derivado.

### 19. El "grado" de una relación es:

- a) El número máximo de ocurrencias asociadas
- b) El número de atributos de la relación
- c) El número de tipos de entidad que participan en ella

**Respuesta correcta:** c) · **Referencia:** §2.4 [CHEN]

Grado unario (1), binario (2), ternario (3). El máximo de ocurrencias asociadas es la cardinalidad.

### 20. Una relación en la que una entidad se asocia consigo misma es:

- a) Ternaria
- b) Recursiva (unaria)
- c) De cardinalidad N:M

**Respuesta correcta:** b) · **Referencia:** §2.4 [ELMASRI]

Una relación recursiva o unaria liga una entidad consigo misma (p. ej. EMPLEADO supervisa a EMPLEADO).

### 21. La razón de cardinalidad de una relación binaria indica:

- a) Si la participación es obligatoria u opcional
- b) El número de atributos de cada entidad
- c) El número máximo de ocurrencias de una entidad asociadas a una de la otra

**Respuesta correcta:** c) · **Referencia:** §2.4 [ELMASRI]

La cardinalidad máxima da los tipos 1:1, 1:N, N:M. La obligatoriedad es la participación (cardinalidad mínima).

### 22. "Un distrito tiene muchos barrios y cada barrio pertenece a un solo distrito" es una relación de cardinalidad:

- a) 1:1
- b) 1:N
- c) N:M

**Respuesta correcta:** b) · **Referencia:** §2.4 [ELMASRI]

Un distrito (1) se asocia con muchos barrios (N), pero cada barrio con un solo distrito.

### 23. La participación total de una entidad en una relación significa que:

- a) Toda ocurrencia de la entidad debe participar en la relación (mínimo 1)
- b) Alguna ocurrencia puede no participar (mínimo 0)
- c) Todas las entidades del modelo participan

**Respuesta correcta:** a) · **Referencia:** §2.4 [ELMASRI]

La participación total (obligatoria) se dibuja con línea doble en Chen; la parcial es opcional (mínimo 0).

### 24. En la notación (mín, máx), el par (0, N) indica:

- a) Participación obligatoria y cardinalidad máxima 1
- b) Participación opcional y cardinalidad máxima muchos
- c) Participación obligatoria y cardinalidad máxima muchos

**Respuesta correcta:** b) · **Referencia:** §2.4 [METRICA3]

El mínimo 0 indica opcionalidad (parcial); el máximo N indica muchos.

### 25. Al transformar una relación N:M al modelo relacional se obtiene:

- a) Una clave ajena en una de las dos tablas
- b) Una única tabla que fusiona las dos entidades
- c) Una tabla intermedia con las claves de ambas entidades

**Respuesta correcta:** c) · **Referencia:** §3.4 [ELMASRI]

La N:M genera una tabla cuya clave primaria es la combinación de las claves de las dos entidades, más los atributos de la relación.

### 26. Al transformar una relación 1:N al modelo relacional:

- a) Se crea siempre una tabla intermedia
- b) La clave del lado "1" se propaga como clave ajena a la tabla del lado "N"
- c) La clave del lado "N" se propaga al lado "1"

**Respuesta correcta:** b) · **Referencia:** §3.4 [ELMASRI]

En 1:N, la clave del lado "1" pasa como clave ajena al lado "N". La tabla intermedia es propia de N:M.

### 27. La relación de generalización/especialización del modelo E-R extendido es del tipo:

- a) "parte-de" (composición)
- b) "es-un" (is-a), con herencia de atributos del supertipo
- c) "muchos-a-muchos"

**Respuesta correcta:** b) · **Referencia:** §3.2 [ELMASRI]

Los subtipos heredan los atributos comunes del supertipo y añaden los específicos.

### 28. En una jerarquía de especialización, una restricción "disjunta" significa que:

- a) Todo ejemplar del supertipo está en algún subtipo
- b) Un ejemplar pertenece a un solo subtipo
- c) Un ejemplar puede pertenecer a varios subtipos a la vez

**Respuesta correcta:** b) · **Referencia:** §3.2 [ELMASRI]

Disjunta = un solo subtipo; solapada = varios. La cobertura total/parcial es la otra restricción (¿todo ejemplar está en algún subtipo?).

### 29. En un diagrama de transición de estados, un "estado" es:

- a) Un estímulo que provoca un cambio
- b) Una situación estable en la que se encuentra el sistema esperando un evento
- c) Una operación que se ejecuta en la transición

**Respuesta correcta:** b) · **Referencia:** §8.1 [YOURDON]

El estímulo es el evento; la operación es la acción.

### 30. El elemento que dispara una transición en un DTE es:

- a) La acción
- b) El estado final
- c) El evento (suceso)

**Respuesta correcta:** c) · **Referencia:** §8.1 [YOURDON]

El evento dispara la transición; la condición (guarda) la habilita; la acción es lo que se ejecuta.

### 31. La etiqueta de una transición en un DTE/UML sigue el patrón:

- a) acción [evento] / condición
- b) evento [condición] / acción
- c) condición / evento [acción]

**Respuesta correcta:** b) · **Referencia:** §8.1 [UML]

El evento dispara, la condición (entre corchetes) restringe y la acción se ejecuta.

### 32. En un DTE bien construido:

- a) Hay un único estado inicial y los estados son mutuamente excluyentes
- b) Puede haber varios estados iniciales
- c) Los estados pueden solaparse en el tiempo

**Respuesta correcta:** a) · **Referencia:** §8.2 [YOURDON]

El sistema está en un único estado en cada instante; el estado inicial es único, aunque puede haber varios finales.

### 33. Una autotransición en un DTE es:

- a) Una transición sin evento
- b) Un estado sin salida
- c) Una transición que vuelve al mismo estado de partida

**Respuesta correcta:** c) · **Referencia:** §8.2 [UML]

Las autotransiciones (mismo estado origen y destino) son válidas.

### 34. El DTE clásico equivale formalmente a:

- a) Una máquina de estados finita
- b) Una tabla relacional
- c) Un diagrama de flujo de datos

**Respuesta correcta:** a) · **Referencia:** §8.3 [UML]

El DTE es una máquina de estados finita; UML lo amplía en el diagrama de estados (estados compuestos, regiones concurrentes).

### 35. ¿Cuál es el equivalente del DTE clásico en UML?

- a) El diagrama de estados (máquina de estados)
- b) El diagrama de clases
- c) El diagrama de actividad

**Respuesta correcta:** a) · **Referencia:** §8.3 [FOWLER]

En UML: E-R ↔ clases; DTE ↔ estados; DFD/flujograma ↔ actividad.

### 36. El diagrama de flujo de datos (DFD) modela:

- a) El orden temporal y las decisiones de un algoritmo
- b) La estructura estática de los datos
- c) El sistema como una red de procesos que transforman datos

**Respuesta correcta:** c) · **Referencia:** §4.1 [DEMARCO]

El DFD muestra qué transformaciones sufren los datos, sin orden temporal (eso es el flujograma).

### 37. ¿Cuáles son los cuatro componentes del DFD?

- a) Proceso, flujo de datos, almacén y entidad externa
- b) Estado, transición, evento y acción
- c) Entidad, atributo, relación y cardinalidad

**Respuesta correcta:** a) · **Referencia:** §4.1 [DEMARCO]

El proceso transforma, el flujo es el dato en movimiento, el almacén el dato en reposo y la entidad externa la frontera.

### 38. En un DFD, un almacén de datos (data store) representa:

- a) Un dato en reposo (fichero, tabla)
- b) Un dato en movimiento
- c) Una transformación de datos

**Respuesta correcta:** a) · **Referencia:** §4.1 [DEMARCO]

El almacén es el dato en reposo; el flujo, el dato en movimiento; el proceso, la transformación.

### 39. Una entidad externa en un DFD es:

- a) Un almacén de datos interno
- b) Un proceso de alto nivel
- c) Una persona, organización o sistema externo que produce o consume datos

**Respuesta correcta:** c) · **Referencia:** §4.1 [DEMARCO]

La entidad externa (terminador) marca la frontera del sistema; se dibuja como rectángulo.

### 40. ¿Cuál de estas conexiones está PROHIBIDA en un DFD?

- a) Un flujo entre una entidad externa y un proceso
- b) Un flujo directo entre dos almacenes de datos
- c) Un flujo entre un proceso y un almacén

**Respuesta correcta:** b) · **Referencia:** §5 [DEMARCO]

Todo flujo debe pasar por un proceso; están prohibidos los flujos directos almacén↔almacén, entidad↔entidad y entidad↔almacén.

### 41. Un proceso de un DFD que solo tiene flujos de entrada y ninguno de salida se denomina, informalmente:

- a) "Agujero negro" (error de modelado)
- b) "Milagro"
- c) Primitiva funcional

**Respuesta correcta:** a) · **Referencia:** §5 [DEMARCO]

Un proceso solo con entradas es un "agujero negro"; solo con salidas, un "milagro". Todo proceso debe tener al menos una entrada y una salida.

### 42. El diagrama de contexto (nivel 0) de un DFD se caracteriza por:

- a) Mostrar todos los procesos elementales del sistema
- b) Detallar la lógica interna de cada proceso
- c) Contener un único proceso que representa todo el sistema, sin almacenes visibles

**Respuesta correcta:** c) · **Referencia:** §6 [YOURDON]

El diagrama de contexto (nivel 0) tiene una sola burbuja rodeada de entidades externas y define el alcance del sistema.

### 43. La descomposición de un DFD por niveles es un proceso:

- a) Descendente (top-down), explotando cada proceso en otro más detallado
- b) Ascendente (bottom-up), de las primitivas al contexto
- c) Horizontal, sin jerarquía

**Respuesta correcta:** a) · **Referencia:** §6 [DEMARCO]

Se parte del contexto y se explota cada proceso (1 → 1.1, 1.2…) hasta llegar a primitivas funcionales.

### 44. Un proceso de un DFD que ya no se descompone más se denomina:

- a) Primitiva funcional
- b) Entidad externa
- c) Diagrama de contexto

**Respuesta correcta:** a) · **Referencia:** §6 [DEMARCO]

La primitiva funcional es el proceso elemental que ya no se descompone y se describe con una mini-spec.

### 45. La regla de equilibrado (balanceo) entre niveles de un DFD exige que:

- a) Los flujos de entrada/salida de un proceso coincidan con los flujos frontera de su diagrama hijo
- b) Todos los procesos tengan el mismo número de flujos
- c) Cada nivel tenga el mismo número de procesos

**Respuesta correcta:** a) · **Referencia:** §6 [DEMARCO]

El equilibrado garantiza la coherencia: lo que entra y sale del proceso padre debe cruzar la frontera de su explosión.

### 46. El diccionario de datos de un análisis estructurado sirve para:

- a) Describir la lógica de los procesos primitivos
- b) Dibujar las cardinalidades del modelo E-R
- c) Definir rigurosamente cada flujo, almacén y dato elemental del DFD

**Respuesta correcta:** c) · **Referencia:** §4.2 [DEMARCO]

El diccionario de datos define los datos con notación `= + { } [ ] ( )`; la lógica de procesos la describe la mini-spec.

### 47. En la notación del diccionario de datos, las llaves { } indican:

- a) Iteración/repetición
- b) Selección/alternativa
- c) Dato opcional

**Respuesta correcta:** a) · **Referencia:** §4.2 [DEMARCO]

`{ }` = iteración; `[ | ]` = selección; `( )` = opcional; `+` = concatenación; `=` = se compone de.

### 48. La especificación de procesos (mini-spec o P-SPEC) describe:

- a) La estructura de los datos almacenados
- b) Las entidades externas del sistema
- c) La lógica de los procesos primitivos (con pseudocódigo o tablas de decisión)

**Respuesta correcta:** c) · **Referencia:** §4.2 [DEMARCO]

La mini-spec detalla cómo funciona cada proceso que ya no se descompone; aquí enlaza con los flujogramas.

### 49. ¿Qué notación de DFD dibuja los procesos como círculos (burbujas)?

- a) Yourdon/DeMarco
- b) Gane/Sarson
- c) Crow's foot (pata de gallo)

**Respuesta correcta:** a) · **Referencia:** §4.3 [GANE-SARSON]

Yourdon/DeMarco usa círculos; Gane/Sarson usa rectángulos de esquinas redondeadas. La pata de gallo es notación E-R, no DFD.

### 50. El equivalente UML del DFD/flujograma es, aproximadamente:

- a) El diagrama de actividad
- b) El diagrama de clases
- c) El diagrama de estados

**Respuesta correcta:** a) · **Referencia:** §4.3 [UML]

El diagrama de actividad UML cubre el flujo de control y de objetos, papel parcialmente análogo al DFD y al flujograma.

### 51. La principal diferencia entre un DFD y un flujograma es que:

- a) El DFD muestra el flujo de control (orden y decisiones) y el flujograma, el flujo de datos
- b) El flujograma muestra el flujo de control y el DFD, el flujo de datos sin secuencia temporal
- c) Son notaciones idénticas con distinto nombre

**Respuesta correcta:** b) · **Referencia:** §7.1 [ISO5807]

El DFD modela transformaciones de datos; el flujograma, la secuencia y las decisiones (control).

### 52. ¿Qué norma internacional normaliza los símbolos de los diagramas de flujo?

- a) ISO 9001
- b) ISO/IEC 27001
- c) ISO 5807:1985

**Respuesta correcta:** c) · **Referencia:** §7.2 [ISO5807]

ISO 5807 (heredera de ANSI X3.5) normaliza los símbolos de los flujogramas.

### 53. En un flujograma, el símbolo de decisión (bifurcación según condición) es:

- a) Un rectángulo
- b) Un rombo
- c) Un óvalo

**Respuesta correcta:** b) · **Referencia:** §7.2 [ISO5807]

El rombo representa la decisión y es el único símbolo con varias salidas (las ramas de la condición). El rectángulo es proceso; el óvalo, terminal.

### 54. El símbolo de terminal (inicio/fin) de un flujograma es:

- a) Un paralelogramo (romboide)
- b) Un óvalo o rectángulo redondeado
- c) Un rombo

**Respuesta correcta:** b) · **Referencia:** §7.2 [ISO5807]

El terminal (inicio/fin) es un óvalo; el romboide es entrada/salida; el rombo, decisión.

### 55. El símbolo romboide (paralelogramo) en un flujograma representa:

- a) Una decisión
- b) Una operación de entrada/salida de datos
- c) El inicio del proceso

**Respuesta correcta:** b) · **Referencia:** §7.2 [ISO5807]

El romboide es E/S (lectura/escritura). La decisión es el rombo; el inicio, el óvalo terminal.

### 56. El teorema de Böhm-Jacopini establece que todo algoritmo puede expresarse con:

- a) Únicamente secuencia y saltos goto
- b) Secuencia, selección e iteración, sin saltos incondicionales (goto)
- c) Recursividad y punteros

**Respuesta correcta:** b) · **Referencia:** §7.3 [BOHM-JACOPINI]

Es el fundamento de la programación estructurada: tres estructuras de control bastan, sin goto.

### 57. La diferencia entre el bucle "mientras" (while) y "repetir-hasta" (do-until) es:

- a) "Mientras" comprueba la condición antes (0 o más veces); "repetir-hasta", después (1 o más veces)
- b) "Mientras" comprueba la condición después; "repetir-hasta", antes
- c) Ambos comprueban la condición exactamente igual

**Respuesta correcta:** a) · **Referencia:** §7.3 [BOHM-JACOPINI]

El while puede no ejecutar el cuerpo ninguna vez; el do-until lo ejecuta al menos una.

### 58. En la terminología española de diagramas, un "ordinograma" es:

- a) El diagrama de alto nivel de los módulos del sistema
- b) El diagrama de flujo detallado de la lógica de un programa
- c) El organigrama de cargos de la organización

**Respuesta correcta:** b) · **Referencia:** §7.5 [METRICA3]

El ordinograma es el flujograma de detalle; el organigrama (de proceso) es la visión de conjunto de los módulos.

### 59. ¿A qué familia de diagramas UML pertenece el diagrama de clases?

- a) Diagramas de comportamiento
- b) Diagramas de estructura
- c) Diagramas de interacción

**Respuesta correcta:** b) · **Referencia:** §7.6 [UML]

El diagrama de clases es de estructura (vista estática) y es el equivalente moderno del modelo E-R. Casos de uso, actividad, estados y secuencia son de comportamiento.

### 60. ¿Cuál es el equivalente UML del modelo Entidad-Relación?

- a) El diagrama de casos de uso
- b) El diagrama de actividad
- c) El diagrama de clases

**Respuesta correcta:** c) · **Referencia:** §7.6 [UML]

El diagrama de clases (estructura) es el equivalente del E-R: clases ↔ entidades, asociaciones ↔ relaciones, multiplicidad ↔ cardinalidad.

## Preguntas sobre los casos prácticos

### Caso 1. Modelo conceptual (E-R) del Padrón Municipal de Habitantes

#### 1. En el modelo conceptual del Padrón, ¿cuál es el identificador de HABITANTE y cómo se representa en notación de Chen?

- a) El nombre_completo, con una elipse doble.
- b) El DNI/NIE, con una elipse discontinua.
- c) El DNI/NIE, con su elipse subrayada.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.3

El identificador (clave) es el atributo cuyo valor distingue cada ocurrencia —aquí, el DNI/NIE— y en Chen se subraya. La elipse doble es del multivaluado y la discontinua, del derivado.

#### 2. Cada habitante puede facilitar uno o varios teléfonos de contacto. ¿Cómo se clasifica el atributo teléfono?

- a) Como compuesto, dibujado con elipses hijas.
- b) Como multivaluado, dibujado con elipse doble.
- c) Como derivado, dibujado con elipse discontinua.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.3

Un atributo multivaluado puede tomar varios valores para una misma ocurrencia, como los varios teléfonos de un habitante; en Chen se dibuja con elipse doble.

#### 3. El Servicio de Estadística quiere conocer también la edad de cada habitante. ¿Cómo debe tratarse en el modelo?

- a) Como atributo derivado de fecha_nacimiento, que se calcula y no se almacena.
- b) Como atributo almacenado, que se guarda junto a la fecha de nacimiento.
- c) Como atributo multivaluado, porque su valor va cambiando cada año.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.3

La edad se obtiene a partir de la fecha de nacimiento: es un atributo derivado (calculado), que no se almacena.

#### 4. El nombre y los apellidos del habitante se agrupan en el atributo nombre_completo. ¿De qué tipo de atributo se trata?

- a) Multivaluado, porque admite varios valores para el mismo habitante.
- b) Compuesto, porque se descompone en partes con significado propio.
- c) Identificador, porque distingue a cada habitante de los demás.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.3

Un atributo compuesto se descompone en partes con significado propio, como nombre y apellidos; el identificador del habitante es el DNI/NIE.

#### 5. ¿Qué cardinalidad máxima tiene la relación EMPADRONADO_EN entre HABITANTE y VIVIENDA?

- a) N:M: un habitante puede estar empadronado en varias viviendas a la vez.
- b) 1:1: cada vivienda tiene empadronado un único habitante y viceversa.
- c) 1:N: una vivienda tiene muchos habitantes y cada habitante, una sola vivienda.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.4

Cada habitante está empadronado en una vivienda y en una vivienda pueden estarlo varios habitantes: una ocurrencia de VIVIENDA se asocia con varias de HABITANTE, y cada HABITANTE con una sola VIVIENDA.

#### 6. ¿Cómo se caracteriza la relación PERTENECE entre VIVIENDA y DISTRITO?

- a) Binaria y 1:N: un distrito agrupa muchas viviendas.
- b) Binaria y N:M: una vivienda está en varios distritos.
- c) Ternaria y 1:N, pues también interviene HABITANTE.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §2.4

Participan dos tipos de entidad (grado binario) y cada vivienda pertenece a un distrito, mientras que un distrito agrupa muchas viviendas: 1:N.

#### 7. «Todo habitante debe estar empadronado en una vivienda; una vivienda puede no tener a nadie empadronado». ¿Qué participación tiene cada entidad en EMPADRONADO_EN?

- a) HABITANTE, parcial; VIVIENDA, total.
- b) Total en ambas entidades.
- c) HABITANTE, total; VIVIENDA, parcial.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §2.4

La participación es total cuando toda ocurrencia debe participar (mínimo 1), como el habitante; es parcial cuando alguna puede no hacerlo (mínimo 0), como la vivienda vacía.

#### 8. La fecha de alta en el padrón solo tiene sentido para la pareja habitante-vivienda. ¿Dónde se coloca en el modelo E-R?

- a) Como atributo de la entidad VIVIENDA.
- b) Como atributo de la relación EMPADRONADO_EN.
- c) Como una entidad propia, FECHA_ALTA.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.4, §3.1

Un atributo que solo tiene sentido para la combinación de dos entidades pertenece a la relación; las relaciones pueden tener atributos propios.

#### 9. Al pasar EMPADRONADO_EN al modelo relacional, ¿cómo se transforma?

- a) La clave de VIVIENDA pasa como clave ajena a la tabla HABITANTE, junto con fecha_alta.
- b) La clave de HABITANTE pasa como clave ajena a la tabla VIVIENDA, junto con fecha_alta.
- c) Se crea la tabla HABITANTE_VIVIENDA con las claves de ambas y la fecha_alta.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §3.4

En una relación 1:N, la clave de la entidad del lado «1» (VIVIENDA) se propaga como clave ajena a la tabla del lado «N» (HABITANTE).

#### 10. Un compañero propone crear una tabla intermedia EMPADRONAMIENTO para esa relación. ¿Qué le responde el técnico?

- a) Que es obligatoria, porque la relación tiene un atributo propio.
- b) Que es obligatoria, porque VIVIENDA tiene participación parcial.
- c) Que no hace falta: la tabla intermedia es propia de las relaciones N:M.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 4 · §3.4

La tabla intermedia, con la combinación de las claves de ambas entidades, es la regla de transformación de las relaciones N:M; en una 1:N basta propagar la clave ajena al lado «N».

### Caso 2. Diagrama de flujo de datos (DFD) de la gestión de una tasa municipal

#### 1. En el diagrama de contexto (nivel 0) del sistema de la tasa de vado, ¿qué se representa?

- a) Una sola burbuja para todo el sistema, sin almacenes visibles.
- b) Los tres procesos principales y los almacenes D1 y D2.
- c) Una sola burbuja, con los almacenes D1 y D2 a su lado.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §6

El nivel 0 tiene un único proceso que representa todo el sistema, rodeado de las entidades externas y los flujos de frontera, y no muestra almacenes.

#### 2. ¿Qué entidades externas aparecen en ese diagrama de contexto?

- a) CONTRIBUYENTE, ENTIDAD_BANCARIA y D1 Liquidaciones.
- b) Solo CONTRIBUYENTE; el banco es un almacén de cobros.
- c) CONTRIBUYENTE y ENTIDAD_BANCARIA.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §4.1

Las entidades externas son personas, organizaciones u otros sistemas que producen o consumen datos: el contribuyente y el banco. D1 es un almacén interno.

#### 3. ¿Cuáles son los flujos que cruzan la frontera del sistema en el diagrama de contexto?

- a) Solicitud_válida y liquidación, entre los procesos 1 y 2.
- b) Solicitud y recibo, con el contribuyente; cobro, con el banco.
- c) Datos_cobro hacia D2 y liquidación hacia D1.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §6

Los flujos de frontera conectan el sistema con sus entidades externas; solicitud_válida, liquidación o datos_cobro son flujos internos que solo aparecen al descomponer.

#### 4. En el DFD de nivel 1, ¿qué nombres de procesos siguen las reglas de construcción?

- a) «1 Validar solicitud», «2 Liquidar tasa» y «3 Registrar cobro».
- b) «1 Solicitud», «2 Liquidación» y «3 Cobro».
- c) «D1 Validar solicitud», «D2 Liquidar tasa» y «D3 Registrar cobro».

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §4.1, §5

Los procesos se numeran (1, 2, 3…) y se nombran con verbo + objeto; los sustantivos son para flujos y almacenes, y la numeración D1, D2… es la de los almacenes.

#### 5. En el nivel 1, ¿qué procesos escriben y leen el almacén D1 Liquidaciones?

- a) Lo escribe «1 Validar solicitud» y lo lee «2 Liquidar tasa».
- b) Lo escribe «2 Liquidar tasa» y lo lee «3 Registrar cobro».
- c) Lo escribe la ENTIDAD_BANCARIA y lo lee «3 Registrar cobro».

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.1

La liquidación calculada se guarda en D1 y el registro del cobro la consulta para marcarla como pagada; una entidad externa nunca escribe directamente en un almacén.

#### 6. Un analista propone que la entidad bancaria grabe el cobro directamente en el almacén D2 Cobros. ¿Es correcto?

- a) Sí: el banco es una entidad de confianza y puede escribir en el almacén.
- b) Sí, siempre que el almacén esté numerado como D2 en el diagrama.
- c) No: entre una entidad externa y un almacén siempre debe mediar un proceso.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §5

Están prohibidos los flujos directos entre una entidad externa y un almacén: todo dato debe pasar por un proceso, aquí «3 Registrar cobro».

#### 7. Si «3 Registrar cobro» recibiera el cobro del banco pero no generase ninguna salida, ¿qué error de modelado tendría?

- a) Un «agujero negro», porque solo tiene flujos de entrada.
- b) Un «milagro», porque no deriva sus salidas de las entradas.
- c) Un desequilibrio entre el nivel 1 y el diagrama de contexto.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §5

Todo proceso debe tener al menos una entrada y una salida: solo con entradas es un «agujero negro»; solo con salidas, un «milagro».

#### 8. ¿Refleja el DFD del vado el orden temporal en que se valida, se liquida y se cobra?

- a) Sí: la numeración 1, 2, 3 indica el orden de ejecución de los procesos.
- b) No: el DFD modela qué se transforma, no la secuencia ni las decisiones.
- c) Sí: cada flecha del DFD indica qué proceso se ejecuta a continuación.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.1, §7.1

El DFD modela función, no secuencia temporal ni decisiones; eso es propio del flujograma. La numeración sirve para la descomposición jerárquica.

#### 9. Al explotar «2 Liquidar tasa» en 2.1, 2.2 y 2.3, ¿qué flujos deben cruzar la frontera del diagrama hijo?

- a) Entra la solicitud del contribuyente y sale el cobro hacia D2.
- b) Los del padre más los nuevos que hagan falta para detallar el cálculo.
- c) Entra solicitud_válida y salen la liquidación (a D1) y el recibo.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §6

Por el equilibrado (balanceo), los flujos de entrada y salida del proceso padre deben coincidir exactamente con los que cruzan la frontera de su diagrama hijo.

#### 10. En la explosión de «2 Liquidar tasa» aparece una salida nueva que no tenía el proceso 2 en el nivel 1. ¿Qué ocurre?

- a) Es correcto, porque los niveles inferiores añaden detalle.
- b) El DFD queda desequilibrado: incumple la regla de balanceo.
- c) Es correcto si el subproceso es una primitiva funcional.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §6

El balanceo exige que el hijo tenga exactamente los flujos de entrada y salida del padre; un flujo nuevo en la frontera rompe la coherencia entre niveles.

### Caso 3. Modelado dinámico (DTE) y flujograma del trámite de una licencia en la sede electrónica

#### 1. En el DTE de la licencia urbanística, ¿cuál es el estado inicial y cuál el estado final?

- a) Inicial: EN TRAMITACIÓN (tras la admisión); final: RESUELTA.
- b) Inicial: INICIADA (desde el pseudoestado inicial); final: ARCHIVADA.
- c) Inicial: INICIADA (al presentarse); final: RESUELTA.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §8.1

La licencia nace INICIADA al presentarse la solicitud y, tras la notificación, queda ARCHIVADA como estado final; RESUELTA todavía tiene una transición de salida.

#### 2. Durante la tramitación se detecta que falta documentación. ¿Qué evento lleva la licencia de EN TRAMITACIÓN a SUBSANACIÓN?

- a) Requerir.
- b) Subsanar.
- c) Resolver.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §8.1

El evento es el estímulo que dispara la transición: al requerir la documentación que falta, la licencia pasa a SUBSANACIÓN; subsanar es el evento de vuelta.

#### 3. ¿Qué etiqueta sigue el patrón correcto para la transición de SUBSANACIÓN a EN TRAMITACIÓN?

- a) aceptar documentación [subsanar] / dentro de plazo
- b) dentro de plazo / subsanar [aceptar documentación]
- c) subsanar [dentro de plazo] / aceptar documentación

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §8.1

La etiqueta de una transición sigue el patrón evento [condición] / acción: el evento (subsanar), la guarda entre corchetes y, tras la barra, la acción.

#### 4. En la etiqueta «requerir [falta documentación] / registrar requerimiento», ¿qué es «falta documentación»?

- a) El evento que dispara la transición.
- b) La acción que se ejecuta al transitar.
- c) La condición (guarda) que debe cumplirse.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §8.1

La condición o guarda es el predicado que debe cumplirse para que la transición ocurra y se escribe entre corchetes.

#### 5. ¿Puede la licencia estar a la vez en EN TRAMITACIÓN y en SUBSANACIÓN?

- a) No: en un DTE los estados son mutuamente excluyentes.
- b) Sí, si ambos estados comparten el mismo evento de salida.
- c) Sí, porque un DTE admite varios estados iniciales.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §8.2

Los estados deben ser mutuamente excluyentes: el sistema está en uno y solo uno en cada instante; además, el DTE tiene un único estado inicial.

#### 6. En el flujograma «comprobar plazo de subsanación», ¿con qué símbolo se representa «Leer fecha_límite y fecha_actual»?

- a) Con un rectángulo, de proceso u operación.
- b) Con un romboide (paralelogramo), de entrada/salida.
- c) Con un rombo, símbolo de las decisiones.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §7.2

La lectura o escritura de datos se representa con el romboide (paralelogramo); el rectángulo es para las operaciones y el rombo para las decisiones.

#### 7. ¿Con qué símbolo se representa la pregunta «¿fecha_actual > fecha_límite?»?

- a) Con un rombo, del que salen las ramas Sí y No.
- b) Con un romboide, del que salen los datos leídos.
- c) Con un rectángulo con doble borde lateral.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §7.2, §7.4

La bifurcación según una condición se representa con un rombo, el único símbolo del que salen dos o más líneas etiquetadas; el doble borde lateral indica una subrutina.

#### 8. Si la fecha actual es posterior a la fecha límite, ¿qué hace el flujograma?

- a) Sigue la rama No y admite la documentación subsanada.
- b) Vuelve a leer las fechas hasta que estén dentro de plazo.
- c) Sigue la rama Sí y marca la solicitud como CADUCADA.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3

Si la fecha actual es posterior a la límite, el plazo ha vencido: la rama Sí lleva al proceso que declara la solicitud caducada; en caso contrario se admite la documentación.

#### 9. ¿Cómo debe terminar el flujograma después de las dos ramas?

- a) Cada rama acaba en un rombo de cierre propio.
- b) Ambas ramas confluyen en un único terminal de fin (óvalo).
- c) La rama de caducidad puede quedar sin terminal de fin.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §7.2, §7.4

El flujograma tiene un único inicio y, preferiblemente, un único fin, representado con el terminal (óvalo); ningún camino puede quedar «perdido».

#### 10. ¿Qué estructura de control emplea el flujograma «comprobar plazo de subsanación»?

- a) Selección (si-entonces-si_no), con un solo rombo y dos ramas excluyentes.
- b) Iteración (mientras), porque repite la comprobación hasta que haya plazo.
- c) Secuencia, porque las acciones se ejecutan una tras otra sin bifurcarse.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §7.3

La selección elige una rama u otra según una condición (en el flujograma, un rombo); aquí no hay repetición ni una mera sucesión de pasos.
