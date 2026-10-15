# Test del tema 19. Lenguajes de interrogación de bases de datos

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-19.html>

## Batería de preguntas

### 1. ¿Qué produce, en el modelo relacional, un lenguaje de interrogación al operar sobre una o más relaciones?

- a) Otra relación (propiedad de cierre)
- b) Un fichero binario sin estructura
- c) Un objeto en memoria fuera del modelo relacional

**Respuesta correcta:** a) · **Referencia:** §1.1 [CODD70]

El resultado de cualquier operación sobre relaciones es, a su vez, una relación, lo que permite componer consultas dentro de otras consultas.

### 2. En el vocabulario del modelo relacional, ¿qué es una tupla?

- a) El nombre de una columna
- b) Una fila de la relación
- c) El esquema completo de la tabla

**Respuesta correcta:** b) · **Referencia:** §1.1 [CODD70]

La relación es la tabla completa; el atributo es la columna; la tupla es cada fila individual.

### 3. ¿Qué demostró Codd sobre el álgebra relacional y el cálculo relacional seguro (safe)?

- a) Que el álgebra es más potente que el cálculo
- b) Que el cálculo relacional no es formalizable matemáticamente
- c) Que ambos son expresivamente equivalentes (completitud relacional)

**Respuesta correcta:** c) · **Referencia:** §1.2 [CODD70; DATE-REL]

Todo lo expresable en álgebra relacional lo es en cálculo relacional seguro, y viceversa; esta equivalencia fundamenta el criterio de completitud relacional para evaluar otros lenguajes de consulta.

### 4. El operador de selección (σ) del álgebra relacional actúa sobre:

- a) Filas, extrayendo las que cumplen una condición
- b) Columnas, eliminando duplicados
- c) Dos relaciones, combinándolas por producto cartesiano

**Respuesta correcta:** a) · **Referencia:** §1.2 [DATE-INTRO, cap. 6]

La proyección (π) es la que opera sobre columnas; el producto cartesiano (×) combina dos relaciones completas.

### 5. ¿Qué requisito deben cumplir dos relaciones para poder aplicarles unión, diferencia o intersección?

- a) Tener el mismo número de filas
- b) Ser compatibles por unión (mismo esquema de atributos)
- c) Compartir una clave primaria

**Respuesta correcta:** b) · **Referencia:** §1.2 [GMUW, cap. 2]

Los operadores binarios de conjuntos exigen que ambas relaciones tengan el mismo número y tipo de atributos; no importa el número de filas.

### 6. La reunión (join, ⋈) del álgebra relacional se define formalmente como:

- a) Un operador unario sobre una sola relación
- b) Sinónimo exacto de la unión (∪)
- c) Un producto cartesiano seguido de una selección por la condición de reunión

**Respuesta correcta:** c) · **Referencia:** §1.2 [DATE-INTRO, cap. 6]

El join es un operador derivado: se puede expresar combinando el producto cartesiano (×) y la selección (σ).

### 7. ¿Qué tipo de consulta resuelve típicamente el operador de división (÷) del álgebra relacional?

- a) «Qué X están relacionados con TODOS los Y»
- b) «Cuántas filas tiene la tabla»
- c) «Ordenar las filas por un atributo»

**Respuesta correcta:** a) · **Referencia:** §1.2 [DATE-INTRO, cap. 6]

Es el operador derivado propio de consultas de universalidad, como «contribuyentes que tienen liquidados todos los tipos de tributo».

### 8. En el cálculo relacional de dominios, las variables representan:

- a) Tuplas completas de una relación
- b) Valores de un dominio (una columna concreta)
- c) Nombres de tablas del esquema

**Respuesta correcta:** b) · **Referencia:** §1.2 [CODD70]

Frente al cálculo de tuplas (variables = tuplas completas), el cálculo de dominios usa variables que representan valores de una columna; es la base conceptual de QBE.

### 9. ¿Cuál de las siguientes afirmaciones sobre álgebra y cálculo relacional es correcta?

- a) El álgebra es declarativa y el cálculo procedimental
- b) Solo el álgebra relacional tiene fundamento matemático formal
- c) El álgebra es procedimental (dice CÓMO) y el cálculo es declarativo (dice QUÉ)

**Respuesta correcta:** c) · **Referencia:** §1.2 [DATE-REL, cap. 6]

Es la distinción fundamental entre ambos lenguajes equivalentes.

### 10. SQL, respecto al álgebra y el cálculo relacional, se describe como:

- a) Declarativo en su sintaxis, pero traducido internamente a operadores algebraicos por el optimizador
- b) Puramente procedimental, sin relación con el cálculo relacional
- c) Un lenguaje ajeno al modelo relacional de Codd

**Respuesta correcta:** a) · **Referencia:** §1.4 [DATE-REL, cap. 6]

SQL se parece al cálculo relacional en superficie, pero el motor lo ejecuta como un árbol de operadores algebraicos.

### 11. La propiedad de cierre (closure) del álgebra relacional permite:

- a) Ejecutar consultas sin necesidad de optimizador
- b) Componer operadores anidando el resultado de uno como entrada de otro
- c) Prescindir del esquema de las relaciones

**Respuesta correcta:** b) · **Referencia:** §1.2 [DATE-INTRO, cap. 6]

Como cada operación produce otra relación, su resultado puede alimentar directamente a la siguiente operación.

### 12. ¿Quién formuló por primera vez el modelo relacional en el que se apoyan el álgebra y el cálculo relacional?

- a) Chamberlin y Boyce, en el artículo de SEQUEL
- b) Melton y Simon, en su guía del estándar SQL
- c) E. F. Codd, en su artículo de 1970 sobre bases de datos relacionales

**Respuesta correcta:** c) · **Referencia:** §1.1 [CODD70]

<em>A Relational Model of Data for Large Shared Data Banks</em> (CACM, 1970) es el artículo fundacional del modelo relacional.

### 13. ¿Qué sublenguaje se encarga de crear, modificar y eliminar la estructura del esquema (tablas, índices, vistas)?

- a) DDL
- b) DML
- c) DCL

**Respuesta correcta:** a) · **Referencia:** §1.3 [SILBERSCHATZ, cap. 3]

El Lenguaje de Definición de Datos opera sobre el catálogo del SGBD con <code>CREATE</code>, <code>ALTER</code>, <code>DROP</code> y <code>TRUNCATE</code>.

### 14. MERGE, INSERT, UPDATE y DELETE pertenecen al sublenguaje:

- a) DDL
- b) DML
- c) TCL

**Respuesta correcta:** b) · **Referencia:** §1.3 [ELMASRI, cap. 6]

Son las sentencias que modifican el contenido de las tablas sin alterar su estructura.

### 15. Según el estándar ISO/IEC 9075, la sentencia SELECT se clasifica formalmente dentro de:

- a) DCL
- b) DDL
- c) DML (la separación DQL es una convención didáctica)

**Respuesta correcta:** c) · **Referencia:** §1.3 [ISO9075]

El estándar no separa formalmente DQL; es una distinción muy usada en manuales y oposiciones por la naturaleza claramente distinta del SELECT (no modifica datos) frente al resto del DML.

### 16. GRANT y REVOKE son sentencias del sublenguaje:

- a) DCL
- b) TCL
- c) DQL

**Respuesta correcta:** a) · **Referencia:** §1.3 [SILBERSCHATZ, cap. 3]

El Lenguaje de Control de Datos gestiona permisos: <code>GRANT</code> concede privilegios y <code>REVOKE</code> los retira.

### 17. COMMIT, ROLLBACK y SAVEPOINT pertenecen a:

- a) DDL
- b) TCL
- c) DML

**Respuesta correcta:** b) · **Referencia:** §1.3 [ACID83]

El Lenguaje de Control de Transacciones gestiona el ciclo de vida de la transacción y sustenta las propiedades ACID.

### 18. ¿Cuál de estas afirmaciones distingue correctamente lo procedimental de lo declarativo?

- a) Lo declarativo especifica el procedimiento paso a paso
- b) Ambos enfoques son equivalentes y no se distinguen en la práctica
- c) Lo procedimental dice CÓMO obtener el resultado; lo declarativo dice QUÉ se quiere, y el sistema decide cómo

**Respuesta correcta:** c) · **Referencia:** §1.4 [MELTON, cap. 1]

Es la distinción central de §1.4, aplicable tanto al álgebra/cálculo como a SQL frente a un lenguaje de programación clásico.

### 19. El acceso a datos mediante ODBC/JDBC tiene como objetivo principal:

- a) Ofrecer una interfaz común de acceso independiente del SGBD concreto, mediante un driver específico
- b) Sustituir completamente al SQL por un lenguaje de objetos
- c) Eliminar la necesidad de un servidor de bases de datos

**Respuesta correcta:** a) · **Referencia:** §1.5 [SILBERSCHATZ, cap. 10]

ODBC (C) y JDBC (Java) siguen el mismo patrón: driver del motor + interfaz común para la aplicación cliente.

### 20. En el contexto del acceso a datos desde aplicaciones, un ORM (Object-Relational Mapping):

- a) Sustituye el modelo relacional por un modelo de grafos
- b) Traduce automáticamente entre objetos del lenguaje y filas de tablas relacionales, generando el SQL correspondiente
- c) Es un sinónimo de SQL embebido estático

**Respuesta correcta:** b) · **Referencia:** §1.5 [SILBERSCHATZ, cap. 10]

Facilita la productividad, aunque puede generar SQL subóptimo si se usa sin entender la traducción resultante.

### 21. SQL nace originalmente con el nombre de:

- a) QUEL
- b) System R
- c) SEQUEL, diseñado por Chamberlin y Boyce sobre el prototipo System R

**Respuesta correcta:** c) · **Referencia:** §2.1 [CHAMBERLIN74]

El nombre se abrevió después a SQL por un conflicto de marca registrada.

### 22. El primer estándar ANSI de SQL se publicó en:

- a) 1986 (SQL-86), adoptado por ISO en 1987
- b) 1974, con la publicación de SEQUEL
- c) 1999, con SQL3

**Respuesta correcta:** a) · **Referencia:** §2.1 [MELTON, cap. 1]

Es el primer estándar formal, tras años de dialectos comerciales dispares.

### 23. La edición del estándar SQL que introdujo la sintaxis moderna de JOIN explícito y las subconsultas tal como se usan hoy fue:

- a) SQL-86
- b) SQL-92 (SQL2)
- c) SQL:2003

**Respuesta correcta:** b) · **Referencia:** §2.1 [MELTON, cap. 1]

Fue la revisión más citada del estándar por su gran expansión de la sintaxis de consulta.

### 24. ¿Qué aportó SQL:1999 (SQL3) al estándar?

- a) Las funciones de ventana analíticas
- b) El soporte nativo de JSON
- c) La recursividad (CTE recursivas) y los disparadores

**Respuesta correcta:** c) · **Referencia:** §2.1 [EISENBERG99]

Dos de los cuatro bloques de este mismo Tema 19 se incorporaron formalmente en esta edición.

### 25. Desde SQL:1999, el esquema de niveles de conformidad de SQL-92 (Entry/Intermediate/Full) se sustituyó por:

- a) Un núcleo («core») obligatorio más «features» opcionales identificadas por código
- b) Un único nivel obligatorio para todos los SGBD
- c) La certificación ISO 25010 de calidad del software

**Respuesta correcta:** a) · **Referencia:** §2.2 [MELTON, cap. 2]

Sustituye el esquema «todo o nada» de tres niveles por una declaración más granular de conformidad.

### 26. ¿Qué son PL/SQL, T-SQL y PL/pgSQL?

- a) Ediciones sucesivas del estándar ISO/IEC 9075
- b) Dialectos procedimentales propios de cada motor (Oracle, SQL Server, PostgreSQL), no estándar
- c) Sinónimos del lenguaje SQL/PSM, idénticos entre sí

**Respuesta correcta:** b) · **Referencia:** §2.9 [MELTON-PSM]

Se inspiran en la referencia SQL/PSM del estándar, pero cada uno tiene su propia sintaxis.

### 27. El orden LÓGICO en que un motor SQL evalúa las cláusulas de un SELECT es:

- a) SELECT → FROM → WHERE → GROUP BY
- b) WHERE → SELECT → FROM → ORDER BY
- c) FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

**Respuesta correcta:** c) · **Referencia:** §2.3 [SILBERSCHATZ, cap. 3]

Este orden lógico no coincide con el orden en que se escribe la sentencia.

### 28. ¿Por qué, en la mayoría de motores, un alias definido en el SELECT no puede usarse en la cláusula WHERE de la misma consulta?

- a) Porque WHERE se evalúa antes de que el motor calcule las expresiones del SELECT, según el orden lógico de evaluación
- b) Porque los alias no existen en el estándar SQL
- c) Porque WHERE solo admite nombres de tabla, nunca de columna

**Respuesta correcta:** a) · **Referencia:** §2.3 [SILBERSCHATZ, cap. 3]

Por la misma razón, sí puede usarse en ORDER BY, que se evalúa después.

### 29. ¿Qué diferencia principal existe entre WHERE y HAVING?

- a) Son sinónimos intercambiables en cualquier posición
- b) WHERE filtra filas antes de agrupar; HAVING filtra grupos después de la agregación
- c) HAVING se ejecuta siempre antes que WHERE

**Respuesta correcta:** b) · **Referencia:** §2.4 [SILBERSCHATZ, cap. 3]

Es una de las distinciones básicas del bloque SQL.

### 30. ¿Cuál de estas funciones NO es una función de agregación estándar de GROUP BY?

- a) SUM
- b) AVG
- c) ROW_NUMBER (es una función de ventana, no de agregación de GROUP BY)

**Respuesta correcta:** c) · **Referencia:** §2.4-2.8 [ISO9075; ZEMKE03]

<code>ROW_NUMBER()</code> requiere la cláusula <code>OVER</code> y no colapsa filas, a diferencia de <code>SUM</code>/<code>AVG</code>/<code>COUNT</code>/<code>MIN</code>/<code>MAX</code>.

### 31. Toda columna del SELECT que no forme parte de una función de agregación debe aparecer, por regla general, en:

- a) La cláusula GROUP BY
- b) La cláusula ORDER BY únicamente
- c) La cláusula WHERE

**Respuesta correcta:** a) · **Referencia:** §2.4 [SILBERSCHATZ, cap. 3]

Es la regla de dependencia funcional del agrupamiento: toda columna «suelta» del SELECT debe estar entre las columnas de agrupación.

### 32. Un INNER JOIN devuelve:

- a) Todas las filas de la tabla izquierda, coincidan o no
- b) Solo las filas que coinciden en ambas tablas según la condición de reunión
- c) El producto cartesiano completo sin condición

**Respuesta correcta:** b) · **Referencia:** §2.5 [ELMASRI, cap. 7]

Es el join más restrictivo de los tres «outer» y no produce valores NULL por ausencia de coincidencia.

### 33. ¿Qué join es la forma estándar de responder a «todos los contribuyentes, tengan o no tributos liquidados»?

- a) INNER JOIN
- b) CROSS JOIN
- c) LEFT [OUTER] JOIN

**Respuesta correcta:** c) · **Referencia:** §2.5 [ELMASRI, cap. 7]

Devuelve todas las filas de la tabla izquierda y, si no hay coincidencia en la derecha, sus columnas aparecen como NULL.

### 34. Un SELF JOIN es:

- a) Una tabla unida consigo misma, usando alias distintos para cada «copia» lógica
- b) Un join que solo puede hacerse con la cláusula NATURAL JOIN
- c) Sinónimo de CROSS JOIN

**Respuesta correcta:** a) · **Referencia:** §2.5 [ELMASRI, cap. 7]

Es imprescindible dar alias distintos a las dos referencias de la misma tabla para poder distinguirlas en la consulta.

### 35. El NATURAL JOIN se desaconseja en la práctica profesional principalmente porque:

- a) No existe en el estándar SQL
- b) Es una reunión implícita por columnas homónimas, frágil ante cambios de esquema
- c) Solo funciona con tablas vacías

**Respuesta correcta:** b) · **Referencia:** §2.5 [ELMASRI, cap. 7]

Un cambio de nombre de columna, o añadir una columna homónima nueva, altera silenciosamente el resultado.

### 36. En un FULL OUTER JOIN entre CONTRIBUYENTE y TRIBUTO, una fila de CONTRIBUYENTE sin tributos asociados aparecerá:

- a) Excluida del resultado
- b) Duplicada
- c) Con las columnas de TRIBUTO a NULL

**Respuesta correcta:** c) · **Referencia:** §2.5 [ELMASRI, cap. 7]

El FULL OUTER JOIN conserva todas las filas de ambas tablas, coincidan o no, rellenando con NULL el lado que falte.

### 37. Una subconsulta no correlacionada se caracteriza porque:

- a) Es independiente de la fila de la consulta externa y el motor puede ejecutarla una sola vez
- b) Debe reevaluarse obligatoriamente por cada fila de la consulta externa
- c) No puede usarse con el predicado IN

**Respuesta correcta:** a) · **Referencia:** §2.6 [DATE-INTRO, cap. 8]

No referencia ninguna columna de la consulta que la contiene.

### 38. Una subconsulta correlacionada:

- a) Nunca referencia columnas de la consulta externa
- b) Referencia una columna de la consulta externa y su resultado depende de la fila actual
- c) Solo puede aparecer en la cláusula FROM

**Respuesta correcta:** b) · **Referencia:** §2.6 [SILBERSCHATZ, cap. 3]

Es el rasgo que la distingue de la no correlacionada; el optimizador puede reescribirla como join en muchos casos.

### 39. ¿Qué predicado comprueba si la subconsulta devuelve al menos una fila, sin importar su valor?

- a) IN
- b) ALL
- c) EXISTS

**Respuesta correcta:** c) · **Referencia:** §2.6 [DATE-INTRO, cap. 8]

Comprueba solo la existencia de filas, no su contenido, y suele ser más eficiente que IN porque puede detenerse en la primera coincidencia.

### 40. ¿Qué riesgo clásico presenta NOT IN cuando la subconsulta puede devolver un valor NULL?

- a) Puede no devolver ninguna fila, por la lógica trivaluada de SQL
- b) Provoca siempre un error de sintaxis
- c) Se comporta exactamente igual que NOT EXISTS en todos los casos

**Respuesta correcta:** a) · **Referencia:** §2.6 [SILBERSCHATZ, cap. 3]

NOT EXISTS no tiene ese problema y suele ser la alternativa más segura.

### 41. Una CTE (Common Table Expression), definida con WITH, es:

- a) Una tabla física permanente creada en el catálogo
- b) Un conjunto de resultados nombrado y temporal, que existe solo durante la ejecución de la sentencia
- c) Un tipo de índice sobre columnas calculadas

**Respuesta correcta:** b) · **Referencia:** §2.7 [EISENBERG99]

Mejora la legibilidad frente a subconsultas anidadas y permite referenciarse varias veces en la misma consulta.

### 42. Toda CTE recursiva (WITH RECURSIVE) necesita obligatoriamente:

- a) Un ORDER BY en el miembro ancla
- b) Usar UNION en lugar de UNION ALL para evitar bucles
- c) Un miembro ancla sin referencia a sí mismo y un miembro recursivo unido con UNION ALL

**Respuesta correcta:** c) · **Referencia:** §2.7 [ISO9075; EISENBERG99]

Sin una condición de reunión que reduzca el conjunto en cada paso, la recursión no terminaría.

### 43. Las funciones de ventana (OVER, PARTITION BY) se diferencian de GROUP BY en que:

- a) Conservan todas las filas originales, añadiendo una columna calculada sobre la partición, sin colapsar el resultado
- b) Siempre reducen el número de filas del resultado a una por grupo
- c) No pueden usar funciones de agregación como SUM o AVG

**Respuesta correcta:** a) · **Referencia:** §2.8 [ZEMKE03]

Es la diferencia clave frente a GROUP BY, que sí colapsa las filas en una por grupo.

### 44. ¿Qué función de ventana asigna un número secuencial único dentro de la partición, sin dejar huecos ni empates?

- a) RANK()
- b) ROW_NUMBER()
- c) NTILE()

**Respuesta correcta:** b) · **Referencia:** §2.8 [ZEMKE03]

RANK() sí puede dejar huecos tras un empate (1,2,2,4); DENSE_RANK() no deja huecos pero sí permite empates (1,2,2,3); ROW_NUMBER() nunca empata.

### 45. SQL/PSM (ISO/IEC 9075-4) es:

- a) Un motor de bases de datos comercial
- b) La sentencia estándar para crear vistas actualizables
- c) La referencia normativa para procedimientos almacenados, que cada motor implementa con su propio dialecto (PL/SQL, T-SQL, PL/pgSQL)

**Respuesta correcta:** c) · **Referencia:** §2.9 [MELTON-PSM]

Fija los conceptos comunes (variables, cursores, control de flujo, excepciones), pero la sintaxis concreta difiere por motor.

### 46. El soporte nativo de JSON en SQL (funciones como JSON_VALUE, JSON_TABLE) se incorporó formalmente en:

- a) SQL:2016
- b) SQL-92
- c) SQL:1999

**Respuesta correcta:** a) · **Referencia:** §2.9 [MELTON, cap. 12]

Es uno de los hitos que acercan SQL a los datos semiestructurados típicos de NoSQL.

### 47. Un procedimiento almacenado se diferencia de una función almacenada en que:

- a) La función nunca puede tener parámetros de entrada
- b) La función siempre devuelve un único valor mediante RETURN y suele poder usarse dentro de una expresión SQL; el procedimiento se invoca como sentencia independiente
- c) Un procedimiento no puede ejecutar sentencias DML

**Respuesta correcta:** b) · **Referencia:** §3.1 [MELTON-PSM]

Un procedimiento puede devolver cero, uno o varios valores mediante parámetros OUT/INOUT.

### 48. ¿Cuál es la principal ventaja de rendimiento de un procedimiento almacenado frente a enviar SQL dinámico repetidamente?

- a) Consume menos espacio en disco
- b) No necesita permisos de ejecución
- c) Reutiliza el plan de ejecución cacheado tras la primera invocación, evitando repetir el análisis y la optimización

**Respuesta correcta:** c) · **Referencia:** §3.2 [GMUW, cap. 8]

El coste de analizar y optimizar se paga una vez, no en cada llamada.

### 49. Un parámetro de modo OUT en un procedimiento almacenado:

- a) Recibe el valor que el procedimiento le asigna y se devuelve al llamador al terminar; su valor de entrada se ignora
- b) Solo puede leerse dentro del procedimiento, nunca modificarse
- c) Es el modo por defecto de todo parámetro si no se indica lo contrario

**Respuesta correcta:** a) · **Referencia:** §3.3 [MELTON-PSM; MSSQL-DOC]

El modo por defecto es IN, no OUT.

### 50. El ciclo habitual de un cursor explícito sigue la secuencia:

- a) OPEN → DECLARE → CLOSE → FETCH
- b) DECLARE → OPEN → FETCH (en bucle) → CLOSE
- c) FETCH → DECLARE → OPEN → CLOSE

**Respuesta correcta:** b) · **Referencia:** §3.4 [SILBERSCHATZ, cap. 5]

Olvidar el CLOSE mantiene recursos y bloqueos ocupados durante la sesión.

### 51. Un cursor scrollable, frente a uno forward-only, se caracteriza por:

- a) No poder recorrer ninguna fila del resultado
- b) Ser siempre implícito, nunca declarado por el programador
- c) Poder moverse hacia adelante y hacia atrás, e incluso saltar a una fila concreta

**Respuesta correcta:** c) · **Referencia:** §3.4 [ORACLE-DOC]

Consume más recursos que el forward-only, que solo avanza.

### 52. En la gestión de excepciones de un procedimiento almacenado, el código SQLSTATE:

- a) Es un código de cinco caracteres normalizado por el estándar SQL para identificar el tipo de error
- b) Es exclusivo de un único motor comercial y no está estandarizado
- c) Sustituye por completo a los bloques de manejo de errores del procedimiento

**Respuesta correcta:** a) · **Referencia:** §3.6 [MELTON-PSM]

Muchos motores añaden además su propio código numérico (SQLCODE) específico del producto.

### 53. Un disparador (trigger) se diferencia de un procedimiento almacenado normal en que:

- a) Siempre requiere parámetros de entrada explícitos
- b) Se ejecuta automáticamente en respuesta a un evento, sin que nadie lo invoque directamente por su nombre
- c) No puede acceder a los valores de la fila afectada

**Respuesta correcta:** b) · **Referencia:** §4.1 [SILBERSCHATZ, cap. 5]

Un disparador no admite parámetros al estilo de un procedimiento; recibe el contexto del evento (OLD/NEW).

### 54. Un disparador BEFORE, a diferencia de uno AFTER:

- a) Solo puede usarse sobre vistas
- b) Se ejecuta siempre en una transacción distinta
- c) Se ejecuta antes de aplicar el cambio y puede validar, modificar o incluso cancelar la operación

**Respuesta correcta:** c) · **Referencia:** §4.2 [ISO9075]

AFTER, en cambio, se ejecuta cuando el cambio ya está aplicado, útil para acciones derivadas como la auditoría.

### 55. Un disparador definido FOR EACH ROW:

- a) Se ejecuta una vez por cada fila afectada por la sentencia, con acceso a los valores OLD y NEW
- b) Se ejecuta una única vez por sentencia, sin importar el número de filas afectadas
- c) Solo puede combinarse con eventos programados por tiempo

**Respuesta correcta:** a) · **Referencia:** §4.2 [ELMASRI, cap. 5]

FOR EACH STATEMENT es el que se ejecuta una única vez por sentencia, sin acceso directo a cada fila.

### 56. Un disparador INSTEAD OF es imprescindible cuando:

- a) La tabla base tiene una clave primaria compuesta
- b) Se necesita sustituir una operación DML sobre una vista no directamente actualizable (por ejemplo, con JOIN)
- c) Se quiere programar una tarea de mantenimiento periódico por tiempo

**Respuesta correcta:** b) · **Referencia:** §4.2 [MYSQL-DOC]

El disparador INSTEAD OF traduce la operación sobre la vista a las operaciones equivalentes sobre las tablas base.

### 57. Los eventos programados (scheduled events / jobs) se disparan:

- a) Por una sentencia INSERT sobre la tabla asociada
- b) Por una sentencia DELETE exclusivamente
- c) Por tiempo, no por una operación DML, y se usan típicamente para mantenimiento periódico

**Respuesta correcta:** c) · **Referencia:** §4.2 [MYSQL-DOC; MSSQL-DOC; ORACLE-DOC; PSQL-DOC]

Ejemplos: Event Scheduler de MySQL, SQL Server Agent, DBMS_SCHEDULER de Oracle, pg_cron de PostgreSQL.

### 58. ¿Cuál es un riesgo característico de encadenar varios disparadores entre sí (trigger chain)?

- a) Efectos en cascada difíciles de depurar, incluyendo el riesgo de recursión no controlada
- b) Ninguno: los disparadores encadenados siempre mejoran el rendimiento
- c) El estándar SQL prohíbe expresamente más de un disparador por tabla

**Respuesta correcta:** a) · **Referencia:** §4.4 [SILBERSCHATZ, cap. 5]

Es uno de los motivos por los que se recomienda usar disparadores con moderación y preferir restricciones declarativas cuando sea posible.

### 59. SQL/PGQ, incorporado en SQL:2023, permite:

- a) Sustituir por completo el modelo relacional por un modelo de grafos
- b) Expresar consultas de grafos de propiedades directamente sobre tablas relacionales
- c) Eliminar la necesidad de índices en el SGBD

**Respuesta correcta:** b) · **Referencia:** §5 [MELTON, cap. 12]

No sustituye el modelo relacional: añade una sintaxis declarativa de grafos sobre las mismas tablas.

### 60. Las tendencias actuales del lenguaje SQL (JSON nativo, SQL/PGQ, funciones analíticas avanzadas):

- a) Sustituyen los fundamentos del modelo relacional y el núcleo declarativo del SELECT
- b) Solo son relevantes para sistemas NoSQL, no para SGBD relacionales
- c) Amplían el estándar SQL sin sustituir sus fundamentos: el modelo relacional y el núcleo declarativo siguen siendo la base

**Respuesta correcta:** c) · **Referencia:** §5 [MELTON, cap. 12]

El Tema 19 completo —desde el modelo relacional hasta los disparadores— sigue vigente como fundamento de estas extensiones más recientes.

## Preguntas sobre los casos prácticos

### Caso 1. Análisis de recaudación de tributos por distrito

#### 1. En el supuesto planteado, Hacienda quiere ver solo los distritos cuyo total recaudado supere los 100.000 €. ¿Dónde debe expresarse esa condición?

- a) En la cláusula WHERE, con la condición SUM(t.importe) > 100000, antes del GROUP BY.
- b) En la cláusula HAVING, con la condición SUM(t.importe) > 100000, después del GROUP BY.
- c) En la cláusula ORDER BY, que descarta los grupos que no alcanzan el valor indicado.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.4

La condición depende de un total agregado por distrito, así que filtra grupos ya formados: eso es HAVING, que se evalúa después de GROUP BY.

#### 2. ¿Por qué la condición sobre el total recaudado no puede ir en la cláusula WHERE de la consulta?

- a) Porque WHERE filtra filas individuales antes de que existan los grupos y no puede contener funciones de agregación.
- b) Porque WHERE se evalúa después del ORDER BY, cuando el resultado ya está ordenado y no admite más filtros.
- c) Porque WHERE solo admite condiciones sobre columnas de clave primaria, como id_distrito o dni.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.3 y §2.4

En el orden lógico de evaluación (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY), WHERE actúa fila a fila antes de agrupar, por lo que no puede usar SUM().

#### 3. La consulta del distrito muestra id_distrito, nombre_distrito, COUNT(*) y SUM(t.importe). ¿Qué columnas deben figurar en el GROUP BY?

- a) Solo las expresiones agregadas COUNT(*) y SUM(t.importe), que son las que se calculan por grupo.
- b) Ninguna, porque el motor agrupa automáticamente por todas las columnas que aparecen en el SELECT.
- c) id_distrito y nombre_distrito, porque toda columna del SELECT no agregada debe figurar en el GROUP BY.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.4

Regla de dependencia funcional del GROUP BY: toda columna del SELECT que no esté dentro de una función de agregación debe aparecer en la cláusula de agrupación.

#### 4. La consulta termina con ORDER BY total_recaudado DESC, usando el alias definido en el SELECT. ¿Es válido?

- a) Sí, porque ORDER BY se evalúa después del SELECT, cuando el alias ya existe.
- b) No, porque un alias del SELECT solo puede utilizarse dentro de la cláusula WHERE.
- c) No, porque ORDER BY se evalúa antes del SELECT y hay que repetir SUM(t.importe).

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.3

El orden lógico de evaluación sitúa ORDER BY después de SELECT; por eso el alias sí puede usarse en ORDER BY, aunque no en WHERE.

#### 5. Para obtener todos los contribuyentes de un distrito, tengan o no algún tributo liquidado, ¿qué reunión debe usarse?

- a) Un INNER JOIN entre CONTRIBUYENTE y TRIBUTO por el DNI del contribuyente.
- b) Un LEFT JOIN desde CONTRIBUYENTE hacia TRIBUTO por el DNI del contribuyente.
- c) Un CROSS JOIN entre CONTRIBUYENTE y TRIBUTO, filtrado después por el distrito.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.5

El LEFT JOIN conserva todas las filas de la tabla izquierda (CONTRIBUYENTE) aunque no tengan coincidencia en la derecha; el INNER JOIN perdería a quienes no tienen tributos.

#### 6. En el resultado de esa reunión, ¿cómo aparece un contribuyente del distrito que no tiene ningún tributo liquidado?

- a) No aparece, porque la reunión descarta las filas sin coincidencia en la tabla de la derecha.
- b) Aparece con el importe a cero, que el motor asigna por defecto a las filas sin pareja.
- c) Aparece con su nombre y con la columna importe a NULL, al no existir la fila de la derecha.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.5

En un LEFT JOIN, cuando la fila de la derecha no existe, sus columnas aparecen como NULL; el contribuyente se conserva.

#### 7. El técnico quiere ahora listar solo los contribuyentes del distrito que NO tienen ningún tributo. Partiendo del LEFT JOIN anterior, ¿qué debe añadir?

- a) La condición WHERE t.importe IS NULL, que detecta la ausencia de fila en TRIBUTO.
- b) La condición WHERE t.importe = 0, que identifica a los contribuyentes sin liquidaciones.
- c) Un ORDER BY t.importe, que agrupa al principio a los contribuyentes sin tributos.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §2.5

El NULL que genera el LEFT JOIN en las columnas de la derecha es precisamente lo que permite detectar la ausencia de relación con WHERE t.importe IS NULL.

#### 8. En la cuestión 3, la subconsulta que calcula la media de importes filtra por el distrito de la fila que se está evaluando (c.id_distrito). ¿Qué tipo de subconsulta es?

- a) No correlacionada: el motor la ejecuta una sola vez y reutiliza su resultado para todas las filas.
- b) Una expresión de tabla común recursiva, porque se referencia a sí misma en cada paso.
- c) Correlacionada: referencia una columna de la consulta externa y su resultado depende de la fila actual.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §2.6

Al referenciar c.id_distrito de la consulta externa, la media cambia según el contribuyente evaluado: es una subconsulta correlacionada.

#### 9. Para mostrar cada tributo con el puesto que ocupa entre los tributos del mismo contribuyente, de mayor a menor importe y sin perder filas, ¿qué expresión es la adecuada?

- a) GROUP BY dni_contribuyente con COUNT(*), que numera los tributos de cada contribuyente.
- b) RANK() OVER (PARTITION BY dni_contribuyente ORDER BY importe DESC).
- c) ROW_NUMBER() OVER (ORDER BY dni_contribuyente), sin partición por contribuyente.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §2.8

Una función de ventana conserva todas las filas y calcula el puesto dentro de cada partición; PARTITION BY agrupa por contribuyente y el ORDER BY del OVER fija el orden por importe.

#### 10. Un contribuyente tiene cuatro tributos y los dos segundos de mayor importe empatan. Con RANK(), ¿qué puesto recibe el cuarto tributo?

- a) El 4, porque RANK() salta números tras un empate (1, 2, 2, 4).
- b) El 3, porque RANK() no deja huecos en la numeración tras un empate.
- c) El 2, porque RANK() repite el último puesto hasta el final de la partición.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §2.8

RANK() da el mismo puesto a los empatados y salta números después (1, 2, 2, 4); la numeración sin huecos (1, 2, 2, 3) es la de DENSE_RANK().

### Caso 2. Procedimiento almacenado de recálculo de bonificaciones del Padrón

#### 1. En la cabecera de bonificar_tributos_distrito, ¿qué modo debe tener el parámetro que indica el distrito a procesar?

- a) OUT, porque el procedimiento devuelve el distrito procesado al llamador al terminar.
- b) INOUT, porque el procedimiento necesita modificar el distrito durante el recorrido.
- c) IN, porque es un dato de entrada que el procedimiento solo lee y no modifica.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §3.3

IN es el modo de entrada: el llamador pasa el valor y el procedimiento solo lo lee. Es, además, el modo por defecto.

#### 2. ¿Qué modo debe tener el parámetro que devuelve el número de tributos bonificados?

- a) IN, porque el llamador debe indicar de antemano cuántos tributos se van a bonificar.
- b) OUT, porque el procedimiento le asigna el valor y lo devuelve al llamador al terminar.
- c) Ninguno: un procedimiento devuelve siempre su resultado mediante la cláusula RETURN.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §3.3

Un parámetro OUT recibe el valor que le asigna el procedimiento y se devuelve al llamador; su valor de entrada se ignora. RETURN es propio de las funciones.

#### 3. Un compañero propone convertir el procedimiento en una función almacenada. ¿Qué rasgo distinguiría a la función?

- a) Que devuelve siempre un único valor mediante RETURN y puede usarse dentro de una expresión SQL.
- b) Que admite varios parámetros de salida OUT y se invoca como sentencia independiente con CALL.
- c) Que se ejecuta automáticamente cada vez que se actualiza un importe de la tabla TRIBUTO.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §3.1 y §3.3

La función devuelve un único valor con RETURN y suele poder usarse en un SELECT; el procedimiento se invoca con CALL y puede devolver varios valores por parámetros OUT.

#### 4. ¿Por qué en este supuesto se recorre el resultado con un cursor en lugar de lanzar una única sentencia UPDATE de conjunto?

- a) Porque una sentencia UPDATE no puede modificar más de una fila de la tabla en cada ejecución.
- b) Porque en una versión posterior cada tributo llevará una regla distinta según su tipo y hay que tratarlo fila a fila.
- c) Porque recorrer fila a fila con un cursor es siempre más rápido que una operación de conjunto.

**Respuesta correcta:** b) · **Referencia:** Caso 2, enunciado y cuestión 2 · §3.4

El cursor está justificado cuando la regla no se puede expresar como un UPDATE de conjunto; si se pudiera, la operación de conjunto sería preferible por rendimiento.

#### 5. ¿Cuál es la secuencia correcta del ciclo de vida del cursor que recorre los tributos del distrito?

- a) OPEN → DECLARE → FETCH en bucle → CLOSE.
- b) DECLARE → FETCH en bucle → OPEN → CLOSE.
- c) DECLARE → OPEN → FETCH en bucle → CLOSE.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §3.4

El cursor explícito se declara sobre un SELECT, se abre, se leen sus filas con FETCH dentro de un bucle hasta que no quedan más y, por último, se cierra.

#### 6. El recorrido solo necesita avanzar, fila a fila, desde el primer tributo hasta el último. ¿Qué tipo de cursor es el adecuado?

- a) Un cursor forward-only, que solo avanza hacia adelante y es el más ligero.
- b) Un cursor scrollable, que permite moverse hacia atrás y saltar a una fila concreta.
- c) Un cursor implícito, que el programador declara y controla paso a paso.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §3.4

El forward-only solo avanza, consume menos recursos y es el más usado; el scrollable consume más. El cursor implícito lo gestiona el propio SGBD, no el programador.

#### 7. Si el programador olvidara la instrucción CLOSE al terminar el bucle, ¿qué consecuencia tendría?

- a) El cursor volvería automáticamente a la primera fila y repetiría el recorrido completo.
- b) El SGBD desharía todas las bonificaciones aplicadas durante el recorrido del cursor.
- c) El cursor seguiría consumiendo recursos del servidor (memoria, bloqueos) mientras dure la sesión.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §3.4

Un cursor abierto y no cerrado consume memoria y bloqueos del servidor mientras dura la sesión; olvidar el CLOSE es una mala práctica habitual.

#### 8. Dentro del bucle se aplica la bonificación del 10 % a un tributo de 800 €. ¿Qué importe queda y cómo se calcula?

- a) 80 €, multiplicando el importe por 0,10.
- b) 720 €, multiplicando el importe por 0,90.
- c) 880 €, multiplicando el importe por 1,10.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3

Bonificar un 10 % significa cobrar el 90 % del importe: 800 × 0,90 = 720 €.

#### 9. Tras actualizar cada tributo dentro del bucle, ¿qué debe hacerse con el parámetro de salida que cuenta los tributos bonificados?

- a) Incrementarlo en una unidad: p_num_bonificados = p_num_bonificados + 1.
- b) Asignarle el nuevo importe del tributo que se acaba de actualizar.
- c) Leerlo para decidir si el tributo actual debe bonificarse o no.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §3.3

El parámetro OUT acumula cuántos tributos se han bonificado: se suma uno por cada fila actualizada y su valor final se devuelve al llamador.

#### 10. Durante la ejecución falla la actualización de un tributo concreto. Si el negocio no exige que el lote sea todo o nada, ¿cuál es el tratamiento más razonable?

- a) Hacer un ROLLBACK global que deshaga todas las bonificaciones aplicadas hasta ese momento.
- b) Capturar la excepción con un manejador vacío, sin registrarla, y seguir con el recorrido.
- c) Capturar la excepción dentro del bucle, registrar el error y continuar con el siguiente tributo.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §3.6

El fallo de un tributo no debe impedir bonificar el resto, pero el error no puede silenciarse: un manejador vacío que «traga» la excepción oculta fallos difíciles de depurar.

### Caso 3. Auditoría de cambios de estado en expedientes

#### 1. Para impedir que un expediente pase a CERRADO sin haber pasado antes por RESUELTO, ¿qué tipo de disparador debe usarse?

- a) AFTER UPDATE de sentencia, que se ejecuta una vez cuando el cambio ya se ha aplicado.
- b) BEFORE UPDATE de fila, que valida cada fila y puede cancelar la operación antes de aplicarla.
- c) INSTEAD OF UPDATE sobre la tabla EXPEDIENTE, que sustituye la actualización original.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §4.2

El disparador BEFORE se ejecuta antes de aplicar el cambio y puede cancelarlo; de fila, para disponer de los valores de cada expediente. INSTEAD OF es exclusivo de vistas.

#### 2. Para registrar en AUDITORIA_EXPEDIENTE cada cambio de estado, ¿qué tipo de disparador es el adecuado?

- a) BEFORE UPDATE de sentencia, que se ejecuta una sola vez antes de la actualización.
- b) Un evento programado nocturno que revise los expedientes modificados durante el día.
- c) AFTER UPDATE de fila, que registra el cambio de cada expediente una vez aplicado.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §4.2 y §4.3

La auditoría es la elección natural de un disparador AFTER: se ejecuta cuando el dato ya ha quedado escrito y, siendo de fila, accede a los valores anterior y nuevo.

#### 3. ¿Por qué el disparador de auditoría debe ser de fila y no de sentencia?

- a) Porque el de fila se ejecuta por cada fila afectada con acceso a OLD y NEW; el de sentencia no accede a los valores de cada fila.
- b) Porque el de sentencia no llega a ejecutarse cuando la actualización afecta a más de una fila de la tabla.
- c) Porque el de fila es el único que puede activarse con UPDATE; el de sentencia solo responde a INSERT.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §4.2

El disparador FOR EACH STATEMENT se ejecuta una sola vez por sentencia, afecte a cero o a diez mil filas, sin acceso directo a los valores individuales de cada fila.

#### 4. ¿Qué condición debe comprobar el disparador de validación para lanzar el error?

- a) SI ANTIGUO.estado = 'CERRADO' Y NUEVO.estado <> 'RESUELTO'.
- b) SI NUEVO.estado = 'RESUELTO' Y ANTIGUO.estado <> 'CERRADO'.
- c) SI NUEVO.estado = 'CERRADO' Y ANTIGUO.estado <> 'RESUELTO'.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §4.2

Lo prohibido es llegar a CERRADO (valor nuevo) desde un estado que no sea RESUELTO (valor anterior).

#### 5. Cuando el disparador de validación detecta un cierre indebido, ¿qué debe hacer?

- a) Insertar una fila en la tabla de auditoría y dejar que la actualización continúe.
- b) Lanzar un error de negocio con un mensaje descriptivo, que cancela la operación.
- c) Ejecutar un COMMIT que confirme el estado anterior del expediente afectado.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §3.6 y §4.3

Las reglas de negocio que no expresan las restricciones declarativas se implementan con un disparador BEFORE que, si no se cumple la condición, cancela la operación lanzando un error.

#### 6. El disparador de auditoría solo debe insertar una fila cuando el estado ha cambiado realmente. ¿Qué condición lo garantiza?

- a) SI NUEVO.estado <> ANTIGUO.estado.
- b) SI NUEVO.estado = 'CERRADO'.
- c) SI ANTIGUO.estado = 'ABIERTO'.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §4.3

Un UPDATE puede tocar otras columnas sin modificar el estado; comparar el valor anterior con el nuevo evita registrar cambios que no son de estado.

#### 7. Para rellenar estado_anterior y estado_nuevo en AUDITORIA_EXPEDIENTE, ¿qué valores usa el disparador?

- a) Los de la última fila registrada en AUDITORIA_EXPEDIENTE para ese mismo expediente.
- b) ANTIGUO.estado y NUEVO.estado, que el disparador de fila recibe del evento.
- c) NUEVO.estado en ambas columnas, porque el valor anterior ya no existe tras el UPDATE.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §4.2

Un disparador de fila sobre UPDATE accede a OLD (valor antes del cambio) y NEW (valor después); en un AFTER UPDATE ambos están disponibles.

#### 8. Un desarrollador propone que la aplicación pase al disparador, como parámetro, el identificador del funcionario que hace el cambio. ¿Es viable?

- a) Sí, declarándolo como parámetro IN en la cabecera del disparador.
- b) Sí, declarándolo como parámetro OUT para devolverlo a la aplicación.
- c) No: el disparador no admite parámetros; recibe implícitamente el contexto del evento.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §4.1

Un disparador no se invoca por su nombre ni admite parámetros de entrada al estilo de un procedimiento: trabaja con los valores OLD/NEW de la fila afectada. El usuario se obtiene con una función como USUARIO_ACTUAL().

#### 9. En el futuro se añade un tercer disparador sobre EXPEDIENTE que también modifica la propia tabla EXPEDIENTE. ¿Qué riesgo hay que vigilar?

- a) Una cadena de disparadores que reactive los otros dos y pueda llegar a una recursión no controlada.
- b) Que el nuevo disparador nunca llegue a ejecutarse, porque una tabla solo admite dos disparadores.
- c) Que los disparadores anteriores pierdan el acceso a los valores ANTIGUO y NUEVO de cada fila.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §4.4

Un disparador que vuelve a modificar la tabla que lo activó puede desencadenar efectos en cascada («trigger chain»), difíciles de depurar y, en el peor caso, recursivos.

#### 10. ¿Qué medida mitiga ese riesgo de forma adecuada?

- a) Añadir nuevos disparadores de control que vigilen y registren la ejecución de los tres anteriores.
- b) Documentar cada disparador, evitar que un AFTER reescriba su propia tabla y probar con cargas masivas.
- c) Probar cada disparador solo con actualizaciones de una fila, para aislar bien el efecto de cada uno.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §4.4

Las buenas prácticas son documentar cada disparador, evitar cascadas profundas y probar el comportamiento ante operaciones masivas, no solo ante cambios de una fila.
