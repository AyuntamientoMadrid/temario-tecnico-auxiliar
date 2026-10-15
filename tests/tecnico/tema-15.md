# Test del tema 15. Bases de datos y SGBD

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-15.html>

## Batería de preguntas

### 1. ¿Cuál es la diferencia entre una base de datos y un SGBD?

- a) La base de datos es el conjunto de datos; el SGBD es el software que la gestiona
- b) Son lo mismo
- c) El SGBD es el conjunto de datos; la base de datos es el hardware

**Respuesta correcta:** a) · **Referencia:** §1.2 [ELMASRI]

La **base de datos** es el conjunto de datos; el **SGBD** (Oracle, PostgreSQL…) es el software que la gestiona.

### 2. El principal problema del almacenamiento en ficheros propios por aplicación es:

- a) La redundancia e inconsistencia de los datos
- b) Que ocupan poco espacio
- c) Que son demasiado rápidos

**Respuesta correcta:** a) · **Referencia:** §1.1

Los ficheros aislados duplican datos (redundancia) que pueden quedar inconsistentes entre aplicaciones; la BD los integra.

### 3. El diccionario de datos (catálogo) de un SGBD contiene:

- a) Las copias de seguridad
- b) Solo los datos de los usuarios
- c) Los metadatos: la descripción de la estructura de la base de datos

**Respuesta correcta:** c) · **Referencia:** §1.3

El **diccionario de datos** almacena los **metadatos** (tablas, columnas, tipos, restricciones, usuarios): la descripción de la propia BD.

### 4. La sentencia `CREATE TABLE` pertenece al sublenguaje:

- a) DML
- b) DCL
- c) DDL

**Respuesta correcta:** c) · **Referencia:** §1.5 [ISO-9075]

`CREATE`, `ALTER` y `DROP` son **DDL** (definición). El DML manipula datos; el DCL controla el acceso.

### 5. Las sentencias `SELECT`, `INSERT`, `UPDATE` y `DELETE` forman parte del:

- a) DDL
- b) TCL
- c) DML (lenguaje de manipulación de datos)

**Respuesta correcta:** c) · **Referencia:** §1.5

Son **DML** (manipulación de datos). El DDL define la estructura; el TCL gestiona transacciones.

### 6. Las sentencias `GRANT` y `REVOKE` pertenecen al:

- a) DCL (control de acceso)
- b) DDL
- c) DML

**Respuesta correcta:** a) · **Referencia:** §1.5, §5.1

`GRANT` y `REVOKE` son **DCL**: conceden y retiran privilegios a usuarios y roles.

### 7. `COMMIT` y `ROLLBACK` pertenecen al:

- a) DDL
- b) DCL
- c) TCL (control de transacciones)

**Respuesta correcta:** c) · **Referencia:** §1.5, §2.1

`COMMIT` (confirma) y `ROLLBACK` (deshace) son **TCL**, el control de transacciones.

### 8. El componente del SGBD que genera el plan de ejecución eficiente de una consulta es:

- a) El gestor de almacenamiento
- b) El procesador de consultas (optimizador)
- c) El diccionario de datos

**Respuesta correcta:** b) · **Referencia:** §1.4

El **procesador de consultas** interpreta y **optimiza** las sentencias generando un plan de ejecución eficiente.

### 9. El rol responsable de la estructura física, los permisos, las copias y el rendimiento de la BD es:

- a) El usuario final
- b) El administrador de la base de datos (DBA)
- c) El programador de aplicaciones

**Respuesta correcta:** b) · **Referencia:** §1.6

El **DBA** administra la estructura física, los usuarios, las copias de seguridad, la disponibilidad y el rendimiento.

### 10. Una función de control esencial del SGBD es:

- a) Garantizar integridad, seguridad, concurrencia y recuperación
- b) Compilar el sistema operativo
- c) Fabricar el hardware de almacenamiento

**Respuesta correcta:** a) · **Referencia:** §1.3

El SGBD controla **integridad, seguridad, concurrencia y recuperación** ante fallos.

### 11. Una transacción se define como:

- a) Una copia de seguridad
- b) Un índice de la base de datos
- c) Una unidad lógica de trabajo indivisible (todo o nada)

**Respuesta correcta:** c) · **Referencia:** §2.1 [SILBERSCHATZ-DB]

La **transacción** es una unidad lógica de trabajo que se ejecuta como un todo indivisible: o todo, o nada.

### 12. ¿Qué significa la "A" de ACID?

- a) Acceso
- b) Análisis
- c) Atomicidad (todo o nada)

**Respuesta correcta:** c) · **Referencia:** §2.1 [ACID-HAERDER]

**A** = **Atomicidad**: si falla cualquier paso, se deshacen todos (rollback). ACID = Atomicidad, Consistencia, Aislamiento, Durabilidad.

### 13. La propiedad ACID que garantiza que un cambio confirmado persiste aunque caiga el sistema es:

- a) Atomicidad
- b) Aislamiento
- c) Durabilidad

**Respuesta correcta:** c) · **Referencia:** §2.1

La **durabilidad** garantiza que, tras el `COMMIT`, el cambio persiste pese a fallos, gracias al log de transacciones.

### 14. La propiedad ACID que evita que una transacción vea los estados intermedios de otra concurrente es:

- a) Consistencia
- b) Aislamiento
- c) Durabilidad

**Respuesta correcta:** b) · **Referencia:** §2.1

El **aislamiento** hace que el resultado de transacciones concurrentes sea como si se ejecutaran en serie.

### 15. Leer datos que otra transacción ha modificado pero aún no ha confirmado es una anomalía llamada:

- a) Lectura no repetible
- b) Lectura sucia (dirty read)
- c) Actualización perdida

**Respuesta correcta:** b) · **Referencia:** §2.2

La **lectura sucia** lee datos no confirmados que podrían deshacerse después.

### 16. El control de concurrencia en el que el SGBD mantiene varias versiones de cada dato, de modo que los lectores no bloquean a los escritores, es:

- a) Bloqueo en dos fases (2PL)
- b) MVCC (control multiversión)
- c) WAL

**Respuesta correcta:** b) · **Referencia:** §2.2 [POSTGRES-DOC]

El **MVCC** mantiene varias versiones; los lectores no bloquean a los escritores (lo usan PostgreSQL y Oracle).

### 17. El nivel de aislamiento SQL que evita todas las anomalías (sucia, no repetible y fantasma) es:

- a) Serializable
- b) Read Committed
- c) Repeatable Read

**Respuesta correcta:** a) · **Referencia:** §2.3 [ISO-9075]

**Serializable** es el nivel más alto: evita lectura sucia, no repetible y fantasma, a costa de menos concurrencia.

### 18. La técnica por la que el SGBD anota en un log lo que va a hacer antes de aplicarlo se denomina:

- a) Sharding
- b) Write-Ahead Logging (WAL)
- c) Normalización

**Respuesta correcta:** b) · **Referencia:** §2.4 [SILBERSCHATZ-DB]

El **WAL** (registro anticipado) anota los cambios en el log antes de aplicarlos, permitiendo redo/undo tras un fallo.

### 19. Tras un fallo, el SGBD usa el log para:

- a) Borrar la base de datos
- b) Crear nuevos usuarios
- c) Rehacer (redo) las transacciones confirmadas y deshacer (undo) las no confirmadas

**Respuesta correcta:** c) · **Referencia:** §2.4

La recuperación **rehace** las confirmadas y **deshace** las no confirmadas, garantizando atomicidad y durabilidad.

### 20. El protocolo de bloqueo que garantiza la seriabilidad de las transacciones es:

- a) El sharding
- b) El bloqueo en dos fases (2PL)
- c) El modelo en estrella

**Respuesta correcta:** b) · **Referencia:** §2.2

El **2PL (bloqueo en dos fases)** garantiza la seriabilidad; su riesgo es el interbloqueo entre transacciones.

### 21. La propiedad ACID de consistencia significa que:

- a) Los datos se replican en varios nodos
- b) Las consultas son rápidas
- c) La transacción lleva la BD de un estado válido a otro válido, respetando la integridad

**Respuesta correcta:** c) · **Referencia:** §2.1

La **consistencia** garantiza que la transacción respeta todas las reglas de integridad, pasando de un estado válido a otro.

### 22. Una lectura fantasma (phantom read) se produce cuando:

- a) Una consulta repetida devuelve filas nuevas insertadas por otra transacción
- b) Se borra la base de datos
- c) Se pierde la conexión

**Respuesta correcta:** a) · **Referencia:** §2.2, §2.3

La **lectura fantasma** aparece cuando una consulta repetida ve filas nuevas insertadas por otra transacción. La evita el nivel Serializable.

### 23. La arquitectura ANSI/SPARC define tres esquemas:

- a) Primario, secundario y terciario
- b) DDL, DML y DCL
- c) Interno, conceptual y externo

**Respuesta correcta:** c) · **Referencia:** §3 [ANSI-SPARC]

**ANSI/SPARC**: nivel **interno** (físico), **conceptual** (lógico global) y **externo** (vistas).

### 24. Poder añadir un índice (cambio de almacenamiento) sin afectar a las aplicaciones es un ejemplo de:

- a) Independencia lógica de datos
- b) Independencia física de datos
- c) Replicación

**Respuesta correcta:** b) · **Referencia:** §3

La **independencia física** permite cambiar el nivel interno (índices, ficheros) sin afectar al conceptual ni a las aplicaciones.

### 25. El nivel externo de ANSI/SPARC corresponde a:

- a) El almacenamiento físico
- b) El log de transacciones
- c) Las vistas parciales adaptadas a cada grupo de usuarios

**Respuesta correcta:** c) · **Referencia:** §3

El **nivel externo** son las **vistas**: lo que cada grupo de usuarios ve de la BD, según sus necesidades y permisos.

### 26. El nivel conceptual de ANSI/SPARC describe:

- a) Cómo se almacenan físicamente los datos
- b) Solo los índices
- c) La estructura lógica global de toda la base de datos

**Respuesta correcta:** c) · **Referencia:** §3

El **nivel conceptual** describe la estructura lógica global (entidades, relaciones, restricciones), independiente del almacenamiento.

### 27. El modelo de datos dominante, propuesto por Codd en 1970, es:

- a) El jerárquico
- b) El relacional (tablas)
- c) El de grafos

**Respuesta correcta:** b) · **Referencia:** §4.3 [CODD-1970]

El **modelo relacional** (Codd, 1970) organiza los datos en tablas y es el dominante; es la base de SQL.

### 28. En el modelo relacional, el atributo que referencia la clave primaria de otra tabla es:

- a) El índice
- b) La clave ajena (foránea)
- c) La vista

**Respuesta correcta:** b) · **Referencia:** §4.3

La **clave ajena (foránea)** referencia la clave primaria de otra tabla, estableciendo la integridad referencial.

### 29. La integridad de entidad exige que la clave primaria:

- a) Pueda ser nula
- b) Cambie en cada consulta
- c) No sea nula ni se repita

**Respuesta correcta:** c) · **Referencia:** §4.3 [DATE]

La **integridad de entidad**: la clave primaria no puede ser nula ni repetirse (identifica unívocamente cada fila).

### 30. La operación del álgebra relacional que combina filas de dos tablas según una condición es:

- a) La reunión (join)
- b) La proyección
- c) La selección

**Respuesta correcta:** a) · **Referencia:** §4.3

El **join (reunión)** combina filas de dos tablas según una condición (normalmente la igualdad de claves).

### 31. Un SGBD que extiende el modelo relacional con tipos complejos, herencia y objetos, manteniendo SQL, es:

- a) Jerárquico
- b) Clave-valor
- c) Objeto-relacional

**Respuesta correcta:** c) · **Referencia:** §4.4 [ISO-9075-OR]

El **objeto-relacional (ORDBMS)** extiende el relacional con objetos manteniendo SQL (Oracle, PostgreSQL, SQL:1999+).

### 32. Las bases de datos NoSQL se caracterizan por:

- a) Ser siempre relacionales
- b) Renunciar al modelo relacional estricto para ganar escalabilidad horizontal y flexibilidad de esquema
- c) No poder almacenar grandes volúmenes

**Respuesta correcta:** b) · **Referencia:** §4.5 [SADALAGE-FOWLER]

**NoSQL** ("Not only SQL") gana escalabilidad horizontal y esquema flexible, en respuesta al big data.

### 33. MongoDB es un ejemplo de base de datos NoSQL de tipo:

- a) Documental
- b) Clave-valor
- c) Grafos

**Respuesta correcta:** a) · **Referencia:** §4.5 [MONGODB-DOC]

**MongoDB** es **documental** (documentos JSON/BSON). Redis es clave-valor; Neo4j, de grafos.

### 34. Neo4j es una base de datos NoSQL de tipo:

- a) Columnar
- b) De grafos
- c) Documental

**Respuesta correcta:** b) · **Referencia:** §4.5

**Neo4j** es de **grafos** (nodos y relaciones), ideal para redes y recomendaciones.

### 35. El teorema CAP afirma que un sistema distribuido solo puede garantizar a la vez:

- a) Las tres propiedades C, A y P
- b) Dos de las tres: Consistencia, Disponibilidad y tolerancia a Particiones
- c) Ninguna de ellas

**Respuesta correcta:** b) · **Referencia:** §4.5 [CAP-BREWER]

El **teorema CAP** (Brewer): solo **dos de tres** (Consistencia, Disponibilidad, Particiones). Ante una partición se elige entre C y A.

### 36. El modelo BASE, alternativa a ACID en muchos NoSQL, prioriza:

- a) La consistencia inmediata por encima de todo
- b) La disponibilidad y la consistencia eventual
- c) El cifrado de los datos

**Respuesta correcta:** b) · **Referencia:** §4.5

**BASE** (Basically Available, Soft state, Eventual consistency) prioriza disponibilidad y consistencia eventual frente a la consistencia inmediata de ACID.

### 37. Redis es un ejemplo de base de datos NoSQL de tipo:

- a) De grafos
- b) Relacional
- c) Clave-valor

**Respuesta correcta:** c) · **Referencia:** §4.5

**Redis** es **clave-valor**, de acceso ultrarrápido (caché, sesiones).

### 38. El procesamiento OLTP se caracteriza por:

- a) Operaciones transaccionales cortas del día a día
- b) Consultas analíticas masivas sobre datos históricos
- c) No usar bases de datos

**Respuesta correcta:** a) · **Referencia:** §4.6

**OLTP** = transaccional, operaciones cortas del día a día (el Padrón en funcionamiento). OLAP es el analítico.

### 39. Un data warehouse (almacén de datos) sirve para:

- a) Sustituir al sistema operativo
- b) Cifrar los discos
- c) Consolidar datos históricos de varias fuentes para el análisis (OLAP)

**Respuesta correcta:** c) · **Referencia:** §4.6 [KIMBALL-DW]

El **data warehouse** consolida datos históricos para el análisis (OLAP), separándolo de los sistemas operacionales (OLTP).

### 40. El modelo de diseño típico de un data warehouse, con una tabla de hechos rodeada de dimensiones, es:

- a) El modelo en estrella
- b) El modelo jerárquico
- c) El modelo en red

**Respuesta correcta:** a) · **Referencia:** §4.6

El **modelo en estrella** (tabla de hechos + dimensiones) es el diseño típico de un data warehouse para OLAP.

### 41. Cassandra es un ejemplo de base de datos NoSQL de tipo:

- a) Documental
- b) Columnar (familias de columnas)
- c) Clave-valor

**Respuesta correcta:** b) · **Referencia:** §4.5

**Cassandra** es **columnar** (familias de columnas), optimizada para grandes volúmenes y mucha escritura.

### 42. Los SGBD jerárquicos organizan los datos en:

- a) Una estructura de árbol (relaciones padre-hijo 1:N)
- b) Tablas relacionadas por claves
- c) Documentos JSON

**Respuesta correcta:** a) · **Referencia:** §4.1

Los **jerárquicos** usan una estructura de **árbol** (padre-hijo 1:N); son históricos (IBM IMS) y rígidos para N:M.

### 43. Conceder solo lectura de una tabla a un rol se hace con:

- a) `DROP TABLE tabla;`
- b) `GRANT SELECT ON tabla TO rol;`
- c) `COMMIT;`

**Respuesta correcta:** b) · **Referencia:** §5.1 [ISO-9075]

`GRANT SELECT ON tabla TO rol;` concede el privilegio de **lectura**. Gestionar por roles simplifica la administración.

### 44. Agrupar los privilegios en conjuntos que se asignan a los usuarios se hace mediante:

- a) Índices
- b) Roles
- c) Vistas materializadas

**Respuesta correcta:** b) · **Referencia:** §5.1

Los **roles** agrupan privilegios; asignar roles (no privilegios sueltos) simplifica la gestión de muchos usuarios.

### 45. Repartir (particionar) los datos entre varios nodos según una clave para escalar horizontalmente se denomina:

- a) Replicación
- b) Sharding
- c) Normalización

**Respuesta correcta:** b) · **Referencia:** §5.3

El **sharding** reparte los datos entre nodos según una clave, para escalar horizontalmente (típico en NoSQL).

### 46. Mantener copias idénticas de los datos en varios nodos se denomina:

- a) Replicación
- b) Fragmentación
- c) Indexación

**Respuesta correcta:** a) · **Referencia:** §5.3

La **replicación** mantiene copias en varios nodos: mejora la disponibilidad y la lectura, pero complica la consistencia.

### 47. La conmutación automática a un nodo de respaldo cuando falla el principal se llama:

- a) Commit
- b) Sharding
- c) Failover

**Respuesta correcta:** c) · **Referencia:** §5.4

El **failover** es la conmutación por error a un nodo de respaldo, base de la alta disponibilidad.

### 48. La recuperación a un punto en el tiempo (PITR) se consigue:

- a) Solo con una copia completa
- b) Combinando una copia de seguridad con el log de transacciones
- c) Borrando el log

**Respuesta correcta:** b) · **Referencia:** §5.5 [POSTGRES-DOC]

El **PITR** restaura una copia y aplica el **log** hasta el instante exacto anterior al incidente.

### 49. Una copia de seguridad incremental:

- a) Copia toda la base de datos cada vez
- b) No es posible
- c) Copia solo lo que ha cambiado desde la última copia

**Respuesta correcta:** c) · **Referencia:** §5.5

La copia **incremental** copia solo lo cambiado desde la última, ahorrando espacio y tiempo frente a la completa.

### 50. Analizar cómo el optimizador resuelve una consulta lenta se hace con:

- a) El plan de ejecución (EXPLAIN)
- b) Un GRANT
- c) Un ROLLBACK

**Respuesta correcta:** a) · **Referencia:** §5.7

El **plan de ejecución** (`EXPLAIN`) muestra cómo el optimizador resuelve la consulta, base del *tuning*.

### 51. La principal palanca para acelerar una consulta que hace un recorrido completo de una tabla grande es:

- a) Borrar la tabla
- b) Desactivar la integridad referencial
- c) Crear un índice adecuado

**Respuesta correcta:** c) · **Referencia:** §5.7

Crear un **índice** adecuado convierte un recorrido completo (full table scan) en una búsqueda O(log n).

### 52. El espacio lógico sobre ficheros donde el DBA organiza el almacenamiento físico de la BD se denomina:

- a) Tablespace
- b) Vista
- c) Trigger

**Respuesta correcta:** a) · **Referencia:** §5.2

Los **tablespaces** son los espacios lógicos sobre ficheros donde se organiza el almacenamiento (tablas, índices).

### 53. La base de datos como servicio gestionada en la nube se denomina:

- a) DBaaS
- b) DDL
- c) OLAP

**Respuesta correcta:** a) · **Referencia:** §5.8

**DBaaS** (Database as a Service): SGBD gestionados en la nube (Amazon RDS, Azure SQL, Cloud SQL).

### 54. Un inconveniente típico del DBaaS para una Administración pública es:

- a) La ubicación de los datos y el cumplimiento del RGPD (soberanía del dato)
- b) Que nunca tiene copias de seguridad
- c) Que es siempre gratuito

**Respuesta correcta:** a) · **Referencia:** §5.8

El **DBaaS** plantea dudas de **ubicación de los datos** y cumplimiento del **RGPD/ENS** (soberanía), además del *vendor lock-in*.

### 55. La gobernanza del dato incluye:

- a) Calidad, metadatos, ciclo de vida y protección de datos personales
- b) Solo el cifrado del disco
- c) Únicamente la compra de hardware

**Respuesta correcta:** a) · **Referencia:** §5.6 [RGPD]

La **gobernanza** abarca calidad, metadatos, ciclo de vida, clasificación y protección de datos (RGPD/LOPDGDD).

### 56. El tratamiento de datos personales en una base de datos del Ayuntamiento debe cumplir:

- a) El RGPD y la LOPDGDD
- b) Solo el manual del fabricante
- c) Ninguna normativa

**Respuesta correcta:** a) · **Referencia:** §5.1, §5.6 [RGPD][LOPDGDD]

Los datos personales obligan a cumplir el **RGPD** y la **LOPDGDD** (minimización, control de acceso, cifrado, registro de accesos).

### 57. La alta disponibilidad de una base de datos se logra principalmente con:

- a) Borrando índices
- b) Reduciendo la seguridad
- c) Clústeres, replicación y failover

**Respuesta correcta:** c) · **Referencia:** §5.4

La **alta disponibilidad** se apoya en clústeres, replicación primario-secundario y conmutación por error (failover).

### 58. Dividir una tabla por filas entre varios nodos es una forma de:

- a) Normalización
- b) Fragmentación horizontal
- c) Indexación

**Respuesta correcta:** b) · **Referencia:** §5.3

Dividir una tabla por **filas** es **fragmentación horizontal**; por columnas, vertical. Es base de la distribución.

### 59. Una ventaja del DBaaS es:

- a) Que el proveedor gestiona infraestructura, copias, parches y escalado
- b) Que elimina la necesidad de seguridad
- c) Que los datos nunca salen del equipo local

**Respuesta correcta:** a) · **Referencia:** §5.8

El **DBaaS** descarga en el proveedor la infraestructura, las copias, los parches y el escalado, con pago por uso.

### 60. El particionado de una tabla muy grande por rango de fechas sirve para:

- a) Mejorar el rendimiento y el mantenimiento
- b) Eliminar la clave primaria
- c) Impedir las consultas

**Respuesta correcta:** a) · **Referencia:** §5.2

El **particionado** (por fecha, territorio…) mejora el rendimiento de las consultas y facilita el mantenimiento de tablas grandes.

## Preguntas sobre los casos prácticos

### Caso 1. Integridad y concurrencia en la base de datos del Padrón

#### 1. En el supuesto planteado, ¿qué mecanismo del modelo relacional impide que un habitante quede asignado a un distrito que no existe en la tabla DISTRITO?

- a) La integridad de entidad.
- b) La integridad referencial.
- c) La restricción de dominio CHECK.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §4.3

La integridad referencial exige que toda clave ajena corresponda a una clave primaria existente en la tabla referenciada (o sea nula), lo que impide referencias huérfanas.

#### 2. ¿Qué papel desempeñan las columnas implicadas en esa relación entre HABITANTE y DISTRITO?

- a) distrito_id es la clave primaria de HABITANTE y referencia la clave ajena id de DISTRITO.
- b) id es una clave ajena de DISTRITO que referencia la clave primaria distrito_id de HABITANTE.
- c) distrito_id es una clave ajena de HABITANTE que referencia la clave primaria id de DISTRITO.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §4.3

La clave ajena es el atributo que referencia la clave primaria de otra tabla: aquí, distrito_id (en HABITANTE) apunta a id (en DISTRITO).

#### 3. Un empleado intenta dar de alta a un habitante con un distrito_id que no figura en la tabla DISTRITO. Con la integridad referencial definida, ¿qué hace el SGBD?

- a) Rechaza la operación, porque la clave ajena no corresponde a ninguna clave primaria existente.
- b) Acepta el alta y crea automáticamente el distrito con ese identificador en la tabla DISTRITO.
- c) Acepta el alta y deja la referencia pendiente hasta que alguien cree después el distrito.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §4.3

La integridad referencial impide las referencias huérfanas: el SGBD no admite una clave ajena que no corresponda a una clave primaria existente.

#### 4. Un cambio de domicilio actualiza varias tablas y el sistema cae a mitad. ¿Qué propiedad garantiza que el cambio no quede «a medias»?

- a) El aislamiento, que impide que otros vean los estados intermedios.
- b) La durabilidad, que conserva lo ya escrito pese al corte.
- c) La atomicidad («todo o nada»).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.1

La atomicidad obliga a que las operaciones de una transacción se completen todas o no se aplique ninguna: si falla un paso, se deshacen todos.

#### 5. ¿Con qué sentencias, y de qué sublenguaje de SQL, se confirma o se deshace la transacción del cambio de domicilio?

- a) COMMIT y ROLLBACK, del TCL.
- b) GRANT y REVOKE, del DCL.
- c) INSERT y DELETE, del DML.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §1.5, §2.1

El TCL gestiona las transacciones: COMMIT confirma los cambios y ROLLBACK los deshace. GRANT y REVOKE controlan el acceso (DCL).

#### 6. Al reiniciar tras la caída, el SGBD encuentra en el log el cambio de domicilio, que no llegó a confirmarse. ¿Qué hace con él?

- a) Lo rehace (redo) para completar las tablas que faltaban.
- b) Lo deshace (undo), porque la transacción no se confirmó.
- c) Lo conserva tal cual hasta que el empleado lo termine.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.4

Tras un fallo, el SGBD usa el log para rehacer las transacciones confirmadas y deshacer las no confirmadas; así se preserva la atomicidad.

#### 7. Dos empleados modifican a la vez el mismo registro de un habitante y uno sobrescribe el cambio del otro. ¿Cómo se llama esta anomalía?

- a) Lectura sucia (dirty read).
- b) Lectura fantasma (phantom read).
- c) Actualización perdida (lost update).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §2.2

Hay actualización perdida cuando dos transacciones actualizan el mismo dato y una sobrescribe a la otra; la lectura sucia consiste en leer datos aún no confirmados.

#### 8. ¿Qué dos técnicas emplea el SGBD para controlar este tipo de concurrencia?

- a) Los bloqueos (protocolo 2PL) y el control multiversión (MVCC).
- b) El Write-Ahead Logging (WAL) y los puntos de control (checkpoints).
- c) Los índices B+árbol y el particionado de tablas por rango.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §2.2

El control de concurrencia se hace con bloqueos (el 2PL garantiza la seriabilidad) o con MVCC, que mantiene varias versiones de cada dato. WAL y checkpoints sirven a la recuperación.

#### 9. Una vez confirmada un alta en el Padrón, el servidor se apaga justo después. ¿Qué propiedad garantiza que el alta no se pierda y gracias a qué elemento?

- a) La consistencia, gracias al diccionario de datos.
- b) La durabilidad, gracias al log de transacciones (WAL).
- c) El aislamiento, gracias al control multiversión.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §2.1, §2.4

La durabilidad asegura que, tras el COMMIT, el cambio persiste aunque falle el sistema; se apoya en el log, donde el SGBD anota lo que va a hacer antes de aplicarlo.

#### 10. Al arrancar de nuevo el servidor, ¿qué hace el SGBD con esa alta que ya estaba confirmada?

- a) La rehace (redo) a partir del log, si sus cambios no habían llegado a los datos.
- b) La deshace (undo), porque el apagón la interrumpió antes de escribirse.
- c) La descarta y obliga al empleado a repetir el alta del habitante.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §2.4

Con el log, el SGBD rehace las transacciones confirmadas y deshace solo las no confirmadas; un alta confirmada no se pierde.

### Caso 2. Administración y rendimiento de la base de datos de tributos

#### 1. En el supuesto planteado, la consulta de un recibo por NIF tarda demasiado. ¿Qué herramienta usa el DBA para ver cómo resuelve el SGBD esa consulta?

- a) El plan de ejecución (EXPLAIN).
- b) El diccionario de datos del sistema.
- c) El log de transacciones (WAL).

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §5.7

El plan de ejecución (EXPLAIN) muestra cómo el optimizador resuelve la consulta y es el punto de partida del ajuste de rendimiento.

#### 2. El plan revela un recorrido completo de la tabla de recibos (full table scan). ¿Qué medida aplica el DBA?

- a) Elevar el nivel de aislamiento de la sesión a Serializable.
- b) Crear un índice sobre la columna NIF.
- c) Hacer una copia completa (full) de la tabla.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §5.2, §5.7

La palanca habitual ante un recorrido completo es crear un índice adecuado sobre la columna de búsqueda; el aislamiento y las copias no aceleran la consulta.

#### 3. Con el índice sobre el NIF, ¿cómo cambia el coste de localizar un recibo?

- a) Pasa a crecer con el cuadrado del número de filas, O(n²).
- b) Sigue siendo proporcional al número de filas, O(n).
- c) Se reduce a un orden logarítmico, O(log n).

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §5.7

El índice (normalmente un B+árbol) evita recorrer millones de filas y reduce la búsqueda a O(log n); el recorrido completo es el que crece con n.

#### 4. El personal de atención solo debe poder consultar los recibos. ¿Con qué sublenguaje y sentencia lo configura el DBA?

- a) Con el DML: SELECT * FROM recibos WHERE rol = 'atencion';
- b) Con el DCL: GRANT SELECT ON recibos TO rol_atencion;
- c) Con el DDL: ALTER TABLE recibos READ ONLY FOR rol_atencion;

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §1.5, §5.1

Los privilegios se gestionan con el DCL: GRANT SELECT concede solo lectura sobre la tabla al rol indicado.

#### 5. Si el rol de atención tuviera concedido por error el permiso de modificación, ¿qué sentencia se lo retira?

- a) REVOKE UPDATE ON recibos FROM rol_atencion;
- b) ROLLBACK UPDATE ON recibos FROM rol_atencion;
- c) DELETE UPDATE ON recibos FROM rol_atencion;

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §5.1

En el DCL, GRANT concede privilegios y REVOKE los retira; ROLLBACK deshace transacciones y DELETE borra filas.

#### 6. ¿Por qué conviene conceder estos privilegios a un rol y no a cada empleado de atención por separado?

- a) Porque el rol cifra los recibos y evita registrar los accesos de cada empleado.
- b) Porque el rol permite modificar recibos sin necesidad de ninguna sentencia GRANT.
- c) Porque el rol simplifica la gestión de miles de usuarios y aplica el mínimo privilegio.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §5.1

Los roles agrupan privilegios: se conceden una vez al rol y el rol se asigna a los empleados, lo que simplifica la gestión y ajusta cada perfil al mínimo privilegio.

#### 7. Se quiere poder restaurar la base de datos de tributos al instante exacto anterior a un borrado accidental. ¿Cómo se llama esa capacidad?

- a) Recuperación a un punto en el tiempo (PITR).
- b) Conmutación por error (failover).
- c) Copia incremental desde la última copia.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §5.5

La recuperación a un punto en el tiempo (PITR) restaura la base de datos al instante exacto anterior a un incidente; el failover conmuta a otro nodo ante un fallo.

#### 8. Además de una copia de seguridad, ¿qué necesita el DBA para aplicar esa recuperación al instante previo al borrado?

- a) El diccionario de datos con los metadatos.
- b) Una réplica en otro nodo con failover.
- c) El log de transacciones.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §5.5

El PITR combina una copia de seguridad con el log de transacciones, que permite reaplicar los cambios hasta el instante elegido.

#### 9. Los recibos contienen datos personales. ¿Qué normativa obliga a controlar y registrar los accesos y a proteger esa información?

- a) Únicamente el ENI, por tratarse de interoperabilidad.
- b) El RGPD y la LOPDGDD, además del ENS.
- c) El estándar SQL (ISO/IEC 9075) y ANSI/SPARC.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §5.1, §5.6

Los datos personales obligan a cumplir el RGPD y la LOPDGDD (y, en el sector público, el ENS): minimización, control de acceso, cifrado y registro de accesos.

#### 10. ¿Qué medida forma parte de las obligaciones sobre los datos personales de los recibos?

- a) Dar acceso de lectura a toda la plantilla para favorecer la transparencia.
- b) Conservar todos los datos de forma indefinida por si se necesitan.
- c) Registrar los accesos y minimizar los datos personales tratados.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §5.1, §5.6

El RGPD/LOPDGDD exige minimización, control de acceso, cifrado y registro de accesos; además, la gobernanza fija un ciclo de vida con retención y borrado.

### Caso 3. Elección de tecnología para los datos abiertos y la analítica

#### 1. En el supuesto planteado, para la gestión diaria del Padrón y los tributos con máxima integridad, ¿qué tipo de SGBD y de procesamiento son los adecuados?

- a) Un SGBD documental NoSQL con procesamiento OLAP.
- b) Un SGBD relacional con procesamiento OLTP.
- c) Un SGBD multidimensional con cubos OLAP.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §4.3, §4.6

La gestión del día a día son operaciones transaccionales cortas (OLTP) y requiere la integridad y las garantías ACID de un SGBD relacional.

#### 2. ¿Qué aporta el SGBD relacional a la gestión de los tributos frente a un NoSQL?

- a) Esquema flexible y escalado horizontal.
- b) Disponibilidad con consistencia eventual.
- c) Esquema rígido, ACID e integridad fuerte.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §4.5

El relacional aporta esquema rígido, ACID e integridad fuerte, ideal para transacciones como tributos o nóminas; el esquema flexible y la consistencia eventual son propios de NoSQL.

#### 3. Para analizar la evolución demográfica y la recaudación por distrito y año cruzando varias fuentes, ¿qué infraestructura propone el técnico?

- a) Un data warehouse alimentado desde las fuentes operacionales.
- b) Lanzar las consultas masivas sobre la base de datos OLTP del Padrón.
- c) Una base de datos NoSQL de grafos con los recibos y los habitantes.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §4.6

El data warehouse consolida datos históricos de varias fuentes para el análisis y lo separa de los sistemas operacionales.

#### 4. ¿Con qué tipo de procesamiento se explota ese almacén para los cuadros de mando?

- a) OLTP, con muchas operaciones transaccionales cortas.
- b) OLAP, con cubos y agregaciones (drill-down, roll-up).
- c) TCL, con transacciones confirmadas mediante COMMIT.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §4.6

El procesamiento OLAP está orientado a consultas masivas para el análisis y organiza los datos en cubos que permiten agregaciones rápidas.

#### 5. ¿Cómo se llama el modelo de diseño típico de ese almacén de datos?

- a) Modelo jerárquico, en árbol padre-hijo.
- b) Modelo en red, según CODASYL.
- c) Modelo en estrella.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §4.6

El diseño típico de un data warehouse es el modelo en estrella: una tabla de hechos rodeada de dimensiones. Los modelos jerárquico y en red son tipologías históricas de SGBD.

#### 6. En ese modelo en estrella, ¿qué papel tienen «distrito» y «año»?

- a) Son dimensiones que rodean la tabla de hechos.
- b) Son tablas de hechos situadas en el centro.
- c) Son vistas del nivel externo ANSI/SPARC.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §4.6

En el modelo en estrella, la tabla de hechos se rodea de dimensiones como el tiempo, el distrito o el concepto, por las que se agregan los datos.

#### 7. Si se optara por una base de datos NoSQL distribuida para un servicio web masivo, ¿qué compromiso impone el teorema CAP?

- a) Que hay que renunciar a la tolerancia a particiones para tener consistencia y disponibilidad.
- b) Que ante una partición de red hay que elegir entre consistencia y disponibilidad.
- c) Que un sistema distribuido puede garantizar a la vez las tres propiedades.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §4.5

El teorema CAP permite garantizar solo dos de las tres propiedades; como las particiones son inevitables en un sistema distribuido, se elige entre consistencia y disponibilidad.

#### 8. ¿Qué modelo suelen seguir esos sistemas NoSQL en lugar de ACID?

- a) El modelo ANSI/SPARC de tres esquemas.
- b) El protocolo de bloqueo en dos fases (2PL).
- c) El modelo BASE, con consistencia eventual.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §4.5

Muchos NoSQL siguen el modelo BASE (Basically Available, Soft state, Eventual consistency), que prioriza la disponibilidad y la consistencia eventual.

#### 9. Antes de contratar una base de datos en la nube (DBaaS) con datos de ciudadanos, ¿qué cautela debe valorar la Administración?

- a) La ubicación de los datos y el cumplimiento del RGPD y del ENS.
- b) Que el proveedor no realiza copias de seguridad ni aplica parches.
- c) Que el DBaaS no permite escalar ni ofrecer alta disponibilidad.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §5.8

En el DBaaS el proveedor gestiona copias, parches y escalado; el riesgo de gobierno está en dónde residen los datos (RGPD, datos en la UE, soberanía) y en el ENS.

#### 10. La otra cautela es el riesgo de que el Ayuntamiento quede atado a un único proveedor de nube. ¿Cómo se denomina?

- a) Conmutación por error (failover).
- b) Dependencia del proveedor (vendor lock-in).
- c) Reparto por clave entre nodos (sharding).

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §5.8

La dependencia del proveedor (vendor lock-in) es uno de los inconvenientes de gobierno del DBaaS; failover y sharding son técnicas de disponibilidad y escalado.
