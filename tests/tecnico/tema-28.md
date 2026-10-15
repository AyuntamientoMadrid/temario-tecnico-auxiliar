# Test del tema 28. Virtualización de sistemas y virtualización de puestos de usuario

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-28.html>

## Batería de preguntas

### 1. ¿Cuáles son las tres propiedades que Popek y Goldberg (1974) exigen a un monitor de máquina virtual?

- a) Equivalencia, control de recursos y eficiencia
- b) Portabilidad, escalabilidad y disponibilidad
- c) Aislamiento, cifrado y trazabilidad

**Respuesta correcta:** a) · **Referencia:** §1.1 [POPEK74]

La equivalencia exige que el programa se comporte igual que sobre hardware real; el control de recursos, que el monitor gobierne todo el hardware; y la eficiencia, que la mayoría de las instrucciones se ejecuten directamente en la CPU.

### 2. ¿Qué propiedad de Popek y Goldberg incumple un emulador y por eso no se considera un hipervisor?

- a) La equivalencia, porque el programa no se comporta igual
- b) La eficiencia, porque traduce cada instrucción en lugar de ejecutarla directamente
- c) El control de recursos, porque no aísla las máquinas entre sí

**Respuesta correcta:** b) · **Referencia:** §1.1 [POPEK74]

A cambio de incumplirla, el emulador puede ejecutar código de una arquitectura distinta a la del anfitrión, algo que un hipervisor no permite.

### 3. Según el teorema de virtualizabilidad, ¿cuándo es una arquitectura virtualizable de forma clásica?

- a) Cuando dispone de al menos cuatro anillos de privilegio
- b) Cuando su unidad de gestión de memoria admite paginación
- c) Cuando toda instrucción sensible es también privilegiada

**Respuesta correcta:** c) · **Referencia:** §1.1 [POPEK74] [ROBIN00]

Si se cumple, el monitor puede ejecutar el huésped sin privilegios y limitarse a atrapar y emular las excepciones. El x86 original no lo cumplía: tenía 17 instrucciones sensibles no privilegiadas.

### 4. ¿Dónde y cuándo nace la virtualización de sistemas tal como la conocemos?

- a) Con VMware sobre x86, a finales de los años noventa
- b) En los grandes sistemas de IBM en los años sesenta, con CP-67 y VM/370
- c) Con la aparición de Xen y la paravirtualización en 2003

**Respuesta correcta:** b) · **Referencia:** §1.1 [HIST-IBM] [ROBIN00]

El objetivo entonces era repartir en tiempo compartido un equipo carísimo. VMware y Xen resolvieron después el problema específico del x86, que era arquitectónico y no de potencia.

### 5. En la terminología de virtualización, ¿qué es el «anfitrión» (host)?

- a) La máquina física que aporta los recursos reales y ejecuta el hipervisor
- b) El sistema operativo virtualizado que se ejecuta dentro de una máquina virtual
- c) La consola centralizada desde la que se gestiona el clúster

**Respuesta correcta:** a) · **Referencia:** §1.1 [NIST-SP800-125]

El sistema operativo virtualizado es el huésped (guest) y la consola centralizada es el servidor de gestión.

### 6. ¿Qué caracteriza a la virtualización total o completa?

- a) El núcleo del huésped se modifica para emitir llamadas al hipervisor
- b) Exige obligatoriamente extensiones de virtualización en la CPU
- c) El huésped se instala sin modificar y no sabe que está virtualizado

**Respuesta correcta:** c) · **Referencia:** §1.2.1 [POPEK74] [ROBIN00]

Su implementación clásica en x86 combinaba ejecución directa del código de usuario con traducción binaria dinámica del código privilegiado del núcleo huésped.

### 7. ¿Cuál es el inconveniente principal de la paravirtualización del núcleo?

- a) Ofrece un rendimiento inferior al de la traducción binaria
- b) Impide utilizar controladores de dispositivo eficientes
- c) Exige modificar el núcleo del sistema huésped, lo que descarta los sistemas cerrados

**Respuesta correcta:** c) · **Referencia:** §1.2.2 [XEN-DOC]

Su rendimiento es precisamente superior al de la traducción binaria, pero solo puede aplicarse a sistemas cuyo código pueda adaptarse.

### 8. En la arquitectura de Xen, ¿qué es <code>dom0</code>?

- a) La máquina virtual privilegiada, con controladores reales, desde la que se administra el sistema
- b) El identificador del hipervisor dentro de la estructura de control de la CPU
- c) El dominio de red por defecto al que se conectan las máquinas virtuales

**Respuesta correcta:** a) · **Referencia:** §1.2.2 [XEN-DOC]

Las máquinas virtuales no privilegiadas de los usuarios se denominan <code>domU</code>.

### 9. ¿Qué aportan las extensiones Intel VT-x y AMD-V a la virtualización?

- a) Duplican el número de núcleos disponibles para las máquinas virtuales
- b) Añaden un modo de ejecución adicional para el hipervisor, de modo que el huésped conserva su anillo 0 sin traducción binaria
- c) Cifran la memoria de cada máquina virtual con una clave distinta

**Respuesta correcta:** b) · **Referencia:** §1.2.3 [INTEL-SDM] [AMD-APM]

Intel lo articula con los modos VMX raíz y no raíz y la estructura VMCS; AMD, con SVM y la estructura VMCB.

### 10. ¿Qué problema resuelven las tablas de páginas extendidas (EPT) o anidadas (NPT)?

- a) La doble traducción de memoria, que antes exigía mantener por software costosas tablas de páginas sombra
- b) El acceso directo a memoria de los dispositivos asignados a una máquina virtual
- c) La compatibilidad de CPU entre anfitriones para permitir la migración en caliente

**Respuesta correcta:** a) · **Referencia:** §1.2.3 [INTEL-SDM] [AMD-APM]

El acceso directo a memoria de los dispositivos lo resuelve la IOMMU (VT-d / AMD-Vi), que es un mecanismo distinto.

### 11. ¿Cuál es el requisito imprescindible para asignar directamente un dispositivo físico a una máquina virtual (passthrough)?

- a) Que el huésped esté paravirtualizado
- b) Que el dispositivo admita SR-IOV
- c) Que la plataforma disponga de IOMMU (Intel VT-d o AMD-Vi)

**Respuesta correcta:** c) · **Referencia:** §1.2.3 y §2.2.2 [INTEL-VTD] [PCI-SRIOV]

Sin ella, el dispositivo podría leer y escribir por acceso directo toda la memoria del anfitrión. SR-IOV es una evolución que además permite repartir el dispositivo, pero no es requisito de la asignación directa simple.

### 12. ¿Cómo se clasifica KVM y por qué?

- a) De Tipo 2, porque se ejecuta sobre un sistema operativo Linux completo
- b) De Tipo 1, porque es un módulo que convierte al propio núcleo de Linux en hipervisor con acceso directo al hardware
- c) No es un hipervisor, sino un emulador de dispositivos

**Respuesta correcta:** b) · **Referencia:** §1.3.1 [KVM-DOC] [HYPERV-DOC]

Lo mismo sucede con Hyper-V: al habilitar el rol, el hipervisor se sitúa por debajo del sistema, que pasa a ser una partición privilegiada.

### 13. ¿Qué es OVF/OVA en un entorno de virtualización?

- a) Un formato de disco virtual con aprovisionamiento fino e instantáneas internas
- b) Un formato abierto de empaquetado e intercambio de máquinas virtuales, no un formato de disco
- c) El protocolo de comunicación entre el hipervisor y la consola de gestión

**Respuesta correcta:** b) · **Referencia:** §2.1 [VMWARE-DOC]

Combina un descriptor XML con los discos de la máquina; OVA es ese mismo contenido en un único fichero. Formatos de disco son VMDK, VHD/VHDX, QCOW2 y RAW.

### 14. ¿Por qué una instantánea (snapshot) no es una copia de seguridad?

- a) Porque solo guarda la memoria y nunca el disco de la máquina virtual
- b) Porque el hipervisor la elimina automáticamente cada 24 horas
- c) Porque reside en el mismo almacenamiento que la máquina y sus ficheros delta crecen degradando el rendimiento

**Respuesta correcta:** c) · **Referencia:** §2.1 [VMWARE-DOC]

Si se pierde la cabina se pierden también las instantáneas. Sirven para revertir un cambio a corto plazo, no para proteger datos.

### 15. ¿Cuál es el riesgo específico del aprovisionamiento fino (thin provisioning)?

- a) Que la suma de lo comprometido supere la capacidad real y, al llenarse el almacén, las máquinas virtuales se detengan
- b) Que el rendimiento de lectura sea siempre inferior al del aprovisionamiento grueso
- c) Que impida tomar instantáneas de la máquina virtual

**Respuesta correcta:** a) · **Referencia:** §2.1 [VMWARE-DOC]

Por eso el sobreaprovisionamiento exige vigilancia activa del espacio libre del almacén de datos.

### 16. En cuanto a la sobreasignación de recursos, ¿qué afirmación es correcta?

- a) Sobreasignar CPU degrada el servicio con esperas, mientras que sobreasignar memoria puede llegar a romperlo
- b) La memoria es el recurso que más margen de sobreasignación admite sin consecuencias
- c) La sobreasignación está desaconsejada en todos los recursos por igual

**Respuesta correcta:** a) · **Referencia:** §2.2 [VMWARE-DOC]

Cuando falta CPU las máquinas esperan turno; cuando falta memoria el hipervisor acaba recurriendo al intercambio a disco, que hunde el rendimiento.

### 17. ¿Qué expresa la métrica de tiempo de espera de CPU (CPU ready o <code>%RDY</code>)?

- a) El porcentaje de tiempo que la CPU física permanece ociosa
- b) El porcentaje de tiempo que una vCPU está lista para ejecutarse pero espera un núcleo libre
- c) La latencia media de las operaciones de disco de la máquina virtual

**Respuesta correcta:** b) · **Referencia:** §2.2.1 [VMWARE-DOC]

Es el indicador de contención de CPU por excelencia: puede ser alto aunque la utilización global del anfitrión no parezca extrema.

### 18. ¿Qué efecto tiene asignar a una máquina virtual más vCPU de las que necesita?

- a) Ninguno: el hipervisor ignora las vCPU que no se usan
- b) Mejora siempre el rendimiento, porque dispone de más capacidad de reserva
- c) Empeora el rendimiento, porque el planificador debe encontrar hueco para más entidades y aumenta el tiempo de espera

**Respuesta correcta:** c) · **Referencia:** §2.2.1 [VMWARE-DOC]

Perjudica además a las máquinas vecinas del mismo anfitrión. La regla es empezar corto y crecer con datos de monitorización.

### 19. Ordene de menos a más dañina las técnicas de recuperación de memoria del hipervisor.

- a) Intercambio a disco, compresión, globo y compartición de páginas
- b) Globo, compartición de páginas, intercambio a disco y compresión
- c) Compartición de páginas idénticas, globo, compresión e intercambio a disco

**Respuesta correcta:** c) · **Referencia:** §2.2.1 [VMWARE-DOC] [KVM-DOC]

La aparición de intercambio del hipervisor a disco es siempre señal de un problema de dimensionamiento, porque el hipervisor elige a ciegas qué página sacrificar.

### 20. ¿En qué consiste la técnica del globo de memoria (ballooning)?

- a) Un controlador instalado en el huésped reclama memoria dentro de él, forzándole a liberar sus páginas menos usadas para devolverlas al hipervisor
- b) El hipervisor comprime las páginas menos usadas y las guarda en una caché en memoria
- c) El hipervisor duplica la memoria asignada a la máquina virtual durante los picos de carga

**Respuesta correcta:** a) · **Referencia:** §2.2.1 [VMWARE-DOC]

Su virtud es que la decisión de qué página sacrificar la toma el huésped, que es quien mejor conoce su propio uso de memoria.

### 21. ¿Qué es virtio?

- a) Un formato de disco virtual propio del ecosistema KVM
- b) Un estándar abierto de dispositivos paravirtualizados de entrada/salida, con controladores como virtio-net y virtio-blk
- c) El protocolo de representación remota usado por los escritorios virtuales de Red Hat

**Respuesta correcta:** b) · **Referencia:** §2.2.2 [VIRTIO]

Es paravirtualización aplicada a los dispositivos, no al núcleo, y por eso sigue plenamente vigente aunque la paravirtualización del núcleo esté desplazada. El protocolo de representación de Red Hat es SPICE.

### 22. ¿Qué distingue a SR-IOV de la asignación directa simple de un dispositivo?

- a) No necesita IOMMU, a diferencia de la asignación directa
- b) Conserva íntegramente la posibilidad de migrar la máquina virtual en caliente
- c) Presenta el dispositivo como una función física y varias funciones virtuales, repartibles entre distintas máquinas virtuales

**Respuesta correcta:** c) · **Referencia:** §2.2.2 [PCI-SRIOV]

Sigue necesitando IOMMU y mantiene, en general, las mismas restricciones de movilidad que la asignación directa.

### 23. ¿Qué modelo de entrada/salida es el habitual por defecto en producción?

- a) El dispositivo paravirtualizado, por combinar rendimiento alto con portabilidad y migración en caliente
- b) La emulación completa, por no exigir controladores en el huésped
- c) La asignación directa, por ofrecer rendimiento nativo

**Respuesta correcta:** a) · **Referencia:** §2.2.2 [VIRTIO] [VMWARE-DOC]

La emulación se reserva a la instalación y a huéspedes antiguos, y la asignación directa a casos concretos que justifiquen perder la movilidad.

### 24. ¿Qué primitivas del núcleo Linux sustentan el aislamiento de un contenedor?

- a) Las tablas de páginas extendidas y la IOMMU
- b) Los espacios de nombres (namespaces) y los grupos de control (cgroups)
- c) Los anillos de privilegio y la traducción binaria

**Respuesta correcta:** b) · **Referencia:** §2.3 [LINUX-NS] [OCI-SPEC]

Los primeros aíslan qué ve el proceso (procesos, red, montajes, identificadores) y los segundos limitan cuánto consume. Se complementan con capacidades, seccomp y módulos de seguridad como SELinux o AppArmor.

### 25. ¿Cuál es la diferencia fundamental entre una máquina virtual y un contenedor?

- a) El contenedor arranca más rápido, pero por lo demás son equivalentes
- b) La máquina virtual solo admite sistemas de código abierto y el contenedor cualquiera
- c) La máquina virtual virtualiza el hardware y lleva su propio núcleo; el contenedor virtualiza el sistema operativo y comparte el núcleo del anfitrión

**Respuesta correcta:** c) · **Referencia:** §2.3.1 [NIST-SP800-190]

De ahí se derivan todas las demás diferencias: tamaño, tiempo de arranque, densidad, aislamiento y sistemas operativos admitidos.

### 26. ¿Puede un contenedor ejecutar un sistema operativo distinto del núcleo del anfitrión?

- a) No: al compartir el núcleo, solo puede ejecutar el mismo sistema; cuando parece lo contrario, hay una máquina virtual ligera por debajo
- b) Sí, porque el motor de contenedores traduce las llamadas al sistema
- c) Sí, siempre que la CPU disponga de extensiones de virtualización

**Respuesta correcta:** a) · **Referencia:** §2.3.1 [NIST-SP800-190]

Es el caso de los contenedores Linux ejecutados sobre un equipo con otro sistema operativo.

### 27. ¿Cuál es el riesgo de seguridad más característico de los contenedores frente a las máquinas virtuales?

- a) La imposibilidad de aplicar control de acceso basado en roles
- b) Que una escalada de privilegios en el núcleo compartido permita escapar del contenedor y afectar al anfitrión y a sus vecinos
- c) Que no admitan cifrado del almacenamiento persistente

**Respuesta correcta:** b) · **Referencia:** §2.3 y §2.3.1 [NIST-SP800-190]

Es la diferencia de aislamiento esencial, y la razón por la que existen los contenedores aislados por hipervisor.

### 28. ¿Qué diferencia una política de alta disponibilidad (HA) de la tolerancia a fallos (FT)?

- a) HA se aplica a eventos planificados y FT a eventos imprevistos
- b) HA reinicia la máquina virtual en otro anfitrión, con corte y pérdida del estado en memoria; FT mantiene una copia en espejo sincronizada y conmuta sin corte
- c) HA exige almacenamiento compartido y FT no lo necesita

**Respuesta correcta:** b) · **Referencia:** §2.4 [VMWARE-DOC]

Ambas responden a eventos imprevistos; la planificada sin corte es la migración en caliente. FT duplica el consumo de recursos y se reserva a servicios críticos.

### 29. En la migración en caliente por precopia iterativa, ¿cuándo se detiene la máquina virtual?

- a) Solo en una parada final de milisegundos, para transferir las últimas páginas sucias y el estado de CPU y dispositivos
- b) Durante toda la transferencia de memoria, que dura varios segundos
- c) No se detiene en ningún momento, ni siquiera brevemente

**Respuesta correcta:** a) · **Referencia:** §2.4 [VMWARE-DOC] [KVM-DOC]

El grueso de la memoria se copia mientras la máquina sigue funcionando en el origen, repitiendo pasadas sobre las páginas que se van ensuciando.

### 30. ¿Cuál de los siguientes NO es un requisito de la migración en caliente?

- a) Compatibilidad de CPU entre el anfitrión de origen y el de destino
- b) Acceso de ambos anfitriones al mismo almacenamiento (o migración simultánea del disco)
- c) Que la máquina virtual tenga un dispositivo asignado directamente en passthrough

**Respuesta correcta:** c) · **Referencia:** §2.4 [VMWARE-DOC] [PCI-SRIOV]

Es justamente lo contrario: un dispositivo asignado directamente ata la máquina al hardware del origen y, por regla general, impide la migración en caliente.

### 31. ¿Para qué sirve una regla de antiafinidad en un clúster de virtualización?

- a) Para impedir que dos máquinas virtuales concretas se ejecuten en el mismo anfitrión, evitando que un par redundante caiga junto
- b) Para forzar que dos máquinas virtuales se ejecuten siempre en el mismo anfitrión y reducir la latencia entre ellas
- c) Para excluir a un anfitrión del balanceo automático de carga

**Respuesta correcta:** a) · **Referencia:** §2.4 [VMWARE-DOC]

Forzar la coincidencia es la regla de afinidad, que es la contraria.

### 32. ¿Qué permite el modo mantenimiento de un anfitrión?

- a) Suspender temporalmente las copias de seguridad de sus máquinas virtuales
- b) Aplicar parches al sistema huésped sin reiniciarlo
- c) Vaciar automáticamente y en caliente todas sus máquinas virtuales hacia otros nodos antes de intervenir el equipo

**Respuesta correcta:** c) · **Referencia:** §2.4 [VMWARE-DOC]

Es la razón por la que, en un entorno virtualizado bien diseñado, el mantenimiento del hardware deja de requerir ventanas de parada del servicio.

### 33. ¿Qué define a la infraestructura de escritorios virtuales (VDI)?

- a) Un único sistema operativo de servidor que atiende muchas sesiones de usuario simultáneas
- b) Una máquina virtual con sistema operativo de cliente por usuario, ejecutada en el centro de datos y consumida en remoto
- c) La entrega de aplicaciones empaquetadas en burbujas aisladas sobre el equipo del usuario

**Respuesta correcta:** b) · **Referencia:** §3.1.1 [HORIZON-DOC] [CITRIX-DOC]

La opción A describe los escritorios basados en sesiones (RDSH) y la C, la virtualización de aplicaciones.

### 34. ¿Qué diferencia hay entre un cliente ligero y VDI?

- a) El cliente ligero es el dispositivo terminal del usuario; VDI es la arquitectura del lado del servidor
- b) Son sinónimos: cliente ligero es el nombre comercial de VDI
- c) El cliente ligero exige VDI, mientras que VDI puede prescindir de cualquier terminal

**Respuesta correcta:** a) · **Referencia:** §3.1 [HORIZON-DOC]

Se puede hacer VDI con clientes ligeros, con clientes cero, con PC reutilizados o con un simple navegador HTML5.

### 35. ¿Qué es una tormenta de arranque (boot storm) en VDI?

- a) Un ataque de denegación de servicio contra el broker de conexiones
- b) El pico simultáneo de entrada/salida que se produce cuando cientos de escritorios arrancan y cargan perfiles a la misma hora
- c) La saturación del enlace de red provocada por la migración masiva de escritorios entre anfitriones

**Respuesta correcta:** b) · **Referencia:** §3.1.1 [HORIZON-DOC] [CITRIX-DOC]

Se mitiga con almacenamiento de estado sólido, encendido escalonado y preencendido, cachés de la imagen maestra, clones instantáneos y análisis antivirus desfasado en el tiempo.

### 36. En un modelo de escritorios basados en sesiones (RDSH), ¿qué ocurre?

- a) Cada usuario dispone de su propia máquina virtual con sistema operativo de cliente
- b) Cada usuario recibe una copia de la imagen maestra que se descarta al cerrar sesión
- c) Un único sistema operativo de servidor atiende simultáneamente a muchos usuarios, cada uno en su sesión

**Respuesta correcta:** c) · **Referencia:** §3.1.2 [AVD-DOC]

Por eso su densidad y su coste por puesto son mucho mejores que los de VDI, a costa de un aislamiento menor y de una personalización limitada.

### 37. ¿Cuál es la principal desventaja del modelo de escritorios por sesiones frente a VDI?

- a) Que exige un sistema operativo de cliente por usuario, lo que dispara el coste
- b) Que el aislamiento es menor: un proceso descontrolado o un cuelgue afecta a todos los usuarios de ese servidor
- c) Que impide publicar aplicaciones individuales

**Respuesta correcta:** b) · **Referencia:** §3.1.2 [AVD-DOC]

Además, la compatibilidad es la del sistema operativo de servidor y no se puede instalar software por usuario. La publicación de aplicaciones individuales es precisamente una de sus capacidades.

### 38. ¿Qué problema resuelve de forma característica la virtualización de aplicaciones?

- a) La convivencia en un mismo puesto de versiones incompatibles de la misma aplicación, cada una en su burbuja aislada
- b) La necesidad de disponer de un sistema operativo de servidor para publicar escritorios
- c) La imposibilidad de migrar en caliente una máquina virtual con dispositivos asignados

**Respuesta correcta:** a) · **Referencia:** §3.1.3 [APPV]

Aporta además despliegue y retirada limpios, entrega bajo demanda y actualización centralizada del paquete.

### 39. ¿Cuál es una limitación reconocida de la virtualización de aplicaciones?

- a) Obliga a que el puesto del usuario sea un escritorio virtual y no un equipo físico
- b) Impide actualizar la aplicación sin reinstalarla en cada puesto
- c) No toda aplicación es virtualizable: las que instalan controladores en modo núcleo o servicios de sistema profundos suelen quedar fuera

**Respuesta correcta:** c) · **Referencia:** §3.1.3 [APPV]

A ello se añade el coste de trabajo técnico y de pruebas del empaquetado inicial.

### 40. ¿Cuál de estas funciones NO corresponde al broker de conexiones de una plataforma VDI?

- a) Autenticar al usuario y comprobar sus autorizaciones
- b) Transportar el flujo del protocolo de representación durante toda la sesión
- c) Seleccionar o encender el escritorio y redirigir hacia él al cliente

**Respuesta correcta:** b) · **Referencia:** §3.2.1 [CITRIX-DOC] [HORIZON-DOC]

El broker interviene en el establecimiento, no en el tráfico: una vez asignado el escritorio, el protocolo fluye directamente entre el cliente y el escritorio, o a través de la pasarela.

### 41. ¿Qué consecuencia tiene la indisponibilidad del broker de conexiones?

- a) No pueden abrirse sesiones nuevas, aunque las sesiones ya establecidas sigan funcionando
- b) Todos los escritorios virtuales se apagan de inmediato
- c) Las sesiones existentes pierden la conexión y los datos no guardados

**Respuesta correcta:** a) · **Referencia:** §3.2.1 [CITRIX-DOC]

Al ser un punto único de fallo, se despliega siempre redundado y balanceado, con su base de datos en alta disponibilidad.

### 42. ¿Qué caracteriza a un clon instantáneo (instant clone) frente a un clon enlazado?

- a) Que cada escritorio recibe una copia completa e independiente de la plantilla
- b) Que el escritorio arranca desde la red sin disco propio
- c) Que se deriva de una máquina plantilla ya arrancada en memoria, por lo que está disponible en segundos y comparte también páginas de memoria

**Respuesta correcta:** c) · **Referencia:** §3.2.2 [HORIZON-DOC]

Es una de las mejores mitigaciones de la tormenta de arranque en conjuntos no persistentes grandes.

### 43. ¿Cuál de estos protocolos de representación remota está definido en un RFC del IETF?

- a) ICA/HDX
- b) PCoIP
- c) RFB, el protocolo en el que se basa VNC

**Respuesta correcta:** c) · **Referencia:** §3.3 [RFC6143] [MS-RDPBCGR]

Está publicado como RFC 6143. ICA/HDX es de Citrix y PCoIP de Teradici/HP; RDP, aunque es de Microsoft, cuenta con especificación abierta publicada.

### 44. En una plataforma VDI, ¿qué factor de red determina más la calidad percibida por el usuario?

- a) Exclusivamente el ancho de banda bruto del enlace
- b) La latencia de ida y vuelta y su estabilidad, más que el ancho de banda bruto
- c) El número de saltos de encaminamiento hasta el centro de datos

**Respuesta correcta:** b) · **Referencia:** §3.3 [CITRIX-DOC] [PCOIP]

Un enlace de gran caudal pero con latencia alta o fluctuante ofrece una experiencia peor que uno modesto y estable.

### 45. ¿Qué exige inevitablemente el modelo de escritorio no persistente?

- a) Gestionar el perfil y los datos del usuario fuera del escritorio, con contenedor de perfil y redirección de carpetas
- b) Asignar a cada usuario un escritorio fijo con clones completos
- c) Renunciar a la aplicación de directivas de configuración

**Respuesta correcta:** a) · **Referencia:** §3.4 [FSLOGIX]

Como el escritorio se descarta al cerrar sesión, todo lo que no esté en la imagen o en el perfil externo se pierde.

### 46. ¿Cuál es la principal ventaja operativa del escritorio no dedicado frente al dedicado?

- a) Que permite a cada usuario instalar su propio software
- b) Que se gestiona y se parchea una sola imagen maestra en lugar de escritorio por escritorio
- c) Que elimina la necesidad de disponer de un broker de conexiones

**Respuesta correcta:** b) · **Referencia:** §3.4 [HORIZON-DOC] [CITRIX-DOC]

A ello se suman un ahorro de almacenamiento muy notable y un escritorio siempre limpio en cada inicio de sesión.

### 47. ¿Qué caracteriza a una infraestructura hiperconvergente (HCI)?

- a) Que los discos residen en los propios nodos de cómputo y un software distribuido los agrega y replica presentando un almacén único
- b) Que separa el cómputo de una cabina externa mediante una red de almacenamiento dedicada
- c) Que sustituye el hipervisor por un motor de contenedores

**Respuesta correcta:** a) · **Referencia:** §4.1 [VMWARE-DOC] [HYPERV-DOC]

El crecimiento se produce añadiendo nodos, con lo que cómputo y almacenamiento escalan juntos.

### 48. ¿Por qué encaja especialmente bien la hiperconvergencia con VDI?

- a) Porque elimina la necesidad de proteger los datos con réplicas
- b) Porque permite prescindir del broker de conexiones
- c) Porque atiende con almacenamiento local rápido un patrón de entrada/salida muy exigente y muy repetitivo, deduplicable entre escritorios casi idénticos

**Respuesta correcta:** c) · **Referencia:** §4.1 [VMWARE-DOC]

Además, su crecimiento por nodos encaja con un despliegue VDI que se amplía por bloques de usuarios.

### 49. ¿Cuántos segmentos permite identificar VXLAN y sobre qué protocolo encapsula?

- a) 4.094 segmentos, encapsulando sobre TCP
- b) Unos 16 millones de segmentos mediante un identificador VNI de 24 bits, encapsulando sobre UDP
- c) 65.535 segmentos, encapsulando sobre GRE

**Respuesta correcta:** b) · **Referencia:** §4.2 [RFC7348]

Los 4.094 segmentos son el límite de la VLAN 802.1Q, con identificador de 12 bits, que VXLAN viene precisamente a superar.

### 50. ¿En qué consiste la arquitectura SDN?

- a) En sustituir los conmutadores físicos por conmutadores virtuales alojados en los anfitriones
- b) En encapsular tramas de nivel 2 dentro de paquetes de nivel 3
- c) En separar el plano de control del plano de datos, concentrando el primero en un controlador centralizado y programable

**Respuesta correcta:** c) · **Referencia:** §4.2 [ONF-SDN]

Se articula con una interfaz norte hacia las aplicaciones y una interfaz sur hacia los dispositivos, siendo OpenFlow el protocolo histórico de referencia para esta última.

### 51. ¿Qué protege la microsegmentación que un cortafuegos perimetral no puede proteger?

- a) El tráfico este-oeste entre servidores dentro del propio centro de datos, que nunca atraviesa el perímetro
- b) El tráfico cifrado con TLS procedente de Internet
- c) El acceso físico a los armarios del centro de proceso de datos

**Respuesta correcta:** a) · **Referencia:** §4.2 [NIST-SP800-125]

Es precisamente el que un atacante utiliza para moverse lateralmente tras comprometer un primer sistema.

### 52. ¿Qué es la proliferación descontrolada de máquinas virtuales (VM sprawl) y por qué preocupa?

- a) Es la migración automática excesiva de máquinas entre anfitriones, que satura la red de migración
- b) Es la acumulación de máquinas, plantillas e instantáneas que nadie da de baja, consumiendo licencias, almacenamiento y superficie de ataque sin parchear
- c) Es el crecimiento de los discos con aprovisionamiento fino por encima de lo previsto

**Respuesta correcta:** b) · **Referencia:** §4.3 [NIST-SP800-125]

Sus contramedidas son de gestión: etiquetado obligatorio con responsable y finalidad, fecha de caducidad de los entornos temporales, revisión periódica y procedimiento formal de baja.

### 53. ¿Cuáles son las cinco dimensiones de seguridad del Esquema Nacional de Seguridad?

- a) Confidencialidad, integridad, disponibilidad, eficiencia y sostenibilidad
- b) Prevención, detección, respuesta, recuperación y mejora continua
- c) Disponibilidad, integridad, confidencialidad, autenticidad y trazabilidad

**Respuesta correcta:** c) · **Referencia:** §5.1 [ENS]

Se recuerdan con las siglas D-I-C-A-T. Prevención, detección, respuesta y conservación son principios básicos, no dimensiones.

### 54. Según el Real Decreto 311/2022, ¿con qué periodicidad deben auditarse los sistemas de categoría media y alta?

- a) Al menos cada dos años, mediante auditoría ordinaria
- b) Anualmente, mediante autoevaluación
- c) Solo cuando se produzca un cambio sustancial en el sistema

**Respuesta correcta:** a) · **Referencia:** §5.1 [ENS]

Los sistemas de categoría básica pueden acreditar su conformidad mediante autoevaluación y la correspondiente declaración.

### 55. ¿Cuál es la buena práctica de seguridad respecto a la red de gestión de un entorno virtualizado?

- a) Compartirla con la red de máquinas virtuales para simplificar el direccionamiento
- b) Publicarla a través de la pasarela de acceso seguro para permitir la administración desde Internet
- c) Mantenerla separada de los demás flujos y nunca accesible desde la red de usuarios

**Respuesta correcta:** c) · **Referencia:** §5.1 [NIST-SP800-125] [ENS]

Es una recomendación expresa del NIST, y en el entorno de un ayuntamiento resulta exigible por la vía de las medidas de separación de flujos y de control de accesos del ENS.

### 56. ¿Por qué el compromiso del plano de gestión es tan grave en un entorno virtualizado?

- a) Porque impide aplicar parches al hipervisor hasta que se restablezca
- b) Porque quien controla la consola controla todas las máquinas virtuales sin necesidad de entrar en ninguna de ellas
- c) Porque provoca automáticamente el escape de las máquinas virtuales hacia el anfitrión

**Respuesta correcta:** b) · **Referencia:** §5.1 [NIST-SP800-125]

Es, en la práctica, el vector más rentable para un atacante, y por eso exige acceso nominal, autenticación reforzada, mínimo privilegio y registro de actividad externo.

### 57. ¿Qué exige el artículo 32 del RGPD que afecta directamente a la política de copias de un entorno virtualizado?

- a) La capacidad de restaurar la disponibilidad y el acceso a los datos tras un incidente, y la verificación periódica de la eficacia de las medidas
- b) La conservación de las copias durante un mínimo de cinco años
- c) El almacenamiento de las copias exclusivamente en soporte cifrado extraíble

**Respuesta correcta:** a) · **Referencia:** §5.2 y §5.3 [RGPD]

Es el fundamento jurídico directo de las pruebas de restauración documentadas; el artículo cita además la seudonimización y el cifrado.

### 58. Se solicita un clon de la máquina virtual del padrón para un entorno de pruebas. ¿Cuál es la actuación correcta?

- a) Clonarla tal cual, ya que se trata del mismo responsable del tratamiento
- b) Aplicar el principio de minimización, clonando con datos seudonimizados o sintéticos, con autorización registrada, mismas medidas de seguridad y fecha de destrucción
- c) Denegar cualquier copia, porque los datos del padrón no pueden salir de producción bajo ningún concepto

**Respuesta correcta:** b) · **Referencia:** §5.2 [RGPD] [LOPDGDD]

Un clon de producción olvidado en un entorno menos protegido es uno de los orígenes más frecuentes de brecha de datos.

### 59. ¿Qué diferencia el RTO del RPO?

- a) El RTO mide los datos perdidos y el RPO el tiempo de restablecimiento
- b) Ambos miden lo mismo, pero el RTO se expresa en horas y el RPO en minutos
- c) El RTO es el tiempo máximo tolerable hasta restablecer el servicio y el RPO la cantidad máxima tolerable de datos perdidos

**Respuesta correcta:** c) · **Referencia:** §5.3 [NIST-SP800-34]

El RTO mira hacia delante y el RPO hacia atrás; ambos los fija el análisis de impacto en el negocio, no la decisión técnica.

### 60. ¿Cómo se calcula el indicador PUE de un centro de datos y qué valor es el óptimo?

- a) Energía total del centro de datos dividida entre la energía del equipamiento TI; el óptimo teórico es 1,0
- b) Energía del equipamiento TI dividida entre la energía total; el óptimo es el valor más alto posible
- c) Número de máquinas virtuales por anfitrión; el óptimo depende del perfil de carga

**Respuesta correcta:** a) · **Referencia:** §5.4 [ISO30134]

Está definido en la norma ISO/IEC 30134-2. Cuidado: un PUE bajo mide la eficiencia de la instalación, no si los servidores están bien aprovechados, así que debe leerse junto con la utilización real. La opción C describe la ratio de consolidación.

## Preguntas sobre los casos prácticos

### Caso 1. Consolidación del centro de proceso de datos municipal

#### 1. La utilización media de los 34 servidores es del 11 % de CPU. ¿Qué ventaja de la virtualización explota directamente ese dato?

- a) La consolidación: agrupar máquinas virtuales en pocos anfitriones eleva la utilización.
- b) La emulación: ejecutar en x86 aplicaciones escritas para otra arquitectura de procesador.
- c) La tolerancia a fallos: duplicar cada servidor en otro anfitrión sincronizado.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §1.1

Un servidor dedicado a una sola aplicación opera muy por debajo de su capacidad; agrupar varias máquinas virtuales reduce drásticamente el número de equipos.

#### 2. La consolidación concentra el riesgo: la caída de un anfitrión afecta a muchos servicios. ¿Cuál es su contramedida?

- a) Asignar más vCPU de las necesarias a cada máquina, para que absorba los picos.
- b) Un clúster con capacidad N+1, alta disponibilidad (HA) y reglas de antiafinidad.
- c) Desactivar la HA, para que un fallo no arrastre las máquinas a otro anfitrión.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §1.1

Si un anfitrión soporta muchas máquinas virtuales, su caída afecta a todos sus servicios; el clúster debe poder perder un nodo.

#### 3. Cada anfitrión tiene 32 núcleos físicos y se toma una ratio de 4 vCPU por núcleo. ¿Qué resulta para las 96 vCPU necesarias?

- a) 32 vCPU asignables por anfitrión: por CPU harían falta tres.
- b) 256 vCPU por anfitrión, porque el multihilo duplica los núcleos útiles.
- c) 128 vCPU asignables por anfitrión: por CPU bastaría con uno solo.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.2

32 núcleos × 4 = 128 vCPU por anfitrión; el multihilo simultáneo no duplica la capacidad real.

#### 4. Sin sobreasignar memoria, ¿cuántos anfitriones hacen falta para los 680 GB y qué recurso limita el dimensionamiento?

- a) Dos anfitriones: el recurso limitante es la CPU, por las 96 vCPU.
- b) Dos anfitriones (680 / 512 = 1,33): el recurso limitante es la memoria.
- c) Uno: sobreasignando la memoria no hay ningún recurso limitante.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.2.1

La memoria es el recurso que de verdad limita la densidad de un anfitrión; por CPU bastaba uno.

#### 5. Aplicando la regla N+1, ¿cuántos anfitriones debe tener el clúster?

- a) Tres: los dos que exige la memoria más uno de reserva.
- b) Dos: la regla N+1 ya está incluida en el redondeo de 1,33 a 2.
- c) Cuatro: uno por cada procesador de los dos anfitriones necesarios.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §2.4

N+1 dimensiona el clúster para perder un nodo: con tres, la caída de uno deja 1.024 GB para los 680 GB comprometidos.

#### 6. ¿Qué mecanismo permite parchear el hardware de un anfitrión sin parar el padrón ni el registro?

- a) Apagar las máquinas, moverlas en frío a otro anfitrión y arrancarlas allí de madrugada.
- b) La alta disponibilidad (HA), que reinicia las máquinas en otro anfitrión sin ningún corte.
- c) El modo mantenimiento, que vacía el anfitrión migrando sus máquinas en caliente.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §2.4

La migración en caliente usa precopia iterativa de memoria y solo detiene la máquina unos milisegundos; la HA, en cambio, reinicia y sí implica corte.

#### 7. ¿Qué circunstancia impide migrar en caliente una máquina virtual al vaciar el anfitrión?

- a) Usar controladores paravirtualizados virtio para la red y el disco.
- b) Tener más vCPU asignadas que núcleos físicos tiene el anfitrión de destino.
- c) Tener un dispositivo asignado directamente (passthrough o SR-IOV).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §2.4

Los requisitos son CPU compatible, red compartida y de migración, almacenamiento común y ausencia de dispositivos en passthrough o SR-IOV.

#### 8. ¿Qué protege al par redundante del registro frente a la caída de un único servidor físico?

- a) Una regla de antiafinidad, que impide que los dos nodos se ejecuten en el mismo anfitrión.
- b) Una regla de afinidad, que los mantiene en el mismo anfitrión para reducir su latencia.
- c) La migración en caliente, que los traslada antes de que el anfitrión llegue a fallar.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §2.4

La antiafinidad es imprescindible para los pares redundantes; la HA reinicia después las máquinas ante un fallo no planificado, con corte.

#### 9. ¿Qué mide el PUE y cuál es su limitación?

- a) Energía del equipamiento TI entre energía total; cuanto más alto, más eficiente es el centro de datos.
- b) Energía total del centro entre energía del equipamiento TI; no dice si los servidores están bien aprovechados.
- c) La ratio de máquinas virtuales por anfitrión; no tiene en cuenta el consumo de la refrigeración.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §5.4

El óptimo teórico es 1,0; un centro con PUE excelente lleno de servidores ociosos sigue derrochando, por eso se lee junto con la utilización real.

#### 10. ¿Por qué elevar la utilización media de los anfitriones es una palanca de ahorro energético?

- a) Porque el consumo de un servidor no es proporcional a su carga: tiene un consumo de base considerable.
- b) Porque un servidor al 11 % de carga consume el 11 % de su potencia máxima, y al subirla se ahorra.
- c) Porque los anfitriones muy cargados desactivan solos la refrigeración de la sala.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §5.4

Un servidor casi ocioso consume una fracción muy elevada de su potencia máxima; pocos servidores bien utilizados consumen menos que muchos infrautilizados.

### Caso 2. Diseño del puesto de trabajo virtual para las oficinas de atención a la ciudadanía

#### 1. ¿Qué modelo conviene a los 700 usuarios de mostrador, con cuatro aplicaciones fijas y sin instalar software?

- a) VDI con escritorios dedicados persistentes, uno por usuario y con clon completo.
- b) Escritorios basados en sesiones (RDSH), por su densidad y menor coste por puesto.
- c) Virtualización en el cliente, con un hipervisor de Tipo 2 en cada puesto de mostrador.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §3.1.2

Es el colectivo numeroso y homogéneo con un conjunto fijo de aplicaciones, caso natural del modelo de sesiones, que comparte un único sistema de servidor.

#### 2. ¿Y a los 150 técnicos que necesitan instalar de vez en cuando herramientas propias?

- a) Escritorios por sesiones, porque cada usuario puede instalar software en su sesión.
- b) Solo virtualización de aplicaciones, sin escritorio virtual de ningún tipo.
- c) VDI, por la personalización y el aislamiento de una máquina virtual por usuario.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §3.1.1

En un sistema compartido no se instala software por usuario; VDI ofrece aislamiento alto y la compatibilidad de un sistema de cliente.

#### 3. ¿Qué modelo procede para los 50 usuarios de cartografía con carga gráfica elevada?

- a) VDI con GPU virtual, porque su perfil de recursos no cabe en un servidor de sesiones.
- b) Escritorios por sesiones, aumentando el número de usuarios por servidor.
- c) Clientes ligeros conectados a un escritorio por sesiones sin aceleración gráfica.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §3.1.1

El perfil avanzado (4-8 vCPU, 16 GB y GPU virtual) degradaría a los demás usuarios de un servidor de sesiones.

#### 4. ¿Qué estrategia de persistencia conviene a los 700 puestos homogéneos de mostrador?

- a) Persistente con clones completos, para que cada usuario conserve los cambios que haga.
- b) Dedicada, porque solo los escritorios dedicados se parchean desde una imagen maestra.
- c) No persistente: una sola imagen que parchear, gran ahorro de almacenamiento y escritorio limpio cada vez.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §3.4

Con el modelo de sesiones elegido, el usuario no tiene máquina propia: entra en cualquiera de los servidores de sesión, idénticos y creados desde una imagen maestra, y su entorno va aparte. El entorno limpio en cada inicio refuerza además la confidencialidad de los datos del padrón del mostrador.

#### 5. ¿Qué piezas impiden que el usuario de un escritorio no persistente pierda su entorno?

- a) Guardar el perfil en el disco del propio escritorio para que se recupere al reiniciar.
- b) Contenedor de perfil en disco virtual, redirección de carpetas a la red y directivas en cada inicio.
- c) Convertir los escritorios en persistentes cuando un usuario se queje de perder datos.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §3.4

El modelo no persistente exige resolver la persistencia del usuario fuera del escritorio; las capas de aplicación completan el esquema.

#### 6. ¿Cómo se aplica un parche crítico del sistema operativo a esos escritorios?

- a) Una vez sobre la imagen maestra: copia de trabajo, parche, piloto, nueva versión sellada y publicación.
- b) Escritorio por escritorio, con la herramienta de despliegue de software corporativa.
- c) Directamente sobre todos los escritorios, sin piloto, porque se recrean cada noche.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §3.2.2

Los escritorios no persistentes adoptan la nueva versión en su siguiente reinicio, y si es defectuosa se revierte a la anterior con la misma operación.

#### 7. Todos los usuarios inician sesión entre las 8:00 y las 8:20. ¿Qué fenómeno provocará?

- a) Un «cerebro dividido» (split brain), porque dos anfitriones arrancan el mismo escritorio.
- b) Una tormenta de arranque y de inicio de sesión: un pico de E/S que el almacenamiento no absorbe.
- c) Una hiperpaginación de los anfitriones por falta de núcleos físicos de CPU.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §3.1.1

Cientos de escritorios arrancan, cargan perfiles y actualizan el antivirus a la vez; si el almacenamiento se dimensionó por consumo medio, no lo absorbe.

#### 8. ¿Cuál de estas medidas mitiga ese fenómeno?

- a) Lanzar el análisis antivirus completo de cada escritorio al iniciar sesión.
- b) Dimensionar el almacenamiento por el consumo medio de la jornada laboral.
- c) Preencender los escritorios de forma programada y escalonada antes de las 8:00.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §3.1.1

También valen el almacenamiento de estado sólido con caché de lectura, los clones instantáneos, el antivirus desfasado y la deduplicación.

#### 9. En los dos distritos con enlaces problemáticos, ¿qué factor de red determina la calidad percibida del escritorio virtual?

- a) La latencia de ida y vuelta y su estabilidad (fluctuación), más que el ancho de banda bruto.
- b) El ancho de banda bruto del enlace, con independencia de su latencia y su estabilidad.
- c) El número de saltos de encaminamiento entre la oficina y el centro de datos.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §3.3

Un enlace de mucho caudal pero inestable da peor experiencia que uno modesto y estable.

#### 10. ¿Cómo se firma con la tarjeta criptográfica desde el escritorio virtual y qué riesgo introduce ese mecanismo?

- a) Copiando el certificado en la imagen maestra; el riesgo es que la imagen ocupe más espacio.
- b) Instalando el lector en el anfitrión del centro de datos; el riesgo es la latencia del enlace.
- c) Con la redirección del lector de tarjeta por un canal virtual; los canales de redirección son vías de fuga.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §3.3

Portapapeles, unidades locales, impresión y USB deben estar deshabilitados por defecto y habilitarse por excepción justificada (art. 25 RGPD).

### Caso 3. Seguridad, cumplimiento y continuidad del entorno virtualizado

#### 1. La consola de gestión del clúster es accesible desde la red de usuarios. ¿Por qué es grave y cómo se corrige?

- a) Consume caudal de la red de usuarios: basta con limitar su ancho de banda.
- b) No es grave si la contraseña de la consola es larga y compleja.
- c) Quien controla la consola controla todas las máquinas: hay que segregar la red de gestión.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §5.1

Es el activo más crítico del entorno; si hace falta acceso remoto, solo a través de un mecanismo seguro con doble factor.

#### 2. Tres administradores comparten una cuenta. ¿Qué dimensión del ENS se destruye y cuál es la corrección?

- a) La trazabilidad; cuentas nominales, roles con mínimo privilegio y registro exportado fuera del entorno.
- b) La disponibilidad; basta con cambiar la contraseña compartida una vez al mes y comunicarla a los tres.
- c) Ninguna, si la contraseña de la cuenta se custodia en un sobre cerrado y bajo llave.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §4.3

Con una cuenta compartida no se puede saber quién ejecutó cada operación; el registro se exporta fuera para que no pueda alterarse desde el propio entorno.

#### 3. ¿Qué riesgo tienen las doce instantáneas de más de seis meses?

- a) Son copias de seguridad válidas que conviene conservar como histórico del entorno.
- b) Degradan el rendimiento y pueden llenar el almacén de datos, deteniendo máquinas virtuales.
- c) Ninguno, porque una instantánea no ocupa espacio en el almacén de datos.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §4.3

Una instantánea no es una copia de seguridad; las antiguas se consolidan y eliminan.

#### 4. ¿Qué hacer con las cuarenta máquinas virtuales apagadas desde hace más de un año y sin parchear?

- a) Incluirlas en los ciclos de actualización o darlas de baja tras consultar a la unidad responsable.
- b) Dejarlas como están, porque una máquina virtual apagada no puede ser vulnerable a ningún ataque.
- c) Eliminarlas de inmediato sin consultar a nadie, porque ninguna unidad las ha usado en un año.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §5.1

Es proliferación descontrolada: una máquina latente no recibe parches y es un sistema vulnerable el día que alguien la enciende.

#### 5. Las copias están en un repositorio del propio clúster, con las mismas credenciales que el hipervisor. ¿Qué riesgo concreto supone?

- a) Que las copias consumen ciclos de CPU de las máquinas virtuales en producción.
- b) Que la restauración es más lenta por estar el repositorio en el mismo clúster.
- c) Un compromiso del plano de gestión destruiría a la vez los datos y sus copias.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §5.3

Es exactamente lo que busca el ransomware moderno, que localiza y cifra las copias antes de actuar; además se incumple la regla 3-2-1.

#### 6. ¿En qué se funda jurídicamente la obligación de hacer pruebas de restauración?

- a) En el artículo 5.1.c del RGPD, que impone la minimización de los datos personales.
- b) En el artículo 32 del RGPD (capacidad de restaurar y verificación de la eficacia) y en el ENS.
- c) En el artículo 28 del RGPD, que regula los contratos con el encargado del tratamiento.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §5.2 · art. 32 RGPD

El artículo 32 exige la capacidad de restaurar la disponibilidad tras un incidente y verificar periódicamente las medidas; el ENS, pruebas periódicas de continuidad.

#### 7. La sede tiene un RPO de 15 minutos y un RTO de 1 hora, y se protege con una copia completa nocturna. ¿Los cumple?

- a) Sí: la copia completa nocturna garantiza un RPO de 15 minutos y un RTO de 1 hora.
- b) No: el RPO real es de hasta 24 horas y la restauración completa suele superar la hora.
- c) Solo incumple el RTO, porque el RPO de una copia diaria se mide en minutos.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §5.3

Una copia nocturna da un RPO de hasta 24 horas, y restaurar la máquina completa desde el repositorio consume en general más de una hora.

#### 8. ¿Qué combinación técnica sí satisface esos objetivos?

- a) Replicación asíncrona cada 15 minutos o menos a un segundo emplazamiento y recuperación orquestada probada.
- b) Copia incremental horaria en el mismo clúster y restauración manual de las máquinas afectadas.
- c) Copia completa nocturna en cinta y restauración completa desde la cinta en el segundo emplazamiento.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §5.3

El plan orquestado fija el orden de arranque, las dependencias y el direccionamiento, y se prueba en una red aislada sin afectar a producción.

#### 9. ¿Quién debe fijar el RTO y el RPO de la sede electrónica?

- a) El técnico de sistemas, según la tecnología de copia y réplica que tenga disponible.
- b) La organización responsable del servicio, mediante el análisis de impacto (BIA).
- c) El fabricante del hipervisor, según las capacidades de su producto de réplica.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §5.3

Son decisiones de la organización, no del técnico: de ellos se derivan la tecnología y el coste, nunca al revés.

#### 10. Desarrollo trabaja con un clon del padrón con datos reales en un entorno sin las medidas de producción. ¿Qué procede?

- a) Mantenerlo, siempre que se cifre el disco virtual del clon de pruebas.
- b) Mantenerlo, porque el artículo 32 del RGPD permite clonar datos para pruebas.
- c) Sustituirlo por datos seudonimizados o sintéticos (minimización y protección desde el diseño).

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §5.2 · arts. 5.1.c y 25 RGPD

Un clon de producción olvidado en un entorno menos protegido es uno de los orígenes más frecuentes de brecha; además debe autorizarse, protegerse como el original y tener fecha de destrucción.
