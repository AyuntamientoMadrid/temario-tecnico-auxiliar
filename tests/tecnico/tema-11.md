# Test del tema 11. Informática básica. Representación y comunicación de la información

25 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-11.html>

## Batería de preguntas

### 1. ¿Cuál es la unidad mínima de información en un sistema informático?

- a) Byte
- b) Bit
- c) Nibble

**Respuesta correcta:** b) · **Referencia:** §7

El bit (binary digit) representa 0 o 1, unidad mínima.

### 2. En la arquitectura Von Neumann, ¿cuál es la causa principal de su cuello de botella?

- a) Los datos y las instrucciones comparten el mismo bus de memoria
- b) La ALU no puede hacer operaciones aritméticas y lógicas simultáneamente
- c) La UC no puede decodificar más de una instrucción a la vez

**Respuesta correcta:** a) · **Referencia:** §3.1

Bus compartido impide búsqueda simultánea de datos e instrucciones.

### 3. ¿Qué característica diferencia fundamentalmente la arquitectura Harvard de la Von Neumann?

- a) Harvard separa memoria de instrucciones y de datos
- b) Harvard usa microprocesadores RISC exclusivamente
- c) Harvard no utiliza buses de control

**Respuesta correcta:** a) · **Referencia:** §3.2

Harvard usa memorias y buses separados para datos e instrucciones.

### 4. ¿Cuál de las siguientes afirmaciones sobre los procesadores RISC es correcta?

- a) Solo las instrucciones de carga/almacenamiento acceden a memoria de datos
- b) Usan instrucciones complejas que requieren 4-10 ciclos
- c) Son la arquitectura predominante en x86

**Respuesta correcta:** a) · **Referencia:** §5.2.1

Arquitectura load-store: característica fundamental RISC.

### 5. ¿Qué componente de la CPU contiene la dirección de la siguiente instrucción a ejecutar?

- a) Contador de Programa (CP)
- b) Registro de Instrucción (RI)
- c) Registro de Estado (FLAGS)

**Respuesta correcta:** a) · **Referencia:** §5.3.2

El CP apunta a la siguiente instrucción; RI contiene la actual.

### 6. ¿Cuántos bytes representa 1 KiB (kibibyte)?

- a) 1.000 bytes
- b) 1.024 bytes
- c) 512 bytes

**Respuesta correcta:** b) · **Referencia:** §7.1

KiB binario = 2^10 = 1.024 B. KB decimal = 1.000 B.

### 7. En la primera generación de ordenadores (1940-1952), ¿cuál era el componente electrónico principal?

- a) Transistores
- b) Circuitos integrados
- c) Válvulas de vacío

**Respuesta correcta:** c) · **Referencia:** §4.1

Válvulas y tubos de vacío (ENIAC).

### 8. ¿Qué tipo de bus transporta las direcciones de memoria en operaciones de lectura/escritura?

- a) Bus de datos
- b) Bus de control
- c) Bus de direcciones

**Respuesta correcta:** c) · **Referencia:** §5.1

Bus de direcciones, unidireccional CPU→memoria.

### 9. ¿Qué tipo de ROM se borra por luz ultravioleta y se reprograma eléctricamente?

- a) PROM
- b) EPROM
- c) EEPROM

**Respuesta correcta:** b) · **Referencia:** §6.3

EPROM: ventana de cuarzo para UV, reprogramacion eléctrica.

### 10. ¿Cuál NO es una función básica de un SI?

- a) Compilación de código fuente
- b) Procesamiento
- c) Almacenamiento

**Respuesta correcta:** a) · **Referencia:** §2.4

Funciones EAPS: Entrada/Almacenamiento/Procesamiento/Salida.

### 11. ¿Cuántos pines tiene un módulo de memoria DDR4?

- a) 240 pines
- b) 184 pines
- c) 288 pines

**Respuesta correcta:** c) · **Referencia:** §6.2.3

DDR4=288p (como DDR5 pero incompatibles por voltaje).

### 12. ¿Qué codificación usa 1-4 bytes y es compatible con ASCII de 7 bits?

- a) EBCDIC
- b) UTF-8
- c) ISO-8859-1

**Respuesta correcta:** b) · **Referencia:** §9.3

UTF-8: longitud variable, compatible ASCII, dominante en web.

### 13. ¿Qué tecnología permite a un núcleo ejecutar 2 tareas simultáneas?

- a) MultiThreading (HyperThreading / SMT)
- b) Multiprocesamiento
- c) Multinúcleo

**Respuesta correcta:** a) · **Referencia:** §5.2.3

SMT duplica unidades lógicas; Intel=HTT, AMD=SMT.

### 14. ¿Qué afirmación describe correctamente una diferencia entre UEFI y la BIOS tradicional?

- a) UEFI solo puede utilizar discos con esquema de particiones MBR
- b) UEFI es una arquitectura de firmware más moderna y permite arrancar desde discos GPT
- c) BIOS y UEFI son esquemas de particionado de discos

**Respuesta correcta:** b) · **Referencia:** §6.4

BIOS y UEFI son firmware; MBR y GPT son esquemas de particionado. UEFI arranca de forma nativa desde GPT (MBR: 4 entradas y 2 TiB; son límites del esquema, no del firmware).

### 15. ¿Qué ocurre durante la fase FETCH del ciclo de instrucciones?

- a) La ALU ejecuta la operación
- b) El CP se decrementa
- c) La instrucción es localizada en memoria y transferida al RI

**Respuesta correcta:** c) · **Referencia:** §5.4

CP→MAR→Mem→MBR→RI. CP se incrementa, no decrementa.

### 16. En la pirámide DIKW, ¿cuál es el orden correcto de abajo a arriba?

- a) Dato→Conocimiento→Información→Sabiduría
- b) Dato→Información→Conocimiento→Sabiduría
- c) Información→Dato→Sabiduría→Conocimiento

**Respuesta correcta:** b) · **Referencia:** §1.3

DIKW (Ackoff 1989): Dato · Información · Conocimiento · Sabiduría.

### 17. ¿Cuál de las siguientes NO es una dimensión habitualmente utilizada para evaluar la calidad de los datos?

- a) Exactitud
- b) Completitud
- c) Velocidad del procesador

**Respuesta correcta:** c) · **Referencia:** §1.5

Exactitud, completitud, consistencia y actualidad son características de calidad del dato (modelo ISO/IEC 25012); la velocidad del procesador es una característica del hardware.

### 18. Atendiendo a su función de registro de altas, bajas y modificaciones de los datos padronales, el sistema del Padrón Municipal se clasifica como:

- a) EIS (Executive Information System)
- b) DSS (Decision Support System)
- c) TPS (Transaction Processing System)

**Respuesta correcta:** c) · **Referencia:** §2.5

TPS: registra transacciones individuales y frecuentes (altas, bajas y modificaciones) en el nivel operativo.

### 19. ¿Cuántas etapas tiene el cauce segmentado (pipeline) RISC clásico (modelo MIPS)?

- a) 3 etapas
- b) 5 etapas
- c) 7 etapas

**Respuesta correcta:** b) · **Referencia:** §5.2.4

5 etapas: IF-ID-EX-MEM-WB.

### 20. ¿Qué indica el bit ZF (Zero Flag) del registro FLAGS en x86?

- a) El resultado de la última operación es cero
- b) El procesador está en modo protegido
- c) Se ha producido un desbordamiento

**Respuesta correcta:** a) · **Referencia:** §5.3.1.1

ZF=1 si resultado cero. Bit 6 del registro FLAGS.

### 21. ¿Cuál es el rango de un entero de 8 bits en complemento a 2?

- a) De 0 a 255
- b) De -127 a +127
- c) De -128 a +127

**Respuesta correcta:** c) · **Referencia:** §8.2

C2 8 bits: -2^7 a +2^7-1 = -128 a +127.

### 22. ¿Cómo se distribuyen los bits en IEEE 754 de precisión simple (float de 32 bits)?

- a) 1 bit signo, 8 bits exponente, 23 bits mantisa
- b) 1 bit signo, 11 bits exponente, 20 bits mantisa
- c) 2 bits signo, 7 bits exponente, 23 bits mantisa

**Respuesta correcta:** a) · **Referencia:** §8.3

Precisión simple: 1+8+23. Precisión doble: 1+11+52.

### 23. ¿Cuántos bytes utiliza UTF-8 para codificar un carácter cuyo punto de código está entre U+0800 y U+FFFF (por ejemplo, el carácter chino 中, U+4E2D)?

- a) 1 byte
- b) 2 bytes
- c) 3 bytes

**Respuesta correcta:** c) · **Referencia:** §9.3

RFC 3629: U+0800 a U+FFFF = 3 bytes (1110xxxx 10xxxxxx 10xxxxxx). El BMP completo ocupa 1, 2 o 3 bytes según el rango.

### 24. ¿Qué componente hardware traduce direcciones virtuales a físicas?

- a) TLB de forma autónoma
- b) La ALU mediante operaciones aritméticas
- c) MMU consultando la tabla de páginas

**Respuesta correcta:** c) · **Referencia:** §6.2.8

MMU es la lógica; TLB es solo una caché de traducciones.

### 25. ¿Qué hace el Secure Boot de UEFI?

- a) Cifra el disco al iniciar
- b) Verifica la firma de los componentes de arranque para reducir el riesgo de malware de arranque (bootkits)
- c) Requiere TPM 3.0 o superior

**Respuesta correcta:** b) · **Referencia:** §6.4

Verifica la firma de los componentes de arranque; reduce, no elimina, el riesgo de bootkits. Windows 11 exige equipo UEFI compatible con Secure Boot y TPM 2.0.

## Preguntas sobre los casos prácticos

### Caso 1. Caso 1

#### 1. Atendiendo a su función de registro de altas, bajas y modificaciones de los datos padronales, ¿qué tipo de sistema de información es el Padrón y en qué nivel organizacional se sitúa?

- a) Un TPS, en el nivel operativo.
- b) Un MIS, en el nivel de gestión o táctico.
- c) Un DSS, en el nivel analítico.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.6

En esa función el Padrón registra transacciones individuales (altas, bajas y modificaciones) en tiempo real: es un TPS, el tipo de sistema propio del nivel operativo.

#### 2. ¿Qué rasgo del Padrón justifica esa clasificación?

- a) Elabora informes periódicos consolidados que utilizan los mandos medios para supervisar el servicio.
- b) Procesa transacciones individuales de altas, bajas y modificaciones en tiempo real, en el nivel operativo.
- c) Ofrece un cuadro de mando con indicadores muy agregados para el equipo de gobierno municipal.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.6

El TPS es el sistema del nivel operativo: maneja transacciones individuales, en tiempo real y en alto volumen. Los informes periódicos son propios del MIS y el cuadro de mando, del EIS.

#### 3. ¿Cuántos hilos lógicos presenta al sistema operativo el servidor del Padrón, con 2 procesadores AMD EPYC 9354 de 32 núcleos con SMT cada uno?

- a) 64 hilos lógicos.
- b) 256 hilos lógicos.
- c) 128 hilos lógicos.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §5.2.3

Con SMT cada núcleo ejecuta 2 hilos: 32 núcleos × 2 = 64 hilos por procesador, y con 2 procesadores, 128 hilos lógicos.

#### 4. Los puestos de atención llevan un Intel Core i5-14400 con 6 núcleos P y 4 núcleos E, y la tabla indica 16 hilos. ¿Cómo se obtiene esa cifra?

- a) Cada núcleo P ejecuta 2 hilos con HyperThreading y cada núcleo E, 1 hilo: 6 × 2 + 4 = 16.
- b) Cada uno de los 10 núcleos ejecuta 2 hilos, menos 4 hilos reservados para el sistema: 10 × 2 − 4 = 16.
- c) Solo los núcleos E tienen HyperThreading y ejecutan 4 hilos cada uno, sin contar los núcleos P: 4 × 4 = 16.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §5.2.3

Los núcleos de eficiencia (E) no tienen HyperThreading para ahorrar energía; solo los núcleos de rendimiento (P) ejecutan 2 hilos cada uno.

#### 5. El servidor del Padrón monta dos procesadores físicos en una placa con dos zócalos. Esta configuración es un ejemplo de:

- a) Multinúcleo.
- b) Multithreading.
- c) Multiprocesamiento.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §5.2.3

Un equipo con más de una CPU física (varios zócalos) es multiprocesamiento; el multinúcleo es un único chip con varios núcleos y el multithreading duplica las unidades lógicas de cada núcleo.

#### 6. ¿Pueden instalarse los módulos DDR5 de los puestos nuevos en las placas base DDR4 existentes?

- a) Sí, porque ambos tipos utilizan módulos DIMM de 288 pines.
- b) No, porque DDR4 y DDR5 son física y eléctricamente incompatibles.
- c) Sí, siempre que se ajuste el voltaje de la placa desde la BIOS.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §6.2.3

Aunque comparten 288 pines, DDR4 y DDR5 son incompatibles física y eléctricamente: hace falta una placa base compatible con DDR5.

#### 7. Un compañero sostiene que, al tener DDR4 y DDR5 los mismos pines, los módulos deberían encajar. ¿Qué diferencias desmienten su razonamiento?

- a) DDR4 funciona a 1,2 V y DDR5 a 1,1 V, y la muesca está en distinta posición.
- b) DDR4 funciona a 1,5 V y DDR5 a 1,2 V, y DDR5 tiene 240 pines en lugar de 288.
- c) DDR4 funciona a 1,1 V y DDR5 a 1,2 V, y DDR4 integra el PMIC en el propio módulo.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §6.2.3

La tabla comparativa DDR asigna 1,2 V a DDR4 y 1,1 V a DDR5; además, la muesca cambia de posición y DDR5 integra el PMIC en el módulo.

#### 8. ¿Qué capacidad de corrección aporta la memoria ECC del servidor del Padrón?

- a) Detecta y corrige errores de 1 y de 2 bits, y detecta sin corregir los de 3 bits.
- b) Detecta y corrige errores de 1 bit, y detecta sin corregir los errores de 2 bits.
- c) Detecta errores de 1 bit sin corregirlos, y corrige los errores de 2 bits o más.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §6.2.5

La memoria ECC detecta y corrige los errores de un bit y detecta, sin poder corregirlos, los de dos bits.

#### 9. ¿Por qué el servidor del Padrón usa memoria ECC y los puestos de atención no?

- a) Porque la memoria ECC es más rápida que la No-ECC y el servidor necesita el máximo rendimiento.
- b) Porque la ECC no requiere soporte de la placa base ni del procesador, a diferencia de la No-ECC.
- c) Porque en el servidor un error de memoria podría generar inconsistencias en los datos de los ciudadanos.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 4 · §6.2.5

La ECC es crítica en servidores que gestionan datos de ciudadanos; es algo más cara y más lenta (~2-3 %) y exige soporte de placa base y procesador, mientras que los puestos de uso interactivo no necesitan ese nivel de fiabilidad.

#### 10. Los SSD de los equipos son NAND Flash TLC. ¿Qué implica esta tecnología frente a SLC o MLC?

- a) Almacena 3 bits por celda: más densidad y menor coste, pero menor durabilidad.
- b) Almacena 1 bit por celda: más velocidad y durabilidad, pero mayor coste.
- c) Almacena 4 bits por celda: máxima densidad, pero la mínima durabilidad.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 5 · §6.3.1

TLC (Triple-Level Cell) guarda 3 bits por celda: gana densidad y abarata el coste frente a SLC (1 bit) y MLC (2 bits), a cambio de menor durabilidad; 4 bits por celda es QLC.
