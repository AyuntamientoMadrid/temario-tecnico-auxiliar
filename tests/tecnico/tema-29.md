# Test del tema 29. Control remoto de puesto de usuario y gestión de la resolución de incidencias

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-29.html>

## Batería de preguntas

### 1. ¿Cuál es la diferencia esencial entre VDI y RDSH?

- a) En VDI cada usuario dispone de una máquina virtual completa con su propio sistema operativo, mientras que en RDSH varias sesiones comparten un mismo sistema operativo de servidor
- b) En VDI las aplicaciones se ejecutan en el equipo del usuario y en RDSH en el centro de datos
- c) VDI exige cliente ligero y RDSH exige obligatoriamente un cliente pesado

**Respuesta correcta:** a) · **Referencia:** §1.1.1 [MS-RDS]

De ahí que RDSH sea más eficiente en recursos por usuario pero ofrezca menor aislamiento: un usuario que consume memoria en exceso degrada a los demás.

### 2. En un entorno de escritorio virtualizado, ¿qué viaja fundamentalmente por la red entre el centro de datos y el puesto del usuario?

- a) El código fuente de las aplicaciones que se van a ejecutar en local
- b) La imagen de pantalla, las pulsaciones de teclado, el ratón, el audio y los periféricos redirigidos
- c) Únicamente los ficheros de datos que el usuario abre y guarda

**Respuesta correcta:** b) · **Referencia:** §1.1.1 [VDI-VENDORS]

La aplicación se ejecuta en el servidor; el puesto solo transmite entradas y recibe la representación de la pantalla. Por eso sin red no hay puesto.

### 3. Un equipo cuyo agente de gestión ha dejado de comunicar con la plataforma centralizada, pero que el usuario sigue utilizando con normalidad, ¿en qué situación se encuentra?

- a) En una situación irrelevante mientras el usuario pueda trabajar
- b) En una situación óptima, porque consume menos recursos al no ejecutar el agente
- c) Fuera de control de la organización: no se parchea, no se inventaría y no admite asistencia desatendida

**Respuesta correcta:** c) · **Referencia:** §1.1.2 [MS-INTUNE]

La pérdida de comunicación del agente es en sí misma una incidencia de soporte, aunque el usuario no perciba ningún síntoma.

### 4. Tres usuarios de la misma planta informan a la misma hora de que la red va lenta, mientras que en otra sede no hay problemas. ¿Cuál es el orden de diagnóstico correcto?

- a) Revisar uno a uno los tres puestos, porque el fallo es siempre local
- b) Confirmar el alcance real, comprobar el estado de los equipos de red de la sede, buscar una incidencia mayor ya abierta y solo entonces bajar al puesto individual
- c) Escalar de inmediato al fabricante del equipamiento de red sin comprobar nada

**Respuesta correcta:** b) · **Referencia:** §1.1.2 [ITIL4]

La coincidencia de varios usuarios en el mismo emplazamiento y a la misma hora desplaza la hipótesis hacia una capa compartida. Además, los tres avisos deben agruparse bajo una única incidencia.

### 5. ¿Cuál de estas afirmaciones distingue correctamente control remoto, acceso remoto y gestión remota?

- a) El control remoto sirve al soporte para ver y manejar el escritorio ajeno; el acceso remoto sirve al usuario para trabajar desde fuera; la gestión remota sirve al administrador para ejecutar tareas a escala
- b) Son tres nombres del mismo concepto y se usan indistintamente en la práctica profesional
- c) El acceso remoto se usa siempre para el soporte y el control remoto solo para el teletrabajo

**Respuesta correcta:** a) · **Referencia:** §1.2 [ITIL4]

Pueden compartir protocolos, pero responden a finalidades distintas y exigen autorizaciones distintas.

### 6. ¿Qué caracteriza a la asistencia remota desatendida frente a la atendida?

- a) Que es más rápida porque no cifra el canal de comunicación
- b) Que solo puede realizarse dentro de la red corporativa
- c) Que permite conectarse sin que haya nadie delante del equipo, por lo que exige autorización previa, mínimo privilegio, registro completo y auditoría reforzada

**Respuesta correcta:** c) · **Referencia:** §1.2 [ENS]

La ausencia de consentimiento en cada sesión debe compensarse con controles más estrictos, y en todo caso la sesión debe quedar registrada y ser atribuible a una persona identificada.

### 7. En una conexión de control remoto, ¿quién actúa como servidor?

- a) Siempre el equipo del técnico, porque es quien inicia la conexión
- b) El servidor de mediación, en todos los modelos de arquitectura
- c) El equipo que es controlado, es decir, el del usuario, que sirve su pantalla al visor del técnico

**Respuesta correcta:** c) · **Referencia:** §1.2.1 [RFC6143]

Es una inversión terminológica; en X Window ocurre algo análogo, con el servidor X ejecutándose donde está la pantalla del usuario.

### 8. ¿Por qué las herramientas modernas de asistencia usan un servidor de mediación al que ambos extremos se conectan?

- a) Porque ambos extremos abren una conexión saliente, normalmente por HTTPS, lo que atraviesa NAT y cortafuegos sin necesidad de abrir puertos entrantes
- b) Porque el cifrado solo es posible cuando existe un tercero que conserva las claves
- c) Porque el protocolo RFB obliga a usar un intermediario según el RFC 6143

**Respuesta correcta:** a) · **Referencia:** §1.2.1 [MS-RDS]

Además, centraliza la autenticación, la autorización y el registro. Su contrapartida es la dependencia de esa infraestructura de mediación.

### 9. Una empleada en teletrabajo informa de que no le levanta la VPN y el CAU necesita ver su equipo. ¿Qué arquitectura de conexión es viable?

- a) La conexión directa cliente-servidor, publicando el puerto 3389 en su rúter doméstico
- b) La conexión mediada, porque el agente del portátil abre una conexión saliente hacia el servidor de mediación sin depender de la VPN averiada
- c) Ninguna: la incidencia exige necesariamente desplazamiento al domicilio

**Respuesta correcta:** b) · **Referencia:** §1.2.1 [MS-QUICKASSIST]

La regla general es que la herramienta de soporte no debe depender del servicio que puede estar averiado.

### 10. En el modelo AAA aplicado a una sesión de asistencia remota, ¿qué debe autenticarse?

- a) Tanto el técnico, con identidad nominal del directorio corporativo, como el equipo remoto, mediante certificado o huella de clave del servidor
- b) Únicamente el técnico, ya que el equipo remoto pertenece a la organización
- c) Únicamente el equipo remoto, ya que el técnico está en la red interna de administración

**Respuesta correcta:** a) · **Referencia:** §1.2.2 [RFC4253]

Si el visor acepta cualquier certificado o clave de servidor sin verificación, un atacante puede interponerse y capturar la sesión completa.

### 11. ¿Qué transmite el protocolo RFB, base de VNC, según el RFC 6143?

- a) Órdenes de dibujo de alto nivel y canales virtuales para redirigir impresoras y discos
- b) Únicamente texto cifrado y flujos de terminal
- c) El contenido del framebuffer, es decir, los píxeles de la pantalla, junto con los eventos de teclado y ratón en sentido inverso

**Respuesta correcta:** c) · **Referencia:** §1.3.1 [RFC6143]

De ahí su independencia del sistema operativo y su mayor consumo de ancho de banda frente a los protocolos de primitivas gráficas.

### 12. ¿En qué puertos operan, respectivamente, RDP, VNC y SSH?

- a) 3306, 5432 y 22
- b) 3389, 5900 y 22
- c) 3389, 5900 y 23

**Respuesta correcta:** b) · **Referencia:** §1.3.1 [MS-RDPBCGR]

RDP usa TCP y UDP 3389; VNC, TCP 5900 más el número de pantalla; SSH, TCP 22. El puerto 23 corresponde a Telnet, obsoleto por transmitir en claro.

### 13. ¿Cuál de estas afirmaciones sobre RDP es correcta?

- a) Transmite primitivas gráficas y multiplexa canales virtuales que permiten redirigir impresoras, discos, portapapeles y tarjetas inteligentes
- b) Transmite píxeles en bruto y por eso comparte siempre la sesión de consola del usuario
- c) Carece de cifrado propio, por lo que debe tunelizarse obligatoriamente sobre SSH

**Respuesta correcta:** a) · **Referencia:** §1.3.1 [MS-RDPBCGR]

Además, integra TLS y autenticación a nivel de red, y por defecto abre una sesión independiente en lugar de compartir la del usuario.

### 14. Las tres capas en las que se estructura el protocolo SSH son:

- a) Física, de enlace y de red
- b) Presentación, sesión y aplicación
- c) Transporte, autenticación de usuario y conexión

**Respuesta correcta:** c) · **Referencia:** §1.3.1 [RFC4251]

La capa de transporte negocia claves y autentica al servidor; la de autenticación identifica al usuario; la de conexión multiplexa canales, incluido el reenvío de puertos.

### 15. ¿Qué protocolo implementa Microsoft bajo el nombre de WinRM y en qué puertos opera?

- a) NETCONF, en el puerto 830
- b) WS-Management de DMTF, en los puertos TCP 5985 para HTTP y 5986 para HTTPS
- c) IPMI, en el puerto UDP 623

**Respuesta correcta:** b) · **Referencia:** §1.3.1 [MS-WINRM]

WinRM es la base de PowerShell Remoting y el equivalente funcional de SSH para la gestión sin interfaz gráfica en el mundo Windows.

### 16. Un equipo situado en una sede remota no arranca el sistema operativo. ¿Qué tecnología permite intervenir sin desplazamiento?

- a) La gestión fuera de banda mediante el controlador de gestión del equipo, con IPMI en el puerto UDP 623 o Redfish sobre HTTPS
- b) Una sesión de RDP contra el puerto 3389 del equipo averiado
- c) Una sesión de VNC sobre túnel SSH contra el puerto 5900

**Respuesta correcta:** a) · **Referencia:** §1.3.1 [IPMI2]

RDP, VNC y SSH son mecanismos dentro de banda: sus servidores son procesos del sistema operativo, de modo que si este no arranca no hay nada a lo que conectarse.

### 17. El paquete mágico de Wake-on-LAN se dirige convencionalmente a los puertos:

- a) TCP 22 y 23
- b) UDP 7 y 9
- c) UDP 161 y 162

**Respuesta correcta:** b) · **Referencia:** §1.3.1 [RFC862]

Permite encender por red equipos apagados para parchearlos fuera del horario laboral. Los puertos UDP 161 y 162 corresponden a SNMP.

### 18. Respecto de la seguridad de VNC clásico, ¿qué afirmación es correcta?

- a) Cifra todo el tráfico con TLS 1.3 desde la versión definida en el RFC 6143
- b) No necesita protección adicional si se cambia el puerto por defecto
- c) No cifra el tráfico y su autenticación es débil, por lo que debe tunelizarse sobre SSH o TLS y escuchar solo en la interfaz local

**Respuesta correcta:** c) · **Referencia:** §1.3.2 [RFC6143]

Un servidor VNC expuesto directamente a internet constituye un fallo grave de seguridad.

### 19. ¿Qué aporta la confidencialidad hacia adelante (forward secrecy) en TLS a una sesión de asistencia?

- a) Que comprometer en el futuro la clave privada del servidor no permita descifrar sesiones pasadas que hubieran sido grabadas
- b) Que la sesión pueda reanudarse automáticamente tras una caída de la red
- c) Que el técnico no necesite autenticarse si el certificado del servidor es válido

**Respuesta correcta:** a) · **Referencia:** §1.3.2 [RFC9846]

Es una propiedad del intercambio de claves, no del cifrado simétrico ni de la autenticación.

### 20. Un técnico necesita asistir a una usuaria y ver exactamente lo que ella ve en su pantalla. ¿Qué mecanismo NO le sirve?

- a) La herramienta de asistencia atendida con código de sesión y consentimiento
- b) Una conexión de escritorio remoto estándar por RDP, que abre una sesión nueva e independiente
- c) La observación de sesión (shadowing) en servicios de escritorio remoto

**Respuesta correcta:** b) · **Referencia:** §1.3.3 [MS-RDS]

El técnico vería un escritorio distinto del que la usuaria tiene delante y no reproduciría su problema; además, ciertos periféricos como el lector de tarjeta criptográfica no estarían disponibles en esa sesión.

### 21. En el reenvío de X11 sobre SSH, ¿dónde se ejecuta el servidor X?

- a) En el equipo remoto donde se ejecuta la aplicación gráfica
- b) En el servidor de mediación que empareja ambos extremos
- c) En la máquina del usuario, donde está la pantalla; la aplicación remota actúa como cliente

**Respuesta correcta:** c) · **Referencia:** §1.3.3 [X11]

Es el modelo cliente-servidor invertido característico del sistema X Window, y una fuente habitual de confusión.

### 22. ¿Cuál es la principal aportación de una plataforma de gestión centralizada del puesto a la calidad del servicio?

- a) Que convierte el soporte reactivo en proactivo, reduciendo el número de incidencias y no solo el tiempo de resolución
- b) Que sustituye por completo al Centro de Atención a Usuarios
- c) Que elimina la necesidad de mantener un acuerdo de nivel de servicio

**Respuesta correcta:** a) · **Referencia:** §1.3.4 [MS-INTUNE]

Detectar el disco lleno, el parche que falta o el antivirus desactualizado antes de que provoquen la incidencia es más valioso que resolverla rápido.

### 23. Según ITIL, ¿cuál es el objetivo de la gestión de incidencias?

- a) Identificar la causa raíz del fallo antes de actuar sobre el servicio
- b) Restablecer el servicio normal lo antes posible, minimizando el impacto adverso en la actividad
- c) Documentar el fallo para que no vuelva a producirse en el futuro

**Respuesta correcta:** b) · **Referencia:** §2.1.1 [ITIL4]

Hallar la causa raíz corresponde a la gestión de problemas, que trabaja sin la urgencia del servicio caído.

### 24. Respecto de la certificación en gestión de servicios TI:

- a) ITIL certifica organizaciones y COBIT certifica personas
- b) ISO/IEC 20000-1 certifica exclusivamente a personas mediante examen
- c) ITIL certifica a personas, mientras que la certificación de una organización en gestión del servicio se obtiene con ISO/IEC 20000-1

**Respuesta correcta:** c) · **Referencia:** §2.1.1 [ISO20000]

ITIL propone buenas prácticas adaptables; ISO/IEC 20000-1 impone requisitos auditables de un sistema de gestión del servicio.

### 25. ¿Qué cambio estructural introduce ITIL 4 respecto de ITIL v3?

- a) Suprime la figura del Centro de Atención a Usuarios y la sustituye por la automatización
- b) Sustituye la estructura de procesos por fases del ciclo de vida por el Sistema de Valor del Servicio, y habla de prácticas en lugar de procesos
- c) Elimina la distinción entre incidencia y problema por considerarla artificial

**Respuesta correcta:** b) · **Referencia:** §2.1.1 [ITIL4]

En ITIL v3 el Service Desk era una función y la gestión de incidencias un proceso de la fase de operación; en ITIL 4 ambos son prácticas.

### 26. En un tique de incidencia, el estado «en espera del usuario» tiene la particularidad de que:

- a) Normalmente detiene el reloj del acuerdo de nivel de servicio, por lo que su uso debe estar reglado y auditado
- b) Acelera el cómputo del tiempo de resolución para compensar la espera
- c) Obliga automáticamente al cierre del tique transcurridas veinticuatro horas

**Respuesta correcta:** a) · **Referencia:** §2.1.2 [ITIL4]

Abusar de este estado para parar el reloj es una de las malas prácticas más habituales y falsea por completo los indicadores de cumplimiento.

### 27. El flujo de incidencia grave (major incident) se caracteriza por:

- a) Aplicarse automáticamente a todas las incidencias de prioridad 3 o superior
- b) Prescindir del registro en la herramienta para ganar tiempo
- c) Designar un responsable de la incidencia, establecer comunicación periódica a los afectados y a la dirección, y realizar una revisión posterior

**Respuesta correcta:** c) · **Referencia:** §2.1.2 [ITIL4]

Además, no espera al escalado normal: se escala de inmediato, tanto funcional como jerárquicamente.

### 28. El rasgo definitorio del Centro de Atención a Usuarios es:

- a) Resolver todas las incidencias sin escalar ninguna a otros grupos
- b) Ser el punto único de contacto entre los usuarios y la organización de tecnología
- c) Depender jerárquicamente del área de seguridad de la información

**Respuesta correcta:** b) · **Referencia:** §2.2.1 [ITIL4]

El usuario no tiene que saber a qué equipo técnico corresponde su problema: llama a un solo sitio y desde ahí se orquesta todo, conservando el CAU la propiedad del tique.

### 29. ¿Cuál es el objetivo económico de la estructura por niveles de soporte?

- a) Resolver el mayor volumen posible en los niveles más bajos, que son los más baratos por contacto
- b) Concentrar la resolución en el nivel 3, que es el más cualificado
- c) Igualar el número de incidencias resueltas en cada nivel

**Respuesta correcta:** a) · **Referencia:** §2.2.1 [ITIL4]

Cada escalado innecesario consume un recurso escaso, y por eso la tasa de resolución en primer contacto y la tasa de escalado son los dos indicadores que mejor miden la salud del modelo.

### 30. Un CAU multicanal debe garantizar que:

- a) Cada canal disponga de su propia herramienta y de su propio registro independiente
- b) El teléfono sea el único canal admitido para incidencias críticas
- c) Todos los canales desemboquen en un único registro y una única herramienta

**Respuesta correcta:** c) · **Referencia:** §2.2.2 [ISO20000]

La multicanalidad está en la entrada, nunca en el registro: registros separados por canal destruyen la trazabilidad, duplican incidencias e impiden medir.

### 31. La categorización de cierre de un tique difiere con frecuencia de la de apertura. Esto:

- a) Es siempre un error del técnico que debe corregirse retroactivamente
- b) Es información valiosa: mide el acierto del primer nivel al clasificar y sirve para depurar la taxonomía y los guiones de diagnóstico
- c) Impide utilizar los datos para el análisis de tendencias

**Respuesta correcta:** b) · **Referencia:** §2.2.2 [ITIL4]

La de apertura refleja lo que parecía; la de cierre, lo que era. Los análisis de tendencias deben apoyarse en la categorización de cierre.

### 32. Al diseñar la taxonomía de categorización de un CAU, la regla correcta es:

- a) Crear el máximo número posible de hojas para ganar precisión estadística
- b) Permitir que cada técnico defina sus propias categorías según su experiencia
- c) Definir pocas categorías, bien diferenciadas y mutuamente excluyentes

**Respuesta correcta:** c) · **Referencia:** §2.2.2 [ITIL4]

Una taxonomía con doscientas hojas se usa mal y produce datos inservibles; y si dos técnicos clasifican distinto el mismo caso, los indicadores mienten.

### 33. La prioridad de una incidencia se determina:

- a) Cruzando el impacto con la urgencia mediante una matriz y criterios objetivos escritos
- b) Aplicando exclusivamente el número de usuarios afectados
- c) Según la calificación que el propio usuario dé a su caso al llamar

**Respuesta correcta:** a) · **Referencia:** §2.3.1 [ITIL4]

La opinión del usuario es información a considerar, pero si la prioridad la fija quien más insiste, las incidencias verdaderamente críticas se retrasan.

### 34. Falla el proceso nocturno de copia de seguridad de un servidor de expedientes. Son las diez de la mañana y la próxima ventana de copia es a las once de la noche. ¿Cómo se valoran impacto y urgencia?

- a) Impacto bajo y urgencia baja, porque ningún usuario percibe el fallo
- b) Impacto alto, porque afecta a la protección de todos los expedientes, y urgencia media, porque hay margen hasta la siguiente ventana
- c) Impacto alto y urgencia alta, por tratarse de un servidor

**Respuesta correcta:** b) · **Referencia:** §2.3.1 [ITIL4]

Es el ejemplo canónico de que un impacto alto no implica automáticamente prioridad crítica. Si a las diez de la noche siguiera sin resolverse, la urgencia pasaría a alta y habría que reevaluar la prioridad.

### 35. Veinte usuarios llaman por separado informando del mismo fallo. La actuación correcta es:

- a) Cerrar diecinueve como duplicados sin registrarlos, para no inflar las estadísticas
- b) Tratarlos como veinte incidencias independientes de impacto bajo
- c) Vincularlos a una incidencia común cuyo impacto refleje a los veinte afectados, lo que eleva su prioridad

**Respuesta correcta:** c) · **Referencia:** §2.3.1 [ITIL4]

La agrupación eleva el impacto y permite comunicar de una sola vez a todos los afectados cuando se restablezca el servicio.

### 36. ¿Qué es el escalado funcional?

- a) El traslado de la incidencia a un grupo con mayor conocimiento técnico o mayores permisos, del nivel 1 al 2, al 3 o al proveedor
- b) El aviso a un nivel de autoridad superior para que decida o autorice
- c) La reasignación del tique a otro técnico del mismo nivel por carga de trabajo

**Respuesta correcta:** a) · **Referencia:** §2.3.2 [ITIL4]

Es horizontal y responde a «no sé o no puedo resolverlo»; no aporta autoridad, sino conocimiento.

### 37. El escalado jerárquico procede cuando:

- a) El técnico de primer nivel carece del conocimiento técnico necesario
- b) Es preciso instalar un parche en un servidor gestionado por otro equipo
- c) Se van a incumplir los plazos, hace falta autorizar una parada o un gasto, o el impacto exige comunicación a la dirección

**Respuesta correcta:** c) · **Referencia:** §2.3.2 [ITIL4]

El escalado jerárquico no aporta conocimiento técnico: aporta decisión y recursos. Ambos escalados pueden coexistir en la misma incidencia.

### 38. Cuando una incidencia se escala a un nivel superior:

- a) La propiedad del tique se transfiere al grupo destinatario, que pasa a informar al usuario
- b) El CAU conserva la propiedad del tique y sigue siendo responsable de su seguimiento y de informar al usuario
- c) El tique se cierra y se abre uno nuevo a nombre del grupo resolutor

**Respuesta correcta:** b) · **Referencia:** §2.3.2 [ITIL4]

Escalar no es quitárselo de encima; además, el escalado debe ir documentado con el síntoma, el alcance y las comprobaciones ya realizadas y descartadas.

### 39. ¿Puede cerrarse una incidencia aplicando únicamente una solución temporal o rodeo?

- a) Sí, siempre que el servicio esté restablecido, el rodeo esté documentado y se haya abierto el problema correspondiente si la causa persiste
- b) No: la gestión de incidencias solo puede cerrar tras eliminar la causa raíz
- c) Sí, y sin necesidad de documentar nada, porque el usuario ya puede trabajar

**Respuesta correcta:** a) · **Referencia:** §2.3.3 [ITIL4]

Cerrar con rodeo sin abrir el problema es justamente la práctica que hace que la misma incidencia reaparezca indefinidamente.

### 40. Respecto del cierre de un tique, la regla general es:

- a) Cerrar en cuanto el técnico verifica que el servicio funciona, sin más trámite
- b) No cerrar sin confirmación del usuario, salvo la regla de cierre automático tras un plazo pactado sin respuesta, dejando constancia de los intentos
- c) Mantener el tique abierto indefinidamente hasta que el usuario solicite su cierre por escrito

**Respuesta correcta:** b) · **Referencia:** §2.3.3 [ITIL4]

La verificación técnica y la del usuario no son la misma cosa: es el usuario quien define si el servicio está restablecido.

### 41. Una tasa de reapertura alta es una señal de alarma porque indica que:

- a) Se está cerrando antes de tiempo, quizá para cumplir formalmente el acuerdo de nivel de servicio
- b) El volumen de incidencias es superior al que el CAU puede absorber
- c) La taxonomía de categorización tiene demasiadas hojas

**Respuesta correcta:** a) · **Referencia:** §2.3.3 [ITIL4]

Es un ejemplo del riesgo general de las métricas: medir mal induce a comportarse mal. Por eso la productividad se contrasta siempre con la reapertura y con la satisfacción.

### 42. ¿Qué distingue a un OLA de un SLA y de un UC?

- a) El OLA se firma con el proveedor externo y el UC con el cliente
- b) El OLA sustituye al SLA cuando el servicio está externalizado
- c) El OLA es un acuerdo interno entre equipos de la propia organización; el SLA se pacta con el cliente y el UC es el contrato con un proveedor externo

**Respuesta correcta:** c) · **Referencia:** §2.3.4 [ITIL4]

Los OLA y los UC deben estar dimensionados de forma que permitan cumplir el SLA.

### 43. El SLA compromete resolver las incidencias críticas en cuatro horas, pero el contrato con el fabricante garantiza la sustitución de piezas al siguiente día laborable. ¿Qué falla y cómo se corrige?

- a) Nada falla: el plazo del fabricante no afecta al cómputo del SLA en ningún caso
- b) El contrato de soporte no sostiene el SLA; se corrige elevando el UC o diseñando el servicio con redundancia para que el restablecimiento no dependa de la pieza
- c) Falla el OLA interno, que debe reducirse a dos horas para compensar

**Respuesta correcta:** b) · **Referencia:** §2.3.4 [ISO20000]

Lo que el SLA compromete es restablecer el servicio, no reparar el componente averiado: por eso la redundancia más un stock propio de repuestos suele ser más barata y fiable que un contrato de respuesta ultrarrápida.

### 44. La diferencia entre tiempo de respuesta y tiempo de resolución es que:

- a) El de respuesta mide hasta el primer contacto efectivo o la asignación, y el de resolución hasta el restablecimiento del servicio
- b) El de respuesta mide el tiempo total del tique y el de resolución solo la parte trabajada
- c) Son sinónimos y se informan de forma conjunta en un único indicador

**Respuesta correcta:** a) · **Referencia:** §2.3.4 [ITIL4]

Un CAU puede cumplir escrupulosamente el tiempo de respuesta e incumplir de forma sistemática el de resolución: por eso ambos se miden e informan por separado.

### 45. Un usuario solicita el alta de acceso a una carpeta compartida. Se trata de:

- a) Una incidencia de prioridad baja, por afectar a un solo usuario
- b) Un problema, porque revela una carencia en la configuración de permisos
- c) Una petición de servicio: nada está roto y es una solicitud prevista en el catálogo, que además exigirá autorización previa

**Respuesta correcta:** c) · **Referencia:** §2.4.1 [ITIL4]

Las peticiones se miden por cumplimiento de plazo, no por rapidez de restablecimiento, y mezclarlas con las incidencias en un mismo indicador produce cifras sin sentido.

### 46. Los tres tipos de evento que distingue ITIL son:

- a) Crítico, mayor y menor
- b) Informativo, advertencia y excepción
- c) Preventivo, correctivo y evolutivo

**Respuesta correcta:** b) · **Referencia:** §2.4.1 [ITIL4]

El informativo registra algo previsto; la advertencia señala la proximidad de un umbral y permite actuar antes; la excepción indica que el umbral se ha superado y suele generar una incidencia automática.

### 47. ¿Por qué el evento de advertencia es el de mayor valor económico?

- a) Porque permite evitar la incidencia en lugar de resolverla, habilitando el soporte proactivo
- b) Porque siempre genera un tique de prioridad crítica que se atiende antes
- c) Porque es el único tipo de evento que la monitorización puede correlacionar

**Respuesta correcta:** a) · **Referencia:** §2.4.1 [NAGIOS]

Un servicio de soporte maduro se reconoce en que una parte creciente de su trabajo procede de eventos de advertencia y no de llamadas de usuarios.

### 48. El riesgo característico de una monitorización mal ajustada es el exceso de alertas. ¿Qué técnica lo mitiga?

- a) Elevar todos los umbrales hasta que solo se notifiquen las caídas totales
- b) Enviar todas las alertas al buzón del responsable del CAU para que las filtre
- c) Correlacionar los eventos para emitir una única alerta con la causa, suprimirlas durante las ventanas de mantenimiento y ajustar los umbrales de forma continua

**Respuesta correcta:** c) · **Referencia:** §2.4.1 [NAGIOS]

Un enlace caído genera cien alertas de los servicios que dependen de él; hay que emitir una sola con la causa, o el operador dejará de mirarlas.

### 49. ¿Qué es un error conocido?

- a) Una incidencia que se repite más de tres veces en el mismo mes
- b) Un problema ya analizado, del que se conoce la causa y/o una solución temporal documentada
- c) Un fallo del que se ha informado al fabricante y aún no ha respondido

**Respuesta correcta:** b) · **Referencia:** §2.4.1 [ITIL4]

Se registra en la base de datos de errores conocidos (KEDB), que la gestión de problemas escribe y la de incidencias consulta.

### 50. Ciento cuarenta incidencias idénticas resueltas una a una con el mismo rodeo indican que:

- a) La gestión de incidencias funciona pero el servicio falla: hay que abrir un problema, analizar la causa raíz y planificar la solución definitiva como un cambio
- b) El acuerdo de nivel de servicio debe relajarse para absorber ese volumen
- c) La categorización de apertura está mal diseñada y debe rehacerse la taxonomía

**Respuesta correcta:** a) · **Referencia:** §2.4.2 [ITIL4]

El resultado se mide en la caída de una familia entera de incidencias, no en el tiempo de resolución de cada una.

### 51. El principio de mínimo privilegio aplicado a la asistencia remota tiene dos dimensiones:

- a) El número de técnicos autorizados y el número de equipos del parque
- b) Qué permisos se conceden —los imprescindibles— y durante cuánto tiempo —solo el necesario—
- c) El coste de la herramienta y la formación del personal que la utiliza

**Respuesta correcta:** b) · **Referencia:** §3.1.1 [ENS]

Se completa con la segregación de funciones, que impide que una misma persona administre la herramienta de asistencia y audite sus registros.

### 52. En un servicio de soporte, el uso de cuentas genéricas compartidas por el equipo de técnicos:

- a) Está desaconsejado porque destruye la trazabilidad: las actuaciones dejan de ser atribuibles a una persona identificada
- b) Es recomendable porque simplifica la gestión de altas y bajas de personal
- c) Es indiferente siempre que la sesión vaya cifrada

**Respuesta correcta:** a) · **Referencia:** §3.1.1 [ENS]

La identidad debe ser nominal y provenir del directorio corporativo, con separación entre la cuenta ofimática del técnico y la cuenta con la que administra.

### 53. En una auditoría de las sesiones de asistencia remota, ¿cuál es el hallazgo más significativo?

- a) Que alguna sesión haya durado más de una hora
- b) Que se hayan usado modos de solo visualización en lugar de control total
- c) La sesión sin tique asociado, porque revela un acceso sin justificación registrada

**Respuesta correcta:** c) · **Referencia:** §3.1.2 [ENS]

Toda sesión debe responder a una causa registrada; el tique es lo que convierte el acceso en legítimo y auditable.

### 54. Los registros de actividad de las sesiones de asistencia deben:

- a) Almacenarse en el propio equipo atendido, para facilitar su consulta local
- b) Centralizarse en un sistema independiente del sistema auditado, con control de acceso propio y plazo de conservación definido
- c) Borrarse al cerrar cada incidencia, para minimizar el tratamiento de datos

**Respuesta correcta:** b) · **Referencia:** §3.1.2 [ISO27001]

Un registro que el propio administrador puede borrar no acredita nada. Además, sin sincronización horaria común los registros de distintos equipos no pueden correlacionarse.

### 55. Las cinco dimensiones de seguridad del Esquema Nacional de Seguridad son:

- a) Disponibilidad, autenticidad, integridad, confidencialidad y trazabilidad
- b) Confidencialidad, integridad, disponibilidad, resiliencia y continuidad
- c) Prevención, detección, respuesta, conservación y vigilancia

**Respuesta correcta:** a) · **Referencia:** §3.2.1 [ENS]

Cada una se valora en nivel bajo, medio o alto, y la categoría del sistema —básica, media o alta— la determina el nivel más alto alcanzado por cualquiera de ellas.

### 56. Respecto de la auditoría de seguridad exigida por el ENS:

- a) Todos los sistemas deben auditarse anualmente con independencia de su categoría
- b) Solo se audita cuando se produce un incidente de seguridad notificable
- c) Los sistemas de categoría media y alta se auditan al menos cada dos años, mientras que los de categoría básica admiten autoevaluación

**Respuesta correcta:** c) · **Referencia:** §3.2.1 [ENS]

Además, cualquier modificación sustancial del sistema obliga a repetir la auditoría, y la conformidad debe publicarse con su distintivo en la sede electrónica.

### 57. Si durante una asistencia remota se produce o se descubre una brecha de datos personales, el plazo de notificación a la autoridad de control es:

- a) De quince días naturales desde que se tuvo constancia
- b) Sin dilación indebida y, de ser posible, en un plazo máximo de 72 horas desde que se tuvo constancia
- c) De un mes, prorrogable por otro mes en casos complejos

**Respuesta correcta:** b) · **Referencia:** §3.2.2 [RGPD]

La comunicación a los propios interesados procede además cuando la brecha entrañe alto riesgo para sus derechos y libertades.

### 58. Cuando el servicio de asistencia remota se presta mediante una herramienta en la nube de un tercero, ese proveedor:

- a) Queda al margen del RGPD por limitarse a transportar tráfico cifrado
- b) Es responsable del tratamiento, y desplaza esa condición de la Administración
- c) Es encargado del tratamiento y debe existir un contrato que fije objeto, finalidad, tipo de datos, obligaciones de seguridad y devolución o supresión al terminar

**Respuesta correcta:** c) · **Referencia:** §3.2.2 [RGPD]

Además hay que analizar la ubicación del servidor de mediación y de las grabaciones por la eventual transferencia internacional de datos.

### 59. Un CAU registra en un mes 6.000 incidencias, de las que el nivel 1 resuelve 4.200 en primer contacto. ¿Cuál es su FCR?

- a) 70 %
- b) 30 %
- c) 42 %

**Respuesta correcta:** a) · **Referencia:** §3.3.1 [ITIL4]

La resolución en primer contacto es 4.200 dividido entre 6.000. El 30 % restante corresponde a la tasa de escalado, indicador complementario del anterior.

### 60. Un artículo de la base de conocimiento debe redactarse:

- a) Desde la causa técnica, para que sea preciso y verificable por el nivel 3
- b) En inglés, para facilitar la búsqueda en la documentación del fabricante
- c) Desde el síntoma, porque el técnico que lo busca sabe lo que ve, no lo que falla

**Respuesta correcta:** c) · **Referencia:** §3.3.2 [ITIL4]

Los artículos escritos desde la causa resultan invisibles en la búsqueda y no se usan, por muy correctos que sean. Además, deben tener responsable, fecha de caducidad y retirada activa cuando quedan obsoletos.

## Preguntas sobre los casos prácticos

### Caso 1. Diagnóstico y asistencia remota en el puesto de una Oficina de Atención a la Ciudadanía

#### 1. En el supuesto planteado, antes de tocar el equipo de la tramitadora, ¿qué datos mínimos debe recoger el técnico del CAU?

- a) El número de tique, la contraseña de dominio de la usuaria para entrar en su sesión y el modelo del lector de tarjetas que tiene conectado.
- b) Identificación de la usuaria y su ubicación, fecha, hora y canal, el síntoma en sus palabras, el equipo según el inventario y el servicio afectado.
- c) La causa probable del fallo, la prioridad que la propia usuaria considera adecuada y el plazo en que necesita tener firmado el expediente.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.2.2

El registro identifica a quién, cuándo, por qué canal, qué síntoma describe, sobre qué equipo y qué servicio está afectado; la prioridad no la fija el usuario y nunca se piden sus credenciales.

#### 2. ¿Qué pregunta de acotación resulta más rentable para reorientar el diagnóstico y revisar el impacto de la incidencia?

- a) ¿Le ocurre solo a usted o también a sus compañeros de la oficina?
- b) ¿Qué número de serie figura en la etiqueta del lector de tarjetas?
- c) ¿Prefiere que la atienda un técnico presencial o uno en remoto?

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.2.2

Si el fallo afecta a toda la oficina, la hipótesis se desplaza a una capa compartida y el impacto sube; si solo le pasa a ella, el problema está en su puesto.

#### 3. De las hipótesis de causa por capas, ¿cuál es la única que puede exigir presencia o la colaboración física de la usuaria y conviene descartar pronto?

- a) Que el certificado de la tarjeta haya caducado o haya sido revocado.
- b) Que el componente criptográfico esté desactualizado o desinstalado.
- c) Que el lector de tarjetas esté desconectado o el sistema no lo reconozca.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §1.1.2

Es la hipótesis de la capa de hardware o periférico: las de aplicaciones, identidad, configuración y conectividad se comprueban en remoto en pocos minutos.

#### 4. Si la causa fuera que el certificado de la tramitadora ha caducado o ha sido revocado, ¿en qué capa del puesto se situaría el fallo?

- a) En la capa de hardware, y exigiría desplazarse al puesto.
- b) En la capa de identidad, y podría comprobarse en remoto.
- c) En la capa de conectividad, porque depende de la red municipal.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §1.1.2

La validez del certificado es una cuestión de identidad del usuario, no del dispositivo ni de la red, y se verifica sin necesidad de presencia.

#### 5. ¿Qué tipo de sesión de control remoto debe abrir el técnico para atender a la tramitadora?

- a) Una asistencia desatendida en modo control exclusivo, oscureciendo la pantalla de la usuaria.
- b) Una sesión independiente por escritorio remoto, sin interferir con la sesión de la usuaria.
- c) Una asistencia atendida en modo control compartido sobre la sesión que la usuaria ya tiene abierta.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §1.2

La usuaria está presente y debe consentir; el control compartido le permite ver lo que hace el técnico e interrumpir, y es el modo estándar de la asistencia atendida.

#### 6. ¿Por qué NO sirve en este supuesto una conexión de escritorio remoto estándar por RDP?

- a) Porque abre una sesión nueva, en la que el técnico no ve el escritorio de la usuaria ni dispone de su tarjeta criptográfica.
- b) Porque RDP trabaja en el puerto TCP 5900, que el cortafuegos de la red corporativa municipal mantiene bloqueado.
- c) Porque RDP solo transmite órdenes de consola sin interfaz gráfica, y la firma se hace desde el navegador web.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §1.3.3

RDP estándar crea una sesión independiente: no reproduce el fallo que la usuaria tiene delante y la tarjeta y su lector están asociados a la sesión de ella. RDP usa el puerto 3389.

#### 7. ¿Cómo se materializa en esta asistencia el consentimiento de la tramitadora a la sesión?

- a) Mediante su contraseña de dominio, que facilita al técnico para que acceda a la sesión.
- b) Mediante un código de sesión de un solo uso que ella genera y facilita al técnico.
- c) Mediante la cuenta genérica del CAU, que tiene autorizado el acceso a todos los puestos.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §1.2.2

El código de un solo uso no autentica al técnico, pero prueba que la usuaria solicitó la sesión y la limita a esa ocasión; las credenciales nunca se comparten y las cuentas genéricas están proscritas.

#### 8. La tramitadora tiene abiertos varios documentos con datos de otros vecinos que nada tienen que ver con el fallo de firma. ¿Qué debe hacer el técnico?

- a) Pedirle que cierre los documentos con datos de terceros que no sean necesarios, en aplicación del principio de minimización.
- b) Grabar la sesión completa con esos documentos visibles, para dejar constancia de lo que había en la pantalla de la usuaria.
- c) Pasar a control exclusivo y oscurecer la pantalla, para que la usuaria no vea los datos que el técnico consulta en su equipo.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §1.2.2, §3.2.2

El acceso a datos personales durante la asistencia solo es lícito para resolver la incidencia registrada; lo que no sea necesario debe cerrarse antes de trabajar.

#### 9. Tras actualizar el componente criptográfico, el técnico comprueba que la firma funciona. ¿Cuándo puede darse por cerrada la incidencia?

- a) En cuanto el técnico verifica que la versión instalada es la correcta, porque la comprobación técnica ya acredita la solución.
- b) Al terminar la sesión de control remoto, que cierra el tique de forma automática con la misma categoría con la que se abrió.
- c) Cuando la usuaria firma el expediente pendiente y confirma que puede trabajar, documentando lo hecho y la categoría de cierre.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 4 · §2.3.3

La verificación técnica y la del usuario no son lo mismo: hay que confirmar que la usuaria puede trabajar y documentar la resolución con su categorización de cierre, que puede diferir de la de apertura.

#### 10. Cerrado el tique, ¿qué actuación permite saber si se trataba de un caso aislado o de un problema que conviene abrir?

- a) Esperar a que otros usuarios llamen con el mismo síntoma y, entonces, reabrir el tique de la tramitadora.
- b) Consultar en el inventario cuántos puestos más tienen la versión afectada del componente criptográfico.
- c) Preguntar a la tramitadora si recuerda a algún compañero que haya tenido alguna vez un fallo parecido.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §2.3.3, §3.3.2

El inventario permite medir el alcance de forma proactiva; si hay más puestos con la misma versión, se abre el problema correspondiente.

### Caso 2. Priorización, escalado y acuerdo de nivel de servicio ante una caída del servicio de firma

#### 1. En el supuesto planteado, ¿cómo deben tratarse las catorce llamadas recibidas en el CAU?

- a) Abriendo catorce incidencias independientes, cada una con la prioridad que corresponda a su oficina.
- b) Registrando solo la primera llamada y descartando las otras trece como duplicados sin dejar constancia.
- c) Registrando cada contacto y vinculándolos todos a una única incidencia que representa el fallo del servicio.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §2.3.1

Hay catorce usuarios que esperan respuesta, por lo que cada contacto se registra, pero el fallo es uno solo y se gestiona como una incidencia común con todos ellos como afectados.

#### 2. ¿Qué efecto tiene sobre la incidencia la agrupación de las catorce llamadas?

- a) Rebaja la prioridad, porque el CAU pasa a gestionar un único tique en lugar de catorce tiques distintos.
- b) Eleva el impacto, que pasa de un usuario a varias unidades de seis distritos, y permite avisar a todos a la vez.
- c) No altera la prioridad, que depende únicamente de la urgencia que declara la primera oficina que llama.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §2.3.1

La agrupación eleva el impacto, porque la incidencia común refleja a todos los afectados, y permite comunicar de una sola vez el restablecimiento.

#### 3. ¿Cómo debe valorarse el impacto de la caída del servicio de firma?

- a) Alto, porque está afectado un servicio esencial en varias unidades y distritos y se interrumpe la atención al ciudadano.
- b) Medio, porque las aplicaciones internas de gestión siguen funcionando y el servicio solo está degradado con rodeo.
- c) Bajo, porque el fallo no se reproduce en los puestos del CAU y cada oficina solo tiene unos pocos afectados.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §2.3.1

Servicio esencial caído en varias unidades con la atención al ciudadano interrumpida es el criterio de impacto alto; no consta rodeo disponible.

#### 4. Valorado el impacto como alto, ¿qué urgencia y qué prioridad corresponden con la matriz de impacto y urgencia?

- a) Urgencia media, porque el SLA concede cuatro horas, y prioridad 2, alta.
- b) Urgencia baja, porque la firma puede posponerse a mañana, y prioridad 3, media.
- c) Urgencia alta, porque el daño se produce ahora y no hay rodeo, y prioridad 1, crítica.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §2.3.1

La urgencia mide cuánto puede esperar: hay vecinos esperando y no consta rodeo. Impacto alto por urgencia alta da prioridad 1 en la matriz 3×3.

#### 5. Además de asignar la prioridad 1, ¿qué procede hacer con esta incidencia?

- a) Activar el procedimiento de incidencia grave, que es un flujo propio con responsable designado y revisión posterior.
- b) Nada más, porque toda incidencia de prioridad 1 es por definición grave y sigue el mismo flujo que las demás.
- c) Cerrarla y abrir en su lugar un problema, porque hay más de diez usuarios afectados por la misma causa.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §2.3.1

La incidencia grave no es simplemente la de prioridad 1: es una categoría con procedimiento propio que se activa por criterios definidos, como el número de afectados y la criticidad del servicio.

#### 6. ¿A quién debe dirigirse el escalado funcional de esta incidencia y por qué?

- a) Al responsable del CAU y a la dirección, porque son quienes conocen la plataforma de firma y pueden diagnosticar la causa técnica del fallo.
- b) Al equipo de administración electrónica o de la plataforma de firma, porque el fallo está en un componente central y el primer nivel no puede resolverlo.
- c) Al técnico de segundo nivel de cada distrito, porque el fallo está en los puestos de las oficinas y hay que revisarlos uno por uno.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §2.3.2

El escalado funcional busca más conocimiento o permisos. El fallo no se reproduce en el CAU, afecta a seis distritos a la vez y a un solo servicio: no está en los puestos sino en un componente central.

#### 7. ¿Qué aporta en este supuesto el escalado jerárquico al responsable del CAU y, a través de él, a la dirección?

- a) El diagnóstico técnico de la plataforma de firma, que el primer nivel no conoce y que la dirección analiza con sus propios medios.
- b) La propiedad del tique, que pasa del CAU a la dirección, de modo que el CAU deja de informar a los usuarios afectados.
- c) Capacidad de decisión y recursos: activar la incidencia grave, designar responsable y autorizar, si hace falta, una reversión de emergencia.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §2.3.2

El escalado jerárquico no aporta conocimiento técnico, sino quien decida y quien aporte recursos; la propiedad del tique sigue siendo del CAU.

#### 8. ¿Qué información debe acompañar a los escalados?

- a) Síntoma exacto, alcance confirmado, hora de inicio, comprobaciones ya descartadas, cambios recientes y qué se pide a cada destinatario.
- b) Únicamente el número de tique, porque el destinatario debe repetir el diagnóstico desde el principio para no arrastrar sesgos.
- c) La lista de los catorce usuarios con sus datos de contacto, para que el equipo receptor los llame uno a uno y repita las pruebas.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §2.3.2

El escalado debe permitir al receptor actuar sin repetir lo ya hecho: qué pasa, a cuántos afecta, desde cuándo, qué se ha descartado, qué ha cambiado y qué se le pide.

#### 9. Mientras dura la incidencia, ¿cómo debe comunicarse el CAU con las oficinas afectadas?

- a) Solo cuando el servicio esté restablecido, para no generar expectativas que luego no puedan cumplirse en plazo.
- b) De forma proactiva y periódica, con una previsión realista y actualizaciones a intervalos fijos aunque no haya novedades.
- c) Solo a las oficinas que vuelvan a llamar, para no saturar a las demás con avisos que todavía no aportan nada.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §2.1.2

Las oficinas necesitan poder decir algo al ciudadano que espera: la comunicación estructurada y periódica forma parte del procedimiento de incidencia grave.

#### 10. El servicio se restablece con un rodeo y la causa raíz aún no está determinada. ¿Qué debe hacerse a continuación?

- a) Cerrar la incidencia y archivar el caso, porque una vez restablecido el servicio la causa raíz deja de ser relevante.
- b) Aplicar en producción la solución definitiva en cuanto se conozca, sin ventana ni plan de reversión, para ganar tiempo.
- c) Abrir el problema, registrar el error conocido y su rodeo en la KEDB y tramitar la solución definitiva por gestión de cambios.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §2.3.3, §2.4.2

Restablecer no es resolver la causa: la gestión de problemas analiza la causa raíz, la KEDB documenta el rodeo y la solución definitiva entra como cambio con evaluación de riesgo, ventana y plan de reversión.

### Caso 3. Seguridad, cumplimiento normativo y mejora continua del servicio de asistencia

#### 1. En el piloto, varios técnicos comparten una misma cuenta para conectarse a los puestos. ¿Qué exigencia incumple esa práctica?

- a) La identificación nominal y, con ella, la trazabilidad: las actuaciones dejan de ser atribuibles a una persona.
- b) La disponibilidad, porque una cuenta compartida se bloquea antes por los intentos fallidos de acceso.
- c) La exactitud de los datos, porque varios técnicos pueden modificar a la vez los expedientes del usuario.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §3.1.1

Con cuentas compartidas no puede saberse quién hizo cada actuación, de modo que ni se puede auditar ni exigir responsabilidad: se pierde la trazabilidad del ENS.

#### 2. ¿Cómo se corrige el hallazgo de las cuentas compartidas?

- a) Manteniendo la cuenta común pero cambiando su contraseña cada mes y comunicándola solo a los técnicos que estén de guardia ese mes.
- b) Manteniendo la cuenta común y anotando en una hoja aparte qué técnico la ha utilizado en cada turno de trabajo del servicio de soporte.
- c) Con cuentas nominales del directorio corporativo, autenticación multifactor para quien controla en remoto y perfiles por rol con alcance limitado.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §3.1.1

La corrección es estructural: identidad nominal, segundo factor para el perfil con capacidad de control remoto, separación de cuentas y RBAC con alcance limitado a los equipos que corresponden a cada técnico.

#### 3. El 18 % de las sesiones registradas no tiene tique asociado. ¿Qué revela este hallazgo?

- a) Un simple defecto de los indicadores del servicio, sin consecuencias en materia de seguridad ni de protección de datos.
- b) Accesos sin justificación registrada, que afectan a la trazabilidad del ENS y a la limitación de la finalidad del RGPD.
- c) Un problema de disponibilidad del servicio, porque esas sesiones consumen licencias de la herramienta sin estar previstas.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §3.1.2

Una sesión sin tique es un acceso a un puesto, y a los datos que contiene, sin causa documentada que lo legitime: es el hallazgo de auditoría más significativo en este ámbito.

#### 4. ¿Qué medida corrige de forma efectiva las sesiones sin tique?

- a) Configurar la herramienta para exigir un tique válido antes de iniciar la sesión y revisar periódicamente las excepciones.
- b) Recordar por correo a los técnicos que deben abrir el tique y comprobar su cumplimiento al terminar el contrato.
- c) Borrar del registro las sesiones sin tique para que el porcentaje no distorsione los informes de seguimiento.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §3.1.2

La herramienta debe impedir la sesión sin tique válido, y la revisión periódica de sesiones sin tique, accesos desatendidos y fuera de horario, con alertas, completa el control.

#### 5. ¿Qué categoría ENS cabe prever para el sistema al que dan soporte los puestos, que trata expedientes con datos personales de ciudadanos?

- a) BÁSICA, porque la disponibilidad del soporte al puesto es baja y la categoría la fija la dimensión con el nivel más bajo.
- b) MEDIA o superior, porque alcanzará al menos nivel medio en confidencialidad, integridad y trazabilidad, y manda el nivel más alto.
- c) MEDIA en todo caso, porque la categoría es la media aritmética de los niveles asignados a las cinco dimensiones.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §3.2.1

Cada dimensión se valora como baja, media o alta y la categoría la determina el nivel más alto alcanzado por cualquiera de ellas; los datos personales llevan al menos al nivel medio.

#### 6. ¿Qué debe exigir el pliego respecto del registro de la actividad de las sesiones de asistencia?

- a) Guardarlo en el propio puesto asistido, para que el empleado pueda consultarlo cuando quiera y lo conserve mientras utilice ese mismo equipo.
- b) Que lo custodie y lo audite el mismo administrador de la herramienta de asistencia, para que las revisiones de los registros sean más ágiles.
- c) Protegerlo frente a manipulación, también del administrador, centralizarlo en un sistema independiente, con hora común y plazo de conservación definido.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §3.1.2, §3.2.1

El registro solo garantiza la trazabilidad si no puede alterarse ni siquiera por quien administra la herramienta; además, quien administra no debe ser quien audita (segregación de funciones).

#### 7. La herramienta del licitador usa un servidor de mediación en la nube del propio fabricante. ¿Qué es lo preferible exigir en el pliego?

- a) El despliegue del servidor de mediación en las instalaciones del Ayuntamiento o su alojamiento en la Unión Europea.
- b) Nada adicional, porque el tráfico va cifrado y el fabricante, al no ver los datos, no es encargado del tratamiento.
- c) La prohibición de toda asistencia remota durante el contrato y la vuelta al soporte presencial en todas las sedes.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §3.2.2

Por el servidor de mediación pasan las pantallas de los puestos municipales: el proveedor es encargado del tratamiento (art. 28 RGPD) y, si los datos salen del EEE, hay que analizar la transferencia internacional.

#### 8. La propuesta prevé grabar en vídeo todas las sesiones. ¿Cuál es la configuración proporcionada?

- a) Grabar todas las sesiones por defecto, porque cuanto más se registre mayor será el nivel de seguridad del sistema.
- b) No grabar nunca ninguna sesión, porque la LOPDGDD prohíbe todo control sobre los dispositivos de los empleados.
- c) Grabar solo los accesos de mayor privilegio y los desatendidos, informando antes al personal y a su representación.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §3.2.2

Grabarlo todo captura el correo, los documentos y datos de terceros del empleado; la organización puede establecer controles, pero informando antes al personal y a sus representantes (arts. 87-91 LOPDGDD).

#### 9. Si el contrato se siguiera solo con el número de tiques cerrados por técnico, ¿qué riesgo habría?

- a) Ninguno, porque el volumen resuelto por técnico es el indicador más completo de la calidad del servicio.
- b) Que se premie cerrar rápido y mal, por lo que debe contrastarse con la tasa de reapertura y la satisfacción.
- c) Que la tasa de reapertura baje de forma artificial, porque los tiques cerrados ya no pueden volver a abrirse.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §3.3.1

Un indicador aislado siempre se puede maximizar a costa del servicio: la productividad debe equilibrarse con la reapertura, que detecta cierres prematuros, y con la satisfacción.

#### 10. ¿Cómo debe informarse el cumplimiento del SLA en el seguimiento del contrato?

- a) Por separado para respuesta y para resolución y segmentado por prioridad, porque la media global oculta lo crítico.
- b) Como una única media global de todos los tiques del mes, que es la cifra que mejor resume el servicio prestado.
- c) Solo mediante el tiempo de respuesta, porque el de resolución depende del usuario y no es imputable al proveedor.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §3.3.1

Una media global puede esconder un mal comportamiento en las incidencias críticas; además, vigilar solo el SLA incentiva abusar del estado «en espera del usuario» para detener el reloj.
