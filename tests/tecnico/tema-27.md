# Test del tema 27. Administración del sistema operativo y software de base

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-27.html>

## Batería de preguntas

### 1. ¿Qué se entiende por «software de base»?

- a) El conjunto de programas que hacen utilizable el hardware y proporcionan a las aplicaciones un entorno de ejecución homogéneo
- b) El software que resuelve directamente el problema funcional del usuario final
- c) Exclusivamente el núcleo del sistema operativo, sin controladores ni bibliotecas

**Respuesta correcta:** a) · **Referencia:** §1.1 [SILBERSCHATZ]

Incluye firmware, sistema operativo, controladores, bibliotecas del sistema, utilidades y, en sentido amplio, el middleware. No resuelve el problema del usuario: habilita a quien lo resuelve.

### 2. ¿Cuál es la única vía legítima para que una aplicación en modo usuario solicite un servicio del núcleo?

- a) El acceso directo a los registros del dispositivo
- b) La escritura en el sector de arranque del disco
- c) La llamada al sistema (<em>system call</em>), que provoca un cambio controlado a modo núcleo

**Respuesta correcta:** c) · **Referencia:** §1.1 [STALLINGS] [POSIX]

El hardware distingue modo privilegiado y modo usuario; una aplicación nunca toca el hardware directamente. Las llamadas tienen un coste, por lo que agrupar el trabajo rinde mejor que hacer millones de llamadas pequeñas.

### 3. En un núcleo monolítico:

- a) Solo permanecen en modo núcleo la planificación, la memoria básica y la comunicación entre procesos
- b) Todos los servicios del sistema (archivos, red, controladores) se ejecutan dentro del espacio del núcleo
- c) Cada servicio se ejecuta en una máquina virtual independiente

**Respuesta correcta:** b) · **Referencia:** §1.1.1 [TANENBAUM]

De ahí su ventaja (rendimiento: las llamadas entre subsistemas son llamadas a función) y su inconveniente (un fallo en un controlador puede tumbar el sistema entero).

### 4. ¿Cómo se clasifica el núcleo de Linux?

- a) Monolítico modular, con módulos cargables y descargables en caliente
- b) Micronúcleo puro, con los controladores en modo usuario
- c) Núcleo por capas estrictas, sin posibilidad de extensión en ejecución

**Respuesta correcta:** a) · **Referencia:** §1.1.1 [TANENBAUM]

Es un error frecuente confundir la modularidad con el micronúcleo: los módulos de Linux se cargan <strong>dentro</strong> del espacio del núcleo (<code>lsmod</code>, <code>modprobe</code>, <code>rmmod</code>). Micronúcleos puros son MINIX 3, QNX o L4.

### 5. ¿Qué permanece en el espacio del núcleo en una arquitectura de micronúcleo?

- a) Los sistemas de archivos y la pila de red completa
- b) Únicamente la planificación, la gestión básica de memoria y la comunicación entre procesos
- c) Todos los controladores de dispositivo, por razones de rendimiento

**Respuesta correcta:** b) · **Referencia:** §1.1.1 [TANENBAUM] [SILBERSCHATZ]

El resto —sistemas de archivos, pila de red, controladores— corre como procesos servidores en modo usuario que se comunican por paso de mensajes. Gana robustez y pierde rendimiento.

### 6. La partición del sistema EFI (ESP) que utiliza el arranque UEFI:

- a) Se ubica siempre en el sector 0 del disco, en formato MBR
- b) Debe estar cifrada obligatoriamente con la clave del TPM
- c) Está formateada en FAT32 y contiene los archivos <code>.efi</code> de arranque

**Respuesta correcta:** c) · **Referencia:** §1.2.1 [UEFI-SPEC]

UEFI sustituye a la BIOS heredada, trabaja con tabla de particiones GPT y localiza los cargadores como archivos dentro de la ESP, en lugar de leer un sector de arranque.

### 7. ¿Cuál es la función del Arranque Seguro (<em>Secure Boot</em>)?

- a) Verificar la firma digital de cada componente de la cadena de arranque antes de ejecutarlo
- b) Cifrar el contenido del disco duro para impedir su lectura si se extrae
- c) Realizar una copia de seguridad automática del sector de arranque en cada inicio

**Respuesta correcta:** a) · **Referencia:** §1.2.1 [UEFI-SPEC]

Impide que se cargue código no confiable —como un <em>rootkit</em>— antes que el sistema operativo. Un núcleo o un controlador sin firmar detiene el arranque, lo que a veces se manifiesta justo después de una actualización.

### 8. ¿Para qué sirve el <code>initramfs</code> (o <code>initrd</code>) en un sistema Linux?

- a) Para almacenar los registros del sistema durante el arranque
- b) Para aportar en memoria los controladores imprescindibles que permiten montar el sistema de archivos raíz real
- c) Para sustituir permanentemente al sistema de archivos raíz en sistemas sin disco

**Respuesta correcta:** b) · **Referencia:** §1.2.1 [RH-DOC] [GRUB-DOC]

Si el <code>initramfs</code> no incluye el controlador correcto —por ejemplo, el del RAID o el del cifrado—, el núcleo arranca pero no encuentra la raíz y se produce un <em>kernel panic</em>: avería clásica tras actualizar el núcleo.

### 9. ¿Cuál es la diferencia esencial entre un proceso y un hilo?

- a) El hilo puede ejecutarse en modo núcleo y el proceso no
- b) El proceso es siempre más rápido de crear que el hilo
- c) El proceso posee el espacio de direcciones y los recursos; el hilo es la unidad de planificación y comparte ese espacio

**Respuesta correcta:** c) · **Referencia:** §2.1 [SILBERSCHATZ]

Por eso cambiar de hilo dentro de un proceso es más barato que cambiar de proceso, y por eso un hilo que corrompe memoria puede afectar a todos sus hermanos.

### 10. Ante un servicio que no responde, ¿cuál es la secuencia correcta de terminación?

- a) Enviar primero <code>SIGTERM</code> y, solo si no responde, <code>SIGKILL</code>
- b) Enviar directamente <code>SIGKILL</code>, que es el método limpio
- c) Enviar <code>SIGKILL</code> y a continuación <code>SIGTERM</code> para confirmar

**Respuesta correcta:** a) · **Referencia:** §2.1 [MAN-PAGES]

<code>SIGTERM</code> (15) pide terminar y permite al proceso cerrar archivos y guardar estado; <code>SIGKILL</code> (9) lo mata sin que pueda capturarlo. Matar así un gestor de bases de datos puede exigir después una recuperación.

### 11. Un proceso «zombi» es aquel que:

- a) Consume el 100 % de la CPU sin realizar trabajo útil
- b) Ha terminado, pero su proceso padre no ha recogido su código de salida
- c) Está bloqueado en una operación de entrada/salida que no responde

**Respuesta correcta:** b) · **Referencia:** §2.1 [SILBERSCHATZ] [MAN-PAGES]

Ocupa una entrada en la tabla de procesos pero no consume CPU. La acumulación de zombis indica un programa padre mal escrito. El proceso cuyo padre muere antes que él es el «huérfano», adoptado por el PID 1.

### 12. Un servidor presenta CPU de usuario muy baja, porcentaje de espera de E/S muy alto y valores de intercambio (<code>si</code>/<code>so</code>) constantemente elevados. ¿Qué está ocurriendo?

- a) Un ataque de denegación de servicio sobre la interfaz de red
- b) Una saturación del procesador por exceso de hilos activos
- c) Hiperpaginación (<em>thrashing</em>): el sistema dedica más tiempo a intercambiar páginas que a trabajar

**Respuesta correcta:** c) · **Referencia:** §2.1 [SILBERSCHATZ]

La solución no es un disco más rápido, sino reducir el grado de multiprogramación o ampliar la memoria física. Ampliar el espacio de intercambio solo cambia el síntoma.

### 13. Un «fallo de página» (<em>page fault</em>) se produce cuando:

- a) El proceso accede a una página que no está presente en memoria física y el núcleo debe traerla
- b) La tabla de páginas se corrompe y hay que reiniciar el sistema
- c) Dos procesos intentan escribir simultáneamente en el mismo marco de página

**Respuesta correcta:** a) · **Referencia:** §2.1 [SILBERSCHATZ] [TANENBAUM]

Es un mecanismo normal de la memoria virtual, no un error: el núcleo trae la página, actualiza la tabla y reanuda la instrucción. El problema aparece cuando la tasa de fallos se dispara.

### 14. ¿Qué aporta el diario (<em>journaling</em>) de un sistema de archivos?

- a) Comprime los archivos poco usados para ahorrar espacio
- b) Permite recuperar la coherencia en segundos tras un corte, repitiendo o descartando las operaciones incompletas anotadas previamente
- c) Registra qué usuario ha accedido a cada archivo, a efectos de auditoría

**Respuesta correcta:** b) · **Referencia:** §2.2 [SILBERSCHATZ]

Un sistema sin diario, como FAT32, obliga a una comprobación completa del volumen y puede perder datos. La auditoría de accesos es cosa del registro de eventos, no del diario.

### 15. Se ha ejecutado <code>lvextend</code> para ampliar un volumen lógico, pero <code>df -h</code> sigue mostrando el tamaño anterior. ¿Qué falta?

- a) Reiniciar el servidor para que el núcleo relea la tabla de particiones
- b) Volver a crear el grupo de volúmenes desde cero
- c) Ampliar el sistema de archivos que reside dentro del volumen (<code>resize2fs</code>, <code>xfs_growfs</code>)

**Respuesta correcta:** c) · **Referencia:** §2.2.1 [LVM-DOC] [RH-DOC]

Ampliar en LVM son dos pasos: primero el volumen lógico y después el sistema de archivos. Ninguno de los dos exige reiniciar: ambos pueden hacerse en caliente.

### 16. En un sistema de cuotas de disco, el límite blando (<em>soft</em>):

- a) Puede superarse temporalmente durante un periodo de gracia, con avisos al usuario
- b) Impide cualquier escritura en el momento en que se alcanza
- c) Se aplica solo a los administradores del sistema

**Respuesta correcta:** a) · **Referencia:** §2.2.1 [MAN-PAGES] [ENS]

El que impide la escritura sin excepción es el límite duro (<em>hard</em>). Las cuotas evitan que un solo usuario o proceso agote un volumen compartido y provoque una caída, que es una incidencia de disponibilidad.

### 17. En Windows, si se elimina una cuenta de usuario y se vuelve a crear con el mismo nombre:

- a) Conserva todos sus permisos, porque las ACL guardan el nombre de la cuenta
- b) Pierde todos sus permisos, porque se genera un SID nuevo y las ACL guardan el SID, no el nombre
- c) Conserva los permisos solo si se recrea en la misma unidad organizativa

**Respuesta correcta:** b) · **Referencia:** §3.1 [MS-AD]

Por eso <strong>renombrar</strong> una cuenta es seguro (conserva el SID) y <strong>borrarla y recrearla</strong> no lo es. Es un error clásico en la gestión de altas y bajas.

### 18. En una lista de control de acceso (ACL) de Windows, si un usuario tiene concedido el permiso de lectura por pertenecer a un grupo y denegado explícitamente ese mismo permiso por otra entrada:

- a) Prevalece el permiso concedido, por ser más específico
- b) El sistema solicita al administrador que resuelva el conflicto
- c) Prevalece la denegación explícita y el acceso se rechaza

**Respuesta correcta:** c) · **Referencia:** §3.1 [MS-AD]

Es la regla básica de evaluación de ACL: la denegación explícita gana sobre el permiso. Los permisos, además, se heredan del contenedor padre salvo que se rompa expresamente la herencia.

### 19. El orden de precedencia en la aplicación de las directivas de grupo (GPO) es:

- a) Local, Sitio, Dominio y Unidad organizativa, prevaleciendo la última aplicada
- b) Unidad organizativa, Dominio, Sitio y Local, prevaleciendo la primera aplicada
- c) Alfabético por nombre de la directiva, sin relación con la estructura del directorio

**Respuesta correcta:** a) · **Referencia:** §3.1 [MS-GPO]

Es la regla conocida como LSDUO (o LSDOU): gana la directiva más cercana al objeto, salvo bloqueos de herencia o directivas marcadas como obligatorias.

### 20. Dentro del modelo AAA, ¿a qué pregunta responde la autorización?

- a) ¿Quién eres?
- b) ¿Qué hiciste?
- c) ¿Qué puedes hacer?

**Respuesta correcta:** c) · **Referencia:** §3.1.1 [ENS]

La autenticación responde a «¿quién eres?» y la auditoría o trazabilidad, a «¿qué hiciste?». Son tres funciones distintas y consecutivas, y las tres son exigibles en el Esquema Nacional de Seguridad.

### 21. ¿Cuál de estas combinaciones constituye una autenticación multifactor?

- a) Contraseña más pregunta de seguridad
- b) Contraseña más código generado por una aplicación en el teléfono
- c) Contraseña más repetición de la contraseña en un segundo campo

**Respuesta correcta:** b) · **Referencia:** §3.1.1 [ISO27002] [ENS]

Combina «algo que sabes» con «algo que tienes», es decir, factores de <strong>categorías distintas</strong>. Contraseña y pregunta de seguridad son ambos «algo que sabes», por lo que no constituyen multifactor.

### 22. El modelo de control de acceso basado en roles (RBAC) se caracteriza porque:

- a) Los permisos se asignan a roles y las personas se adscriben a esos roles
- b) El propietario de cada recurso decide discrecionalmente quién accede
- c) La política la impone el sistema mediante etiquetas de seguridad inalterables por el usuario

**Respuesta correcta:** a) · **Referencia:** §3.1.1 [SILBERSCHATZ]

Es el modelo recomendado en organizaciones grandes porque el alta y la baja se reducen a añadir o retirar el rol. La opción B describe el modelo discrecional (DAC) y la C, el obligatorio (MAC).

### 23. ¿Qué diferencia hay entre <code>systemctl start apache2</code> y <code>systemctl enable apache2</code>?

- a) Ninguna: son sinónimos en systemd
- b) <code>start</code> habilita el arranque automático y <code>enable</code> lo arranca en ese momento
- c) <code>start</code> lo arranca en ese momento y <code>enable</code> lo habilita para el próximo inicio del sistema

**Respuesta correcta:** c) · **Referencia:** §3.2 [SYSTEMD] [MS-WINSERVER]

Son operaciones independientes: <code>enable --now</code> hace ambas. El equivalente conceptual en Windows es la diferencia entre el <strong>estado</strong> del servicio y su <strong>tipo de inicio</strong>.

### 24. ¿Qué significa la línea de <code>cron</code> siguiente: <code>30 2 <em> </em> 1</code>?

- a) Cada 30 minutos durante las dos primeras horas del día 1 de cada mes
- b) Los lunes a las 02:30
- c) El día 30 de febrero, a la hora 1 (entrada inválida)

**Respuesta correcta:** b) · **Referencia:** §3.2 [MAN-PAGES]

Los cinco campos son, en este orden: minuto, hora, día del mes, mes y día de la semana (0-7, con 0 y 7 = domingo). Aquí: minuto 30, hora 2, cualquier día del mes, cualquier mes, día de la semana 1 (lunes).

### 25. ¿Cuál es la medida del anexo II del ENS que exige mantener un inventario actualizado de todos los elementos del sistema y se aplica en las tres categorías?

- a) <code>op.exp.1</code> — Inventario de activos
- b) <code>mp.info.6</code> — Copias de seguridad
- c) <code>op.cont.2</code> — Plan de continuidad

**Respuesta correcta:** a) · **Referencia:** §4.1 [ENS]

Es la medida fundacional: sin inventario no puede haber análisis de riesgos, ni gestión de parches, ni recuperación fiable. Se aplica en categoría BÁSICA, MEDIA y ALTA sin excepción.

### 26. Reiniciar un servicio caído para devolver el servicio al usuario y, días después, investigar por qué se caía cada martes, corresponde respectivamente a:

- a) Gestión de cambios y gestión de configuración
- b) Gestión de problemas y gestión de incidencias
- c) Gestión de incidencias y gestión de problemas

**Respuesta correcta:** c) · **Referencia:** §4.1 [ITIL] [ISO20000]

La incidencia busca <strong>restablecer</strong> el servicio cuanto antes, aunque sea con una solución temporal; el problema busca eliminar la <strong>causa subyacente</strong>. Son objetivos distintos y sucesivos.

### 27. Un sistema tiene la dimensión de disponibilidad valorada en nivel ALTO y todas las demás en nivel BAJO. ¿Cuál es su categoría según el ENS?

- a) BÁSICA, porque predominan las dimensiones de nivel bajo
- b) ALTA, porque basta con que una dimensión alcance el nivel ALTO
- c) MEDIA, como resultado de promediar los niveles de las cinco dimensiones

**Respuesta correcta:** b) · **Referencia:** §4.2.1 [ENS]

La categoría no se promedia: manda la dimensión más alta. Es MEDIA cuando alguna alcanza el nivel MEDIO y ninguna lo supera, y BÁSICA cuando alguna alcanza el nivel BAJO y ninguna lo supera.

### 28. ¿Cuáles son las cinco dimensiones de seguridad del anexo I del ENS?

- a) Disponibilidad, integridad, confidencialidad, autenticidad y trazabilidad
- b) Disponibilidad, integridad, confidencialidad, interoperabilidad y accesibilidad
- c) Confidencialidad, integridad, disponibilidad, eficiencia y economía

**Respuesta correcta:** a) · **Referencia:** §4.2.1 [ENS]

Mnemotécnica: D-I-C-A-T. La interoperabilidad y la accesibilidad son exigencias reales, pero pertenecen al Esquema Nacional de Interoperabilidad y a la normativa de accesibilidad, no a las dimensiones del ENS.

### 29. Respecto a la diferenciación de responsabilidades del artículo 11 del ENS, es cierto que:

- a) El responsable del sistema y el responsable de la seguridad deben ser necesariamente la misma persona
- b) Solo se exige designar un responsable de la seguridad, y los demás papeles son opcionales
- c) La responsabilidad de la seguridad debe estar diferenciada de la responsabilidad sobre la explotación del sistema

**Respuesta correcta:** c) · **Referencia:** §4.2.1 [ENS]

El ENS distingue cuatro papeles: responsable de la información, del servicio, de la seguridad y del sistema. Quien administra no puede ser, a la vez, quien decide y supervisa si esa administración es segura.

### 30. Sobre la auditoría de la seguridad prevista en el ENS:

- a) Debe realizarse mensualmente en todos los sistemas, con independencia de su categoría
- b) Es una auditoría regular ordinaria al menos cada dos años, y extraordinaria ante modificaciones sustanciales; los sistemas de categoría BÁSICA requieren autoevaluación
- c) Solo se realiza cuando se produce un incidente de seguridad con impacto acreditado

**Respuesta correcta:** b) · **Referencia:** §4.2.1 [ENS]

La auditoría extraordinaria, además, reinicia el cómputo del plazo de dos años para la siguiente ordinaria.

### 31. El artículo 21 del ENS, «Integridad y actualización del sistema», exige:

- a) Autorización formal previa para incluir o modificar cualquier elemento físico o lógico del catálogo de activos, y evaluación y monitorización permanentes
- b) Que todas las actualizaciones se apliquen automáticamente en el plazo de 24 horas desde su publicación
- c) Que el sistema se reinstale íntegramente cada doce meses

**Respuesta correcta:** a) · **Referencia:** §4.2.1 [ENS]

La monitorización permanente permite adecuar el estado de seguridad atendiendo a deficiencias de configuración, vulnerabilidades identificadas y actualizaciones que afecten al sistema.

### 32. ¿Qué exige el artículo 32 del RGPD en relación con las copias de seguridad?

- a) Que las copias se conserven exactamente durante cinco años
- b) Que las copias se almacenen siempre fuera del territorio de la Unión Europea
- c) La capacidad de restaurar la disponibilidad y el acceso a los datos personales de forma rápida tras un incidente, y la verificación regular de la eficacia de las medidas

**Respuesta correcta:** c) · **Referencia:** §4.2 [RGPD]

Es decir: copiar <strong>y</strong> probar la restauración no es una buena práctica opcional, sino una obligación legal.

### 33. Sustituir un disco cuyo recuento de sectores reasignados está creciendo, antes de que llegue a fallar, es un ejemplo de mantenimiento:

- a) Correctivo, porque el disco presenta un defecto
- b) Preventivo, porque actúa sobre un fallo latente antes de que se manifieste
- c) Adaptativo, porque adapta el sistema a un hardware nuevo

**Respuesta correcta:** b) · **Referencia:** §5.1 [ISO14764] [SMART-DOC]

El criterio que separa los tipos de mantenimiento es el momento y la causa: el correctivo es reactivo (ya ha fallado) y el preventivo, proactivo. Guiado por telemetría S.M.A.R.T., se denomina además predictivo.

### 34. El mantenimiento «evolutivo» del enunciado oficial se corresponde, en la norma ISO/IEC 14764, con:

- a) El mantenimiento perfectivo más el adaptativo
- b) El mantenimiento correctivo más el preventivo
- c) Únicamente el mantenimiento correctivo de emergencia

**Respuesta correcta:** a) · **Referencia:** §5.1 [ISO14764]

El perfectivo mejora rendimiento o mantenibilidad sin corregir ningún fallo; el adaptativo acomoda cambios del entorno (nueva versión soportada, hardware nuevo, cambio normativo). Ninguno responde a un fallo ya producido.

### 35. Respecto al mantenimiento de una unidad de estado sólido (SSD):

- a) Debe desfragmentarse semanalmente para mantener el rendimiento
- b) No debe desfragmentarse: la operación adecuada es TRIM u optimización
- c) Debe formatearse a bajo nivel cada seis meses

**Respuesta correcta:** b) · **Referencia:** §5.1 [MS-PERF]

Desfragmentar una SSD no mejora nada y consume ciclos de escritura, acortando su vida. TRIM informa al dispositivo de qué bloques ya no contienen datos válidos.

### 36. ¿Qué es una «línea base» (<em>baseline</em>) en monitorización de sistemas?

- a) El valor máximo que un contador puede alcanzar antes de generar una alarma
- b) El límite contractual de disponibilidad fijado en el acuerdo de nivel de servicio
- c) La medición del comportamiento normal del sistema con la que se comparan las mediciones posteriores

**Respuesta correcta:** c) · **Referencia:** §5.2 [MS-PERF]

Sin línea base, afirmar que un servidor «va lento» no es verificable. Conviene rehacerla tras cada cambio importante y desglosarla por franja horaria y día de la semana.

### 37. Una disponibilidad comprometida del 99,9 % anual equivale aproximadamente a una caída máxima de:

- a) Unas 8 horas y 46 minutos al año
- b) Unos 5 minutos al año
- c) Unos 3 días y 15 horas al año

**Respuesta correcta:** a) · **Referencia:** §5.2 [ISO20000]

Los «cinco nueves» (99,999 %) equivalen a unos 5 minutos anuales y el 99 % («dos nueves»), a unos 3 días y 15 horas. Las paradas planificadas y comunicadas suelen quedar excluidas del cómputo.

### 38. Los indicadores MTBF y MTTR miden, respectivamente:

- a) El coste medio de un fallo y el coste medio de una reparación
- b) El tiempo medio entre fallos (fiabilidad) y el tiempo medio de reparación (capacidad de recuperación)
- c) El número medio de incidencias por usuario y por servicio

**Respuesta correcta:** b) · **Referencia:** §5.2 [ISO20000]

La disponibilidad puede expresarse como MTBF ÷ (MTBF + MTTR): se mejora espaciando los fallos o reparando más rápido, y lo segundo suele ser más barato.

### 39. Al dimensionar un sistema en la gestión de capacidad, lo correcto es:

- a) Tomar el valor mínimo registrado, para no sobredimensionar la inversión
- b) Tomar la media aritmética del uso diario a lo largo del año
- c) Tomar un percentil alto de la carga (por ejemplo, el percentil 95) y considerar los picos previsibles del calendario

**Respuesta correcta:** c) · **Referencia:** §5.2 [ISO20000]

La media oculta los picos, y son los picos los que tiran el servicio: apertura de plazos, campañas de tributos o convocatorias de empleo público.

### 40. Un servidor Linux muestra muy poca memoria «libre» pero mucha memoria «disponible». La interpretación correcta es:

- a) Es normal y deseable: el sistema usa la memoria sobrante como caché de disco y la cede cuando hace falta
- b) El servidor está a punto de agotar la memoria y hay que reiniciarlo
- c) Hay una fuga de memoria en el núcleo que exige actualizarlo

**Respuesta correcta:** a) · **Referencia:** §5.2.1 [MAN-PAGES]

La métrica que hay que vigilar es la memoria <strong>disponible</strong> y, sobre todo, la tasa de intercambio (<code>si</code>/<code>so</code>), no la memoria «libre».

### 41. Mantener en producción un sistema operativo que ha alcanzado su fin de vida (EOL) implica:

- a) Un ahorro admisible siempre que el sistema no esté publicado en Internet
- b) Que las nuevas vulnerabilidades descubiertas quedarán sin corregir, lo que en el sector público supone un incumplimiento del ENS
- c) Que el fabricante sigue publicando parches de seguridad, aunque no funcionales

**Respuesta correcta:** b) · **Referencia:** §6.1 [ENS]

Si es inevitable convivir con él temporalmente, hay que documentar la excepción con su análisis de riesgo, medidas compensatorias (aislamiento, restricción de accesos, vigilancia reforzada) y fecha límite de migración.

### 42. En versionado semántico, el paso de la versión 4.2.7 a la 5.0.0 indica:

- a) Una simple corrección de errores, sin riesgo apreciable
- b) Funcionalidad nueva compatible con la versión anterior
- c) Cambios incompatibles con la versión anterior, que exigen pruebas completas antes de producción

**Respuesta correcta:** c) · **Referencia:** §6.1 [SEMVER]

En <code>MAYOR.MENOR.PARCHE</code>, el incremento de la cifra mayor anuncia ruptura de compatibilidad; el de la menor, funcionalidad compatible; y el del parche, corrección de errores.

### 43. ¿Qué diferencia hay entre CVE y CVSS?

- a) CVE es el identificador único y público de una vulnerabilidad; CVSS es la puntuación de su gravedad
- b) CVE es la puntuación de gravedad; CVSS es el catálogo de fabricantes afectados
- c) Son dos nombres del mismo sistema, según se use en Europa o en Estados Unidos

**Respuesta correcta:** a) · **Referencia:** §6.1 [CVE] [NIST-CVSS]

Regla mnemotécnica: <strong>CVE identifica, CVSS puntúa</strong>. La prioridad real de parcheo combina la puntuación con la exposición del activo, su criticidad y la existencia de explotación activa.

### 44. En la escala CVSS, una vulnerabilidad se considera de gravedad CRÍTICA cuando su puntuación se sitúa entre:

- a) 7,0 y 8,9
- b) 9,0 y 10,0
- c) 4,0 y 6,9

**Respuesta correcta:** b) · **Referencia:** §6.1 [NIST-CVSS]

Las bandas son: baja (0,1-3,9), media (4,0-6,9), alta (7,0-8,9) y crítica (9,0-10,0). La puntuación ordena la prioridad, pero no la determina por sí sola.

### 45. Ante una vulnerabilidad de día cero (<em>zero-day</em>) que afecta a un servicio publicado, la actuación correcta es:

- a) Esperar sin actuar hasta que el fabricante publique el parche oficial
- b) Apagar definitivamente el servicio y no volver a prestarlo
- c) Aplicar mitigaciones temporales —deshabilitar la función afectada, filtrar accesos, reforzar la vigilancia— y documentarlas hasta que exista parche

**Respuesta correcta:** c) · **Referencia:** §6.1 [NIST80040]

Un día cero es una vulnerabilidad conocida y explotada sin corrección disponible: no actuar equivale a aceptar el riesgo sin medida compensatoria alguna.

### 46. ¿Cuál es el primer paso del proceso de gestión de parches según la metodología del NIST?

- a) Inventariar los activos y el software instalado
- b) Desplegar el parche en el entorno de producción crítica
- c) Redactar el informe de cumplimiento para la auditoría

**Respuesta correcta:** a) · **Referencia:** §6.2 [NIST80040] [ENS]

Sin inventario no se sabe qué hay que parchear. La secuencia completa es: inventariar, identificar, priorizar, probar, desplegar y verificar y documentar.

### 47. El despliegue de actualizaciones «por anillos» consiste en:

- a) Aplicar el parche simultáneamente en todo el parque para reducir la ventana de exposición
- b) Aplicarlo en oleadas sucesivas —laboratorio, piloto, producción no crítica y producción crítica— con verificación entre etapas
- c) Instalar el parche solo en las máquinas que el usuario solicite expresamente

**Respuesta correcta:** b) · **Referencia:** §6.2 [NIST80040] [MS-WSUS]

El anillo piloto debe ser <strong>representativo</strong> del parque: si deja fuera un modelo de equipo o un software departamental, el fallo aparecerá en el despliegue masivo.

### 48. El refuerzo R2 de la medida <code>op.exp.4</code> del ENS exige que, antes de aplicar configuraciones, parches y actualizaciones de seguridad:

- a) Se comunique la intervención al Centro Criptológico Nacional
- b) Se obtenga la conformidad expresa de todos los usuarios afectados
- c) Se prevea un mecanismo para revertirlos en caso de aparición de efectos adversos

**Respuesta correcta:** c) · **Referencia:** §6.2.1 [ENS]

Es la formulación normativa de la regla de oro del parcheo: no se aplica en producción un cambio que no se sepa deshacer. El refuerzo R1 de la misma medida exige la prueba previa en un entorno equivalente al de producción.

### 49. En el protocolo syslog, ¿qué relación hay entre el número de severidad y la gravedad del mensaje?

- a) Cuanto menor es el número, más grave es el mensaje: 0 es «emergencia» y 7 es «depuración»
- b) Cuanto mayor es el número, más grave es el mensaje: 7 es «emergencia» y 0 es «depuración»
- c) El número indica el subsistema emisor y no guarda relación con la gravedad

**Respuesta correcta:** a) · **Referencia:** §7.1 [RFC5424]

El subsistema emisor lo indica la <strong>facilidad</strong> (<code>auth</code>, <code>cron</code>, <code>kern</code>…), no la severidad. Filtrar «severidad 3 o inferior» significa quedarse con los errores y todo lo más grave.

### 50. ¿Por qué es imprescindible la sincronización horaria (NTP) en la gestión de registros?

- a) Porque los registros solo se escriben en horario laboral
- b) Porque el protocolo syslog rechaza mensajes con marca de tiempo
- c) Porque sin una hora común entre sistemas no es posible correlacionar los eventos de varias máquinas

**Respuesta correcta:** c) · **Referencia:** §7.1 [RFC5905] [NIST80092]

Un reloj desincronizado, además, provoca fallos de autenticación en protocolos que dependen de marcas de tiempo y resta valor probatorio a los registros.

### 51. ¿Cuál es la razón principal para centralizar los registros en un servidor distinto del auditado?

- a) Reducir el consumo de disco del servidor de aplicaciones
- b) Impedir que quien comprometa una máquina pueda borrar las huellas de su actividad
- c) Cumplir el requisito de interoperabilidad del ENI en materia de formatos

**Respuesta correcta:** b) · **Referencia:** §7.1 [NIST80092] [ENS]

Es una medida de seguridad, no de ahorro: el atacante que obtiene privilegios en un sistema intenta borrar sus registros, y no debe poder hacerlo en el repositorio central.

### 52. Ante una incidencia que ha dejado sin servicio a la sede electrónica, el orden de actuación correcto es:

- a) Contener y restablecer el servicio primero, y analizar la causa raíz después
- b) Analizar exhaustivamente la causa raíz antes de tocar nada, para no perder información
- c) Notificar a los medios de comunicación antes de intervenir técnicamente

**Respuesta correcta:** a) · **Referencia:** §7.2 [ITIL] [NIST80061]

Restablecer y averiguar la causa son objetivos distintos y sucesivos. Quedarse depurando con el servicio caído es el error típico. La preservación de evidencias, cuando hay sospecha de incidente de seguridad, se compatibiliza aislando el sistema en lugar de apagarlo precipitadamente.

### 53. Varios servicios de un servidor fallan de forma aparentemente aleatoria, no se puede iniciar sesión gráfica y la base de datos ha pasado a solo lectura. La primera comprobación debe ser:

- a) Reinstalar el sistema operativo desde la imagen corporativa
- b) Sustituir la tarjeta de red por si estuviera defectuosa
- c) El espacio libre en disco y en inodos de los sistemas de archivos

**Respuesta correcta:** c) · **Referencia:** §7.2 [MAN-PAGES]

El disco lleno es la causa número uno de incidencias «misteriosas», y <code>df -h</code> junto con <code>df -i</code> la resuelven en segundos. Un sistema de archivos puede además quedarse sin inodos aun teniendo espacio libre.

### 54. Las fases de la gestión de incidentes de seguridad según el NIST son:

- a) Detección, facturación, sustitución y archivo
- b) Preparación; detección y análisis; contención, erradicación y recuperación; y lecciones aprendidas
- c) Auditoría, sanción, publicación y cierre

**Respuesta correcta:** b) · **Referencia:** §7.2 [NIST80061] [ENS]

A ello se añade, en el sector público, la notificación del incidente conforme al procedimiento del ENS y, si hay datos personales comprometidos, la notificación de la brecha conforme al RGPD.

### 55. En un equipo Windows con el almacén de componentes dañado, el orden correcto de reparación es:

- a) Ejecutar <code>DISM /RestoreHealth</code> para reparar el almacén y después <code>sfc /scannow</code> para reparar los archivos del sistema
- b) Ejecutar <code>sfc /scannow</code> primero y <code>DISM</code> solo si el equipo no arranca
- c) Formatear la partición del sistema, porque no hay reparación posible

**Respuesta correcta:** a) · **Referencia:** §8.1 [MS-WINRE]

<code>sfc</code> toma los archivos de reemplazo del almacén de componentes: si ese almacén está corrupto, <code>sfc</code> no puede reparar nada. De ahí el orden.

### 56. Respecto a la utilidad <code>fsck</code> de comprobación del sistema de archivos:

- a) Debe ejecutarse siempre con el sistema de archivos montado en lectura y escritura, para que pueda corregir en caliente
- b) Solo puede ejecutarse desde el gestor de arranque, nunca desde un medio de rescate
- c) No debe ejecutarse sobre un sistema de archivos montado en lectura y escritura: se ejecuta desde un medio de rescate, en modo de emergencia o programada para el siguiente arranque

**Respuesta correcta:** c) · **Referencia:** §8.1 [MAN-PAGES]

Comprobar y reparar un sistema de archivos montado y activo puede destruir datos.

### 57. Un servidor Linux arranca pero se queda colgado al iniciar los servicios. ¿Qué mecanismo permite entrar con una sesión de administrador y los servicios detenidos para diagnosticarlo?

- a) Ejecutar <code>fsck</code> desde el gestor de arranque GRUB
- b) Arrancar en <code>rescue.target</code> (o <code>emergency.target</code>), editando temporalmente la entrada de GRUB
- c) Reinstalar el gestor de arranque con <code>grub-install</code>

**Respuesta correcta:** b) · **Referencia:** §8.1 [SYSTEMD] [GRUB-DOC]

<code>rescue.target</code> monta el sistema de archivos y ofrece una sesión de administrador sin arrancar los servicios; <code>emergency.target</code> es aún más mínimo. El equivalente en Windows es el modo seguro.

### 58. El RPO (<em>Recovery Point Objective</em>) de un servicio expresa:

- a) La cantidad de datos que se admite perder, medida en tiempo, y determina la frecuencia de las copias
- b) El tiempo máximo que el servicio puede permanecer caído antes de restablecerse
- c) El porcentaje de disponibilidad comprometido en el acuerdo de nivel de servicio

**Respuesta correcta:** a) · **Referencia:** §8.2 [NIST80034] [ISO22301]

El RPO mira hacia atrás (pérdida de datos) y el RTO hacia delante (tiempo sin servicio). Ambos los fija el responsable del servicio a partir del análisis de impacto, no el técnico.

### 59. Para restaurar un sistema protegido con copia total semanal y copias incrementales diarias se necesita:

- a) Únicamente la última copia incremental
- b) La copia total y la última copia incremental
- c) La copia total y todas las copias incrementales posteriores, en orden

**Respuesta correcta:** c) · **Referencia:** §8.2 [NIST80034]

La incremental copia lo cambiado desde la última copia de cualquier tipo: si se pierde o corrompe un eslabón, la cadena se rompe. Con copias <strong>diferenciales</strong> bastaría la total más la última diferencial.

### 60. Según la medida <code>mp.info.6</code> del ENS y sus refuerzos, respecto a las copias de seguridad:

- a) Basta con acreditar que el trabajo de copia finaliza sin errores en el registro de la herramienta
- b) Los procedimientos de copia y de restauración deben probarse regularmente, y al menos una copia debe almacenarse separada, en lugar diferente
- c) Todas las copias deben conservarse en el mismo centro de proceso de datos, para agilizar la recuperación

**Respuesta correcta:** b) · **Referencia:** §8.2 [ENS] [NIST80034]

El objetivo es que un mismo incidente no pueda afectar a la vez al repositorio original y a la copia. Una copia nunca restaurada no es una copia: es una suposición.

## Preguntas sobre los casos prácticos

### Caso 1. Puesta en servicio de un servidor de la Sede Electrónica

#### 1. ¿Cómo debe organizarse el segundo disco para que un componente en bucle no vuelva a llenar el volumen del sistema?

- a) Con LVM y volúmenes lógicos separados para los datos y para los registros.
- b) Con una única partición grande montada en / para dar más margen al sistema.
- c) Llevando los registros a /tmp, cuyo contenido el sistema vacía periódicamente.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.2.1

Si el volumen de registros es independiente, un componente en bucle llena su propio volumen y no el del sistema ni el de los datos.

#### 2. ¿Cuál es el orden correcto de las capas de almacenamiento que se montan sobre el disco nuevo?

- a) Sistema de archivos → partición → LVM → dispositivo de bloques → punto de montaje.
- b) Dispositivo de bloques → partición → LVM (PV → VG → LV) → sistema de archivos → punto de montaje.
- c) Dispositivo de bloques → sistema de archivos → LVM (LV → VG → PV) → partición → punto de montaje.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.2.1

Sobre el dispositivo de bloques se construye la pila: partición, volumen lógico (PV, VG y LV), sistema de archivos y punto de montaje.

#### 3. Más adelante hay que ampliar el volumen de datos sin parar el servicio. ¿Qué hay que hacer?

- a) Ejecutar solo lvextend: el sistema de archivos ocupa el nuevo espacio de forma automática.
- b) Desmontar el volumen, pasar fsck y ampliar después el grupo de volúmenes con vgextend.
- c) Ejecutar lvextend sobre el volumen lógico y, después, resize2fs o xfs_growfs sobre el sistema de archivos.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.2.1

Son dos pasos: si solo se amplía el volumen lógico, df sigue mostrando el tamaño antiguo.

#### 4. ¿Qué esquema de cuentas procede para los tres técnicos de explotación?

- a) Una cuenta compartida «explotacion», con la contraseña custodiada en sobre cerrado por el jefe de equipo.
- b) Una cuenta nominal por técnico y, para administrar, una cuenta de administración diferenciada con segundo factor.
- c) La cuenta root para los tres, con contraseña larga y cambio obligatorio cada sesenta días.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §3.1

Las cuentas compartidas destruyen la trazabilidad; mínimo privilegio y separación de funciones exigen separar la cuenta de uso diario de la de administración.

#### 5. ¿Con qué cuenta debe ejecutarse la aplicación de terceros?

- a) Con una cuenta de servicio propia, sin sesión interactiva y con permisos solo sobre sus directorios.
- b) Con la cuenta nominal del técnico que la instala, para que quede trazado quién la puso en marcha.
- c) Con la cuenta root, para evitar fallos de permisos al escribir sus registros y sus datos.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §3.2

El servicio se ejecuta con privilegios mínimos y sin depender de la cuenta de una persona.

#### 6. ¿Qué mecanismo permite a los técnicos reiniciar el servicio sin ser administradores plenos?

- a) Darles la contraseña de root solo para las ventanas de mantenimiento.
- b) Activar el bit SUID en systemctl para que cualquier usuario lo ejecute como root.
- c) Sudo acotado a las órdenes concretas (reinicio y consulta del registro) para su grupo.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §3.1.1

Sudo permite acotar exactamente qué puede hacer cada operador y registra cada orden ejecutada.

#### 7. ¿Qué garantiza que el servicio de la aplicación vuelva a arrancar tras un reinicio del servidor?

- a) Ejecutar systemctl start, que deja el servicio activo también en los arranques siguientes.
- b) Programar en cron un systemctl restart cada minuto para relanzarlo si se ha detenido.
- c) Habilitarlo con systemctl enable (o enable --now): start solo lo arranca en ese momento.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §3.2

start y enable son operaciones independientes: un servicio arrancado pero no habilitado desaparece tras reiniciar.

#### 8. ¿Cuál de estas es una buena práctica exigible al proceso nocturno de consolidación?

- a) Que sea idempotente y use un bloqueo para no solaparse consigo mismo si un día tarda de más.
- b) Que se ejecute con la cuenta nominal del técnico que lo programó, para saber quién responde.
- c) Que solo envíe aviso cuando termine bien, para no saturar el buzón del equipo de explotación.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §3.2

La tarea debe ser idempotente, usar un bloqueo, registrar su resultado, avisar también si falla y correr con una cuenta de servicio.

#### 9. ¿Qué documentación debe existir antes de considerar el servidor «en servicio»?

- a) Solo el manual de la aplicación de terceros, el contrato de soporte y la factura de compra del servidor.
- b) Inventario, arquitectura, configuración base, procedimientos operativos, registro de cambios, plan de continuidad y ANS.
- c) Las contraseñas de todas las cuentas, el código fuente de la aplicación y sus licencias de uso.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §4.1

La documentación debe ser suficiente para reconstruir el servicio desde cero y no depender de una persona concreta.

#### 10. ¿Por qué el inventario es la pieza fundacional de esa documentación?

- a) Porque no se puede proteger, parchear ni recuperar lo que no se sabe que existe (op.exp.1 del ENS).
- b) Porque es la única medida del ENS que se exige solo a los sistemas de categoría ALTA.
- c) Porque sustituye al registro de cambios y al plan de continuidad del servidor.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §4.1

De él dependen el análisis de riesgos, la gestión de parches y la recuperación; op.exp.1 se aplica en las tres categorías.

### Caso 2. Ventana de mantenimiento y parche crítico

#### 1. ¿Cómo se determina la prioridad real de aplicación del parche de la vulnerabilidad con CVSS 9,4?

- a) Solo con la puntuación CVSS: al ser superior a 9,0, el parche tiene la máxima prioridad.
- b) Combinando gravedad, exposición del activo, criticidad del servicio y explotación activa.
- c) Con la fecha de publicación: los parches se aplican en el orden en que salen.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §6.1

Aquí los cuatro factores apuntan en la misma dirección: banda crítica, componente publicado en Internet, servicio con efectos jurídicos y explotación activa.

#### 2. ¿Por qué la puntuación CVSS, por sí sola, no determina la prioridad?

- a) Porque CVSS solo puntúa de 0 a 5 y no distingue las vulnerabilidades críticas.
- b) Porque un 9,4 pertenece a la banda alta, no a la crítica, de la escala CVSS.
- c) Porque puntúa la vulnerabilidad, no el riesgo del activo concreto en que está.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §6.1

Una vulnerabilidad de 9,8 en un servicio deshabilitado puede ser menos urgente que una de 7,0 explotada en un servidor publicado.

#### 3. Un responsable propone aplicarlo «esta misma tarde en todo el parque». ¿Cómo debe valorarse?

- a) Debe rechazarse: la urgencia comprime los plazos, pero no suprime las etapas de prueba y despliegue.
- b) Debe aceptarse: la explotación activa obliga a saltarse las pruebas y desplegar en todo el parque.
- c) Debe rechazarse y dejar el parche para el ciclo mensual ordinario, como cualquier otra actualización.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §6.2

Un parche defectuoso aplicado a la vez a 4.200 puestos convertiría un incidente de seguridad en una caída generalizada.

#### 4. ¿En qué orden deben recorrerse los anillos de despliegue en este supuesto?

- a) Primero los 6 servidores de la Sede, por estar expuestos; después piloto, puestos y laboratorio.
- b) Los 4.200 puestos a la vez y, si no hay fallos, los servidores de la Sede al día siguiente.
- c) Laboratorio, piloto, producción no crítica y, por último, los servidores de la Sede en ventana.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §6.2

La producción crítica va la última, en ventana de mantenimiento y con la marcha atrás preparada, tras verificar cada anillo.

#### 5. Mientras el parche recorre los anillos, ¿qué se hace con el componente expuesto de la Sede?

- a) Aplicar mitigaciones temporales en el perímetro sobre el componente expuesto.
- b) Desactivar el registro de actividad para aligerar la carga de los servidores.
- c) Nada: hasta que llegue su anillo, el componente se deja tal como está.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §6.1

Con explotación activa no se espera sin más: se aplican mitigaciones temporales (filtrar, restringir accesos, reforzar la vigilancia) mientras llega la corrección.

#### 6. ¿Cómo se tramita este despliegue en la gestión de cambios?

- a) Como cambio estándar preaprobado, que no necesita documentarse.
- b) Como cambio de emergencia: se ejecuta primero y se documenta y aprueba formalmente después.
- c) Como cambio normal, que debe esperar a la reunión ordinaria del comité de cambios.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.1

El cambio de emergencia se ejecuta para atajar el riesgo, pero se documenta y aprueba después, nunca «en lugar de».

#### 7. ¿Qué medida del anexo II del ENS regula esta actividad?

- a) op.exp.1 — Inventario de activos.
- b) op.exp.4 — Mantenimiento y actualizaciones de seguridad.
- c) mp.info.6 — Copias de seguridad.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §4.2.1

op.exp.4 exige seguir los anuncios del fabricante y un procedimiento para analizar, priorizar y decidir cuándo aplicar las actualizaciones.

#### 8. ¿Qué obliga a hacer el refuerzo R1 de esa medida?

- a) Prever un mecanismo para revertir los parches si aparecen efectos adversos.
- b) Someter el sistema a una auditoría extraordinaria tras cada actualización.
- c) Probar en preproducción, en un entorno consistente con producción, antes de aplicar.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §6.2.1

R1 son las pruebas en preproducción; la reversión es el refuerzo R2 (prevención de fallos).

#### 9. Solo la disponibilidad de la Sede está en nivel ALTO. ¿Qué refuerzos de op.exp.4 le son exigibles?

- a) Los dos, R1 y R2, porque el sistema es de categoría ALTA.
- b) Solo R1, porque con una única dimensión en ALTO el sistema es de categoría MEDIA.
- c) Ninguno, porque los refuerzos son recomendaciones y no medidas exigibles.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §4.2.1

Manda la dimensión más alta: basta una dimensión en nivel ALTO para que todo el sistema sea de categoría ALTA, y R2 se exige en ALTA.

#### 10. ¿Qué mecanismo de marcha atrás procede para los 6 servidores de la Sede y qué límite tiene?

- a) La restauración desde copia de seguridad, porque es el mecanismo más rápido disponible.
- b) El punto de restauración del sistema, que además recupera los datos de los usuarios.
- c) La instantánea previa de cada máquina virtual, que no sustituye a la copia de seguridad.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §6.2.1

La instantánea es inmediata y completa, pero depende del mismo almacenamiento: si se pierde la cabina o se cifra el volumen, se pierden ambas.

### Caso 3. Caída de un servidor: diagnóstico, reparación y recuperación

#### 1. El servidor del Padrón no arranca y no encuentra el volumen raíz. ¿Cuál es la primera hipótesis razonable?

- a) Un fallo de la red del centro de proceso de datos, que impide las conexiones remotas.
- b) Un certificado caducado en el servidor de aplicaciones del Padrón.
- c) La actualización del núcleo aplicada la noche anterior.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §7.2

La primera pregunta útil es qué ha cambiado: la inmensa mayoría de las incidencias siguen a un cambio.

#### 2. ¿De qué es firma clásica el mensaje «no encuentra el volumen raíz» tras actualizar el núcleo?

- a) De un initramfs regenerado sin el controlador necesario para montar la raíz.
- b) De una partición ESP dañada, que impide al firmware cargar el gestor de arranque.
- c) De un disco lleno en /var/log, que impide al sistema escribir sus registros.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §1.2.1

Si el initramfs no incluye el controlador del RAID, del cifrado o de la cabina, el sistema arranca y muere por no encontrar la raíz.

#### 3. Además de diagnosticar el servidor caído, ¿qué medida de contención procede?

- a) Aplicar la misma actualización al resto de servidores para homogeneizar el parque.
- b) Detener el despliegue de esa actualización en el resto de servidores hasta aclarar lo ocurrido.
- c) Reinstalar desde cero todos los servidores que recibieron la actualización la misma noche.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §7.2

Aislar y contener evita que el fallo se propague a otros servidores mientras se investiga.

#### 4. ¿En qué eslabón de la cadena de arranque se ha detenido el sistema?

- a) En el del núcleo y el initramfs, después del gestor de arranque y antes del proceso inicial.
- b) En el del firmware, antes de llegar a cargar el gestor de arranque desde el disco.
- c) En el del proceso inicial (systemd), al activar los servicios del objetivo multiusuario.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §8.1

El síntoma «no se encuentra el volumen raíz» corresponde al punto de fallo núcleo/initramfs.

#### 5. ¿Cuál es la técnica de reparación de menor coste que debe intentarse primero?

- a) Restaurar el servidor desde la copia de seguridad del sábado.
- b) Arrancar desde un medio vivo y reinstalar el gestor de arranque con chroot.
- c) Arrancar la entrada anterior del núcleo desde el menú de GRUB.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §6.2.1

Es la actuación con mejor relación entre probabilidad de éxito y coste, y devuelve el servicio en minutos.

#### 6. Si no arranca ninguna entrada del núcleo, ¿cuál es el siguiente paso razonable antes de restaurar?

- a) Ejecutar fsck sobre la raíz montada en lectura y escritura para reparar el volumen.
- b) Arrancar desde un medio vivo, montar los volúmenes, hacer chroot y regenerar el initramfs.
- c) Ejecutar bootrec /rebuildbcd desde el entorno de recuperación del sistema.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §8.1

Con chroot se «entra» en la instalación dañada para repararla desde dentro; fsck nunca se ejecuta con el sistema montado en lectura y escritura.

#### 7. Restablecido el servicio, ¿dónde se acredita qué se instaló la noche del domingo y cuándo?

- a) En el registro de autenticación (auth.log o secure) del servidor afectado.
- b) En los registros del gestor de paquetes, junto a los del arranque anterior (journalctl -b -1).
- c) En los registros de la aplicación de Padrón, que anotan las versiones del núcleo.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §7.1

El gestor de paquetes deja constancia de lo instalado; journalctl -b -1 muestra los errores del arranque anterior.

#### 8. ¿Qué dos requisitos deben cumplir esos registros para no perder su valor como evidencia?

- a) Sincronización horaria por NTP y centralización protegida en un servidor distinto.
- b) Rotación diaria y compresión, para que no agoten el disco del servidor auditado.
- c) Nivel de depuración (debug) activado y conservación en el disco local del servidor.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §7.1

Sin hora común no se correlacionan eventos de varias máquinas, y sin centralización los registros desaparecen con la máquina o pueden alterarse.

#### 9. Si hubiera que restaurar el lunes, ¿qué copias se necesitarían?

- a) Solo la última incremental, la del domingo, que ya contiene todos los datos del servidor.
- b) La total del sábado, todas las incrementales posteriores en orden y los registros horarios.
- c) La total del sábado y la última diferencial, que acumula lo cambiado desde entonces.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §8.2

La incremental restaura en tantos pasos como copias tenga la cadena; si falta una, la cadena se rompe.

#### 10. ¿Cumple la estrategia descrita el RPO de una hora y el RTO de cuatro horas?

- a) Cumple ambos, porque existe una copia horaria de los registros de transacción.
- b) Incumple el RPO, porque las copias incrementales solo se hacen una vez al día.
- c) Cumple el RPO; el RTO depende del tiempo real medido en una prueba de restauración.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §8.2

La pérdida máxima es de una hora; el RTO solo se conoce restaurando de verdad, como exige el refuerzo R1 de mp.info.6 del ENS.
