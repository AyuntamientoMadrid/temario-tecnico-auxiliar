# Test del tema 12. Periféricos: conectividad y administración

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-12.html>

## Batería de preguntas

### 1. ¿Qué es un periférico?

- a) Cualquier programa que se ejecuta en la CPU
- b) Un dispositivo que se conecta a la unidad central para introducir, extraer, comunicar o almacenar información
- c) La memoria principal del ordenador donde se cargan los procesos

**Respuesta correcta:** b) · **Referencia:** §1.1 [ISO7498]

El periférico queda fuera del núcleo de cómputo, pero a su servicio.

### 2. Un escáner es un periférico de:

- a) Salida
- b) Comunicación
- c) Entrada

**Respuesta correcta:** c) · **Referencia:** §1.2 [ISO7498]

El escáner introduce datos (la imagen del documento) en el sistema.

### 3. ¿A qué categoría funcional pertenece una impresora multifunción que imprime y escanea?

- a) Entrada/salida (E/S)
- b) Solo salida
- c) Solo entrada

**Respuesta correcta:** a) · **Referencia:** §1.2 [ISO7498]

Combina la salida (imprimir) con la entrada (escanear).

### 4. Un disco duro, respecto al flujo de datos, se considera periférico de:

- a) Solo entrada
- b) Entrada/salida y almacenamiento
- c) Solo comunicación

**Respuesta correcta:** b) · **Referencia:** §1.2 [ISO7498]

Lee y escribe datos (E/S) y los conserva de forma persistente (almacenamiento).

### 5. Una impresora conectada por su propia interfaz de red, con IP y accesible por cualquier equipo autorizado, es un periférico:

- a) En red
- b) Local
- c) Interno

**Respuesta correcta:** a) · **Referencia:** §1.3 [ISO7498]

No depende de un PC intermediario; se accede a ella directamente por la red.

### 6. En la cadena de conexión de un periférico, ¿qué elemento es el conector físico?

- a) El driver
- b) El bus
- c) El puerto

**Respuesta correcta:** c) · **Referencia:** §1.4 [USB-IF]

El puerto es el conector físico; la interfaz/bus son las reglas y líneas, y el driver es el software.

### 7. El USB es un bus de tipo:

- a) Paralelo, sin conexión en caliente
- b) Serie, con conexión en caliente y Plug &amp; Play
- c) Óptico, exclusivo para vídeo

**Respuesta correcta:** b) · **Referencia:** §2.2 [USB-IF]

Además puede alimentar dispositivos por el propio cable.

### 8. ¿Cuál es la velocidad máxima de USB 2.0 (Hi-Speed)?

- a) 480 Mbps
- b) 5 Gbps
- c) 40 Gbps

**Respuesta correcta:** a) · **Referencia:** §2.2 [USB-IF]

USB 3.2 Gen 1 alcanza 5 Gbps y USB4, 40 Gbps.

### 9. Sobre el conector USB-C, es correcto afirmar que:

- a) Solo transporta datos, nunca vídeo ni energía
- b) Es un protocolo que siempre implica 40 Gbps
- c) Es un conector reversible que puede transportar datos, vídeo y energía

**Respuesta correcta:** c) · **Referencia:** §2.2 [USB-IF]

USB-C es una forma física; su velocidad depende de la versión interna (2.0, 3.2, USB4).

### 10. USB Power Delivery (USB PD 3.1) permite entregar por USB-C hasta:

- a) 15 W
- b) 240 W
- c) 5 W

**Respuesta correcta:** b) · **Referencia:** §2.2 [USB-IF]

Suficiente para cargar portátiles y monitores con un solo cable.

### 11. ¿Qué interfaz de vídeo digital admite encadenar varios monitores en serie mediante MST?

- a) VGA
- b) HDMI
- c) DisplayPort

**Respuesta correcta:** c) · **Referencia:** §2.3 [VESA-DP]

Multi-Stream Transport (MST) permite el <em>daisy-chain</em> de varias pantallas desde una salida.

### 12. HDMI se caracteriza principalmente por:

- a) Ser una interfaz digital de vídeo y audio dominante en el ámbito de consumo (TV, consolas, proyectores)
- b) Ser analógica y estar en desuso
- c) Transportar solo audio, nunca vídeo

**Respuesta correcta:** a) · **Referencia:** §2.3 [HDMI]

Lleva vídeo y audio por el mismo cable; HDMI 2.1 admite 4K/120 y 8K.

### 13. Thunderbolt 4, desde su versión 3, utiliza el conector:

- a) RJ-45
- b) USB-C
- c) VGA

**Respuesta correcta:** b) · **Referencia:** §2.4 [TB]

Combina datos (PCIe), vídeo (DisplayPort) y energía; garantiza 40 Gbps y sirvió de base a USB4.

### 14. El antiguo puerto VGA se diferencia de HDMI y DisplayPort en que:

- a) Es analógico, mientras que HDMI y DisplayPort son digitales
- b) Es mucho más rápido que ambos
- c) Transporta también audio de alta definición

**Respuesta correcta:** a) · **Referencia:** §2.3 [HDMI]

VGA está en desuso; DVI fue la interfaz de transición.

### 15. Bluetooth es una tecnología de red inalámbrica de tipo:

- a) WLAN de largo alcance
- b) WAN metropolitana
- c) WPAN (área personal), de corto alcance

**Respuesta correcta:** c) · **Referencia:** §2.5 [BT-SIG]

Trabaja en 2,4 GHz y conecta periféricos cercanos; BLE optimiza el consumo.

### 16. ¿Qué familia de normas define el Wi-Fi?

- a) IEEE 802.3
- b) IEEE 802.11
- c) ISO 9660

**Respuesta correcta:** b) · **Referencia:** §2.5 [IEEE802.11]

El Wi-Fi es una WLAN; 802.3 corresponde a Ethernet cableada.

### 17. Wi-Fi 6E se distingue de Wi-Fi 6 porque:

- a) Añade el uso de la banda de 6 GHz
- b) Elimina la banda de 5 GHz
- c) Solo funciona por cable

**Respuesta correcta:** a) · **Referencia:** §2.5 [IEEE802.11]

Ambos usan la norma 802.11ax; la «E» amplía a 6 GHz. Wi-Fi 7 es 802.11be.

### 18. NFC (Near Field Communication) se caracteriza por un alcance:

- a) De cientos de metros
- b) De unos 10 metros
- c) Muy corto, inferior a 4 cm

**Respuesta correcta:** c) · **Referencia:** §2.6 [BT-SIG]

Opera a 13,56 MHz; se usa en pagos, transporte y emparejamiento rápido.

### 19. ¿Qué estándar unifica la interoperabilidad de dispositivos del hogar/edificio inteligente de distintos fabricantes?

- a) Matter (habitualmente sobre la red de malla Thread)
- b) RS-232
- c) PostScript

**Respuesta correcta:** a) · **Referencia:** §2.6 [BT-SIG]

Matter estandariza la interoperabilidad IoT; Thread es la red de malla de baja potencia.

### 20. Un controlador de dispositivo (driver) es:

- a) El conector físico del periférico
- b) El software que traduce entre el sistema operativo y el hardware concreto del periférico
- c) La memoria interna del periférico

**Respuesta correcta:** b) · **Referencia:** §2.7 [MS-DEVMGR]

Sin el driver adecuado el dispositivo no funciona o lo hace en modo genérico.

### 21. ¿Qué es el firmware de un periférico?

- a) Un tipo de cable de conexión
- b) El papel de una impresora
- c) El software grabado en el propio dispositivo que controla su electrónica interna

**Respuesta correcta:** c) · **Referencia:** §2.7 [MS-DEVMGR]

Se actualiza para corregir fallos o añadir funciones.

### 22. La firma digital de controladores (driver signing) sirve para:

- a) Garantizar el origen e integridad del driver y evitar código malicioso en el núcleo
- b) Acelerar la impresión
- c) Aumentar la capacidad del disco

**Respuesta correcta:** a) · **Referencia:** §2.7 [MS-DEVMGR]

Los sistemas modernos exigen drivers firmados.

### 23. Plug &amp; Play (PnP) consiste en:

- a) Cifrar automáticamente los soportes extraíbles
- b) Detectar, identificar y configurar automáticamente un dispositivo al conectarlo
- c) Comprimir los archivos antes de imprimirlos

**Respuesta correcta:** b) · **Referencia:** §2.8 [MS-DEVMGR]

No debe confundirse con el hot-plug (conexión en caliente).

### 24. En Linux, ¿qué subsistema gestiona la detección y creación automática de nodos de dispositivo?

- a) CUPS
- b) BitLocker
- c) udev (con sysfs)

**Respuesta correcta:** c) · **Referencia:** §2.8, §3.1 [LINUX-UDEV]

udev aplica reglas y crea los nodos; CUPS gestiona impresión y BitLocker es cifrado de Windows.

### 25. ¿Qué herramienta de Windows permite ver y gestionar el hardware instalado?

- a) El Administrador de dispositivos
- b) El Bloc de notas
- c) El desfragmentador

**Respuesta correcta:** a) · **Referencia:** §3.2 [MS-DEVMGR]

Muestra dispositivos, drivers y posibles conflictos.

### 26. En Linux, la impresión se gestiona habitualmente con:

- a) SANE
- b) CUPS
- c) fdisk

**Respuesta correcta:** b) · **Referencia:** §3.2 [LINUX-UDEV]

CUPS gestiona la impresión (interfaz web en localhost:631); SANE es para escaneo y fdisk para particiones.

### 27. Ante un periférico que no funciona, el método de diagnóstico correcto empieza por:

- a) Reinstalar el sistema operativo
- b) Formatear el disco
- c) Comprobar lo físico: cable, puerto y alimentación

**Respuesta correcta:** c) · **Referencia:** §3.4 [MS-DEVMGR]

Se va de lo físico y sencillo a lo lógico y complejo.

### 28. Si un periférico dejó de funcionar justo tras actualizar su driver, la acción más razonable es:

- a) Cambiar la fuente de alimentación
- b) Revertir (rollback) el driver a la versión anterior
- c) Sustituir la placa base

**Respuesta correcta:** b) · **Referencia:** §3.4 [MS-DEVMGR]

El rollback deshace una actualización problemática de controlador.

### 29. Mantener actualizados los controladores es importante porque, entre otras cosas:

- a) Corrige fallos, mejora el rendimiento y cierra vulnerabilidades de seguridad
- b) Aumenta el tamaño físico del disco
- c) Sustituye a la necesidad de hacer copias de seguridad

**Respuesta correcta:** a) · **Referencia:** §3.3 [MS-DEVMGR]

Conviene usar solo drivers firmados y crear un punto de restauración previo.

### 30. Un ataque tipo BadUSB consiste en:

- a) Sobrecalentar el puerto USB
- b) Aumentar la velocidad del bus indebidamente
- c) Un dispositivo USB que simula ser un teclado y ejecuta comandos maliciosos

**Respuesta correcta:** c) · **Referencia:** §3.6 [ENS]

Se mitiga controlando clases de dispositivo y deshabilitando el autoarranque.

### 31. ¿Qué tecnología cifra discos y memorias en Windows para que un soporte perdido sea ilegible?

- a) CUPS
- b) BitLocker
- c) PostScript

**Respuesta correcta:** b) · **Referencia:** §3.6 [MS-DEVMGR][ENS]

En Linux el equivalente es LUKS; ambos cifran soportes.

### 32. Las soluciones DLP (Data Loss Prevention) sirven para:

- a) Impedir o controlar la copia de datos sensibles a soportes externos
- b) Aumentar la resolución del escáner
- c) Acelerar la carga de drivers

**Respuesta correcta:** a) · **Referencia:** §3.6 [ENS]

Reducen el riesgo de fuga de información por periféricos.

### 33. Al dar de baja un equipo, para evitar la recuperación de datos de su disco se debe:

- a) Formatearlo en modo rápido y venderlo
- b) Guardarlo sin más en un almacén
- c) Realizar un borrado seguro (sobrescritura) o la destrucción física certificada

**Respuesta correcta:** c) · **Referencia:** §3.6 [ENS]

El formateo rápido no elimina realmente los datos.

### 34. El <em>pull printing</em> (impresión con liberación segura) consiste en que:

- a) El documento solo se imprime cuando el usuario se identifica en el equipo
- b) El documento se imprime automáticamente en todas las impresoras del edificio
- c) Se elimina la cola de impresión

**Respuesta correcta:** a) · **Referencia:** §3.5, §4.3 [ENS]

Evita que documentos con datos personales queden olvidados en la bandeja.

### 35. En una impresora láser, el tóner se fija al papel mediante:

- a) Gotas de tinta líquida
- b) Calor y presión (fusor)
- c) Impacto de agujas

**Respuesta correcta:** b) · **Referencia:** §4.1 [HP-PRINT]

El láser marca el tambor, el tóner se adhiere y el fusor lo fija por calor.

### 36. ¿Qué tecnología de impresión es la más adecuada para reproducir fotografías en color con calidad?

- a) Matricial
- b) Térmica de tickets
- c) Inyección de tinta

**Respuesta correcta:** c) · **Referencia:** §4.1 [HP-PRINT]

Proyecta gotas de tinta líquida y ofrece excelente reproducción del color.

### 37. ¿Qué tecnología de impresión permite hacer copia por presión (papel autocopiativo, formularios multicopia)?

- a) Matricial (de impacto)
- b) Láser
- c) Inyección

**Respuesta correcta:** a) · **Referencia:** §4.1 [HP-PRINT]

Es la única que, al golpear el papel, genera copia por presión.

### 38. El consumible característico de una impresora láser es:

- a) El cartucho de tinta líquida
- b) El tóner (cartucho de polvo)
- c) La cinta entintada

**Respuesta correcta:** b) · **Referencia:** §4.2 [HP-PRINT]

El tóner tiene alto rendimiento (miles de páginas).

### 39. PostScript y PCL son ejemplos de:

- a) Sistemas de archivos
- b) Protocolos inalámbricos
- c) Lenguajes de descripción de página (PDL)

**Respuesta correcta:** c) · **Referencia:** §4.3 [HP-PRINT]

PostScript (Adobe) es independiente del dispositivo; PCL (HP) es muy común en ofimática.

### 40. El componente que recibe los trabajos de impresión, los pone en cola y los envía en orden a la impresora es:

- a) El spooler (cola de impresión)
- b) El fusor
- c) El sensor CIS

**Respuesta correcta:** a) · **Referencia:** §4.3 [HP-PRINT]

Libera enseguida la aplicación y gestiona prioridades, pausas y reintentos.

### 41. La impresión 3D o fabricación aditiva construye objetos:

- a) Quitando material de un bloque macizo
- b) Capa a capa, añadiendo material a partir de un modelo digital
- c) Únicamente en dos dimensiones

**Respuesta correcta:** b) · **Referencia:** §4.4 [ISO3664]

Frente a la fabricación sustractiva, la aditiva añade material solo donde hace falta.

### 42. ¿Qué tecnología de impresión 3D deposita filamento termoplástico fundido capa a capa?

- a) SLA (estereolitografía)
- b) SLS (sinterizado por láser)
- c) FDM (modelado por deposición fundida)

**Respuesta correcta:** c) · **Referencia:** §4.4 [ISO3664]

Es la más común y económica; SLA usa resina y SLS sinteriza polvo.

### 43. ¿Cuál de estos dispositivos de almacenamiento carece de partes móviles?

- a) El SSD (memoria flash NAND)
- b) El disco duro HDD
- c) La cinta magnética LTO

**Respuesta correcta:** a) · **Referencia:** §5.1 [APFS-NTFS]

Al no tener partes móviles es más rápido, silencioso y resistente que un HDD.

### 44. Los CD, DVD y Blu-ray son soportes de almacenamiento:

- a) Magnéticos
- b) Ópticos (lectura con láser)
- c) De estado sólido

**Respuesta correcta:** b) · **Referencia:** §5.1 [ISO9660]

DVD almacena 4,7 GB por capa y Blu-ray entre 25 y 100 GB.

### 45. Para el archivo masivo a largo plazo, por su bajo coste por TB, sigue siendo referencia:

- a) El CD-ROM
- b) El SSD NVMe
- c) La cinta magnética (LTO)

**Respuesta correcta:** c) · **Referencia:** §5.1 [APFS-NTFS]

Es un soporte secuencial de altísima capacidad y bajo coste para copias y archivo.

### 46. Un SSD NVMe se diferencia de un SSD SATA en que:

- a) NVMe es más lento
- b) NVMe usa PCIe y es mucho más rápido que SATA
- c) Ambos tienen exactamente la misma velocidad

**Respuesta correcta:** b) · **Referencia:** §5.2 [APFS-NTFS]

NVMe aprovecha el paralelismo de la flash; se usa en formato M.2.

### 47. El sistema de archivos FAT32 tiene como limitación destacada:

- a) No admite archivos mayores de 4 GB
- b) No es compatible con Windows
- c) No permite nombrar carpetas

**Respuesta correcta:** a) · **Referencia:** §5.3 [APFS-NTFS]

Para soportes extraíbles grandes se prefiere exFAT.

### 48. ¿Qué sistema de archivos es el estándar en Linux, con journaling?

- a) NTFS
- b) APFS
- c) ext4

**Respuesta correcta:** c) · **Referencia:** §5.3 [APFS-NTFS]

NTFS es el de Windows y APFS el de macOS; el journaling ayuda a recuperar la coherencia tras un corte.

### 49. El esquema de particionado moderno, asociado a UEFI y sin el límite de 2 TB, es:

- a) MBR
- b) GPT (GUID Partition Table)
- c) FAT

**Respuesta correcta:** b) · **Referencia:** §5.4 [UEFI-GPT]

MBR está limitado a 2 TB y 4 particiones primarias.

### 50. Una copia de seguridad incremental copia:

- a) Solo los datos cambiados desde la última copia (completa o incremental)
- b) Todos los datos cada vez
- c) Solo los datos cambiados desde la última copia completa

**Respuesta correcta:** a) · **Referencia:** §5.5

Para restaurar se necesitan la completa y toda la cadena de incrementales. La diferencial, en cambio, copia lo cambiado desde la última completa.

### 51. La regla 3-2-1 de copias de seguridad recomienda:

- a) 3 discos duros idénticos en el mismo equipo
- b) 3 copias completas cada día
- c) 3 copias, en 2 tipos de soporte, con 1 copia fuera de las instalaciones

**Respuesta correcta:** c) · **Referencia:** §5.5

Además hay que verificar periódicamente que la restauración funciona.

### 52. ¿Cuál de estas afirmaciones sobre RAID es CORRECTA?

- a) RAID no es una copia de seguridad: protege frente a la avería de un disco, no frente a un borrado o un ransomware
- b) RAID sustituye completamente a las copias de seguridad
- c) RAID 0 ofrece la máxima tolerancia a fallos

**Respuesta correcta:** a) · **Referencia:** §5.6 [SNIA-RAID]

RAID 0 no tiene redundancia; se necesitan RAID y backup.

### 53. ¿Qué nivel RAID hace un espejo (copia idéntica) que tolera el fallo de un disco?

- a) RAID 0
- b) RAID 1
- c) RAID 5

**Respuesta correcta:** b) · **Referencia:** §5.6 [SNIA-RAID]

El <em>mirroring</em> duplica los datos; ofrece alta fiabilidad pero solo el 50 % de capacidad útil.

### 54. RAID 5 se basa en:

- a) Un simple espejo de dos discos
- b) Reparto sin ninguna redundancia
- c) Striping con paridad distribuida, que tolera el fallo de 1 disco (mínimo 3 discos)

**Respuesta correcta:** c) · **Referencia:** §5.6 [SNIA-RAID]

RAID 6 añade doble paridad y tolera 2 fallos.

### 55. El sensor de un escáner que capta la luz reflejada del documento puede ser de tipo:

- a) CCD o CIS
- b) HDMI o VGA
- c) FAT o NTFS

**Respuesta correcta:** a) · **Referencia:** §6.1 [NTI-DIGIT]

El CCD ofrece mayor calidad y el CIS es más compacto y económico.

### 56. El OCR (Reconocimiento Óptico de Caracteres) sirve para:

- a) Aumentar la resolución del monitor
- b) Convertir la imagen de un texto en texto editable y buscable
- c) Cifrar el documento escaneado

**Respuesta correcta:** b) · **Referencia:** §6.1 [NTI-DIGIT]

Suele generar un PDF con capa de texto (PDF buscable).

### 57. El modelo de color RGB es:

- a) Sustractivo, propio de la impresión
- b) Un espacio independiente del dispositivo
- c) Aditivo, propio de pantallas, cámaras y escáneres (la suma de los tres da blanco)

**Respuesta correcta:** c) · **Referencia:** §6.3 [CIE]

CMYK es el sustractivo de la impresión y CIELAB el de referencia independiente del dispositivo.

### 58. ¿Qué formato de imagen utiliza compresión CON pérdida y es idóneo para fotografías?

- a) JPEG
- b) PNG
- c) TIFF

**Respuesta correcta:** a) · **Referencia:** §6.4 [ISO15948]

Su factor de calidad regula la compresión; PNG y TIFF son sin pérdida.

### 59. Según la NTI de Digitalización de Documentos, la resolución mínima para digitalizar un documento en soporte papel es de:

- a) 72 ppp
- b) 200 ppp
- c) 1.200 ppp

**Respuesta correcta:** b) · **Referencia:** §6.5 [NTI-DIGIT]

La NTI (Resolución de 19-jul-2011, ENI) fija ese mínimo para garantizar fidelidad sin archivos desproporcionados.

### 60. El resultado de una digitalización certificada conforme a la NTI, firmada y con metadatos, es:

- a) Un simple borrador sin validez
- b) Una fotocopia en papel
- c) Una copia auténtica con el mismo valor que el original (art. 27 Ley 39/2015)

**Respuesta correcta:** c) · **Referencia:** §6.6 [NTI-DIGIT][L39-2015]

La imagen electrónica firmada (o con CSV) puede sustituir al original en papel.

## Preguntas sobre los casos prácticos

### Caso 1. Puesto de trabajo de una Oficina de Atención a la Ciudadanía

#### 1. En el supuesto planteado, el portátil debe conectarse al docking con un solo cable que lleve datos, vídeo para los monitores y energía de carga. ¿Qué interfaz es la idónea?

- a) HDMI 2.1, que transporta por el mismo cable el vídeo, el audio digital y el canal de retorno eARC.
- b) Thunderbolt sobre conector USB-C (o USB4 con USB Power Delivery), que combina datos PCIe, vídeo DisplayPort y energía.
- c) eSATA, la versión externa de SATA, que conecta el portátil a los periféricos de la estación de acoplamiento.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.4

Desde Thunderbolt 3 se usa el conector USB-C y un único cable combina datos (PCIe), vídeo (DisplayPort) y energía; es la interfaz típica de las docking stations.

#### 2. El técnico comprueba que el portátil tiene un puerto USB-C y da por hecho que servirá para el docking. ¿Qué debe tener en cuenta?

- a) Que USB-C es solo la forma del conector: por dentro el puerto puede ser USB 2.0 o USB4, y hay que comprobar el protocolo.
- b) Que todo puerto USB-C es internamente USB4, por lo que garantiza 40 Gbps y la salida de vídeo a los monitores.
- c) Que USB-C solo transporta datos y energía, de modo que el vídeo de los monitores exige un cable HDMI aparte.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.2

El contenido advierte que USB-C es un conector, no una velocidad: un puerto USB-C puede ser USB 2.0 o USB4 y por fuera son idénticos.

#### 3. Para conectar los dos monitores del puesto desde una sola salida del docking, encadenándolos en serie, ¿qué interfaz y tecnología deben usarse?

- a) HDMI con eARC, que permite encadenar varios monitores desde una única salida del equipo.
- b) DVI con conexión en cadena, interfaz de transición que sustituyó a VGA en el entorno profesional.
- c) DisplayPort con MST (Multi-Stream Transport), que permite la conexión en cadena (daisy-chain).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.3

La gran ventaja de DisplayPort es MST, que permite encadenar varios monitores en serie desde una sola salida.

#### 4. Si en lugar de DisplayPort se usara la alternativa propia del ámbito de consumo, HDMI, ¿qué implicaría para los dos monitores del puesto?

- a) Que normalmente haría falta una salida HDMI por cada monitor, porque HDMI no los encadena en serie.
- b) Que los monitores podrían encadenarse igual, ya que HDMI 2.1 incorpora la tecnología MST de VESA.
- c) Que la señal pasaría a ser analógica y necesitaría un convertidor para cada uno de los monitores.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §2.3

El contenido resume: HDMI = consumo/audiovisual, un monitor por puerto; DisplayPort admite varios monitores en cadena (MST). HDMI es digital.

#### 5. Windows detecta el lector de DNI electrónico, pero aparece con un aviso en el Administrador de dispositivos y no funciona. ¿Cómo debe interpretarse ese aviso?

- a) Como una avería física del chip del DNI que se ha insertado.
- b) Como un problema de controlador (driver) del lector.
- c) Como una interferencia con el teclado y el ratón inalámbricos.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §3.4

Un dispositivo detectado pero marcado con aviso en el Administrador de dispositivos indica un problema de controlador (driver).

#### 6. Ante el lector de DNI que no funciona, ¿por dónde debe empezar el diagnóstico del técnico?

- a) Por reinstalar el sistema operativo del portátil para descartar daños en el sistema.
- b) Por revertir el controlador del lector a la versión anterior que tuviera instalada.
- c) Por comprobar lo físico: el cable y el puerto en que está conectado el lector.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §3.4

El diagnóstico va de lo físico y sencillo a lo lógico y complejo: primero cable y puerto; reinstalar el sistema ante un cable suelto es el error clásico.

#### 7. Windows ha cargado para el lector un controlador genérico, que no basta para que funcione. ¿Qué debe hacer el técnico?

- a) Instalar o actualizar el controlador del fabricante, preferiblemente firmado digitalmente.
- b) Mantener el controlador genérico, que es el que desbloquea todas las funciones del lector.
- c) Desactivar la exigencia de firma para poder instalar cualquier controlador que funcione.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §2.7

El driver genérico da funcionalidad básica y el del fabricante desbloquea todas las funciones; la firma garantiza origen e integridad y evita código malicioso.

#### 8. Para aislar si el fallo está en el lector de DNI o en el propio portátil, ¿qué prueba corresponde al final del diagnóstico?

- a) Reinstalar el sistema operativo del portátil antes de probar el lector en otro sitio.
- b) Sustituir el docking por otro modelo, puesto que el lector depende de su firmware.
- c) Probar el lector en otro equipo y, si procede, otro dispositivo en el mismo puerto.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §3.4

El paso «Aislar» consiste en probar el periférico en otro equipo (¿falla el dispositivo o el equipo?) y otro dispositivo en el mismo puerto.

#### 9. ¿Cómo se aplica en el puesto la prohibición municipal de usar memorias USB no autorizadas?

- a) Cifrando con BitLocker todas las memorias USB, de modo que cualquiera de ellas pueda usarse libremente en el puesto.
- b) Con políticas de control de dispositivos (GPO) que bloquean el almacenamiento extraíble no autorizado, junto a listas blancas.
- c) Desactivando Plug & Play en el portátil, para que ningún dispositivo USB se detecte al conectarlo al equipo.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §3.5

Se aplica con políticas de control de dispositivos y puertos por directiva de grupo (GPO) que bloquean el almacenamiento extraíble no autorizado, junto a listas blancas.

#### 10. Además del bloqueo de memorias USB, ¿qué dos medidas de protección de la información exigibles por el Esquema Nacional de Seguridad propone la solución para el portátil?

- a) Cifrar su disco con BitLocker y someterlo a borrado seguro cuando el equipo se dé de baja.
- b) Montar un RAID 0 en el disco y aplicarle un formateo rápido cuando el equipo se dé de baja.
- c) Imprimir con liberación segura y conectar los dos monitores en cadena mediante DisplayPort.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §3.6

Medidas del ENS: cifrado con BitLocker (soporte perdido = ilegible) y borrado seguro del disco al dar de baja el equipo.

### Caso 2. Renovación del parque de impresión de un distrito

#### 1. En el supuesto planteado, ¿por qué la impresión láser es la adecuada para el grueso del trabajo del distrito?

- a) Por su excelente reproducción del color y de las fotografías, idónea para los carteles del distrito.
- b) Porque es la única tecnología capaz de hacer copia por presión sobre los formularios multicopia.
- c) Por su alta velocidad y su bajo coste por página, idóneos para grandes volúmenes de texto en blanco y negro.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §4.1

La láser ofrece alta velocidad y bajo coste por página, ideal para grandes volúmenes de texto en blanco y negro (informes, notificaciones).

#### 2. ¿Qué tecnología conviene mantener para los formularios multicopia por presión de la unidad de recaudación?

- a) La impresora térmica, que transfiere la tinta de una cinta por calor sobre el papel autocopiativo.
- b) La impresora matricial (de impacto), única que genera copia por presión sobre papel autocopiativo.
- c) La impresora láser en red, cuyo fusor ejerce la presión suficiente para obtener las copias.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §4.1

Para los formularios multicopia conviene mantener una matricial (de impacto), «la única que genera copia por presión sobre papel autocopiativo».

#### 3. Tras la renovación del parque, ¿a qué se reservaría, si acaso, la impresión de inyección de tinta?

- a) Al color fotográfico puntual.
- b) A los formularios multicopia.
- c) A las notificaciones en blanco y negro.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §4.1

Con láser para el volumen y matricial para el multicopia, la inyección de tinta queda, si acaso, para el color fotográfico puntual.

#### 4. Un empleado manda imprimir una notificación a la multifunción en red. ¿Qué hace el spooler?

- a) Traduce la página a un formato independiente del papel concreto, como hacen PostScript o PCL con cada trabajo.
- b) Recibe el trabajo, lo pone en cola y lo envía en orden a la impresora, liberando enseguida la aplicación del usuario.
- c) Asigna a la impresora una dirección IP propia para que cualquier equipo autorizado la use sin un PC intermediario.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.3

El spooler recibe los trabajos, los pone en cola y los envía en orden a la impresora, liberando la aplicación y gestionando prioridades, pausas y reintentos.

#### 5. ¿Qué protocolo de impresión moderno debe citarse para las nuevas multifunción en red?

- a) LPD/LPR, el protocolo clásico de colas.
- b) El puerto RAW 9100 de la impresora.
- c) IPP (Internet Printing Protocol).

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §4.3

IPP es el estándar moderno (base de AirPrint y de la impresión sin driver); LPD/LPR y el puerto RAW 9100 son los antiguos.

#### 6. Para describir las páginas que enviarán los equipos a las multifunción, ¿qué ejemplos de lenguaje de descripción de página (PDL) son correctos?

- a) PostScript o PCL, además del PDF directo.
- b) IPP o LPD/LPR, además del RAW 9100.
- c) RGB o CMYK, además del modelo CIELAB.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §4.3

Los principales PDL son PostScript, PCL y, cada vez más, PDF directo; IPP y LPD/LPR son protocolos y RGB/CMYK, modelos de color.

#### 7. ¿Qué mecanismo evita que las notificaciones con datos personales queden olvidadas en la bandeja de la multifunción?

- a) La impresión dúplex por defecto, fijada por GPO, que reduce a la mitad las hojas que salen a la bandeja de la impresora.
- b) El spooler, que envía cada trabajo a la impresora en el orden de llegada y lo borra en cuanto termina de imprimirlo.
- c) La impresión con liberación segura (pull printing): el documento solo se imprime cuando el usuario se identifica con tarjeta o PIN.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §4.3, §3.5

Con la liberación segura el trabajo se retiene en la cola y solo se imprime cuando el usuario se identifica con su tarjeta o PIN en el equipo.

#### 8. Al comparar los consumibles de las nuevas láser con los de las impresoras de inyección de tinta actuales, ¿qué es correcto?

- a) La tinta líquida rinde miles de páginas por cartucho, mientras que el tóner debe sustituirse con más frecuencia.
- b) El tóner es un cartucho de polvo de alto rendimiento (miles de páginas); la tinta rinde menos y cuesta más por página.
- c) El tóner y la tinta tienen el mismo coste por página; solo cambia la forma en que se fijan sobre el papel.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §4.2

La láser usa tóner (polvo, alto rendimiento, miles de páginas) frente a los cartuchos de tinta, de menor rendimiento y mayor coste por página.

#### 9. ¿Con qué criterio económico se decide la elección de impresoras en un parque grande como el del distrito?

- a) Con el coste por página (CPP) y el rendimiento del consumible.
- b) Con el precio de compra de cada equipo, sin tener en cuenta el consumible.
- c) Con la resolución en ppp que alcanza cada impresora del distrito.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §4.2

El coste por página (CPP) y el rendimiento del consumible son los criterios económicos que guían la elección en un parque grande.

#### 10. ¿Qué dos medidas de configuración centralizada por GPO propone la solución para ahorrar consumibles en el distrito?

- a) Fijar por defecto la impresión en color y a la máxima resolución en ppp.
- b) Instalar a mano en cada puesto los drivers y la impresora por defecto.
- c) Fijar por defecto la impresión a doble cara (dúplex) y en blanco y negro.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §3.2

Con directivas de grupo (GPO) se fija la configuración: doble cara y blanco y negro por defecto para ahorrar consumibles; la instalación no se hace máquina por máquina.

### Caso 3. Almacenamiento y digitalización de expedientes

#### 1. En el supuesto planteado, ¿qué nivel RAID NO cumpliría el requisito de que la avería de un disco no detenga el servicio ni pierda datos?

- a) RAID 5, porque usa paridad distribuida.
- b) RAID 0, porque reparte los datos sin redundancia.
- c) RAID 6, porque usa doble paridad.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §5.6

RAID 0 no tiene tolerancia a fallos (si falla un disco se pierde todo); RAID 5 tolera 1 fallo y RAID 6, 2 fallos.

#### 2. Un empleado del archivo borra por error una carpeta de expedientes del servidor, que tiene RAID 6. ¿Qué es correcto?

- a) El RAID 6 recupera la carpeta de forma automática, porque tolera la avería de dos discos.
- b) La carpeta sigue en los bloques de doble paridad y se recupera reconstruyendo el conjunto.
- c) El RAID no protege frente al borrado: la carpeta debe restaurarse desde la copia de seguridad.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §5.6

El RAID protege frente a la avería de un disco, pero NO es una copia de seguridad: no protege frente a un borrado accidental, un ransomware ni un desastre.

#### 3. ¿Cuál de estos diseños de copias cumple la regla 3-2-1 para el archivo?

- a) Datos de producción en el servidor, una copia en un NAS y otra en cinta o en la nube fuera de las instalaciones.
- b) Datos de producción en el servidor y dos copias en cinta guardadas en el propio servicio de archivo municipal.
- c) Datos de producción en el servidor y dos copias en otros dos volúmenes del mismo conjunto RAID del servidor.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §5.5

Regla 3-2-1: 3 copias (producción + 2), en 2 tipos de soporte distintos (p. ej. NAS + cinta o nube), con 1 copia fuera de las instalaciones.

#### 4. El archivo hace una copia completa el domingo e incrementales el resto de días. Si un ransomware cifra el servidor el viernes, ¿qué se necesita para restaurar?

- a) Solo la última copia incremental, que ya contiene todos los cambios de la semana.
- b) La copia completa del domingo y únicamente la última incremental realizada.
- c) La copia completa del domingo y toda la cadena de incrementales posteriores.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §5.5

La incremental copia solo lo cambiado desde la última copia; para restaurar hace falta la completa y toda la cadena de incrementales.

#### 5. Si en lugar de incrementales el archivo hiciera copias diferenciales diarias, ¿qué se necesitaría para restaurar?

- a) Solo la última diferencial realizada.
- b) La copia completa y la última diferencial.
- c) La completa y la primera diferencial.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §5.5

La diferencial copia lo cambiado desde la última completa; la restauración se hace con solo dos piezas: completa + última diferencial.

#### 6. ¿Por qué FAT32 no serviría para el recurso de red que guarda los expedientes escaneados de más de 5 GB?

- a) Porque no admite archivos mayores de 4 GB.
- b) Porque no puede leerse desde equipos Linux.
- c) Porque no admite más de 4 particiones.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §5.3

FAT32 es muy compatible pero tiene un límite de 4 GB por archivo, y los expedientes superan los 5 GB; el límite de 4 particiones primarias es de MBR.

#### 7. ¿Qué sistema de archivos es el habitual para el recurso de red compartido del servidor de archivo?

- a) exFAT, el sucesor de FAT32 pensado para los servidores de ficheros.
- b) NTFS o ext4, que aportan permisos y journaling, con acceso por SMB/NFS.
- c) ISO 9660 o UDF, por ser los formatos de archivo a largo plazo.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §5.3, §5.4

Para un recurso de red compartido lo habitual es NTFS/ext4 con acceso por SMB/NFS; exFAT es para extraíbles e ISO 9660/UDF, para ópticos.

#### 8. Al configurar el escáner del archivo para la digitalización certificada, ¿qué ajuste cumple la NTI?

- a) Capturar a 100 ppp en escala de grises, suficiente para que funcione el OCR.
- b) Capturar a 150 ppp en color, para reducir el tamaño de los expedientes.
- c) Capturar a 200 ppp o más y guardar en PDF/A, formato preferible para el archivo.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §6.5

La NTI exige una resolución mínima de 200 ppp para el papel y formatos del catálogo de estándares, priorizando PDF/A para el archivo a largo plazo.

#### 9. ¿Cuál es el orden correcto del proceso de digitalización certificada según la NTI?

- a) Captura, optimización/OCR, metadatos, firma o CSV e incorporación al expediente.
- b) Captura, firma o CSV, optimización/OCR, metadatos e incorporación al expediente.
- c) Metadatos, captura, firma o CSV, optimización/OCR e incorporación al expediente.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §6.6

Pasos NTI: (1) captura; (2) optimización/OCR sin alterar el contenido; (3) metadatos mínimos; (4) firma electrónica o CSV; (5) incorporación al expediente y al archivo.

#### 10. ¿Qué permite, en el supuesto, devolver el expediente en papel al ciudadano?

- a) Que la imagen pase por OCR y se guarde como PDF buscable en el servidor del archivo.
- b) Que la imagen, con metadatos y firma o CSV, sea una copia auténtica (art. 27 Ley 39/2015).
- c) Que la imagen se almacene en un RAID 6 con una copia de seguridad fuera del edificio.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §6.5, §6.6

Con metadatos y firma/CSV que garantizan integridad y autenticidad se obtiene una copia auténtica (art. 27 Ley 39/2015), que permite devolver el papel.
