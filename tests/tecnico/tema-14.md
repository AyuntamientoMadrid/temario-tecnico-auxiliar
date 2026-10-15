# Test del tema 14. Los sistemas operativos

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-14.html>

## Batería de preguntas

### 1. Las dos visiones complementarias de un sistema operativo son:

- a) Compilador y enlazador
- b) Máquina extendida y gestor de recursos
- c) Hardware y firmware

**Respuesta correcta:** b) · **Referencia:** §1.1 [SILBERSCHATZ-OS]

El SO es **máquina extendida** (oculta el hardware) y **gestor de recursos** (reparte CPU, memoria y dispositivos).

### 2. El mecanismo por el que una aplicación en modo usuario solicita un servicio al núcleo es:

- a) La interrupción de reloj
- b) El cambio de contexto
- c) La llamada al sistema (syscall)

**Respuesta correcta:** c) · **Referencia:** §1.1 [STALLINGS-OS]

La **syscall** provoca un cambio controlado (trap) de modo usuario a modo núcleo para solicitar un servicio.

### 3. ¿Qué se ejecuta en modo núcleo (privilegiado)?

- a) Solo las aplicaciones de usuario
- b) Únicamente el navegador web
- c) El sistema operativo, con acceso total al hardware

**Respuesta correcta:** c) · **Referencia:** §1.1

El SO se ejecuta en **modo núcleo** con acceso total; las aplicaciones, en modo usuario restringido.

### 4. La multitarea apropiativa (preemptiva) se caracteriza por:

- a) El SO retira la CPU al proceso mediante interrupciones de reloj
- b) Cada proceso cede la CPU voluntariamente
- c) Solo puede ejecutarse un proceso a la vez en todo el sistema

**Respuesta correcta:** a) · **Referencia:** §1.2

En la apropiativa, **el SO retira la CPU**; en la cooperativa, el proceso la cede voluntariamente (un proceso colgado bloquearía el sistema).

### 5. ¿Cuál de estos conceptos implica varias CPU o núcleos físicos ejecutando en paralelo?

- a) Multitarea
- b) Multiproceso
- c) Multihilo

**Respuesta correcta:** b) · **Referencia:** §1.2

**Multiproceso** = varias CPU/núcleos en paralelo. Multitarea = procesos alternándose (aunque haya 1 CPU); multihilo = hilos dentro de un proceso.

### 6. Una arquitectura de SO en la que el núcleo es mínimo y los servicios (ficheros, drivers) corren en modo usuario es:

- a) Monolítica
- b) Por lotes
- c) Microkernel

**Respuesta correcta:** c) · **Referencia:** §1.3 [TANENBAUM-MOS]

El **microkernel** reduce el núcleo al mínimo y ejecuta los servicios en modo usuario (más robusto, más lento por mensajería). Ej.: MINIX, QNX.

### 7. El núcleo de Linux es:

- a) Microkernel puro
- b) Monolítico modular
- c) Sin núcleo

**Respuesta correcta:** b) · **Referencia:** §1.3, §4.2

Linux es **monolítico** (todo en el núcleo, rápido) pero **modular** (carga módulos en caliente).

### 8. ¿Qué arquitectura de núcleo usan Windows NT y macOS?

- a) Microkernel puro
- b) Por capas estricta
- c) Híbrida

**Respuesta correcta:** c) · **Referencia:** §1.3, §3.2

Ambos son **híbridos**: combinan un núcleo amplio con cierta modularidad y servicios en espacio de usuario.

### 9. Un sistema operativo de tiempo real estricto (hard) se caracteriza por:

- a) Ejecutar trabajos en serie sin interacción
- b) Garantizar tiempos de respuesta acotados, críticos si se incumplen
- c) Repartir la CPU entre muchos usuarios interactivos

**Respuesta correcta:** b) · **Referencia:** §1.4

El RTOS **hard** garantiza plazos cuyo incumplimiento es crítico (aviónica, control industrial). El soft tolera pequeños retrasos.

### 10. ¿En qué año y por quién se publicó el núcleo Linux?

- a) 1969, por Ken Thompson
- b) 1991, por Linus Torvalds
- c) 1983, por Richard Stallman

**Respuesta correcta:** b) · **Referencia:** §1.5, §4.1

Linus Torvalds publicó el **núcleo Linux en 1991**. Thompson/Ritchie crearon UNIX (1969); Stallman, el proyecto GNU (1983).

### 11. ¿Cuándo nació UNIX y qué lo hizo portable?

- a) 1969 en Bell Labs; su reescritura en lenguaje C
- b) 1991; su licencia GPL
- c) 2007; su interfaz táctil

**Respuesta correcta:** a) · **Referencia:** §1.5, §4.1

UNIX nació en **1969 (Bell Labs)**; su reescritura en **C** (1973) lo hizo portable.

### 12. La interfaz de línea de comandos (CLI) frente a la gráfica (GUI):

- a) Es potente, ligera y automatizable mediante scripts
- b) Es menos potente y no automatizable
- c) Solo existe en sistemas móviles

**Respuesta correcta:** a) · **Referencia:** §2.6

La **CLI** es potente, ligera y *scriptable* (preferida en servidores). La **GUI** es más accesible para el usuario final.

### 13. La diferencia esencial entre un proceso y un hilo es:

- a) El hilo siempre es más lento que el proceso
- b) No hay diferencia, son sinónimos
- c) El proceso tiene espacio de memoria propio; los hilos de un proceso comparten su memoria

**Respuesta correcta:** c) · **Referencia:** §2.1

El **proceso** tiene memoria propia y aislada; los **hilos** de un proceso comparten su memoria (cada uno con su pila). Crear un hilo es más barato.

### 14. La estructura donde el SO guarda el estado, los registros y los recursos de un proceso es:

- a) La tabla de páginas
- b) El PCB (Bloque de Control de Proceso)
- c) El cargador de arranque

**Respuesta correcta:** b) · **Referencia:** §2.1 [SILBERSCHATZ-OS]

El **PCB (Process Control Block)** describe cada proceso: PID, estado, registros, info de planificación, memoria y ficheros abiertos.

### 15. Cuando un proceso solicita una operación de E/S, pasa al estado:

- a) Listo
- b) Bloqueado
- c) En ejecución

**Respuesta correcta:** b) · **Referencia:** §2.1

Al esperar un evento (E/S, recurso) el proceso pasa a **bloqueado**; cuando la E/S termina vuelve a **listo**.

### 16. El algoritmo de planificación que asigna a cada proceso un quantum y lo pasa al final de la cola al agotarlo es:

- a) Round-Robin
- b) FCFS
- c) SJF

**Respuesta correcta:** a) · **Referencia:** §2.1 [SILBERSCHATZ-OS]

**Round-Robin** reparte la CPU por turnos (quantum); es la base del tiempo compartido.

### 17. El "efecto convoy" (procesos cortos esperando tras uno largo) es típico del algoritmo:

- a) Round-Robin
- b) Colas multinivel
- c) FCFS (orden de llegada)

**Respuesta correcta:** c) · **Referencia:** §2.1

**FCFS** (First Come First Served) penaliza a los procesos cortos que llegan tras uno largo: efecto convoy.

### 18. La inanición (starvation) de los procesos de baja prioridad se mitiga con:

- a) El efecto convoy
- b) El envejecimiento (aging)
- c) El thrashing

**Respuesta correcta:** b) · **Referencia:** §2.1

El **envejecimiento (aging)** sube la prioridad de un proceso conforme espera, evitando la inanición.

### 19. ¿Cuántas condiciones de Coffman deben darse simultáneamente para que haya interbloqueo?

- a) Dos
- b) Cuatro
- c) Seis

**Respuesta correcta:** b) · **Referencia:** §2.1 [TANENBAUM-MOS]

Las **4 condiciones de Coffman**: exclusión mutua, retención y espera, no apropiación y espera circular. Romper cualquiera evita el deadlock.

### 20. El algoritmo del banquero (Dijkstra) es una estrategia de:

- a) Planificación de CPU
- b) Reemplazo de páginas
- c) Evitación del interbloqueo

**Respuesta correcta:** c) · **Referencia:** §2.1

El **algoritmo del banquero** es de **evitación**: solo concede recursos si el estado resultante es seguro.

### 21. La memoria virtual permite que:

- a) Un proceso use solo la RAM física disponible
- b) Cada proceso disponga de un espacio lógico mayor que la RAM, con disco como respaldo
- c) Se elimine por completo el uso de disco

**Respuesta correcta:** b) · **Referencia:** §2.2 [SILBERSCHATZ-OS]

La **memoria virtual** da a cada proceso un espacio lógico mayor que la RAM; la MMU traduce direcciones y el disco (swap) actúa de respaldo.

### 22. En la paginación, las páginas y los marcos tienen:

- a) Tamaño variable según la lógica del programa
- b) Tamaño siempre de 1 byte
- c) Tamaño fijo e igual

**Respuesta correcta:** c) · **Referencia:** §2.2

En **paginación** página y marco son de **tamaño fijo** (p. ej. 4 KB), lo que elimina la fragmentación externa. La segmentación usa bloques de tamaño variable.

### 23. El componente hardware que traduce direcciones lógicas a físicas es:

- a) La MMU (Memory Management Unit)
- b) La ALU
- c) El spooler

**Respuesta correcta:** a) · **Referencia:** §2.2

La **MMU** traduce en cada acceso la dirección lógica a física; la TLB cachea traducciones recientes.

### 24. La hiperpaginación (thrashing) ocurre cuando:

- a) Hay demasiados fallos de página por falta de RAM y el rendimiento se desploma
- b) El disco está cifrado
- c) La CPU tiene demasiados núcleos

**Respuesta correcta:** a) · **Referencia:** §2.2

El **thrashing** es la degradación por exceso de fallos de página al faltar memoria: el sistema intercambia más de lo que ejecuta.

### 25. Un fallo de página (page fault) significa que:

- a) El disco está lleno
- b) La página solicitada no está en la RAM y hay que traerla de disco
- c) El proceso ha terminado

**Respuesta correcta:** b) · **Referencia:** §2.2

El **fallo de página** indica que la página no está en RAM; el SO la trae de disco, expulsando otra si es necesario (LRU, FIFO…).

### 26. El mecanismo por el que un dispositivo avisa a la CPU al terminar una operación, evitando la espera activa, es:

- a) La interrupción
- b) El polling
- c) El swapping

**Respuesta correcta:** a) · **Referencia:** §2.3

La **interrupción** permite que el dispositivo avise a la CPU, en lugar de que esta pregunte continuamente (polling, espera activa).

### 27. El DMA (Direct Memory Access) sirve para:

- a) Transferir datos entre dispositivo y memoria sin intervención continua de la CPU
- b) Cifrar el disco
- c) Planificar procesos

**Respuesta correcta:** a) · **Referencia:** §2.3

El **DMA** transfiere bloques entre dispositivo y memoria sin que la CPU intervenga continuamente; solo se le avisa al terminar.

### 28. El spooling se utiliza típicamente para:

- a) Gestionar la cola de trabajos de dispositivos compartidos como la impresora
- b) Cifrar contraseñas
- c) Acelerar la CPU

**Respuesta correcta:** a) · **Referencia:** §2.3

El **spooling** encola en disco los trabajos de dispositivos lentos y compartidos (impresoras) y los sirve en orden.

### 29. El módulo de software que traduce las órdenes genéricas del SO al lenguaje de un dispositivo concreto es:

- a) El planificador
- b) El intérprete de comandos
- c) El controlador (driver)

**Respuesta correcta:** c) · **Referencia:** §2.3

El **driver (controlador)** traduce las órdenes del SO al protocolo de cada dispositivo, ofreciendo una interfaz uniforme.

### 30. El principio de seguridad que recomienda conceder a cada usuario o proceso solo los permisos imprescindibles es:

- a) El máximo privilegio
- b) El mínimo privilegio
- c) La espera circular

**Respuesta correcta:** b) · **Referencia:** §2.5 [ENS-RD311]

El **mínimo privilegio** otorga solo los permisos necesarios, reduciendo el impacto de un fallo o ataque. Es base del ENS.

### 31. El núcleo de Windows moderno se denomina:

- a) XNU, microkernel puro
- b) Linux
- c) NT, de arquitectura híbrida

**Respuesta correcta:** c) · **Referencia:** §3.2 [WININTERNALS]

Windows se basa en el núcleo **NT**, híbrido, con Executive, Kernel, drivers y la HAL en modo núcleo.

### 32. La capa de Windows que aísla el núcleo de las particularidades del hardware es:

- a) La HAL (Hardware Abstraction Layer)
- b) El Registro
- c) PowerShell

**Respuesta correcta:** a) · **Referencia:** §3.2

La **HAL** abstrae el hardware, facilitando la portabilidad del núcleo NT.

### 33. ¿Qué caracteriza a PowerShell frente a las shells Unix clásicas?

- a) Está orientada a objetos (pasa objetos por la tubería, no texto)
- b) Solo funciona con ratón
- c) No permite scripting

**Respuesta correcta:** a) · **Referencia:** §3.3 [MS-PWSH]

**PowerShell** es orientada a **objetos**: los cmdlets (`Verbo-Nombre`) pasan objetos con propiedades, no cadenas de texto.

### 34. El servicio de directorio que centraliza autenticación, usuarios y políticas en un dominio Windows es:

- a) BitLocker
- b) Windows Defender
- c) Active Directory

**Respuesta correcta:** c) · **Referencia:** §3.6 [MS-AD]

**Active Directory** centraliza la autenticación (Kerberos), los usuarios, los equipos y las **GPO** del dominio.

### 35. Las políticas que aplican configuración y seguridad de forma uniforme a los equipos de un dominio se llaman:

- a) Cmdlets
- b) GPO (políticas de grupo)
- c) Inodos

**Respuesta correcta:** b) · **Referencia:** §3.6

Las **GPO (Group Policy Objects)** aplican configuración y seguridad de forma centralizada en un dominio Active Directory.

### 36. El mecanismo de Windows que solicita confirmación para acciones con privilegios de administrador es:

- a) WSUS
- b) ReFS
- c) UAC (User Account Control)

**Respuesta correcta:** c) · **Referencia:** §3.6

El **UAC** pide confirmación para las acciones que requieren privilegios elevados, aplicando el mínimo privilegio.

### 37. El cifrado de disco completo integrado en Windows es:

- a) EFS
- b) BitLocker
- c) FileVault

**Respuesta correcta:** b) · **Referencia:** §3.6

**BitLocker** cifra el disco completo (apoyado en TPM). EFS cifra ficheros sueltos; FileVault es de macOS.

### 38. El sistema de ficheros nativo de Windows es:

- a) ext4
- b) NTFS
- c) APFS

**Respuesta correcta:** b) · **Referencia:** §3.4

**NTFS** (journaling, ACL, EFS) es el nativo de Windows. ReFS para resiliencia; ext4 es de Linux; APFS de Apple.

### 39. La edición de Windows Server que prescinde de la GUI completa para reducir recursos y superficie de ataque es:

- a) Server Core
- b) Home
- c) Enterprise

**Respuesta correcta:** a) · **Referencia:** §3.8

**Server Core** prescinde de la GUI completa, administrándose por línea de comandos (PowerShell) y de forma remota.

### 40. El protocolo de autenticación usado por Active Directory es:

- a) HTTP
- b) SMTP
- c) Kerberos

**Respuesta correcta:** c) · **Referencia:** §3.6

Active Directory autentica con **Kerberos** (tickets), el protocolo estándar de autenticación en dominios Windows.

### 41. La configuración del sistema en Windows se centraliza en:

- a) El Registro (base de datos jerárquica)
- b) El directorio /etc
- c) El fichero hosts

**Respuesta correcta:** a) · **Referencia:** §3.2

El **Registro de Windows** es la base de datos jerárquica que centraliza la configuración del sistema y las aplicaciones.

### 42. En cuanto a la interfaz gráfica, Windows se diferencia de Linux en que:

- a) Windows no tiene interfaz gráfica
- b) La GUI de Windows es siempre opcional
- c) La GUI de Windows está integrada y no es separable del sistema

**Respuesta correcta:** c) · **Referencia:** §3.5, §4.5

En Windows la **GUI está integrada** en el SO; en Linux es modular y opcional (un servidor puede funcionar solo con CLI).

### 43. El estándar que normaliza la API, la shell y las utilidades entre sistemas Unix es:

- a) NTFS
- b) POSIX (IEEE 1003)
- c) HTTP

**Respuesta correcta:** b) · **Referencia:** §4.1 [POSIX]

**POSIX (IEEE 1003)** garantiza la portabilidad del software entre los distintos sistemas Unix.

### 44. La combinación del núcleo de Torvalds con las herramientas de Stallman se denomina:

- a) Windows NT
- b) GNU/Linux
- c) Android puro

**Respuesta correcta:** b) · **Referencia:** §4.1

**GNU/Linux**: el núcleo **Linux** (Torvalds) más las herramientas **GNU** (Stallman, GPL) forman el sistema completo. Linux, en rigor, es solo el núcleo.

### 45. El componente del kernel Linux que ofrece una interfaz común a los distintos sistemas de ficheros es:

- a) El VFS (Virtual File System)
- b) La HAL
- c) El planificador

**Respuesta correcta:** a) · **Referencia:** §4.2

El **VFS** abstrae ext4, XFS, NFS… tras una interfaz única, de modo que las aplicaciones los usan igual.

### 46. En Linux moderno, el proceso con PID 1 que gestiona el arranque y los servicios es:

- a) bootmgr
- b) systemd
- c) explorer

**Respuesta correcta:** b) · **Referencia:** §4.3

**systemd** es el PID 1 actual (sustituye al init System V); gestiona *units* y *targets* y se controla con `systemctl`.

### 47. En Linux, los discos y particiones:

- a) Reciben letras de unidad (C:, D:)
- b) No se pueden usar
- c) Se montan en directorios bajo la raíz única "/"

**Respuesta correcta:** c) · **Referencia:** §4.4 [FHS]

En Linux todo cuelga de la **raíz única `/`**; los discos se **montan** en directorios (no hay letras de unidad como en Windows).

### 48. Según el FHS, ¿dónde se ubican los ficheros de configuración del sistema en Linux?

- a) /etc
- b) /home
- c) /dev

**Respuesta correcta:** a) · **Referencia:** §4.4

**`/etc`** contiene la configuración del sistema. `/home` son las carpetas de usuario; `/dev`, los dispositivos.

### 49. El comando que ejecuta una orden puntual con privilegios elevados de forma controlada y auditada es:

- a) chmod
- b) grep
- c) sudo

**Respuesta correcta:** c) · **Referencia:** §4.6

**`sudo`** ejecuta comandos con privilegios de root de forma controlada, en lugar de trabajar siempre como superusuario.

### 50. SELinux y AppArmor son mecanismos de:

- a) Control de acceso obligatorio (MAC) que refuerzan los permisos
- b) Cifrado de disco
- c) Planificación de CPU

**Respuesta correcta:** a) · **Referencia:** §4.6

**SELinux** (Red Hat) y **AppArmor** (Debian/Ubuntu) son **MAC**: refuerzan el control de acceso por encima de los permisos discrecionales.

### 51. El gestor de paquetes de las distribuciones Debian/Ubuntu es:

- a) APT/dpkg
- b) DNF/RPM
- c) PowerShell

**Respuesta correcta:** a) · **Referencia:** §4.7

**APT/dpkg** es de Debian/Ubuntu; **DNF/RPM** es de Red Hat/Fedora. Actualizan desde repositorios firmados.

### 52. El software libre (licencia GPL) garantiza las libertades de:

- a) Solo usar, nunca modificar
- b) Solo para empresas privadas
- c) Usar, estudiar, modificar y distribuir

**Respuesta correcta:** c) · **Referencia:** §4.7 [GPL]

El **software libre** (GPL) garantiza usar, estudiar, modificar y distribuir; encaja con los estándares abiertos del sector público.

### 53. El sistema operativo Android está basado en:

- a) El kernel Linux
- b) El núcleo NT de Windows
- c) El núcleo Darwin

**Respuesta correcta:** a) · **Referencia:** §5.2 [AOSP]

**Android** se construye sobre el **kernel Linux**; iOS, sobre Darwin/Unix.

### 54. iOS se basa en el núcleo:

- a) Darwin/XNU (Mach + BSD)
- b) Linux
- c) Windows NT

**Respuesta correcta:** a) · **Referencia:** §5.3 [APPLE-DARWIN]

**iOS** se basa en **Darwin**, cuyo núcleo XNU combina el micronúcleo **Mach** con componentes **BSD**.

### 55. El mecanismo por el que cada app móvil se ejecuta aislada, con acceso solo a sus datos, es:

- a) El spooling
- b) El sandboxing
- c) El polling

**Respuesta correcta:** b) · **Referencia:** §5.1

El **sandboxing** aísla cada aplicación; combinado con los **permisos por app** es la base de la seguridad móvil.

### 56. En Android, desde la versión 6, los permisos sensibles (cámara, ubicación) se conceden:

- a) Solo al comprar el dispositivo
- b) Nunca se piden
- c) En tiempo de ejecución, de forma revocable

**Respuesta correcta:** c) · **Referencia:** §5.2 [ANDROID-SEC]

Desde Android 6 los permisos sensibles se conceden **en tiempo de ejecución** y son revocables por el usuario.

### 57. El coprocesador aislado de iOS que custodia claves y datos biométricos es:

- a) La HAL
- b) El spooler
- c) El Secure Enclave

**Respuesta correcta:** c) · **Referencia:** §5.3 [APPLE-PSEC]

El **Secure Enclave** es un coprocesador aislado que guarda las claves y los datos biométricos (Touch ID / Face ID).

### 58. ¿Cuál es una diferencia correcta entre Android e iOS?

- a) Android es cerrado; iOS es de código abierto
- b) Ambos usan el mismo núcleo
- c) Android es abierto (AOSP, multifabricante); iOS es cerrado (solo hardware Apple)

**Respuesta correcta:** c) · **Referencia:** §5.4

**Android** es abierto (AOSP) y multifabricante; **iOS** es cerrado y exclusivo del hardware de Apple.

### 59. Una solución MDM (Mobile Device Management) permite:

- a) Compilar el kernel
- b) Administrar centralizadamente los dispositivos: cifrado, políticas, distribución de apps y borrado remoto
- c) Sustituir a la CPU

**Respuesta correcta:** b) · **Referencia:** §5.4

El **MDM** gestiona de forma centralizada los móviles corporativos: políticas de seguridad, apps, separación de perfiles y **borrado remoto**.

### 60. El factor de diseño más diferenciador de un SO móvil frente a uno de escritorio es:

- a) La gestión agresiva de la energía (batería) y de los recursos limitados
- b) La ausencia total de seguridad
- c) Que no admiten aplicaciones

**Respuesta correcta:** a) · **Referencia:** §5.1

Los SO móviles priorizan la **gestión de energía** (batería) y operan con **recursos limitados**, además del táctil, los sensores y el sandboxing.

## Preguntas sobre los casos prácticos

### Caso 1. Gestión del parque de puestos de trabajo (Windows)

#### 1. En el supuesto planteado, ¿qué servicio de Windows centraliza la autenticación y la administración de los miles de puestos, y con qué protocolo autentica a los empleados?

- a) WSUS, que registra usuarios y equipos en un dominio y autentica mediante el chip TPM.
- b) El Registro de Windows, que guarda los usuarios de cada puesto y autentica mediante UAC.
- c) Active Directory, que organiza usuarios y equipos en un dominio y autentica mediante Kerberos.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §3.6

Active Directory es el servicio de directorio que centraliza en un dominio la autenticación, los usuarios y los equipos; el protocolo de autenticación que emplea es Kerberos.

#### 2. El técnico quiere imponer a la vez el bloqueo de pantalla, el cifrado y las restricciones de software en todos los puestos del dominio. ¿Qué mecanismo emplea?

- a) Las políticas de grupo (GPO), definidas en Active Directory y aplicadas a todos los equipos.
- b) La edición del Registro con regedit en cada puesto, replicando a mano la misma configuración.
- c) El Administrador de Control de Servicios, que propaga la configuración como un servicio más.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §3.6

Las GPO se aplican desde Active Directory y llevan la misma configuración y seguridad de forma uniforme a miles de puestos, sin tocar equipo por equipo.

#### 3. La configuración de seguridad que se distribuya por GPO a los puestos del Ayuntamiento, como sistemas del sector público, debe ajustarse a:

- a) El estándar POSIX (IEEE 1003), que fija la configuración segura de los puestos Windows.
- b) Las guías CCN-STIC del Centro Criptológico Nacional, que definen el bastionado obligatorio.
- c) La jerarquía FHS, que establece qué directorios del puesto deben quedar protegidos.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.5, §3.6

En el sector público, el ENS y las guías CCN-STIC del Centro Criptológico Nacional definen el bastionado (hardening) de los sistemas operativos. POSIX y FHS son estándares de Unix/Linux.

#### 4. Para impedir que los empleados instalen software o cambien la configuración del sistema, ¿qué medida es la adecuada?

- a) Retirar a los usuarios los derechos de administrador local y mantener UAC activo (mínimo privilegio).
- b) Conceder a todos derechos de administrador local y confiar en el antivirus Defender para frenarlos.
- c) Desactivar UAC para que los avisos no interrumpan y registrar después los cambios en el Visor de eventos.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §2.5, §3.6

El principio de mínimo privilegio concede a cada usuario solo los permisos imprescindibles: sin administrador local y con UAC exigiendo confirmación para las acciones privilegiadas.

#### 5. Un empleado intenta modificar una opción del sistema y aparece una ventana que pide confirmación con credenciales de administrador. ¿Qué componente actúa?

- a) Microsoft Defender, que bloquea la acción por considerarla un posible malware.
- b) BitLocker, que exige las credenciales antes de permitir acceder al disco cifrado.
- c) UAC (User Account Control), que pide confirmación para las acciones privilegiadas.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §3.6

UAC solicita confirmación explícita para las acciones que requieren privilegios de administrador, aplicando el mínimo privilegio.

#### 6. ¿Cómo distribuiría el técnico los parches de seguridad a todo el parque de forma controlada?

- a) Dejando que cada usuario ejecute Windows Update cuando lo considere oportuno.
- b) Centralizando el parcheado con WSUS o Intune, que aprueban y distribuyen las actualizaciones.
- c) Instalando los parches con el gestor de paquetes APT desde repositorios firmados.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §3.6

En entornos corporativos Windows Update se centraliza con WSUS o Microsoft Intune, que permiten aprobar y distribuir las actualizaciones; APT es el gestor de paquetes de Debian/Ubuntu.

#### 7. Un responsable propone aplazar indefinidamente los parches del parque para evitar incidencias tras las actualizaciones. ¿Qué objeción técnica procede?

- a) Que un sistema operativo sin parchear es la principal vía de ataque contra los puestos.
- b) Que los parches solo añaden funciones nuevas y nunca corrigen vulnerabilidades del sistema.
- c) Que, con BitLocker activo en los puestos, aplazar el parcheado no tiene ningún efecto.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §2.5

Las actualizaciones de seguridad corrigen periódicamente vulnerabilidades; un SO sin parchear es la principal vía de ataque, con o sin cifrado de disco.

#### 8. La ventana de actualizaciones de los puestos (cuándo se instalan los parches) debe ser la misma en todo el dominio. ¿Dónde se configura de forma centralizada?

- a) En el Registro de cada puesto, que el usuario ajusta desde regedit.
- b) En el TPM de cada portátil, que fija la hora de instalación de parches.
- c) En una política de grupo (GPO) aplicada desde Active Directory.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestiones 2 y 3 · §3.6

La ventana de actualizaciones forma parte de la configuración de seguridad que las GPO imponen de forma centralizada a todos los puestos del dominio.

#### 9. Para que los datos de un portátil robado no puedan leerse, ¿qué tecnología de Windows aplicaría el técnico?

- a) ReFS, que protege la integridad de los datos del disco mediante checksums.
- b) BitLocker, que cifra el disco completo del portátil.
- c) Microsoft Defender, que impide abrir los ficheros desde otro equipo.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §3.6

BitLocker es el cifrado de disco completo integrado en Windows: aunque roben el portátil, sin las credenciales el disco es ilegible.

#### 10. ¿En qué componente del portátil se apoya BitLocker para proteger el cifrado del disco?

- a) En el chip TPM del equipo.
- b) En el Secure Enclave del procesador.
- c) En la HAL del núcleo NT.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §3.6

BitLocker se apoya en el chip TPM. El Secure Enclave es el coprocesador de iOS y la HAL es la capa que abstrae el hardware en el núcleo NT.

### Caso 2. Diagnóstico de un servidor Linux de la sede electrónica

#### 1. Para ver en tiempo real qué procesos del servidor consumen más CPU, el técnico ejecuta:

- a) df, que muestra los procesos ordenados por uso de CPU.
- b) journalctl, que lista en directo el consumo de cada proceso.
- c) top (o htop, o ps aux --sort=-%cpu).

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §2.1, §4.3

top (o htop/ps) muestra los procesos por consumo de CPU; df informa del espacio en disco y journalctl consulta los registros de systemd.

#### 2. Un proceso monopoliza la CPU. Los demás procesos, que están preparados para ejecutarse y solo les falta la CPU, ¿en qué estado se encuentran?

- a) Listo (ready), esperando en la cola de listos.
- b) Bloqueado, esperando el fin de una E/S.
- c) Nuevo, pendiente de que se cree su PCB.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §2.1

Un proceso preparado que espera a que el planificador le asigne la CPU está en estado listo; el estado bloqueado corresponde a la espera de un evento como el fin de una E/S.

#### 3. ¿Cómo reparte la CPU un sistema operativo de tiempo compartido para que ningún proceso la acapare?

- a) Por orden de llegada (FCFS): cada proceso usa la CPU hasta terminar.
- b) Por turnos con Round-Robin: cada proceso recibe un quantum y vuelve al final de la cola.
- c) Por la ráfaga más corta (SJF): primero se atienden siempre los trabajos breves.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §2.1

Round-Robin asigna a cada proceso un quantum de tiempo fijo y, al agotarlo, lo pasa al final de la cola de listos; es la base del tiempo compartido.

#### 4. El servidor tiene poca RAM libre y mucho uso de swap. ¿Qué es la memoria virtual que está utilizando?

- a) Un espacio lógico por proceso mayor que la RAM, con el disco (swap) como respaldo.
- b) Una ampliación física de la RAM que se obtiene usando la caché del procesador.
- c) Un modo en que cada proceso usa directamente direcciones físicas de la RAM.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §2.2

La memoria virtual da a cada proceso un espacio de direcciones lógico propio y mayor que la RAM; la MMU traduce las direcciones y las partes no usadas quedan en disco (swap).

#### 5. Los indicadores del servidor muestran muchísimos fallos de página. ¿Qué significa cada uno?

- a) Que una página tiene un error de escritura y el SO debe reparar el disco.
- b) Que la MMU no puede traducir la dirección y el proceso se termina.
- c) Que la página solicitada no está en RAM y el SO debe traerla de disco.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §2.2

Un fallo de página se produce al acceder a una página que no está en RAM: el SO la trae de disco y, si no hay marcos libres, expulsa una víctima.

#### 6. Con tan poca RAM, el servidor pasa más tiempo intercambiando páginas con el disco que ejecutando procesos. ¿Cómo se llama este fenómeno?

- a) Interbloqueo (deadlock).
- b) Hiperpaginación (thrashing).
- c) Inanición (starvation).

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §2.2

Un exceso de fallos de página por falta de RAM provoca hiperpaginación: el sistema intercambia páginas en lugar de ejecutar y el rendimiento se desploma.

#### 7. Diagnosticada la hiperpaginación en el servidor de la sede, ¿qué medida la resuelve?

- a) Reducir el quantum de Round-Robin para que los procesos roten más rápido.
- b) Cambiar el planificador a FCFS para eliminar los cambios de contexto.
- c) Ampliar la RAM del servidor o reducir la carga que soporta.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §2.2

La hiperpaginación nace de la falta de memoria física, no de la planificación de la CPU: se corrige dando más RAM o reduciendo la carga.

#### 8. ¿Qué componente es el proceso PID 1 del servidor y gestiona el arranque y los servicios?

- a) systemd, que sustituyó al init tradicional de System V.
- b) El init de System V, con sus runlevels de 0 a 6.
- c) El VFS, que arranca los servicios del sistema.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §4.2, §4.3

En Linux moderno el primer proceso (PID 1) es systemd, que sustituyó al init de System V y gestiona los servicios como units.

#### 9. ¿Con qué órdenes comprueba y reinicia el técnico el servicio web Apache y consulta después sus registros?

- a) services.msc para reiniciarlo y el Visor de eventos para los registros.
- b) systemctl status/restart apache2 y, para los registros, journalctl.
- c) kill apache2 para reiniciarlo y df para consultar los registros.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §4.3

systemd se administra con systemctl (start, stop, enable, status, restart) y sus registros se consultan con journalctl; services.msc y el Visor de eventos son herramientas de Windows.

#### 10. Para una acción administrativa puntual sin trabajar permanentemente como root, ¿qué emplea el técnico y qué principio respeta?

- a) El comando su para abrir una sesión de root, conforme a la defensa en profundidad.
- b) Un chmod 777 sobre el fichero afectado, conforme al principio de mínimo privilegio.
- c) El comando sudo, controlado y auditado, conforme al principio de mínimo privilegio.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §4.6

sudo ejecuta órdenes puntuales con privilegios elevados de forma controlada y auditada, en lugar de trabajar siempre como root: es el mínimo privilegio.

### Caso 3. Dispositivos móviles corporativos

#### 1. ¿Qué mecanismo impide, tanto en Android como en iOS, que la app municipal de inspección lea los datos de otra aplicación del terminal?

- a) El Secure Enclave, que guarda por separado los datos de cada aplicación.
- b) La HAL, que reparte el almacenamiento entre las aplicaciones instaladas.
- c) El sandboxing, que aísla cada app con acceso solo a sus propios datos.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §5.1

El sandboxing ejecuta cada aplicación aislada, con acceso solo a sus propios datos y a los permisos concedidos. El Secure Enclave custodia claves y biometría.

#### 2. En las tabletas Android, ¿cómo se materializa ese aislamiento de cada aplicación?

- a) Todas las apps comparten un mismo usuario y se separan solo por permisos.
- b) Cada app se ejecuta con su propio UID de Linux.
- c) Cada app arranca su propio núcleo Linux independiente.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §5.2

En Android cada app se ejecuta aislada con su propio UID de Linux, reforzada además por SELinux.

#### 3. La app de inspección necesita la cámara y la ubicación. En Android, ¿cómo obtiene acceso a esos recursos sensibles?

- a) Mediante permisos por app concedidos en tiempo de ejecución y revocables.
- b) Mediante un permiso global del sistema que vale para todas las apps.
- c) Mediante la instalación, tras la cual el permiso ya no puede revocarse.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §5.2

Desde Android 6 los permisos sensibles (ubicación, cámara, micrófono, contactos) se conceden a cada app en tiempo de ejecución y son revocables.

#### 4. ¿En qué núcleo se basa cada sistema operativo de los terminales de los inspectores?

- a) Android en Darwin/XNU e iOS en el kernel Linux.
- b) Android en el kernel Linux e iOS en Darwin/XNU (Unix).
- c) Ambos en el microkernel MINIX, adaptado por cada fabricante.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §5.2, §5.3

Android se construye sobre el kernel Linux; iOS se basa en Darwin, cuyo núcleo es XNU (Mach + BSD).

#### 5. El servicio quiere publicar la app municipal en los terminales. ¿Qué diferencia de distribución de aplicaciones debe tener en cuenta?

- a) Que Android solo admite Google Play e iOS admite tiendas alternativas.
- b) Que ambas plataformas admiten tiendas alternativas sin restricciones.
- c) Que Android admite Google Play y tiendas alternativas; iOS, solo el App Store.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §5.4

Android es abierto y admite Google Play y tiendas alternativas; iOS es cerrado y su única vía de instalación es el App Store.

#### 6. Si el Ayuntamiento quiere comprar tabletas a varios fabricantes distintos, ¿qué plataforma lo permite y por qué?

- a) Android, porque es abierto (AOSP) y lo adaptan numerosos fabricantes.
- b) iOS, porque Apple licencia su sistema a otros fabricantes de tabletas.
- c) Cualquiera de las dos, porque ambas se distribuyen como código AOSP.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §5.2, §5.4

Android es de código abierto (AOSP) y multifabricante; iOS es cerrado y funciona solo en hardware de Apple.

#### 7. Para administrar de forma centralizada el cifrado, el PIN, las restricciones y la distribución de las apps municipales en todos los terminales, el técnico propone:

- a) Una consola WSUS que apruebe las apps y las políticas de los móviles.
- b) Una solución MDM (Mobile Device Management) en la que se inscriben los dispositivos.
- c) El Secure Enclave de cada terminal, configurado uno a uno por el técnico.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §5.4

Las soluciones MDM/EMM inscriben los dispositivos y aplican de forma centralizada políticas (cifrado, PIN, restricciones), distribución de apps y borrado remoto.

#### 8. Algunos inspectores usan la tableta también para fines personales. ¿Qué función del MDM permite proteger los datos municipales sin invadir lo personal?

- a) El borrado remoto periódico de todos los datos del terminal.
- b) La revocación de todos los permisos de las apps personales.
- c) La separación del perfil corporativo respecto del personal.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §5.4

Entre las funciones del MDM está separar el perfil corporativo del personal, de modo que las políticas y los datos municipales quedan aislados de lo privado.

#### 9. Un inspector pierde una tableta con datos de ciudadanos. ¿Qué medida técnica protege la información?

- a) El borrado remoto del terminal desde la plataforma MDM, además del cifrado.
- b) La desinstalación de la app municipal desde Google Play cuando aparezca.
- c) El cambio de la contraseña del inspector en el dominio Active Directory.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §5.4

La plataforma MDM permite borrar remotamente un terminal perdido o robado; junto con el cifrado del dispositivo, protege los datos del ciudadano.

#### 10. ¿Qué normativa exige proteger los datos de los ciudadanos de los terminales perdidos?

- a) La licencia GPL y el estándar POSIX.
- b) El ENS y la normativa de protección de datos.
- c) El ENI únicamente, por ser datos públicos.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §5.4 [ENS-RD311]

La gestión de los terminales corporativos y el borrado remoto responden al Esquema Nacional de Seguridad y a la normativa de protección de datos.
