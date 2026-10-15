# Test del tema 17. Diseño de bases de datos y normalización

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-17.html>

## Batería de preguntas

### 1. ¿Cuál es el orden correcto de los tres niveles de diseño de una base de datos?

- a) Físico → lógico → conceptual
- b) Conceptual → lógico → físico
- c) Lógico → conceptual → físico

**Respuesta correcta:** b) · **Referencia:** §1.2 [ELMASRI]

Se va de lo más abstracto (independiente del SGBD) a lo más concreto (producto y almacenamiento).

### 2. El diseño conceptual de una base de datos se caracteriza por ser:

- a) Una descripción de los ficheros físicos en disco
- b) Dependiente del producto concreto (Oracle, PostgreSQL)
- c) Independiente de cualquier SGBD

**Respuesta correcta:** c) · **Referencia:** §1.2 [ELMASRI]

El modelo conceptual (típicamente E-R) describe la realidad sin atarse a ninguna tecnología.

### 3. ¿Qué permite la independencia física de datos?

- a) Cambiar el nombre de las entidades sin más
- b) Eliminar las claves primarias
- c) Modificar el almacenamiento (índices, ficheros) sin alterar el esquema lógico ni las aplicaciones

**Respuesta correcta:** c) · **Referencia:** §1.3 [DATE]

Es la independencia más fácil de conseguir gracias a la separación en niveles.

### 4. ¿Cuál NO es un objetivo del diseño de bases de datos?

- a) Mínima redundancia controlada
- b) Maximizar deliberadamente la duplicación de datos
- c) Integridad de los datos

**Respuesta correcta:** b) · **Referencia:** §1.3 [ELMASRI]

La redundancia no controlada provoca anomalías; el diseño busca minimizarla.

### 5. El diseño lógico de una base de datos relacional produce:

- a) El conjunto de tablas con sus claves, normalizadas, independiente del producto
- b) El diagrama de despliegue de servidores
- c) El código fuente de la aplicación cliente

**Respuesta correcta:** a) · **Referencia:** §2.1 [ELMASRI]

Transforma el modelo conceptual en el modelo del tipo de SGBD elegido (relacional).

### 6. La independencia lógica de datos se apoya principalmente en:

- a) Los índices bitmap
- b) El particionamiento por rango
- c) Las vistas

**Respuesta correcta:** c) · **Referencia:** §1.3 [DATE]

Las vistas permiten cambiar el esquema lógico afectando lo mínimo a las aplicaciones que consultan a través de ellas.

### 7. ¿A qué nivel de diseño corresponde decidir el particionamiento de una tabla y sus índices?

- a) Diseño conceptual
- b) Diseño físico
- c) Análisis de requisitos

**Respuesta correcta:** b) · **Referencia:** §2.6 [RAMAKRISHNAN]

El diseño físico decide el almacenamiento y las estructuras de acceso en el producto concreto.

### 8. La arquitectura ANSI/SPARC de tres esquemas se relaciona con el diseño en niveles en que:

- a) El esquema interno equivale al diseño físico y los esquemas externos a las vistas
- b) Solo define un único esquema global
- c) Sustituye al modelo relacional

**Respuesta correcta:** a) · **Referencia:** §1.2 [SILBER]

Interno↔físico, conceptual↔lógico, externos↔vistas de usuario.

### 9. En el modelo entidad-relación, una entidad se representa gráficamente con:

- a) Un rombo
- b) Una elipse
- c) Un rectángulo

**Respuesta correcta:** c) · **Referencia:** §1.4 [CHEN76]

El rombo es la relación y la elipse el atributo.

### 10. ¿Qué representa un rombo en un diagrama E-R?

- a) Una relación (interrelación) entre entidades
- b) Un atributo
- c) Una clave primaria

**Respuesta correcta:** a) · **Referencia:** §1.4 [CHEN76]

El rombo une dos o más entidades; la cardinalidad se anota en las líneas.

### 11. Una relación 1:N entre DISTRITO y HABITANTE se transforma en el modelo relacional:

- a) Creando una tabla intermedia con dos claves ajenas
- b) Propagando la clave de DISTRITO como clave ajena en HABITANTE
- c) Fusionando ambas entidades en una sola tabla siempre

**Respuesta correcta:** b) · **Referencia:** §2.2 [ELMASRI]

En 1:N la clave del lado «1» va al lado «N»; no se crea tabla nueva.

### 12. Una relación N:M entre HABITANTE y TRIBUTO se transforma:

- a) Propagando la clave de uno en el otro
- b) Sin cambios en el esquema
- c) Creando una tabla intermedia con clave compuesta y dos claves ajenas

**Respuesta correcta:** c) · **Referencia:** §2.2 [ELMASRI]

La tabla puente almacena además los atributos propios de la relación (p. ej. porcentaje de titularidad).

### 13. Un atributo multivaluado (p. ej. varios teléfonos de un habitante) se transforma en:

- a) Una tabla aparte relacionada por clave ajena
- b) Una columna que contiene la lista separada por comas
- c) Tres columnas fijas: telefono1, telefono2, telefono3

**Respuesta correcta:** a) · **Referencia:** §2.2 [ELMASRI]

Guardar varios valores en una celda violaría la 1FN; las columnas fijas limitan artificialmente el número.

### 14. ¿Qué es una entidad débil?

- a) Una entidad con muchos atributos
- b) Una entidad que no participa en ninguna relación
- c) Una entidad sin clave propia que depende de otra entidad fuerte

**Respuesta correcta:** c) · **Referencia:** §1.4 [ELMASRI]

Su clave primaria incluye la clave de la entidad fuerte de la que depende.

### 15. La participación total de una entidad en una relación significa que:

- a) La relación es siempre N:M
- b) La entidad tiene varios atributos clave
- c) Toda ocurrencia de la entidad debe participar en la relación

**Respuesta correcta:** c) · **Referencia:** §1.4 [ELMASRI]

En el modelo lógico se traduce en una clave ajena NOT NULL.

### 16. Un atributo derivado (como la edad a partir de la fecha de nacimiento):

- a) En principio no se almacena, se calcula
- b) Debe ser siempre clave primaria
- c) Obliga a crear una tabla intermedia

**Respuesta correcta:** a) · **Referencia:** §2.2 [ELMASRI]

Almacenarlo introduce redundancia; solo se hace por desnormalización justificada.

### 17. Una relación recursiva (reflexiva) es aquella en la que:

- a) Una entidad se relaciona consigo misma
- b) Participan exactamente tres entidades
- c) No hay cardinalidad definida

**Respuesta correcta:** a) · **Referencia:** §1.4 [ELMASRI]

Ejemplo: un EMPLEADO «es jefe de» otro EMPLEADO.

### 18. Una clave subrogada (surrogate) es:

- a) Una clave ajena que admite nulos
- b) Un identificador artificial sin significado de negocio (p. ej. autonumérico)
- c) Una clave formada por todos los atributos de la tabla

**Respuesta correcta:** b) · **Referencia:** §2.5 [DATE]

Aporta estabilidad frente a las claves naturales, que pueden cambiar.

### 19. La integridad de entidad establece que:

- a) Las claves ajenas no pueden existir
- b) Toda tabla debe tener al menos 100 filas
- c) Ningún atributo de la clave primaria puede ser nulo

**Respuesta correcta:** c) · **Referencia:** §2.4 [CODD70]

Si lo fuera, no podría identificar unívocamente la fila.

### 20. La integridad referencial exige que el valor de una clave ajena:

- a) Coincida con un valor existente de la clave primaria referenciada o sea nulo
- b) Sea siempre distinto al de la clave primaria
- c) Sea único en toda la base de datos

**Respuesta correcta:** a) · **Referencia:** §2.4 [DATE]

Evita las «referencias colgantes».

### 21. ¿Qué política referencial borra automáticamente las filas hijas al borrar la fila padre?

- a) NO ACTION / RESTRICT
- b) CASCADE
- c) SET DEFAULT

**Respuesta correcta:** b) · **Referencia:** §2.4 [ISO9075]

Propaga el borrado o la actualización a las filas que referencian la fila padre.

### 22. ¿A qué sublenguaje de SQL pertenece la sentencia CREATE TABLE?

- a) DML
- b) DCL
- c) DDL

**Respuesta correcta:** c) · **Referencia:** §2.5 [ISO9075]

El DDL (Data Definition Language) define la estructura: tablas, índices, vistas y restricciones.

### 23. Las sentencias GRANT y REVOKE pertenecen a:

- a) DCL (control de acceso/permisos)
- b) DML
- c) TCL

**Respuesta correcta:** a) · **Referencia:** §2.5 [ISO9075]

El DCL controla los privilegios de usuarios y roles.

### 24. ¿Cuál de estas afirmaciones sobre DELETE y TRUNCATE es correcta?

- a) Ambas son DML y soportan WHERE
- b) TRUNCATE permite borrar filas concretas con WHERE
- c) DELETE es DML (transaccional, con WHERE) y TRUNCATE es DDL (vacía la tabla)

**Respuesta correcta:** c) · **Referencia:** §2.5 [ISO9075]

TRUNCATE es rápida y normalmente no transaccional ni filtrable.

### 25. Un índice de tipo hash es adecuado para:

- a) Búsquedas por rango (BETWEEN, &lt;, &gt;)
- b) Búsquedas por igualdad exacta
- c) Ordenar el resultado con ORDER BY

**Respuesta correcta:** b) · **Referencia:** §2.8 [RAMAKRISHNAN]

El hash no soporta rangos ni orden; para eso se usa el B+tree.

### 26. ¿Qué ventaja tiene el índice B+tree que no tiene el hash?

- a) Sirve para búsquedas por igualdad y también por rango y orden
- b) Ocupa menos espacio siempre
- c) No necesita mantenerse al insertar

**Respuesta correcta:** a) · **Referencia:** §2.8 [RAMAKRISHNAN]

Sus hojas están al mismo nivel y enlazadas, lo que facilita los recorridos por rango.

### 27. Crear muchos índices sobre una tabla:

- a) Siempre mejora el rendimiento global
- b) No tiene ningún efecto secundario
- c) Acelera lecturas pero penaliza escrituras y consume espacio

**Respuesta correcta:** c) · **Referencia:** §2.8 [RAMAKRISHNAN]

Cada índice debe mantenerse en cada INSERT/UPDATE/DELETE.

### 28. El índice bitmap es especialmente eficiente en columnas:

- a) De muy alta cardinalidad (como el DNI)
- b) De baja cardinalidad (como el sexo o el distrito) en entornos analíticos
- c) De tipo BLOB

**Respuesta correcta:** b) · **Referencia:** §2.8 [ORA-CONCEPTS]

Penaliza la concurrencia de escrituras, por eso es típico de OLAP.

### 29. Un índice agrupado (clustered):

- a) Puede haber tantos como se quiera por tabla
- b) Determina el orden físico de las filas y solo puede haber uno por tabla
- c) No tiene relación con el orden de las filas

**Respuesta correcta:** b) · **Referencia:** §2.8 [MS-SQL-INDEX]

A menudo coincide con la clave primaria.

### 30. El plan de ejecución de una consulta es:

- a) La ruta de operaciones físicas que el optimizador elige para resolverla
- b) El texto literal de la sentencia SQL
- c) La lista de usuarios con permiso sobre la tabla

**Respuesta correcta:** a) · **Referencia:** §2.9 [SILBER]

Se inspecciona con EXPLAIN y depende de las estadísticas.

### 31. En el modelo relacional, el grado de una relación es:

- a) El número de tuplas (filas)
- b) El número de atributos (columnas)
- c) El número de claves ajenas

**Respuesta correcta:** b) · **Referencia:** §3.1 [DATE]

La cardinalidad, en cambio, es el número de filas.

### 32. La cardinalidad de una relación se refiere a:

- a) El número de tuplas (filas)
- b) El número de columnas
- c) El número de dominios definidos

**Respuesta correcta:** a) · **Referencia:** §3.1 [DATE]

Grado = columnas; cardinalidad = filas.

### 33. El dominio de un atributo es:

- a) El nombre de la tabla
- b) La clave primaria de la relación
- c) El conjunto de valores válidos que puede tomar el atributo

**Respuesta correcta:** c) · **Referencia:** §3.1 [DATE]

Por ejemplo, el dominio de «distrito» son los códigos 1..21.

### 34. ¿Qué diferencia hay entre una relación teórica y una tabla SQL?

- a) Ninguna, son idénticas
- b) La tabla SQL no admite claves
- c) La relación teórica es un conjunto (sin duplicados); la tabla SQL es un multiconjunto (permite filas repetidas salvo restricción)

**Respuesta correcta:** c) · **Referencia:** §3.1 [DATE]

Por eso SELECT puede devolver duplicados salvo DISTINCT.

### 35. Una superclave es:

- a) Un conjunto de atributos que identifica unívocamente una tupla (puede no ser mínimo)
- b) Siempre un único atributo
- c) Una clave que apunta a otra tabla

**Respuesta correcta:** a) · **Referencia:** §3.2 [DATE]

La clave candidata es la superclave mínima.

### 36. Una clave candidata es:

- a) Cualquier columna de la tabla
- b) Una superclave mínima (si se le quita un atributo deja de identificar)
- c) La clave que se descarta del diseño

**Respuesta correcta:** b) · **Referencia:** §3.2 [ELMASRI]

De entre las candidatas, la elegida es la primaria; las demás, alternativas.

### 37. Las claves candidatas no elegidas como primaria se denominan:

- a) Claves alternativas
- b) Claves ajenas
- c) Superclaves

**Respuesta correcta:** a) · **Referencia:** §3.2 [DATE]

Suelen implementarse con una restricción UNIQUE.

### 38. En la relación HABITANTE(dni, nss, nombre), si elegimos dni como primaria, el NSS es:

- a) Una clave ajena
- b) Un atributo no clave cualquiera
- c) Una clave alternativa (candidata no elegida)

**Respuesta correcta:** c) · **Referencia:** §3.2 [DATE]

El NSS también identifica unívocamente, pero no fue elegido como primaria.

### 39. El valor NULL en el modelo relacional representa:

- a) El número cero
- b) Información ausente o desconocida
- c) Una cadena vacía

**Respuesta correcta:** b) · **Referencia:** §3.3 [DATE]

No es cero ni cadena vacía, e introduce una lógica de tres valores.

### 40. ¿Cuál de estas es una regla de integridad del modelo relacional?

- a) Toda tabla debe tener exactamente una clave ajena
- b) Los nombres de columna deben ir en mayúsculas
- c) La integridad referencial: toda clave ajena referencia una fila existente o es nula

**Respuesta correcta:** c) · **Referencia:** §3.3 [CODD70]

Junto con la integridad de entidad, de dominio y las reglas de negocio.

### 41. El álgebra relacional es un lenguaje:

- a) Procedimental (indica cómo obtener el resultado paso a paso)
- b) Declarativo puro (solo indica qué se quiere)
- c) De definición de estructura (DDL)

**Respuesta correcta:** a) · **Referencia:** §3.4 [DATE]

El cálculo relacional, en cambio, es declarativo.

### 42. La operación de selección (σ) del álgebra relacional:

- a) Elige columnas
- b) Filtra las filas que cumplen una condición
- c) Une dos tablas

**Respuesta correcta:** b) · **Referencia:** §3.4 [ELMASRI]

La proyección (π) es la que elige columnas.

### 43. La operación de proyección (π) del álgebra relacional:

- a) Selecciona columnas (atributos), eliminando duplicados
- b) Filtra filas según una condición
- c) Calcula el producto cartesiano

**Respuesta correcta:** a) · **Referencia:** §3.4 [ELMASRI]

No confundir con la selección σ, que filtra filas.

### 44. ¿Cuáles son los cinco operadores primitivos del álgebra relacional?

- a) Join, intersección, división, unión y selección
- b) Selección, proyección, unión, diferencia y producto cartesiano
- c) Selección, proyección, join, división y renombrado

**Respuesta correcta:** b) · **Referencia:** §3.4 [CODD70]

El join, la intersección y la división se derivan de estos cinco.

### 45. La operación de división (÷) resuelve consultas del tipo:

- a) «cuántas filas tiene la tabla»
- b) «cuál es el valor máximo de una columna»
- c) «qué elementos están relacionados con TODOS los de otro conjunto»

**Respuesta correcta:** c) · **Referencia:** §3.4 [DATE]

Por ejemplo, qué habitantes han pagado todos los tributos obligatorios.

### 46. El cálculo relacional es un lenguaje:

- a) Declarativo (describe qué se quiere, no cómo obtenerlo)
- b) Procedimental
- c) De control de transacciones

**Respuesta correcta:** a) · **Referencia:** §3.5 [DATE]

Tiene dos variantes: de tuplas y de dominios.

### 47. Respecto al poder expresivo, el álgebra relacional y el cálculo relacional:

- a) El álgebra es más potente que el cálculo
- b) El cálculo es más potente que el álgebra
- c) Son equivalentes (mismo poder expresivo)

**Respuesta correcta:** c) · **Referencia:** §3.5 [DATE]

Es el teorema de equivalencia de Codd; SQL se inspira en ambos.

### 48. La normalización tiene como objetivo principal:

- a) Aumentar la velocidad de todas las consultas
- b) Eliminar la redundancia y las anomalías de actualización
- c) Reducir el número de tablas al mínimo

**Respuesta correcta:** b) · **Referencia:** §4.1 [CODD72]

Se basa en el análisis de las dependencias funcionales.

### 49. ¿Cuáles son las tres anomalías que provoca un mal diseño?

- a) De compilación, de ejecución y de sintaxis
- b) De inserción, de borrado y de actualización
- c) De red, de disco y de memoria

**Respuesta correcta:** b) · **Referencia:** §4.1 [ELMASRI]

Las tres derivan de la redundancia de datos.

### 50. Una dependencia funcional X → Y significa que:

- a) Y siempre es mayor que X
- b) X e Y son claves ajenas
- c) El valor de X determina unívocamente el valor de Y

**Respuesta correcta:** c) · **Referencia:** §4.2 [ELMASRI]

X es el determinante; dos tuplas con igual X tienen igual Y.

### 51. ¿Cuáles son los tres axiomas de Armstrong?

- a) Reflexividad, aumento y transitividad
- b) Unión, descomposición y pseudotransitividad
- c) Inserción, borrado y actualización

**Respuesta correcta:** a) · **Referencia:** §4.2 [ARMSTRONG74]

Son correctos y completos; las demás reglas se derivan de ellos.

### 52. El cierre de atributos X⁺ sirve para:

- a) Ordenar las filas de una tabla
- b) Determinar si X es superclave y hallar las claves candidatas
- c) Calcular el tamaño físico de la tabla

**Respuesta correcta:** b) · **Referencia:** §4.2 [ELMASRI]

Si X⁺ contiene todos los atributos, X es superclave.

### 53. Una relación está en Primera Forma Normal (1FN) cuando:

- a) No tiene claves ajenas
- b) Todos sus atributos son atómicos (un solo valor por celda)
- c) Tiene menos de cinco columnas

**Respuesta correcta:** b) · **Referencia:** §4.3 [CODD70]

Sin grupos repetitivos ni valores multivaluados.

### 54. La Segunda Forma Normal (2FN) elimina:

- a) Las dependencias transitivas
- b) Las dependencias multivaluadas
- c) Las dependencias funcionales parciales de la clave

**Respuesta correcta:** c) · **Referencia:** §4.4 [CODD72]

Solo tiene riesgo cuando la clave primaria es compuesta.

### 55. Si la clave primaria de una relación en 1FN es un único atributo, entonces:

- a) Está automáticamente en 2FN
- b) Nunca puede estar en 3FN
- c) No puede tener claves ajenas

**Respuesta correcta:** a) · **Referencia:** §4.4 [CODD72]

Sin clave compuesta no puede haber dependencias parciales.

### 56. La Tercera Forma Normal (3FN) exige que no haya:

- a) Dependencias transitivas entre atributos no clave
- b) Claves primarias
- c) Valores nulos en ninguna columna

**Respuesta correcta:** a) · **Referencia:** §4.5 [CODD72]

Mnemotecnia: cada atributo depende de la clave, toda la clave y nada más que la clave.

### 57. La Forma Normal de Boyce-Codd (BCNF) exige que:

- a) Toda tabla tenga clave subrogada
- b) Todo determinante de una dependencia funcional no trivial sea clave candidata
- c) No existan claves ajenas

**Respuesta correcta:** b) · **Referencia:** §4.6 [CODD74BCNF]

Es una 3FN reforzada; toda relación en BCNF está en 3FN.

### 58. ¿Qué propiedad de una descomposición es obligatoria?

- a) Que aumente el número de tablas
- b) La descomposición sin pérdida de información (lossless join)
- c) Que elimine todas las claves ajenas

**Respuesta correcta:** b) · **Referencia:** §4.6 [SILBER]

Se garantiza si el atributo común es clave de al menos una de las tablas resultantes.

### 59. La Cuarta Forma Normal (4FN) trata las dependencias:

- a) Funcionales parciales
- b) Transitivas
- c) Multivaluadas

**Respuesta correcta:** c) · **Referencia:** §4.7 [FAGIN77]

La 5FN, por su parte, trata las dependencias de reunión (join).

### 60. La desnormalización controlada consiste en:

- a) Reintroducir redundancia de forma deliberada para mejorar el rendimiento, asumiendo el coste de mantener la coherencia
- b) Eliminar todas las claves primarias
- c) Volver siempre a la 1FN

**Respuesta correcta:** a) · **Referencia:** §4.8 [RAMAKRISHNAN]

Se aplica al final, sobre cuellos de botella medidos, típica en entornos OLAP.

## Preguntas sobre los casos prácticos

### Caso 1. Diseño lógico del registro de expedientes

#### 1. En el supuesto del registro de expedientes, ¿qué entidades deben identificarse?

- a) PROCEDIMIENTO, EXPEDIENTE, INTERESADO y UNIDAD.
- b) EXPEDIENTE, INTERESADO y UNIDAD; el procedimiento es solo un atributo del expediente.
- c) EXPEDIENTE, CIUDADANO, FECHA_APERTURA y UNIDAD.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §1.4

Son objetos con existencia propia sobre los que se guardan datos: el procedimiento tiene su propio código y denominación, y la fecha de apertura es un atributo del expediente.

#### 2. ¿Qué clave primaria corresponde a la tabla EXPEDIENTE?

- a) fecha_apertura.
- b) La combinación (num_exp, cod_proc).
- c) num_exp.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §3.2

El número identifica cada expediente. (num_exp, cod_proc) también identifica, pero no es mínima: es una superclave, no una clave candidata.

#### 3. ¿Cómo se representa en el modelo relacional la relación «una unidad tramita muchos expedientes»?

- a) Con num_exp como clave ajena en UNIDAD, sin crear tabla nueva.
- b) Con cod_unidad como clave ajena en EXPEDIENTE, sin crear tabla nueva.
- c) Con una tabla intermedia UNIDAD_EXPEDIENTE con ambas claves.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.2

En una relación 1:N, la clave de la entidad del lado «1» (UNIDAD) se propaga como clave ajena en la tabla del lado «N» (EXPEDIENTE); la tabla intermedia es para las N:M.

#### 4. Teniendo en cuenta sus relaciones 1:N, ¿cómo queda la tabla EXPEDIENTE?

- a) EXPEDIENTE(num_exp PK, fecha_apertura, dni FK, cod_unidad FK).
- b) EXPEDIENTE(num_exp, cod_unidad PK, fecha_apertura, cod_proc FK).
- c) EXPEDIENTE(num_exp PK, fecha_apertura, cod_proc FK, cod_unidad FK).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.2

Recibe como claves ajenas las de PROCEDIMIENTO y UNIDAD (lados «1»). El DNI no puede ir en EXPEDIENTE, porque con interesados es N:M y un expediente tiene varios.

#### 5. La relación entre EXPEDIENTE e INTERESADO es N:M. ¿Cuál es la solución relacional correcta?

- a) Una tabla INTERVENCION(num_exp, dni, rol) con PK(num_exp, dni) y dos claves ajenas.
- b) Añadir dni como clave ajena en EXPEDIENTE para enlazar con el interesado.
- c) Una tabla INTERVENCION(num_exp, dni, rol) con PK(num_exp) y dni como clave ajena.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §2.2

La N:M se resuelve con una tabla intermedia cuya clave primaria combina las claves de ambas entidades, con una clave ajena hacia cada una; con PK(num_exp) un expediente solo podría tener un interesado.

#### 6. En cada expediente, el ciudadano interviene como titular o como representante. ¿Dónde se guarda ese rol?

- a) En la tabla INTERESADO, como atributo del ciudadano.
- b) En la tabla intermedia INTERVENCION, como atributo de la relación.
- c) En la tabla EXPEDIENTE, como atributo del expediente.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §2.2

El rol depende de la pareja expediente-ciudadano (el mismo ciudadano puede ser titular en uno y representante en otro): es propio de la relación y vive en la tabla intermedia.

#### 7. ¿Qué regla de integridad garantiza que no exista ningún expediente sin número?

- a) La integridad de entidad, porque num_exp es la clave primaria.
- b) La integridad referencial, porque num_exp se referencia desde INTERVENCION.
- c) La integridad de dominio, porque num_exp tiene un formato definido.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §2.4

La integridad de entidad prohíbe que un atributo de la clave primaria tome valor nulo: si fuese nula, no podría identificar la fila.

#### 8. ¿Qué regla impide asignar un expediente a una unidad tramitadora que no existe?

- a) La integridad de entidad sobre la columna cod_unidad.
- b) Una restricción UNIQUE sobre cod_unidad en EXPEDIENTE.
- c) La integridad referencial sobre la clave ajena cod_unidad.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 4 · §2.4

La integridad referencial exige que el valor de una clave ajena coincida con una clave primaria existente (o sea nulo). Un UNIQUE impediría que una unidad tramitase varios expedientes.

#### 9. Se intenta borrar una unidad que aún tramita expedientes. ¿Qué política referencial es la adecuada?

- a) CASCADE: borrar a la vez todos los expedientes de la unidad.
- b) RESTRICT / NO ACTION: rechazar el borrado mientras haya expedientes.
- c) SET NULL: dejar a nulo la unidad de esos expedientes.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §2.4

RESTRICT/NO ACTION rechaza la operación si hay filas hijas que referencian la fila padre, de modo que ningún expediente queda sin unidad ni se borra.

#### 10. Si por error se hubiera definido CASCADE sobre cod_unidad, ¿qué pasaría al borrar esa unidad?

- a) El SGBD rechazaría el borrado de la unidad.
- b) Los expedientes quedarían con la unidad a nulo.
- c) Se borrarían también todos los expedientes que tramita.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 4 · §2.4

CASCADE propaga el borrado de la fila padre a las filas hijas; rechazar es RESTRICT y poner a nulo es SET NULL.

### Caso 2. Normalización del registro de licencias

#### 1. En el supuesto de la tabla LICENCIA, el mismo distrito aparece con nombres distintos en filas diferentes. ¿Qué anomalía lo explica?

- a) La anomalía de inserción.
- b) La anomalía de actualización.
- c) La anomalía de borrado.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §4.1

Un dato repetido en muchas filas hay que cambiarlo en todas; si se olvida alguna, queda inconsistente. Eso ha ocurrido con el nombre del distrito.

#### 2. Al borrar la última licencia de un distrito se pierde su tasa. ¿Qué anomalía es?

- a) La anomalía de borrado.
- b) La anomalía de inserción.
- c) La anomalía de actualización.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §4.1

Hay anomalía de borrado cuando, al eliminar una fila, se pierde información que no se quería eliminar, como el nombre y la tasa del distrito.

#### 3. El servicio quiere registrar un distrito nuevo con su tasa antes de que tenga ninguna licencia, y no puede. ¿Qué anomalía sufre?

- a) La anomalía de borrado.
- b) La anomalía de actualización.
- c) La anomalía de inserción.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §4.1

La anomalía de inserción impide dar de alta un hecho (el distrito) sin conocer otro no relacionado (una licencia), porque ambos viven en la misma tabla.

#### 4. El atributo tecnicos guarda varios nombres separados por comas. ¿Qué forma normal incumple?

- a) La 1FN, porque la celda no contiene un valor atómico.
- b) La 2FN, porque depende de una parte de la clave.
- c) La 3FN, porque depende de otro atributo no clave.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §4.3

La 1FN exige que todos los atributos sean atómicos, con un único valor por celda; una lista de nombres en una celda la viola.

#### 5. ¿Cómo se lleva la tabla LICENCIA a 1FN?

- a) Sustituyendo tecnicos por las columnas tecnico1, tecnico2 y tecnico3.
- b) Con una tabla ASIGNACION(num_lic, tecnico) cuya clave es (num_lic, tecnico).
- c) Manteniendo la lista de técnicos, pero ordenada alfabéticamente.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.3

Los valores multivaluados se extraen a una tabla aparte relacionada por clave ajena; las columnas repetidas tecnico1, tecnico2… son también una violación típica de la 1FN.

#### 6. Tras pasar a 1FN, ¿está LICENCIA(num_lic PK, titular_dni, titular_nombre, cod_distrito, nombre_distrito, tasa_distrito) en 2FN?

- a) No: titular_nombre depende solo de una parte de la clave primaria.
- b) No: hay que separar antes DISTRITO para poder alcanzar la 2FN.
- c) Sí: su clave es simple (num_lic), así que no puede haber dependencias parciales.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §4.4

La 2FN elimina dependencias de una parte de la clave, lo que solo puede ocurrir con claves compuestas; con clave de un único atributo, 1FN implica 2FN.

#### 7. num_lic → cod_distrito y cod_distrito → {nombre_distrito, tasa_distrito}. ¿Qué tipo de dependencia hay y qué forma normal la elimina?

- a) Parcial, que elimina la 2FN.
- b) Transitiva, que elimina la 3FN.
- c) Multivaluada, que elimina la 4FN.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §4.2, §4.5

nombre_distrito y tasa_distrito dependen de la clave a través de un atributo no clave (cod_distrito): es una dependencia transitiva, y la 3FN la elimina.

#### 8. ¿Qué conjunto de tablas deja LICENCIA (sin los técnicos) en 3FN?

- a) LICENCIA(num_lic PK, titular_dni FK, cod_distrito FK), TITULAR(titular_dni PK, titular_nombre) y DISTRITO(cod_distrito PK, nombre_distrito, tasa_distrito).
- b) LICENCIA(num_lic PK, titular_dni, titular_nombre, cod_distrito FK), DISTRITO(cod_distrito PK, nombre_distrito) y TASA(cod_distrito PK, tasa_distrito).
- c) LICENCIA(num_lic PK, titular_dni FK, cod_distrito FK, nombre_distrito), TITULAR(titular_dni PK, titular_nombre) y DISTRITO(cod_distrito PK, tasa_distrito).

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §4.5

Hay dos dependencias transitivas (a través de cod_distrito y de titular_dni): se separan DISTRITO y TITULAR, y en LICENCIA quedan solo sus claves ajenas.

#### 9. ¿Por qué el diseño normalizado elimina las incoherencias detectadas en los nombres de distrito?

- a) Porque los índices de cada tabla impiden guardar valores duplicados.
- b) Porque los disparadores corrigen las filas que quedan inconsistentes.
- c) Porque cada hecho, como el nombre del distrito, se guarda una sola vez.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §4.1

La normalización garantiza que cada hecho se almacene una sola vez: el nombre y la tasa del distrito viven solo en DISTRITO y no pueden quedar inconsistentes.

#### 10. ¿Hasta qué forma normal es razonable llegar en este diseño?

- a) Hasta la 3FN, que aquí ya cumple BCNF porque todo determinante es clave.
- b) Hasta la 4FN, porque la lista de técnicos es una dependencia multivaluada.
- c) Solo hasta la 2FN, porque la clave de LICENCIA es un único atributo.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §4.6, §4.7

En las tablas resultantes el único determinante es la clave, de modo que cumplen BCNF; llegar a 3FN o BCNF es suficiente en la inmensa mayoría de los diseños.

### Caso 3. Diseño físico y consultas sobre las multas de tráfico

#### 1. En la tabla MULTA, ¿qué índice propondría para la consulta (a), buscar multas por matrícula?

- a) Un índice bitmap sobre matricula, columna de baja cardinalidad.
- b) Ninguno: el full table scan es lo más rápido en tablas grandes.
- c) Un índice B-tree sobre matricula, columna muy selectiva.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §2.8

La matrícula es muy selectiva y la búsqueda es por igualdad: un B-tree es adecuado. El bitmap es para columnas de baja cardinalidad, y el full scan solo compensa en tablas pequeñas.

#### 2. Para la consulta (b), listar multas de un rango de fechas, ¿qué índice es el adecuado?

- a) Un índice hash sobre fecha_denuncia.
- b) Un índice B-tree sobre fecha_denuncia.
- c) Un índice bitmap sobre importe.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §2.8

El B-tree sirve para igualdad y para rangos (BETWEEN, <, >); el hash solo sirve para igualdad exacta y no admite rangos.

#### 3. ¿Qué efecto tendrán los nuevos índices sobre la carga nocturna de denuncias?

- a) La ralentizarán, porque cada INSERT debe actualizar los índices.
- b) La acelerarán, porque las filas se insertan ya ordenadas.
- c) No le afectarán, porque los índices solo intervienen en lecturas.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §2.8

Los índices aceleran las lecturas pero penalizan las escrituras, porque hay que mantenerlos en cada INSERT; hay que equilibrar cuántos se crean.

#### 4. La consulta por matrícula hace un full table scan. ¿Con qué herramienta lo comprueba el técnico?

- a) Con ANALYZE, que muestra el plan elegido.
- b) Con EXPLAIN o EXPLAIN PLAN, que muestra el plan de ejecución.
- c) Con REINDEX, que muestra los índices usados.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §2.9

El plan de ejecución se inspecciona con EXPLAIN (PostgreSQL/MySQL) o EXPLAIN PLAN (Oracle). ANALYZE recalcula estadísticas y REINDEX reconstruye índices.

#### 5. ¿Qué necesita el optimizador para elegir bien el plan de ejecución?

- a) Que la tabla MULTA esté normalizada hasta BCNF.
- b) Un índice hash sobre cada columna de la tabla.
- c) Estadísticas actualizadas sobre filas y distribución de valores.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §2.9

El optimizador basado en costes estima cada plan con estadísticas (número de filas, distribución de valores, cardinalidad); por eso hay que mantenerlas al día (ANALYZE).

#### 6. Tras crear el índice sobre matricula, la consulta sigue haciendo full table scan. ¿Qué causa es posible?

- a) Que las estadísticas estén desactualizadas o la consulta aplique una función sobre la columna.
- b) Que un índice B-tree no pueda usarse en búsquedas por igualdad exacta.
- c) Que el plan de ejecución se fije al crear la tabla y ya no pueda cambiar.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §2.9

El optimizador puede ignorar un índice si las estadísticas están desactualizadas o si la consulta aplica una función sobre la columna indexada (WHERE UPPER(…) = …).

#### 7. ¿Cómo organizaría físicamente MULTA para que el informe anual no recorra los 20 millones de filas?

- a) Particionándola por hash de la matrícula.
- b) Separándola en dos tablas, pagadas y pendientes.
- c) Particionándola por rango de fecha, por años.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §2.9

El particionamiento por rango de fechas permite que la consulta de un año acceda solo a su partición; el hash por matrícula reparte las filas sin agruparlas por año.

#### 8. ¿Cómo se llama el beneficio por el que el informe del año solo lee su partición?

- a) Index-only scan.
- b) Partition pruning.
- c) Hash join.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §2.9

Con partition pruning la consulta accede solo a la partición relevante; además, el particionamiento facilita el mantenimiento y el archivado.

#### 9. Para el cuadro de mando con el total recaudado por distrito y año, ¿qué técnica aplicaría?

- a) Una vista materializada (o tabla de resumen) con esos totales.
- b) Normalizar la tabla MULTA hasta la forma normal de Boyce-Codd.
- c) Un índice hash sobre la columna importe de la tabla MULTA.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §2.9, §4.8

La vista materializada o tabla de resumen precalcula el agregado y evita recalcularlo en cada acceso: es una técnica de desnormalización controlada.

#### 10. ¿Qué contrapartida asume esa técnica y cómo se tratan el sistema transaccional y el analítico?

- a) Ninguna, porque se actualiza sola; ambos sistemas se desnormalizan.
- b) Hay que refrescarla; el transaccional sigue normalizado y el analítico se desnormaliza.
- c) Hay que refrescarla; el transaccional se desnormaliza y el analítico no.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §4.8

La desnormalización gana velocidad de lectura a costa de redundancia que hay que mantener; es típica de los entornos analíticos y poco recomendable en los transaccionales con muchas escrituras.
