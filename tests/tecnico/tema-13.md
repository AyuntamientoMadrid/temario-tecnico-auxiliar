# Test del tema 13. La gestión de los datos

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-13.html>

## Batería de preguntas

### 1. ¿Por qué se define un Tipo Abstracto de Datos (TAD)?

- a) Por su representación interna en memoria
- b) Por el lenguaje de programación en que se codifica
- c) Por las operaciones que ofrece y su comportamiento, con independencia de la implementación

**Respuesta correcta:** c) · **Referencia:** §1.1 [AHU][LISKOV-GUTTAG]

Un TAD se define por *qué* operaciones ofrece y *qué* hacen (su comportamiento), no por *cómo* se almacenan los datos. La representación es la estructura de datos; el TAD es la especificación.

### 2. El principio que esconde la representación interna de un TAD, exponiendo solo su interfaz pública, se denomina:

- a) Encapsulamiento
- b) Ocultación de la información
- c) Modularidad

**Respuesta correcta:** b) · **Referencia:** §1.2 [LISKOV-GUTTAG]

La **ocultación de la información** (information hiding) hace que la representación interna no sea accesible desde el exterior; solo se expone la interfaz. El encapsulamiento es agrupar datos y operaciones; la ocultación es esconder la representación.

### 3. ¿Cuáles son las tres patas de la especificación de un TAD?

- a) Datos, punteros y memoria
- b) Valores, operaciones y comportamiento
- c) Clases, objetos y herencia

**Respuesta correcta:** b) · **Referencia:** §1.3 [AHU]

Un TAD se especifica por sus **valores** (dominio), sus **operaciones** (interfaz) y su **comportamiento** (axiomas que rigen la semántica).

### 4. El comportamiento de un TAD se formaliza mediante:

- a) Diagramas de flujo
- b) Axiomas (especificación algebraica)
- c) Código fuente en C

**Respuesta correcta:** b) · **Referencia:** §1.3 [AHU][KNUTH-V1]

El comportamiento se expresa con **axiomas ecuacionales** (especificación algebraica) que relacionan las operaciones, sin mencionar ninguna implementación.

### 5. Una propiedad deseable de la modularidad es:

- a) Alta cohesión y bajo acoplamiento
- b) Bajo cohesión y alto acoplamiento
- c) Máximo número de dependencias entre módulos

**Respuesta correcta:** a) · **Referencia:** §1.2

Un buen diseño modular busca **alta cohesión** (cada módulo hace una cosa bien) y **bajo acoplamiento** (mínima dependencia entre módulos).

### 6. ¿Qué relación existe entre un TAD y una estructura de datos?

- a) Son sinónimos exactos
- b) El TAD es la especificación; la estructura de datos es una de sus posibles implementaciones
- c) La estructura de datos es la especificación; el TAD es el código

**Respuesta correcta:** b) · **Referencia:** §1.4

Un mismo TAD admite varias estructuras de datos; por ejemplo, el TAD Pila puede implementarse con un array o con una lista enlazada.

### 7. Los cuatro principios fundamentales en que se sustentan los TAD son:

- a) Herencia, polimorfismo, sobrecarga y composición
- b) Abstracción, encapsulamiento, ocultación y modularidad
- c) Cohesión, acoplamiento, recursividad e iteración

**Respuesta correcta:** b) · **Referencia:** §1.2 [LISKOV-GUTTAG]

Abstracción (qué, no cómo), encapsulamiento (agrupar), ocultación (esconder la representación) y modularidad (descomponer en módulos).

### 8. En Java, el TAD Diccionario se corresponde con la interfaz:

- a) `Map`
- b) `List`
- c) `Queue`

**Respuesta correcta:** a) · **Referencia:** §1.5 [ORACLE-JCF]

El TAD Diccionario (pares clave→valor) se materializa en `Map` (`HashMap`, `TreeMap`). `List` es secuencia; `Queue`, cola FIFO.

### 9. El acceso a un elemento por su índice en un array tiene complejidad:

- a) O(n)
- b) O(1)
- c) O(log n)

**Respuesta correcta:** b) · **Referencia:** §2.2 [WIRTH]

El array permite **acceso directo O(1)**: la dirección se calcula con `B + i × T`, sin recorrer la estructura.

### 10. En un array bidimensional `A[F][C]` almacenado por filas (row-major), la dirección de `A[i][j]` es:

- a) `B + (j × F + i) × T`
- b) `B + (i × C + j) × T`
- c) `B + (i + j) × T`

**Respuesta correcta:** b) · **Referencia:** §2.2

En row-major (C, Java), `dirección = B + (i × C + j) × T`. La fórmula B corresponde a column-major (Fortran).

### 11. Frente a un array, una ventaja de la lista enlazada es:

- a) Acceso por posición en O(1)
- b) Inserción y borrado en O(1) con puntero al nodo
- c) Menor consumo de memoria

**Respuesta correcta:** b) · **Referencia:** §2.3 [KNUTH-V1]

La lista enlazada inserta/borra en O(1) (con puntero al nodo), pero su acceso por posición es O(n) y consume más memoria (punteros).

### 12. Una pila (stack) sigue la política:

- a) FIFO (primero en entrar, primero en salir)
- b) LIFO (último en entrar, primero en salir)
- c) Acceso aleatorio por índice

**Respuesta correcta:** b) · **Referencia:** §2.4 [KNUTH-V1]

La pila es **LIFO**: se apila y desapila por el mismo extremo (la cima). El último en entrar es el primero en salir.

### 13. ¿Qué estructura de datos usa el recorrido en anchura (BFS) de un grafo o árbol?

- a) Una cola
- b) Una pila
- c) Un montículo

**Respuesta correcta:** a) · **Referencia:** §2.6.1, §2.7 [CLRS, cap. 20]

El recorrido por niveles / BFS se implementa con una **cola** (FIFO). El DFS usa pila o recursión.

### 14. Una cola de prioridad se implementa eficientemente con:

- a) Un array desordenado
- b) Una lista enlazada simple
- c) Un montículo (heap)

**Respuesta correcta:** c) · **Referencia:** §2.4, §2.6.4 [CLRS, cap. 6]

El **montículo** permite insertar y extraer el elemento de mayor prioridad en O(log n), lo que lo hace ideal para una cola de prioridad.

### 15. En una tabla hash, una colisión se produce cuando:

- a) La tabla está llena
- b) Dos claves distintas producen el mismo índice
- c) La función hash devuelve un valor negativo

**Respuesta correcta:** b) · **Referencia:** §2.5 [CLRS, cap. 11]

Una colisión es que dos claves diferentes den el mismo índice. Es inevitable (principio del palomar) y se resuelve por encadenamiento o direccionamiento abierto.

### 16. El acceso medio a una tabla hash bien dimensionada es:

- a) O(1)
- b) O(log n)
- c) O(n)

**Respuesta correcta:** a) · **Referencia:** §2.5 [CLRS, cap. 11]

El acceso medio es **O(1)**; el peor caso es O(n) (si todas las claves colisionan en la misma cubeta).

### 17. El factor de carga de una tabla hash se define como:

- a) `α = n/m` (elementos / posiciones)
- b) `α = m/n` (posiciones / elementos)
- c) El número de colisiones totales

**Respuesta correcta:** a) · **Referencia:** §2.5

El factor de carga es **α = n/m** (elementos almacenados / posiciones de la tabla). Cuando supera ~0,75, se hace rehashing.

### 18. El recorrido inorden de un árbol binario de búsqueda (ABB) produce:

- a) Los elementos ordenados
- b) Los elementos en orden aleatorio
- c) Solo las hojas

**Respuesta correcta:** a) · **Referencia:** §2.6.1 [CLRS, cap. 12]

El recorrido **inorden** (Izquierdo-Raíz-Derecho) de un ABB devuelve la secuencia **ordenada** de claves.

### 19. En el recorrido preorden de un árbol binario, ¿qué se visita primero?

- a) El subárbol izquierdo
- b) La raíz
- c) El subárbol derecho

**Respuesta correcta:** b) · **Referencia:** §2.6.1

Preorden = **Raíz** – Izquierdo – Derecho: la raíz se visita antes que los subárboles. En postorden, la raíz va la última.

### 20. ¿Qué le ocurre a un ABB si se insertan claves ya ordenadas y no está autoequilibrado?

- a) Se mantiene equilibrado automáticamente
- b) Degenera en una lista, con operaciones O(n)
- c) Se convierte en un grafo

**Respuesta correcta:** b) · **Referencia:** §2.6.2 [CLRS, cap. 12-13]

Sin equilibrado, insertar datos ordenados hace que el ABB **degenere** en una lista enlazada, y las operaciones pasan de O(log n) a O(n). Por eso existen AVL y rojo-negro.

### 21. ¿Qué estructura es el índice estándar de las bases de datos y muchos sistemas de ficheros?

- a) Lista enlazada
- b) B+árbol
- c) Tabla hash sin colisiones

**Respuesta correcta:** b) · **Referencia:** §2.6.3 [CLRS, cap. 18][FOLK-FILESTRUCT]

El **B+árbol** es el índice por excelencia: equilibrado, con muchas claves por nodo (optimizado para disco) y hojas enlazadas para recorridos por rango.

### 22. En un max-heap almacenado en array, los hijos del nodo en la posición `i` están en:

- a) `i-1` e `i+1`
- b) `i/2` e `i×2`
- c) `2i+1` y `2i+2`

**Respuesta correcta:** c) · **Referencia:** §2.6.4 [CLRS, cap. 6]

En un heap sobre array, los hijos de `i` están en `2i+1` y `2i+2`, y el padre en `⌊(i−1)/2⌋`.

### 23. Para un grafo disperso (pocas aristas), la representación más eficiente en memoria es:

- a) Matriz de adyacencia, O(V²)
- b) Lista de adyacencia, O(V+E)
- c) Tabla hash de vértices

**Respuesta correcta:** b) · **Referencia:** §2.7 [CLRS, cap. 20]

La **lista de adyacencia** ocupa O(V+E), ideal para grafos dispersos. La matriz de adyacencia (O(V²)) conviene a grafos densos.

### 24. El recorrido en profundidad (DFS) de un grafo se apoya en:

- a) Una pila o recursión
- b) Una cola
- c) Un árbol B+

**Respuesta correcta:** a) · **Referencia:** §2.7

El **DFS** usa una **pila** (o recursión, que usa la pila de ejecución). El BFS usa una cola.

### 25. ¿Qué algoritmo calcula el camino de coste mínimo en un grafo ponderado con pesos no negativos?

- a) Dijkstra
- b) Quicksort
- c) Búsqueda binaria

**Respuesta correcta:** a) · **Referencia:** §2.7

El algoritmo de **Dijkstra** resuelve el camino mínimo con pesos no negativos. Bellman-Ford admite pesos negativos.

### 26. Una estructura de datos NO lineal es:

- a) La pila
- b) La cola
- c) El árbol

**Respuesta correcta:** c) · **Referencia:** §2.1

El **árbol** (y el grafo) es no lineal: un elemento puede tener varios sucesores. Pila, cola, array y lista son lineales.

### 27. En la organización secuencial de ficheros, acceder al registro n-ésimo concreto tiene coste:

- a) O(1)
- b) O(n)
- c) O(log n)

**Respuesta correcta:** b) · **Referencia:** §3.2 [FOLK-FILESTRUCT]

En la organización **secuencial** hay que recorrer los registros anteriores → O(n). Es óptima, en cambio, para procesar todo el fichero de una pasada.

### 28. La organización de ficheros que permite acceso directo Y secuencial mediante un índice se denomina:

- a) Directa (hash)
- b) Secuencial indexada (ISAM/VSAM)
- c) Contigua pura

**Respuesta correcta:** b) · **Referencia:** §3.2 [FOLK-FILESTRUCT][TANENBAUM-MOS]

La **secuencial indexada** (ISAM/VSAM) combina un fichero ordenado con un índice (hoy, un B+árbol), permitiendo acceso directo y secuencial.

### 29. En la organización directa (hashing) de ficheros, la posición del registro:

- a) Se busca recorriendo el fichero entero
- b) Siempre coincide con el orden alfabético
- c) Se calcula a partir de su clave con una función hash

**Respuesta correcta:** c) · **Referencia:** §3.3 [KNUTH-V3]

En la organización **directa**, `h(clave)` calcula la dirección → acceso O(1). Inconveniente: no mantiene el orden de las claves.

### 30. Un índice disperso (sparse) tiene:

- a) Una entrada por cada registro
- b) Una entrada por cada campo
- c) Una entrada por cada bloque

**Respuesta correcta:** c) · **Referencia:** §3.4 [SILBERSCHATZ-OS]

El índice **disperso** tiene una entrada por bloque (no por registro), por lo que es más pequeño; requiere datos ordenados. El denso tiene una entrada por registro.

### 31. ¿Qué sistema de ficheros tiene un límite de 4 GB por fichero?

- a) NTFS
- b) FAT32
- c) ext4

**Respuesta correcta:** b) · **Referencia:** §3.5

**FAT32** limita los ficheros a 4 GB. exFAT lo supera; NTFS y ext4 admiten ficheros mucho mayores.

### 32. El mecanismo por el que el sistema de ficheros anota las operaciones en un diario para poder recuperarse tras un fallo se llama:

- a) Striping
- b) Journaling
- c) Defragmentación

**Respuesta correcta:** b) · **Referencia:** §3.6 [SILBERSCHATZ-OS]

El **journaling** registra las operaciones en un diario antes de aplicarlas; tras un corte, rehace o deshace lo pendiente. Lo usan NTFS, ext4 y XFS.

### 33. ¿Qué nivel RAID ofrece striping SIN ninguna redundancia?

- a) RAID 1
- b) RAID 5
- c) RAID 0

**Respuesta correcta:** c) · **Referencia:** §3.6 [PATTERSON-RAID]

**RAID 0** reparte los datos (striping) para máximo rendimiento, pero sin redundancia: el fallo de un disco pierde todo.

### 34. RAID 5 utiliza:

- a) Paridad distribuida, tolerando el fallo de un disco
- b) Espejo completo de los datos
- c) Doble paridad, tolerando dos fallos

**Respuesta correcta:** a) · **Referencia:** §3.6 [SNIA-RAID]

**RAID 5** usa **paridad distribuida** y tolera el fallo de **un** disco (mínimo 3). La doble paridad (2 fallos) es RAID 6.

### 35. Cuatro discos de 4 TB en RAID 5 ofrecen una capacidad útil de:

- a) 16 TB
- b) 8 TB
- c) 12 TB

**Respuesta correcta:** c) · **Referencia:** §3.6

Capacidad útil = `(n−1)/n × total = 3/4 × 16 = 12 TB` (el equivalente a un disco se dedica a paridad).

### 36. ¿Cuál de estas afirmaciones sobre RAID es correcta?

- a) El RAID no sustituye a la copia de seguridad
- b) El RAID sustituye a la copia de seguridad
- c) RAID 1 no tolera ningún fallo

**Respuesta correcta:** a) · **Referencia:** §3.6

El RAID protege frente a fallos de disco, pero **no** frente a borrados, ransomware o desastres: **no sustituye al backup**. RAID 1 (espejo) sí tolera 1 fallo.

### 37. El método de asignación de espacio en disco que usa un bloque índice (inodo/MFT) con punteros a los bloques del fichero es la asignación:

- a) Indexada
- b) Contigua
- c) Enlazada

**Respuesta correcta:** a) · **Referencia:** §3.5 [SILBERSCHATZ-OS]

La asignación **indexada** usa un bloque índice (inodo en Unix, registro MFT en NTFS) con los punteros a los bloques. Es la de ext4, NTFS y APFS.

### 38. El sistema de ficheros que emplea copy-on-write y snapshots en macOS/iOS es:

- a) FAT32
- b) NTFS
- c) APFS

**Respuesta correcta:** c) · **Referencia:** §3.5, §3.6 [APFS-REF]

**APFS** (Apple File System) usa copy-on-write, snapshots y clones. ZFS también usa COW; NTFS usa journaling.

### 39. ¿Cuál de estas NO es una propiedad obligatoria de un algoritmo según Knuth?

- a) Finitud
- b) Recursividad
- c) Efectividad

**Respuesta correcta:** b) · **Referencia:** §4.1 [KNUTH-V1]

Las propiedades son finitud, definición, entrada, salida y efectividad. La **recursividad** es una técnica, no un requisito (un algoritmo puede ser iterativo).

### 40. La notación que expresa la cota superior (peor caso) de la complejidad es:

- a) O grande
- b) Omega (Ω)
- c) Theta (Θ)

**Respuesta correcta:** a) · **Referencia:** §4.2 [CLRS, cap. 3]

**O grande** es la cota superior (no crece más que g(n)). Ω es la cota inferior y Θ la cota ajustada.

### 41. Ordena de menor a mayor crecimiento estas complejidades: O(n²), O(1), O(n log n), O(log n).

- a) O(log n) < O(1) < O(n²) < O(n log n)
- b) O(1) < O(n²) < O(log n) < O(n log n)
- c) O(1) < O(log n) < O(n log n) < O(n²)

**Respuesta correcta:** c) · **Referencia:** §4.2

La jerarquía es O(1) < O(log n) < O(n) < O(n log n) < O(n²) < … Memorizarla es de alto rendimiento.

### 42. Todo algoritmo recursivo debe tener obligatoriamente:

- a) Un caso base que detiene la recursión
- b) Un único parámetro
- c) Más de dos llamadas recursivas

**Respuesta correcta:** a) · **Referencia:** §4.3 [CLRS, cap. 4]

Necesita un **caso base** (que detiene) y un caso recursivo que converge hacia él. Sin caso base se produce stack overflow.

### 43. ¿Dónde se apilan los marcos de activación de las llamadas recursivas?

- a) En la cola de tareas
- b) En la pila de ejecución
- c) En el montículo de prioridad

**Respuesta correcta:** b) · **Referencia:** §4.3, §2.4

Cada llamada recursiva apila un marco de activación en la **pila de ejecución**. Una recursión que no converge la desborda (stack overflow).

### 44. ¿Cuál de estos algoritmos de ordenación es O(n²) en el caso medio?

- a) Inserción
- b) Mergesort
- c) Heapsort

**Respuesta correcta:** a) · **Referencia:** §4.4.1, §4.4.4

La **inserción** (como burbuja y selección) es O(n²). Mergesort y heapsort son O(n log n).

### 45. ¿Qué algoritmo de ordenación garantiza O(n log n) y es estable, pero requiere O(n) de memoria auxiliar?

- a) Mergesort
- b) Quicksort
- c) Burbuja

**Respuesta correcta:** a) · **Referencia:** §4.4.2 [CLRS, cap. 2]

**Mergesort** garantiza O(n log n) y es estable, pero necesita O(n) de memoria para la mezcla. Ideal para ordenación externa.

### 46. El peor caso de quicksort es:

- a) O(n log n)
- b) O(log n)
- c) O(n²)

**Respuesta correcta:** c) · **Referencia:** §4.4.2 [CLRS, cap. 7]

Quicksort es O(n log n) de media, pero **O(n²)** en el peor caso (pivote sistemáticamente mal elegido). Es in-place y muy rápido en la práctica.

### 47. ¿Qué algoritmo de ordenación es O(n log n) garantizado e in-place (memoria O(1))?

- a) Mergesort
- b) Inserción
- c) Heapsort

**Respuesta correcta:** c) · **Referencia:** §4.4.2 [CLRS, cap. 6]

**Heapsort** garantiza O(n log n) y es in-place, aunque no es estable. Mergesort gasta O(n); inserción es O(n²).

### 48. El límite teórico inferior de la ordenación por comparación es:

- a) Ω(n)
- b) Ω(n²)
- c) Ω(n log n)

**Respuesta correcta:** c) · **Referencia:** §4.4.4 [CLRS, cap. 8]

Ningún algoritmo de ordenación **por comparación** puede bajar de **Ω(n log n)**. Los no comparativos (counting, radix) lo evitan usando el valor como índice.

### 49. La búsqueda binaria tiene complejidad O(log n) pero exige que:

- a) Los datos estén en una lista enlazada
- b) Haya menos de 100 elementos
- c) Los datos estén ordenados

**Respuesta correcta:** c) · **Referencia:** §4.5.2 [KNUTH-V3]

La **búsqueda binaria** requiere datos **ordenados** y de acceso directo (array). Si no, hay que ordenarlos antes o usar búsqueda secuencial.

### 50. Buscar un valor en un vector ordenado de 1.000.000 de elementos con búsqueda binaria requiere, como máximo, unas:

- a) 20 comparaciones
- b) 1.000 comparaciones
- c) 1.000.000 comparaciones

**Respuesta correcta:** a) · **Referencia:** §4.5.2

⌈log₂(1.000.000)⌉ ≈ **20** comparaciones. La secuencial necesitaría hasta 1.000.000.

### 51. La búsqueda secuencial (lineal) es la única posible cuando:

- a) Los datos están ordenados en un array
- b) Se usa una tabla hash
- c) Los datos no están ordenados o están en una lista enlazada

**Respuesta correcta:** c) · **Referencia:** §4.5.1

Sobre datos **no ordenados** o estructuras de acceso secuencial (listas, ficheros secuenciales), solo cabe la búsqueda secuencial O(n).

### 52. La búsqueda por interpolación, frente a la binaria, es más rápida cuando los datos:

- a) Están ordenados y uniformemente distribuidos
- b) Están desordenados
- c) Son de tipo texto

**Respuesta correcta:** a) · **Referencia:** §4.5.3 [KNUTH-V3]

La **interpolación** estima la posición y alcanza O(log log n) de media si los datos están ordenados y **uniformemente distribuidos**.

### 53. El formato de un fichero determina:

- a) El tamaño físico del disco
- b) La velocidad del procesador
- c) Cómo se interpretan sus bytes (su significado)

**Respuesta correcta:** c) · **Referencia:** §5.1

El **formato** es el convenio que determina cómo deben interpretarse los bytes. Sin conocer el formato, una secuencia de bytes carece de significado.

### 54. En la codificación UTF-8, la letra "ñ" (U+00F1) ocupa:

- a) 2 bytes
- b) 1 byte
- c) 4 bytes

**Respuesta correcta:** a) · **Referencia:** §5.2 [UNICODE-STD]

Los code points entre U+0080 y U+07FF se codifican en **2 bytes** en UTF-8 (la "ñ" es C3 B1). Los caracteres ASCII ocupan 1 byte.

### 55. El orden de bytes "big-endian" se caracteriza por colocar primero el byte:

- a) Menos significativo
- b) De paridad
- c) Más significativo

**Respuesta correcta:** c) · **Referencia:** §5.1

**Big-endian** coloca el byte más significativo primero (orden de red). Little-endian (x86) coloca primero el menos significativo.

### 56. ¿Qué identifica de forma fiable el tipo real de un fichero, con independencia de su extensión?

- a) El nombre del fichero
- b) La fecha de creación
- c) El número mágico (bytes iniciales)

**Respuesta correcta:** c) · **Referencia:** §5.4 [LIBMAGIC]

El **número mágico** (primeros bytes, p. ej. `%PDF`, `PK`, `89 50 4E 47` de PNG) identifica el formato real. La extensión es solo una convención del nombre.

### 57. La normativa de la Administración (ENI) obliga, para garantizar la conservación, a usar:

- a) Formatos propietarios cerrados
- b) Únicamente formatos comprimidos con pérdida
- c) Formatos abiertos y estándar (PDF/A, ODF, XML)

**Respuesta correcta:** c) · **Referencia:** §5.3 [ENI-RD4-2010][NTI-FORMATOS]

El **Esquema Nacional de Interoperabilidad** exige **formatos abiertos y estándar** (PDF/A para archivo, ODF, XML/JSON/CSV).

### 58. El permiso POSIX `chmod 640` sobre un fichero significa:

- a) Propietario rwx, grupo rwx, otros rwx
- b) Propietario r--, grupo rw-, otros rwx
- c) Propietario rw-, grupo r--, otros ---

**Respuesta correcta:** c) · **Referencia:** §5.5.1 [POSIX]

6 = rw- (propietario), 4 = r-- (grupo), 0 = --- (otros). Es el permiso típico de un documento confidencial de solo lectura para el grupo.

### 59. En el modelo de permisos NTFS basado en ACL, ante un conflicto:

- a) Prevalece la denegación explícita
- b) Prevalece siempre el permiso
- c) Se ignoran ambas reglas

**Respuesta correcta:** a) · **Referencia:** §5.5.2 [MS-NTFS]

En NTFS, la **denegación explícita prevalece** sobre el permiso. Las ACL admiten reglas por usuario concreto y herencia desde la carpeta padre.

### 60. Cuando el control de acceso del sistema operativo no protege (p. ej. robo físico del disco), la medida adecuada es:

- a) Cifrar la información (EFS, BitLocker, LUKS)
- b) Cambiar la extensión de los ficheros
- c) Comprimir los ficheros con ZIP

**Respuesta correcta:** a) · **Referencia:** §5.5.3 [ENS-RD311]

Ante el robo del disco (que evita el SO), la protección es el **cifrado** a nivel de fichero (EFS) o de volumen (BitLocker, LUKS, FileVault).

## Preguntas sobre los casos prácticos

### Caso 1. El fichero del Padrón Municipal de Habitantes

#### 1. Para la consulta de un habitante por su DNI/NIE en el fichero del Padrón (unos 3,3 millones de registros), ¿qué organización de fichero es la más adecuada?

- a) Secuencial indexada, con un índice que permita el acceso directo por DNI/NIE.
- b) Secuencial pura, con los registros grabados por orden de fecha de alta.
- c) Enlazada, con cada registro apuntando al siguiente de su mismo distrito.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §3.2

La organización secuencial indexada combina el fichero de datos con índices que permiten el acceso directo por clave además del secuencial.

#### 2. ¿Por qué no bastaría una organización secuencial pura para esa consulta?

- a) Porque no admite registros de longitud variable como el nombre y los apellidos del habitante.
- b) Porque obligaría a recorrer hasta 3,3 millones de registros en cada consulta, con coste O(n).
- c) Porque solo puede utilizarse sobre soportes de cinta y no sobre discos ni sobre SSD.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §3.2

En un fichero secuencial, para leer un registro concreto hay que recorrer los anteriores: el acceso es O(n), lento para consultas individuales.

#### 3. ¿Qué índice crearía sobre el DNI/NIE y con qué complejidad de acceso?

- a) Un árbol binario de búsqueda sin equilibrar, con acceso O(1).
- b) Un montículo (heap) sobre el DNI/NIE, con acceso O(n log n).
- c) Un índice primario B+árbol, con acceso O(log n).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.6.3, §3.4

El B+árbol es el índice estándar de ficheros y bases de datos: equilibrado, con muchas claves por nodo y acceso O(log n).

#### 4. ¿Cuántos accesos a disco necesita, aproximadamente, localizar a un habitante con ese índice?

- a) 3-4 accesos, la altura del árbol.
- b) Unos 20 accesos, como un árbol binario.
- c) Hasta 3,3 millones, uno por registro.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §3.4

Al almacenar muchas claves por nodo, el B+árbol tiene pocos niveles: con 3,3 millones de registros basta con 3-4 accesos a disco.

#### 5. Para la operación 2 (listar a todos los habitantes de un distrito), conviene:

- a) Recorrer el fichero completo ordenado por DNI/NIE y filtrar por distrito.
- b) Una tabla hash sobre el DNI/NIE, que localiza cada registro en O(1).
- c) Un índice secundario sobre el distrito, para no recorrer todo el fichero.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §3.4

Un índice secundario por distrito permite listar los habitantes de un distrito sin recorrer los 3,3 millones de registros; el índice por DNI no sirve para esa consulta.

#### 6. ¿Qué característica del B+árbol facilita los recorridos por rango?

- a) Que sus nodos internos guardan los registros completos y no solo claves-guía.
- b) Que sus hojas, donde están todas las claves, están enlazadas en una lista ordenada.
- c) Que calcula la posición de cada clave con una función hash que mantiene el orden.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.6.3

En el B+árbol todas las claves de datos están en las hojas, enlazadas formando una lista ordenada; los nodos internos solo tienen claves-guía.

#### 7. Para validar en tiempo real, durante un alta, si un DNI ya existe, ¿qué estructura elegiría?

- a) Una tabla hash (o el índice único sobre DNI), con coste medio O(1).
- b) Una búsqueda secuencial sobre el fichero, con coste medio O(n/2).
- c) Una lista enlazada ordenada por DNI, con coste medio O(log n).

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §2.5, §4.5.4

Comprobar si una clave existe en una tabla hash cuesta O(1) de media, idóneo para una validación inmediata durante el alta.

#### 8. Ese coste O(1) es el del caso medio. ¿Qué coste tendría la comprobación en el peor caso, si todas las claves colisionaran en la misma posición?

- a) O(log n).
- b) O(n).
- c) O(n²).

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §2.5

En una tabla hash el acceso medio es O(1), pero si todas las claves colisionan en la misma posición la búsqueda degenera a O(n).

#### 9. ¿En qué operaciones se nota el coste de mantener varios índices sobre el Padrón?

- a) En las consultas por DNI/NIE, porque deben consultarse todos los índices.
- b) En los listados por distrito, porque el índice secundario se recalcula entero.
- c) En las altas, bajas y modificaciones, porque cada índice debe actualizarse.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 4 · §3.4

Cada índice acelera un tipo de consulta a costa de espacio y de un coste de mantenimiento en altas, bajas y modificaciones.

#### 10. ¿Cómo justificaría ese coste ante un responsable?

- a) Las consultas, mucho más frecuentes que las altas, pasan de O(n) a O(log n) u O(1).
- b) Los índices reducen el espacio total que ocupa el fichero del Padrón en el disco.
- c) Los índices evitan tener que actualizar el fichero de datos cuando se producen altas.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §3.4

El balance favorece los índices: penalizan algo las altas, pero aceleran las consultas, que son mucho más frecuentes; además ocupan espacio adicional, no lo reducen.

### Caso 2. Procesamiento del censo electoral

#### 1. El censo de 200.000 electores no cabe cómodamente en memoria y hay que conservar el orden previo por segundo apellido. ¿Qué algoritmo de ordenación elegiría?

- a) Quicksort.
- b) Mergesort.
- c) Heapsort.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §4.4.2

Mergesort es O(n log n) garantizado, estable y apto para ordenación externa, porque se basa en mezclar bloques ya ordenados.

#### 2. ¿Qué propiedades justifican esa elección?

- a) Es in situ, no necesita memoria adicional y es el más rápido en la práctica.
- b) Es O(n) en todos los casos porque usa el valor de la clave como índice.
- c) Es O(n log n) garantizado, estable y apto para ordenación externa.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §4.4.2

Mergesort garantiza O(n log n), es estable y se usa para ficheros que no caben en memoria; ser in situ y el más rápido en la práctica describe a quicksort, y el O(n) sin comparar claves, a los algoritmos no comparativos.

#### 3. ¿Por qué se descarta quicksort en este caso, aunque sea rápido?

- a) Porque no es estable y degrada a O(n²) en el peor caso.
- b) Porque es estable pero necesita memoria auxiliar O(n).
- c) Porque solo ordena claves numéricas de rango acotado.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §4.4.2

Quicksort es O(n log n) de media pero O(n²) en el peor caso, y no es estable: no garantiza conservar el orden por segundo apellido.

#### 4. Heapsort también garantiza O(n log n). ¿Por qué no sirve aquí?

- a) Porque necesita memoria auxiliar O(n).
- b) Porque no es estable.
- c) Porque degrada a O(n²) en el peor caso.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §4.4.2, §4.4.4

Heapsort es O(n log n) garantizado e in situ, pero no es estable, así que no conservaría el orden previo por segundo apellido.

#### 5. ¿Qué inconveniente tiene mergesort que conviene tener en cuenta al dimensionar el sistema?

- a) Requiere memoria auxiliar O(n) para la fase de mezcla.
- b) No es estable cuando hay apellidos repetidos en el censo.
- c) Degrada a O(n²) si el censo ya viene casi ordenado.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §4.4.2

Mergesort es estable y garantiza O(n log n) en todos los casos, pero gasta memoria auxiliar O(n) para mezclar.

#### 6. ¿Qué significa que un algoritmo de ordenación sea estable?

- a) Que su tiempo de ejecución no varía con el orden inicial de los datos.
- b) Que ordena sin necesitar memoria adicional a la del propio vector.
- c) Que conserva el orden relativo de los elementos con clave igual.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §4.4

Un algoritmo es estable si conserva el orden relativo de los elementos con clave igual; ordenar sin memoria adicional es ser in situ.

#### 7. ¿Por qué es relevante la estabilidad al ordenar el censo por primer apellido?

- a) Porque sin ella el algoritmo no podría ordenar a los electores que tienen dos apellidos compuestos.
- b) Porque los electores con igual primer apellido deben mantener el orden por segundo apellido ya fijado.
- c) Porque un algoritmo estable ordena el censo en O(n), más rápido que uno que no lo es.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.4

Al ordenar por varios criterios sucesivos, solo un algoritmo estable garantiza que, a igual primer apellido, se conserve el orden por segundo apellido de la pasada anterior.

#### 8. Durante la jornada electoral hay que localizar a un elector por su posición alfabética. ¿Qué algoritmo de búsqueda se aplica y qué requisito impone?

- a) Búsqueda secuencial, O(log n), que exige que el censo esté ordenado.
- b) Búsqueda binaria, O(n), que no exige ningún orden previo del censo.
- c) Búsqueda binaria, O(log n), que exige que el censo esté ordenado.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §4.5.2

La búsqueda binaria divide a la mitad el espacio de búsqueda en cada paso (O(log n)), pero exige datos ordenados; la secuencial es O(n) y no requiere orden.

#### 9. Para 200.000 electores, ¿cuántas comparaciones necesita como máximo la búsqueda binaria, frente a la secuencial?

- a) Unas 18, frente a hasta 200.000 de la secuencial.
- b) Unas 100.000, frente a hasta 200.000 de la secuencial.
- c) Unas 448, frente a hasta 200.000 de la secuencial.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §4.5.2

La binaria necesita a lo sumo ⌈log₂(200.000)⌉ = 18 comparaciones (2¹⁸ = 262.144); la secuencial puede necesitar recorrer los 200.000.

#### 10. Si un proceso auxiliar fuese O(n²), ¿de qué orden sería el número de operaciones con n = 200.000?

- a) Del orden de 4 × 10⁵ operaciones.
- b) Del orden de 4 × 10¹⁰ operaciones.
- c) Del orden de 3,5 × 10⁶ operaciones.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §4.2

n² = (2 × 10⁵)² = 4 × 10¹⁰; 4 × 10⁵ sería 2n, y unos 3,5 × 10⁶ corresponden a n log₂ n.

### Caso 3. Gestión documental segura en la sede electrónica

#### 1. ¿Qué formato de fichero exigiría para los documentos de archivo de la sede electrónica?

- a) DOCX.
- b) JPEG.
- c) PDF/A.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §5.3

PDF/A es el formato para documentos de archivo: autocontenido, sin dependencias externas y pensado para la conservación a largo plazo.

#### 2. ¿De qué normativa procede la obligación de usar formatos abiertos y estándar en la Administración?

- a) Del Esquema Nacional de Interoperabilidad (RD 4/2010) y la Norma Técnica de Catálogo de estándares.
- b) Del Esquema Nacional de Seguridad y de la norma técnica de control de acceso a los ficheros.
- c) Del Reglamento de los Servicios de Prevención y de la norma técnica de digitalización.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §5.3 [ENI-RD4-2010]

El Esquema Nacional de Interoperabilidad y la Norma Técnica de Catálogo de estándares obligan a usar formatos abiertos y estándar para la conservación y el acceso a largo plazo.

#### 3. Solo el funcionario instructor debe poder modificar el expediente, su unidad consultarlo y el resto no tener acceso. ¿Qué permiso POSIX lo implementa?

- a) chmod 750.
- b) chmod 640.
- c) chmod 664.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §5.5.1

640 equivale a rw- para el propietario, r-- para el grupo y --- para otros; 750 da ejecución y 664 permite escribir al grupo y leer a otros.

#### 4. Con ese esquema, ¿qué pueden hacer los miembros de la unidad del instructor?

- a) Leer y modificar el expediente.
- b) Ni leer ni modificar el expediente.
- c) Leer el expediente, pero no modificarlo.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §5.5.1

El dígito 4 del grupo equivale a r--: solo lectura.

#### 5. En un entorno Windows/NTFS, un usuario de otra unidad tiene permiso de lectura a través de un grupo, pero también una denegación explícita sobre el expediente. ¿Qué ocurre?

- a) Puede leerlo, porque el permiso del grupo prevalece sobre la denegación.
- b) No puede acceder, porque la denegación explícita prevalece sobre el permiso.
- c) Puede leerlo, porque en NTFS se aplica el permiso concedido en primer lugar.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §5.5.2

En el modelo ACL de NTFS, las reglas de denegación explícita prevalecen sobre las de permiso.

#### 6. ¿Qué mecanismo emplearía para detectar si un documento se ha alterado tras su firma?

- a) Una función hash criptográfica, como SHA-256.
- b) Una suma de verificación simple, como un CRC.
- c) Un algoritmo de compresión sin pérdida, como GZIP.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §5.3

Con una función hash criptográfica cualquier alteración del documento cambia radicalmente su huella, lo que permite detectar manipulaciones.

#### 7. ¿Por qué no basta con un checksum o CRC simple para esta finalidad?

- a) Porque no detecta los errores de transmisión ni de almacenamiento del documento.
- b) Porque solo puede calcularse sobre ficheros de texto plano y no sobre PDF/A.
- c) Porque detecta errores accidentales, pero no resiste una manipulación intencionada.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §5.3

Los checksums y CRC detectan errores de transmisión o almacenamiento, pero no resisten la manipulación intencionada.

#### 8. Un proveedor propone calcular las huellas de los documentos con MD5. ¿Es adecuado?

- a) No, porque MD5 se considera obsoleta por colisiones demostradas.
- b) Sí, porque MD5 es una función hash criptográfica como SHA-256.
- c) Sí, siempre que se combine con un CRC sobre el mismo documento.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §5.3

MD5 y SHA-1 se consideran obsoletas por colisiones demostradas; para integridad se usan SHA-256 o SHA-3.

#### 9. ¿Qué configuración de almacenamiento permite seguir operando ante el fallo de un disco?

- a) RAID 0, con reparto de datos, que tolera el fallo de un disco.
- b) RAID 5, con paridad distribuida, que tolera el fallo de un disco.
- c) Un único disco con journaling, que tolera el fallo de ese disco.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §3.6

RAID 5 reparte los datos con paridad distribuida y tolera el fallo de un disco; RAID 0 no tiene redundancia y el journaling protege la consistencia, no frente a la pérdida del disco.

#### 10. ¿Sustituye ese RAID a la copia de seguridad de los expedientes?

- a) Sí, porque con la paridad se pueden reconstruir siempre todos los datos perdidos.
- b) Sí, siempre que se use RAID 6, que tolera el fallo simultáneo de dos discos.
- c) No, porque protege del fallo de disco, pero no de borrados, ransomware ni desastres.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §3.6

El RAID protege de fallos de disco, pero no de borrados, ransomware ni desastres: hace falta, además, copia de seguridad.
