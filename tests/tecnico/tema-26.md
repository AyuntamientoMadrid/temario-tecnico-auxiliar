# Test del tema 26. Almacenamiento, virtualización y copias de seguridad

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-26.html>

## Batería de preguntas

### 1. ¿Qué caracteriza al almacenamiento de conexión directa (DAS)?

- a) Está conectado directamente a un servidor por un bus local y no se comparte con otros servidores
- b) Sirve ficheros por la red IP mediante NFS o SMB a muchos clientes simultáneos
- c) Requiere una red dedicada de Fibre Channel con conmutadores y zoning

**Respuesta correcta:** a) · **Referencia:** §1.1.1 [SNIA-DICT]

El DAS emplea interfaces SAS, SATA o NVMe sin red de almacenamiento de por medio; su limitación esencial no es el rendimiento, que es excelente, sino la imposibilidad de compartirlo.

### 2. En una cabina NAS, ¿quién gestiona el sistema de ficheros?

- a) El servidor cliente, que formatea el volumen recibido
- b) La propia cabina, que publica carpetas y ficheros a los clientes
- c) El conmutador de la red de almacenamiento

**Respuesta correcta:** b) · **Referencia:** §1.1.2 [SNIA-DICT]

Es la diferencia estructural con la SAN: si se sirven ficheros, el sistema de ficheros vive en la cabina; si se sirven bloques, lo pone el servidor.

### 3. ¿Qué unidad presenta una SAN a los servidores?

- a) Una carpeta compartida con permisos por usuario
- b) Un contenedor de objetos accesible por HTTP
- c) Un LUN, que el servidor ve como si fuera un disco propio

**Respuesta correcta:** c) · **Referencia:** §1.1.2 [SNIA-DICT] [T10-SCSI]

El LUN (<em>Logical Unit Number</em>) es la unidad lógica de bloque que la cabina presenta; el servidor le aplica su tabla de particiones y su sistema de ficheros.

### 4. ¿Dónde se configura el zoning en una red de almacenamiento Fibre Channel?

- a) En la controladora RAID del servidor
- b) En el conmutador de la SAN
- c) En el sistema operativo invitado de cada máquina virtual

**Respuesta correcta:** b) · **Referencia:** §1.1.2 [T11-FC] [NIST-SP800-209]

El zoning se configura en el conmutador y decide qué iniciador ve qué objetivo; el LUN masking, que es complementario, se configura en la cabina y decide qué unidad lógica ve cada servidor.

### 5. ¿Cuál de estos rasgos define al almacenamiento de objetos?

- a) Un árbol jerárquico de directorios con permisos heredados
- b) Acceso mediante comandos SCSI encapsulados en TCP
- c) Espacio de nombres plano, metadatos ricos y acceso por API REST sobre HTTP

**Respuesta correcta:** c) · **Referencia:** §1.1.3 [SNIA-DICT] [RFC9110]

El objeto se compone de contenido, metadatos extensibles e identificador único, y se guarda en contenedores sin jerarquía real de carpetas.

### 6. ¿Para cuál de estos usos NO es adecuado el almacenamiento de objetos?

- a) Alojar el disco de una base de datos transaccional en producción
- b) Guardar copias de seguridad inmutables con retención WORM
- c) Conservar documentos digitalizados del archivo electrónico

**Respuesta correcta:** a) · **Referencia:** §1.1.3 [SNIA-DICT] [S3-LOCK]

El objeto no admite modificación parcial —se escribe una versión nueva— y su latencia es la de una petición HTTP, lo que lo descarta para cargas transaccionales.

### 7. ¿Qué es una cabina de almacenamiento unificado?

- a) Una cabina que solo admite un protocolo, elegido en la instalación
- b) Un conjunto de cabinas idénticas replicadas entre dos centros de proceso de datos
- c) Una cabina que ofrece simultáneamente acceso por bloque, por fichero y, en muchos casos, por objeto sobre el mismo pool

**Respuesta correcta:** c) · **Referencia:** §1.1.3 [SNIA-DICT]

Su ventaja es la consolidación; su riesgo, convertirse en un punto único de fallo de servicios muy distintos, lo que obliga a que las copias no residan en ella.

### 8. ¿Qué puerto TCP utiliza iSCSI de forma estándar?

- a) 3260
- b) 2049
- c) 445

**Respuesta correcta:** a) · **Referencia:** §1.2.1 [RFC7143]

El 2049 corresponde a NFS y el 445 a SMB. Los extremos iSCSI se nombran con IQN y la autenticación estándar es CHAP.

### 9. ¿Qué identificador emplea Fibre Channel para nombrar sus puertos?

- a) IQN
- b) WWN
- c) NQN

**Respuesta correcta:** b) · **Referencia:** §1.2.1 [T11-FC]

El WWN (<em>World Wide Name</em>) es un identificador único de 64 bits, análogo funcional de la dirección MAC. El IQN identifica extremos iSCSI y el NQN, extremos NVMe over Fabrics.

### 10. ¿Qué aporta NVMe over Fabrics frente a iSCSI?

- a) Permite servir ficheros además de bloques
- b) Elimina la necesidad de red, al ser una conexión directa
- c) Transporta el juego de comandos NVMe, con colas paralelas y menor latencia, sobre RDMA, Fibre Channel o TCP

**Respuesta correcta:** c) · **Referencia:** §1.2.1 [NVME-OF]

Sustituye el modelo de cola única de SCSI por miles de colas paralelas, diseñado para memoria flash.

### 11. ¿Qué versión de NFS incorpora sesiones con estado, seguridad Kerberos integrada y pNFS?

- a) NFS versión 2
- b) NFS versión 4.1
- c) NFS versión 3

**Respuesta correcta:** b) · **Referencia:** §1.2.1 [RFC8881] [RFC1813]

Definida en el RFC 8881, unifica montaje y bloqueo en un solo protocolo sobre el puerto 2049, frente a la versión 3, sin estado y dependiente de protocolos auxiliares.

### 12. ¿Cuál de estas funciones es propia de SMB 3.x?

- a) Cifrado en tránsito, multichannel y continuidad transparente ante la caída de un nodo
- b) Encapsular comandos SCSI para presentar LUN a los servidores
- c) Calcular la ubicación de los objetos mediante el algoritmo CRUSH

**Respuesta correcta:** a) · **Referencia:** §1.2.1 [MS-SMB2]

SMB 3.x opera sobre el puerto 445 y se integra con la autenticación de dominio y las listas de control de acceso.

### 13. En un conjunto RAID 5 de 8 discos de 4 TB, ¿cuál es la capacidad útil aproximada y cuántos discos tolera?

- a) 32 TB y tolera 1 disco
- b) 16 TB y tolera 2 discos
- c) 28 TB y tolera 1 disco

**Respuesta correcta:** c) · **Referencia:** §1.2.2 [PATTERSON88]

RAID 5 ofrece una capacidad útil de n−1 discos: (8−1) × 4 = 28 TB, con tolerancia al fallo de un solo disco.

### 14. ¿Qué nivel RAID ofrece doble paridad distribuida?

- a) RAID 6
- b) RAID 5
- c) RAID 10

**Respuesta correcta:** a) · **Referencia:** §1.2.2 [PATTERSON88]

RAID 6 tolera el fallo simultáneo de dos discos y ofrece una capacidad útil de n−2, lo que lo ha convertido en el mínimo razonable con discos de gran capacidad por el riesgo durante la reconstrucción.

### 15. ¿Qué nivel RAID conviene a una base de datos con escritura muy intensa?

- a) RAID 5, porque desperdicia menos capacidad
- b) RAID 10, porque su penalización de escritura es de solo dos operaciones
- c) RAID 0, porque es el más rápido en todos los escenarios

**Respuesta correcta:** b) · **Referencia:** §1.2.2 [PATTERSON88]

RAID 5 exige cuatro operaciones físicas por escritura y RAID 6 seis; además, RAID 0 carece por completo de tolerancia a fallos.

### 16. ¿Cuál es el riesgo característico del aprovisionamiento fino (thin provisioning)?

- a) Que el servidor no pueda ampliar el volumen en caliente
- b) Que obligue a reservar toda la capacidad desde el primer momento
- c) Que, si el pool se llena físicamente, fallen a la vez todos los volúmenes que dependen de él

**Respuesta correcta:** c) · **Referencia:** §1.2.2 [SNIA-DICT] [T10-SCSI]

El sobreaprovisionamiento exige umbrales de alerta y un procedimiento de ampliación; la orden UNMAP permite devolver al pool el espacio liberado.

### 17. ¿Qué diferencia hay entre deduplicación en origen y en destino?

- a) En origen se ejecuta en el cliente, con lo que se reduce también el tráfico de red; en destino, en la cabina o el repositorio
- b) En origen se ejecuta después de escribir y en destino antes de escribir
- c) En origen solo se aplica a ficheros y en destino solo a bloques

**Respuesta correcta:** a) · **Referencia:** §1.2.2 [SNIA-DICT]

La distinción entre antes o después de escribir es la de deduplicación en línea (inline) frente a posproceso, que es un eje diferente.

### 18. ¿En qué consiste la virtualización del almacenamiento?

- a) En ejecutar varios sistemas operativos sobre un mismo servidor mediante un hipervisor
- b) En sustituir los discos magnéticos por unidades de estado sólido
- c) En interponer una capa de abstracción que presenta volúmenes lógicos independientes del hardware físico que los soporta

**Respuesta correcta:** c) · **Referencia:** §2.1 [SNIA-DICT]

No debe confundirse con la virtualización de servidores, que es su principal consumidor pero una disciplina distinta.

### 19. LVM en Linux es un ejemplo canónico de virtualización de almacenamiento…

- a) Basada en la cabina
- b) Basada en el host
- c) Basada en la red

**Respuesta correcta:** b) · **Referencia:** §2.1.1 [LVM-LINUX]

El gestor de volúmenes lógicos se ejecuta en el sistema operativo del servidor y agrupa volúmenes físicos en grupos de volúmenes de los que talla volúmenes lógicos ampliables en caliente.

### 20. Se quiere unificar cabinas de fabricantes distintos y migrar los datos sin parar el servicio. ¿Qué modelo de virtualización encaja mejor?

- a) Basada en la red, mediante un appliance o conmutador virtualizador situado en el fabric
- b) Basada en el host, instalando un gestor de volúmenes en cada servidor
- c) Basada en la cabina, activando los pools de una de ellas

**Respuesta correcta:** a) · **Referencia:** §2.1.1 [SNIA-DICT]

Es el modelo que mejor resuelve la heterogeneidad; su precio es la latencia añadida al operar en banda y la necesidad de duplicar el dispositivo.

### 21. En una capa de virtualización que trabaja «fuera de banda» (out-of-band)…

- a) Todas las lecturas y escrituras atraviesan la capa de virtualización
- b) La capa se ejecuta necesariamente dentro de la cabina de almacenamiento
- c) La capa gestiona solo los metadatos y los datos van directamente del servidor a la cabina

**Respuesta correcta:** c) · **Referencia:** §2.1 [SNIA-DICT]

Por eso no añade latencia, a costa de exigir software específico en cada servidor. El modelo en banda es el contrario.

### 22. ¿Cuál es el rasgo definitorio del almacenamiento definido por software (SDS)?

- a) Que se gestiona mediante una consola gráfica en lugar de por línea de órdenes
- b) Que separa el plano de control, basado en políticas, del plano de datos, y se ejecuta sobre hardware estándar
- c) Que sustituye el RAID por una controladora propietaria de doble paridad

**Respuesta correcta:** b) · **Referencia:** §2.1.2 [SNIA-SDS]

No basta con que un producto se gobierne por software: lo distintivo es que la inteligencia deja de residir en hardware propietario y el crecimiento es horizontal.

### 23. ¿Cómo protege el dato una solución SDS típica?

- a) Mediante réplica de varias copias entre nodos o codificación de borrado (erasure coding)
- b) Mediante una única controladora RAID compartida por todos los nodos
- c) Mediante cintas WORM insertadas en cada nodo

**Respuesta correcta:** a) · **Referencia:** §2.1.2 [CEPH] [SNIA-SDS]

La protección se hace por software y puede tolerar la caída de discos, de nodos o incluso de armarios completos, según la política definida.

### 24. ¿Qué elimina una infraestructura hiperconvergente (HCI) respecto de la arquitectura clásica de tres capas?

- a) La necesidad de hipervisor, al ejecutar las aplicaciones directamente sobre el hardware
- b) La necesidad de copias de seguridad, al replicar los bloques entre nodos
- c) La cabina de almacenamiento dedicada, sustituida por los discos locales de los nodos agregados por software

**Respuesta correcta:** c) · **Referencia:** §2.2.1 [VSAN] [NUTANIX]

Con ella desaparecen también el fabric Fibre Channel, el zoning y el LUN masking, y la gestión se unifica en una sola consola.

### 25. ¿Cuál es la unidad de crecimiento de una infraestructura hiperconvergente?

- a) El nodo, que aporta a la vez cómputo, memoria y capacidad
- b) La bandeja de discos de la cabina
- c) El conmutador de la red de almacenamiento

**Respuesta correcta:** a) · **Referencia:** §2.2.1 [VSAN] [S2D]

Es su virtud —crecimiento incremental y predecible— y su limitación, porque ambos recursos crecen acoplados, algo que se mitiga con nodos solo de almacenamiento.

### 26. ¿Por qué debe reservarse espacio libre sin usar en el pool de un clúster hiperconvergente?

- a) Porque el aprovisionamiento fino lo exige para poder crear volúmenes nuevos
- b) Porque el sistema necesita sitio para reconstruir los datos cuando cae un disco o un nodo
- c) Porque el hipervisor guarda ahí los ficheros de configuración del clúster

**Respuesta correcta:** b) · **Referencia:** §2.2.1 [VSAN] [NUTANIX]

Llenar el pool al límite deja al clúster sin capacidad de autorrepararse; es el error de dimensionado más frecuente en estas arquitecturas.

### 27. ¿Cuál de estas causas de pérdida de datos NO queda cubierta por un RAID 6?

- a) El fallo simultáneo de dos discos del conjunto
- b) El borrado accidental de una carpeta por un usuario
- c) El fallo de un único disco durante la reconstrucción de otro

**Respuesta correcta:** b) · **Referencia:** §3.1 [ISO27002] [NIST-SP800-209]

El RAID protege del fallo físico del disco, pero replica al instante el borrado, la corrupción lógica y el cifrado por ransomware: no es una copia de seguridad.

### 28. ¿Qué determina el RPO en una política de copias?

- a) La tecnología de recuperación que hay que emplear
- b) El número de emplazamientos alternativos necesarios
- c) La frecuencia con que hay que realizar las copias

**Respuesta correcta:** c) · **Referencia:** §3.1.1 [ISO22301] [NIST-SP800-34]

El RPO expresa cuántos datos, medidos en tiempo, se acepta perder; si es de 4 horas, no puede copiarse una sola vez al día.

### 29. Un servicio tiene un RTO de 15 minutos. ¿Qué solución es coherente?

- a) Disponer de una réplica encendible en el emplazamiento alternativo
- b) Realizar una copia completa diaria en cinta y custodiarla fuera del edificio
- c) Ampliar la retención de las copias diarias a 30 días

**Respuesta correcta:** a) · **Referencia:** §3.1.1 [NIST-SP800-34]

El RTO determina la tecnología de recuperación: restaurar volúmenes grandes desde cinta se mide en horas, no en minutos. La retención no influye en el tiempo de recuperación.

### 30. ¿Qué significa MTD (o MTPD) en la planificación de la continuidad?

- a) El tiempo medio de reparación de un componente averiado
- b) El tiempo máximo que el servicio puede estar interrumpido antes de que el daño sea inasumible
- c) El intervalo disponible para ejecutar la copia sin degradar el servicio

**Respuesta correcta:** b) · **Referencia:** §3.1.1 [ISO22301]

El RTO debe fijarse siempre por debajo del MTD. El tiempo medio de reparación es el MTTR y el intervalo de ejecución es la ventana de copia.

### 31. ¿En qué consiste la regla 3-2-1?

- a) Tres copias de los datos, en dos soportes distintos, con una fuera de la ubicación
- b) Tres copias diarias, dos semanales y una mensual
- c) Tres emplazamientos, dos redes y un único administrador responsable

**Respuesta correcta:** a) · **Referencia:** §3.1.2 [ISO27002] [NIST-SP800-209]

Las tres copias incluyen el propio original más dos copias adicionales; su extensión 3-2-1-1-0 añade una copia inmutable o fuera de línea y cero errores de verificación.

### 32. ¿Qué añade la regla 3-2-1-1-0 respecto de la clásica 3-2-1?

- a) Una copia adicional en la misma cabina y un informe mensual
- b) Un servidor de copia adicional y cero agentes instalados
- c) Una copia inmutable o fuera de línea y la exigencia de cero errores tras la verificación

**Respuesta correcta:** c) · **Referencia:** §3.1.2 [NIST-SP800-209]

El añadido responde al ransomware moderno, que busca y cifra primero las copias y el catálogo para impedir la recuperación.

### 33. ¿Cumple la regla 3-2-1 una copia guardada en la misma cabina que aloja los datos originales?

- a) Sí, siempre que se guarde en un pool distinto del original
- b) No, porque comparte el fallo de la cabina, el incendio de la sala y el alcance de un atacante
- c) Sí, siempre que la copia esté cifrada

**Respuesta correcta:** b) · **Referencia:** §3.1.2 [ISO27002]

La independencia respecto del original es justamente lo que distingue una copia de seguridad de una instantánea.

### 34. En el esquema de retención GFS, ¿qué representa el nivel «abuelo»?

- a) La copia mensual, conservada típicamente durante doce meses
- b) La copia diaria, conservada entre siete y catorce días
- c) La copia inmutable custodiada por un tercero

**Respuesta correcta:** a) · **Referencia:** §3.1.2 [ISO27002]

El «hijo» es la copia diaria, el «padre» la semanal y el «abuelo» la mensual, con vigencia creciente; por encima suele añadirse una copia anual.

### 35. ¿Por qué la retención de las copias no puede ser indefinida cuando contienen datos personales?

- a) Porque el software de copia no admite retenciones superiores a un año
- b) Porque el catálogo perdería la referencia de las copias antiguas
- c) Porque el artículo 5.1.e del RGPD impone la limitación del plazo de conservación

**Respuesta correcta:** c) · **Referencia:** §3.1.2 [RGPD] [NIST-SP800-88]

La retención debe estar justificada y documentada, y su vencimiento debe ejecutarse con destrucción segura del soporte.

### 36. Una copia incremental guarda…

- a) Todo lo que ha cambiado desde la última copia completa
- b) Todo lo que ha cambiado desde la copia anterior, sea del tipo que sea
- c) Todos los datos seleccionados, con independencia de si han cambiado

**Respuesta correcta:** b) · **Referencia:** §3.2.1 [NIST-SP800-34]

Es la más rápida y la que menos ocupa, pero la restauración exige la completa y toda la cadena de incrementales posteriores en orden.

### 37. Se hace copia completa el domingo y diferenciales de lunes a sábado. ¿Cuántas piezas hacen falta para restaurar el estado del jueves?

- a) Cinco: la completa y las cuatro diferenciales
- b) Una: solo la diferencial del jueves
- c) Dos: la completa del domingo y la diferencial del jueves

**Respuesta correcta:** c) · **Referencia:** §3.2.1 [NIST-SP800-34]

La diferencial acumula todos los cambios desde la última completa, de modo que basta con la última. Con incrementales harían falta cinco piezas encadenadas.

### 38. ¿Qué es una copia completa sintética?

- a) Una completa que el software fabrica en el repositorio combinando la completa anterior con los incrementales, sin leer el sistema de origen
- b) Una completa que se realiza con el servicio detenido para garantizar la consistencia
- c) Una completa cifrada y firmada digitalmente antes de enviarla a la nube

**Respuesta correcta:** a) · **Referencia:** §3.2.1 [VEEAM-DOC]

Es la base del modelo incremental para siempre: no consume ventana ni carga la producción y deja un punto de restauración de una sola pieza.

### 39. ¿Qué técnica ofrece el RPO más bajo posible?

- a) La copia diferencial cada seis horas
- b) La protección continua de datos (CDP), que registra cada escritura según se produce
- c) La copia completa sintética diaria

**Respuesta correcta:** b) · **Referencia:** §3.2.1 [NIST-SP800-34]

Permite volver a prácticamente cualquier instante, con un RPO de segundos, a costa de un consumo de recursos considerablemente mayor.

### 40. ¿Qué nivel de consistencia obtiene una copia realizada sin coordinación alguna con la aplicación?

- a) Consistente con la aplicación
- b) Consistente con el sistema de ficheros
- c) Consistente con el bloque (crash-consistent), equivalente a haber desenchufado el servidor

**Respuesta correcta:** c) · **Referencia:** §4.1 [MS-VSS] [VMW-VADP]

Los bloques están, pero puede faltar lo que había en memoria, de modo que la base de datos restaurada podría necesitar recuperación o no abrir.

### 41. ¿Qué caracteriza a una copia inmutable con bloqueo de objetos en modo de cumplimiento?

- a) Que solo puede leerla el usuario que la creó
- b) Que no puede modificarse ni borrarse por nadie, ni siquiera por la cuenta administradora, hasta que expire la retención
- c) Que se guarda automáticamente en un soporte extraíble

**Respuesta correcta:** b) · **Referencia:** §3.2.2 [S3-LOCK]

En el modo de gobernanza, en cambio, un usuario con un permiso especial sí puede levantar la retención antes de tiempo.

### 42. ¿Cuál es la ventaja distintiva de la cinta LTO como soporte de copia?

- a) Que un cartucho extraído de la biblioteca queda físicamente inalcanzable por la red, con coste por terabyte mínimo
- b) Que ofrece la restauración más rápida de todos los soportes
- c) Que permite modificar los datos ya escritos sin reescribir el cartucho

**Respuesta correcta:** a) · **Referencia:** §3.2.2 [LTO]

Su acceso es secuencial, por lo que la restauración es lenta; existen además cartuchos WORM que impiden por hardware la reescritura.

### 43. ¿Qué diferencia hay entre una copia inmutable y una copia fuera de línea?

- a) Ninguna: son dos nombres del mismo mecanismo
- b) La inmutable se guarda en cinta y la fuera de línea, en disco
- c) La inmutable está conectada pero no puede modificarse durante la retención; la fuera de línea es inalcanzable porque no existe camino hasta ella

**Respuesta correcta:** c) · **Referencia:** §3.2.2 [S3-LOCK] [NIST-SP800-209]

Ambas persiguen el mismo fin: que un atacante con credenciales de administrador no pueda destruir la copia.

### 44. ¿Cuál es la pieza más crítica de la arquitectura de una solución de copias de seguridad?

- a) El agente instalado en cada sistema de origen
- b) El catálogo del servidor de control, que indexa qué hay en cada copia
- c) La consola gráfica de administración

**Respuesta correcta:** b) · **Referencia:** §3.3.1 [NIST-SP800-34]

Sin catálogo la restauración granular es casi imposible, por lo que debe copiarse aparte y todo plan de recuperación debe contemplar su reconstrucción como primer paso.

### 45. ¿Para qué sirve el protocolo NDMP?

- a) Para copiar una cabina NAS enviando sus datos directamente al destino sin pasar por un servidor intermedio
- b) Para cifrar el tráfico entre el agente y el servidor de copia
- c) Para deduplicar los bloques en el cliente antes de enviarlos

**Respuesta correcta:** a) · **Referencia:** §3.3.1 [NDMP]

Preserva además los atributos y permisos propios del sistema de ficheros de la cabina.

### 46. ¿Cuál es la única verificación que mide el RTO real de un servicio?

- a) La comprobación de que el trabajo de copia ha terminado sin errores
- b) El cálculo de la suma de verificación de los bloques escritos
- c) La prueba de restauración real, documentada y cronometrada

**Respuesta correcta:** c) · **Referencia:** §3.3.2 [ENS] [RGPD]

Que un trabajo termine «con éxito» no significa que la copia sirva; el ENS exige probar el plan y el RGPD, en su artículo 32.1.d, la verificación regular de la eficacia.

### 47. ¿Qué relación hay entre el plan de recuperación ante desastres (DRP) y el plan de continuidad del negocio (BCP)?

- a) El DRP es la parte TIC del BCP, que es más amplio y abarca personas, sedes, procesos y proveedores
- b) Son sinónimos y la norma emplea ambos términos indistintamente
- c) El BCP es la parte técnica y el DRP el documento de gestión

**Respuesta correcta:** a) · **Referencia:** §3.3.2 [ISO27031] [NIST-SP800-34]

Su articulación se describe en la norma ISO/IEC 27031 y en la guía NIST SP 800-34.

### 48. Un emplazamiento alternativo que dispone de espacio, energía y comunicaciones, pero sin equipos ni datos, se denomina…

- a) Emplazamiento caliente (hot site)
- b) Emplazamiento frío (cold site)
- c) Emplazamiento templado (warm site)

**Respuesta correcta:** b) · **Referencia:** §3.3.2 [NIST-SP800-34]

Su activación se mide en días o semanas y su coste es bajo; el templado tiene el equipamiento instalado y datos parcialmente actualizados, y el caliente permite conmutar en minutos u horas.

### 49. En Windows, ¿qué papel desempeña el Servicio de instantáneas de volumen (VSS)?

- a) Deduplicar los bloques del volumen antes de enviarlos al repositorio
- b) Cifrar la copia en tránsito hacia el servidor de control
- c) Coordinar solicitante, escritores y proveedor para lograr una copia consistente con la aplicación

**Respuesta correcta:** c) · **Referencia:** §4.1 [MS-VSS]

Los escritores —SQL Server, Exchange, Active Directory— vacían sus búferes y congelan sus escrituras unos segundos mientras se crea la instantánea.

### 50. ¿Qué requisitos exige una recuperación bare-metal sobre hardware distinto del original?

- a) Una copia de imagen o volumen, un soporte de arranque de rescate y la inyección de controladores de almacenamiento y red
- b) Una copia de ficheros y la reinstalación previa del sistema operativo
- c) Una réplica síncrona del volumen y un sistema de ficheros de clúster

**Respuesta correcta:** a) · **Referencia:** §4.1.1 [NIST-SP800-34]

Sin esos controladores el sistema restaurado no arranca; restaurar una copia de ficheros sobre un equipo vacío no reconstruye un sistema arrancable.

### 51. En la copia sin agente de una máquina virtual, ¿de dónde obtiene los datos el software de copia?

- a) De un agente ligero instalado temporalmente en el sistema invitado
- b) Del registro de transacciones de la aplicación
- c) Del hipervisor, a través de su API de protección de datos, leyendo los discos virtuales

**Respuesta correcta:** c) · **Referencia:** §4.2.1 [VMW-VADP] [HYPERV-RCT]

En vSphere ese conjunto de interfaces se conoce como VADP; en Hyper-V se apoya en los escritores VSS del anfitrión y en RCT.

### 52. ¿Qué modo de transporte de la copia sin agente lee directamente el LUN de la cabina sin cargar la red IP?

- a) NBDSSL
- b) SAN, también llamado LAN-free
- c) HotAdd

**Respuesta correcta:** b) · **Referencia:** §4.2.1 [VMW-VADP]

Exige un proxy con acceso a la red de almacenamiento. HotAdd conecta en caliente los discos al proxy virtual y NBD/NBDSSL usa la red de gestión del anfitrión, más lenta pero siempre disponible.

### 53. Una instantánea de máquina virtual mantenida durante meses provoca principalmente…

- a) Crecimiento incontrolado del fichero delta, degradación del rendimiento y una consolidación muy costosa
- b) La pérdida del seguimiento de bloques modificados del hipervisor
- c) La imposibilidad de migrar la máquina virtual entre anfitriones

**Respuesta correcta:** a) · **Referencia:** §4.2.2 [VMW-SNAP]

El delta puede llegar a llenar el almacén de datos, y cada lectura debe recorrer la cadena de instantáneas encadenadas.

### 54. ¿Por qué una instantánea no es una copia de seguridad?

- a) Porque no captura el estado de la memoria de la máquina virtual
- b) Porque vive en el mismo almacén que el dato original y depende de él
- c) Porque no puede crearse con la máquina encendida

**Respuesta correcta:** b) · **Referencia:** §4.2.2 [VMW-SNAP] [ISO27002]

Si se pierde o se corrompe el almacén de datos, se pierden ambos; la copia de seguridad, en cambio, es independiente y reside en otro sitio.

### 55. ¿Qué aporta el seguimiento de bloques modificados (CBT) a la copia de una máquina virtual?

- a) Cifra los bloques antes de enviarlos al repositorio
- b) Garantiza la consistencia de la base de datos alojada en la máquina virtual
- c) Permite que el incremental lea solo los bloques cambiados, sin recorrer todo el disco virtual

**Respuesta correcta:** c) · **Referencia:** §4.2.2 [VMW-VADP] [HYPERV-RCT]

Es una función del hipervisor —RCT en Hyper-V—, reduce drásticamente la ventana de copia y hace viable el modelo incremental para siempre.

### 56. ¿Cuál es la diferencia esencial entre replicar una máquina virtual y hacer su copia de seguridad?

- a) La réplica está lista para arrancar en el destino, mientras que la copia hay que restaurarla antes de poder usarla
- b) La réplica conserva más puntos de restauración históricos que la copia
- c) La réplica protege mejor frente a la corrupción lógica y el ransomware

**Respuesta correcta:** a) · **Referencia:** §4.2.3 [NIST-SP800-34]

Precisamente por eso la réplica da un RTO de minutos, pero guarda pocos puntos en el tiempo y replica la corrupción casi al instante: ambas son complementarias.

### 57. ¿En qué consiste la restauración instantánea (instant recovery) de una máquina virtual?

- a) En restaurar únicamente los ficheros seleccionados por el usuario
- b) En arrancar la máquina directamente desde el repositorio de copias mientras sus datos se migran en segundo plano
- c) En conmutar el servicio a la réplica del emplazamiento alternativo

**Respuesta correcta:** b) · **Referencia:** §4.2.3 [VEEAM-DOC]

El servicio vuelve en minutos aunque la restauración completa tarde horas; es la técnica que más ha reducido el RTO en la última década.

### 58. ¿Qué artículo del Real Decreto 311/2022 (ENS) establece que los sistemas dispondrán de copias de seguridad y de mecanismos que garanticen la continuidad de las operaciones?

- a) El artículo 26, sobre continuidad de la actividad
- b) El artículo 5, sobre categorización de los sistemas
- c) El artículo 44, sobre auditoría de la seguridad

**Respuesta correcta:** a) · **Referencia:** §5.1.1 [ENS]

Ese mandato se desarrolla en el Anexo II mediante la medida mp.info.6, de copias de seguridad, y el grupo op.cont, de continuidad del servicio.

### 59. Según el ENS, ¿qué nivel de protección debe aplicarse a las copias de seguridad?

- a) Un nivel inferior al de los datos originales, por tratarse de información ya consolidada
- b) Únicamente la protección física del soporte donde residen
- c) El mismo nivel de seguridad que a los datos originales, en control de acceso, cifrado y protección física

**Respuesta correcta:** c) · **Referencia:** §5.1.1 [ENS] [CCN-STIC]

Es la exigencia menos intuitiva y la más incumplida: una copia mal custodiada es una fuga de datos esperando a ocurrir.

### 60. Un ciudadano ejerce su derecho de supresión y los datos figuran también en las copias de seguridad. ¿Cuál es la actuación correcta?

- a) Restaurar cada copia, borrar el dato y volver a generar la copia
- b) Suprimir el dato en producción, bloquear el tratamiento en las copias y volver a aplicar la supresión si alguna se restaura
- c) Destruir de inmediato todas las copias que contengan ese dato

**Respuesta correcta:** b) · **Referencia:** §5.2.1 [RGPD] [LOPDGDD] [AEPD]

Editar una copia consolidada es inviable y destruiría su integridad; la supresión efectiva llega cuando la copia vence conforme a la política de retención.

## Preguntas sobre los casos prácticos

### Caso 1. Diseño del almacenamiento para el nuevo CPD municipal

#### 1. Para la base de datos del Padrón, con escritura intensa y latencia mínima, ¿qué modo de acceso conviene?

- a) Por bloque: el motor pone su propio sistema de ficheros y modifica bloques parcialmente.
- b) Por fichero: la cabina NAS gestiona el sistema de ficheros y los bloqueos del motor.
- c) Por objeto: cada registro del Padrón se guarda como un objeto con metadatos ricos.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §1.1.3

El acceso por bloque ofrece la latencia más baja y permite la modificación parcial; el objeto no la permite y su latencia es la de una petición HTTP.

#### 2. ¿Qué modo de acceso conviene a las carpetas departamentales de los 1.200 empleados?

- a) Por bloque, con un LUN por departamento que cada puesto formatea con su propio sistema de ficheros.
- b) Por fichero, porque los usuarios comparten carpetas con permisos y bloqueos gestionados por la cabina.
- c) Por objeto, porque el espacio de nombres plano facilita los permisos por unidad administrativa.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §1.1.2

Lo que se comparte son ficheros entre muchos usuarios concurrentes; un LUN no se comparte entre cientos de puestos.

#### 3. Los documentos de expedientes finalizados se escriben una vez, se consultan poco y se conservan muchos años con sus metadatos. ¿Qué modo de acceso les conviene?

- a) Por bloque, porque su latencia mínima acelera las consultas ocasionales al archivo.
- b) Por fichero, porque solo un árbol de directorios conserva los metadatos del expediente.
- c) Por objeto, que admite metadatos ricos y encaja con el versionado y la inmutabilidad.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §1.1.3

El terreno del almacenamiento de objetos es el dato que se escribe una vez y se lee poco, con metadatos definibles por el usuario y retención WORM.

#### 4. Las carpetas departamentales están en un entorno Windows con autenticación de dominio. ¿Qué protocolo procede?

- a) iSCSI, sobre el puerto 3260, con autenticación CHAP entre la cabina y los puestos.
- b) SMB 3.x, sobre el puerto 445, integrado con Kerberos y las ACL del dominio.
- c) NFS v3, sin estado, apoyado en mountd y lockd para gestionar los bloqueos.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §1.2.1

SMB es el protocolo de fichero del mundo Windows; NFS se usaría en un entorno Unix e iSCSI es de bloque.

#### 5. ¿Qué protocolo de acceso es adecuado para el Padrón y para los discos de las máquinas virtuales?

- a) Fibre Channel, o iSCSI sobre una red segregada de 10/25 Gbit/s si el presupuesto lo aconseja.
- b) SMB 3.x con multichannel, porque reparte el tráfico de la base de datos entre varias tarjetas.
- c) HTTPS con la API de S3, porque el acceso REST reduce la latencia de las escrituras.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §1.2.1

Las dos cargas necesitan acceso de bloque de baja latencia; NVMe-oF sería la opción si se busca la latencia mínima.

#### 6. ¿Qué nivel RAID conviene al Padrón, con escritura intensa?

- a) RAID 5, porque desperdicia menos disco y su paridad distribuida acelera las escrituras.
- b) RAID 6, porque la doble paridad reduce la penalización de escritura respecto a RAID 10.
- c) RAID 10, porque cada escritura cuesta dos operaciones físicas, frente a cuatro en RAID 5 y seis en RAID 6.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §1.2.2

Con mucha escritura importa la penalización: RAID 10 la tiene mínima, aunque solo aproveche la mitad de la capacidad.

#### 7. ¿Qué esquema de protección conviene al archivo electrónico, de lectura dominante y discos de gran capacidad?

- a) RAID 0, porque los documentos se leen poco y basta con repartirlos en bandas entre todos los discos del grupo.
- b) RAID 10, porque su espejo es el único nivel que tolera el fallo simultáneo de dos discos cualesquiera.
- c) RAID 6 o codificación de borrado, porque prima la capacidad y RAID 5 es arriesgado al reconstruir discos grandes.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §1.2.2

Con discos de decenas de terabytes la reconstrucción dura horas o días y un segundo fallo destruiría un RAID 5; RAID 6 tolera dos.

#### 8. ¿Qué modelo de virtualización permite migrar los datos de la cabina antigua a la nueva, de otro fabricante, sin detener el servicio?

- a) La virtualización basada en red (o la de cabina externa desde la nueva), que migra los bloques en segundo plano.
- b) La virtualización basada en host con LVM, que comparte un mismo pool entre todos los servidores.
- c) La virtualización basada en la cabina antigua, que exporta sus instantáneas a la nueva cabina.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §2.1.1

El modelo de red unifica cabinas heterogéneas y permite la migración sin parada; la abstracción de host no se comparte entre servidores.

#### 9. ¿Cuál es el inconveniente característico de ese modelo de virtualización?

- a) Que exige instalar software específico en cada servidor para localizar sus bloques.
- b) Que, al operar en banda, añade latencia y es un punto crítico que hay que desplegar en pareja.
- c) Que consume CPU de cada servidor y multiplica los puntos de administración.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §2.1.1

Todas las lecturas y escrituras pasan por el dispositivo intermedio: su caída dejaría sin datos a todos los servidores.

#### 10. ¿Qué dos técnicas ahorrarán más espacio en los discos de las 120 máquinas virtuales y qué riesgo operativo introducen?

- a) Deduplicación y thin provisioning; si el pool se llena de verdad, todos los volúmenes fallan a la vez.
- b) Instantáneas de cabina y cifrado en reposo; las instantáneas dependen del volumen original.
- c) RAID 5 y compresión; cada escritura exige cuatro operaciones físicas en la cabina.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §1.2.2

La misma imagen base da ratios de deduplicación de 5:1 a 20:1, y el aprovisionamiento fino sobreaprovisiona: exige alertas y vigilancia del llenado real.

### Caso 2. Política de copias, RTO/RPO y ventana de respaldo

#### 1. Con la copia completa diaria a las 02:00 y una restauración que tarda unas 3 horas, ¿cuáles son el RPO y el RTO reales del Padrón?

- a) RPO de 3 horas y RTO de hasta 24 horas.
- b) RPO de hasta 24 horas y RTO de al menos 3 horas.
- c) RPO de 15 minutos y RTO de 1 hora, porque la copia es completa.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §3.1.1

El RPO mide los datos perdidos desde la última copia (hasta un día) y el RTO el tiempo de vuelta al servicio (la restauración de 3 horas).

#### 2. ¿Qué corrección permite cumplir el RPO de 15 minutos del Padrón?

- a) Adelantar la copia completa diaria a las 00:00.
- b) Sustituir la copia completa diaria por una diferencial diaria.
- c) Añadir una copia del registro de transacciones cada 15 minutos.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §3.1.1

El RPO fija la frecuencia: copiar el registro cada 15 minutos permite además recuperar la base de datos hasta un instante concreto.

#### 3. ¿Y qué corrección permite cumplir el RTO de 1 hora?

- a) Una réplica de la base de datos en el segundo emplazamiento, o una restauración instantánea.
- b) Copiar el registro de transacciones con más frecuencia, porque acelera la restauración.
- c) Ampliar la retención de las copias de 14 a 30 días en el mismo repositorio.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §3.1.1

El RTO se corrige cambiando la tecnología de recuperación: copiar más a menudo no acelera ni un minuto la restauración.

#### 4. ¿Caben los 20 TB en la ventana de 8 horas con una red de 10 Gbit/s?

- a) No cabe: a 10 Gbit/s solo se transfieren unos 3,6 TB en 8 horas, aun con eficiencia plena.
- b) Cabe con holgura: 10 Gbit/s equivalen a 10 GB/s, unos 288 TB en la ventana nocturna.
- c) Cabe muy justo (≈ 21,6 TB con un 60 % de eficiencia) y solo si origen y destino sostienen ese caudal.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §3.1.2

10 Gbit/s ≈ 1,25 GB/s; al 60 %, 0,75 GB/s × 28.800 s ≈ 21,6 TB. En la práctica la limitación suele ser la lectura del origen, no la red.

#### 5. ¿Qué medida resuelve el problema de la ventana de forma sostenible?

- a) Copiar desde el sistema en marcha en lugar de desde instantáneas, para no ocupar espacio en la cabina.
- b) Pasar a completa semanal e incrementales diarios, o a incremental para siempre con completas sintéticas.
- c) Duplicar la retención para no tener que repetir la copia completa cada noche.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §3.1.2

Los incrementales mueven solo el 2-5 % diario; las completas sintéticas se fabrican en el repositorio sin leer de nuevo el origen.

#### 6. Respecto de la regla 3-2-1, ¿qué incumple la política actual de copias?

- a) Hay solo dos copias (original y repositorio) y ninguna está fuera de la ubicación.
- b) Solo la verificación, porque el original y el repositorio ya suman las tres copias exigidas.
- c) Nada, porque el repositorio de copias es un equipo distinto de la cabina de producción.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §3.1.2

La regla exige tres copias (el original y dos más) y una fuera de la ubicación; un repositorio en la misma sala comparte el incendio o la inundación.

#### 7. El repositorio de copias está integrado en el dominio corporativo con las mismas credenciales de administración. ¿Por qué es grave?

- a) Porque impide cifrar las copias en tránsito entre el repositorio y la cabina.
- b) Porque un atacante que comprometa el directorio podría destruir también las copias.
- c) Porque obliga a restaurar con la cuenta del responsable del servicio afectado.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §3.1.2

Una copia conectada con credenciales del mismo dominio no cumple la copia inmutable o desconectada; procede usar credenciales separadas y MFA en la consola.

#### 8. ¿Qué diseño de destinos satisface la regla 3-2-1-1-0 en el CPD municipal?

- a) Dos repositorios de disco en la misma sala, ambos con las credenciales del dominio corporativo.
- b) Instantáneas de la cabina como segunda copia y RAID 6 en la cabina como tercera copia.
- c) Repositorio local deduplicado, réplica al segundo CPD y copia inmutable WORM en objetos más cinta LTO extraída.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §3.1.2

Da tres copias, dos soportes, una fuera, una inmutable o fuera de línea; las instantáneas y el RAID no son copias de seguridad.

#### 9. ¿Qué exige la normativa respecto de las pruebas de restauración?

- a) El ENS (verificar copias y, en categoría ALTA, probar el plan) y el RGPD (art. 32.1.d, verificación regular).
- b) Nada con carácter obligatorio: son una recomendación de las guías CCN-STIC sin rango normativo.
- c) Solo el RGPD, en su artículo 5.1.e, que obliga a restaurar cada copia antes de destruirla.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §3.3.2 · art. 32.1.d RGPD

La prueba de restauración es una obligación jurídica, no una buena práctica opcional.

#### 10. ¿Qué límite legal tiene el esquema de retención escalonada (GFS) que se proponga?

- a) Ninguno: el artículo 17 de la Ley 39/2015 permite conservar las copias de seguridad de forma indefinida, sin plazo.
- b) El artículo 32.1.c del RGPD, que fija una retención máxima de 14 días para las copias diarias del repositorio.
- c) La limitación del plazo de conservación del artículo 5.1.e del RGPD: retención justificada y destrucción segura al vencer.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §3.1.2 · art. 5.1.e RGPD

Las copias con datos personales no pueden guardarse «para siempre por si acaso»; el archivo electrónico de la Ley 39/2015 es otra función.

### Caso 3. Recuperación ante un incidente de ransomware

#### 1. ¿Por qué la réplica de las máquinas virtuales al segundo CPD no sirvió frente al ransomware?

- a) Porque solo copia la configuración de las máquinas virtuales y no sus discos.
- b) Porque el segundo CPD no tenía la categoría ALTA del Esquema Nacional de Seguridad.
- c) Porque mantiene una copia fiel y actualizada y replicó el cifrado casi al instante.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §4.2.3

La réplica reduce el RTO ante el desastre del emplazamiento, pero no protege frente a la corrupción del contenido ni conserva estados anteriores.

#### 2. En este incidente, ¿qué mecanismo conserva estados anteriores y resiste a un atacante con credenciales de administrador?

- a) La copia de seguridad inmutable o fuera de línea.
- b) La instantánea de la máquina virtual en su almacén de datos.
- c) La réplica síncrona al segundo emplazamiento.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §3.2.2

Solo la copia da profundidad histórica, y solo la inmutable o desconectada resiste a quien tiene credenciales de administrador.

#### 3. ¿Cuál debe ser la primera actuación de la recuperación?

- a) Restaurar el gestor de expedientes, por ser el servicio de mayor criticidad del CPD.
- b) Contener el incidente (aislar la red, detener la propagación, preservar evidencias) y declarar el desastre.
- c) Notificar a la AEPD antes de tocar ninguno de los sistemas afectados por el cifrado.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §3.3.2

Antes de restaurar hay que detener la propagación y declarar el desastre conforme al DRP.

#### 4. ¿Cuál es la primera tarea técnica ineludible de la reconstrucción?

- a) Reconstruir el servidor de copia y su catálogo, sin el cual no hay restauración granular.
- b) Restaurar el servidor de ficheros departamental, por ser el más usado por los empleados.
- c) Encender la réplica del segundo CPD para recuperar el servicio en minutos.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §3.3.1

El catálogo sabe qué hay en cada copia: todo DRP debe prever reconstruirlo antes de restaurar nada más.

#### 5. ¿Sobre qué sistemas deben restaurarse los servicios?

- a) Sobre los mismos servidores cifrados, una vez eliminados los ficheros cifrados.
- b) Sobre la réplica del segundo CPD, que ya tiene las máquinas virtuales configuradas.
- c) Sobre sistemas reconstruidos desde cero y parcheados, nunca sobre los comprometidos.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §3.3.2

Los servicios se restauran por orden de criticidad conforme a sus RTO, y se validan antes de reabrirlos.

#### 6. El forense sitúa la primera actividad anómala nueve días antes del cifrado. ¿Desde qué punto debe restaurarse?

- a) Desde la copia más reciente de la copia inmutable, la del día anterior al cifrado.
- b) Desde un punto anterior a la primera actividad anómala, es decir, de más de nueve días atrás.
- c) Desde la réplica del segundo CPD, tras descifrar sus bloques con las claves de la copia.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §3.1.2

Las copias posteriores a la intrusión pueden contener ya las herramientas del atacante o datos comprometidos.

#### 7. ¿Qué consecuencia tiene ese punto de restauración sobre la retención mínima de la política?

- a) Hay que reducir la retención a siete días, para que las copias no conserven el código del atacante.
- b) Retención escalonada de semanas y meses, y copia inmutable más larga que la permanencia oculta del atacante.
- c) Hay que conservar todas las copias de forma indefinida, sin plazo de destrucción.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §3.1.2

Una retención de pocos días habría dejado a la organización sin ningún punto limpio; es la justificación práctica de la retención larga (GFS).

#### 8. Entre los datos cifrados hay datos personales de ciudadanos. ¿Qué obligación impone el RGPD?

- a) Notificar la violación de seguridad a la AEPD en 72 horas desde que se tuvo constancia (art. 33).
- b) Ninguna, porque una pérdida de disponibilidad sin divulgación no es una violación de seguridad.
- c) Notificarla a la AEPD en el plazo de un mes, una vez concluida la restauración (art. 32).

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §5.2.1 · art. 33 RGPD

La violación de seguridad abarca la destrucción, pérdida o alteración, no solo la divulgación; una pérdida de disponibilidad también es una brecha.

#### 9. ¿Cuándo hay que comunicar además el incidente a los ciudadanos afectados?

- a) Siempre, en las mismas 72 horas, con independencia del riesgo para sus derechos.
- b) Cuando el riesgo para sus derechos y libertades sea alto (art. 34 RGPD).
- c) Nunca, si existe una copia inmutable que permita recuperar los datos.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §5.2.1 · art. 34 RGPD

La comunicación a los interesados depende de que el riesgo para sus derechos y libertades sea alto.

#### 10. ¿Qué medida del ENS exige que las copias no puedan alterarse ni destruirse de forma no autorizada y que se autorice y registre cada restauración?

- a) La medida [op.cont.1] Análisis de impacto.
- b) La medida [op.ext] de servicios prestados por terceros.
- c) La medida [mp.info.6] Copias de seguridad.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §5.1.1

La medida [mp.info.6], que despliega el artículo 26 del RD 311/2022, incluye la protección de las copias y el registro de las restauraciones.
