# Simulacro práctico. Plataforma de cita previa y renovación de las Oficinas de Atención a la Ciudadanía

Supuesto y 30 preguntas tipo test, con el formato de la parte práctica del examen (Grupo II).

## Supuesto

Las Oficinas de Atención a la Ciudadanía del Ayuntamiento atienden cada día a miles de personas que acuden a realizar trámites presenciales, como el empadronamiento o la obtención de certificados, en su mayoría con cita previa. El sistema actual de citas está obsoleto, y la red, los puestos de trabajo y la conexión de las oficinas con el centro de proceso de datos municipal han llegado al final de su vida útil.

El Ayuntamiento quiere desarrollar una nueva plataforma de cita previa multicanal, accesible desde la web municipal, desde una aplicación móvil y mediante videoatención, con un gestor de turnos en cada oficina (quioscos que imprimen el tique, pantallas de llamada y tabletas para el personal). La plataforma se apoyará en una base de datos relacional y se desplegará en el centro de proceso de datos virtualizado, con parte de los servicios en la nube. Al mismo tiempo se renovarán el cableado, la red inalámbrica y los puestos de las oficinas, que pasarán a ser escritorios virtuales, y la conexión de cada sede con el centro de proceso de datos.

Se plantean, a continuación, una serie de cuestiones prácticas sobre el diseño, la implantación y la explotación del nuevo sistema.

## Preguntas

### 1. La base de datos de la plataforma almacenará los apellidos de la ciudadanía codificados en UTF-8. ¿Cuántos bytes ocupará el apellido «Muñoz»?

- a) 5 bytes.
- b) 6 bytes.
- c) 10 bytes.

**Respuesta correcta:** b) · **Referencia:** Tema 11, §9.3

En UTF-8 los caracteres US-ASCII ocupan 1 byte y los del rango U+0080-U+07FF, como la «ñ» (U+00F1), ocupan 2: 1 + 1 + 2 + 1 + 1 = 6 bytes.

### 2. El gestor de turnos llamará a la ciudadanía por orden de llegada, pero las personas con discapacidad o de edad avanzada deben ser atendidas antes que otras que ya estaban esperando. ¿Qué estructura de datos modela este comportamiento?

- a) Una pila (LIFO), que atiende primero al último en llegar.
- b) Una cola FIFO simple, que respeta el orden de llegada.
- c) Una cola de prioridad, implementada con un montículo.

**Respuesta correcta:** c) · **Referencia:** Tema 13, §2.4

En una cola de prioridad se desencola siempre el elemento de mayor prioridad, no el más antiguo; se implementa eficientemente con un montículo (heap).

### 3. Los quioscos de autoservicio de las oficinas entregarán un tique impreso con el número de turno. ¿Qué tecnología de impresión es la habitual para este uso?

- a) Térmica, que aplica calor sobre papel termosensible.
- b) Matricial, que imprime por impacto sobre una cinta entintada.
- c) Láser, que fija el tóner sobre el papel por fusión.

**Respuesta correcta:** a) · **Referencia:** Tema 12, §4.1

La impresión térmica aplica calor sobre papel termosensible y es la propia de tiques y etiquetas; la láser se usa para documentos y la matricial, para copias por presión.

### 4. En el modelo de datos, una CITA puede incluir varios TRÁMITES y un mismo TRÁMITE puede figurar en muchas citas. Al pasar este diseño al modelo relacional, ¿cómo se representa esa relación?

- a) Propagando la clave de TRÁMITE como clave ajena en la tabla CITA.
- b) Con una tabla intermedia cuya clave combina las de CITA y TRÁMITE.
- c) Propagando la clave de CITA como clave ajena en la tabla TRÁMITE.

**Respuesta correcta:** b) · **Referencia:** Tema 16, §3.4

Una relación N:M se transforma en una tabla intermedia cuya clave primaria es la combinación de las claves de ambas entidades; propagar una clave ajena es la regla de las relaciones 1:N y 1:1.

### 5. Un analista propone la tabla CITA(id_cita, fecha, hora, cod_oficina, direccion_oficina), con id_cita como clave primaria y valores atómicos en todas sus columnas. ¿Qué forma normal incumple?

- a) La primera (1FN), porque contiene grupos repetitivos.
- b) La segunda (2FN), porque hay dependencias parciales de la clave.
- c) La tercera (3FN), porque direccion_oficina depende de cod_oficina.

**Respuesta correcta:** c) · **Referencia:** Tema 17, §4.5

Con clave simple y valores atómicos la tabla ya está en 2FN; direccion_oficina depende de la clave a través de cod_oficina, un atributo no clave, y esa dependencia transitiva viola la 3FN.

### 6. En las pruebas, dos ciudadanos reservan a la vez el último hueco libre de una oficina: ambas transacciones leen que está libre, lo asignan a su solicitante y confirman. Al final el hueco solo figura a nombre del segundo, aunque el primero recibió confirmación. ¿Qué anomalía de concurrencia se ha producido?

- a) Actualización perdida.
- b) Lectura sucia.
- c) Lectura fantasma.

**Respuesta correcta:** a) · **Referencia:** Tema 15, §2.2

Hay actualización perdida cuando dos transacciones actualizan el mismo dato y una sobrescribe a la otra; la lectura sucia exige leer datos no confirmados y la fantasma, filas nuevas insertadas por otra transacción.

### 7. Se necesita una consulta que devuelva, para el último mes, las oficinas que han atendido más de 500 citas. Tras agrupar por oficina con GROUP BY, ¿en qué cláusula debe expresarse la condición COUNT(*) > 500?

- a) En HAVING, que filtra los grupos ya agregados.
- b) En WHERE, que filtra las filas antes de agrupar.
- c) En ORDER BY, que se evalúa después de SELECT.

**Respuesta correcta:** a) · **Referencia:** Tema 19, §2.4

WHERE filtra filas individuales antes de que existan los grupos y no admite funciones de agregación; una condición sobre un total agregado por grupo va en HAVING.

### 8. Un módulo estadístico calcula el tiempo medio de espera con la instrucción real media = total_minutos / num_citas, donde ambas variables son enteras y valen 7 y 2. En un lenguaje con división entera, ¿qué valor queda en media?

- a) 3,5
- b) 3,0
- c) 4,0

**Respuesta correcta:** b) · **Referencia:** Tema 18, §2.4

La división se evalúa primero entre enteros (7 / 2 = 3, se pierde el decimal) y solo después se convierte a real; para obtener 3,5 hay que convertir antes de dividir.

### 9. Los avisos por SMS se enviarán mediante un servicio heredado cuya interfaz no coincide con la que espera el módulo de notificaciones de la nueva plataforma. Se quiere que ambos colaboren sin modificar ninguno de los dos. ¿Qué patrón de diseño procede?

- a) Singleton.
- b) Observer.
- c) Adapter.

**Respuesta correcta:** c) · **Referencia:** Tema 20, §4.4

Adapter convierte la interfaz de una clase existente en otra que el cliente espera y permite colaborar a clases incompatibles; Observer resuelve la notificación uno a muchos y Singleton, la instancia única.

### 10. Antes de la puesta en producción se quiere comprobar si, con una carga moderada mantenida durante 48 horas, aparecen fugas de memoria o se agota progresivamente el pool de conexiones JDBC. ¿Qué tipo de prueba debe planificarse con JMeter?

- a) Una prueba de estrés, que busca el punto de ruptura.
- b) Una prueba de carga, con el pico de tráfico previsto.
- c) Una prueba de resistencia (soak), con carga sostenida.

**Respuesta correcta:** c) · **Referencia:** Tema 21, §3.3

La prueba de resistencia aplica una carga moderada sostenida durante un periodo largo para detectar problemas que solo aparecen con el tiempo, como fugas de memoria o el agotamiento del pool de conexiones.

### 11. La aplicación móvil reintenta automáticamente las peticiones que fallan por pérdida de cobertura. ¿Cuál de estas peticiones a la API REST de la plataforma no es seguro reintentar, porque podría crear dos citas?

- a) POST /citas
- b) PUT /citas/4711
- c) DELETE /citas/4711

**Respuesta correcta:** a) · **Referencia:** Tema 22, §6.6

GET, PUT y DELETE son idempotentes; POST no lo es, porque repetirlo crea, en general, un recurso distinto cada vez. Reintentar solo es seguro con verbos idempotentes.

### 12. En las pruebas de la web, un usuario autenticado cambia en la URL el identificador de su cita (/citas/1001 por /citas/1002) y consigue ver los datos de otra persona. ¿Qué vulnerabilidad pone de manifiesto?

- a) Secuencia de comandos en sitios cruzados (XSS) reflejada.
- b) Control de acceso roto, en su variante IDOR.
- c) Falsificación de petición en sitios cruzados (CSRF).

**Respuesta correcta:** b) · **Referencia:** Tema 23, §10.2.1

La aplicación no verifica en el servidor que el usuario tenga permiso sobre el recurso concreto que pide; cambiar el identificador en la URL para acceder al de otro ciudadano es la variante IDOR del control de acceso roto.

### 13. En las pruebas de la aplicación en Android, si el usuario gira el móvil mientras rellena el formulario de solicitud de cita, se borra lo que había escrito. ¿Cuál es la causa más probable?

- a) Girar la pantalla destruye y recrea la Activity, y su estado no se ha guardado.
- b) El sistema ha revocado a la aplicación un permiso concedido en tiempo de ejecución.
- c) El sistema ha detenido el Service en segundo plano por falta de memoria.

**Respuesta correcta:** a) · **Referencia:** Tema 24, §2.1.1

En Android, girar la pantalla destruye y recrea la Activity por defecto; si el estado no se guarda en onSaveInstanceState() o en un ViewModel, se pierde lo que el usuario había escrito.

### 14. El diseño gráfico propone, para el texto normal de la web de cita previa, un gris claro sobre fondo blanco con una relación de contraste de 3:1. ¿Cumple el nivel AA de las WCAG?

- a) Sí, porque 3:1 es el mínimo de nivel AA para cualquier texto.
- b) No, porque el texto normal exige al menos 4,5:1.
- c) Sí, porque el contraste mínimo solo se exige en el nivel AAA.

**Respuesta correcta:** b) · **Referencia:** Tema 25, §2.1

El criterio 1.4.3, de nivel AA, exige un contraste mínimo de 4,5:1 para el texto normal y de 3:1 solo para el texto grande.

### 15. Se decide desplegar los servidores de aplicaciones de la plataforma en un servicio en la nube de tipo IaaS. ¿A quién corresponde administrar y parchear el sistema operativo de esas máquinas virtuales?

- a) Al proveedor, porque gestiona el hipervisor y el hardware.
- b) Al proveedor, siempre que el contrato le exija cumplir el ENS.
- c) Al Ayuntamiento, como cliente del servicio.

**Respuesta correcta:** c) · **Referencia:** Tema 31, §3

Entre IaaS y PaaS la frontera es el sistema operativo: en IaaS lo administra el cliente, y el proveedor solo aporta la virtualización, los servidores, el almacenamiento y la red.

### 16. Los puestos de las oficinas pasan a ser escritorios virtuales (VDI). Cada mañana, al abrir al público, todos los empleados inician sesión a la vez y durante varios minutos los escritorios responden con gran lentitud, con un pico de E/S en el almacenamiento. ¿Cómo se denomina este fenómeno?

- a) Tormenta de arranque o de inicio de sesión.
- b) Ruido del vecino entre inquilinos de la nube.
- c) Agotamiento del almacenamiento con aprovisionamiento fino.

**Respuesta correcta:** a) · **Referencia:** Tema 28, §3.1.1

La tormenta de arranque (boot storm) y su variante de inicio de sesión (login storm) se producen cuando cientos de escritorios arrancan y cargan perfiles a la vez, provocando un pico de E/S que el almacenamiento debe absorber.

### 17. La base de datos de citas se copia de forma completa el domingo y con copias diferenciales de lunes a sábado. Si hay que restaurarla al estado de la copia del jueves, ¿qué copias se necesitan?

- a) Solo la diferencial del jueves, que ya incluye todos los datos.
- b) La completa del domingo y las diferenciales de lunes a jueves.
- c) La completa del domingo y la diferencial del jueves.

**Respuesta correcta:** c) · **Referencia:** Tema 26, §3.2.1

La diferencial copia todo lo que ha cambiado desde la última completa, de modo que restaurar exige solo dos piezas: la última completa y la última diferencial.

### 18. El volumen lógico LVM que almacena los justificantes se ha quedado pequeño. El administrador ejecuta lvextend para ampliarlo, pero df sigue mostrando el tamaño antiguo. ¿Qué falta por hacer?

- a) Reiniciar el servidor para que el núcleo reconozca el nuevo tamaño.
- b) Ampliar también el sistema de archivos, por ejemplo con resize2fs.
- c) Ejecutar fsck sobre el volumen montado para que recalcule su tamaño.

**Respuesta correcta:** b) · **Referencia:** Tema 27, §2.2.1

Ampliar espacio en LVM son dos pasos: agrandar el volumen lógico (lvextend) y después el sistema de archivos que contiene (resize2fs en ext4, xfs_growfs en XFS). Además, fsck nunca se ejecuta sobre un sistema de archivos montado en lectura y escritura.

### 19. Las tabletas con las que el personal gestiona la cola en la sala de espera se administrarán con una plataforma MDM. Si una de ellas es sustraída, ¿qué actuación de la plataforma protege los datos que contiene?

- a) El borrado remoto del terminal desde la consola central.
- b) La revocación del permiso de cámara a la aplicación de turnos.
- c) La reinstalación de la aplicación desde la tienda oficial.

**Respuesta correcta:** a) · **Referencia:** Tema 14, §5.4

La plataforma MDM permite forzar el cifrado y el bloqueo, distribuir aplicaciones y borrar remotamente un terminal perdido o robado para proteger sus datos.

### 20. Una funcionaria de una oficina llama al CAU porque no consigue imprimir un justificante desde su escritorio. El técnico necesita ver exactamente lo que ella tiene en pantalla. ¿Qué debe hacer?

- a) Abrir una sesión RDP estándar contra el equipo de la funcionaria.
- b) Conectarse a través de la gestión fuera de banda (IPMI) del equipo.
- c) Usar una herramienta que comparta la sesión abierta de la usuaria.

**Respuesta correcta:** c) · **Referencia:** Tema 29, §1.3.3

Para asistir hay que compartir la sesión del usuario; RDP estándar abre una sesión independiente y el técnico vería un escritorio distinto del que el usuario tiene delante.

### 21. Tras la renovación del cableado, un puesto de mostrador conectado a una roseta situada a 115 metros de cable del armario presenta errores intermitentes de red. ¿Qué los explica?

- a) Que la roseta no es de Cat 8, la categoría de mayor alcance.
- b) Que se supera el límite de 100 metros del canal de cobre.
- c) Que el puerto del conmutador funciona en modo dúplex.

**Respuesta correcta:** b) · **Referencia:** Tema 33, §2.1.1

El canal de cobre Ethernet admite 100 m (90 m de cable fijo más 10 m de latiguillos) y superarlo produce errores intermitentes; la Cat 8, además, solo garantiza 30 m.

### 22. En la sala de espera de una oficina se instalarán tres puntos de acceso Wi-Fi contiguos que operarán en la banda de 2,4 GHz. ¿Qué asignación de canales evita el solapamiento entre ellos?

- a) Canales 1, 6 y 11.
- b) Canales 1, 2 y 3.
- c) Canales 3, 6 y 9.

**Respuesta correcta:** a) · **Referencia:** Tema 37, §2.3.2

En 2,4 GHz solo hay tres canales que no se solapan, el 1, el 6 y el 11, porque cada canal ocupa unos 20 MHz y los canales están separados solo 5 MHz.

### 23. Un puesto de mostrador recién instalado no accede a la aplicación de cita previa. El técnico comprueba que el equipo tiene la dirección IP 169.254.37.12. ¿Dónde está el problema?

- a) En la resolución de nombres: el servidor DNS no responde.
- b) En la asignación de dirección: no ha obtenido concesión DHCP.
- c) En el encaminamiento: la puerta de enlace no enruta entre VLAN.

**Respuesta correcta:** b) · **Referencia:** Tema 30, §1.2.2

Una dirección 169.254.x.x es de autoconfiguración y el equipo se la asigna cuando no encuentra servidor DHCP; el problema es de DHCP, no de DNS ni de encaminamiento.

### 24. Para la VLAN de puestos de una oficina con 100 equipos se quiere asignar, dentro del bloque privado 10.20.0.0/16, la subred más pequeña que los acoja. ¿Qué prefijo debe usarse?

- a) /26
- b) /24
- c) /25

**Respuesta correcta:** c) · **Referencia:** Tema 34, §6.1

Una /25 ofrece 2^7 − 2 = 126 direcciones de equipo; una /26 solo ofrece 62, y una /24 (254) también los acoge, pero no es la más pequeña.

### 25. Cada oficina debe quedar unida de forma permanente con el centro de proceso de datos a través de internet, sin instalar ningún software en los puestos. ¿Qué solución procede?

- a) Una VPN de sitio a sitio entre las pasarelas de ambos extremos, con IPsec.
- b) Una VPN de acceso remoto, con un cliente instalado en cada puesto.
- c) Publicar en internet las aplicaciones del centro de proceso de datos.

**Respuesta correcta:** a) · **Referencia:** Tema 36, §4.1.1

La VPN de sitio a sitio une dos redes completas mediante un túnel permanente entre pasarelas, normalmente IPsec en modo túnel con ESP; los equipos no instalan nada y ven la red remota como otra subred.

### 26. El servidor web público de cita previa se ubicará en la DMZ y necesita datos de la base de datos de la red interna. ¿Qué diseño respeta la regla que define una DMZ?

- a) Permitir que el servidor web abra sesiones directas contra la base de datos interna.
- b) Hacer que la conexión parta de la red interna o de un intermediario de la DMZ.
- c) Abrir desde la DMZ hacia la red interna los puertos que utilice la aplicación.

**Respuesta correcta:** b) · **Referencia:** Tema 36, §2.4.1

Desde la DMZ no se puede iniciar ninguna conexión hacia la red interna; si un servidor de la DMZ necesita un dato interno, la conexión debe originarse en la red interna o hacerse a través de un intermediario situado en la propia DMZ.

### 27. En horas punta, algunos ciudadanos reciben un error 504 al confirmar la cita; la respuesta la genera el balanceador situado delante de los servidores de aplicaciones. ¿Qué indica ese código?

- a) Que el servidor de origen devolvió al balanceador una respuesta no válida.
- b) Que el usuario está autenticado, pero no tiene permiso sobre el recurso.
- c) Que el servidor de origen no respondió a tiempo al balanceador.

**Respuesta correcta:** c) · **Referencia:** Tema 35, §4.2.1

El 504 indica que el servidor de origen no respondió a tiempo al intermediario; el 502 corresponde a una respuesta no válida del origen y el 403, a la falta de permiso.

### 28. Se quiere enviar a un ciudadano un documento cifrado de forma que solo él pueda abrirlo. Con criptografía asimétrica, ¿con qué clave debe cifrarse?

- a) Con la clave privada del Ayuntamiento.
- b) Con la clave pública del ciudadano.
- c) Con la clave privada del ciudadano.

**Respuesta correcta:** b) · **Referencia:** Tema 32, §5.1.1

Para la confidencialidad, el emisor cifra con la clave pública del receptor, y solo este puede descifrar con su clave privada; cifrar con la privada del emisor es firmar, no ocultar el contenido.

### 29. Los responsables valoran así las dimensiones de seguridad de la plataforma: confidencialidad MEDIO, disponibilidad MEDIO, integridad BAJO, autenticidad BAJO y trazabilidad BAJO. Según el ENS, ¿qué categoría le corresponde y cómo debe acreditarse su conformidad?

- a) Categoría BÁSICA, con autoevaluación y declaración de conformidad.
- b) Categoría MEDIA, con autoevaluación y declaración de conformidad.
- c) Categoría MEDIA, con auditoría y certificación de conformidad.

**Respuesta correcta:** c) · **Referencia:** Tema 39, §2.4.2 y §2.5.2

Manda la dimensión más alta: si alguna alcanza MEDIO y ninguna ALTO, la categoría es MEDIA. Los sistemas de categoría MEDIA o ALTA necesitan una auditoría para la certificación de su conformidad; la autoevaluación es solo para la BÁSICA.

### 30. La videoatención se basará en WebRTC. Cuando el equipo del ciudadano y el del empleado no logran conectarse directamente por estar tras dispositivos NAT restrictivos, ¿qué elemento retransmite el audio y el vídeo entre ambos?

- a) Un servidor TURN.
- b) Un servidor STUN.
- c) El algoritmo ICE.

**Respuesta correcta:** a) · **Referencia:** Tema 40, §2.2.2

STUN solo descubre la dirección pública y no lleva media; ICE prueba los candidatos y decide; TURN es el que retransmite el audio y el vídeo cuando no hay conexión directa.
