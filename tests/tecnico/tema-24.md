# Test del tema 24. Desarrollo para dispositivos móviles

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-24.html>

## Batería de preguntas

### 1. ¿Qué define a una aplicación móvil nativa?

- a) Se desarrolla con el SDK oficial de cada plataforma y se compila a código ejecutable por ella
- b) Se escribe en HTML, CSS y JavaScript y se ejecuta dentro de un WebView empaquetado
- c) Se distribuye exclusivamente fuera de las tiendas de aplicaciones

**Respuesta correcta:** a) · **Referencia:** §1.2.1 [ANDROID-DEV]

Nativo significa Kotlin o Java con Android Studio para Android, y Swift u Objective-C con Xcode para iOS, usando los componentes de interfaz del propio sistema.

### 2. ¿Cuál es el rasgo técnico distintivo de una aplicación híbrida de contenedor web?

- a) Compila el código fuente a lenguaje máquina de cada plataforma
- b) La interfaz se renderiza dentro de un WebView embebido en una app nativa mínima
- c) Utiliza componentes nativos del sistema controlados desde JavaScript

**Respuesta correcta:** b) · **Referencia:** §1.2.2 [CORDOVA-DOC]

Cordova, Ionic y Capacitor empaquetan la aplicación web dentro de un contenedor nativo cuya única pantalla es un WebView a pantalla completa.

### 3. ¿Qué dos piezas convierten una aplicación web en una PWA?

- a) El fichero de manifiesto de Android y el fichero Info.plist
- b) Un plugin de Cordova y un puente asíncrono
- c) El Service Worker y el Web App Manifest

**Respuesta correcta:** c) · **Referencia:** §1.2.3 [SERVICE-WORKERS] [WEB-APP-MANIFEST]

El Service Worker actúa como proxy de red y permite funcionar sin conexión; el manifiesto aporta los metadatos de instalación en la pantalla de inicio. Ambos exigen HTTPS.

### 4. La fragmentación es una característica típicamente asociada a:

- a) iOS, por la variedad de versiones de Swift
- b) Android, por la diversidad de fabricantes, tamaños de pantalla, densidades y versiones del sistema
- c) Las PWA, por la diversidad de servidores web

**Respuesta correcta:** b) · **Referencia:** §1.1 [ANDROID-DEV]

Al ser un sistema abierto adaptado por múltiples fabricantes, Android obliga al desarrollador a absorber esa diversidad con recursos alternativos y bibliotecas de compatibilidad.

### 5. Respecto a los permisos sensibles (cámara, localización, micrófono) en las versiones modernas de Android e iOS:

- a) Se conceden en tiempo de ejecución y el usuario puede revocarlos en cualquier momento
- b) Se conceden de forma definitiva durante la instalación de la aplicación
- c) Los concede automáticamente la tienda tras revisar la aplicación

**Respuesta correcta:** a) · **Referencia:** §1.1.1 [ANDROID-DEV] [APPLE-DEV]

Desde Android 6.0 (API 23) y en iOS moderno, la app debe pedirlos al usarlos y funcionar de forma degradada si se deniegan, sin fallar.

### 6. ¿Cuáles son los elementos que más batería consumen en un dispositivo móvil?

- a) El sistema de ficheros y la caché de la aplicación
- b) El almacén seguro de credenciales y el cifrado en reposo
- c) La pantalla, la radio de comunicaciones y el GPS

**Respuesta correcta:** c) · **Referencia:** §1.1.2 [ANDROID-DEV]

De ahí las técnicas de agrupación de transferencias y de diferimiento del trabajo no urgente: activar la radio tiene un coste fijo elevado que penaliza muchos envíos pequeños y dispersos.

### 7. ¿Qué consecuencia directa tiene para el programador la limitación de memoria de un dispositivo móvil?

- a) Que no se pueden usar bases de datos relacionales en el dispositivo
- b) Que la aplicación debe cifrar toda la información que guarde en disco
- c) Que el sistema puede terminar la aplicación en segundo plano y esta debe poder restaurar su estado

**Respuesta correcta:** c) · **Referencia:** §1.1.2 [ANDROID-DEV] [APPLE-DEV]

El sistema sacrifica procesos para liberar memoria, por lo que el estado debe guardarse al perder el primer plano y no confiarse a un evento de cierre.

### 8. El diálogo ANR (<em>Application Not Responding</em>) de Android aparece cuando:

- a) El hilo principal permanece bloqueado durante varios segundos
- b) La aplicación solicita un permiso que el usuario ha denegado
- c) La firma digital del paquete no coincide con la registrada

**Respuesta correcta:** a) · **Referencia:** §2.1.1 [ANDROID-DEV]

Toda operación de red o de entrada/salida debe ejecutarse fuera del hilo principal. En iOS el equivalente es la congelación de la interfaz y el posible cierre por el watchdog del sistema.

### 9. ¿Qué requisito impone el uso de Service Workers en una PWA?

- a) Estar publicada previamente en Google Play o en la App Store
- b) Servir la aplicación mediante HTTPS, es decir, en un contexto seguro
- c) Disponer de un certificado de firma emitido por Apple

**Respuesta correcta:** b) · **Referencia:** §1.2.3 [SERVICE-WORKERS]

Los navegadores solo registran Service Workers en contextos seguros, precisamente porque interceptan todas las peticiones de red de la aplicación.

### 10. Señale la afirmación correcta sobre las PWA frente a las aplicaciones de tienda:

- a) No pasan por revisión ni por las tiendas, pero su acceso al hardware es limitado y desigual entre plataformas
- b) Ofrecen el mismo acceso al hardware que una aplicación nativa en cualquier plataforma
- c) Deben firmarse con la clave de desarrollador antes de instalarse desde el navegador

**Respuesta correcta:** a) · **Referencia:** §1.2.3 [MDN-PWA]

Se instalan desde el navegador, lo que agiliza la distribución, pero pierden visibilidad en el catálogo de las tiendas y capacidades del dispositivo, con más restricciones históricas en iOS.

### 11. En una aplicación móvil, ¿quién decide cuándo se detiene o se destruye la aplicación?

- a) La propia aplicación, mediante su método principal de finalización
- b) La tienda de aplicaciones, según la política de la plataforma
- c) El sistema operativo; el programador solo reacciona implementando los métodos de ciclo de vida

**Respuesta correcta:** c) · **Referencia:** §2.1 [ANDROID-LIFECYCLE] [APPLE-DEV]

Es la diferencia estructural más importante frente al desarrollo de escritorio: la aplicación no es dueña de su propia ejecución.

### 12. ¿Qué ocurre por defecto en Android al girar el dispositivo?

- a) La Activity conserva íntegramente su estado sin intervención del programador
- b) La Activity se destruye y se recrea, por lo que el estado debe guardarse expresamente
- c) El sistema suspende la Activity hasta que el usuario devuelve el dispositivo a su orientación anterior

**Respuesta correcta:** b) · **Referencia:** §2.1.1 [ANDROID-LIFECYCLE] [JETPACK]

Los cambios de configuración recrean la Activity. El estado transitorio se conserva con onSaveInstanceState() y el estado más amplio, en un ViewModel.

### 13. ¿En qué callback de una Activity de Android conviene liberar recursos exclusivos como la cámara o el GPS?

- a) En onPause(), porque es el primer aviso de que se ha perdido el foco
- b) En onCreate(), antes de inflar el diseño
- c) En onDestroy(), porque es el único punto garantizado

**Respuesta correcta:** a) · **Referencia:** §2.1.1 [ANDROID-LIFECYCLE]

Además, onPause() debe ser muy breve. onDestroy() no está garantizado: si el sistema mata el proceso, puede no llegar a ejecutarse.

### 14. El estado <em>Suspended</em> de una aplicación iOS significa que:

- a) La aplicación ha sido desinstalada y debe volver a descargarse de la App Store
- b) La aplicación está en primer plano pero no recibe eventos táctiles
- c) La aplicación permanece en memoria pero no ejecuta código, y el sistema puede terminarla sin aviso

**Respuesta correcta:** c) · **Referencia:** §2.1.1 [APPLE-DEV]

Por eso el estado debe persistirse al pasar a segundo plano. El estado en primer plano sin recibir eventos es <em>Inactive</em>.

### 15. ¿Qué motor de base de datos embebido sustenta la persistencia estructurada local tanto en Android como en iOS?

- a) PostgreSQL en modo cliente ligero
- b) SQLite, sin proceso servidor y con la base de datos en un único fichero
- c) MongoDB Mobile, sobre documentos JSON

**Respuesta correcta:** b) · **Referencia:** §2.1.2 [SQLITE] [JETPACK] [COREDATA]

Room en Android y Core Data o SwiftData en iOS se apoyan en SQLite, añadiendo una capa de mapeo objeto-relacional.

### 16. ¿Dónde deben almacenarse las credenciales y los tokens de sesión de una aplicación móvil?

- a) En el Keystore de Android o en el Keychain de iOS
- b) En SharedPreferences o UserDefaults, cifrando el nombre de la clave
- c) En un fichero de texto dentro del almacenamiento externo compartido

**Respuesta correcta:** a) · **Referencia:** §2.1.2 [OWASP-MOBILE] [OWASP-MASVS]

El almacenamiento inseguro de datos es uno de los riesgos clásicos del OWASP Mobile Top 10. Las preferencias y los ficheros en claro nunca son sitio para secretos.

### 17. El <em>sandbox</em> de una aplicación móvil es:

- a) Un entorno de pruebas de la tienda donde se validan las aplicaciones antes de publicarse
- b) Un espacio de almacenamiento y ejecución privado y aislado, inaccesible para otras aplicaciones
- c) Un servicio en la nube donde se replican automáticamente los datos de la aplicación

**Respuesta correcta:** b) · **Referencia:** §2.1.2 [ANDROID-ARCH] [APPLE-ARCH]

Se elimina al desinstalar la app. En Android se apoya en que cada aplicación es un usuario distinto del kernel Linux.

### 18. ¿Qué diferencia hay entre las unidades dp y sp en Android?

- a) Ninguna: son sinónimos y se usan indistintamente
- b) dp se usa para el texto y sp para los márgenes y los iconos
- c) sp es como dp pero además se escala con el tamaño de fuente elegido por el usuario, por lo que se usa para el texto

**Respuesta correcta:** c) · **Referencia:** §2.2.1 [ANDROID-UI]

Medir el texto en dp impediría que la persona que amplía la letra del sistema pueda leer la aplicación: es un defecto de accesibilidad.

### 19. Una aplicación móvil del Ayuntamiento de Madrid está obligada a cumplir requisitos de accesibilidad en virtud de:

- a) El Real Decreto 1112/2018, que extiende la accesibilidad del sector público a las aplicaciones para dispositivos móviles
- b) El Reglamento General de Protección de Datos, en su capítulo de accesibilidad universal
- c) El Esquema Nacional de Interoperabilidad, en su norma técnica de digitalización

**Respuesta correcta:** a) · **Referencia:** §2.2.1 [RD1112-2018] [EN301549]

Transpone la Directiva (UE) 2016/2102 y toma como referencia técnica la norma EN 301 549, que incorpora las WCAG en nivel AA.

### 20. ¿Qué atributo permite que un lector de pantalla anuncie el propósito de un icono sin texto visible en Android?

- a) El atributo placeholder del elemento
- b) El atributo contentDescription
- c) El atributo accessibilityLabel

**Respuesta correcta:** b) · **Referencia:** §2.2.1 [ANDROID-A11Y] [APPLE-DEV]

Es el equivalente de Android para TalkBack. El atributo accessibilityLabel es el propio de iOS para VoiceOver: ambos cumplen la misma función en su plataforma.

### 21. ¿Qué componentes reutilizan las celdas que salen de pantalla para recorrer listas largas con memoria constante?

- a) ConstraintLayout en Android y Auto Layout en iOS
- b) Intent en Android y segue en iOS
- c) RecyclerView en Android y UITableView o UICollectionView en iOS

**Respuesta correcta:** c) · **Referencia:** §2.2.2 [ANDROID-UI] [APPLE-DEV]

El reciclado de vistas evita crear un objeto por elemento, que es lo que permite desplazarse por miles de registros sin agotar la memoria.

### 22. Jetpack Compose y SwiftUI son:

- a) Los frameworks declarativos de interfaz de Android y de iOS respectivamente, ambos de desarrollo nativo
- b) Dos frameworks multiplataforma que permiten compilar la misma interfaz para Android y para iOS
- c) Dos motores de renderizado gráfico basados en Skia

**Respuesta correcta:** a) · **Referencia:** §2.2.2 [ANDROID-UI] [SWIFTUI-DOC]

Sustituyen a los diseños XML con View y a UIKit con storyboards, pero cada uno sigue siendo específico de su plataforma.

### 23. Al consumir una API REST desde una aplicación móvil, ¿qué situación debe tratarse como habitual y no como excepcional?

- a) Que el servidor devuelva un código de estado 200
- b) Que el usuario revoque el permiso de cámara durante la petición
- c) Que no haya red o se agote el tiempo de espera

**Respuesta correcta:** c) · **Referencia:** §2.3.1 [RFC9110]

La conectividad móvil es intermitente por naturaleza: la ausencia de red es un caso normal de funcionamiento, no un error puntual, y la interfaz debe contemplarlo.

### 24. Según la RFC 8252 (<em>OAuth 2.0 for Native Apps</em>), la forma correcta de autenticar al usuario en una aplicación móvil es:

- a) Mostrar un formulario propio dentro de la app que envíe usuario y contraseña al servidor
- b) Usar el navegador del sistema con el flujo de código de autorización y PKCE
- c) Incrustar un WebView con la página de acceso del proveedor de identidad

**Respuesta correcta:** b) · **Referencia:** §2.3.1 [RFC8252] [RFC7636]

Un WebView embebido permitiría a la aplicación leer las credenciales del usuario y rompe el aislamiento de sesión, por lo que está expresamente desaconsejado.

### 25. En una notificación push, ¿quién entrega el mensaje al dispositivo?

- a) El servicio de la plataforma (FCM en Android o APNs en iOS), usando el token de registro
- b) El servidor de la aplicación, abriendo una conexión directa con el dispositivo
- c) La tienda de aplicaciones, tras verificar la firma del mensaje

**Respuesta correcta:** a) · **Referencia:** §2.3.2 [FCM] [APNS]

El servidor de la aplicación envía el mensaje al servicio de la plataforma indicando el token; es ese servicio, con su conexión persistente, quien lo entrega al dispositivo.

### 26. ¿Qué caracteriza a una notificación local frente a una notificación push?

- a) Solo puede mostrarse cuando la aplicación está en primer plano
- b) La programa la propia aplicación en el dispositivo, sin servidor ni conexión de red
- c) Requiere un token de registro emitido por APNs o por FCM

**Respuesta correcta:** b) · **Referencia:** §2.3.2 [FCM] [APNS]

Es la adecuada para recordatorios y alarmas. Al usuario le llega igual que una push, pero su origen y sus requisitos técnicos son distintos.

### 27. En el patrón <em>offline-first</em>, ¿cuál es la única fuente de verdad para la interfaz?

- a) La respuesta más reciente del servidor, almacenada en memoria
- b) La caché HTTP del sistema operativo
- c) El repositorio local del dispositivo, que la interfaz lee y escribe siempre

**Respuesta correcta:** c) · **Referencia:** §2.3.2 [JETPACK]

La pantalla nunca espera a la red: pinta lo que hay en local y un planificador de trabajo diferido sincroniza con el servidor cuando se dan las condiciones.

### 28. Para evitar que un reintento tras un corte de red duplique un registro en el servidor, la solución correcta es:

- a) Enviar un identificador único de operación que el servidor trate como clave de idempotencia
- b) Impedir que el usuario pulse el botón de envío más de una vez
- c) Sustituir el método POST por GET en la petición de creación

**Respuesta correcta:** a) · **Referencia:** §2.3.2 [RFC9110]

Si el identificador ya existe, el servidor devuelve el registro creado en lugar de crear otro. Solo entonces reintentar deja de ser peligroso, que es la condición del modo offline.

### 29. ¿Qué planificadores permiten ejecutar trabajo diferido respetando las restricciones de batería del sistema?

- a) Broadcast Receiver en Android y segue en iOS
- b) WorkManager en Android y BGTaskScheduler en iOS
- c) Content Provider en Android y Core Data en iOS

**Respuesta correcta:** b) · **Referencia:** §2.3.2 [JETPACK] [APPLE-DEV]

Ambos delegan en el sistema la decisión de cuándo ejecutar la tarea, atendiendo a la red disponible, la batería y las políticas de ahorro de energía.

### 30. Ordene de abajo arriba las capas de la plataforma Android:

- a) Núcleo Linux, Java API Framework, HAL, bibliotecas nativas y ART, aplicaciones
- b) HAL, núcleo Linux, aplicaciones, bibliotecas nativas y ART, Java API Framework
- c) Núcleo Linux, HAL, bibliotecas nativas y ART, Java API Framework, aplicaciones

**Respuesta correcta:** c) · **Referencia:** §3.1.1 [ANDROID-ARCH]

El kernel Linux está en la base y las aplicaciones en la cima, con la capa de abstracción de hardware sobre el núcleo y el entorno de ejecución junto a las bibliotecas nativas.

### 31. ¿Qué relación existe entre Dalvik y ART?

- a) ART es el formato de bytecode y Dalvik el entorno que lo ejecuta
- b) ART sustituyó a Dalvik desde Android 5.0, añadiendo compilación AOT en la instalación junto a JIT y perfiles
- c) Ambos coexisten: Dalvik ejecuta las aplicaciones del sistema y ART las de terceros

**Respuesta correcta:** b) · **Referencia:** §3.1.1 [ANDROID-ARCH]

Dalvik, vigente hasta Android 4.4, compilaba únicamente JIT en cada ejecución. El formato de bytecode sigue siendo DEX en ambos casos.

### 32. ¿Cuáles son los cuatro componentes fundamentales de una aplicación Android?

- a) Activity, Service, Broadcast Receiver y Content Provider
- b) Activity, Intent, Fragment y Manifest
- c) View, ViewModel, Repository y Database

**Respuesta correcta:** a) · **Referencia:** §3.1.2 [ANDROID-DEV]

Todos se declaran en el AndroidManifest.xml y se activan mediante Intents. Una app Android no tiene un método principal único de entrada.

### 33. Un Intent implícito se caracteriza por:

- a) Nombrar la clase concreta del componente que debe atenderlo
- b) Ejecutarse siempre de forma síncrona y bloqueante
- c) Describir una acción y unos datos, siendo el sistema quien decide qué aplicación la atiende

**Respuesta correcta:** c) · **Referencia:** §3.1.2 [ANDROID-DEV]

Los intent filters declarados en el manifiesto anuncian qué intents implícitos sabe atender cada aplicación; si hay varias candidatas, el sistema muestra un selector.

### 34. ¿Qué fichero declara en Android los componentes, los permisos y las versiones mínima y objetivo de la API?

- a) El AndroidManifest.xml
- b) El fichero build.gradle del módulo de aplicación
- c) El fichero Info.plist del proyecto

**Respuesta correcta:** a) · **Referencia:** §3.1.2 [ANDROID-DEV]

El fichero build.gradle define la construcción y las variantes, pero la declaración formal de la aplicación ante el sistema es el manifiesto. Info.plist es el equivalente de iOS.

### 35. Los permisos clasificados como <em>peligrosos</em> en Android:

- a) Se conceden automáticamente al instalar la aplicación desde Google Play
- b) Deben solicitarse en tiempo de ejecución y el usuario puede concederlos solo mientras usa la app o solo una vez
- c) Requieren que la aplicación esté firmada con el mismo certificado que la que los declara

**Respuesta correcta:** b) · **Referencia:** §3.1.2 [ANDROID-DEV]

Los que se conceden automáticamente son los permisos normales; los que exigen firma coincidente son los permisos de firma.

### 36. Sobre Kotlin en el desarrollo Android, es cierto que:

- a) Sustituyó por completo a Java, que ya no está soportado por el SDK
- b) Se ejecuta sobre una máquina virtual propia, distinta de la que ejecuta el código Java
- c) Es el lenguaje preferente desde 2019, compila al mismo bytecode que Java y es plenamente interoperable con él

**Respuesta correcta:** c) · **Referencia:** §3.1.3 [KOTLIN-DOC] [ANDROID-DEV]

Oficial desde 2017 y preferente desde 2019, permite migrar una aplicación existente clase a clase, sin reescribirla de golpe.

### 37. ¿Qué aporta la seguridad frente a nulos (<em>null safety</em>) de Kotlin?

- a) El sistema de tipos distingue los tipos que admiten nulo de los que no, y el compilador impide desreferenciar un nulo
- b) El recolector de basura elimina automáticamente las referencias nulas en tiempo de ejecución
- c) Todas las variables se inicializan a un valor por defecto no nulo al declararse

**Respuesta correcta:** a) · **Referencia:** §3.1.3 [KOTLIN-DOC]

Es la respuesta directa a la excepción de puntero nulo, el error más común en Java. Swift resuelve lo mismo con sus opcionales.

### 38. Ordene de arriba abajo las cuatro capas de iOS:

- a) Core OS, Core Services, Media, Cocoa Touch
- b) Cocoa Touch, Core Services, Media, Core OS
- c) Cocoa Touch, Media, Core Services, Core OS

**Respuesta correcta:** c) · **Referencia:** §3.2.1 [APPLE-ARCH]

Cocoa Touch es la capa superior, donde viven UIKit y SwiftUI; Core OS es la más cercana al hardware, con el núcleo Darwin y la seguridad del sistema.

### 39. El equivalente funcional de una Activity de Android en iOS es:

- a) El objeto UIApplication
- b) El UIViewController
- c) El fichero Info.plist

**Respuesta correcta:** b) · **Referencia:** §3.2.2 [APPLE-DEV]

Controla una pantalla, coordinando las vistas y los datos, con sus propios callbacks de ciclo de vida como viewDidLoad() y viewWillAppear().

### 40. Si una aplicación iOS solicita acceso a la cámara sin declarar la cadena de descripción de uso en Info.plist:

- a) Falla en ejecución y, además, es motivo de rechazo en la revisión de la App Store
- b) Funciona con normalidad, porque la descripción solo afecta a la ficha de la tienda
- c) El sistema muestra una descripción genérica automática y concede el permiso

**Respuesta correcta:** a) · **Referencia:** §3.2.2 [APPLE-DEV] [APPSTORE-REVIEW]

La cadena se muestra literalmente al usuario en el diálogo de consentimiento y debe justificar la finalidad del acceso.

### 41. ¿Qué mecanismo de gestión de memoria emplea Swift?

- a) Un recolector de basura generacional equivalente al de ART
- b) Liberación manual de memoria mediante instrucciones explícitas del programador
- c) ARC, conteo automático de referencias resuelto en tiempo de compilación

**Respuesta correcta:** c) · **Referencia:** §3.2.3 [SWIFT-DOC]

Evita las pausas de un recolector de basura, pero obliga al programador a romper los ciclos de retención con referencias weak o unowned.

### 42. En una aplicación construida con Apache Cordova, ¿cómo accede el código JavaScript al GPS del dispositivo?

- a) Directamente, porque el WebView expone la API nativa de localización sin intermediarios
- b) A través de un plugin con parte nativa, mediante un puente de comunicación asíncrono
- c) Solicitando al servidor la posición del dispositivo y recibiéndola en la respuesta

**Respuesta correcta:** b) · **Referencia:** §4.1.1 [CORDOVA-DOC]

Sin plugin no hay acceso al hardware: es la principal dependencia y el principal riesgo de mantenimiento de este enfoque.

### 43. Los ficheros HTML, CSS y JavaScript de una aplicación híbrida de contenedor web:

- a) Van empaquetados dentro del binario instalado, no se descargan de un servidor en cada uso
- b) Se descargan del servidor en cada arranque, como en cualquier página web
- c) Se compilan a código máquina durante la instalación en el dispositivo

**Respuesta correcta:** a) · **Referencia:** §4.1.1 [CORDOVA-DOC]

Es lo que permite que la aplicación arranque y funcione sin conexión, y lo que la distingue de abrir la misma web en el navegador.

### 44. ¿Qué aporta Ionic sobre el modelo de contenedor web?

- a) Un motor de renderizado gráfico propio que sustituye al WebView
- b) Un catálogo de componentes de interfaz web que imitan el aspecto nativo de cada plataforma
- c) La compilación del código JavaScript a Kotlin y a Swift

**Respuesta correcta:** b) · **Referencia:** §4.1.1 [IONIC-DOC] [CAPACITOR-DOC]

Se muestran al estilo Material en Android y al estilo iOS en Apple, e integra frameworks web como Angular, React o Vue. Para la capa nativa impulsa hoy Capacitor.

### 45. ¿Con qué se corresponde un componente <code>&lt;View&gt;</code> de React Native en el dispositivo?

- a) Con un elemento HTML dentro de un WebView embebido
- b) Con una superficie dibujada por el motor gráfico Skia
- c) Con un componente nativo real del sistema: un ViewGroup en Android o un UIView en iOS

**Respuesta correcta:** c) · **Referencia:** §4.2.1 [RN-DOC]

React Native no usa WebView: el código JavaScript maneja componentes nativos, y por eso la aplicación hereda el aspecto y el comportamiento del sistema anfitrión.

### 46. En la nueva arquitectura de React Native, ¿qué sustituye al puente asíncrono con serialización JSON?

- a) JSI, una capa en C++ que permite a JavaScript invocar directamente objetos nativos
- b) Un WebView optimizado con aceleración por hardware
- c) La compilación anticipada del código JavaScript a bytecode DEX

**Respuesta correcta:** a) · **Referencia:** §4.2.1 [RN-DOC]

Sobre JSI se apoyan Fabric, el nuevo renderizador de interfaz, los TurboModules de carga perezosa y Codegen. Elimina el cuello de botella de la serialización.

### 47. ¿Cuál es la diferencia esencial entre React Native y Flutter?

- a) React Native es de código abierto y Flutter es una tecnología propietaria de pago
- b) React Native renderiza con componentes nativos del sistema, mientras que Flutter dibuja cada píxel con su propio motor gráfico
- c) React Native solo funciona en Android y Flutter solo en iOS

**Respuesta correcta:** b) · **Referencia:** §4.2 [RN-DOC] [FLUTTER-DOC]

De ahí que Flutter garantice una apariencia idéntica en todas las plataformas y React Native, una apariencia idéntica a la del sistema anfitrión.

### 48. ¿Cuáles son las tres capas de la arquitectura de Flutter?

- a) WebView, puente de plugins y aplicación contenedora
- b) Presentación, lógica de negocio y acceso a datos
- c) Framework en Dart, Engine en C/C++ y Embedder específico de cada plataforma

**Respuesta correcta:** c) · **Referencia:** §4.2.2 [FLUTTER-DOC]

El Framework contiene los widgets que usa el programador; el Engine incorpora el motor de renderizado Skia o Impeller; el Embedder es la única parte específica de Android o iOS.

### 49. ¿Qué característica del lenguaje Dart hace posible la recarga en caliente (<em>hot reload</em>) durante el desarrollo?

- a) Que se interpreta línea a línea también en producción, sin fase de compilación
- b) Que compila JIT durante el desarrollo y AOT a código máquina en producción
- c) Que se ejecuta sobre la máquina virtual de Java, compartiendo su cargador de clases

**Respuesta correcta:** b) · **Referencia:** §4.2.2 [DART-DOC]

La doble estrategia de compilación permite ver los cambios en menos de un segundo mientras se desarrolla, sin renunciar al rendimiento cercano al nativo en la versión publicada.

### 50. Una desventaja característica de que Flutter dibuje su propia interfaz es:

- a) Que no hereda automáticamente los cambios de aspecto y comportamiento que introduce cada versión nueva del sistema
- b) Que obliga a escribir una base de código distinta para Android y para iOS
- c) Que impide utilizar componentes de diseño con estilo Material

**Respuesta correcta:** a) · **Referencia:** §4.2.2 [FLUTTER-DOC]

A ello se suma un paquete de mayor tamaño, porque incorpora el motor de renderizado, y una accesibilidad que depende del puente propio de Flutter.

### 51. Kotlin Multiplatform se caracteriza por:

- a) Ejecutar HTML y JavaScript dentro de un WebView en ambas plataformas
- b) Compilar el mismo código de interfaz para Android, iOS y web con un motor gráfico propio
- c) Compartir la lógica de negocio en Kotlin manteniendo una interfaz nativa en cada plataforma

**Respuesta correcta:** c) · **Referencia:** §4.2.2 [KMP-DOC]

Es un compromiso intermedio entre el desarrollo nativo puro y la multiplataforma total, que preserva la experiencia de usuario propia de cada sistema.

### 52. .NET MAUI, sucesor de Xamarin.Forms, utiliza como lenguaje:

- a) Dart
- b) C#
- c) TypeScript

**Respuesta correcta:** b) · **Referencia:** §4.2.2 [MAUI-DOC]

Renderiza con controles nativos de cada plataforma y resulta especialmente atractivo cuando la organización ya trabaja sobre el ecosistema .NET.

### 53. Ordene de mayor a menor rendimiento los enfoques de desarrollo móvil:

- a) Nativo, Flutter, React Native, híbrido de contenedor web
- b) Híbrido de contenedor web, React Native, Flutter, nativo
- c) React Native, nativo, híbrido de contenedor web, Flutter

**Respuesta correcta:** a) · **Referencia:** §5.1 [ISO25010]

Cuantas más capas intermedias e interpretación existan, más ciclos de CPU y más memoria se consumen para el mismo resultado, y mayor es también el gasto de batería.

### 54. Respecto a una clave de API incrustada en el código de una aplicación móvil publicada:

- a) Es segura si el código se ofusca antes de compilar
- b) Es segura si se guarda en un fichero de recursos y no en una constante del código
- c) Debe considerarse comprometida, porque el paquete instalado es analizable por ingeniería inversa

**Respuesta correcta:** c) · **Referencia:** §5.1 [OWASP-MASVS] [OWASP-MOBILE]

Las comprobaciones de seguridad decisivas se hacen siempre en el servidor: el cliente es manipulable por definición.

### 55. El catálogo de referencia de los riesgos de seguridad más críticos específicos de aplicaciones móviles es:

- a) El OWASP Mobile Top 10, complementado por el estándar de verificación MASVS
- b) La norma EN 301 549, en su capítulo 11
- c) El Esquema Nacional de Interoperabilidad, en su norma técnica de seguridad

**Respuesta correcta:** a) · **Referencia:** §5.1 [OWASP-MOBILE] [OWASP-MASVS]

Recoge riesgos como el almacenamiento inseguro de datos, la comunicación insegura y la autenticación deficiente. La EN 301 549 es la norma de accesibilidad.

### 56. Sobre la afirmación «una sola base de código supone la mitad de trabajo»:

- a) Es exacta: el ahorro es del 50 % en desarrollo y en mantenimiento
- b) Es inexacta: sigue habiendo que probar en ambas plataformas, adaptar comportamientos específicos, gestionar dos publicaciones y, a veces, escribir código nativo
- c) Es inexacta porque los enfoques multiplataforma no permiten reutilizar código entre Android e iOS

**Respuesta correcta:** b) · **Referencia:** §5.2 [ISO25010]

El ahorro real es significativo pero no llega al 50 %, y el coste dominante a medio plazo es el mantenimiento, no el desarrollo inicial.

### 57. Respecto a las pruebas en el desarrollo móvil:

- a) El emulador reproduce fielmente el rendimiento, los sensores y el consumo de batería del dispositivo real
- b) Basta con probar en un único dispositivo Android, porque el sistema garantiza el comportamiento uniforme
- c) El emulador no sustituye al dispositivo real y la fragmentación de Android obliga a probar sobre una matriz de tamaños, densidades y versiones

**Respuesta correcta:** c) · **Referencia:** §5.2 [ANDROID-DEV]

Cuando no se dispone del parque físico se recurre a granjas de dispositivos en la nube.

### 58. ¿Qué formato de publicación es obligatorio en Google Play para las aplicaciones nuevas desde agosto de 2021?

- a) El AAB (<em>Android App Bundle</em>), a partir del cual Google Play genera los APK optimizados por dispositivo
- b) El APK firmado con la clave de subida del desarrollador
- c) El IPA generado desde el entorno de desarrollo

**Respuesta correcta:** a) · **Referencia:** §5.3 [PLAY-CONSOLE]

El AAB reduce el tamaño de descarga al servir a cada dispositivo solo los recursos que necesita: su densidad, su arquitectura y su idioma. El IPA es el formato de la App Store.

### 59. Una diferencia relevante entre publicar en Google Play y en la App Store es que:

- a) Google Play exige una cuota anual y la App Store un pago único de alta
- b) La App Store somete toda aplicación a revisión humana, mientras que en Google Play la revisión es mayoritariamente automatizada
- c) Solo la App Store permite la publicación por fases a un porcentaje creciente de usuarios

**Respuesta correcta:** b) · **Referencia:** §5.3 [PLAY-CONSOLE] [APPSTORE-REVIEW]

Además, la cuota es al revés de lo que sugiere la primera opción: pago único en Google Play y cuota anual en el Apple Developer Program. Ambas admiten publicación por fases.

### 60. A diferencia de una aplicación web, en una aplicación móvil publicada en una tienda:

- a) La actualización es instantánea para todos los usuarios en cuanto se publica
- b) No es necesario versionar la API del servidor, porque todos los clientes están siempre al día
- c) El usuario puede tardar semanas en actualizar o no actualizar nunca, por lo que hay que versionar la API y mantener compatibilidad hacia atrás

**Respuesta correcta:** c) · **Referencia:** §5.3 [PLAY-CONSOLE] [APPSTORE-REVIEW]

Por eso se recomienda además la publicación por fases y las banderas de característica, que permiten desactivar una funcionalidad sin depender de una actualización de la tienda.

## Preguntas sobre los casos prácticos

### Caso 1. Elección de enfoque para la app de avisos ciudadanos

#### 1. Al comparar las cuatro estrategias para la app de avisos, ¿en cuál de ellas la interfaz la dibuja un motor gráfico propio que pinta cada píxel?

- a) En la multiplataforma compilada con Flutter, que renderiza con su propio motor (Skia/Impeller).
- b) En la híbrida de contenedor web, que renderiza la interfaz con el motor del WebView embebido.
- c) En la nativa, que pinta cada píxel con Kotlin en Android y con Swift en iOS sin usar componentes.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §1.2

Flutter no usa los componentes del sistema: trae su propio motor gráfico y dibuja cada píxel sobre un lienzo.

#### 2. Si el proveedor desarrollara la app de avisos con React Native, ¿cómo se dibujaría su interfaz?

- a) Con HTML, CSS y JavaScript renderizados dentro de un WebView a pantalla completa.
- b) Con componentes nativos reales del sistema, manejados desde el código JavaScript.
- c) Con un motor gráfico propio que dibuja cada píxel sin usar los componentes del sistema.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §4.2.1

React Native no usa WebView: un <View> se convierte en un ViewGroup de Android o en un UIView de iOS.

#### 3. Si la app de avisos se construyera como híbrida de contenedor web (Cordova, Ionic o Capacitor), ¿qué dibujaría la interfaz?

- a) El navegador del sistema, sin aplicación nativa que la empaquete ni paso por las tiendas.
- b) Los componentes nativos de Android y de iOS, a los que se traduce el HTML al compilar.
- c) Un WebView embebido en una app nativa mínima, que renderiza el HTML, el CSS y el JavaScript.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §1.2.2

En el híbrido de contenedor web la app es una web empaquetada dentro de una app nativa cuyo único contenido es un WebView.

#### 4. El proveedor propone una PWA para ahorrar costes. ¿Qué requisito funcional del supuesto la hace arriesgada?

- a) El envío del aviso por HTTPS, que los Service Workers de una PWA no permiten utilizar.
- b) Las notificaciones push al resolverse el aviso, con soporte web históricamente tardío y limitado en iOS.
- c) La consulta del estado de los avisos, porque una PWA no puede hacer peticiones al servidor.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §1.2.3

El vecino debe recibir una notificación cuando se resuelve su aviso, y en iOS las notificaciones push web han tenido un soporte más tardío y limitado.

#### 5. Además de las notificaciones, ¿qué otro inconveniente tiene la PWA para una app de avisos dirigida a toda la ciudadanía?

- a) Que no se distribuye por las tiendas, lo que le resta visibilidad ante los vecinos.
- b) Que solo puede instalarse en terminales corporativos gestionados mediante una plataforma MDM.
- c) Que debe pasar la revisión humana de Apple antes de cada actualización publicada en el servidor.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §1.2.3

La PWA se instala desde el navegador: se ahorra la revisión de las tiendas, pero pierde la visibilidad de su catálogo.

#### 6. Con dos plataformas, presupuesto ajustado, seis meses de plazo y un equipo web sin Kotlin ni Swift, ¿qué enfoque procede?

- a) Nativo, con dos equipos especializados, porque es el único que da acceso a cámara y ubicación.
- b) PWA, porque es la única estrategia que puede llegar a Android y a iOS con un solo código.
- c) Multiplataforma compilado (React Native o Flutter): una sola base de código y un solo equipo.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §5.2

Llegar a las dos plataformas con un solo equipo y presupuesto ajustado apunta al multiplataforma compilado; las capacidades que necesita están cubiertas por bibliotecas maduras.

#### 7. Dentro del multiplataforma compilado, ¿qué framework aprovecha directamente la experiencia del equipo municipal?

- a) Flutter, porque Dart es el mismo lenguaje que el JavaScript que ya domina el equipo web.
- b) .NET MAUI, porque se programa en TypeScript con el modelo de componentes de React.
- c) React Native, que reutiliza su conocimiento de JavaScript y del modelo de componentes de React.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §4.2.1

React Native se escribe en JavaScript/TypeScript con el modelo de componentes de React; Flutter usa Dart y .NET MAUI, C#.

#### 8. El perfil web del equipo haría defendible un híbrido de contenedor web. ¿Por qué se descarta en este supuesto?

- a) Porque penalizaría el rendimiento con las listas de avisos y las fotografías.
- b) Porque un híbrido de contenedor web no puede publicarse en Google Play ni en la App Store.
- c) Porque un híbrido de contenedor web no tiene ninguna forma de acceder a la cámara del móvil.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §4.1.1

Toda la interfaz se renderiza en un WebView y cada llamada al hardware atraviesa el puente, lo que se nota en listas largas y gráficos.

#### 9. ¿Cuál es el principal riesgo a medio plazo del enfoque multiplataforma elegido para la app de avisos?

- a) La duplicación del esfuerzo, al tener que mantener dos bases de código sincronizadas funcionalmente.
- b) La dependencia de un tercero: que el framework tarde en soportar una versión nueva de Android o de iOS.
- c) La falta de soporte de los componentes nativos, que React Native sustituye por un WebView propio.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §5.2

Si el framework tarda en soportar una versión nueva del sistema o una biblioteca clave queda sin mantenimiento, el proyecto queda expuesto.

#### 10. ¿Qué medida mitiga ese riesgo en la contratación de la app de avisos?

- a) Elegir un framework con respaldo corporativo y comunidad amplia, y limitar las dependencias de terceros.
- b) Congelar la versión objetivo de la API de Android para no tener que adaptar nunca la aplicación.
- c) Prever la conversión de la app en PWA en cuanto aparezca una versión nueva de iOS.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §5.2

Un framework respaldado y con comunidad, pocas dependencias, mantenimiento evolutivo exigido en el contrato y la opción de escribir módulos nativos reducen la exposición.

### Caso 2. Ciclo de vida, trabajo sin conexión y sincronización

#### 1. Un vecino gira el móvil mientras redacta el aviso y el texto desaparece. ¿Cuál es la causa técnica en Android?

- a) El giro pasa la app al estado Suspended y el sistema la termina para liberar memoria.
- b) El giro es un cambio de configuración que, por defecto, destruye y recrea la Activity.
- c) El giro dispara onPause(), cuya función es vaciar los campos de texto de la pantalla.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §2.1.1

Girar el dispositivo es un cambio de configuración que destruye y recrea la Activity; el estado no guardado se pierde.

#### 2. ¿Qué mecanismos evitan que se borre el texto del aviso al girar el dispositivo?

- a) Guardarlo en onDestroy(), que se ejecuta siempre antes de recrear la Activity, y releerlo en onResume().
- b) Declarar la orientación en el AndroidManifest.xml como permiso peligroso concedido en tiempo de ejecución.
- c) Guardarlo en onSaveInstanceState() con un Bundle y restaurarlo en onCreate(), o conservarlo en un ViewModel.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §2.1.1

El estado transitorio se guarda en un Bundle con onSaveInstanceState() y se restaura en onCreate(); el ViewModel sobrevive a la recreación. onDestroy() puede no llegar a ejecutarse.

#### 3. Para que el vecino del aparcamiento subterráneo no pierda su aviso, ¿de dónde debe leer y escribir siempre la pantalla?

- a) Del repositorio local (SQLite vía Room o Core Data), que es la única fuente de verdad de la interfaz.
- b) De la respuesta más reciente del servidor, guardada en memoria hasta que vuelva la cobertura.
- c) De la caché HTTP del sistema operativo, que almacena los POST pendientes de enviar.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §2.3.2

En el patrón offline-first la interfaz trabaja siempre contra la copia local y nunca espera a la red.

#### 4. ¿Cómo sabe la app qué avisos redactados sin cobertura quedan aún por enviar al servidor?

- a) Porque el servidor los reclama al dispositivo mediante una notificación push en cuanto hay red.
- b) Porque permanecen en el hilo principal, bloqueados, hasta que el sistema detecta la conexión.
- c) Porque forman una cola de operaciones pendientes, con los registros marcados como sincronizado = false.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §2.3.2

La cola de operaciones pendientes registra con una marca de estado lo que aún no ha llegado al servidor.

#### 5. ¿Qué pieza envía los avisos pendientes cuando hay red, batería y el sistema lo permite?

- a) Un Broadcast Receiver en Android y un segue en iOS, que reenvían el aviso al recuperar cobertura.
- b) Un planificador de trabajo diferido del sistema: WorkManager en Android y BGTaskScheduler en iOS.
- c) Un Content Provider en Android y Core Data en iOS, que publican el aviso directamente en la sede.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §2.3.2

WorkManager y BGTaskScheduler ejecutan la sincronización cuando se cumplen las condiciones de red, batería y oportunidad del sistema.

#### 6. Un vecino con mala cobertura pulsa «Enviar» y su aviso aparece duplicado en la sede. ¿Qué ha ocurrido?

- a) El POST llegó al servidor, pero la respuesta se perdió y el cliente reintentó, creando un segundo aviso.
- b) El POST nunca llegó al servidor, que generó por su cuenta dos avisos al recibir la reconexión.
- c) El servidor repite cada POST por diseño para garantizar la entrega a través de redes inalámbricas.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §2.3.2

El cliente interpretó como fallo la falta de respuesta a una petición que sí se había procesado, y al reintentarla creó otro aviso.

#### 7. En la corrección de los duplicados, ¿qué debe hacer la app (el cliente)?

- a) Generar un UUID nuevo en cada reintento, para que el servidor distinga cada intento de envío.
- b) Generar un UUID de operación al crear el aviso y enviarlo idéntico en todos los reintentos.
- c) Dejar de reintentar y pedir al vecino que repita el aviso completo al recuperar la cobertura.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §2.3.2

El identificador debe ser el mismo en todos los reintentos para que el servidor reconozca que se trata de la misma operación.

#### 8. ¿Y qué debe hacer el servidor municipal cuando recibe un aviso con un identificador de operación que ya tiene registrado?

- a) Crear el aviso de nuevo y borrar el duplicado más antiguo mediante un proceso nocturno.
- b) Responder con un error para que la app muestre al vecino que el envío ha fallado.
- c) Tratarlo como clave de idempotencia y devolver el aviso ya creado en lugar de crear otro.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §2.3.2

Con la idempotencia en el servidor, reintentar deja de ser peligroso, que es la condición para que el modo offline sea viable.

#### 9. El envío del aviso se programó llamando a la API desde el manejador del botón. ¿Qué efecto tiene?

- a) Bloquea el hilo principal: en Android aparece el diálogo ANR y en iOS la interfaz se congela.
- b) Obliga a solicitar de nuevo el permiso de red cada vez que el vecino pulsa el botón de envío.
- c) Provoca el rechazo de la app en la revisión de las tiendas por usar una API privada del sistema.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §2.1.1

La interfaz solo puede tocarse desde el hilo principal y este nunca debe bloquearse; si se bloquea, Android muestra el ANR y en iOS el watchdog puede matar la app.

#### 10. ¿Cómo se corrige ese envío en Kotlin y en Swift?

- a) Moviendo la llamada a onPause() en Kotlin y a viewDidLoad() en Swift, que no bloquean la interfaz.
- b) Sustituyendo la llamada REST por un Intent implícito en Kotlin y por un segue en Swift.
- c) Con una corrutina en Dispatchers.IO en Kotlin y con async/await en Swift, devolviendo solo el resultado a la interfaz.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §2.3.1

La petición se ejecuta en un hilo secundario (withContext(Dispatchers.IO) o Task con await) y solo el resultado vuelve al hilo de interfaz.

### Caso 3. Accesibilidad, permisos, seguridad y publicación

#### 1. ¿Qué norma obliga a la app municipal de avisos a ser accesible?

- a) El Reglamento General de Protección de Datos, por su principio de minimización de datos.
- b) El Esquema Nacional de Seguridad, que exige el nivel AA a las aplicaciones del sector público.
- c) El Real Decreto 1112/2018, con la norma EN 301 549 (WCAG en nivel AA) como referencia técnica.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §2.2.1

El RD 1112/2018 extiende la accesibilidad del sector público a las aplicaciones para dispositivos móviles y toma como referencia la EN 301 549.

#### 2. El botón para adjuntar la fotografía es un simple icono. ¿Qué hay que comprobar para que lo use un vecino ciego?

- a) Que tenga contentDescription en Android y accessibilityLabel en iOS, para TalkBack y VoiceOver.
- b) Que el icono tenga un contraste de al menos 4,5:1, que es lo que leen TalkBack y VoiceOver.
- c) Que el icono mida al menos 48×48 dp, tamaño a partir del cual el lector de pantalla lo anuncia.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §2.2.1

Un icono sin etiqueta es invisible para un lector de pantalla: TalkBack lo leería solo como «botón».

#### 3. ¿Cómo deben gestionarse en Android los permisos de cámara y de ubicación de la app?

- a) Son normales: se declaran en el AndroidManifest.xml y el sistema los concede al instalar la app.
- b) Son peligrosos: se declaran en el AndroidManifest.xml y se solicitan en tiempo de ejecución.
- c) Son especiales: el vecino debe activarlos a mano en los ajustes, sin diálogo dentro de la app.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §3.1.2

Cámara y localización afectan a datos personales: se piden en ejecución, comprobando antes si ya están concedidos, y el usuario puede revocarlos.

#### 4. ¿Qué elemento adicional exige iOS para pedir la cámara y la ubicación?

- a) Una cadena de descripción de uso en Info.plist, como NSCameraUsageDescription.
- b) Una capability de notificaciones push en el fichero de entitlements firmado con la app.
- c) Una declaración de cada permiso en el AndroidManifest.xml compartido con la versión de Android.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §3.2.2

La descripción de uso se muestra literalmente al usuario en el diálogo de consentimiento y, si falta, la app se rechaza en la revisión.

#### 5. Un vecino deniega el permiso de ubicación. ¿Cómo debe comportarse la app de avisos?

- a) Bloquear el envío del aviso hasta que el vecino conceda el permiso desde los ajustes.
- b) Cerrarse y mostrar un mensaje que invite a reinstalarla para volver a solicitar el permiso.
- c) Degradarse: ofrecer la introducción manual de la dirección, sin bloquear el envío del aviso.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §1.1.1

La app debe funcionar de forma degradada, sin fallar, cuando se deniega un permiso, y explicar para qué serviría.

#### 6. El proveedor guarda el token de sesión en SharedPreferences. ¿Cómo se corrige?

- a) Trasladándolo a UserDefaults en iOS y a un fichero del almacenamiento externo en Android.
- b) Trasladándolo al Keystore de Android (o al Keychain en iOS), que es almacenamiento seguro.
- c) Manteniéndolo en SharedPreferences, pero cifrando el nombre de la clave con que se guarda.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §2.1.2

Las preferencias no son almacenamiento seguro; credenciales y tokens van al Keystore o al Keychain («almacenamiento inseguro», OWASP Mobile).

#### 7. La clave de la API de mapas está incrustada en una constante del código. ¿Cuál es la corrección adecuada?

- a) Ofuscar el código antes de compilar, para que la clave no pueda leerse en el paquete.
- b) Sacarla del cliente y enrutar las llamadas por el servidor municipal, que custodia la clave.
- c) Moverla a un fichero de recursos de la app, separado del código fuente compilado.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §5.1

Todo secreto embarcado en la app debe considerarse público, porque el paquete instalado es analizable por ingeniería inversa.

#### 8. La comprobación de que el aviso pertenece al ciudadano se hace en la app. ¿Qué problema crea y cómo se resuelve?

- a) Una referencia directa insegura a objetos (IDOR); la autorización se comprueba en el servidor.
- b) Un XSS dentro del WebView; la comprobación se mueve a un plugin nativo de la propia app.
- c) Un almacenamiento inseguro; la comprobación se guarda cifrada en el Keychain del móvil.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §5.1

El cliente es manipulable: las comprobaciones de autorización decisivas se hacen siempre en el servidor.

#### 9. ¿Qué paquete se envía a cada tienda para publicar la app de avisos?

- a) Un IPA a Google Play y un AAB a App Store Connect, ambos firmados con Play App Signing.
- b) Un AAB firmado a Google Play y un IPA generado en Xcode a App Store Connect.
- c) El mismo APK firmado a las dos tiendas, porque la app es multiplataforma compilada.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §5.3

Google Play exige AAB para las apps nuevas desde agosto de 2021; la App Store recibe un IPA enviado desde Xcode a App Store Connect.

#### 10. ¿Qué estrategia de despliegue es la más prudente para la app de avisos?

- a) Publicación simultánea al 100 % en ambas tiendas, para que todos los vecinos actualicen a la vez.
- b) Beta abierta en Google Play y, sin pasar por TestFlight, publicación directa al 100 % en la App Store.
- c) Canal interno y TestFlight, beta cerrada con vecinos y publicación por fases al 5 %, 20 % y 100 %.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §5.3

Desplegar por fases vigilando la tasa de fallos permite detener el despliegue sin afectar a toda la ciudadanía; además hay que reservar margen para la revisión humana de Apple.
