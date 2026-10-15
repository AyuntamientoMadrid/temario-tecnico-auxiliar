# Test del tema 18. Lenguajes de programación

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-18.html>

## Batería de preguntas

### 1. ¿Qué es un lenguaje de programación de alto nivel?

- a) Una notación cercana al lenguaje humano e independiente de la máquina, que necesita un traductor
- b) El conjunto de instrucciones en binario que ejecuta directamente el procesador
- c) Un lenguaje que solo funciona en una arquitectura de CPU concreta

**Respuesta correcta:** a) · **Referencia:** §1.2 [SEBESTA]

El alto nivel abstrae el hardware; el binario (B) y el dependiente de la CPU (C) son de bajo nivel.

### 2. La diferencia fundamental entre un algoritmo y un programa es que:

- a) Son sinónimos exactos, no hay diferencia
- b) El algoritmo es la secuencia lógica de pasos, independiente del lenguaje; el programa es ese algoritmo escrito en un lenguaje ejecutable
- c) El programa es más abstracto que el algoritmo

**Respuesta correcta:** b) · **Referencia:** §1.1 [SEBESTA]

Un mismo algoritmo puede programarse en C, Java o Python.

### 3. ¿Cuáles son los tres componentes con que se define todo lenguaje de programación?

- a) Compilador, intérprete y ensamblador
- b) Variables, funciones y bucles
- c) Léxico, sintaxis y semántica

**Respuesta correcta:** c) · **Referencia:** §1.1 [ASU]

Vocabulario (léxico), reglas gramaticales (sintaxis) y significado (semántica), igual que un lenguaje natural.

### 4. En la clasificación por generaciones, SQL es un ejemplo típico de:

- a) Lenguaje de 2.ª generación (ensamblador)
- b) Lenguaje de 4.ª generación (declarativo)
- c) Lenguaje de 1.ª generación (máquina)

**Respuesta correcta:** b) · **Referencia:** §1.2 [PRATT]

Los 4GL son declarativos: se indica QUÉ se quiere, no CÓMO obtenerlo. SQL es el ejemplo clásico.

### 5. ¿Qué caracteriza a un lenguaje del paradigma imperativo frente a uno declarativo?

- a) El imperativo solo se usa en inteligencia artificial
- b) El imperativo no admite variables
- c) En el imperativo se indica CÓMO resolver el problema (los pasos); en el declarativo, QUÉ se quiere obtener

**Respuesta correcta:** c) · **Referencia:** §1.2 [SEBESTA]

El declarativo (SQL, Prolog) deja el «cómo» al sistema.

### 6. ¿Cuál es la diferencia entre un compilador y un intérprete?

- a) El compilador traduce el programa completo antes de ejecutarlo; el intérprete traduce y ejecuta instrucción a instrucción
- b) El compilador es más lento porque traduce línea a línea
- c) El intérprete genera siempre un fichero ejecutable independiente

**Respuesta correcta:** a) · **Referencia:** §1.2 [SEBESTA]

El compilador detecta muchos errores antes de ejecutar; el intérprete los revela en ejecución.

### 7. El modelo de ejecución de Java («compile once, run anywhere») se basa en:

- a) Interpretar directamente el código fuente sin traducirlo
- b) Compilar a código máquina específico de cada procesador
- c) Compilar a un código intermedio (bytecode) que ejecuta una máquina virtual (JVM)

**Respuesta correcta:** c) · **Referencia:** §1.2 [SEBESTA]

Es un modelo híbrido: portabilidad del bytecode + compilación JIT para rendimiento.

### 8. La descripción formal de la sintaxis de un lenguaje suele expresarse mediante:

- a) Gramáticas en notación BNF (Backus-Naur Form)
- b) Tablas de verdad booleanas
- c) Diagramas entidad-relación

**Respuesta correcta:** a) · **Referencia:** §1.4 [ASU]

La BNF define reglas de producción que el análisis sintáctico del compilador comprueba.

### 9. Escribir <code>resultado = total / num</code> cuando <code>num</code> vale 0 constituye un:

- a) Error de sintaxis detectado al compilar
- b) Error semántico dinámico (se manifiesta al ejecutar)
- c) Error de estilo o pragmática, sin consecuencias

**Respuesta correcta:** b) · **Referencia:** §1.4 [SCOTT]

La sentencia es sintácticamente correcta; el fallo (división por cero) aparece en tiempo de ejecución.

### 10. ¿Qué es un identificador en un lenguaje de programación?

- a) El nombre que el programador da a variables, constantes, funciones o tipos
- b) Un valor numérico fijo que no puede cambiar
- c) Un símbolo que representa una operación aritmética

**Respuesta correcta:** a) · **Referencia:** §1.5 [SEBESTA]

Suele distinguir mayúsculas de minúsculas y no puede coincidir con una palabra reservada.

### 11. ¿Cuál es la diferencia entre una variable y una constante?

- a) La constante ocupa más memoria que la variable
- b) La variable puede cambiar de valor durante la ejecución; la constante mantiene fijo su valor
- c) La variable no tiene tipo y la constante sí

**Respuesta correcta:** b) · **Referencia:** §1.5 [MCCONNELL]

Usar constantes con nombre evita «números mágicos» y mejora el mantenimiento.

### 12. En programación, ¿qué distingue a una expresión de una sentencia?

- a) La sentencia siempre ocupa una sola línea; la expresión, varias
- b) Solo las expresiones pueden contener variables
- c) Una expresión se evalúa y produce un valor; una sentencia se ejecuta y produce un efecto

**Respuesta correcta:** c) · **Referencia:** §1.6 [SEBESTA]

<code>x + 1</code> es expresión; <code>x = x + 1</code> es una sentencia de asignación.

### 13. Un tipo de dato se define como:

- a) La cantidad de memoria RAM instalada en el equipo
- b) Un conjunto de valores posibles junto con las operaciones permitidas sobre ellos
- c) El nombre que damos a una variable

**Respuesta correcta:** b) · **Referencia:** §2.1 [PIERCE]

El tipo acota valores, fija la memoria ocupada y permite detectar errores.

### 14. ¿Cuál de los siguientes es un tipo de dato simple o primitivo?

- a) El registro (struct)
- b) El array o vector
- c) El booleano

**Respuesta correcta:** c) · **Referencia:** §2.2 [SEBESTA]

Booleano, entero, real y carácter son primitivos (atómicos); array y registro son estructurados.

### 15. Los números reales se representan en los computadores según la norma:

- a) IEEE 754 (coma flotante), con precisión finita
- b) ASCII de 7 bits
- c) Complemento a dos exacto sin pérdida

**Respuesta correcta:** a) · **Referencia:** §2.2 [IEEE754]

Por eso no todos los decimales son exactos y no se deben comparar reales con <code>=</code> directamente.

### 16. ¿Por qué no conviene comparar dos números reales con el operador de igualdad <code>==</code>?

- a) Porque el operador <code>==</code> no existe para reales en ningún lenguaje
- b) Porque los reales siempre son negativos
- c) Porque su representación en coma flotante es aproximada; se compara si su diferencia es menor que una tolerancia

**Respuesta correcta:** c) · **Referencia:** §2.2 [IEEE754]

Se usa <code>|a − b| &lt; ε</code> en lugar de <code>a == b</code>.

### 17. Para almacenar importes de dinero (tributos, tasas) sin errores de redondeo, se recomienda:

- a) Usar entero de céntimos o un tipo decimal exacto, no coma flotante
- b) Usar siempre variables de tipo carácter
- c) Usar coma flotante de doble precisión, que es exacta

**Respuesta correcta:** a) · **Referencia:** §2.2 [IEEE754]

Un error de un céntimo por recibo, multiplicado por miles, es un problema contable real.

### 18. Un tipo enumerado (enum) como <code>ESTADO = {ABIERTO, EN_TRAMITE, RESUELTO}</code> sirve para:

- a) Almacenar números reales con muchos decimales
- b) Definir un conjunto fijo de valores con nombre, mejorando la legibilidad frente a usar números
- c) Reservar memoria dinámica en el montículo

**Respuesta correcta:** b) · **Referencia:** §2.3 [SEBESTA]

Es un tipo definido por el usuario.

### 19. La conversión de tipo que realiza automáticamente el lenguaje, normalmente ampliando de un tipo menor a uno mayor sin pérdida, se llama:

- a) Conversión implícita o coerción
- b) Conversión explícita o cast forzado
- c) Truncamiento manual

**Respuesta correcta:** a) · **Referencia:** §2.4 [SCOTT]

Ejemplo: en <code>3 + 2.5</code> el entero <code>3</code> se convierte a <code>3.0</code> automáticamente (widening).

### 20. Python es un lenguaje de tipado fuerte y dinámico. Esto significa que:

- a) El tipo se comprueba en compilación y permite mezclar tipos libremente
- b) Controla las mezclas de tipos incoherentes (fuerte) y el tipo se asocia al valor y se comprueba en ejecución (dinámico)
- c) No tiene tipos de datos

**Respuesta correcta:** b) · **Referencia:** §2.4 [PIERCE]

Fuerte/débil y estático/dinámico son ejes independientes.

### 21. Los ejes «fuerte/débil» y «estático/dinámico» de un sistema de tipos:

- a) Son exactamente lo mismo expresado de dos formas
- b) Solo se aplican a lenguajes compilados
- c) Son independientes: uno mide cuán estricto es con las mezclas de tipos, el otro cuándo se comprueba el tipo

**Respuesta correcta:** c) · **Referencia:** §2.4 [PIERCE]

Python es fuerte y dinámico; C es estático y relativamente débil.

### 22. En un lenguaje con división entera, ¿qué vale <code>resultado</code> tras <code>entero a=7; entero b=2; real resultado = a / b;</code>?

- a) 3.5, porque el resultado es real
- b) Da error de compilación siempre
- c) 3.0, porque la división se hace primero entre enteros (7/2=3) y luego se convierte a real

**Respuesta correcta:** c) · **Referencia:** §2.4 [SCOTT]

Para obtener 3.5 hay que convertir ANTES de dividir: <code>(real)a / b</code>.

### 23. El operador módulo (<code>mod</code>, <code>%</code>) devuelve:

- a) El resto de la división entera entre dos números
- b) El cociente sin decimales
- c) La potencia del primer número elevado al segundo

**Respuesta correcta:** a) · **Referencia:** §3.1 [SEBESTA]

<code>n mod 2 == 0</code> comprueba si <code>n</code> es par.

### 24. ¿Qué operador se usa para comprobar si un número <code>n</code> es par?

- a) <code>n / 2 == 0</code>
- b) <code>n mod 2 == 0</code>
- c) <code>n ^ 2 == 0</code>

**Respuesta correcta:** b) · **Referencia:** §3.1 [SEBESTA]

Si el resto de dividir entre 2 es cero, el número es par.

### 25. Los operadores relacionales (<code>&lt;</code>, <code>&gt;</code>, <code>==</code>, <code>!=</code>) devuelven un valor de tipo:

- a) Entero
- b) Booleano (verdadero o falso)
- c) Carácter

**Respuesta correcta:** b) · **Referencia:** §3.2 [SEBESTA]

Comparan dos valores y producen el resultado de la comparación.

### 26. El error de escribir <code>si (x = 5)</code> en lugar de <code>si (x == 5)</code> consiste en:

- a) Confundir el operador de asignación (<code>=</code>, guarda un valor) con el de comparación (<code>==</code>, pregunta si son iguales)
- b) Usar un operador que no existe
- c) Escribir un comentario mal cerrado

**Respuesta correcta:** a) · **Referencia:** §3.2 [SEBESTA]

En muchos lenguajes no da error de compilación y provoca un fallo lógico difícil de detectar.

### 27. La evaluación en cortocircuito (short-circuit) en <code>a Y b</code> significa que:

- a) Siempre se evalúan ambos operandos antes de decidir
- b) Si <code>a</code> es falso, <code>b</code> no se evalúa porque el resultado ya es falso
- c) El operador <code>Y</code> se convierte en <code>O</code> automáticamente

**Respuesta correcta:** b) · **Referencia:** §3.2 [SEBESTA]

Se aprovecha para proteger operaciones, p. ej. evitar una división por cero.

### 28. ¿Cuál es el resultado de la expresión <code>2 + 3 * 4</code> aplicando la precedencia habitual de operadores?

- a) 20
- b) 24
- c) 14

**Respuesta correcta:** c) · **Referencia:** §3.4 [SEBESTA]

La multiplicación tiene mayor precedencia que la suma: <code>3*4=12</code>, luego <code>2+12=14</code>. Los paréntesis alterarían el orden.

### 29. La sentencia <code>x += 3</code> es equivalente a:

- a) <code>x = x + 3</code>
- b) <code>x = 3</code>
- c) <code>x = x * 3</code>

**Respuesta correcta:** a) · **Referencia:** §3.3 [SEBESTA]

Es una asignación compuesta que combina la suma con la asignación.

### 30. En una expresión con varios operadores, ¿qué elemento fuerza siempre el orden de evaluación por encima de la precedencia?

- a) El operador de asignación
- b) El operador módulo
- c) Los paréntesis

**Respuesta correcta:** c) · **Referencia:** §3.4 [SEBESTA]

Lo que está entre paréntesis se evalúa primero; en caso de duda, conviene usarlos para mayor legibilidad.

### 31. Según el teorema de Böhm-Jacopini (1966), cualquier algoritmo puede escribirse combinando únicamente:

- a) Compiladores, intérpretes y ensambladores
- b) Secuencia, selección e iteración
- c) Variables, constantes y punteros

**Respuesta correcta:** b) · **Referencia:** §4.1 [BOHM66]

Es el fundamento de la programación estructurada, que evita el <code>goto</code> (Dijkstra, 1968).

### 32. ¿Por qué la programación estructurada desaconseja el uso de la instrucción <code>goto</code>?

- a) Porque el <code>goto</code> es más lento de ejecutar
- b) Porque el <code>goto</code> no existe en ningún lenguaje moderno
- c) Porque genera «código espagueti» difícil de leer y mantener (Dijkstra, 1968)

**Respuesta correcta:** c) · **Referencia:** §4.1 [DIJKSTRA68]

Un programa estructurado tiene un único punto de entrada y de salida por bloque.

### 33. La estructura de selección múltiple <code>segun</code> / <code>switch</code> / <code>case</code> es preferible a muchos <code>si</code> encadenados cuando:

- a) Se decide sobre los distintos valores discretos de una misma expresión
- b) Solo hay dos caminos posibles
- c) No se conoce ninguna condición

**Respuesta correcta:** a) · **Referencia:** §4.2 [SEBESTA]

Es más legible; la rama <code>por_defecto</code> captura los valores no contemplados.

### 34. En un <code>switch</code> de lenguajes como C o Java, olvidar el <code>break</code> al final de cada caso provoca:

- a) Un error de compilación inmediato
- b) Que el programa se detenga
- c) Que la ejecución «caiga» (fall-through) al siguiente caso

**Respuesta correcta:** c) · **Referencia:** §4.2 [SEBESTA]

Es un error frecuente; el <code>break</code> corta la ejecución del caso.

### 35. ¿Cuál es la diferencia entre un bucle <code>mientras</code> (while) y un <code>repetir…hasta</code> (do-while)?

- a) El <code>mientras</code> comprueba la condición antes (puede ejecutarse 0 veces); el <code>repetir…hasta</code> la comprueba después (se ejecuta al menos 1 vez)
- b) El <code>mientras</code> se ejecuta siempre exactamente 10 veces
- c) No hay ninguna diferencia entre ellos

**Respuesta correcta:** a) · **Referencia:** §4.3 [SEBESTA]

El primero es precondicional; el segundo, postcondicional.

### 36. El bucle <code>para</code> (for) es el más adecuado cuando:

- a) La condición no puede evaluarse nunca
- b) Se conoce de antemano el número de repeticiones
- c) Se quiere ejecutar el cuerpo una única vez seguro

**Respuesta correcta:** b) · **Referencia:** §4.3 [SEBESTA]

Integra inicialización, condición e incremento del contador.

### 37. ¿Cuántas veces se ejecuta el cuerpo de <code>i = 5; mientras (i &lt; 5) hacer … i = i + 1; fin_mientras</code>?

- a) 0 veces, porque la condición <code>5 &lt; 5</code> es falsa de entrada
- b) 5 veces
- c) Infinitas veces

**Respuesta correcta:** a) · **Referencia:** §4.3 [SEBESTA]

El <code>mientras</code> es precondicional; comprueba antes de entrar.

### 38. Un bucle infinito se produce cuando:

- a) El bucle tiene demasiadas iteraciones definidas
- b) La condición de continuación nunca llega a hacerse falsa (p. ej. se olvida incrementar el contador)
- c) Se usa un bucle <code>para</code> con contador

**Respuesta correcta:** b) · **Referencia:** §4.3 [SEBESTA]

Es un error grave que cuelga el programa.

### 39. Toda función recursiva correctamente construida debe tener:

- a) Al menos tres parámetros
- b) Una variable global compartida
- c) Un caso base (condición de parada) y un caso recursivo que se acerque a él

**Respuesta correcta:** c) · **Referencia:** §4.4 [ABELSON]

Sin caso base, la recursión es infinita y desborda la pila (stack overflow).

### 40. ¿Qué ocurre si una función recursiva carece de caso base o nunca lo alcanza?

- a) El compilador la convierte automáticamente en iterativa
- b) Se produce recursión infinita que agota la pila de llamadas (stack overflow)
- c) Devuelve siempre el valor 0

**Respuesta correcta:** b) · **Referencia:** §4.4 [CLRS]

Cada llamada pendiente ocupa un marco en la pila.

### 41. Comparando recursividad e iteración para el mismo problema:

- a) La recursión nunca puede sustituirse por iteración
- b) La iteración siempre da resultados incorrectos
- c) Todo algoritmo recursivo puede reescribirse de forma iterativa; la recursión suele ser más elegante pero consume más memoria (marcos de pila)

**Respuesta correcta:** c) · **Referencia:** §4.4 [CLRS]

La iteración es más eficiente en memoria.

### 42. ¿Qué valor devuelve <code>factorial(4)</code> según la definición <code>factorial(n) = n * factorial(n-1)</code>, con caso base <code>factorial(1) = 1</code>?

- a) 24
- b) 10
- c) 12

**Respuesta correcta:** a) · **Referencia:** §4.4 [ABELSON]

<code>4 <em> 3 </em> 2 * 1 = 24</code>. Se apilan 4 llamadas y se desenrollan desde el caso base.

### 43. ¿Cuál es la diferencia entre una función y un procedimiento?

- a) El procedimiento solo puede tener un parámetro
- b) La función se ejecuta más rápido siempre
- c) La función devuelve un valor (se usa en una expresión); el procedimiento no devuelve valor, actúa por sus efectos

**Respuesta correcta:** c) · **Referencia:** §4.5 [ABELSON]

Muchos lenguajes los unifican como funciones que devuelven <code>void</code>.

### 44. Los beneficios de la programación modular (dividir el programa en subprogramas) incluyen:

- a) Reutilización, legibilidad, mantenimiento y prueba independiente, con alta cohesión y bajo acoplamiento
- b) Aumentar el número de líneas de código para que parezca más completo
- c) Impedir el uso de funciones y procedimientos

**Respuesta correcta:** a) · **Referencia:** §4.5 [MCCONNELL]

Es aplicar «divide y vencerás» al diseño del software.

### 45. En el paso de parámetros, el «parámetro formal» es:

- a) El valor concreto que se pasa en la llamada
- b) La variable que aparece en la definición del subprograma
- c) Un tipo de dato primitivo

**Respuesta correcta:** b) · **Referencia:** §4.6 [SCOTT]

El valor concreto de la llamada es el «argumento» o parámetro real.

### 46. Si un procedimiento <code>duplica(x) { x = x * 2 }</code> recibe la variable <code>a = 10</code> por VALOR, tras la llamada <code>duplica(a)</code>:

- a) <code>a</code> sigue valiendo 10, porque se duplicó una copia y el original no cambia
- b) <code>a</code> pasa a valer 20
- c) <code>a</code> queda sin valor definido

**Respuesta correcta:** a) · **Referencia:** §4.6 [SCOTT]

Por referencia, en cambio, <code>a</code> pasaría a valer 20.

### 47. En el paso por referencia, a diferencia del paso por valor:

- a) Nunca se pueden modificar los datos del llamador
- b) Se copia el argumento y el original queda intacto
- c) Se pasa la dirección de la variable, por lo que el subprograma puede modificar el original

**Respuesta correcta:** c) · **Referencia:** §4.6 [SCOTT]

En C se emula con punteros; permite devolver varios resultados.

### 48. El ámbito (scope) de una variable se refiere a:

- a) La cantidad de memoria que ocupa
- b) El número de veces que cambia de valor
- c) La región del programa donde la variable es visible y puede usarse

**Respuesta correcta:** c) · **Referencia:** §4.7 [SCOTT]

Puede ser local (dentro de un subprograma) o global (todo el programa).

### 49. Una variable local declarada <code>static</code> en C tiene:

- a) Ámbito global y tiempo de vida local
- b) Ámbito local (solo visible en su función) pero tiempo de vida global (conserva su valor entre llamadas)
- c) Ni ámbito ni tiempo de vida

**Respuesta correcta:** b) · **Referencia:** §4.7 [SCOTT]

Ámbito (dónde es visible) y tiempo de vida (cuánto existe) son conceptos distintos.

### 50. Las variables locales automáticas de un subprograma se ubican en la memoria denominada:

- a) Pila (stack): nacen al entrar en el subprograma y mueren al salir
- b) Montículo (heap) reservado con <code>new</code>
- c) Registro del procesador exclusivamente

**Respuesta correcta:** a) · **Referencia:** §4.7 [SCOTT]

La memoria dinámica (con <code>new</code>/<code>malloc</code>) va al montículo (heap).

### 51. Un array (vector) se caracteriza por:

- a) Agrupar campos de tipos distintos accedidos por nombre
- b) No tener un orden definido entre sus elementos
- c) Ser una colección de elementos del mismo tipo, contiguos en memoria y accesibles por índice en tiempo O(1)

**Respuesta correcta:** c) · **Referencia:** §5.1 [KNUTH1]

El acceso directo por índice es su gran ventaja.

### 52. Acceder a <code>array[i]</code> con un índice <code>i</code> fuera del rango declarado:

- a) Siempre devuelve el valor 0 sin problemas
- b) Es un error grave: en C corrompe memoria; en Java/Python lanza una excepción (IndexOutOfBounds)
- c) Amplía automáticamente el tamaño del array

**Respuesta correcta:** b) · **Referencia:** §5.1 [KNUTH1]

Hay que respetar los límites del array.

### 53. ¿Cuál es la diferencia esencial entre un array y un registro?

- a) El array agrupa elementos del mismo tipo accedidos por índice; el registro agrupa campos de tipos distintos accedidos por nombre
- b) El array no cabe en memoria y el registro sí
- c) El registro solo puede tener un campo

**Respuesta correcta:** a) · **Referencia:** §5.2 [KNUTH1]

Un array de registros combina ambos.

### 54. El Padrón Municipal (con dni, nombre, fecha de nacimiento y distrito de cada habitante) se modela de forma natural como:

- a) Un único número entero muy grande
- b) Un array (o lista) de registros «Habitante», donde cada habitante es un registro
- c) Una constante booleana

**Respuesta correcta:** b) · **Referencia:** §5.2 [KNUTH1]

Es el paso previo a persistirlo en una base de datos relacional (T17/T19).

### 55. La búsqueda binaria (dicotómica) sobre un array:

- a) Funciona sobre cualquier array, esté ordenado o no
- b) Es más lenta que la búsqueda secuencial
- c) Requiere que el array esté ordenado y tiene coste O(log n), más rápida que la secuencial O(n)

**Respuesta correcta:** c) · **Referencia:** §5.3 [CLRS]

Divide el rango a la mitad en cada paso.

### 56. El principio DRY (Don't Repeat Yourself) en buenas prácticas de programación consiste en:

- a) No repetir código, factorizando lo común en funciones reutilizables
- b) Repetir el código tres veces para asegurar que funciona
- c) Documentar cada línea con un comentario

**Respuesta correcta:** a) · **Referencia:** §6.2 [MCCONNELL]

Junto con KISS (mantenlo simple) y YAGNI, mejora la mantenibilidad.

### 57. Un «error lógico» en un programa se caracteriza por:

- a) Impedir que el programa compile
- b) Detener el programa con un mensaje del sistema operativo
- c) Que el programa se ejecuta sin fallar pero produce un resultado incorrecto; es el más difícil de detectar

**Respuesta correcta:** c) · **Referencia:** §6.3 [KP]

Se caza con pruebas (testing); se distingue del error de compilación y del de ejecución.

### 58. Las pruebas que comprueban una función o módulo de forma aislada se denominan:

- a) Pruebas de aceptación del usuario
- b) Pruebas unitarias
- c) Pruebas de sistema completo

**Respuesta correcta:** b) · **Referencia:** §6.3 [KP]

Las de integración comprueban módulos juntos; las de sistema/aceptación, el conjunto frente a los requisitos.

### 59. El «tipado gradual» (type hints en Python, TypeScript sobre JavaScript) es una tendencia que busca:

- a) Añadir anotaciones de tipo opcionales a lenguajes dinámicos para detectar errores antes sin perder flexibilidad
- b) Eliminar todos los tipos de datos de los lenguajes
- c) Convertir todos los lenguajes en ensamblador

**Respuesta correcta:** a) · **Referencia:** §7 [SCOTT]

Acerca lo mejor del tipado estático y del dinámico.

### 60. Respecto a las tendencias actuales (seguridad de memoria, concurrencia, IA), los fundamentos del tema (tipos, operadores, estructuras de control, modularidad):

- a) Han quedado obsoletos y ya no se usan
- b) Siguen plenamente vigentes por debajo de todas esas tendencias
- c) Solo se aplican a lenguajes de bajo nivel

**Respuesta correcta:** b) · **Referencia:** §7 [SEBESTA]

Rust, WebAssembly o los asistentes de IA se apoyan en los mismos fundamentos.

## Preguntas sobre los casos prácticos

### Caso 1. Cálculo de la tasa de un servicio municipal

#### 1. En el supuesto de la tasa, ¿qué tipo de dato debe usarse para el importe_base y la cuota_final?

- a) Un real en coma flotante, porque admite decimales.
- b) Un entero de céntimos o un tipo decimal exacto.
- c) Una cadena de caracteres, para guardar el símbolo €.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.2

Para dinero se recomienda un entero de céntimos o un tipo decimal exacto, no coma flotante, porque los reales en coma flotante son aproximaciones.

#### 2. ¿Por qué no conviene guardar esos importes en coma flotante?

- a) Porque la representación IEEE 754 es aproximada y puede introducir céntimos erróneos.
- b) Porque la coma flotante no admite valores con parte decimal, como los céntimos.
- c) Porque la coma flotante no permite representar importes negativos ni el cero.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.2

Los reales se representan según IEEE 754 con precisión finita: no todos los decimales son exactos, y un céntimo de error multiplicado por miles de recibos es un problema contable.

#### 3. ¿Qué tipo de dato corresponde al indicador de familia numerosa?

- a) Real, en tanto por uno.
- b) Enumerado con los tramos de renta.
- c) Booleano (verdadero/falso).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.2

El indicador solo puede tomar dos valores, sí o no: es un booleano. El tanto por uno es propio de la bonificación.

#### 4. ¿Qué estructura de control es la más adecuada para asignar la bonificación por tramos de renta?

- a) Una selección múltiple segun / switch sobre la renta.
- b) Un condicional múltiple anidado (si … si_no si … si_no).
- c) Un bucle mientras que recorra los tramos de renta.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §4.2

El condicional múltiple anidado encadena varias condiciones sobre rangos (renta < 12.000; renta ≤ 20.000, porque el tramo «entre 12.000 y 20.000 €» incluye los 20.000; resto), que es lo que pide el cálculo.

#### 5. ¿Por qué se descarta aquí la selección múltiple segun / switch?

- a) Porque switch compara contra valores constantes y aquí se decide por rangos.
- b) Porque switch no admite una rama por defecto para los demás valores.
- c) Porque switch solo puede distinguir entre dos casos distintos.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §4.2

La selección múltiple compara una expresión contra varios valores constantes y es útil con valores discretos; la renta es continua y se clasifica por rangos.

#### 6. Un solicitante tiene una renta de 15.000 € y familia numerosa. ¿Qué bonificación total (en tanto por uno) le corresponde?

- a) 0,25.
- b) 0,55.
- c) 0,30.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestiones 2 y 3

La renta está entre 12.000 y 20.000 €, tramo del 25 % (0,25); la familia numerosa suma 5 puntos acumulables (0,05): 0,25 + 0,05 = 0,30.

#### 7. ¿Qué expresión calcula correctamente la cuota_final?

- a) cuota_final = importe_base * (1 - bonificacion)
- b) cuota_final = importe_base * 1 - bonificacion
- c) cuota_final = importe_base * bonificacion

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §3.1, §3.4

La cuota es la parte no bonificada del importe: importe_base × (1 − bonificación). Sin paréntesis, la multiplicación se evalúa antes que la resta y el resultado sería importe_base − bonificación.

#### 8. Con un importe_base de 200 € y una bonificación total de 0,30, ¿cuál es la cuota_final?

- a) 60 €.
- b) 140 €.
- c) 199,70 €.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3

cuota_final = 200 × (1 − 0,30) = 200 × 0,70 = 140 €. Los 60 € son el importe bonificado, no la cuota.

#### 9. ¿Qué fragmento garantiza que la cuota final nunca sea negativa?

- a) si (cuota_final == 0) entonces cuota_final = 0 fin_si
- b) si (cuota_final < 0) entonces cuota_final = importe_base fin_si
- c) si (cuota_final < 0) entonces cuota_final = 0 fin_si

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §3.2, §4.2

Un condicional simple comprueba si la cuota es menor que cero y, en ese caso, la fija en 0; comparar con == 0 no corrige nada y poner el importe base anularía la bonificación.

#### 10. Los umbrales (12.000, 20.000) y los porcentajes aparecen como literales en el código. ¿Cómo se facilita el cambio de tramos del año que viene?

- a) Sustituyéndolos por constantes con nombre declaradas en un único lugar.
- b) Añadiendo un comentario junto a cada literal que explique su significado.
- c) Usando variables globales que cualquier función pueda modificar.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §1.5, §6.2

Las constantes con nombre (UMBRAL_BAJO = 12000…) eliminan los «números mágicos»: el cambio se hace en un solo punto. Las variables globales modificables se desaconsejan.

### Caso 2. Procesado del censo de habitantes por distrito

#### 1. En el supuesto del censo, ¿qué estructura representa a cada Habitante, con su dni, nombre, edad y codigo_distrito?

- a) Un array de cuatro elementos, todos ellos del mismo tipo de dato.
- b) Un tipo enumerado, con una lista fija de nombres de valores.
- c) Un registro, porque agrupa campos de tipos distintos accesibles por nombre.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §5.2

El registro agrupa campos de tipos posiblemente distintos (cadenas y enteros) bajo un nombre y se accede por nombre de campo; el array es homogéneo.

#### 2. ¿Qué declaraciones necesita el módulo para el censo y para la población por distrito?

- a) censo : array[1..N] de Habitante y poblacion : array[1..21] de entero.
- b) censo : registro de N campos y poblacion : array[1..N] de entero.
- c) censo : array[1..21] de Habitante y poblacion : array[1..N] de entero.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §5.1, §5.2

El censo es un array de registros (uno por habitante) y la población es un array de 21 contadores enteros, uno por distrito.

#### 3. ¿Qué bucle es el adecuado para recorrer el censo y por qué?

- a) Un bucle mientras, porque el número de habitantes es desconocido.
- b) Un bucle para (for), porque se conoce el número N de habitantes.
- c) Un bucle repetir … hasta, porque el censo debe procesarse dos veces.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.3

El bucle para se usa cuando se conoce de antemano el número de repeticiones, como aquí, donde N es conocido.

#### 4. ¿Cuántos recorridos del censo hacen falta para obtener los tres resultados y con qué coste?

- a) Tres recorridos, uno por resultado, con coste O(n²).
- b) Veintiún recorridos, uno por distrito, con coste O(n).
- c) Un único recorrido, con coste O(n).

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §5.3

Dentro del mismo bucle se actualizan el total, los mayores de edad y el contador del distrito: un solo recorrido lineal, O(n).

#### 5. Antes de recorrer el censo, ¿qué debe hacerse con el array poblacion?

- a) Nada: el lenguaje pone siempre a 0 sus posiciones al declararlo.
- b) Inicializar a 0 sus 21 posiciones, igual que total y mayores.
- c) Cargar en cada posición la edad del primer habitante del distrito.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §1.5

Los contadores deben inicializarse antes de acumular; usar una variable declarada pero no inicializada es una fuente clásica de errores (valor «basura» en C).

#### 6. ¿Qué condición cuenta correctamente a los mayores de edad (18 o más)?

- a) si (censo[i].edad >= 18)
- b) si (censo[i].edad > 18)
- c) si (censo.edad[i] >= 18)

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §3.2, §5.2

Hay que incluir los 18 años (>=) y acceder primero al registro i-ésimo y después a su campo edad: censo[i].edad.

#### 7. En la expresión censo[i].codigo_distrito, ¿cómo se accede a cada parte?

- a) censo[i] accede al campo por nombre; .codigo_distrito, al registro por índice.
- b) Ambas partes acceden por índice: i al registro y codigo_distrito a la posición.
- c) censo[i] accede al registro por índice; .codigo_distrito, al campo por nombre.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §5.1, §5.2

Al elemento de un array se accede por índice (en tiempo constante) y al campo de un registro, por su nombre con el punto.

#### 8. Con dist = censo[i].codigo_distrito, ¿qué sentencia incrementa el contador del distrito de ese habitante?

- a) poblacion[i] = poblacion[i] + 1
- b) poblacion[dist] = poblacion[dist] + 1
- c) poblacion = poblacion + dist

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §5.1

El valor del campo codigo_distrito se usa como índice del array poblacion; el índice i recorre habitantes, no distritos.

#### 9. ¿Qué comprobación defensiva debe hacerse antes de usar dist como índice de poblacion?

- a) si (dist >= 1 Y dist <= 21) entonces …
- b) si (dist >= 1 O dist <= 21) entonces …
- c) si (dist > 1 Y dist < 21) entonces …

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §3.2, §6.2

Hay que exigir a la vez (Y) que el valor esté entre 1 y 21, ambos incluidos. Con O la condición siempre es verdadera, y con > y < se excluyen los distritos 1 y 21.

#### 10. Si un registro trae el distrito 0 o 25 y no se comprueba el rango, ¿qué ocurre?

- a) El lenguaje ajusta el índice al extremo más cercano y suma el habitante al distrito 1 o 21.
- b) El compilador detecta el valor erróneo del registro e impide ejecutar el programa.
- c) Un acceso fuera de rango: corrompe memoria en C o lanza IndexOutOfBounds en Java/Python.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §5.1

Acceder a un índice fuera del rango declarado es un error grave: en C corrompe memoria silenciosamente y en Java o Python lanza una excepción.

### Caso 3. Tramitación y numeración de expedientes

#### 1. En el supuesto de los expedientes, ¿qué expresión usa la función es_par(n)?

- a) n mod 2 == 0
- b) n div 2 == 0
- c) n / 2 == 0

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §3.1

El operador módulo devuelve el resto de la división entera: si el resto de dividir entre 2 es cero, el número es par. div devuelve el cociente.

#### 2. ¿Por qué es_par se define como función y no como procedimiento?

- a) Porque no devuelve ningún valor y actúa por sus efectos.
- b) Porque devuelve un valor (booleano) que se usa en expresiones.
- c) Porque recibe un parámetro, cosa que no admite un procedimiento.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §4.5

La función devuelve un valor y se usa dentro de expresiones; el procedimiento no devuelve valor y actúa por sus efectos. Ambos pueden recibir parámetros.

#### 3. En la función recursiva suma_hasta(n), ¿cuál es el caso base?

- a) devolver n + suma_hasta(n - 1)
- b) La llamada inicial suma_hasta(4)
- c) si (n <= 1) entonces devolver n

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §4.4

El caso base es la condición de parada que se resuelve directamente sin volver a llamarse: para n ≤ 1 se devuelve n.

#### 4. ¿Qué caso recursivo es correcto para suma_hasta(n)?

- a) devolver n + suma_hasta(n - 1)
- b) devolver n + suma_hasta(n + 1)
- c) devolver n + suma_hasta(n)

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §4.4

El caso recursivo debe llamarse con un problema más pequeño que se acerque al caso base; con n + 1 se aleja y con n no avanza.

#### 5. ¿Qué pasaría si suma_hasta no tuviera caso base?

- a) Devolvería 0 al llegar a n = 0 y terminaría con normalidad.
- b) El compilador lo detectaría como error de sintaxis.
- c) Recursión infinita hasta agotar la pila (stack overflow).

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §4.4

Sin caso base la recursión no termina: cada llamada pendiente ocupa un marco en la pila hasta agotarla.

#### 6. ¿Qué valor devuelve suma_hasta(4)?

- a) 24.
- b) 10.
- c) 6.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §4.4

suma_hasta(4) = 4 + (3 + (2 + suma_hasta(1))), con suma_hasta(1) = 1: 2 + 1 = 3, 3 + 3 = 6, 4 + 6 = 10. El 24 sería el factorial de 4.

#### 7. ¿Cuántas llamadas a suma_hasta llegan a estar apiladas a la vez al calcular suma_hasta(4)?

- a) Cuatro: suma_hasta(4), (3), (2) y (1).
- b) Tres: suma_hasta(4), (3) y (2).
- c) Cinco: de suma_hasta(4) a suma_hasta(0).

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §4.4

La recursión se detiene en suma_hasta(1), el caso base; hasta entonces cada llamada pendiente ocupa un marco en la pila: 4, 3, 2 y 1.

#### 8. Se llama a incrementar(c) { c = c + 1 } con contador = 10. Si el paso es por valor, ¿cuánto vale contador después?

- a) 11, porque c y contador comparten la misma dirección.
- b) 10, porque se incrementó una copia del argumento.
- c) 0, porque la copia se destruye al salir del procedimiento.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §4.6

En el paso por valor el subprograma trabaja sobre una copia; los cambios no afectan a la variable original del llamador.

#### 9. ¿Y si el paso de contador a incrementar(c) es por referencia?

- a) 10, porque el original nunca se modifica.
- b) 12, porque se incrementan c y contador.
- c) 11, porque se modifica el original.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §4.6

En el paso por referencia el subprograma accede a la variable real, de modo que el incremento persiste: contador pasa de 10 a 11.

#### 10. ¿Qué explica que, con el paso por referencia, la llamada sí modifique contador?

- a) Que el procedimiento devuelve el nuevo valor de c al llamador.
- b) Que se pasa la dirección de la variable, no una copia de su valor.
- c) Que c se declara como variable global visible en todo el programa.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §4.5, §4.6

Por referencia se pasa la dirección de la variable original y el subprograma trabaja sobre ella; un procedimiento, además, no devuelve valor.
