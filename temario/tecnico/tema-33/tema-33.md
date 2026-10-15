# Tema 33. Comunicaciones

**Bloque:** técnico  
**Enunciado oficial** (BOAM n.º 10.032, de 23 de diciembre de 2025): Comunicaciones. Medios de transmisión. Modos de comunicación. Equipos terminales y equipos de interconexión y conmutación. Redes de comunicaciones. Redes de conmutación y redes de difusión. Comunicaciones móviles e inalámbricas.

Versión web: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-33.html> · PDF: [tema-33.pdf](tema-33.pdf) · Test: [../../../tests/tecnico/tema-33.md](../../../tests/tecnico/tema-33.md)

## Índice

- 1. Conceptos generales de telecomunicaciones y modelo de comunicación
  - 1.1. Elementos del sistema de transmisión y perturbaciones en el canal
  - 1.2. Transmisión analógica y digital: ancho de banda y velocidad de transmisión
- 2. Medios de transmisión
  - 2.1. Medios de transmisión guiados
  - 2.2. Medios de transmisión no guiados
  - 2.3. Parámetros de caracterización y calidad en medios de transmisión
- 3. Modos de comunicación
  - 3.1. Modos según la direccionalidad: simplex, half-duplex y full-duplex
  - 3.2. Modos según el sincronismo: transmisión síncrona y asíncrona
  - 3.3. Modos según la forma de transmisión: serie y paralelo
- 4. Equipos terminales y de red
  - 4.1. Equipos terminales de datos y equipos de conversión
  - 4.2. Equipos de interconexión y conmutación de red
- 5. Redes de comunicaciones
  - 5.1. Clasificación por cobertura geográfica: PAN, LAN, MAN y WAN
  - 5.2. Topologías de red físicas y lógicas
- 6. Redes de conmutación y redes de difusión
  - 6.1. Redes de conmutación
  - 6.2. Redes de difusión
- 7. Redes e infraestructuras inalámbricas
  - 7.1. Redes de área personal y local inalámbricas
  - 7.2. Redes de área metropolitana y extensa inalámbricas
- 8. Comunicaciones móviles
  - 8.1. Evolución y arquitectura de redes celulares móviles
  - 8.2. Tecnologías consolidadas y de alta capacidad
- 9. Seguridad y normativa en la Administración Pública
  - 9.1. Aspectos de seguridad e integridad en redes inalámbricas
  - 9.2. Marco normativo y regulatorio de telecomunicaciones en el ámbito público
- Cierre: los ocho datos que no se pueden fallar

### Conceptos clave para memorizar

| Concepto | Dato clave |
|----|----|
| Telecomunicación (definición legal) | *«Toda transmisión, emisión o recepción de signos, señales, escritos, imágenes, sonidos o informaciones de cualquier naturaleza por hilo, radioelectricidad, medios ópticos u otros sistemas electromagnéticos»* — anexo II, apartado **79**, de la Ley 11/2022. Es la definición que hay que poder reproducir |
| Elementos del modelo de Shannon | **Cinco**: fuente → transmisor → **canal** (donde entra el ruido) → receptor → destino. El **ruido** ataca al canal, no al mensaje |
| Perturbaciones del canal | **Atenuación** (pérdida de potencia con la distancia) · **distorsión** (deformación de la señal, típicamente por retardo diferencial) · **ruido** (energía ajena añadida: térmico, de intermodulación, **diafonía** y **impulsivo**) · **interferencia** · **eco**. El ruido **térmico** es inevitable; el **impulsivo** es el más dañino en transmisión digital |
| Ancho de banda vs velocidad | **Ancho de banda** = rango de frecuencias, en **hercios (Hz)**. **Velocidad de transmisión** = bits por segundo (**bps**). **Velocidad de modulación** = símbolos por segundo (**baudios**). **Baudio ≠ bit/s**: solo coinciden si cada símbolo lleva **un** bit |
| Nyquist y Shannon | **Nyquist** (canal sin ruido): `C = 2·B·log₂(M)`. **Shannon** (canal con ruido): `C = B·log₂(1 + S/N)`. Shannon fija el **límite absoluto**; ningún esquema de modulación lo supera |
| Muestreo | **Teorema del muestreo**: `fm ≥ 2·fmax`. La telefonía digital muestrea la voz (300-3.400 Hz) a **8.000 muestras/s** con **8 bits** → **64 kbps**, que es el **canal E0** de la MIC/PCM |
| Módem, códec y adaptador | **Módem** = analógico ↔ digital sobre el medio (modula y demodula). **Códec** = digital ↔ analógico de la fuente (codifica y decodifica). Son operaciones **inversas**, no sinónimos |
| Medios guiados | **Par trenzado** (UTP/FTP/STP, categorías 5e a 8, conector **RJ-45**, **100 m** máximo en Ethernet) · **Coaxial** (malla apantallada, 50 Ω o 75 Ω) · **Fibra óptica** (inmune a interferencias electromagnéticas, sin diafonía, gran ancho de banda) |
| Fibra monomodo vs multimodo | **Multimodo** (**OM1-OM5**, núcleo 50 o 62,5 µm, LED o VCSEL, **distancias cortas**, más barata). **Monomodo** (**OS1/OS2**, núcleo ≈ 9 µm, láser, **decenas o centenares de kilómetros**). A mayor núcleo, más **dispersión modal** y menos alcance |
| Espectro radioeléctrico (definición legal) | *«Ondas electromagnéticas, cuya frecuencia se fija convencionalmente por debajo de 3.000 GHz, que se propagan por el espacio sin guía artificial»* — anexo II.21 de la Ley 11/2022. Es **bien de dominio público**, de titularidad y administración **estatal** (art. 85.1) |
| Bandas de la UIT | VLF, LF, **MF** (ondas medias), **HF** (onda corta, propagación ionosférica), **VHF** (30-300 MHz), **UHF** (300 MHz-3 GHz), **SHF** (3-30 GHz, microondas y satélite), EHF (30-300 GHz, ondas milimétricas). Cada banda decádica multiplica por diez la anterior |
| Regla física clave | **A más frecuencia**: más ancho de banda disponible y más capacidad, pero **menos alcance** y **peor penetración** en obstáculos. Explica por qué el 5G de 700 MHz da cobertura y el de 26 GHz da capacidad |
| Parámetros de calidad | **Ancho de banda** · **latencia** (retardo) · **fluctuación o *jitter*** (variación de la latencia) · **tasa de error de bit (BER)** · **relación señal-ruido (S/N, en dB)** · **atenuación (dB/km)** · **pérdida de paquetes**. El **decibelio** es **logarítmico**: 3 dB ≈ el doble de potencia; 10 dB = diez veces |
| Direccionalidad | **Símplex** (un solo sentido: radiodifusión, TDT) · **semidúplex** o *half-duplex* (los dos sentidos, **alternando**: walkie-talkie, **TETRA**) · **dúplex** o *full-duplex* (los dos sentidos **a la vez**: telefonía, Ethernet conmutado) |
| Síncrona vs asíncrona | **Asíncrona**: carácter a carácter, con **bit de arranque y de parada**, sin reloj común → sobrecarga de **≈ 20-30 %**, barata. **Síncrona**: bloques o tramas con **sincronismo de reloj** y delimitadores, mucho más eficiente en volumen |
| Serie vs paralelo | **Serie**: un bit detrás de otro por un único canal. **Paralelo**: varios bits a la vez por hilos distintos. A alta velocidad **gana el serie**, porque el paralelo sufre **desviación temporal (*skew*) y diafonía**. Por eso PCI Express, SATA, USB y Ethernet son **serie** |
| Equipos terminales (ETD/ETCD) | **ETD (DTE)**: origen o destino de los datos (ordenador, terminal). **ETCD (DCE)**: adapta la señal al medio y suele aportar el reloj (módem, ONT, adaptador de terminal). El límite entre ambos es el **punto de terminación de red** |
| Dispositivos por capa | **Capa 1**: repetidor, concentrador (*hub*), **transceptor**. **Capa 2**: puente, **conmutador (*switch*)**, punto de acceso inalámbrico. **Capa 3**: **encaminador (*router*)**, conmutador de capa 3. **Capas superiores**: **pasarela (*gateway*)**, cortafuegos de aplicación |
| Concentrador vs conmutador | El **concentrador** repite por todos los puertos: **un solo dominio de colisión**, medio compartido, semidúplex. El **conmutador** reenvía **solo al puerto destino** según la tabla MAC: **un dominio de colisión por puerto** y dúplex. **El conmutador NO divide el dominio de difusión**; eso solo lo hacen el **encaminador** o las **VLAN** |
| Dominios de colisión y de difusión | **Repetidor/hub**: 1 dominio de colisión, 1 de difusión. **Switch**: N dominios de colisión (uno por puerto), 1 de difusión. **Router**: N dominios de colisión y **N dominios de difusión** |
| Redes por cobertura | **PAN** (metros: Bluetooth, NFC, Zigbee) · **LAN** (edificio o recinto) · **CAN** (campus) · **MAN** (área metropolitana) · **WAN** (país o continente). Añadidos modernos: **BAN** (corporal), **SAN** (almacenamiento) y **WLAN/WPAN/WMAN/WWAN** para sus versiones inalámbricas |
| Topologías | **Bus** (troncal común, terminadores) · **anillo** (testigo, doble anillo en FDDI) · **estrella** (nodo central; **la más usada en LAN**) · **árbol** (estrella jerárquica) · **malla** (redundante; completa = **n(n−1)/2** enlaces) · **mixta**. Distinguir **topología física** (cableado) de **topología lógica** (recorrido de la señal): Ethernet moderno es **estrella física** con lógica de **bus conmutado** |
| Conmutación de circuitos | Reserva un **camino físico dedicado** durante toda la comunicación. Tres fases: **establecimiento, transferencia y liberación**. Retardo constante, sin fluctuación, pero **desaprovecha** la capacidad en los silencios. Ejemplo canónico: la **RTC** |
| Conmutación de paquetes | Divide en **paquetes** que se encaminan de forma independiente y compiten por el enlace: **multiplexación estadística**, aprovechamiento máximo, pero **fluctuación** y posible pérdida. Dos variantes: **datagrama** (sin conexión, cada paquete decide su ruta, pueden desordenarse) y **circuito virtual** (ruta fijada al inicio, orden garantizado; X.25, Frame Relay, ATM, MPLS) |
| Conmutación de mensajes | **Almacenamiento y reenvío** del mensaje **completo**, sin fragmentar, sin camino reservado. Retardos altos y necesidad de mucha memoria en los nodos: **hoy en desuso** como técnica de red, sobrevive en la lógica del correo electrónico |
| Difusión y multidifusión | **Unidifusión** (uno a uno) · **multidifusión** (uno a un grupo suscrito) · **difusión** (uno a todos) · **anydifusión** (al más cercano del grupo, propia de **IPv6**). **IPv6 no tiene broadcast**: lo sustituye por multidifusión a `ff02::1` |
| Direcciones de difusión | MAC de difusión: **FF:FF:FF:FF:FF:FF**. IPv4 limitada: **255.255.255.255** (no se encamina). Multidifusión IPv4: **224.0.0.0/4** (clase D), con MAC **01:00:5E:…**. Protocolo de suscripción: **IGMP** en IPv4 y **MLD** en IPv6 |
| Tormenta de difusión | Exceso de tráfico de difusión que satura el dominio; se agrava con **bucles de nivel 2** porque la trama Ethernet **no tiene TTL**. Remedios: **STP/RSTP**, **VLAN** para acotar el dominio y control de tormentas en el conmutador |
| Wi-Fi: generaciones | **Wi-Fi 4** = 802.11n · **Wi-Fi 5** = 802.11ac · **Wi-Fi 6** = 802.11ax · **Wi-Fi 6E** = 802.11ax en **6 GHz** · **Wi-Fi 7** = **802.11be**, publicado el **22 de julio de 2025** (canales de **320 MHz**, **4096-QAM** y **operación multienlace, MLO**) · **Wi-Fi 8** = 802.11bn, previsto para **2028** |
| Wi-Fi: modos y elementos | **BSS** (una celda con su punto de acceso) · **ESS** (varias celdas con el mismo **SSID**) · **modo *ad hoc*/IBSS** (sin punto de acceso). Acceso al medio: **CSMA/CA** (no CSMA/CD: en radio no se puede detectar la colisión mientras se transmite) |
| Otras redes inalámbricas | **Bluetooth** (WPAN, 2,4 GHz, piconet de 1 maestro y hasta 7 esclavos activos) · **NFC** (13,56 MHz, **≈ 10 cm**) · **Zigbee** (802.15.4, malla, domótica) · **LoRaWAN y NB-IoT** (LPWAN: poco caudal, mucho alcance, años de batería) · **WiMAX** (802.16, WMAN, hoy residual) |
| Satélite | **GEO** (35.786 km, fijo respecto a la Tierra, **≈ 250 ms** de ida y vuelta) · **MEO** (2.000-35.786 km; GPS y Galileo) · **LEO** (300-2.000 km, latencia baja, exige **constelaciones**). Bandas **C, Ku, Ka** |
| Generaciones móviles | **1G** analógica (TACS) · **2G GSM** digital, conmutación de circuitos, **SMS**, **SIM**; **GPRS (2.5G)** y **EDGE** añaden paquetes · **3G UMTS** (WCDMA), **HSPA** · **4G LTE**, **todo IP y solo paquetes**, voz por **VoLTE** · **5G NR** (eMBB, URLLC, mMTC) |
| Célula y reutilización | La red **celular** divide el territorio en celdas con **reutilización de frecuencias**: celdas no adyacentes repiten canal. El **traspaso (*handover*)** mantiene la llamada al cambiar de celda; el **itinerancia (*roaming*)** permite usar la red de otro operador |
| 5G: las tres familias de uso | **eMBB** (banda ancha móvil mejorada) · **URLLC** (comunicaciones ultrafiables de baja latencia) · **mMTC** (comunicaciones masivas entre máquinas). Habilitadores: **MIMO masivo**, **haces (*beamforming*)**, ***network slicing*** y **computación en el borde (MEC)** |
| Espectro 5G en España | Tres bandas prioritarias: **700 MHz** (cobertura; liberada por el **segundo dividendo digital**, RD **391/2019**, migración de la TDT completada el **31-10-2020**) · **3,5 GHz** (banda de capacidad y cobertura equilibradas) · **26 GHz** (ondas milimétricas, subastada en **2022**). La banda **470-694 MHz** queda para TDT **al menos hasta 2030** |
| Seguridad inalámbrica | **WEP** (RC4, roto: **no usar**) · **WPA** (TKIP, transitorio) · **WPA2** (**AES-CCMP**, 802.11i) · **WPA3** (**SAE**, sustituye al PSK; **192 bits** en modo Enterprise; **OWE** para redes abiertas). Empresarial: **802.1X + EAP + RADIUS**, autenticación por usuario y no por clave compartida |
| Wi-Fi en el ENS | **`mp.com.4.2`**: si se emplean comunicaciones inalámbricas, será **en un segmento separado**. **`mp.com.2`** (confidencialidad, dimensión **C**) y **`mp.com.3`** (integridad y autenticidad, dimensión **IA**) exigen **VPN cifrada** fuera del dominio propio y, desde nivel MEDIO, **algoritmos autorizados por el CCN** |
| Marco legal español | **Ley 11/2022, de 28 de junio, General de Telecomunicaciones**: 8 títulos, 114 artículos y 3 anexos. Las telecomunicaciones son **servicios de interés general en libre competencia** (art. 2.1); **solo** son servicio público los del **art. 4** (seguridad nacional, defensa, seguridad pública, seguridad vial y protección civil) |
| Servicio universal | Art. **37**: acceso adecuado a **internet de banda ancha en ubicación fija** con velocidad mínima de **10 Mbit/s** en sentido descendente, escalable por real decreto a **30 Mbit/s**, más **comunicaciones vocales**. El **anexo III** lista los **once** servicios que debe soportar |
| Administraciones públicas y redes | Art. **13**: cuando una Administración instala y explota redes públicas debe respetar el **principio de inversor privado**, con **separación de cuentas**, neutralidad, transparencia, no distorsión de la competencia y no discriminación. Excepción con **fallo de mercado** declarado: la **TDT en zonas sin cobertura** |
| Reguladores | **CNMC** (regulación *ex ante* de mercados, resolución de conflictos, supervisión de precios del servicio universal) · **Ministerio** competente en telecomunicaciones (espectro, inspección, incidentes del art. 63) · **UIT** en el plano internacional · **CEPT/ECC** y **RSPG** en el europeo |

## Contenido

### Convenciones del documento

Este tema incluye cuatro tipos de **cajas callout** para facilitar el estudio:

> **Dato clave.** Información de alta densidad memorística: cifras, frecuencias, distancias, siglas, normas IEEE y artículos de la Ley General de Telecomunicaciones.

> **Ejercicio resuelto.** Problema + solución paso a paso: calcular una capacidad de canal, dimensionar un enlace, elegir un medio de transmisión, contar dominios de colisión y de difusión.

> **Ejemplo de aplicación en el ayto.** Aplicación real de la teoría al entorno municipal (red del IAM, sedes de distrito, oficinas de atención a la ciudadanía, red de la Policía Municipal, wifi de uso público).

> **Relación con otros temas.** Enlace conceptual a otros temas del temario oficial.

**Este es el tema-cimiento del bloque de comunicaciones**, y conviene entender su papel antes de empezar. El temario oficial dedica ocho temas a las redes —del 30 al 38, más el 39 en su vertiente normativa— y **este es el primero de todos ellos por orden lógico**, aunque no lo sea por número. Aquí se establece el vocabulario y la física: qué es una comunicación, por qué medio viaja, en qué modo, con qué equipos, en qué tipo de red y con qué técnica de conmutación. Los temas siguientes construyen sobre ese cimiento: el **Tema 34** añade el modelo de capas y los protocolos TCP/IP, el **Tema 35** el servicio de internet, el **Tema 36** la seguridad de las comunicaciones, el **Tema 37** la red de área local en detalle y el **Tema 38** una tecnología radio concreta, TETRA.

De ahí se derivan las **fronteras** que este tema respeta deliberadamente, y que conviene tener presentes para no estudiar dos veces lo mismo ni dejar huecos:

| Materia | Dónde se desarrolla | Qué hace este tema |
|----|----|----|
| Modelo **OSI** y modelo **TCP/IP**, direccionamiento IP, protocolos | **Tema 34** | Usa las capas **solo** como criterio para clasificar los equipos de interconexión (§4.2) |
| **Internet**, servicios, HTTP, HTTPS, TLS | **Tema 35** | No entra: cita internet como red de redes de conmutación de paquetes |
| **Seguridad perimetral**, cortafuegos, IDS/IPS, VPN de acceso remoto | **Tema 36** | Solo la seguridad **específicamente inalámbrica** (§9.1) |
| **Redes locales**: tipología, técnicas de transmisión, **métodos de acceso al medio**, dispositivos | **Tema 37** | Los equipos de interconexión sí (los pide el enunciado), pero **no** CSMA/CD, token ni las tramas Ethernet |
| **TETRA** | **Tema 38** | Lo cita como ejemplo canónico de semidúplex y de radio troncal profesional |
| **Administración** de la red local, VLAN, monitorización | **Tema 30** | Da el fundamento (segmentación, difusión), no la operación |
| **Principios del ENS y del ENI** | **Tema 39** | Cita solo las medidas `mp.com` que afectan a las comunicaciones |

La segunda advertencia es de método. En un tema de comunicaciones hay **dos clases de pregunta** y hay que llevar las dos. La primera es conceptual: *¿qué distingue la conmutación de circuitos de la de paquetes?*, *¿por qué un conmutador no divide el dominio de difusión?*, *¿por qué en radio no se usa CSMA/CD?*. La segunda es de dato puro: *¿cuántos metros mide como máximo un enlace de cobre en Ethernet?*, *¿qué frecuencia usa NFC?*, *¿qué velocidad mínima fija el servicio universal?*. La primera clase se aprueba entendiendo; la segunda, memorizando. Las cajas naranjas de este documento marcan exactamente lo memorizable.

Las fuentes se citan con etiquetas breves tipo `[LGT]`, `[IEEE802.11]` o `[UIT-T]`; el registro completo está en la pestaña Fuentes. **Todo el articulado de la Ley 11/2022 citado en este tema se ha verificado contra el texto consolidado del BOE**, no de memoria, y lo mismo vale para las medidas `mp.com` del ENS.

**Caso de referencia usado en todo el tema** (contexto Ayuntamiento de Madrid, supuesto simplificado): la **red de comunicaciones que conecta una Oficina de Atención a la Ciudadanía de un distrito con el centro de proceso de datos del IAM**. Esa oficina tiene puestos de trabajo cableados, una impresora multifunción, teléfonos IP, un sistema de gestión de turnos, cámaras de videovigilancia, una wifi para el personal, otra wifi de cortesía para el público y un enlace de respaldo. Cada sección del tema pregunta algo distinto sobre esa misma oficina: por qué medio llegan los datos (§2), en qué modo circulan (§3), con qué equipos (§4), en qué tipo de red y topología (§5), con qué técnica de conmutación (§6), qué hay de inalámbrico (§7 y §8) y qué obligaciones legales y de seguridad pesan sobre todo ello (§9).

------------------------------------------------------------------------

### 1. Conceptos generales de telecomunicaciones y modelo de comunicación

#### 1.1. Elementos del sistema de transmisión y perturbaciones en el canal

**Qué es una telecomunicación.** El punto de partida no es una definición de manual, sino una **definición legal** que conviene poder reproducir casi literalmente, porque es la que maneja la normativa española:

> **Dato clave.** **Telecomunicación** es *«toda transmisión, emisión o recepción de signos, señales, escritos, imágenes, sonidos o informaciones de cualquier naturaleza por hilo, radioelectricidad, medios ópticos u otros sistemas electromagnéticos»* \[LGT, anexo II, apartado 79\]. Tres rasgos clave de la definición: (1) es **indiferente el contenido** («informaciones de cualquier naturaleza»); (2) es **indiferente el medio** (hilo, radio, óptico u otros sistemas electromagnéticos); y (3) cubre las **tres operaciones** —transmitir, emitir y recibir—, no solo la primera. El prefijo *tele-* añade la idea de **distancia**.

Conviene deslindar tres palabras que el temario usa con precisión distinta:

- **Comunicación**: proceso de transferencia de información entre dos o más entidades.
- **Telecomunicación**: comunicación **a distancia** por medios electromagnéticos, en los términos de la definición legal.
- **Transmisión de datos**: la telecomunicación cuya información es **digital** y cuyos extremos son, típicamente, equipos informáticos. Es el objeto central de este tema.

**El modelo de Shannon.** El esquema canónico de todo sistema de comunicación tiene **cinco elementos** y procede del artículo fundacional de Claude Shannon de 1948 \[SHANNON\]. Ver **diagrama D1**.

| Elemento | Función | Ejemplo en la oficina de distrito |
|----|----|----|
| **Fuente de información** | Genera el mensaje que se quiere transmitir | El puesto de trabajo que envía un formulario de la sede |
| **Transmisor** (emisor o codificador) | Convierte el mensaje en una **señal** apta para el medio: codifica, modula, amplifica | La tarjeta de red que convierte los bits en pulsos eléctricos |
| **Canal** (medio de transmisión) | Soporte físico por el que viaja la señal. **Es donde se introduce el ruido** | El cable de par trenzado y la fibra que sale de la oficina |
| **Receptor** (decodificador) | Operación inversa a la del transmisor: demodula y reconstruye el mensaje | La tarjeta de red del servidor en el CPD del IAM |
| **Destino** | Entidad a la que va dirigido el mensaje | La aplicación de tramitación de expedientes |

> **Dato clave.** En el modelo de Shannon la **fuente de ruido actúa sobre el CANAL**, no sobre el mensaje ni sobre el transmisor. Es un detalle de dibujo importante: el ruido se suma a la señal **durante su tránsito**. De ahí que todas las técnicas de protección —codificación de canal, detección y corrección de errores, cifrado, regeneración— se apliquen **antes** de entrar al canal y **después** de salir de él, nunca dentro.

A esos cinco elementos, muchos manuales añaden el **protocolo** —el conjunto de reglas que hacen inteligible el intercambio— y el **mensaje** propiamente dicho, con lo que la enumeración pasa a ser de siete \[FOROUZAN\]. Las dos formulaciones son correctas: la de cinco es la del modelo físico de Shannon; la de siete es la del modelo de comunicación de datos. Si una pregunta enumera «emisor, receptor, mensaje, medio y protocolo», está usando la segunda.

**Señal analógica y señal digital.** Una **señal analógica** varía de forma **continua** en el tiempo y puede tomar infinitos valores dentro de un rango (la voz, una onda senoidal). Una **señal digital** toma un número **finito y discreto** de valores, típicamente dos (0 y 1), y varía a saltos. La distinción es del **soporte**, no del contenido: la voz humana es analógica, pero se puede transmitir digitalizada, y un bit es digital, pero puede viajar modulado sobre una portadora analógica.

Esa doble posibilidad genera cuatro combinaciones que conviene tener claras, porque cada una tiene su equipo característico (ver §4.1):

| Fuente | Transmisión | Equipo que hace la conversión | Ejemplo |
|----|----|----|----|
| Analógica | Analógica | Modulador de amplitud, frecuencia o fase | Radio FM |
| Analógica | **Digital** | **Códec** (codificador-decodificador) | Telefonía IP, MP3, videoconferencia |
| **Digital** | Analógica | **Módem** (modulador-demodulador) | ADSL, cable módem, radioenlace |
| Digital | Digital | Codificador de línea (NRZ, Manchester, 4B/5B…) | Ethernet sobre par trenzado |

> **Dato clave.** **Módem y códec no son sinónimos y hacen operaciones inversas.** El **módem** parte de datos **digitales** y los adapta a un medio **analógico** (modula) y viceversa (demodula). El **códec** parte de una señal **analógica** de la fuente y la convierte en **digital** (codifica) y viceversa (decodifica). Regla mnemotécnica: el módem mira **al medio**; el códec mira **a la fuente**.

**La digitalización de una señal analógica** sigue tres pasos, en este orden y sin excepción \[STALLINGS\]:

1.  **Muestreo (*sampling*)**: se toman valores de la señal a intervalos regulares. La frecuencia de muestreo la fija el **teorema del muestreo** (§1.2).
2.  **Cuantificación**: cada muestra se aproxima al valor más cercano de una escala finita de niveles. Aquí aparece un error inevitable, el **ruido de cuantificación**, que disminuye al aumentar el número de niveles.
3.  **Codificación**: cada nivel se representa como una combinación de bits.

El resultado clásico de esa cadena es la **modulación por impulsos codificados (MIC o PCM)** de la telefonía, cuyo cálculo es el ejercicio numérico más repetido del tema y se resuelve en §1.2.

**Perturbaciones del canal.** Ninguna señal llega igual que salió. Las alteraciones se agrupan en cinco familias, y conviene distinguirlas. Ver **diagrama D2**.

**1. Atenuación.** Pérdida de **potencia** de la señal conforme avanza por el medio. Crece con la **distancia** y, en general, con la **frecuencia** —lo que la hace además **selectiva**, porque no afecta por igual a todos los componentes de la señal—. Se mide en **decibelios**, y en los medios guiados se expresa como atenuación **por unidad de longitud** (dB/km en fibra, dB/100 m en cobre). Se combate con **amplificadores** (en señal analógica, que amplifican también el ruido) o con **repetidores regeneradores** (en señal digital, que reconstruyen la señal limpia). Es la razón última de que exista un **límite de longitud** en cada medio.

**2. Distorsión.** **Deformación** de la señal: llega, pero con otra forma. La variedad más importante en transmisión digital es la **distorsión de retardo**, causada porque las distintas componentes de frecuencia viajan a velocidades ligeramente distintas por el medio; los símbolos se «desparraman» y acaban solapándose con los vecinos, fenómeno llamado **interferencia entre símbolos (ISI)**. Se corrige con **ecualizadores**. En fibra óptica el mismo fenómeno recibe el nombre de **dispersión** (modal, cromática y por modo de polarización).

**3. Ruido.** **Energía eléctrica no deseada** que se **añade** a la señal. Sus cuatro tipos clásicos \[STALLINGS\] son:

- **Ruido térmico** (o de fondo, o blanco, o de Johnson): agitación térmica de los electrones. Está presente en **todos** los medios y a todas las frecuencias, y **no se puede eliminar**: es el que fija el límite físico de Shannon.
- **Ruido de intermodulación**: aparece cuando dos o más señales de frecuencias distintas comparten el medio y la no linealidad del sistema genera componentes espurias en frecuencias suma y diferencia.
- **Diafonía (*crosstalk*)**: acoplamiento no deseado entre pares o circuitos **próximos**. Es el enemigo característico del **par trenzado**, y la razón física de que los pares se trencen. Se mide con parámetros como **NEXT** (diafonía en el extremo próximo) y **FEXT** (en el extremo lejano).
- **Ruido impulsivo**: picos irregulares de gran amplitud y corta duración (una tormenta, el arranque de un motor, un relé). Es **el más dañino en transmisión digital**, porque en unos milisegundos destruye un bloque entero de bits, mientras que en una conversación analógica solo produce un chasquido.

> **Dato clave.** Doble asimetría clave: el **ruido térmico** es inevitable pero previsible; el **ruido impulsivo** es esporádico pero devastador **en digital**. Y al revés: la señal analógica tolera mal el ruido acumulado (los amplificadores lo amplifican con la señal), mientras que la digital lo tolera bien hasta un umbral **y luego falla de golpe**. Esta es la ventaja decisiva de lo digital: la **regeneración** de la señal en cada repetidor deja el ruido a cero.

**4. Interferencia.** Energía procedente de **otra fuente de comunicación** —otro emisor, otro sistema— que se superpone a la señal útil. Es especialmente crítica en los medios **no guiados**, donde el medio es compartido por todos, y es la razón de la regulación administrativa del espectro (§9.2). La **interferencia electromagnética (EMI)** de origen industrial afecta a los medios de cobre, pero **no a la fibra óptica**, que por ser dieléctrica es inmune.

**5. Eco y otras alteraciones.** El **eco** es el retorno de parte de la señal por reflexión, típico de las desadaptaciones de impedancia; se combate con **canceladores de eco**. Hay que añadir la **fluctuación de fase (*jitter*)**, las **variaciones de amplitud** y los **desvanecimientos (*fading*)** propios de la radio, causados por la propagación multitrayecto.

> **Ejemplo de aplicación en el ayto.** Las tres perturbaciones aparecen juntas en un caso real de la oficina de distrito. Un latiguillo de par trenzado que discurre junto a la canalización eléctrica del cuarto de comunicaciones sufre **interferencia** electromagnética; si además se ha usado cable sin apantallar y se han destrenzado cinco centímetros al conectorizar, aparece **diafonía**; y si alguien ha hecho una tirada de 130 metros hasta un puesto alejado, la **atenuación** deja el enlace por debajo del margen exigido. El síntoma que ve el usuario es siempre el mismo —«la red va lenta»—, pero las tres causas son distintas y se diagnostican con un **certificador de cableado**, no con un ping.

#### 1.2. Transmisión analógica y digital: ancho de banda y velocidad de transmisión

**Ancho de banda.** Es el **rango de frecuencias** que un canal deja pasar sin atenuación apreciable, y se mide en **hercios (Hz)**. Se calcula como la diferencia entre la frecuencia máxima y la mínima del canal. El canal telefónico clásico, por ejemplo, tiene un ancho de banda de unos **3.100 Hz** (de 300 a 3.400 Hz). En el lenguaje corriente «ancho de banda» se usa como sinónimo de velocidad —«tengo 600 megas de ancho de banda»—, y conviene no confundirlos:

> **Dato clave.** **Ancho de banda ≠ velocidad de transmisión.** El **ancho de banda** es un rango de **frecuencias** y se mide en **hercios (Hz)**. La **velocidad de transmisión** o **régimen binario** es un flujo de **bits** y se mide en **bits por segundo (bps)**. Están relacionados —a más ancho de banda, más capacidad posible— pero no son la misma magnitud, y la relación entre ambos depende de la **modulación** y del **ruido**.

Hay una **tercera** magnitud que completa el trío:

- **Velocidad de transmisión** o **tasa binaria**: bits por segundo (**bps**, kbps, Mbps, Gbps).
- **Velocidad de modulación** o **tasa de símbolos**: símbolos (cambios de estado de la señal) por segundo, medida en **baudios (Bd)**.

La relación es `Vt = Vm · log₂(M)`, donde **M** es el número de estados o símbolos distintos que puede tomar la señal.

> **Dato clave.** **Baudio no es bit por segundo.** Coinciden **solo** cuando cada símbolo transporta **un** bit (M = 2). Si la modulación es de **4 estados** (por ejemplo, QPSK), cada símbolo lleva **2 bits** y la velocidad en bps es **el doble** que en baudios. Con **16-QAM**, cuatro veces; con **4096-QAM** —la de Wi-Fi 7—, **doce veces**, porque `log₂(4096) = 12`.

**Los dos teoremas de capacidad.** Fijan cuánta información cabe por un canal, y son los dos únicos cálculos que hay que saber hacer de memoria. Ver **diagrama D3**.

**Nyquist — canal ideal, sin ruido** \[NYQUIST\]:

    C = 2 · B · log₂(M)

donde `C` es la capacidad en bps, `B` el ancho de banda en Hz y `M` el número de niveles o símbolos. Consecuencia contraintuitiva: en un canal sin ruido, aumentando `M` la capacidad crecería **sin límite**. En la práctica no es así porque, al multiplicar los niveles, se acercan tanto entre sí que el ruido los confunde. De ahí el segundo teorema.

**Shannon — canal real, con ruido** \[SHANNON\]:

    C = B · log₂(1 + S/N)

donde `S/N` es la **relación señal-ruido en veces** (no en decibelios). Este resultado es el **límite absoluto**: ninguna modulación, ninguna codificación y ninguna técnica futura permite superar la capacidad de Shannon en un canal dado. Lo que hacen las tecnologías modernas es **acercarse** a él (con códigos correctores como LDPC o turbo códigos).

> **Dato clave.** Conversión entre relación señal-ruido en decibelios y en veces: `S/N (dB) = 10 · log₁₀(S/N)`. Y al revés, `S/N = 10^(dB/10)`. **30 dB = 1.000 veces**, **20 dB = 100 veces**, **10 dB = 10 veces**, **3 dB ≈ 2 veces**. El error más frecuente es meter los decibelios directamente en la fórmula de Shannon.

> **Ejercicio resuelto.** **Capacidad de un canal telefónico.** Se dispone de un canal con **B = 3.100 Hz** y una relación señal-ruido de **30 dB**. **(a)** ¿Cuál es su capacidad máxima teórica? **(b)** ¿Cuántos niveles de señalización harían falta, según Nyquist, para alcanzarla? **Solución.** **(a)** Primero se pasan los decibelios a veces: `S/N = 10^(30/10) = 10³ = 1.000`. Shannon: `C = 3.100 · log₂(1 + 1.000) = 3.100 · log₂(1.001) ≈ 3.100 · 9,97 ≈ `**`30.900 bps`**. Es decir, unos **30 kbps** —exactamente el orden de magnitud de los módems telefónicos de los años noventa, que no era casualidad: estaban rozando el límite físico del par de cobre en banda vocal—. **(b)** Nyquist: `30.900 = 2 · 3.100 · log₂(M)` → `log₂(M) = 30.900 / 6.200 ≈ 4,98` → `M ≈ 2^4,98 ≈ `**`32 niveles`**. **Lectura del resultado**: los dos teoremas se usan juntos. **Shannon dice cuánto** cabe como máximo, **Nyquist dice cómo** habría que modular para conseguirlo. Si el cálculo de Nyquist exigiera un número de niveles irrealizable, la conclusión sería que hay que **mejorar la relación señal-ruido**, no la modulación.

**El teorema del muestreo.** Para digitalizar una señal analógica sin perder información hay que muestrearla a una frecuencia **al menos el doble** de su componente de frecuencia más alta:

    fm ≥ 2 · fmax

Si no se cumple, aparece el **solapamiento espectral (*aliasing*)** y la señal reconstruida es irrecuperablemente distinta de la original.

> **Ejercicio resuelto.** **El canal telefónico digital de 64 kbps.** La telefonía transmite voz limitada a la banda **300-3.400 Hz**. Deduzca el régimen binario del canal digital básico. **Solución.** 1. **Frecuencia de muestreo**: `fmax = 3.400 Hz` → `fm ≥ 6.800 Hz`. Se normalizó en **8.000 muestras por segundo**, dejando un margen de guarda \[UIT-T, G.711\]. 2. **Cuantificación y codificación**: cada muestra se codifica con **8 bits** (256 niveles, con ley A en Europa y ley µ en América). 3. **Régimen binario**: `8.000 muestras/s × 8 bits/muestra = `**`64.000 bps = 64 kbps`**. Ese canal de 64 kbps es el **E0**, el ladrillo elemental de toda la jerarquía digital europea. Agrupando **32 intervalos de tiempo** de 64 kbps se obtiene el **E1 = 2,048 Mbit/s** \[UIT-T, G.704\], de los cuales 30 transportan voz y **dos son de señalización y sincronismo**. Es el dato numérico clave de todo el bloque de telefonía, y el origen del clásico «un primario de treinta canales».

**Multiplexación.** Compartir un mismo medio físico entre varias comunicaciones simultáneas. Cuatro técnicas, con sus siglas:

| Técnica | Sigla | Qué reparte | Ejemplo |
|----|----|----|----|
| **Por división de frecuencia** | **FDM** | El espectro se divide en subbandas, cada canal en la suya, con **bandas de guarda** | Radio y TV analógicas, ADSL, portadoras de cable |
| **Por división de longitud de onda** | **WDM / DWDM** | Es FDM aplicada a la **fibra óptica**: cada canal, un color de luz | Redes troncales de operador; decenas de canales de 100 Gbit/s por una sola fibra |
| **Por división de tiempo** | **TDM** | Cada canal ocupa **intervalos de tiempo** periódicos del medio | E1/T1, SDH, GSM |
| **Por división de código** | **CDMA** | Todos transmiten a la vez en toda la banda, separados por **códigos ortogonales** | 3G (UMTS/WCDMA), GPS |

Dentro de TDM hay que distinguir dos variantes, y la distinción es exactamente la misma que separa la conmutación de circuitos de la de paquetes (§6.1):

- **TDM síncrona**: a cada canal se le asigna **siempre** su intervalo, lo use o no. Sencilla y de retardo constante, pero **desaprovecha** el medio cuando un canal calla.
- **TDM estadística** o **asíncrona**: los intervalos se asignan **bajo demanda**, solo a quien tiene algo que enviar. Aprovecha mucho mejor el medio, pero obliga a identificar a qué canal pertenece cada fragmento y introduce **fluctuación**.

> **Relación con otros temas.** La **codificación de la información** (representación binaria, sistemas de numeración, códigos) corresponde al **Tema 11**, y los **formatos de información y ficheros** al **Tema 13**. Este tema da por sabido qué es un bit y se ocupa de **cómo viaja**.

------------------------------------------------------------------------

### 2. Medios de transmisión

El **medio de transmisión** es el soporte físico por el que viaja la señal: el «canal» del modelo de Shannon. La clasificación de primer nivel es la única realmente estructural del tema y hay que tenerla automatizada:

- **Medios guiados** (o **confinados**, o **de cable**): la señal se propaga **confinada** por un soporte físico que la conduce y la dirige. El camino lo marca el propio medio.
- **Medios no guiados** (o **inalámbricos**, o **radiados**): la señal se propaga **libremente** por el espacio en forma de onda electromagnética. No hay soporte físico, sino **antenas** que emiten y recogen.

> **Dato clave.** El criterio de la clasificación es la **existencia de guía artificial**, no la naturaleza de la señal ni la distancia. Un enlace por microondas punto a punto de 40 km es **no guiado** aunque sea direccional y fijo; un cable submarino de 6.000 km es **guiado**. La propia Ley 11/2022 usa ese criterio en la definición de **espectro radioeléctrico**: ondas *«que se propagan por el espacio sin guía artificial»* \[LGT, anexo II.21\].

#### 2.1. Medios de transmisión guiados

##### 2.1.1. Par trenzado, cable coaxial y fibra óptica

Los tres medios guiados de uso general, en orden histórico y de prestaciones crecientes. Ver **diagrama D4**.

**A. Par trenzado (*twisted pair*).**

Dos conductores de cobre aislados y **trenzados** entre sí formando una hélice. El trenzado no es decorativo: al invertir la posición relativa de los dos hilos de forma periódica, las interferencias que capta cada uno tienden a **cancelarse** en el par, y se reduce drásticamente la **diafonía** con los pares vecinos. **A más vueltas por metro, mejor rechazo** y mayor categoría del cable.

El cable de red típico agrupa **cuatro pares** (ocho hilos) y termina en un conector **RJ-45** de 8 posiciones y 8 contactos, con dos esquemas de conexionado normalizados, **T568A** y **T568B** \[ISO11801\].

Según su apantallamiento se clasifican con una nomenclatura de dos partes (*pantalla global / pantalla por par*):

| Tipo | Nombre | Descripción |
|----|----|----|
| **UTP** | *Unshielded Twisted Pair* | **Sin apantallar**. El más barato, flexible y extendido en interiores |
| **FTP** | *Foiled Twisted Pair* | Pantalla **global** de lámina de aluminio |
| **STP** | *Shielded Twisted Pair* | Pantalla **por par**, típicamente de malla |
| **S/FTP** | — | Malla global **más** lámina por cada par: el máximo apantallamiento |

Y según sus prestaciones se agrupan en **categorías** \[ISO11801\]:

| Categoría | Ancho de banda | Uso típico | Alcance a esa velocidad |
|----|----|----|----|
| **Cat 5e** | 100 MHz | 1000BASE-T (1 Gbit/s) | 100 m |
| **Cat 6** | 250 MHz | 1 Gbit/s; 10 Gbit/s solo hasta ~55 m | 100 m / 55 m |
| **Cat 6A** | 500 MHz | **10GBASE-T (10 Gbit/s)** | **100 m** |
| **Cat 7 / 7A** | 600 / 1.000 MHz | 10 Gbit/s con conectores GG45 o TERA | 100 m |
| **Cat 8** | **2.000 MHz** | 25 y 40 Gbit/s en centro de datos | **30 m** |

> **Dato clave.** El límite de **100 metros** del enlace permanente de cobre en Ethernet es el dato numérico clave del cableado, y su desglose normalizado es: **90 m** de cable horizontal fijo (del armario a la roseta) **+ 10 m** repartidos entre latiguillos de ambos extremos \[ISO11801\] \[IEEE802.3\]. Superarlo no produce un fallo limpio, sino **errores intermitentes**, que es lo que lo hace tan difícil de diagnosticar. La **Cat 8**, en cambio, solo garantiza **30 m**: al subir la frecuencia, baja el alcance.

Una capacidad asociada al par trenzado cada vez más relevante es la **alimentación por Ethernet (PoE)**, que lleva por el mismo cable datos y corriente continua \[IEEE802.3\]:

| Norma | Nombre comercial | Potencia en el equipo fuente | Pares usados |
|----|----|----|----|
| **802.3af** | PoE | **15,4 W** (12,95 W en el dispositivo) | 2 pares |
| **802.3at** | PoE+ | **30 W** (25,5 W en el dispositivo) | 2 pares |
| **802.3bt** | PoE++ / 4PPoE | **60 W** (tipo 3) y **90-100 W** (tipo 4) | **4 pares** |

**B. Cable coaxial.**

Un conductor central de cobre, un dieléctrico aislante, una **malla conductora** que lo rodea concéntricamente y una cubierta exterior. La malla cumple dos funciones: es el segundo conductor del circuito **y** es una **pantalla** contra interferencias, lo que le da mucha mejor inmunidad y mayor ancho de banda que el par trenzado sin apantallar.

Dos impedancias características normalizadas, y conviene no confundirlas:

- **50 ohmios**: transmisión **digital** en banda base. Fue el cable de la Ethernet original (**10BASE5**, «cable amarillo» o *thick*, hasta 500 m por segmento; y **10BASE2**, «cheapernet» o *thin*, hasta 185 m con conectores BNC en T).
- **75 ohmios**: transmisión **analógica** en banda ancha. Es el de la **televisión** por cable y por antena y el del acceso a internet por cable (**DOCSIS**), y sigue muy vivo por eso.

En redes locales el coaxial está **completamente desplazado** por el par trenzado y la fibra desde los años noventa, pero conviene saber por qué desapareció: su topología natural era el **bus**, con **terminadores** en los extremos, de modo que un fallo en cualquier punto del cable **dejaba sin servicio a todo el segmento**, y localizarlo era penoso.

**C. Fibra óptica.**

Un filamento de vidrio de sílice (o de plástico, en aplicaciones de bajo coste) formado por un **núcleo** de índice de refracción alto, un **revestimiento** de índice más bajo y una cubierta protectora. La luz introducida en el núcleo dentro de un cierto ángulo —el **cono de aceptación**— avanza por **reflexión total interna** en la frontera núcleo-revestimiento, sin escapar. El emisor es un **LED** o un **diodo láser**; el receptor, un **fotodiodo**.

Sus ventajas son categóricas y hay que poder enumerarlas:

- **Ancho de banda enorme**, del orden de terahercios, y con multiplexación por longitud de onda (**DWDM**) decenas de canales por hebra.
- **Atenuación muy baja**: del orden de **0,2 dB/km** en tercera ventana, frente a decenas de dB/km del cobre. De ahí los enlaces de decenas o centenares de kilómetros sin regeneración.
- **Inmunidad total a las interferencias electromagnéticas** y **ausencia de diafonía**: no es un conductor eléctrico, sino un dieléctrico.
- **No radia**, lo que la hace mucho más **difícil de pinchar** sin ser detectado.
- **Ligereza y tamaño** muy inferiores a los del cobre de capacidad equivalente.
- **Aislamiento galvánico**: no transmite diferencias de potencial ni rayos entre edificios.

Y sus inconvenientes: **coste** de los equipos terminales, **fragilidad** al doblado con radios pequeños, **dificultad de empalme** (fusionadora, personal cualificado, precisión micrométrica) y **no transporta energía**, de modo que un equipo remoto conectado por fibra necesita alimentación propia (no hay «PoE óptico»).

Los dos grandes tipos, con su tabla de designaciones:

|  | **Multimodo (MM)** | **Monomodo (SM)** |
|----|----|----|
| **Diámetro del núcleo** | **50 o 62,5 µm** | **≈ 8-10 µm** |
| **Fuente de luz** | LED o **VCSEL** | **Diodo láser** |
| **Modos de propagación** | Muchos caminos simultáneos | **Uno solo** |
| **Limitación principal** | **Dispersión modal**: los rayos recorren caminos de distinta longitud y llegan desfasados | Dispersión cromática, mucho menor |
| **Alcance típico** | Decenas o centenares de metros | **Decenas o centenares de kilómetros** |
| **Designaciones** | **OM1, OM2, OM3, OM4, OM5** | **OS1, OS2** |
| **Coste** | Menor en electrónica, mayor en fibra | Mayor en electrónica, menor en fibra |
| **Uso típico** | Vertical de edificio, centro de datos | Enlaces entre sedes, acceso FTTH, troncales |

> **Dato clave.** La regla que resume la diferencia: **a mayor diámetro de núcleo, más modos de propagación, más dispersión modal y menos alcance**. Por eso la fibra de largo alcance es la de núcleo **más fino**, que es justo lo contrario de lo que sugiere la intuición. Las **tres ventanas** de trabajo son **850 nm** (primera, multimodo), **1.310 nm** (segunda) y **1.550 nm** (tercera, la de mínima atenuación y la usada en larga distancia y DWDM) \[OM-OS\].

Sobre fibra se construyen hoy las redes de acceso **FTTH** (*Fiber To The Home*) mediante arquitecturas **PON** (*Passive Optical Network*), que reparten una misma fibra entre varios abonados con **divisores ópticos pasivos**, sin electrónica intermedia: **GPON** (2,5 Gbit/s descendente / 1,25 ascendente, \[UIT-T, G.984\]) y **XGS-PON** (10 Gbit/s simétricos, \[UIT-T, G.9807.1\]).

> **Ejemplo de aplicación en el ayto.** El cableado de la Oficina de Atención a la Ciudadanía combina los tres criterios anteriores de forma típica. **Horizontal** (del armario de planta a cada roseta de puesto): **par trenzado Cat 6A**, porque hay que dar 1 Gbit/s hoy con margen para 10 Gbit/s mañana, alimentar por **PoE+** los teléfonos IP, los puntos de acceso wifi y las cámaras, y ninguna tirada supera los 90 m. **Vertical** (entre plantas): **fibra multimodo OM4**, por distancia y por aislamiento galvánico entre cuadros eléctricos distintos. **Acometida** al centro de proceso de datos del IAM: **fibra monomodo OS2**, porque son kilómetros. Y **coaxial de 75 Ω** solo en el residuo de la instalación de televisión de la sala de espera.

#### 2.2. Medios de transmisión no guiados

##### 2.2.1. Espectro radioeléctrico, radiofrecuencia, microondas e infrarrojos

**El espectro radioeléctrico.** La definición hay que saberla en su versión legal, porque delimita el objeto de toda la regulación de §9.2:

> **Dato clave.** **Espectro radioeléctrico**: *«ondas electromagnéticas, cuya frecuencia se fija convencionalmente por debajo de 3.000 GHz, que se propagan por el espacio sin guía artificial»* \[LGT, anexo II.21\]. Dos datos clave de la definición: el límite superior **convencional** de **3.000 GHz (3 THz)** y la exigencia de **ausencia de guía artificial**. Y su consecuencia jurídica, en el art. 85.1: el espectro es un **bien de dominio público**, cuya **titularidad y administración corresponden al Estado**.

Una onda electromagnética se caracteriza por su **frecuencia** (f, en hercios) y su **longitud de onda** (λ, en metros), ligadas por la velocidad de propagación:

    λ = c / f       (c ≈ 3 · 10⁸ m/s en el vacío)

De donde se deduce la regla física que gobierna todo el diseño radio: **frecuencia y longitud de onda son inversamente proporcionales**. A 100 MHz (FM) la longitud de onda es de 3 metros; a 2,4 GHz (Wi-Fi) es de 12,5 cm; a 26 GHz (5G milimétrico), de 1,15 cm. Y el tamaño de las antenas es proporcional a la longitud de onda, lo que explica que un móvil pueda llevar decenas de antenas de 5G milimétrico y solo una de 700 MHz.

**Las bandas de la UIT.** La nomenclatura oficial divide el espectro en bandas **decádicas** —cada una multiplica por diez la anterior— \[UIT-R\]. Ver **diagrama D5**:

| Banda | Sigla | Frecuencias | Longitud de onda | Uso característico |
|----|----|----|----|----|
| Muy baja frecuencia | **VLF** | 3-30 kHz | 100-10 km | Comunicación con submarinos |
| Baja frecuencia | **LF** | 30-300 kHz | 10-1 km | Radionavegación, onda larga |
| Media frecuencia | **MF** | 300 kHz-3 MHz | 1.000-100 m | **Radiodifusión en onda media (AM)** |
| Alta frecuencia | **HF** | **3-30 MHz** | 100-10 m | **Onda corta**: propagación **ionosférica**, alcance intercontinental |
| Muy alta frecuencia | **VHF** | **30-300 MHz** | 10-1 m | **Radio FM**, TV analógica, aviación, marina |
| Ultra alta frecuencia | **UHF** | **300 MHz-3 GHz** | 1 m-10 cm | **TDT, telefonía móvil, Wi-Fi de 2,4 GHz, TETRA** |
| Súper alta frecuencia | **SHF** | **3-30 GHz** | 10-1 cm | **Microondas**, satélite, Wi-Fi de 5 y 6 GHz, radar |
| Extra alta frecuencia | **EHF** | **30-300 GHz** | 10-1 mm | **Ondas milimétricas**: 5G de 26 GHz, radioenlaces de gran capacidad |

**Formas de propagación.** Tres mecanismos, cada uno dominante en un rango:

1.  **Onda de superficie o terrestre**: la onda sigue la curvatura del terreno. Domina por debajo de **2 MHz** (onda larga y media). Alcance de cientos de kilómetros, con mucha atenuación.
2.  **Onda ionosférica o espacial**: la onda se **refleja** en las capas ionizadas de la atmósfera y vuelve a la Tierra, pudiendo dar varios «saltos». Domina en **HF** (3-30 MHz) y es la que permite la radioafición intercontinental. Depende de la hora, la estación y la actividad solar, lo que la hace **poco fiable** para servicios comerciales.
3.  **Onda directa o de visión directa (*line of sight*)**: la onda viaja en línea recta del emisor al receptor. Domina por encima de **30 MHz**, es decir, en VHF, UHF, SHF y EHF, que son las bandas de **todos** los servicios modernos. Su alcance está limitado por el **horizonte radioeléctrico**, ligeramente superior al óptico por la refracción atmosférica.

> **Dato clave.** La **regla de oro de la radio**, que explica prácticamente todas las decisiones de diseño y de espectro del tema: **a mayor frecuencia**, (a) más **ancho de banda** disponible y por tanto más **capacidad**; (b) antenas y equipos **más pequeños**; pero (c) **menor alcance**, (d) **peor penetración** en paredes y obstáculos, y (e) mayor sensibilidad a la **lluvia** y a los obstáculos móviles. Es exactamente la razón de que el **5G de 700 MHz** se use para **cobertura** rural y en interiores, y el **5G de 26 GHz** para **capacidad** en puntos calientes urbanos (§8.2).

**Radiofrecuencia, microondas e infrarrojos.** Se distinguen tres modalidades, que en rigor son tres tramos del mismo espectro electromagnético:

**Radiofrecuencia en sentido estricto (radiodifusión y radio móvil).** Bandas de MF a UHF. Su rasgo distintivo es que la transmisión suele ser **omnidireccional**: la antena radia en todas las direcciones del plano, y cualquier receptor dentro de la cobertura recibe la señal. Eso la hace idónea para **difusión** (§6.2) y para **movilidad**, y es la banda de la radio, la TDT, la telefonía móvil, el Wi-Fi de 2,4 GHz y TETRA.

**Microondas.** Por convención, de **1 GHz** en adelante (SHF y parte alta de UHF y EHF). Su rasgo distintivo es que las antenas son **directivas** —parabólicas o de bocina—, concentran la energía en un haz estrecho y permiten enlaces punto a punto de gran capacidad. Dos modalidades:

- **Microondas terrestres**: radioenlaces entre torres con **visión directa**. La distancia entre repetidores viene limitada por el horizonte y ronda los **40-50 km** en la práctica. Se usan para interconectar sedes cuando tender fibra es inviable, y como **respaldo** de los enlaces cableados.
- **Microondas por satélite**: el satélite actúa como **repetidor en el cielo**, recibiendo en una frecuencia (enlace ascendente) y retransmitiendo en otra (descendente) para evitar interferencias. Bandas **C** (≈ 4/6 GHz), **Ku** (≈ 12/14 GHz) y **Ka** (≈ 20/30 GHz). Ver §7.2.

**Infrarrojos.** Por encima de las microondas y justo por debajo de la luz visible. Son **de muy corto alcance** y, sobre todo, **no atraviesan paredes**, lo que tiene dos consecuencias opuestas: es una limitación severa (obliga a la visión directa dentro de una habitación) y una **ventaja de seguridad y de reutilización** (la señal no sale del recinto, así que la misma frecuencia puede usarse en la habitación de al lado sin interferencia). Su uso clásico es el mando a distancia y el enlace **IrDA** entre dispositivos; en redes de datos ha sido desplazado por completo por el Wi-Fi, aunque reaparece en la investigación sobre **comunicación por luz visible (Li-Fi)**.

> **Dato clave.** El **infrarrojo no requiere autorización administrativa** de uso del espectro **porque no es espectro radioeléctrico**: queda por encima del límite convencional de 3.000 GHz de la definición legal. Las bandas **ISM** (*Industrial, Scientific and Medical*) de **2,4 GHz** y **5 GHz** sí son espectro radioeléctrico, pero son de **uso común** —no exigen concesión individual, solo cumplir los límites de potencia—, y esa es la razón económica y jurídica de la explosión del Wi-Fi.

#### 2.3. Parámetros de caracterización y calidad en medios de transmisión

Un medio de transmisión —y por extensión un enlace o un servicio— se caracteriza y se contrata por un conjunto de parámetros medibles. Saber **qué mide cada uno y en qué unidad** es lo que permite redactar o interpretar un acuerdo de nivel de servicio. Ver **diagrama D6**.

| Parámetro | Qué mide | Unidad | Qué lo degrada |
|----|----|----|----|
| **Ancho de banda** | Rango de frecuencias del canal | **Hz** | Las características físicas del medio |
| **Capacidad / caudal** (*throughput*) | Bits efectivamente entregados por segundo | **bps** | Ruido, colisiones, sobrecarga de protocolo |
| **Atenuación** | Pérdida de potencia | **dB** (o **dB/km**) | Distancia y frecuencia |
| **Relación señal-ruido** | Cociente entre potencia útil y ruido | **dB** | Ruido térmico, interferencias |
| **Latencia** o retardo | Tiempo que tarda un bit en llegar | **ms** | Distancia, número de saltos, encolamiento |
| **Fluctuación** (*jitter*) | **Variación** de la latencia entre paquetes | **ms** | Encolamiento variable, rutas distintas |
| **Tasa de error de bit (BER)** | Bits erróneos entre bits transmitidos | Adimensional (p. ej. **10⁻⁹**) | Ruido, interferencias, atenuación |
| **Pérdida de paquetes** | Porcentaje de paquetes que no llegan | **%** | Congestión, descartes, errores |
| **Diafonía (NEXT/FEXT)** | Acoplamiento entre pares vecinos | **dB** | Destrenzado, mala conectorización |
| **Disponibilidad** | Porcentaje de tiempo con servicio | **%** (p. ej. 99,9 %) | Averías, cortes, mantenimiento |

Tres precisiones que separan al que ha entendido del que ha memorizado:

**1. Latencia y fluctuación no son lo mismo, y no molestan a lo mismo.** La **latencia** es el retardo; la **fluctuación** es lo irregular que es ese retardo. Una transferencia de ficheros tolera muy bien una latencia alta (tarda más, y ya está) pero le da igual la fluctuación. Una **llamada de voz o una videoconferencia** es justo al revés: sufre con la fluctuación —que produce cortes y voz metálica— y necesita latencia baja para que la conversación sea natural. Los memorias intermedias antifluctuación (*jitter buffers*) del teléfono IP convierten fluctuación en latencia, que es el mal menor.

**2. El decibelio es logarítmico, y por eso engaña.** `dB = 10 · log₁₀(P₁/P₂)` para potencias. Consecuencias clave: **3 dB ≈ el doble** de potencia, **10 dB = diez veces**, **20 dB = cien veces**, **30 dB = mil veces**. Un enlace que pierde 30 dB no ha perdido «un poco más» que uno que pierde 10: ha perdido **cien veces más**. Y las atenuaciones en decibelios de tramos sucesivos **se suman**, en lugar de multiplicarse, que es precisamente la comodidad por la que se usa esta escala.

**3. Caudal no es velocidad nominal.** Entre el régimen binario del medio y los bits útiles que percibe la aplicación hay una diferencia estructural: las **cabeceras** de todos los protocolos implicados, las retransmisiones, el control de flujo y la contienda por el medio. En Wi-Fi la diferencia es especialmente grande —el caudal real ronda **la mitad** o menos de la velocidad nominal anunciada—, porque el medio es compartido y semidúplex, cada trama exige confirmación y el mecanismo de evitación de colisiones consume tiempo. Anunciar «Wi-Fi 6 de 1.200 Mbps» y medir 500 Mbps no es una avería: es el funcionamiento normal.

> **Ejercicio resuelto.** **Elegir el medio para tres enlaces municipales.** Justifique el medio de transmisión más adecuado en cada caso: **(a)** Conectar 40 puestos de trabajo dentro de la planta de una oficina de distrito. **(b)** Conectar esa oficina con el centro de proceso de datos del IAM, a 6 km. **(c)** Dar cobertura de red a una caseta de control de un recinto municipal situada a 800 m del edificio principal, sin canalización disponible y con presupuesto y plazo muy ajustados. **Solución.** **(a)** **Par trenzado Cat 6A** en estrella hasta el armario de planta. Distancias por debajo de 90 m, coste bajo, permite **PoE** para teléfonos y puntos de acceso, y capacidad sobrada. La fibra al puesto sería técnicamente correcta pero económicamente injustificable, y además dejaría sin alimentación a los terminales. **(b)** **Fibra monomodo OS2**. A 6 km el cobre está descartado por atenuación —tres órdenes de magnitud fuera del límite de 100 m—, y la fibra multimodo también, porque su dispersión modal la deja en el orden de cientos de metros. Si el trazado no es propio, la solución práctica es contratar un **circuito de operador** sobre esa misma fibra. **(c)** **Radioenlace de microondas punto a punto** con visión directa, o Wi-Fi exterior direccional en banda de uso común. Es la respuesta correcta precisamente **porque no hay canalización**: abrir zanja para 800 m tiene un coste y un plazo incomparablemente mayores, y requiere licencia de obra. Hay que dejar constancia de los dos condicionantes del medio no guiado: exige **visión directa** despejada y, al ser un medio compartido, obliga a **cifrar el enlace** —lo que en un sistema sujeto al ENS es además exigible por `mp.com.2` y `mp.com.3` (§9.1)—.

> **Relación con otros temas.** Los **conectores y las interfaces del puesto de usuario** (USB, HDMI, DisplayPort, Thunderbolt) corresponden al **Tema 12**. El **cableado estructurado de una red local concreta**, con sus subsistemas y su certificación, se desarrolla en el **Tema 37**.

------------------------------------------------------------------------

### 3. Modos de comunicación

«Modo de comunicación» designa la **forma en que se organiza el intercambio** sobre un medio ya elegido. Hay tres clasificaciones, que son **independientes entre sí** y se combinan: un mismo enlace puede ser a la vez dúplex, síncrono y serie. Conviene subrayarlo desde el principio, porque el error habitual es tratarlas como si fueran tres respuestas alternativas a la misma pregunta.

| Criterio | Pregunta que responde | Categorías |
|----|----|----|
| **Direccionalidad** | ¿En qué sentidos puede fluir la información y cuándo? | Símplex · Semidúplex · Dúplex |
| **Sincronismo** | ¿Cómo sabe el receptor dónde empieza y acaba cada elemento? | Asíncrona · Síncrona |
| **Forma de transmisión** | ¿Cuántos bits viajan a la vez? | Serie · Paralelo |

#### 3.1. Modos según la direccionalidad: simplex, half-duplex y full-duplex

Ver **diagrama D7**.

**Símplex (*simplex*).** La información fluye **en un solo sentido**, siempre el mismo. Un extremo es exclusivamente emisor y el otro exclusivamente receptor, y esa asignación **no se puede invertir**. Todo el ancho de banda del canal se dedica a ese único sentido.

Ejemplos canónicos: la **radiodifusión sonora**, la **televisión digital terrestre**, un teclado hacia el ordenador, un sensor de temperatura que reporta a un concentrador, un panel informativo de tráfico. Todos comparten un rasgo: **no hay ni se espera respuesta por el mismo canal**.

**Semidúplex (*half-duplex*).** Los dos extremos **pueden** emitir y recibir, pero **no simultáneamente**: se turnan. El canal es único y compartido, y hace falta un mecanismo que arbitre el turno —un botón, un protocolo de acceso al medio, una señal de control—. Entre turno y turno existe un **tiempo de conmutación**, que en enlaces de largo retardo llega a ser significativo.

Ejemplos canónicos: el **walkie-talkie**, la radio profesional **TETRA** con su mecanismo de **pulsar para hablar (*push to talk*)**, una red Ethernet antigua sobre **concentrador**, y **todas las redes Wi-Fi** (§7.1).

**Dúplex (*full-duplex*).** Los dos extremos emiten y reciben **a la vez**. Requiere o bien **dos canales físicos** independientes (dos pares, dos fibras), o bien un único canal dividido por **frecuencia** (**FDD**, *Frequency Division Duplex*: una banda para cada sentido) o por **tiempo** con turnos tan rápidos que se perciben como simultáneos (**TDD**, *Time Division Duplex*).

Ejemplos canónicos: la **telefonía** convencional, un enlace **Ethernet conmutado** moderno (par de transmisión y par de recepción separados), una **videollamada**.

> **Dato clave.** Cuatro trampas frecuentes: **(1) El Wi-Fi es SEMIdúplex**, no dúplex, aunque el usuario navegue y suba a la vez. La razón es física: una antena que está transmitiendo **no puede escuchar** en la misma frecuencia, porque su propia emisión ensordece al receptor. Esa misma razón explica por qué en radio se usa **CSMA/CA** (evitación de colisiones) y no CSMA/CD (detección), como se ve en §7.1. **(2) Ethernet moderno es DÚPLEX** desde que se generalizaron los conmutadores; era **semidúplex** con concentradores y con el coaxial en bus. El cambio no fue del cable, sino del **equipo**. **(3) TDD no es semidúplex.** El TDD alterna turnos de emisión y recepción en el orden de los microsegundos, con lo que el servicio percibido **es dúplex**; el semidúplex, en cambio, es una limitación **visible** para el usuario, que tiene que esperar su turno. **(4) «Bidireccional» no equivale a «simultáneo».** Símplex es unidireccional; semidúplex y dúplex son ambos bidireccionales, y lo que los separa es la **simultaneidad**.

> **Ejemplo de aplicación en el ayto.** Los tres modos conviven en un mismo servicio municipal, el de emergencias. La red **TETRA** de la Policía Municipal y del SAMUR es **semidúplex** por diseño: el agente pulsa para hablar y suelta para escuchar. Esa aparente limitación es en realidad una **ventaja operativa** decisiva, porque permite la **comunicación de grupo** —todos los miembros de la patrulla oyen a la vez lo que dice uno— con una disciplina de turno clara, que es justo lo que se necesita en una emergencia y lo que una llamada dúplex punto a punto no da. En paralelo, el teléfono móvil del mismo agente es **dúplex**, y el panel de mensajería variable de la calle por el que se informa a la ciudadanía es **símplex**. Ver **Tema 38**.

#### 3.2. Modos según el sincronismo: transmisión síncrona y asíncrona

El problema que resuelve el sincronismo es elemental y a la vez crítico: el receptor ve una sucesión de niveles eléctricos y tiene que decidir **dónde empieza y dónde acaba cada bit y cada carácter**. Si su reloj se desvía apenas un poco del reloj del emisor, al cabo de unos cientos de bits estará leyendo en el sitio equivocado y todo lo que reciba será basura. Ver **diagrama D8**.

**Transmisión asíncrona.** Se transmite **carácter a carácter** (o, en general, en unidades pequeñas), y cada uno se delimita con bits de servicio:

- Un **bit de arranque (*start*)**, que rompe el estado de reposo de la línea y avisa al receptor de que empieza un carácter. Es el que **resincroniza** el reloj del receptor en cada carácter.
- Los **bits de datos** (típicamente 7 u 8).
- Opcionalmente un **bit de paridad** para detección de errores.
- Uno o dos **bits de parada (*stop*)**, que devuelven la línea al reposo.

Entre carácter y carácter puede transcurrir un tiempo **arbitrario** —de ahí el nombre—: la línea simplemente queda en reposo. Es sencilla, barata y no necesita reloj común, pero paga un precio alto:

> **Ejercicio resuelto.** **Sobrecarga de la transmisión asíncrona.** Se transmite con 8 bits de datos, 1 bit de arranque, 1 de paridad y 1 de parada. **(a)** ¿Qué porcentaje de la capacidad se dedica a información útil? **(b)** Si la línea va a **9.600 bps**, ¿cuántos caracteres útiles por segundo se entregan? **Solución.** **(a)** Bits por carácter: `1 + 8 + 1 + 1 = 11`. Útiles: 8. Eficiencia: `8/11 = 0,727` → **72,7 %**. Sobrecarga: **27,3 %**, más de una cuarta parte del canal. **(b)** `9.600 / 11 ≈ `**`873 caracteres/s`**. **Lectura**: esa sobrecarga del orden del **20-30 %** es constante e independiente del volumen, y es exactamente lo que hace inviable la transmisión asíncrona para transferir grandes volúmenes de datos. La transmisión **síncrona** amortiza sus bits de servicio sobre bloques de cientos o miles de bytes, con lo que su sobrecarga tiende a ser despreciable.

**Transmisión síncrona.** Se transmite en **bloques o tramas** de muchos caracteres, sin delimitadores por carácter. El sincronismo se mantiene de forma continua por alguno de estos medios:

- **Reloj separado**: una línea física dedicada lleva la señal de reloj (posible solo a distancias cortas).
- **Reloj embebido en la señal**: se emplea una **codificación de línea autosincronizante** que garantiza transiciones frecuentes, de las que el receptor extrae el reloj. El ejemplo canónico es la codificación **Manchester**, que fuerza una transición en el centro de cada bit; otros esquemas (**4B/5B**, **8B/10B**, **64B/66B**) insertan bits redundantes con el mismo fin.
- **Preámbulo y delimitadores**: la trama empieza con un patrón conocido —el **preámbulo** de la trama Ethernet, los caracteres SYN de los protocolos orientados a carácter, la bandera `01111110` de HDLC— que permite al receptor engancharse.

La transmisión síncrona es la de **todas** las redes de datos modernas: Ethernet, la jerarquía digital SDH, las interfaces de la telefonía digital, los enlaces de fibra.

|  | **Asíncrona** | **Síncrona** |
|----|----|----|
| **Unidad** | Carácter | **Bloque o trama** |
| **Delimitación** | Bits de arranque y parada | **Preámbulo y delimitadores** |
| **Reloj** | Independiente en cada extremo, se resincroniza cada carácter | **Común** o extraído de la señal |
| **Eficiencia** | Baja (sobrecarga del 20-30 %) | **Alta** |
| **Coste del equipo** | Bajo | Mayor |
| **Uso típico** | Puerto serie, consola de administración, teclados, sensores sencillos | **Ethernet, SDH, fibra, radio digital** |

> **Dato clave.** No confundir **transmisión síncrona** (nivel físico: cómo se mantiene el reloj) con **comunicación síncrona** (nivel de aplicación: si el emisor espera respuesta antes de continuar). Son conceptos de capas distintas que comparten adjetivo. Una llamada a un servicio web puede ser «asíncrona» en el sentido de aplicación y viajar, sin embargo, por un enlace Ethernet perfectamente **síncrono** en el sentido físico.

#### 3.3. Modos según la forma de transmisión: serie y paralelo

**Transmisión en paralelo.** Los bits de un mismo grupo —típicamente un byte— viajan **simultáneamente** por hilos distintos, uno por bit, más las líneas de control. En cada ciclo de reloj se transfiere el grupo entero.

**Transmisión en serie.** Los bits viajan **uno detrás de otro** por un único canal. En cada ciclo de reloj se transfiere un bit (o un símbolo).

La intuición dice que el paralelo debería ser siempre más rápido, ya que mueve ocho bits por el precio de uno. Durante décadas fue así en distancias muy cortas (el bus interno del ordenador, el puerto de impresora Centronics, el bus SCSI, el IDE/PATA de los discos). Pero **al subir la frecuencia el paralelo se derrumba**, y por tres razones acumulativas:

1.  **Desviación temporal (*skew*)**: los hilos no son exactamente iguales, así que los bits que salieron a la vez **no llegan a la vez**. Cuanto más alta es la frecuencia, más corto es el periodo de bit y antes se hace intolerable esa diferencia. Es la limitación decisiva.
2.  **Diafonía**: ocho o dieciséis hilos conmutando a la vez y muy próximos se interfieren mutuamente.
3.  **Coste y volumen**: más hilos, conectores más grandes, cables más rígidos y más caros.

> **Dato clave.** **A alta velocidad y a cualquier distancia gana la transmisión SERIE.** El propio bus interno del ordenador migró de paralelo a serie: **PCI → PCI Express**, **PATA/IDE → SATA**, **puerto paralelo → USB**, **SCSI → SAS**. Y **todas** las redes de datos —Ethernet, fibra, Wi-Fi, WAN— son **serie**. La forma moderna de ganar velocidad no es poner más hilos en paralelo, sino **agrupar varios canales serie independientes**, cada uno con su propio reloj recuperado (los «carriles» de PCI Express, los cuatro pares de 10GBASE-T, la agregación de enlaces 802.1AX).

|  | **Serie** | **Paralelo** |
|----|----|----|
| **Bits simultáneos** | 1 | **n** (8, 16, 32…) |
| **Hilos** | Pocos | Uno por bit + control |
| **Distancia útil** | **Grande** | Muy corta |
| **Frecuencia alcanzable** | **Muy alta** | Limitada por el *skew* |
| **Coste** | Bajo | Alto |
| **Uso actual** | **Todo**: USB, SATA, PCIe, Ethernet, fibra, radio | Residual: buses internos muy cortos, memoria |

> **Relación con otros temas.** Los **buses y las interfaces internas** del equipo microinformático se estudian en el **Tema 11**, y la **conectividad de periféricos** (USB, Thunderbolt) en el **Tema 12**. Aquí interesa únicamente el criterio general —serie frente a paralelo— y su porqué físico.

------------------------------------------------------------------------

### 4. Equipos terminales y de red

El enunciado oficial agrupa en una sola materia dos categorías de equipos que conviene separar desde el principio, porque ocupan **posiciones distintas** en la red:

- Los **equipos terminales** están en los **extremos**: son el origen y el destino de la información, o la adaptan al medio para que pueda salir.
- Los **equipos de interconexión y conmutación** están **en medio**: no generan ni consumen la información, sino que la **encaminan** de un punto a otro.

#### 4.1. Equipos terminales de datos y equipos de conversión

**La pareja ETD/ETCD.** La terminología clásica de las recomendaciones de la UIT-T distingue dos funciones en el extremo de una línea de datos:

- **ETD** (**Equipo Terminal de Datos**; en inglés **DTE**, *Data Terminal Equipment*): el equipo que es **fuente o destino** de los datos. Un ordenador, un servidor, una impresora de red, un terminal de punto de venta, un encaminador visto desde la línea del operador.
- **ETCD** (**Equipo Terminal del Circuito de Datos**; en inglés **DCE**, *Data Circuit-terminating Equipment*): el equipo que **adapta** la señal del ETD a las características del medio de transmisión, y que habitualmente **proporciona la señal de reloj** al ETD y termina físicamente el circuito. Un módem, una unidad de terminación de red, una ONT de fibra.

> **Dato clave.** Tres precisiones sobre ETD/ETCD: (1) el **ETCD suministra el reloj** en los enlaces síncronos, y el ETD se sincroniza con él; (2) el punto donde termina la red del operador y empieza la del cliente se denomina **punto de terminación de red (PTR)**, y es la **frontera de responsabilidad** jurídica y técnica; (3) el **equipo terminal** tiene definición legal: *«el equipo conectado directa o indirectamente a la interfaz de una red pública de telecomunicaciones para transmitir, procesar o recibir información»*, y la ley precisa que la conexión *«podrá realizarse por cable, fibra óptica o vía electromagnética»* y que **también son equipos terminales los de las estaciones terrenas de comunicación por satélite** \[LGT, anexo II.19\].

**Equipos de conversión.** Son los que traducen entre representaciones de la señal, y ya se anticiparon en §1.1:

| Equipo | Qué convierte | Dónde aparece hoy |
|----|----|----|
| **Módem** | Datos **digitales** ↔ señal **analógica** del medio | Módem de cable (DOCSIS), módem ADSL/VDSL, módem de radioenlace, módem de satélite |
| **Códec** | Señal **analógica** de la fuente ↔ **digital** | Telefonía IP, videoconferencia, digitalización de audio y vídeo |
| **Transceptor** (*transceiver*) | Adapta la señal eléctrica a un medio concreto; integra transmisor y receptor | Los módulos **SFP, SFP+, QSFP** intercambiables de conmutadores y encaminadores |
| **Convertidor de medio** | Traduce entre dos medios físicos, sin tocar el contenido | Conversor cobre ↔ fibra en un armario de comunicaciones |
| **Adaptador de terminal** | Adapta un terminal a una interfaz de red que no es la suya | Adaptador de teléfono analógico a red IP (**ATA**) |
| **Multiplexor / demultiplexor** | Agrupa varios canales en uno y lo deshace | Multiplexor de la jerarquía digital, equipo DWDM |
| **ONT / ONU** | Termina la fibra del acceso en casa del cliente | Cajita de fibra de las acometidas FTTH |

> **Dato clave.** El «**router** que da el operador» es, en rigor, **tres equipos en una caja**: un **módem** u **ONT** que termina la línea, un **encaminador** que separa la red del cliente de la del operador, y un **conmutador** con **punto de acceso inalámbrico** que da servicio a los equipos de casa. Muchas dudas sobre equipos de red se resuelven simplemente **desagregando** ese dispositivo en sus funciones.

**Otros equipos terminales.** El terminal ya no es solo el ordenador. En una red municipal actual conviven **teléfonos IP**, **impresoras multifunción**, **cámaras de videovigilancia IP**, **pantallas de gestión de turnos**, **lectores de tarjeta**, **terminales de control de presencia**, **sensores** de temperatura y ocupación y **paneles informativos**. Todos ellos son terminales a efectos de este tema, y todos comparten dos consecuencias prácticas: son **puntos de entrada** a la red que hay que autenticar y segmentar (§9.1), y muchos se alimentan por **PoE**, lo que los ata al conmutador también eléctricamente.

#### 4.2. Equipos de interconexión y conmutación de red

La clasificación **canónica** de los equipos de interconexión es por la **capa del modelo de referencia** en la que operan: cuanto más alta es la capa a la que un equipo «mira», más información maneja, más decisiones puede tomar y más lento y caro resulta. Ver **diagrama D9**.

> **Relación con otros temas.** El **modelo OSI y el modelo TCP/IP** son el objeto del **Tema 34**. Aquí solo se usan sus capas 1, 2 y 3 —física, enlace y red— como **criterio de clasificación** de los equipos, y basta con retener que la capa 1 maneja **señales**, la capa 2 maneja **tramas y direcciones MAC** dentro de una misma red, y la capa 3 maneja **paquetes y direcciones IP** entre redes distintas.

##### 4.2.1. Repetidores, concentradores, puentes, conmutadores y encaminadores

**Repetidor (*repeater*) — capa 1.** Recibe una señal atenuada y deformada, la **regenera** y la retransmite con su forma y amplitud originales. Es importante entender que **no amplifica**: un amplificador multiplicaría también el ruido, mientras que el repetidor **reconstruye la señal digital limpia**, dejando el ruido acumulado a cero. Es la razón de ser de la superioridad de la transmisión digital sobre la analógica en larga distancia (§1.1). Su única función es **extender el alcance** del medio. No entiende de direcciones, ni de tramas, ni filtra nada.

**Concentrador (*hub*) — capa 1.** Es, en esencia, un **repetidor multipuerto**. Todo lo que entra por un puerto sale **regenerado por todos los demás**, sin excepción y sin mirar a quién va dirigido. Consecuencias:

- Todos los equipos conectados comparten el mismo medio: forman **un único dominio de colisión**.
- El ancho de banda nominal se **reparte** entre todos los que transmiten.
- El funcionamiento es forzosamente **semidúplex**.
- Cualquier equipo conectado puede **ver el tráfico de todos los demás**, lo que es un problema de confidencialidad de primer orden.

Está **totalmente obsoleto** y no se instala desde hace dos décadas, pero conviene conocerlo, precisamente porque su comparación con el conmutador es la que fija los conceptos.

**Puente (*bridge*) — capa 2.** Une dos segmentos de red y **decide si deja pasar cada trama** en función de su **dirección MAC de destino**: si origen y destino están en el mismo segmento, la filtra; si están en segmentos distintos, la reenvía. Construye y mantiene una **tabla de direcciones MAC** aprendiendo de las tramas que ve pasar (*aprendizaje transparente*). Su efecto es **segmentar el dominio de colisión** —cada segmento pasa a tener el suyo—. Históricamente era un equipo con dos o cuatro puertos e implementado en software.

**Conmutador (*switch*) — capa 2.** Es un **puente multipuerto implementado en hardware**, y es hoy el equipo central de cualquier red local. Su funcionamiento se resume en cuatro operaciones:

1.  **Aprender**: al recibir una trama, asocia la **MAC de origen** al puerto por el que llegó y lo guarda en su **tabla MAC** (o tabla CAM).
2.  **Reenviar**: busca la **MAC de destino** en la tabla y envía la trama **solo** por el puerto correspondiente.
3.  **Inundar (*flooding*)**: si la MAC de destino **no está** en la tabla, o es una dirección de **difusión** o **multidifusión**, envía la trama por **todos** los puertos menos el de entrada.
4.  **Envejecer**: elimina de la tabla las entradas que llevan un tiempo sin usarse.

> **Dato clave.** **El conmutador segmenta el dominio de COLISIÓN, pero NO el dominio de DIFUSIÓN.** Cada puerto es su propio dominio de colisión y puede trabajar en **dúplex**, pero una trama de difusión (`FF:FF:FF:FF:FF:FF`) se propaga por **todos** los puertos. Para dividir el dominio de difusión solo hay dos caminos: un **encaminador** (capa 3) o unas **VLAN** \[IEEE802.1\] configuradas en el propio conmutador —que en realidad es lo mismo, porque cada VLAN es un dominio de difusión distinto y para pasar de una a otra hace falta encaminamiento—. Esta es, con diferencia, **la distinción central sobre equipos de red**. Ver **diagrama D10**.

Los conmutadores admiten tres **modos de conmutación**, con un compromiso entre latencia y fiabilidad:

| Modo | Cuándo empieza a reenviar | Latencia | Detecta tramas erróneas |
|----|----|----|----|
| **Almacenamiento y reenvío** (*store and forward*) | Tras recibir la **trama completa** y comprobar su **CRC** | Mayor | **Sí** |
| **Directo** (*cut-through*) | Tras leer solo la **MAC de destino** (6 primeros bytes) | Mínima | No |
| **Libre de fragmentos** (*fragment free*) | Tras leer los **primeros 64 bytes** | Intermedia | Parcialmente |

**Encaminador (*router*) — capa 3.** Interconecta **redes distintas** y decide por dónde enviar cada **paquete** en función de su **dirección IP de destino** y de una **tabla de encaminamiento**. Sus rasgos distintivos frente al conmutador:

- Trabaja con **direcciones lógicas (IP)**, jerárquicas y asignadas por el administrador, no con direcciones físicas grabadas de fábrica.
- **Detiene la difusión**: cada una de sus interfaces delimita un **dominio de difusión distinto**. Es su función más característica.
- **Decrementa el TTL** de cada paquete y descarta el que llega a cero, lo que **elimina los bucles infinitos**. La trama Ethernet, en cambio, **no tiene TTL**, y por eso un bucle de capa 2 es catastrófico y necesita el protocolo **STP** para evitarse.
- Puede **fragmentar** paquetes al pasar de una red con MTU grande a otra con MTU pequeña.
- Ejecuta **protocolos de encaminamiento** (RIP, OSPF, BGP) para construir dinámicamente su tabla.
- Suele concentrar funciones adicionales: traducción de direcciones (**NAT**), listas de control de acceso, calidad de servicio, terminación de túneles.

**Conmutador de capa 3.** Equipo intermedio y muy frecuente en la práctica: físicamente un conmutador, con muchos puertos y conmutación por hardware, pero capaz de **encaminar entre VLAN** a velocidad de cable. Es el corazón habitual del núcleo de una red de edificio. La distinción clave: el **conmutador de capa 3 encamina entre las redes internas**, mientras que el **encaminador de frontera** conecta con redes externas y aporta las funciones de acceso y seguridad.

|  | **Concentrador** | **Conmutador** | **Encaminador** |
|----|----|----|----|
| **Capa** | 1 — física | 2 — enlace | 3 — red |
| **Direcciones que usa** | Ninguna | **MAC** | **IP** |
| **Criterio de reenvío** | Ninguno: repite por todos | Tabla **MAC** | Tabla de **encaminamiento** |
| **Dominios de colisión** | **1** | **Uno por puerto** | Uno por interfaz |
| **Dominios de difusión** | **1** | **1** (salvo VLAN) | **Uno por interfaz** |
| **Dúplex** | Semidúplex | **Dúplex** | Dúplex |
| **Descarta bucles** | No | Con **STP** | **Sí**, por TTL |

> **Ejercicio resuelto.** **Contar dominios de colisión y de difusión.** Una red municipal tiene: un **encaminador** con **3** interfaces activas; conectado a la primera, un **conmutador** de **24** puertos con **24** equipos; a la segunda, un **concentrador** con **8** equipos; y a la tercera, un **conmutador** de **12** puertos configurado con **3 VLAN**, con **12** equipos repartidos entre ellas. ¿Cuántos dominios de colisión y de difusión hay? **Solución.** **Dominios de colisión.** Cada puerto activo de conmutador es uno; el concentrador entero es **uno solo**; cada interfaz de encaminador es uno. - Conmutador de 24 puertos: `24` puertos con equipo + `1` de subida al encaminador = **25**. - Concentrador: **1** (los 8 equipos comparten medio) + `1` del enlace concentrador-encaminador… que es **el mismo** dominio, porque el concentrador no segmenta: **1**. - Conmutador de 12 puertos: `12` + `1` de subida = **13**. - Total: `25 + 1 + 13 = `**`39 dominios de colisión`**. **Dominios de difusión.** Uno por interfaz de encaminador, salvo que haya VLAN, que multiplican. - Interfaz 1 (conmutador plano): **1**. - Interfaz 2 (concentrador): **1**. - Interfaz 3 (conmutador con 3 VLAN): **3**. - Total: `1 + 1 + 3 = `**`5 dominios de difusión`**. **Lectura del resultado**: el concentrador es un desastre en colisiones (ocho equipos compitiendo por un medio) pero indiferente en difusión; el conmutador arregla lo primero y **no toca lo segundo**; y solo las **VLAN** y el **encaminador** actúan sobre la difusión. La conclusión operativa —y la razón por la que el ENS exige `mp.com.4`— es que **acotar el dominio de difusión es lo que limita la propagación de un incidente**.

##### 4.2.2. Pasarelas y puntos de acceso inalámbricos

**Pasarela (*gateway*).** El término tiene dos acepciones:

1.  **Acepción estricta y clásica**: equipo que interconecta redes con **arquitecturas o protocolos distintos**, realizando la **traducción completa** entre ellos, hasta la capa de aplicación si es preciso. Es, por definición, el equipo de interconexión **de más alto nivel**. Ejemplos: una **pasarela de voz** que traduce entre la red telefónica conmutada y la telefonía IP; una pasarela de correo entre dos sistemas de mensajería distintos; una pasarela de IoT que traduce entre Zigbee o LoRaWAN e IP; una pasarela de pago que traduce entre un comercio y una red bancaria.
2.  **Acepción coloquial**: la «**puerta de enlace predeterminada**» (*default gateway*) que se configura en cada equipo, que es simplemente **la dirección IP del encaminador** al que se envía todo lo que no es local. En esta acepción, la pasarela es un **encaminador de capa 3**, no un traductor de protocolos.

> **Dato clave.** Si el enunciado pregunta por el equipo de interconexión que opera **en las capas superiores** y **traduce entre arquitecturas distintas**, la respuesta es **pasarela**. Si pregunta por la dirección que se configura en el equipo para salir de la red local, la respuesta es **puerta de enlace predeterminada**, que es un **encaminador**. Es el mismo nombre para dos cosas distintas.

**Punto de acceso inalámbrico (*access point*, AP) — capa 2.** Equipo que crea una **celda** de red inalámbrica y actúa de puente entre esa celda y la red cableada. Conceptualmente es un **puente entre dos medios**: convierte tramas 802.11 en tramas 802.3 y viceversa. Sus elementos, que se detallan en §7.1:

- Anuncia un identificador de red, el **SSID**, mediante tramas de **baliza (*beacon*)** periódicas.
- Los clientes se **asocian** a él y quedan bajo su control de acceso al medio.
- Un punto de acceso con sus clientes forma un **BSS** (*Basic Service Set*), identificado por el **BSSID**, que normalmente es la MAC de la radio del punto de acceso.
- Varios puntos de acceso con el mismo SSID forman un **ESS** (*Extended Service Set*), entre cuyas celdas el cliente puede desplazarse con **itinerancia interna (*roaming*)**.

En instalaciones profesionales los puntos de acceso no se configuran uno a uno, sino que son **ligeros (*thin*)** y se gestionan desde un **controlador de red inalámbrica (WLC)**, que centraliza la configuración, el reparto de canales y potencias, la itinerancia rápida y la aplicación de la política de seguridad. Este es el modelo de cualquier despliegue municipal serio.

**Otros equipos que conviene situar.** Aunque su desarrollo corresponde a otros temas, hay que poder ubicarlos en el cuadro:

| Equipo | Capa | Función | Tema |
|----|----|----|----|
| **Cortafuegos** (*firewall*) | 3-4, o 7 si es de aplicación | Filtra el tráfico según una política de seguridad | **T36** |
| **Servidor intermediario** (*proxy*) | 7 | Intermedia peticiones de aplicación; almacena en caché y filtra | T36 |
| **Balanceador de carga** | 4 o 7 | Reparte peticiones entre varios servidores | T22, T31 |
| **Controlador inalámbrico (WLC)** | 2 | Gestiona una flota de puntos de acceso | Este tema, §7.1 |
| **Servidor de acceso remoto / concentrador VPN** | 3 | Termina túneles cifrados de acceso remoto | **T36** |

> **Ejemplo de aplicación en el ayto.** Recorrido de un paquete desde el puesto de la Oficina de Atención a la Ciudadanía hasta la aplicación de tramitación del CPD del IAM, nombrando cada equipo: (1) la **tarjeta de red** del puesto —terminal— pone la trama en el par trenzado; (2) el **conmutador de planta** la recibe, la asocia a la VLAN de puestos de trabajo y la reenvía por su enlace de subida, sin sacarla por los demás puertos; (3) el **conmutador de capa 3** del edificio decide que el destino está en otra red y **encamina** el paquete; (4) el **encaminador de frontera** lo mete por el enlace de fibra hacia el CPD, aplicando la calidad de servicio contratada; (5) en el otro extremo, un **cortafuegos** comprueba la política antes de dejarlo entrar; (6) un **balanceador** elige a cuál de los servidores de la granja se lo entrega. Seis equipos, cuatro capas y una sola pulsación de tecla.

------------------------------------------------------------------------

### 5. Redes de comunicaciones

Una **red de comunicaciones** es el conjunto de medios de transmisión, equipos y protocolos que permite la comunicación entre un número arbitrario de terminales. Como en §2.2.1, conviene arrancar de la definición legal, porque es la que delimita el objeto de la regulación:

> **Dato clave.** **Red de comunicaciones electrónicas**: *«los sistemas de transmisión, se basen o no en una infraestructura permanente o en una capacidad de administración centralizada, y, cuando proceda, los equipos de conmutación o encaminamiento y demás recursos, incluidos los elementos de red que no son activos, que permitan el transporte de señales mediante cables, ondas hertzianas, medios ópticos u otros medios electromagnéticos con inclusión de las redes de satélites, redes fijas (de conmutación de circuitos y de paquetes, incluido internet) y móviles, sistemas de tendido eléctrico, en la medida en que se utilicen para la transmisión de señales, redes utilizadas para la radiodifusión sonora y televisiva y redes de televisión por cable, **con independencia del tipo de información transportada**»* \[LGT, anexo II.61\]. Obsérvese que la definición incluye expresamente **los elementos que no son activos** —conductos, arquetas, torres— y que es **neutral respecto del contenido**.

La misma ley añade dos definiciones cuantitativas:

- **Red de alta capacidad**: la capaz de prestar acceso de banda ancha a **al menos 30 Mbps** \[LGT, anexo II.62\].
- **Red de muy alta capacidad**: la compuesta **totalmente de elementos de fibra óptica** al menos hasta el punto de distribución de la localización donde se presta el servicio, **o** la capaz de ofrecer un rendimiento similar en condiciones usuales de máxima demanda \[LGT, anexo II.63\].

Y una definición de la que penden consecuencias jurídicas importantes: **red pública de comunicaciones electrónicas** es la utilizada *«principalmente para la prestación de servicios de comunicaciones electrónicas disponibles para el público»* \[LGT, anexo II.64\]. La red interna del Ayuntamiento **no** es una red pública en ese sentido: es una red privada de un usuario final, aunque sirva a un servicio público. La distinción es la que decide si son aplicables las obligaciones de los operadores del art. 63 (§9.2).

#### 5.1. Clasificación por cobertura geográfica: PAN, LAN, MAN y WAN

La clasificación por **extensión geográfica** es la más clásica. Ver **diagrama D11**.

| Red | Nombre | Alcance típico | Titularidad | Ejemplos |
|----|----|----|----|----|
| **PAN** | *Personal Area Network* | **Metros** (entorno de una persona) | Del propio usuario | Bluetooth, NFC, Zigbee, USB |
| **LAN** | *Local Area Network* | Edificio o recinto: **decenas a cientos de metros** | **Privada**, del propietario del recinto | Ethernet y Wi-Fi de una oficina de distrito |
| **CAN** | *Campus Area Network* | Varios edificios contiguos de un mismo titular | Privada | Recinto universitario, complejo municipal |
| **MAN** | *Metropolitan Area Network* | **Ciudad o área metropolitana**: decenas de kilómetros | Privada o de operador | Anillo de fibra que une las sedes municipales |
| **WAN** | *Wide Area Network* | **País o continente**, sin límite | Casi siempre de **operador** | Internet, red corporativa multisede, Red SARA |

A esa escala principal se añaden categorías por criterios distintos que conviene conocer para no confundirlas:

- **BAN** (*Body Area Network*): red de sensores sobre el cuerpo, \[IEEE802.15\].6.
- **SAN** (*Storage Area Network*): red **dedicada al almacenamiento**, que conecta servidores con cabinas de disco. No se clasifica por extensión, sino por **función**. Ver **Tema 26**.
- **VPN** (*Virtual Private Network*): red privada **lógica** construida sobre una red pública mediante túneles cifrados. No es una categoría geográfica, sino de **arquitectura**. Ver **Tema 36**.
- **WLAN, WPAN, WMAN, WWAN**: las versiones **inalámbricas** de las anteriores. La `W` inicial es de *wireless*, y es un prefijo, no un nivel más de la escala (§7).
- **GAN** (*Global Area Network*): término poco usado para la cobertura mundial, típicamente por satélite.

> **Dato clave.** Los tres criterios que **de verdad** distinguen una LAN de una WAN, más allá de los kilómetros, y que son los que hacen buena la clasificación: **(1) Titularidad del medio.** En la **LAN** el cableado es **propiedad** de quien la explota; en la **WAN** casi siempre se **contrata** a un operador, porque atraviesa dominio público. Esta es la diferencia estructural. **(2) Velocidad y latencia.** La LAN ofrece gigabits con latencias de microsegundos; la WAN, caudales menores por unidad de coste y latencias de milisegundos. **(3) Tasa de error.** La LAN opera sobre medios controlados y con tasas de error muy bajas; la WAN atraviesa medios heterogéneos y necesita más control de errores.

**Otras clasificaciones útiles de las redes.** El enunciado oficial no las pide expresamente, pero conviene conocerlas:

| Criterio | Categorías |
|----|----|
| **Titularidad** | **Públicas** (disponibles al público, de operador) frente a **privadas** o corporativas |
| **Relación entre nodos** | **Cliente-servidor** frente a **entre iguales** (*peer to peer*) |
| **Medio** | **Cableadas** frente a **inalámbricas**; **fijas** frente a **móviles** |
| **Técnica de transferencia** | **Conmutadas** frente a **de difusión** (§6) |
| **Tipo de conmutación** | De **circuitos**, de **mensajes** o de **paquetes** (§6.1) |

#### 5.2. Topologías de red físicas y lógicas

La **topología** es la forma en que se disponen los nodos y los enlaces de una red. Hay que distinguir dos planos:

- **Topología física**: cómo está **tendido el cable** y dónde están físicamente los equipos.
- **Topología lógica**: cómo **circula realmente la señal** y cómo se accede al medio, con independencia del trazado.

> **Dato clave.** El ejemplo canónico de divergencia entre ambas: **Ethernet moderno sobre conmutador es una estrella física** —todos los cables van radialmente al armario— **con topología lógica de bus conmutado**, en la que cada puerto es un enlace punto a punto dedicado. Y el caso histórico más citado: **Token Ring** era una **estrella física** (todos los cables iban a una unidad de acceso central, la MAU) con **anillo lógico**, porque la señal recorría internamente un bucle. Confundir los dos planos es el error clásico.

Ver **diagrama D12**. Las topologías físicas básicas son seis:

**1. Bus.** Todos los nodos comparten un **único medio troncal**, terminado en sus dos extremos con **terminadores** que evitan las reflexiones. La señal se propaga en ambos sentidos y todos la reciben; cada nodo se queda con lo que va dirigido a él.

- *Ventajas*: mínimo cableado, sencilla y barata, fácil de ampliar en su día.
- *Inconvenientes*: **un corte en el troncal deja sin servicio a toda la red**; medio compartido con colisiones; difícil de diagnosticar; longitud limitada.
- *Ejemplo*: Ethernet original sobre coaxial (10BASE5, 10BASE2). Hoy **en desuso** en datos, aunque el principio sobrevive en buses industriales como CAN.

**2. Anillo.** Cada nodo se conecta exactamente con el **anterior y el siguiente**, cerrando un bucle. La información circula en un sentido y cada nodo la **regenera** y la pasa al siguiente. Suele usar un **testigo (*token*)** que da el turno de transmisión, con lo que **no hay colisiones** y el retardo es acotado y predecible.

- *Ventajas*: acceso **determinista** —se sabe cuánto se espera como máximo—, buen rendimiento con carga alta, cada nodo regenera la señal.
- *Inconvenientes*: **la caída de un nodo rompe el anillo**, salvo que haya doble anillo o conmutación de derivación; añadir o quitar nodos interrumpe el servicio.
- *Ejemplos*: **Token Ring**, **FDDI** (con **doble anillo** contrarrotatorio para tolerancia a fallos) y, muy vivo hoy, los **anillos de fibra metropolitanos** de operador, con protección por conmutación al anillo de reserva en **menos de 50 ms**.

**3. Estrella.** Todos los nodos se conectan a un **nodo central** —hoy un conmutador— y toda la comunicación pasa por él.

- *Ventajas*: **el fallo de un enlace o de un nodo solo afecta a ese nodo**; muy fácil de diagnosticar y de gestionar (la gestión se concentra en un punto); permite dúplex y ancho de banda dedicado por puerto.
- *Inconvenientes*: **el nodo central es un punto único de fallo** y un cuello de botella; consume más cable que el bus.
- *Ejemplo*: **es la topología física de prácticamente toda LAN moderna**, cableada o inalámbrica (donde el punto de acceso hace de centro).

**4. Árbol (o estrella jerárquica).** Varias estrellas conectadas jerárquicamente a través de nodos de nivel superior. Es la topología real de cualquier red de edificio: conmutadores de planta (**acceso**) que suben a conmutadores de edificio (**distribución**) que suben al **núcleo**. Hereda las ventajas de la estrella y añade **escalabilidad**, a costa de que el fallo de un nodo intermedio aísla toda su rama.

**5. Malla (*mesh*).** Cada nodo se conecta con varios otros, ofreciendo **caminos alternativos** entre cualquier par.

- **Malla completa**: todos con todos. El número de enlaces es `n(n−1)/2`, que crece cuadráticamente y la hace **impracticable** salvo para muy pocos nodos.
- **Malla parcial**: solo los enlaces necesarios para garantizar redundancia. Es la de uso real.
- *Ventajas*: **máxima tolerancia a fallos**, reparto de carga, sin punto único de fallo.
- *Inconvenientes*: coste y complejidad de gestión.
- *Ejemplos*: la **red troncal de internet**, las redes de operador, las **redes inalámbricas malladas** \[IEEE802.11\].s y las de sensores Zigbee.

**6. Mixta o híbrida.** La combinación de las anteriores, que es lo que existe en la realidad: una red municipal es un **árbol** dentro de cada edificio, una **malla parcial** entre los nodos troncales y un **anillo** de fibra en el nivel metropolitano.

> **Ejercicio resuelto.** **Enlaces de una malla completa.** Se plantea unir mediante malla completa los **12** centros municipales de un distrito. **(a)** ¿Cuántos enlaces harían falta? **(b)** Si se añadieran **3** centros más, ¿cuántos enlaces nuevos habría que tender? **(c)** ¿Cuál es la conclusión de diseño? **Solución.** **(a)** `n(n−1)/2 = 12 · 11 / 2 = `**`66 enlaces`**. **(b)** Con 15: `15 · 14 / 2 = 105`. Enlaces nuevos: `105 − 66 = `**`39`**. Es decir, **añadir 3 nodos exige 39 enlaces nuevos**, uno por cada nodo preexistente y los de entre ellos. **(c)** El crecimiento es **cuadrático**: la malla completa **no escala**. La solución real es una **malla parcial** —redundancia solo donde el análisis de riesgos la exige— o un **doble anillo**, que con `n` enlaces ya garantiza dos caminos entre cualquier par de nodos. Por eso las redes metropolitanas de fibra se construyen en anillo y no en malla.

**Criterios de elección.** Cuadro resumen:

| Topología | Coste de cable | Tolerancia a fallos | Facilidad de diagnóstico | Punto único de fallo |
|----|----|----|----|----|
| **Bus** | **Mínimo** | Muy baja | Muy difícil | El troncal |
| **Anillo** | Bajo | Baja (media con doble anillo) | Media | Cualquier nodo |
| **Estrella** | Medio | Media | **Muy fácil** | **El nodo central** |
| **Árbol** | Medio-alto | Media | Fácil | Los nodos superiores |
| **Malla** | **Máximo** | **Máxima** | Compleja | **Ninguno** |

> **Ejemplo de aplicación en el ayto.** La red de la Oficina de Atención a la Ciudadanía es un **árbol**: cada puesto en estrella hasta el conmutador de planta, cada conmutador de planta en estrella hasta el conmutador del edificio. Ese conmutador de edificio se conecta al CPD del IAM por **dos** caminos —fibra principal y radioenlace de respaldo—, lo que introduce una **malla parcial mínima** de dos enlaces, que es la respuesta económicamente razonable al riesgo de corte de fibra por una obra en la vía pública. Y el nivel metropolitano que une los centros municipales se organiza en **anillo** de fibra, con protección automática. Tres topologías distintas en tres niveles del mismo servicio, cada una elegida por su criterio: **coste** abajo, **redundancia** arriba.

------------------------------------------------------------------------

### 6. Redes de conmutación y redes de difusión

Esta sección responde a una pregunta distinta de la anterior: no **dónde** están los nodos, sino **cómo llega la información de uno a otro**. La clasificación de primer nivel divide todas las redes en dos grandes familias \[TANENBAUM\]:

- **Redes de conmutación** (o **punto a punto**): la información viaja de nodo en nodo por una sucesión de enlaces, y en cada nodo intermedio **alguien decide** hacia dónde sigue. Ese acto de decisión es la **conmutación**. Son las redes de gran extensión.
- **Redes de difusión** (*broadcast*): existe **un único canal compartido** por todos los nodos, de modo que lo que emite uno **lo reciben todos**, y cada cual decide si el mensaje va dirigido a él. No hay nodos intermedios que decidan. Son las redes pequeñas y las radioeléctricas.

> **Dato clave.** La correlación clásica: **las redes pequeñas y locales tienden a ser de difusión** (medio compartido) y **las grandes tienden a ser de conmutación** (imposible compartir un solo medio entre millones de nodos). No es una ley absoluta —la LAN conmutada moderna es punto a punto por puerto— pero es el criterio con el que se construyó la clasificación.

#### 6.1. Redes de conmutación

**Conmutar** es establecer, en un nodo de la red, un camino temporal entre una entrada y una salida. La red de conmutación es, entonces, una **malla de nodos conmutadores** unidos por enlaces, a la que se conectan los terminales por sus bordes. Las tres técnicas históricas se distinguen por **qué se conmuta y cuándo se decide la ruta**. Ver **diagrama D13**.

##### 6.1.1. Conmutación de circuitos, de mensajes y de paquetes

**A. Conmutación de circuitos.**

Antes de intercambiar información se **establece un camino físico dedicado** de extremo a extremo, reservando en cada nodo intermedio los recursos necesarios. Ese camino permanece **reservado en exclusiva** durante toda la comunicación, se use o no, y se libera al terminar. Tres fases obligatorias:

1.  **Establecimiento**: se señaliza la petición, se busca ruta y se reservan recursos en cada nodo. Introduce un **retardo inicial** apreciable (el tiempo que tarda en «dar tono» y establecer la llamada).
2.  **Transferencia**: la información fluye por el camino reservado, **sin cabeceras de direccionamiento** —el camino ya sabe adónde va— y con **retardo constante**.
3.  **Liberación**: se sueltan los recursos de todos los nodos.

- *Ventajas*: **caudal garantizado** durante toda la comunicación; **retardo constante y mínimo** una vez establecido, sin fluctuación; entrega **ordenada**; transparencia total al contenido.
- *Inconvenientes*: **desaprovecha** la capacidad reservada en los silencios (en una conversación telefónica se calla más de la mitad del tiempo); retardo de establecimiento; **si no hay recursos, la llamada se rechaza** (bloqueo) en lugar de degradarse; poco tolerante a fallos, porque la caída de un nodo del camino **corta** la comunicación y obliga a rehacerla.
- *Ejemplo canónico*: la **red telefónica conmutada (RTC)**, y su versión digital **RDSI**. También la conmutación óptica de circuitos en las troncales.

**B. Conmutación de mensajes.**

**No se reserva ningún camino.** El mensaje **completo**, con la dirección de destino en su cabecera, se envía al primer nodo, que lo **almacena** íntegramente, elige la ruta siguiente y lo **reenvía** cuando el enlace queda libre. Es la técnica de **almacenamiento y reenvío (*store and forward*)** en estado puro.

- *Ventajas*: aprovecha mucho mejor los enlaces que la conmutación de circuitos, porque no reserva nada; permite **prioridades** entre mensajes; permite **difusión** a varios destinos; y **nunca hay bloqueo**: si el enlace está ocupado, el mensaje espera en cola.
- *Inconvenientes*: **retardos altos y muy variables**; los nodos necesitan **mucha memoria** para almacenar mensajes enteros de tamaño arbitrario; **un mensaje grande monopoliza** el enlace y bloquea a los que van detrás; y no sirve para tráfico interactivo o en tiempo real.
- *Estado actual*: **en desuso como técnica de red**. Su ejemplo histórico fue el télex y la conmutación de telegramas. Pero **su lógica sobrevive** en el **correo electrónico**, donde cada servidor almacena el mensaje completo y lo reenvía al siguiente, y en los sistemas de mensajería por colas.

**C. Conmutación de paquetes.**

La información se **divide en paquetes** de tamaño limitado, cada uno con su **cabecera de direccionamiento**, y cada paquete se conmuta de forma independiente por almacenamiento y reenvío. Es la técnica de **internet y de todas las redes de datos modernas**.

La fragmentación en paquetes pequeños resuelve de golpe los dos grandes defectos de la conmutación de mensajes:

- Los nodos solo necesitan memoria para paquetes, no para mensajes enteros.
- Y sobre todo, se produce **encauzamiento (*pipelining*)**: mientras el nodo 2 reenvía el primer paquete al nodo 3, el nodo 1 ya le está enviando el segundo. El resultado es que **el retardo total no es la suma de los tiempos de transmisión completos**, sino mucho menor.

Su recurso clave es la **multiplexación estadística**: el enlace se reparte dinámicamente entre quien tiene algo que enviar en cada instante, sin reservas fijas. Eso da un aprovechamiento del medio muy superior, al precio de que, si en un instante todos quieren transmitir, hay **congestión**, colas, **fluctuación** y eventualmente **pérdida de paquetes**.

Dos modalidades:

|  | **Datagrama** | **Circuito virtual** |
|----|----|----|
| **Ruta** | **Cada paquete decide la suya** en cada nodo | Se fija **una vez**, al inicio, y todos la siguen |
| **Fase previa** | Ninguna: sin conexión | **Establecimiento** del circuito virtual |
| **Cabecera** | Dirección **completa** de destino en cada paquete | **Identificador** corto del circuito virtual |
| **Orden de llegada** | **Puede desordenarse** | **Garantizado** |
| **Ante caída de un nodo** | Los paquetes se **reencaminan** solos | El circuito **se cae** y hay que rehacerlo |
| **Ejemplos** | **IP**, la base de internet | **X.25**, **Frame Relay**, **ATM**, **MPLS** |

> **Dato clave.** El **circuito virtual no es un circuito**: no hay reserva de recursos físicos ni camino dedicado, solo una **ruta preacordada** identificada por una etiqueta corta. Es una técnica de **conmutación de paquetes**, no de circuitos. Y **MPLS**, el mecanismo con el que los operadores construyen hoy las redes privadas virtuales de sus clientes corporativos, es exactamente eso: conmutación de paquetes por **etiquetas** con lógica de circuito virtual. Confundirlo con la conmutación de circuitos es el error clásico de esta sección.

**Cuadro comparativo de las tres técnicas** —el que hay que ser capaz de reproducir—:

|  | **Circuitos** | **Mensajes** | **Paquetes** |
|----|----|----|----|
| **Qué se conmuta** | Un **camino físico** | El **mensaje completo** | **Paquetes** de tamaño limitado |
| **Reserva de recursos** | **Sí**, en exclusiva | No | No |
| **Fase de establecimiento** | **Sí**, obligatoria | No | Solo en circuito virtual |
| **Almacenamiento y reenvío** | No | **Sí** | **Sí** |
| **Aprovechamiento del enlace** | **Bajo** | Alto | **Máximo** |
| **Retardo** | Alto al establecer, **constante** después | **Alto y variable** | Bajo y **variable** |
| **Fluctuación** | **Ninguna** | Alta | Media |
| **Ante saturación** | **Bloqueo**: se rechaza | Encolamiento | **Degradación**: colas y descartes |
| **Memoria en los nodos** | Mínima | **Muchísima** | Moderada |
| **Ejemplo** | **RTC**, RDSI | Télex; hoy, correo electrónico | **IP, internet, todo lo moderno** |

> **Ejercicio resuelto.** **Comparar retardos.** Un mensaje de **9.000 bits** debe atravesar **3 enlaces** (es decir, 2 nodos intermedios) de **3.000 bps** cada uno. Desprecie el retardo de propagación y de proceso. **(a)** Retardo total por **conmutación de mensajes**. **(b)** Retardo total por **conmutación de paquetes**, con paquetes de **3.000 bits** (sin contar cabeceras). **Solución.** **(a)** En conmutación de mensajes, cada nodo debe recibir el mensaje **entero** antes de reenviarlo. Tiempo de transmisión del mensaje en un enlace: `9.000 / 3.000 = 3 s`. Como son 3 enlaces en serie sin solapamiento: `3 · 3 = `**`9 s`**. **(b)** En conmutación de paquetes hay 3 paquetes de 3.000 bits; cada uno tarda `3.000 / 3.000 = 1 s` por enlace. El **primer paquete** llega al destino tras 3 enlaces: `3 · 1 = 3 s`. Los otros dos vienen **detrás en cascada**, uno por segundo: `+1 s` y `+1 s`. Total: `3 + 1 + 1 = `**`5 s`**. **Fórmula general**: `T = (N.º de enlaces + N.º de paquetes − 1) · tiempo de un paquete`, aquí `(3 + 3 − 1) · 1 = 5 s`. **Lectura del resultado**: la conmutación de paquetes ha reducido el retardo **casi a la mitad** sin cambiar ni un solo cable, solo por **encauzamiento**. Y con paquetes más pequeños mejoraría aún más, hasta que el peso de las cabeceras contrarrestara la ganancia. Ahí está el porqué de que internet funcione con paquetes.

#### 6.2. Redes de difusión

##### 6.2.1. Principios de difusión, direcciones broadcast y multicast

**El principio de difusión.** En una red de difusión existe **un solo canal de comunicación compartido** por todas las estaciones. Cuando una transmite, **todas las demás reciben** la señal; cada una examina la dirección de destino y se queda con el mensaje solo si va dirigido a ella, descartándolo en caso contrario.

De ese principio se derivan cuatro consecuencias:

1.  **Hace falta un método de acceso al medio**, porque si dos estaciones transmiten a la vez se produce una **colisión**. Ese método es CSMA/CD en la Ethernet clásica, **CSMA/CA** en Wi-Fi (§7.1) y el paso de testigo en las redes de anillo. *Su desarrollo corresponde al **Tema 37**.*
2.  **La capacidad se reparte** entre todas las estaciones activas.
3.  **La confidencialidad es estructuralmente débil**: cualquier estación puede poner su interfaz en **modo promiscuo** y quedarse con todo el tráfico. Es la razón última de que un concentrador sea inaceptable hoy y de que las redes inalámbricas exijan **cifrado del enlace radio**.
4.  **La difusión es una capacidad nativa y barata**: enviar a todos cuesta exactamente lo mismo que enviar a uno.

Sobre esa base se definen los **cuatro modos de entrega**, que hay que distinguir con precisión. Ver **diagrama D14**:

| Modo | Destinatarios | Descripción |
|----|----|----|
| **Unidifusión** (*unicast*) | **Uno** | Uno a uno. Es la inmensa mayoría del tráfico |
| **Multidifusión** (*multicast*) | **Un grupo** | Uno a los miembros de un grupo que se han **suscrito** voluntariamente |
| **Difusión** (*broadcast*) | **Todos** los del dominio | Uno a todos, sin suscripción |
| **Anydifusión** (*anycast*) | **El más cercano** del grupo | Uno a **cualquiera**, típicamente el más próximo según la métrica de encaminamiento. Propio de **IPv6** y de los DNS raíz |

**Direcciones de difusión y de multidifusión.** Los datos concretos son de memorización obligatoria:

> **Dato clave.** **Nivel 2 (Ethernet).** Dirección MAC de **difusión**: **`FF:FF:FF:FF:FF:FF`** (los 48 bits a uno). Las MAC de **multidifusión** son las que tienen el **bit menos significativo del primer octeto a 1**; el rango reservado para multidifusión IPv4 empieza por **`01:00:5E`**. **Nivel 3 (IPv4).** Difusión **limitada**: **`255.255.255.255`**, que **nunca se encamina** —el encaminador la descarta siempre—. Difusión **dirigida a subred**: la que tiene todos los bits de host a 1 (por ejemplo, `192.168.10.255` en una `/24`). **Multidifusión**: el antiguo espacio de **clase D**, **`224.0.0.0/4`** (de 224.0.0.0 a 239.255.255.255), con direcciones bien conocidas como `224.0.0.1` (todos los equipos del enlace) y `224.0.0.2` (todos los encaminadores). **Nivel 3 (IPv6).** **IPv6 NO TIENE DIFUSIÓN.** La sustituye por **multidifusión** al grupo de todos los nodos del enlace, **`ff02::1`**; el prefijo de toda la multidifusión IPv6 es **`ff00::/8`**. Y añade la **anydifusión**. **Protocolos de suscripción a grupos**: **IGMP** en IPv4 \[RFC1112\] y **MLD** en IPv6.

**Para qué sirve la difusión.** No es un residuo: es **imprescindible** para el funcionamiento de la red, porque resuelve el problema del arranque —cómo hablar con alguien de quien aún no se sabe nada—. Usos legítimos e ineludibles:

- **ARP** \[RFC826\]: para averiguar la MAC que corresponde a una IP, se pregunta **a todos**, porque no se sabe quién la tiene.
- **DHCP**: un equipo que arranca sin dirección IP no puede dirigirse a nadie en concreto; envía su petición **a la difusión** y espera respuesta.
- **Descubrimiento de servicios**: impresoras, pantallas, sistemas de anuncio de servicios en red.
- **Protocolos de encaminamiento y de red** que anuncian su presencia a los vecinos.

**El problema: la tormenta de difusión.** Como toda estación recibe **y procesa** cada trama de difusión —la procesa la CPU, no solo la tarjeta—, un exceso de difusión degrada a **todos** los equipos del dominio a la vez. En su forma extrema, la **tormenta de difusión** satura el dominio hasta dejarlo inutilizable.

> **Dato clave.** La causa más grave de tormenta de difusión es un **bucle de nivel 2**: dos conmutadores unidos por dos caminos. Una única trama de difusión da vueltas indefinidamente y se **multiplica** en cada nodo, y no hay nada que la detenga **porque la trama Ethernet no tiene campo TTL**, a diferencia del paquete IP. En cuestión de segundos la red cae por completo. Los tres remedios, en orden: (1) **STP/RSTP** \[IEEE802.1\], que bloquea lógicamente los enlaces redundantes y los reactiva si falla el principal; (2) **VLAN**, que acotan el tamaño del dominio de difusión y por tanto el alcance del desastre; (3) **control de tormentas** en el conmutador, que limita el porcentaje de tráfico de difusión admitido por puerto.

**Multidifusión: el término medio.** La multidifusión resuelve el problema de enviar el mismo contenido a **muchos pero no a todos**, sin replicarlo tantas veces como destinatarios. El emisor envía **una sola copia**, y la red la **replica solo donde hace falta**, en los puntos de bifurcación del árbol de distribución. Sus aplicaciones típicas: **difusión de vídeo (IPTV)**, **actualización simultánea** de imágenes de sistema a cientos de puestos, **audioconferencia**, distribución de cotizaciones. En redes locales los conmutadores implementan **vigilancia de IGMP (*IGMP snooping*)** para no inundar la multidifusión por todos los puertos, sino solo por aquellos donde hay suscriptores.

**Las redes de difusión en sentido estricto: la radiodifusión.** El término «red de difusión» tiene además su acepción tradicional, la de los **servicios de comunicación audiovisual**: radio y televisión. Su modelo es **símplex puro** y **uno a todos** sin retorno: un centro emisor y un número indeterminado de receptores pasivos, sin canal de vuelta y sin conocimiento de quién recibe.

> **Dato clave.** En la **televisión digital terrestre**, la unidad de transmisión es el **múltiple digital o múltiplex**: *«la señal compuesta transmitida en una frecuencia radioeléctrica determinada que, mediante tecnología digital, permite la incorporación de las señales correspondientes a varios servicios de comunicación audiovisual y de varios servicios de televisión conectada y de comunicaciones electrónicas»* \[L13-2022\]. Es decir, **un múltiplex es un canal radioeléctrico que transporta varios canales de televisión** mediante multiplexación digital: esa es exactamente la ganancia del paso de analógico a digital, y la razón de que se pudiera liberar espectro (el **dividendo digital**, §8.2).

> **Ejemplo de aplicación en el ayto.** El sistema de **gestión de turnos** de la Oficina de Atención a la Ciudadanía usa los tres modos a la vez, y es un buen ejercicio de identificación. Cuando el equipo del mostrador arranca y pide dirección al servidor DHCP, usa **difusión**, porque aún no tiene identidad ni sabe a quién preguntar. Cuando el servidor de turnos envía el número que toca a las **cuatro pantallas** de la sala de espera, lo hace por **multidifusión**: una sola copia por la red, replicada solo hacia los puertos con suscriptores. Y cuando el empleado consulta el expediente del ciudadano que acaba de sentarse, la sesión con el servidor del CPD es **unidifusión**. Un mismo servicio, tres modos de entrega, elegido cada uno por su naturaleza.

------------------------------------------------------------------------

### 7. Redes e infraestructuras inalámbricas

Las redes inalámbricas replican la escala de cobertura de §5.1 anteponiendo la inicial `W` de *wireless*. Es una clasificación paralela, no un nivel adicional. Ver **diagrama D15**.

| Categoría | Alcance | Tecnologías características |
|----|----|----|
| **WPAN** | Metros | **Bluetooth**, **NFC**, **Zigbee**, Thread, UWB |
| **WLAN** | Decenas o cientos de metros | **Wi-Fi** \[IEEE802.11\] |
| **WMAN** | Kilómetros | **WiMAX** \[IEEE802.16\], radioenlaces urbanos |
| **WWAN** | Regional o global | **Redes celulares** (2G a 5G), **satélite**, **LPWAN** |

Todas comparten cuatro rasgos derivados de usar un medio **no guiado y compartido**, y cada uno tiene consecuencias:

1.  **El medio es compartido y semidúplex** (§3.1): la capacidad anunciada se reparte y el caudal real es muy inferior al nominal.
2.  **La cobertura es un volumen, no una línea**: no termina en la pared, lo que crea un problema de seguridad estructural (§9.1) y otro de interferencia con los vecinos.
3.  **La calidad es variable en el tiempo y en el espacio**: atenuación por obstáculos, propagación multitrayecto, desvanecimientos y contienda con otros emisores.
4.  **El espectro está regulado**: solo las bandas de **uso común** (ISM) permiten desplegar sin título habilitante, y aun así con límites de potencia (§9.2).

#### 7.1. Redes de área personal y local inalámbricas

**A. Wi-Fi — la WLAN \[IEEE802.11\].**

**Elementos y modos de operación.** La arquitectura de 802.11 se construye sobre cuatro conceptos que hay que nombrar con precisión:

- **BSS** (*Basic Service Set*): una **celda**, formada por un **punto de acceso** y los clientes asociados a él. Se identifica por el **BSSID**, que es normalmente la **MAC de la radio** del punto de acceso.
- **ESS** (*Extended Service Set*): **varias celdas** con el **mismo SSID** conectadas por una red de distribución cableada, entre las que el cliente se desplaza con **itinerancia**. Es la arquitectura de cualquier despliegue de edificio.
- **SSID** (*Service Set Identifier*): el **nombre** de la red, de hasta 32 caracteres, que el punto de acceso anuncia en tramas de **baliza** periódicas.
- **IBSS** o modo ***ad hoc***: los clientes se comunican **entre sí sin punto de acceso**. Uso residual.

**Acceso al medio: CSMA/CA.** Wi-Fi no puede usar CSMA/CD —detección de colisión— por una razón física ya vista en §3.1: **una radio que transmite no puede escuchar** su propia frecuencia, así que **es incapaz de detectar la colisión mientras se produce**. Por eso usa **CSMA/CA**, acceso múltiple por detección de portadora con **evitación** de colisiones: antes de transmitir escucha, y si el medio está libre espera un tiempo aleatorio (*backoff*) para reducir la probabilidad de que dos estaciones arranquen a la vez; y cada trama recibida correctamente se **confirma con un ACK**, cuya ausencia se interpreta como colisión. Opcionalmente usa el intercambio **RTS/CTS** para resolver el **problema del nodo oculto** —dos clientes que se oyen con el punto de acceso pero no entre sí—. *El desarrollo de los métodos de acceso al medio corresponde al **Tema 37**.*

**Bandas y canales.** Wi-Fi opera en tres bandas de **uso común**:

| Banda | Anchura útil en Europa | Canales sin solape | Características |
|----|----|----|----|
| **2,4 GHz** | 2,400-2,4835 GHz | **3** (1, 6 y 11 con canales de 20 MHz) | **Mayor alcance y penetración**, pero muy congestionada: la comparten Bluetooth, microondas domésticos y mandos |
| **5 GHz** | Varios subbloques entre 5,15 y 5,725 GHz | **Muchos** (19 o más de 20 MHz) | Más capacidad y menos interferencia; **menor alcance**; algunos subbloques exigen **DFS** y control de potencia por compartirse con radares |
| **6 GHz** | 5,925-6,425 GHz en la UE | Muchos | **Wi-Fi 6E y Wi-Fi 7**: espectro limpio, canales muy anchos, alcance corto |

> **Dato clave.** En **2,4 GHz solo hay tres canales que no se solapan** —**1, 6 y 11**— porque cada canal ocupa 20 MHz y están separados solo 5 MHz. Es el dato que explica la mayor parte de los problemas de rendimiento del Wi-Fi doméstico y el criterio básico de planificación de canales en un despliegue profesional: celdas adyacentes **nunca** en el mismo canal.

**Las generaciones.** La Wi-Fi Alliance introdujo la numeración comercial para hacer legible la nomenclatura del IEEE \[WIFI-ALLIANCE\]. La tabla es de memorización directa:

| Generación | Norma IEEE | Año | Bandas | Velocidad máxima teórica | Novedad principal |
|----|----|----|----|----|----|
| — | **802.11** | 1997 | 2,4 GHz | 2 Mbit/s | La norma original |
| — | **802.11b** | 1999 | 2,4 GHz | 11 Mbit/s | Primera de uso masivo |
| — | **802.11a** | 1999 | 5 GHz | 54 Mbit/s | **OFDM** en 5 GHz |
| — | **802.11g** | 2003 | 2,4 GHz | 54 Mbit/s | OFDM en 2,4 GHz, compatible con b |
| **Wi-Fi 4** | **802.11n** | 2009 | 2,4 y 5 GHz | 600 Mbit/s | **MIMO**, canales de 40 MHz |
| **Wi-Fi 5** | **802.11ac** | 2013 | **5 GHz** | ~6,9 Gbit/s | Canales de **80 y 160 MHz**, 256-QAM, MU-MIMO descendente |
| **Wi-Fi 6** | **802.11ax** | 2021 | 2,4 y 5 GHz | ~9,6 Gbit/s | **OFDMA**, MU-MIMO en ambos sentidos, **1024-QAM**, **TWT** (ahorro de energía), **BSS coloring** |
| **Wi-Fi 6E** | 802.11ax | 2021 | **+ 6 GHz** | ~9,6 Gbit/s | Extensión de Wi-Fi 6 a la banda de **6 GHz** |
| **Wi-Fi 7** | **802.11be** | **2025** | 2,4, 5 y 6 GHz | ~46 Gbit/s | Canales de **320 MHz**, **4096-QAM**, **operación multienlace (MLO)** |
| **Wi-Fi 8** | **802.11bn** | ~**2028** | 2,4, 5 y 6 GHz | En definición | **Ultra alta fiabilidad**: estabilidad en el borde de cobertura y latencia acotada |

> **Dato clave.** Cuatro datos precisos sobre las generaciones recientes: **(1)** **IEEE 802.11be (Wi-Fi 7) se publicó el 22 de julio de 2025** \[IEEE802.11\]; es el estándar maduro del ciclo actual. **(2)** Su rasgo distintivo no es la velocidad, sino la **operación multienlace (MLO)**: un mismo cliente usa **varias bandas simultáneamente** —2,4, 5 y 6 GHz— agregando capacidad y, sobre todo, ganando **fiabilidad**, porque si una banda se degrada el tráfico sigue por las otras. **(3)** **4096-QAM** significa `log₂(4096) = `**`12 bits por símbolo`**, frente a los 10 de Wi-Fi 6 (§1.2). **(4)** **Wi-Fi 8 (802.11bn, *Ultra High Reliability*)** está en desarrollo desde noviembre de 2023 y **su publicación se prevé en 2028**; los equipos «preestándar» exhibidos en 2026 **no** son equipos certificados. Cambia el objetivo del estándar: ya no persigue el pico de velocidad en condiciones ideales, sino el **rendimiento fiable en condiciones malas**.

**Otras enmiendas de 802.11 que conviene ubicar**: **802.11i** (seguridad, base de WPA2), **802.11e** (calidad de servicio, base de WMM), **802.11r** (**itinerancia rápida**, esencial para que una llamada de voz sobre wifi no se corte al cambiar de celda), **802.11k** y **802.11v** (información de radio y gestión de la itinerancia asistida) y **802.11s** (redes **malladas**).

**B. Bluetooth — la WPAN por excelencia \[BT-CORE\].**

Trabaja en la banda **ISM de 2,4 GHz** con **salto en frecuencia adaptativo (AFH)**, que le permite convivir con el Wi-Fi esquivando los canales ocupados. Su topología es la **piconet**: un dispositivo **maestro** y hasta **siete esclavos activos** (más otros en estado aparcado); varias piconets enlazadas forman una **scatternet**.

Existen dos familias tecnológicas que comparten marca pero no radio:

- **BR/EDR** (*Basic Rate / Enhanced Data Rate*), el Bluetooth «clásico»: pensado para flujos continuos, como el audio de unos auriculares.
- **Bluetooth LE** (*Low Energy*), introducido en la versión 4.0: pensado para **enviar poco y dormir mucho**, con consumos que permiten años de pila. Es la base de las **radiobalizas (*beacons*)**, los sensores, los relojes y las pulseras.

Las **clases de potencia** determinan el alcance nominal: **clase 1** ≈ 100 m, **clase 2** ≈ 10 m (la más común, la de los auriculares y el móvil) y **clase 3** ≈ 1 m.

Novedades recientes de las que conviene tener la referencia: desde **5.2**, **LE Audio** con el códec **LC3** y la difusión **Auracast**; desde **6.0**, ***Channel Sounding***, que mide la distancia entre dos dispositivos por fase y tiempo de ida y vuelta con precisión centimétrica, lo que abre la puerta a la localización en interiores y a las llaves digitales seguras. La versión vigente del núcleo en agosto de 2026 es la **6.3**, publicada el 6 de mayo de 2026.

**C. Otras redes de área personal.**

| Tecnología | Norma | Frecuencia | Alcance | Rasgo distintivo |
|----|----|----|----|----|
| **NFC** | \[ISO-NFC\] | **13,56 MHz** | **≈ 10 cm** | Comunicación por **acoplamiento inductivo**; el lector puede **alimentar** a la etiqueta pasiva; tres modos: lectura/escritura, emulación de tarjeta y punto a punto |
| **RFID** | ISO 18000 | 125 kHz, 13,56 MHz, 860-960 MHz | cm a metros | Identificación por radiofrecuencia; etiquetas **pasivas** (sin batería), semipasivas y **activas** |
| **Zigbee** | \[IEEE802.15\].4 | 2,4 GHz y 868 MHz | Decenas de m, ampliables en **malla** | Muy bajo consumo, **topología en malla** autoorganizada; domótica y control de edificios |
| **Thread / 6LoWPAN** | \[IEEE802.15\].4 | 2,4 GHz | Malla | Como Zigbee pero **con IPv6 nativo** |
| **UWB** (banda ultraancha) | 802.15.4z | 3,1-10,6 GHz | Decenas de m | **Localización de precisión** (centímetros) por tiempo de vuelo |

> **Dato clave.** **NFC: 13,56 MHz y ~10 cm de alcance.** Los dos datos van juntos, y el alcance corto **es la característica de seguridad**, no una limitación: obliga a una aproximación deliberada y hace impracticable la interceptación a distancia. NFC es un subconjunto de RFID de alta frecuencia con capacidad **bidireccional**, mientras que el RFID clásico es unidireccional de etiqueta a lector.

#### 7.2. Redes de área metropolitana y extensa inalámbricas

**A. WMAN: WiMAX y los radioenlaces urbanos.**

**WiMAX** \[IEEE802.16\] fue la apuesta normalizada por la banda ancha inalámbrica de alcance metropolitano: perfil **fijo** (802.16d, 2004) y **móvil** (802.16e, 2005), con alcances de kilómetros y arquitectura de estación base a abonados. En la práctica **perdió la batalla frente a LTE** y hoy su presencia en Europa es **residual**, aunque sigue apareciendo en el temario como categoría de clasificación —es *la* WMAN— y como solución de nicho para llevar conectividad a zonas sin canalización.

Junto a él, la WMAN realmente desplegada en las ciudades es la de **radioenlaces punto a punto y punto a multipunto** en bandas de microondas, usados por operadores y por grandes usuarios (incluidas las Administraciones) para **enlazar sedes** salvando la vía pública, y como **respaldo** de la fibra.

**B. WWAN: satélite.**

El satélite es un **repetidor de microondas** situado en órbita. Su clasificación por altura:

| Órbita | Altura | Periodo | Latencia ida y vuelta | Rasgos |
|----|----|----|----|----|
| **GEO** (geoestacionaria) | **35.786 km** | **24 h** | **≈ 250 ms** o más | Aparece **fijo** en el cielo: la antena no se mueve. **Tres satélites** cubren casi todo el globo. Latencia alta y mala para tiempo real |
| **MEO** (media) | 2.000-35.786 km | Horas | ≈ 100 ms | Órbita de **GPS**, **Galileo** y **GLONASS** |
| **LEO** (baja) | **300-2.000 km** | ≈ 90 min | **≈ 20-50 ms** | Latencia baja, pero cada satélite **cruza el cielo en minutos**: exige **constelaciones** de cientos o miles y antenas con seguimiento |

> **Dato clave.** La **altura de la órbita geoestacionaria es 35.786 km**, y de ahí se deduce todo lo demás: la señal recorre ida y vuelta unos 72.000 km, que a la velocidad de la luz suponen unos **240-250 ms**, y eso **antes** de procesar nada. Por eso el satélite GEO es excelente para **difusión de televisión** —que tolera cualquier retardo— y malo para videoconferencia o control en tiempo real, y por eso las constelaciones **LEO** han cambiado el panorama del acceso por satélite. Bandas de trabajo: **C** (≈ 4/6 GHz, robusta frente a la lluvia), **Ku** (≈ 12/14 GHz, la de la televisión doméstica) y **Ka** (≈ 20/30 GHz, más capacidad y más sensible a la lluvia).

**C. WWAN: redes de baja potencia y área extensa (LPWAN).**

Familia pensada para el **internet de las cosas**: dispositivos que envían **muy pocos datos, muy de vez en cuando, a mucha distancia y con años de batería**. Renuncian por completo al caudal para ganar alcance y autonomía.

| Tecnología | Espectro | Alcance | Rasgo distintivo |
|----|----|----|----|
| **LoRaWAN** \[LORA\] | **Sin licencia** (868 MHz en Europa) | Kilómetros; decenas en campo abierto | Red propia desplegable por el usuario; clases A, B y C de dispositivo; arquitectura de estrella de estrellas con pasarelas |
| **Sigfox** | Sin licencia | Kilómetros | Mensajes ultracortos, operador único |
| **NB-IoT** | **Licenciado** (3GPP) | Cobertura del operador móvil | Usa la red celular; excelente penetración en sótanos y arquetas |
| **LTE-M** | Licenciado (3GPP) | Cobertura del operador | Más caudal que NB-IoT y admite **movilidad** y voz |

> **Dato clave.** La distinción decisiva dentro de LPWAN es **espectro sin licencia frente a espectro licenciado**. **LoRaWAN y Sigfox** operan en bandas de **uso común**, de modo que una Administración puede **desplegar su propia red** sin depender de un operador ni pagar por dispositivo, pero sin garantía de calidad ni de ausencia de interferencias. **NB-IoT y LTE-M** son tecnologías **3GPP** sobre espectro **licenciado**: hay calidad y cobertura garantizadas por contrato, pero el servicio es del operador. Es exactamente la disyuntiva que se plantea en cualquier proyecto municipal de sensórica urbana.

> **Ejemplo de aplicación en el ayto.** El edificio del distrito acaba concentrando **cinco** tecnologías inalámbricas distintas, cada una en su escala: **Wi-Fi 6** para los puestos móviles y las tabletas de los inspectores (**WLAN**); **Bluetooth LE** en los auriculares del personal de atención telefónica y en las balizas de accesibilidad de la entrada (**WPAN**); **NFC** en los lectores de la tarjeta de empleado del control de presencia (**WPAN**); un **radioenlace de microondas** como respaldo del enlace de fibra con el CPD (**WMAN**); y **NB-IoT** en los sensores de ocupación y de calidad del aire, precisamente porque están en el sótano y en el patio, donde el Wi-Fi no llega y donde la penetración de la red celular sí (**WWAN**). Elegir bien es elegir la escala correcta, no la tecnología más rápida.

------------------------------------------------------------------------

### 8. Comunicaciones móviles

Las **comunicaciones móviles** son las que permiten mantener la comunicación **mientras el terminal se desplaza**, incluso entre zonas de cobertura distintas. Esa capacidad —y no la ausencia de cable— es lo que las define: un portátil conectado por Wi-Fi es inalámbrico, pero no móvil en este sentido, porque al salir del edificio pierde la sesión.

#### 8.1. Evolución y arquitectura de redes celulares móviles

**El principio celular.** El problema que resuelve es de escasez: el espectro asignado a un operador es finito, y si una sola antena diera servicio a toda una ciudad, el número de comunicaciones simultáneas sería ridículo. La solución, formulada en los laboratorios Bell en los años cuarenta y hecha viable en los setenta, consiste en dividir el territorio en **celdas** pequeñas, cada una con su estación base y una **parte** del espectro total, de modo que celdas **no adyacentes puedan reutilizar las mismas frecuencias** sin interferirse. Ver **diagrama D16**.

Los conceptos asociados son de memorización obligatoria:

- **Celda**: zona de cobertura de una estación base. Se representa como un **hexágono** porque es el polígono regular que tesela el plano aproximándose mejor al círculo.
- **Reutilización de frecuencias**: repetir el mismo conjunto de canales en celdas suficientemente separadas. El **patrón de reutilización** (típicamente de 3, 4, 7 o 12 celdas) fija a cuántas celdas de distancia se repite.
- **División celular (*cell splitting*)**: cuando una celda se satura, se sustituye por varias celdas más pequeñas con menos potencia. **Reducir el tamaño de la celda es la forma canónica de aumentar la capacidad total del sistema**, y es exactamente lo que hacen las **microceldas**, **picoceldas** y **femtoceldas** urbanas.
- **Traspaso (*handover* o *handoff*)**: transferencia de una comunicación en curso de una celda a otra sin interrumpirla, al detectarse que la señal de la celda vecina es mejor.
- **Itinerancia (*roaming*)**: capacidad de un abonado de usar la red de **otro operador**, típicamente en otro país, en virtud de un acuerdo. En la Unión Europea está regulada: rige el principio de **«itinerancia como en casa»** \[REG2015-2120\].

> **Dato clave.** **Traspaso e itinerancia no son lo mismo.** El **traspaso** ocurre **dentro** de la red del operador y **durante** una comunicación en curso, y su función es la **continuidad**. La **itinerancia** ocurre **entre redes de operadores distintos** y su función es la **cobertura** fuera de la propia red; no exige que haya comunicación en curso. Es un par de conceptos que se intercambian como distractores con mucha frecuencia.

**Arquitectura general.** Toda red celular, de cualquier generación, se organiza en tres bloques:

1.  **Equipo de usuario**: el terminal más su **módulo de identidad de abonado (SIM o eSIM)**, que es lo que separa la identidad del abonado del aparato. Es una de las grandes aportaciones del GSM.
2.  **Red de acceso radio**: las **estaciones base** (BTS en GSM, NodeB en UMTS, eNodeB en LTE, gNodeB en 5G) y sus controladores, que gestionan el enlace radio, la asignación de recursos y los traspasos.
3.  **Red troncal o núcleo (*core*)**: la inteligencia del sistema. Gestiona el registro y la autenticación de los abonados, la localización, el establecimiento de las comunicaciones, la interconexión con otras redes y la **facturación**. En GSM incluye el **HLR** (registro de abonados propios) y el **VLR** (registro de los visitantes en cada zona); en 5G es una arquitectura **basada en servicios**.

#### 8.2. Tecnologías consolidadas y de alta capacidad

**La evolución generación a generación.** Ver **diagrama D16**. La tabla siguiente es el núcleo memorizable de la sección:

| Gen. | Tecnología | Época | Conmutación | Hitos |
|----|----|----|----|----|
| **1G** | **TACS**, AMPS, NMT | 1980s | Circuitos, **analógica** | Solo voz, sin cifrado, terminales enormes |
| **2G** | **GSM** | 1990s | Circuitos, **digital** | **SMS**, **tarjeta SIM**, cifrado del enlace radio, itinerancia internacional |
| **2.5G** | **GPRS** | 2000 | **+ paquetes** | Primer acceso a datos permanente; facturación por volumen, no por tiempo |
| **2.75G** | **EDGE** | 2003 | Paquetes | Mejora la modulación de GPRS |
| **3G** | **UMTS** (WCDMA) | 2001-2004 | Circuitos + paquetes | **IMT-2000**; videollamada; **CDMA** de banda ancha |
| **3.5G** | **HSPA / HSPA+** | 2006-2010 | Paquetes | Megabits reales; despegue de la internet móvil |
| **4G** | **LTE / LTE-Advanced** | 2010-2013 | **Solo paquetes** | **Todo IP**; la voz pasa a ser un servicio más (**VoLTE**); **OFDMA** y **MIMO**; agregación de portadoras |
| **5G** | **5G NR** | 2019- | Solo paquetes | **IMT-2020**: eMBB, URLLC, mMTC; MIMO masivo, haces, **fraccionamiento de red** |

> **Dato clave.** Los cuatro saltos conceptuales, que valen más que las fechas: **(1) De 1G a 2G**: de **analógico a digital**. Con ello llegan el cifrado, el SMS y la **SIM**. **(2) De 2G a 2.5G (GPRS)**: de **circuitos a paquetes** para los datos, con la consecuencia económica de que se factura por **volumen** y la técnica de que la conexión está **siempre disponible**. **(3) De 3G a 4G (LTE)**: desaparece por completo la conmutación de **circuitos**; la red es **todo IP** y la voz se transporta como datos (**VoLTE**). Es el salto arquitectónico más profundo de la serie. **(4) De 4G a 5G**: de una red que servía a personas a una red que sirve **a tres tipos de cliente distintos a la vez** —personas, máquinas críticas y máquinas masivas— sobre la misma infraestructura.

**5G en detalle.** El marco **IMT-2020** de la UIT define **tres familias de casos de uso** \[UIT-IMT\], que hay que saber enumerar y distinguir:

| Familia | Nombre completo | Qué optimiza | Objetivo de referencia | Ejemplos |
|----|----|----|----|----|
| **eMBB** | Banda ancha móvil mejorada | **Caudal** | **20 Gbit/s** de pico descendente | Vídeo en alta definición, realidad aumentada, acceso fijo inalámbrico |
| **URLLC** | Comunicaciones ultrafiables de baja latencia | **Latencia y fiabilidad** | **1 ms** en la interfaz radio | Conducción conectada, cirugía remota, automatización industrial, telemando de red eléctrica |
| **mMTC** | Comunicaciones masivas entre máquinas | **Densidad de dispositivos** | **10⁶ dispositivos/km²** | Sensórica urbana, contadores, ciudad inteligente |

Sus habilitadores tecnológicos:

- **MIMO masivo**: decenas o cientos de elementos radiantes en la estación base, que multiplican la capacidad reutilizando el espacio.
- **Conformación de haz (*beamforming*)**: en lugar de radiar en todas direcciones, la estación **apunta** un haz al terminal, ganando alcance y reduciendo interferencia.
- **Fraccionamiento de red (*network slicing*)**: sobre una misma infraestructura física se definen **redes lógicas independientes**, cada una con sus garantías de latencia, caudal y aislamiento. Es lo que permite que una red comercial dé servicio a la vez a los abonados y a un servicio de emergencias con calidad garantizada.
- **Computación en el borde (*edge computing*, MEC)**: se acerca la capacidad de proceso a la estación base para no pagar el retardo de ir hasta el centro de datos. Sin ella, el objetivo de 1 ms es inalcanzable. Ver **Tema 31**.
- **Modos de despliegue**: **NSA** (*Non-Standalone*), donde la radio 5G se apoya en el **núcleo 4G** —es como arrancaron casi todas las redes— y **SA** (*Standalone*), con **núcleo 5G propio**, que es el único que habilita realmente el fraccionamiento de red y la URLLC \[3GPP\].

> **Dato clave.** **Sin núcleo 5G autónomo (SA) no hay ni *network slicing* ni URLLC reales.** Un despliegue **NSA** ofrece más velocidad —es decir, solo eMBB—, pero conserva la arquitectura del núcleo 4G. Es la distinción que separa el «5G comercial» del «5G que transforma servicios», y la que hay que citar cuando una pregunta plantee para qué sirve el 5G en un servicio público.

**El espectro del 5G en España.** Tres bandas prioritarias, cada una con una función distinta que se deduce de la regla de oro de §2.2.1:

| Banda | Función | Situación en España |
|----|----|----|
| **700 MHz** (694-790 MHz) | **Cobertura**: gran alcance y penetración en interiores y zonas rurales | Liberada por el **segundo dividendo digital**: **RD 391/2019**, con migración de la TDT a completar antes del **31 de octubre de 2020** \[RD391-2019\] |
| **3,5 GHz** (banda central) | **Equilibrio** entre cobertura y capacidad. Es la banda de referencia del 5G europeo | Asignada a los operadores; el grueso del despliegue actual |
| **26 GHz** (ondas milimétricas) | **Capacidad** en puntos calientes y usos industriales; alcance de decenas o centenares de metros | Subastada en **2022**: 12 concesiones de ámbito estatal y 38 de ámbito autonómico, por **20 años prorrogables** |

> **Dato clave.** El **dividendo digital** es el espectro que se libera al pasar la televisión de analógica a digital, gracias a que la multiplexación digital permite meter **varios canales en un múltiplex** (§6.2.1). Hubo **dos**: el primero liberó la banda de **800 MHz** (para 4G) y el segundo, la de **700 MHz** (para 5G). Dato complementario del **RD 391/2019**: la banda **470-694 MHz** queda garantizada para la **TDT al menos hasta 2030**. Es la cifra que cierra el tema de la difusión terrestre.

**Hacia el 6G.** La UIT trabaja en el marco **IMT-2030**, con horizonte de despliegue en torno a **2030**. Las líneas de investigación —comunicación y detección integradas, inteligencia artificial nativa en la red, bandas de terahercios, integración con constelaciones no terrestres— aún **no son normativa** y en un examen deben citarse como prospectiva, no como hecho.

> **Ejemplo de aplicación en el ayto.** El 5G aparece en un servicio municipal en las tres familias de uso, y conviene saber identificarlas. **eMBB**: una unidad móvil de atención ciudadana desplegada en la calle usa la red 5G comercial como si fuera fibra, con acceso fijo inalámbrico. **URLLC**: la regulación semafórica adaptativa y el telemando de instalaciones exigen latencia acotada y fiabilidad —y por eso solo se puede prometer sobre despliegue **SA** con fraccionamiento de red, no sobre NSA—. **mMTC**: los miles de sensores de ocupación de aparcamiento, contenedores y calidad del aire de la ciudad, que envían unos pocos bytes al día y deben durar años con una pila. Tres exigencias incompatibles entre sí que, antes del 5G, requerían tres redes distintas.

> **Relación con otros temas.** El sistema **TETRA**, la red de radio troncal digital que usan los servicios de emergencia y la Policía Municipal, es el objeto íntegro del **Tema 38**. Aquí basta con situarlo: es una red **celular** de radio profesional, **semidúplex** con pulsar para hablar (§3.1), optimizada para **comunicación de grupo**, establecimiento de llamada en **menos de medio segundo**, prioridades y llamada de emergencia, y con **modo directo** entre terminales sin infraestructura. Es decir: renuncia deliberadamente al caudal para ganar en **disponibilidad y en tiempo de establecimiento**, que es lo que una emergencia necesita.

------------------------------------------------------------------------

### 9. Seguridad y normativa en la Administración Pública

> **Material complementario.** El enunciado oficial de este tema no nombra este apartado. Se mantiene porque sitúa la materia en el Ayuntamiento y en la normativa que le aplica, pero lo exigible es lo que enumera el título del tema.

Esta sección cierra el tema con las dos preguntas que un técnico municipal tiene que saber contestar sobre cualquier comunicación: **¿es segura?** y **¿es legal?**. La primera se responde con el ENS y con la técnica del enlace radio; la segunda, con la Ley General de Telecomunicaciones.

#### 9.1. Aspectos de seguridad e integridad en redes inalámbricas

**El problema de raíz.** Una red cableada tiene una frontera física: para pincharla hay que **entrar en el edificio** y acceder a un cable. Una red inalámbrica **no tiene esa frontera**: la señal atraviesa paredes y sale a la calle, y cualquiera con una antena puede **escuchar todo el tráfico sin dejar rastro alguno**. De ahí se derivan los dos principios que gobiernan toda la seguridad inalámbrica:

1.  **En radio hay que suponer siempre que alguien escucha.** La única protección real es el **cifrado del enlace**, no la ocultación.
2.  **Hay que autenticar al que entra**, y hacerlo de forma que se pueda **imputar** la actividad a una persona concreta —lo que descarta las claves compartidas en entornos profesionales—.

**Ataques característicos:**

| Ataque | En qué consiste |
|----|----|
| **Escucha pasiva** (*eavesdropping*) | Captura del tráfico sin interactuar. **Indetectable**, porque el atacante no emite |
| **Punto de acceso no autorizado** (*rogue AP*) | Alguien conecta un punto de acceso propio a la red corporativa, abriendo una puerta trasera que salta todo el perímetro |
| **Gemelo malvado** (*evil twin*) | Un punto de acceso falso que **suplanta el SSID** legítimo para que los clientes se asocien a él y capturar sus credenciales |
| **Desautenticación** (*deauth*) | Envío de tramas de gestión falsificadas que **expulsan** a los clientes; sirve para forzar la reconexión al gemelo malvado o como denegación de servicio |
| **Interposición** (*man in the middle*) | El atacante se sitúa entre cliente y punto de acceso y ve o altera todo el tráfico |
| **Ataque de diccionario contra la clave precompartida** | Captura del saludo de cuatro vías y prueba de claves **fuera de línea**, sin límite de intentos |
| **Interferencia deliberada** (*jamming*) | Saturación de la banda para denegar el servicio. Muy difícil de evitar, fácil de localizar |
| **Suplantación de MAC** | Clonado de una dirección MAC autorizada; hace **inútil** el filtrado por MAC |

**La evolución de los protocolos de seguridad.** Ver **diagrama D17**:

| Protocolo | Año | Cifrado | Autenticación | Estado |
|----|----|----|----|----|
| **WEP** (*Wired Equivalent Privacy*) | 1999 | **RC4** con vector de inicialización de 24 bits | Clave compartida | **ROTO**. Se descifra en minutos. **Prohibido su uso** |
| **WPA** | 2003 | **TKIP** (sigue usando RC4, con claves por paquete) | PSK o 802.1X | **Obsoleto**. Fue una solución transitoria sobre el hardware de WEP |
| **WPA2** | 2004, \[IEEE802.11\].i | **AES-CCMP** | PSK o **802.1X/EAP** | Aún vigente y muy extendido, pero vulnerable a KRACK y a diccionario sobre PSK |
| **WPA3** | 2018 | **AES**; **GCMP-256** en modo Enterprise de **192 bits** | **SAE** en personal; 802.1X en Enterprise | **El recomendado**. Añade **PFS** y protección de tramas de gestión |

Las tres aportaciones de **WPA3** que hay que saber nombrar:

- **SAE** (*Simultaneous Authentication of Equals*, o «libélula»): sustituye al saludo de cuatro vías del PSK por un intercambio que **impide el ataque de diccionario fuera de línea**, aunque la contraseña sea débil, y proporciona **confidencialidad directa** (*forward secrecy*): capturar el tráfico hoy y descubrir la clave mañana ya no permite descifrarlo.
- **Modo Enterprise de 192 bits**, alineado con las suites criptográficas de alta seguridad, pensado para Administración y sectores críticos.
- **OWE** (*Opportunistic Wireless Encryption*, comercialmente **Wi-Fi Enhanced Open**): cifra el enlace **en redes abiertas sin contraseña**. Resuelve el escándalo silencioso de la wifi de cortesía, en la que hasta ahora todo el tráfico viajaba en claro.

**Medidas ineficaces que hay que saber descartar.** Son las que **no** aportan seguridad real:

> **Dato clave.** **Ocultar el SSID** (desactivar la baliza) **no es una medida de seguridad**: el nombre de la red sigue viajando en claro en las tramas de asociación de cualquier cliente que se conecte, y basta esperar. **Filtrar por dirección MAC** tampoco lo es: las MAC circulan en claro en todas las tramas y **se clonan trivialmente**. Ambas son **medidas cosméticas** que además complican la operación —y que dan una falsa sensación de protección, que es lo peor de todo—. Lo único que protege es el **cifrado robusto** y la **autenticación por usuario**.

**El modelo empresarial: 802.1X + EAP + RADIUS.** Es el que corresponde a cualquier red municipal, y funciona con tres actores \[IEEE802.1\]:

- El **suplicante**: el cliente que quiere entrar.
- El **autenticador**: el punto de acceso o el conmutador, que mantiene el puerto **cerrado** a todo lo que no sea tráfico de autenticación hasta que se resuelva.
- El **servidor de autenticación**: un **RADIUS** que valida las credenciales contra el directorio corporativo.

Sus ventajas frente a la clave precompartida son decisivas y hay que poder enunciarlas: **credenciales individuales** —y por tanto **trazabilidad** por persona, exigible en el ENS—, **revocación** de un solo usuario sin cambiar la clave a todo el mundo, **asignación dinámica de VLAN** según el perfil de quien se conecta, y posibilidad de exigir **certificado de dispositivo** además de credenciales de usuario (EAP-TLS).

**Buenas prácticas de despliegue.** Cierre operativo de la sección:

1.  **Segmentar**: cada red inalámbrica en su propia VLAN, y separar de raíz la **corporativa**, la de **invitados** y la de **dispositivos de internet de las cosas**.
2.  **Aislar clientes** en la red de invitados, de modo que los dispositivos conectados **no se vean entre sí**.
3.  **Portal cautivo** con condiciones de uso e información de tratamiento de datos en la wifi pública.
4.  **Actualizar** el firmware de los puntos de acceso y del controlador: son equipos expuestos y con vulnerabilidades publicadas.
5.  **Desactivar WPS**, cuyo PIN es atacable por fuerza bruta.
6.  **Planificar** canales y potencias: emitir con más potencia de la necesaria amplía la superficie de exposición sin mejorar el servicio dentro.
7.  **Detectar puntos de acceso no autorizados** de forma continua desde el controlador.
8.  **Proteger las tramas de gestión** (802.11w), lo que neutraliza los ataques de desautenticación.
9.  **No confiar en el enlace radio como única capa**: los servicios sensibles deben ir además sobre **TLS** o **VPN**, con arreglo al principio de **defensa en profundidad**.

**Lo que exige el ENS.** Aquí está el anclaje normativo, verificado contra el texto del BOE:

> **Dato clave.** Medidas del anexo II del ENS que gobiernan las comunicaciones \[ENS\]: **`mp.com.1` — Perímetro seguro** (todas las dimensiones; aplica en las **tres categorías**): *«se dispondrá de un sistema de protección perimetral que separe la red interna del exterior. Todo el tráfico deberá atravesar dicho sistema»*, y *«todos los flujos de información a través del perímetro deben estar autorizados previamente»*. **`mp.com.2` — Protección de la confidencialidad** (dimensión **C**): *«se emplearán redes privadas virtuales cifradas cuando la comunicación discurra por redes fuera del propio dominio de seguridad»*. Nivel BAJO, la medida; **MEDIO, + R1** (algoritmos y parámetros **autorizados por el CCN**); **ALTO, + R1 + R2 + R3** (dispositivos **hardware** y productos certificados). **`mp.com.3` — Protección de la integridad y de la autenticidad** (dimensiones **I** y **A**): nivel BAJO, la medida; **MEDIO, + R1 + R2**; **ALTO, + R1 + R2 + R3 + R4**. **`mp.com.4` — Separación de flujos de información en la red** (todas las dimensiones): **no aplica** en categoría BÁSICA; **MEDIA, + \[R1 o R2 o R3\]**; **ALTA, + \[R2 o R3\] + R4**. Sus dos requisitos base son que *«el tráfico por la red se segregará para que cada equipo solamente tenga acceso a la información que necesita»* y —dato capital para este tema— que ***«si se emplean comunicaciones inalámbricas, será en un segmento separado»***. Sus refuerzos son **R1 segmentación lógica básica por VLAN** —con un mínimo de tres subredes: **usuarios, servicios y administración**—, **R2 segmentación lógica avanzada por VPN**, **R3 segmentación física** y **R4 control en los puntos de interconexión**.

> **Ejemplo de aplicación en el ayto.** Diseño inalámbrico de la Oficina de Atención a la Ciudadanía traducido a medidas del ENS. Se despliegan **tres SSID sobre los mismos puntos de acceso**, cada uno en su VLAN, lo que satisface `mp.com.4.2` y su refuerzo **R1**: (1) **corporativa**, con **WPA3-Enterprise** y **802.1X/EAP-TLS** contra el directorio municipal, de modo que cada actuación es imputable a un empleado concreto —requisito de trazabilidad del ENS—; (2) **dispositivos**, para impresoras, pantallas de turnos y sensores, sin acceso a la red de servicios y con listas de control de acceso estrictas, porque son equipos que no se pueden parchear al ritmo de un puesto de trabajo; (3) **cortesía para el público**, en VLAN totalmente aislada con **salida directa a internet**, sin ninguna ruta hacia la red municipal, con **aislamiento entre clientes**, **OWE** para cifrar aunque sea abierta, **portal cautivo** con las condiciones de uso y la información del art. 13 del RGPD, y limitación de caudal. Y sobre todo ello, el principio que no se puede olvidar: el enlace radio es **una** capa, y los servicios municipales siguen exigiendo **TLS** de extremo a extremo por encima de él.

> **Relación con otros temas.** La **seguridad perimetral**, los **cortafuegos**, los **IDS/IPS**, las **VPN de acceso remoto** y la seguridad del **puesto de usuario** son el objeto del **Tema 36**. Las **técnicas criptográficas** y los **protocolos seguros** —AES, TLS, IPsec— se desarrollan en el **Tema 32**. Los **principios del ENS** en su conjunto, en el **Tema 39**. Aquí se han citado únicamente las medidas `mp.com`, que son las específicas de las comunicaciones, y la seguridad propia del enlace radio, que ningún otro tema cubre.

#### 9.2. Marco normativo y regulatorio de telecomunicaciones en el ámbito público

**La norma de cabecera.** La **Ley 11/2022, de 28 de junio, General de Telecomunicaciones** (BOE núm. 155, de 29 de junio de 2022, en vigor desde el 30 de junio) transpone el **Código Europeo de las Comunicaciones Electrónicas** y sustituye a la Ley 9/2014. Consta de **8 títulos, 114 artículos, 30 disposiciones adicionales, 7 transitorias, 1 derogatoria, 6 finales y 3 anexos** \[LGT\]. Ver **diagrama D18**.

| Título | Materia |
|----|----|
| **I** | Disposiciones generales |
| **II** | Suministro de redes y prestación de servicios: libre competencia, registro de operadores, acceso e interconexión, regulación *ex ante*, numeración |
| **III** | **Obligaciones de servicio público** y derechos y obligaciones de carácter público: servicio universal, derechos de ocupación, secreto de las comunicaciones, seguridad de las redes, derechos de los usuarios |
| **IV** | Equipos de telecomunicación: normalización, evaluación de la conformidad, vigilancia del mercado |
| **V** | **Administración del dominio público radioeléctrico** |
| **VI** | Administración de las telecomunicaciones: competencias del Estado, del Ministerio y de la **CNMC** |
| **VII** | Tasas en materia de telecomunicaciones |
| **VIII** | Inspección y régimen sancionador |

**El principio estructural: liberalización.** El punto de partida del sistema:

> **Dato clave.** *«Las telecomunicaciones son **servicios de interés general** que se prestan en régimen de **libre competencia**»*, y *«**solo tienen la consideración de servicio público** o están sometidos a obligaciones de servicio público los servicios regulados en el artículo 4 y en el título III, respectivamente»* \[LGT, art. 2\]. Y el **art. 4.1** cierra el círculo: *«solo tienen la consideración de servicio público los servicios regulados en este artículo»*, que son los de **seguridad nacional, defensa nacional, seguridad pública, seguridad vial y protección civil**. Traducido: **la telefonía y el acceso a internet NO son servicio público en España** —son servicios de interés general en competencia, sujetos a **obligaciones** de servicio público—.

**El servicio universal (arts. 37 a 42).** Es la principal obligación de servicio público y la garantía de que la liberalización no deja a nadie fuera:

> **Dato clave.** **Servicio universal** es *«el conjunto definido de servicios cuya prestación se garantiza para todos los consumidores con independencia de su localización geográfica, en condiciones de neutralidad tecnológica, con una calidad determinada y a un precio asequible»* \[LGT, art. 37.1\]. Incluye **dos** prestaciones: (a) **acceso adecuado y disponible a una internet de banda ancha** a través de una conexión subyacente **en una ubicación fija**, con **velocidad mínima de 10 Mbit/s en sentido descendente**, escalable **por real decreto a 30 Mbit/s** «tan pronto como sea posible»; y (b) **servicios de comunicaciones vocales** a través de esa misma conexión fija. El **anexo III** enumera los **once** servicios que la conexión debe soportar: correo electrónico, motores de búsqueda, formación y educación en línea, prensa o noticias, compra de bienes y servicios, búsqueda de empleo, redes profesionales, **banca por internet**, **utilización de servicios de administración electrónica**, redes sociales y mensajería, y llamadas y videollamadas de calidad estándar.

Tres precisiones: (1) el servicio universal es de **ubicación fija**: **no** garantiza cobertura móvil; (2) la **asequibilidad** se instrumenta mediante **abonos sociales** para rentas bajas o necesidades sociales especiales, cuya evolución **supervisa la CNMC** \[LGT, art. 38\]; (3) por real decreto puede ampliarse a **microempresas, pymes y organizaciones sin ánimo de lucro** \[LGT, art. 37.3\].

**Las Administraciones públicas como operadoras (art. 13).** Este es el artículo que un técnico municipal debe conocer por encima de los demás, porque delimita lo que el Ayuntamiento puede y no puede hacer con una red:

> **Dato clave.** Cuando una Administración pública —directamente o a través de entidades que controle— **instala y explota redes públicas** o **presta servicios de comunicaciones electrónicas disponibles al público**, debe hacerlo *«dando cumplimiento al **principio de inversor privado**, con la debida **separación de cuentas**, con arreglo a los principios de **neutralidad, transparencia, no distorsión de la competencia y no discriminación**»*, y respetando la normativa de **ayudas de Estado** de los arts. 107 y 108 del Tratado de Funcionamiento de la UE \[LGT, art. 13.2\]. La **excepción** expresa: en la difusión del servicio de **televisión digital en zonas sin cobertura de TDT** *«se considera que se produce una situación de fallo de mercado»*, y por ello esas iniciativas **no se sujetan al principio de inversor privado** ni deben comunicarse al Registro de operadores, salvo que la red se ponga a disposición de terceros o se presten por ella otros servicios.

La clave interpretativa: el artículo regula la actuación de la Administración **como operadora frente al público**. La **red interna** del Ayuntamiento —la que une sus sedes y da servicio a sus empleados— es una **red privada de usuario final** y no queda sujeta a ese régimen. La frontera se cruza cuando esa red **se ofrece a terceros**, aunque sea gratuitamente: ahí es donde una wifi municipal abierta a la ciudadanía puede llegar a plantear la cuestión, y por eso conviene delimitarla como servicio de cortesía accesorio y no como servicio de acceso a internet en competencia.

**El dominio público radioeléctrico (título V).** Su régimen se resume en cuatro datos:

> **Dato clave.** (1) *«El espectro radioeléctrico es un **bien de dominio público**, cuya **titularidad y administración corresponden al Estado**»* \[LGT, art. 85.1\], que la ejerce conforme a los tratados internacionales y a las resoluciones de la **UIT**. (2) Los **títulos habilitantes** para su uso son de tres clases: **autorización general** (uso común, sin necesidad de solicitud individual: es el caso del **Wi-Fi** en bandas ISM), **autorización individual** y **concesión administrativa** (uso privativo con reserva de frecuencia, que es el de los operadores móviles). (3) Las **concesiones** de espectro armonizado para comunicaciones electrónicas tienen una duración **mínima de 20 años**, prorrogable hasta un máximo del orden de **40**. (4) El uso del dominio público radioeléctrico está sujeto a **tasa** por reserva \[LGT, título VII\]. La consecuencia práctica para una Administración: **desplegar Wi-Fi o LoRaWAN no requiere título individual** —bandas de uso común—, mientras que **un radioenlace en banda licenciada sí exige autorización** y devenga tasa.

**Otras obligaciones del título III que afectan a cualquier red.** Aunque su desarrollo corresponde a otros temas, hay que saber que existen y qué artículo las contiene:

| Materia | Artículo | Contenido esencial |
|----|----|----|
| **Secreto de las comunicaciones** | **58** | Garantía del art. 18.3 de la Constitución; la interceptación solo cabe con **autorización judicial** |
| **Interceptación legal** | 59 | Obligación de los operadores de facilitarla a los servicios técnicos habilitados |
| **Protección de datos personales** | 60 | Aplicación del RGPD al tráfico y a la facturación |
| **Conservación y cesión de datos** | 61 | Régimen de conservación de datos de tráfico |
| **Cifrado** | 62 | Se puede utilizar cifrado en redes y servicios como instrumento de seguridad |
| **Integridad y seguridad de las redes** | **63** | Los operadores deben **gestionar los riesgos de seguridad** con medidas técnicas y organizativas proporcionadas y en línea con el estado de la técnica, **pudiendo incluir el cifrado**; garantizar la **integridad** de la red; y **notificar al Ministerio** los incidentes de **impacto significativo**, valorado por **cinco parámetros**: número de usuarios afectados, duración, área geográfica, medida en que se ve afectado el funcionamiento y alcance del impacto económico y social |
| **Derechos de los usuarios** | 64-78 | Transparencia contractual, cambio de operador y conservación del número, acceso a **emergencias (112)**, itinerancia |
| **Infraestructuras comunes en edificios (ICT)** | **55** | Remisión al reglamento de **ICT** \[RD346-2011\]; inventario centralizado de edificios con ICT instalada |

> **Dato clave.** El **art. 63** es el «ENS de los operadores», y conviene compararlo con el ENS: el **ENS** obliga a las **entidades del sector público** respecto de **sus** sistemas; el **art. 63 de la LGT** obliga a los **operadores** respecto de las **redes públicas**. El Ayuntamiento está sujeto al primero por sus sistemas, y **se beneficia** del segundo como cliente de los operadores que le prestan servicio. La cifra memorizable son los **cinco parámetros** de valoración del impacto de un incidente notificable.

**Los reguladores y organismos.** Cuadro final del tema:

| Organismo | Ámbito | Funciones principales |
|----|----|----|
| **UIT** (Unión Internacional de Telecomunicaciones) | **Mundial** (agencia de la ONU) | Atribución internacional del espectro (**CMR**), normalización (recomendaciones **UIT-T** y **UIT-R**), desarrollo |
| **CEPT / ECC** y **RSPG** | **Europeo** | Armonización del espectro en Europa y asesoramiento a la Comisión |
| **ETSI** | Europeo | Normalización técnica europea (**TETRA**, GSM y sus sucesores, firma electrónica) |
| **BEREC** | Europeo | Organismo de reguladores europeos de comunicaciones electrónicas |
| **Ministerio** competente en telecomunicaciones | **Estatal** | Gestión del **dominio público radioeléctrico**, registro de operadores, inspección, recepción de las **notificaciones de incidentes** del art. 63 |
| **CNMC** | Estatal | Regulación ***ex ante*** de mercados, análisis de poder significativo, resolución de conflictos entre operadores, supervisión de precios del servicio universal |
| **AEPD** | Estatal | Autoridad de control en materia de protección de datos |
| **CCN-CERT** | Estatal | Capacidad de respuesta a incidentes del sector público; guías **CCN-STIC** |

**Otras normas de contexto que conviene citar.** La **Ley 13/2022, de 7 de julio, General de Comunicación Audiovisual**, que regula los servicios de comunicación audiovisual y define el **múltiplex** (§6.2.1); el **Reglamento (UE) 2015/2120** de **internet abierta**, que consagra la **neutralidad de la red** —tratamiento equitativo del tráfico y prohibición de bloqueo o estrangulamiento salvo excepciones tasadas— y, en su versión vigente, el régimen de **itinerancia** en la Unión; el **RD 346/2011** de **infraestructuras comunes de telecomunicaciones**, que es el que obliga a que todo edificio nuevo nazca preparado para que entren varios operadores; y el **art. 156 de la Ley 40/2015**, que es el fundamento legal del **ENS** y del **ENI** y, por tanto, del marco de interoperabilidad de las redes de las Administraciones \[L40-2015\].

> **Ejercicio resuelto.** **Cuatro decisiones de una red municipal y su encaje legal.** Indique el régimen aplicable a cada actuación del Ayuntamiento. **(a)** Desplegar Wi-Fi en la banda de 5 GHz en las bibliotecas municipales, para uso del personal. **(b)** Instalar un radioenlace propio en banda licenciada entre dos sedes. **(c)** Ofrecer wifi gratuita a la ciudadanía en las plazas de un distrito. **(d)** Contratar a un operador el circuito de fibra que une el distrito con el CPD. **Solución.** **(a)** Banda de **uso común**: basta con respetar los límites de potencia y las condiciones técnicas de uso; **no hace falta título individual** ni pago de tasa por reserva. Y como es red interna de usuario final, **no** entra en el art. 13. **(b)** Uso **privativo** del dominio público radioeléctrico: exige **título habilitante** del Ministerio y devenga **tasa** por reserva del dominio público radioeléctrico \[LGT, título V y título VII\]. **(c)** Aquí sí aparece el **art. 13**: se estaría prestando un servicio disponible **al público**. Hay que valorar el **principio de inversor privado**, la **no distorsión de la competencia** y, en su caso, la comunicación al **Registro de operadores**; en la práctica, delimitar el servicio como **accesorio y limitado** —caudal y usos acotados, sin sustituir a la oferta comercial— y documentar esa delimitación. Es la respuesta que distingue al que ha leído el artículo. **(d)** El Ayuntamiento actúa como **usuario final** que contrata a un operador, con la particularidad de que la contratación se rige además por la **normativa de contratos del sector público**. Las obligaciones de **integridad y seguridad de la red** del art. 63 pesan sobre **el operador**, no sobre el Ayuntamiento; pero las del **ENS** sobre el sistema municipal siguen siendo del Ayuntamiento, que deberá exigir contractualmente las garantías correspondientes —cifrado del circuito, niveles de servicio, notificación de incidentes—.

------------------------------------------------------------------------

### Cierre: los ocho datos que no se pueden fallar

1.  **Telecomunicación** = *«toda transmisión, emisión o recepción de signos, señales, escritos, imágenes, sonidos o informaciones de cualquier naturaleza por hilo, radioelectricidad, medios ópticos u otros sistemas electromagnéticos»* \[LGT, anexo II.79\]. **Espectro radioeléctrico** = ondas por debajo de **3.000 GHz** que se propagan **sin guía artificial**, y es **bien de dominio público estatal**.
2.  **Ancho de banda** se mide en **hercios**; **velocidad de transmisión**, en **bits por segundo**; **velocidad de modulación**, en **baudios**. **Shannon**: `C = B·log₂(1 + S/N)` con S/N **en veces**. **Muestreo**: `fm ≥ 2·fmax`, de donde sale el canal de **64 kbps**.
3.  **Límite de 100 m** del enlace de cobre (90 + 10). **Fibra monomodo** ≈ 9 µm y decenas de kilómetros; **multimodo** 50 o 62,5 µm y cientos de metros. **A mayor frecuencia, más capacidad y menos alcance.**
4.  **Símplex / semidúplex / dúplex**: el **Wi-Fi es semidúplex** porque una radio no puede escuchar mientras transmite; **TETRA** también, por diseño. **A alta velocidad gana la transmisión serie**, por el *skew* del paralelo.
5.  **El conmutador segmenta el dominio de COLISIÓN pero NO el de DIFUSIÓN**; solo lo dividen el **encaminador** y las **VLAN**. El **concentrador** es un solo dominio de colisión y es semidúplex.
6.  **Circuitos**: camino reservado, tres fases, sin fluctuación, desaprovecha. **Paquetes**: multiplexación estadística, encauzamiento, con fluctuación, aprovecha al máximo. El **circuito virtual es conmutación de paquetes**, no de circuitos.
7.  **MAC de difusión `FF:FF:FF:FF:FF:FF`**; **IPv4 limitada `255.255.255.255`**; **multidifusión IPv4 `224.0.0.0/4`**; **IPv6 no tiene difusión** y usa `ff02::1`. La trama Ethernet **no tiene TTL**: de ahí las tormentas de difusión y la necesidad de **STP**.
8.  **Wi-Fi 7 = 802.11be, publicado el 22 de julio de 2025**, con **MLO** y **4096-QAM**; **Wi-Fi 8 = 802.11bn, previsto para 2028**. **WPA3 con SAE**; ocultar el SSID y filtrar por MAC **no son seguridad**. **`mp.com.4.2` del ENS: las comunicaciones inalámbricas van en un segmento separado.** **Servicio universal: 10 Mbit/s** descendentes en ubicación fija, escalables a 30.

## Diagramas

### Índice de diagramas

| ID | Título | Sección | Tipo |
|----|----|----|----|
| D1 | El modelo de comunicación de Shannon: los cinco elementos | §1.1.1 | Flujo |
| D2 | Perturbaciones del canal: atenuación, distorsión, ruido e interferencia | §1.1.1 | Comparativa |
| D3 | De la señal a los bits: muestreo, Nyquist y Shannon | §1.2 | Flujo + fórmulas |
| D4 | Los tres medios de transmisión guiados comparados | §2.1.1 | Comparativa |
| D5 | El espectro radioeléctrico: bandas de la UIT y regla de la frecuencia | §2.2.1 | Escala + regla |
| D6 | Parámetros de calidad de un enlace y qué degrada cada uno | §2.3 | Tabla visual |
| D7 | Símplex, semidúplex y dúplex | §3.1 | Comparativa |
| D8 | Sincronismo y forma de transmisión: asíncrona/síncrona y serie/paralelo | §3.2 y §3.3 | Estructura + comparativa |
| D9 | Equipos de interconexión clasificados por capa | §4.2.1 | Capas |
| D10 | Dominios de colisión y dominios de difusión | §4.2.1 | Esquema |
| D11 | Redes por cobertura geográfica: PAN, LAN, MAN y WAN | §5.1 | Escala |
| D12 | Topologías físicas de red y su tolerancia a fallos | §5.2 | Comparativa |
| D13 | Conmutación de circuitos, de mensajes y de paquetes | §6.1.1 | Comparativa + tiempos |
| D14 | Modos de entrega y direcciones de difusión y multidifusión | §6.2.1 | Esquema + tabla |
| D15 | Redes inalámbricas: escala, arquitectura Wi-Fi y generaciones | §7 | Capas + escalera |
| D16 | La red celular: principio celular y evolución de 1G a 5G | §8.1 y §8.2 | Esquema + línea temporal |
| D17 | Seguridad inalámbrica: de WEP a WPA3 y medidas `mp.com` del ENS | §9.1 | Escalera + tabla |
| D18 | La Ley 11/2022: estructura, servicio universal y art. 13 | §9.2 | Capas |

------------------------------------------------------------------------

### D1 · El modelo de comunicación de Shannon: los cinco elementos

**Sección**: §1.1.1 — Elementos del sistema de transmisión y perturbaciones en el canal **Propósito**: Fijar los cinco elementos en su orden correcto y, sobre todo, dejar claro que el ruido ataca **al canal**, que es el detalle de dibujo clave.

![Modelo de comunicación de Shannon con sus cinco elementos en cadena: fuente de información, transmisor, canal, receptor y destino, con la fuente de ruido actuando sobre el canal y no sobre el mensaje](diagramas/diagrama-01.svg)

------------------------------------------------------------------------

### D2 · Perturbaciones del canal: atenuación, distorsión, ruido e interferencia

**Sección**: §1.1.1 — Elementos del sistema de transmisión y perturbaciones en el canal **Propósito**: Separar con precisión las cinco familias de perturbación, que se confunden entre sí, e identificar el remedio de cada una.

![Las cinco familias de perturbaciones del canal: atenuación, distorsión, ruido con sus cuatro tipos, interferencia y eco, con la definición y el remedio de cada una y el aviso de que el ruido impulsivo es el más dañino en transmisión digital](diagramas/diagrama-02.svg)

------------------------------------------------------------------------

### D3 · De la señal a los bits: muestreo, Nyquist y Shannon

**Sección**: §1.2 — Transmisión analógica y digital: ancho de banda y velocidad de transmisión **Propósito**: Reunir en una sola imagen las tres fórmulas que hay que saber de memoria y el cálculo del canal de 64 kbps, que es el ejercicio numérico más repetido del bloque.

![Digitalización de una señal analógica en tres pasos, muestreo cuantificación y codificación, con el teorema del muestreo, las fórmulas de capacidad de Nyquist y de Shannon y el cálculo del canal telefónico digital de 64 kilobits por segundo](diagramas/diagrama-03.svg)

------------------------------------------------------------------------

### D4 · Los tres medios de transmisión guiados comparados

**Sección**: §2.1.1 — Par trenzado, cable coaxial y fibra óptica **Propósito**: Poner en la misma escala los tres medios guiados y anclar los datos numéricos clave: los 100 metros del cobre, los diámetros de núcleo y las ventanas de la fibra.

![Comparación de los tres medios de transmisión guiados: par trenzado con sus categorías y el límite de cien metros, cable coaxial de cincuenta y setenta y cinco ohmios, y fibra óptica monomodo y multimodo con sus diámetros de núcleo y sus ventanas de trabajo](diagramas/diagrama-04.svg)

------------------------------------------------------------------------

### D5 · El espectro radioeléctrico: bandas de la UIT y regla de la frecuencia

**Sección**: §2.2.1 — Espectro radioeléctrico, radiofrecuencia, microondas e infrarrojos **Propósito**: Ordenar las bandas decádicas con su uso característico y dejar grabada la regla de oro —a más frecuencia, más capacidad y menos alcance—, que explica todas las decisiones de espectro del tema.

![Bandas del espectro radioeléctrico según la Unión Internacional de Telecomunicaciones, de muy baja frecuencia a extra alta frecuencia, con el uso característico de cada una y la regla de que a mayor frecuencia hay más capacidad pero menos alcance y peor penetración](diagramas/diagrama-05.svg)

------------------------------------------------------------------------

### D6 · Parámetros de calidad de un enlace y qué degrada cada uno

**Sección**: §2.3 — Parámetros de caracterización y calidad en medios de transmisión **Propósito**: Fijar la unidad de cada parámetro y separar latencia de fluctuación, que es la confusión más frecuente al interpretar un acuerdo de nivel de servicio.

![Parámetros de calidad de un enlace con su unidad de medida: ancho de banda en hercios, caudal en bits por segundo, atenuación y relación señal ruido en decibelios, latencia y fluctuación en milisegundos, tasa de error de bit y pérdida de paquetes, con la advertencia de que el decibelio es logarítmico](diagramas/diagrama-06.svg)

------------------------------------------------------------------------

### D7 · Símplex, semidúplex y dúplex

**Sección**: §3.1 — Modos según la direccionalidad: símplex, half-dúplex y full-dúplex **Propósito**: Separar los tres modos por la **simultaneidad** —no por la bidireccionalidad— y justificar por qué el Wi-Fi es semidúplex, que es la trampa recurrente.

![Los tres modos de direccionalidad: símplex en un solo sentido, semidúplex en los dos sentidos alternando y dúplex en los dos sentidos a la vez, con ejemplos y con la explicación de por que el Wi-Fi es semidúplex](diagramas/diagrama-07.svg)

------------------------------------------------------------------------

### D8 · Sincronismo y forma de transmisión: asíncrona/síncrona y serie/paralelo

**Sección**: §3.2 — Modos según el sincronismo · §3.3 — Modos según la forma de transmisión **Propósito**: Mostrar la estructura real de un carácter asíncrono —de donde sale la sobrecarga del 27 %— y justificar por qué el paralelo perdió la batalla a alta velocidad.

![Estructura de un carácter en transmisión asíncrona con bit de arranque, ocho bits de datos, paridad y bit de parada, comparada con la trama síncrona, y comparación entre transmisión serie y paralelo con las tres razones por las que el paralelo no escala](diagramas/diagrama-08.svg)

------------------------------------------------------------------------

### D9 · Equipos de interconexión clasificados por capa

**Sección**: §4.2.1 — Repetidores, concentradores, puentes, conmutadores y encaminadores **Propósito**: Ordenar todos los equipos del enunciado por la capa en la que operan y por la dirección que usan para decidir.

![Equipos de interconexión ordenados por capa: en capa uno repetidor concentrador y transceptor que trabajan con señales, en capa dos puente conmutador y punto de acceso que usan direcciones MAC, en capa tres encaminador y conmutador de capa tres que usan direcciones IP, y en capas superiores la pasarela que traduce entre arquitecturas distintas](diagramas/diagrama-09.svg)

------------------------------------------------------------------------

### D10 · Dominios de colisión y dominios de difusión

**Sección**: §4.2.1 — Repetidores, concentradores, puentes, conmutadores y encaminadores **Propósito**: Resolver de un vistazo la distinción central del temario de redes: qué equipo segmenta qué dominio.

![Comparación de concentrador, conmutador y encaminador según los dominios de colisión y de difusión que crean: el concentrador deja un único dominio de colisión y uno de difusión, el conmutador crea un dominio de colisión por puerto pero mantiene uno solo de difusión, y el encaminador crea un dominio de difusión por interfaz](diagramas/diagrama-10.svg)

------------------------------------------------------------------------

### D11 · Redes por cobertura geográfica: PAN, LAN, MAN y WAN

**Sección**: §5.1 — Clasificación por cobertura geográfica **Propósito**: Fijar la escala completa y, sobre todo, los tres criterios que de verdad separan una LAN de una WAN más allá de los kilómetros.

![Escala de redes por cobertura geográfica desde la red de área personal de metros hasta la red de área extensa de alcance continental, pasando por la red local, la de campus y la metropolitana, con los tres criterios que separan una red local de una red extensa: titularidad del medio, velocidad y latencia, y tasa de error](diagramas/diagrama-11.svg)

------------------------------------------------------------------------

### D12 · Topologías físicas de red y su tolerancia a fallos

**Sección**: §5.2 — Topologías de red físicas y lógicas **Propósito**: Dibujar las cinco topologías básicas con su punto único de fallo, y separar el plano físico del lógico, que es la distinción clave.

![Las cinco topologías físicas de red: bus, anillo, estrella, árbol y malla, dibujadas con sus nodos y enlaces, indicando en cada una el punto único de fallo, y la distinción entre topología física y topología lógica con el ejemplo de Ethernet conmutado y de Token Ring](diagramas/diagrama-12.svg)

------------------------------------------------------------------------

### D13 · Conmutación de circuitos, de mensajes y de paquetes

**Sección**: §6.1.1 — Conmutación de circuitos, de mensajes y de paquetes **Propósito**: Comparar las tres técnicas en ocho rasgos clave y visualizar el encauzamiento, que es la razón numérica de que la conmutación de paquetes gane.

![Comparación de las tres técnicas de conmutación: de circuitos con camino reservado y tres fases, de mensajes con almacenamiento y reenvío del mensaje completo, y de paquetes con multiplexación estadística y encauzamiento, más la distinción entre datagrama y circuito virtual](diagramas/diagrama-13.svg)

------------------------------------------------------------------------

### D14 · Modos de entrega y direcciones de difusión y multidifusión

**Sección**: §6.2.1 — Principios de difusión, direcciones broadcast y multicast **Propósito**: Reunir los cuatro modos de entrega con las direcciones exactas de cada uno, que son datos de memorización literal, y marcar la supresión de la difusión en IPv6.

![Los cuatro modos de entrega: unidifusión a uno, multidifusión a un grupo suscrito, difusión a todos y anydifusión al más cercano, con las direcciones de difusión y multidifusión en Ethernet, IPv4 e IPv6, y la advertencia de que IPv6 no tiene difusión](diagramas/diagrama-14.svg)

------------------------------------------------------------------------

### D15 · Redes inalámbricas: escala, arquitectura Wi-Fi y generaciones

**Sección**: §7 — Redes e infraestructuras inalámbricas **Propósito**: Situar cada tecnología inalámbrica en su escala de cobertura y fijar la tabla de generaciones de Wi-Fi con las dos fechas clave: 2025 para Wi-Fi 7 y 2028 para Wi-Fi 8.

![Redes inalámbricas ordenadas por cobertura, de la red de área personal con Bluetooth NFC y Zigbee a la red de área extensa con redes celulares satélite y LPWAN, con la arquitectura Wi-Fi de celda BSS y conjunto extendido ESS, y la tabla de generaciones de Wi-Fi 4 a Wi-Fi 8 con sus años](diagramas/diagrama-15.svg)

------------------------------------------------------------------------

### D16 · La red celular: principio celular y evolución de 1G a 5G

**Sección**: §8.1 — Evolución y arquitectura de redes celulares móviles · §8.2 — Tecnologías consolidadas y de alta capacidad **Propósito**: Explicar la reutilización de frecuencias y encadenar las cinco generaciones con el salto conceptual de cada una y las tres familias de uso del 5G.

![Principio celular con reutilización de frecuencias en celdas hexagonales no adyacentes, traspaso e itinerancia, evolución de las generaciones móviles de 1G analógica a 5G, y las tres familias de uso del 5G: banda ancha mejorada, comunicaciones ultrafiables de baja latencia y comunicaciones masivas entre máquinas](diagramas/diagrama-16.svg)

------------------------------------------------------------------------

### D17 · Seguridad inalámbrica: de WEP a WPA3 y medidas `mp.com` del ENS

**Sección**: §9.1 — Aspectos de seguridad e integridad en redes inalámbricas **Propósito**: Encadenar la evolución de los protocolos con su estado actual, descartar expresamente las dos medidas cosméticas y anclar las cuatro medidas `mp.com` del ENS con su nivel de exigencia.

![Evolución de los protocolos de seguridad inalámbrica desde WEP roto hasta WPA3 con autenticación SAE, medidas que no aportan seguridad real como ocultar el SSID o filtrar por dirección MAC, y las cuatro medidas de protección de las comunicaciones del Esquema Nacional de Seguridad con su nivel de exigencia](diagramas/diagrama-17.svg)

------------------------------------------------------------------------

### D18 · La Ley 11/2022: estructura, servicio universal y art. 13

**Sección**: §9.2 — Marco normativo y regulatorio de telecomunicaciones en el ámbito público **Propósito**: Dar la estructura de la ley y aislar los tres preceptos que un técnico municipal debe conocer literalmente: el art. 2, el art. 37 y el art. 13.

![Estructura de la Ley 11 de 2022 General de Telecomunicaciones con sus ocho títulos, el principio de que las telecomunicaciones son servicios de interés general en libre competencia, el contenido del servicio universal con diez megabits por segundo, y el régimen del artículo 13 para las Administraciones públicas que instalan redes](diagramas/diagrama-18.svg)

## Casos prácticos

Los tres casos recorren el supuesto de referencia del tema (ver la pestaña Contenido, «Convenciones»): la **red de comunicaciones que conecta una Oficina de Atención a la Ciudadanía de un distrito con el centro de proceso de datos del IAM**. El **Caso 1** trabaja los **medios de transmisión, los modos y los parámetros de calidad**; el **Caso 2**, los **equipos de interconexión, las topologías y la difusión**; y el **Caso 3**, el **despliegue inalámbrico y móvil** y su encaje en el **marco normativo y de seguridad**.

------------------------------------------------------------------------

### Caso 1 — Medios de transmisión, modos y calidad del enlace de una oficina de distrito

#### Enunciado

El IAM va a reformar la **Oficina de Atención a la Ciudadanía** de un distrito y debe rediseñar sus comunicaciones. Datos del supuesto:

- El edificio tiene **tres plantas**. En cada planta hay un armario de comunicaciones y el puesto más alejado está a **78 metros** de cable desde su armario.
- En la planta baja hay **40 puestos de trabajo**, **12 teléfonos IP**, **6 cámaras de videovigilancia IP**, **4 pantallas de gestión de turnos** y **una impresora multifunción**.
- Los armarios de las tres plantas deben unirse entre sí; la distancia vertical entre el armario de la planta baja y el de la segunda es de **60 metros** de recorrido de cable, atravesando dos cuadros eléctricos distintos.
- El edificio debe conectarse con el **centro de proceso de datos del IAM**, situado a **6 kilómetros**.
- Existe además una **caseta de control** en el patio trasero, a **300 metros**, sin canalización disponible, con presupuesto y plazo muy ajustados y con visión directa despejada desde la azotea.
- La aplicación de tramitación exige un caudal modesto, pero se va a implantar **telefonía IP** y **videoconferencia** con las juntas de distrito.

#### Cuestiones

**Cuestión 1 — Elección de medios (3 puntos).** Indique y **justifique** el medio de transmisión adecuado para cada uno de los cuatro tramos: horizontal de planta, vertical entre armarios, acometida al CPD y caseta del patio.

**Cuestión 2 — Datos numéricos y límites (2 puntos).** Para el tramo horizontal, indique la **categoría** mínima de cable, la **longitud máxima** normalizada del enlace y su desglose, y qué norma de **alimentación por Ethernet** hace falta para los teléfonos, las cámaras y las pantallas.

**Cuestión 3 — Modos de comunicación (2 puntos).** Clasifique según los **tres criterios** de modo de comunicación (direccionalidad, sincronismo y forma de transmisión): (a) el enlace Ethernet de un puesto de trabajo; (b) el enlace de la caseta del patio; (c) la megafonía de avisos de la sala de espera.

**Cuestión 4 — Parámetros de calidad (3 puntos).** Redacte los **cinco parámetros** que debe recoger el acuerdo de nivel de servicio del circuito contratado al operador para el enlace con el CPD, indicando **unidad** y **por qué** importa cada uno para los servicios previstos. Explique además por qué el caudal real medido en el Wi-Fi de la oficina será muy inferior al anunciado.

#### Solución orientativa

- **C1**: (§2.1.1, §2.2.1, §2.3)

| Tramo | Medio propuesto | Justificación |
|----|----|----|
| **Horizontal de planta** | **Par trenzado Cat 6A (F/UTP o U/FTP)** | Los 78 m están dentro del límite de 100 m; coste bajo por punto; y sobre todo **permite PoE**, que es imprescindible para teléfonos, cámaras y pantallas. La fibra al puesto sería técnicamente válida pero dejaría a esos terminales **sin alimentación** y multiplicaría el coste |
| **Vertical entre armarios** | **Fibra óptica multimodo OM4** | 60 m está dentro del alcance de la multimodo; y hay una razón adicional decisiva: al atravesar **dos cuadros eléctricos distintos** interesa el **aislamiento galvánico** que da un medio dieléctrico, que evita transportar diferencias de potencial y sobretensiones entre plantas |
| **Acometida al CPD (6 km)** | **Fibra monomodo OS2**, normalmente en forma de **circuito contratado a un operador** | El cobre queda descartado por atenuación (tres órdenes de magnitud fuera del límite); la multimodo también, por dispersión modal. A 6 km por vía pública lo realista es contratar el circuito, porque el trazado atraviesa **dominio público** |
| **Caseta del patio (300 m)** | **Radioenlace de microondas punto a punto**, o Wi-Fi exterior direccional en banda de uso común | Es la respuesta correcta **precisamente porque no hay canalización**: abrir zanja tiene un coste y un plazo incomparablemente mayores. Condiciones que hay que declarar: exige **visión directa** —que el enunciado confirma— y, por ser medio compartido, obliga a **cifrar el enlace** |

Conviene añadir la observación general: **la elección del medio no la decide la velocidad, sino la distancia, la necesidad de alimentación y quién es el titular del suelo por el que discurre el cable**.

- **C2**: (§2.1.1)
  - **Categoría mínima: Cat 6A**, con 500 MHz de ancho de banda. Se justifica no por la necesidad actual —1 Gbit/s basta— sino porque es la que garantiza **10GBASE-T a los 100 m completos**, y el cableado horizontal es el elemento de la instalación con **vida útil más larga** (15-20 años) y el más caro de sustituir. La Cat 6 solo da 10 Gbit/s hasta unos 55 m, y la Cat 8 está limitada a 30 m y es de centro de datos.
  - **Longitud máxima del enlace: 100 m**, desglosados en **90 m de cable horizontal fijo** (del armario a la roseta) **más 10 m** repartidos entre los latiguillos de ambos extremos. Los 78 m del enunciado dejan margen suficiente. Hay que advertir de que superar el límite **no produce un fallo limpio**, sino errores intermitentes muy difíciles de diagnosticar.
  - **Alimentación por Ethernet**: los teléfonos IP y las pantallas se cubren con **802.3af (PoE, 15,4 W)**; las **cámaras** con motorización, calefactor o iluminación infrarroja requieren **802.3at (PoE+, 30 W)**. Si se previera algún punto de acceso Wi-Fi 6E/7 de gama alta o un domo con más consumo, habría que dimensionar **802.3bt**. Consecuencia de diseño que conviene señalar: **el conmutador pasa a ser también un equipo eléctrico crítico**, y debe dimensionarse su presupuesto de potencia PoE y respaldarse con SAI.

&nbsp;

- **C3**: (§3.1, §3.2, §3.3)

| Enlace | Direccionalidad | Sincronismo | Forma |
|----|----|----|----|
| **(a) Ethernet del puesto** | **Dúplex**, porque hay pares separados de transmisión y recepción y el equipo del otro extremo es un **conmutador** (con un concentrador sería semidúplex) | **Síncrona**: trama con preámbulo y reloj extraído de la señal por codificación de línea | **Serie** |
| **(b) Radioenlace de la caseta** | **Semidúplex** si es Wi-Fi exterior (una radio no puede escuchar mientras transmite); un radioenlace de microondas profesional puede ser **dúplex** por **FDD**, con una banda por sentido | **Síncrona** | **Serie** |
| **(c) Megafonía de avisos** | **Símplex**: un solo sentido y sin canal de retorno | Analógica en su versión clásica; **síncrona** si es megafonía sobre IP | Serie |

La conclusión que se espera es que **los tres criterios son independientes y se combinan**: casi todo lo moderno es **síncrono y serie**, y lo que de verdad varía de un enlace a otro es la **direccionalidad**.

- **C4**: (§2.3)

| Parámetro | Unidad | Por qué importa aquí |
|----|----|----|
| **Caudal garantizado** | Mbit/s | Debe cubrir la tramitación, la telefonía IP y la videoconferencia simultáneas; conviene que sea **garantizado**, no «hasta» |
| **Latencia máxima** | ms | La videoconferencia con las juntas de distrito deja de ser natural por encima de unos 150 ms de extremo a extremo |
| **Fluctuación (*jitter*) máxima** | ms | **Es el parámetro crítico para la voz**: la variación del retardo produce cortes y voz metálica, mientras que una latencia alta pero estable se tolera |
| **Pérdida de paquetes** | % | Degrada la voz y el vídeo de forma inmediata y muy visible |
| **Disponibilidad y tiempo de resolución** | % y horas | Una oficina de atención presencial sin red **no puede atender**: hay que fijar disponibilidad, ventana de servicio y plazo máximo de reparación |

Cabe añadir, con buen criterio, **la exigencia de cifrado del circuito**, que en un sistema sujeto al ENS deriva de `mp.com.2` y `mp.com.3`, y la **notificación de incidentes** por parte del operador.

**Por qué el caudal real del Wi-Fi es muy inferior al anunciado**: porque el medio radio es **compartido y semidúplex**, la capacidad se reparte entre todos los clientes activos, cada trama debe **confirmarse con un ACK**, el mecanismo **CSMA/CA** consume tiempo en escuchas y esperas aleatorias, y a ello se suman las cabeceras de todos los protocolos. Un caudal real en torno a **la mitad o menos** de la velocidad nominal **no es una avería**: es el funcionamiento normal, y conviene decírselo así a quien reclama.

#### Criterios de evaluación

| Criterio | Puntos |
|----|----|
| Los cuatro medios correctamente elegidos **y justificados por distancia, alimentación y titularidad del suelo** | 3 |
| Categoría 6A, límite de 100 m con desglose 90 + 10 y normas PoE correctas | 2 |
| Clasificación correcta en los tres criterios, señalando que son independientes | 2 |
| Cinco parámetros con su unidad y su justificación funcional | 2 |
| Explicación correcta de la diferencia entre caudal real y nominal en Wi-Fi | 1 |

------------------------------------------------------------------------

#### Preguntas tipo test sobre este caso

##### 1. En el supuesto planteado, ¿qué medio conviene para el cableado horizontal de la planta baja, con teléfonos IP, cámaras y pantallas de turnos?

- a) Par trenzado de categoría 6A, porque los 78 m están dentro del límite y permite alimentar los terminales por PoE.
- b) Fibra óptica multimodo hasta cada puesto, porque ofrece más capacidad y elimina cualquier problema de distancia.
- c) Cable coaxial de 75 Ω, porque transporta a la vez la señal de datos, la de vídeo y la alimentación eléctrica.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.1.1

El coste por punto es bajo y, sobre todo, el par trenzado permite PoE; la fibra al puesto sería técnicamente válida, pero dejaría sin alimentación a los terminales y multiplicaría el coste.

##### 2. El tramo vertical entre armarios mide 60 m y atraviesa dos cuadros eléctricos distintos. ¿Qué medio es el adecuado y por qué?

- a) Par trenzado Cat 6A, porque 60 m caben en el límite de 100 m y el cobre iguala el potencial entre plantas.
- b) Fibra monomodo OS2, porque la multimodo no puede superar los 50 m de recorrido dentro de un edificio.
- c) Fibra multimodo OM4, porque cubre la distancia y, al ser dieléctrica, da aislamiento galvánico entre cuadros.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.1.1

60 m están dentro del alcance de la multimodo, y un medio dieléctrico evita transportar diferencias de potencial y sobretensiones entre plantas alimentadas por cuadros distintos.

##### 3. ¿Qué solución corresponde a la acometida con el CPD del IAM, situado a 6 km?

- a) Par trenzado blindado de categoría 8, tendido por la vía pública hasta el CPD del IAM.
- b) Fibra monomodo OS2, normalmente como circuito contratado a un operador por la vía pública.
- c) Fibra multimodo OM4, porque ofrece mayor ancho de banda que la monomodo en esa distancia.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.1.1

El cobre queda descartado por atenuación y la multimodo por dispersión modal; además, el trazado atraviesa dominio público, por lo que lo realista es contratar el circuito.

##### 4. La caseta del patio está a 300 m, sin canalización, con presupuesto y plazo ajustados y con visión directa desde la azotea. ¿Qué solución procede?

- a) Un radioenlace punto a punto o Wi-Fi exterior direccional, con el enlace cifrado por ser medio compartido.
- b) Abrir zanja y tender fibra monomodo, porque cualquier enlace radio es inaceptable en una red municipal.
- c) Par trenzado Cat 6A con un repetidor a mitad de camino, porque así se superan los 100 m sin obra civil.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.2.1

Sin canalización, la zanja tiene un coste y un plazo incomparablemente mayores; el radioenlace exige visión directa, que el enunciado confirma, y cifrado.

##### 5. Si con 1 Gbit/s basta hoy, ¿por qué se exige categoría 6A en el cableado horizontal?

- a) Porque la categoría 6 no admite PoE y la 6A es la primera categoría que puede alimentar teléfonos y cámaras.
- b) Porque garantiza 10GBASE-T a los 100 m completos y el cableado horizontal dura 15-20 años y es caro de sustituir.
- c) Porque la categoría 8 está prohibida en edificios de oficinas y la 6A es la de mayor capacidad que se permite.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.1.1

La Cat 6 solo da 10 Gbit/s hasta unos 55 m y la Cat 8 se limita a 30 m y es de centro de datos; la 6A protege la inversión durante toda la vida del cableado.

##### 6. El puesto más alejado está a 78 m de cable desde su armario. ¿Respeta el límite normalizado del enlace?

- a) No: el límite del cable horizontal fijo es de 75 m, de modo que habría que añadir otro armario.
- b) Sí, y sobra: el límite de 100 m se aplica solo al cable fijo, sin contar los latiguillos de los extremos.
- c) Sí: el enlace admite 100 m, 90 de cable horizontal fijo más 10 repartidos entre los latiguillos.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.1.1

Los 78 m dejan margen dentro de los 90 m de horizontal; superar el límite no produce un fallo limpio, sino errores intermitentes difíciles de diagnosticar.

##### 7. Las cámaras de videovigilancia tienen motorización, calefactor e iluminación infrarroja. ¿Qué norma de alimentación por Ethernet necesitan?

- a) 802.3af (PoE), con 15,4 W por puerto, igual que los teléfonos.
- b) 802.3at (PoE+), con 30 W por puerto, por su mayor consumo.
- c) Ninguna: deben llevar una fuente de alimentación propia.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §2.1.1

Teléfonos y pantallas se cubren con 802.3af; las cámaras con más consumo requieren 802.3at. El conmutador se convierte en equipo eléctrico crítico y debe dimensionarse su presupuesto PoE.

##### 8. ¿Cómo se clasifica, por su direccionalidad, la megafonía de avisos de la sala de espera?

- a) Semidúplex, porque los avisos se emiten por turnos.
- b) Dúplex, porque varios altavoces suenan a la vez.
- c) Símplex: un solo sentido y sin canal de retorno.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §3.1

La información va solo del emisor a los oyentes, que no pueden responder por el mismo canal.

##### 9. ¿Qué parámetro del acuerdo de nivel de servicio, medido en milisegundos, hace que la videoconferencia con las juntas de distrito deje de ser natural por encima de unos 150 ms de extremo a extremo?

- a) La latencia máxima.
- b) La pérdida de paquetes.
- c) El caudal garantizado.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §2.3

La latencia es el retardo de extremo a extremo; la pérdida se mide en porcentaje y el caudal en Mbit/s.

##### 10. Los usuarios reclaman que el Wi-Fi de la oficina da mucho menos caudal del anunciado. ¿Qué hay que responderles?

- a) Que es una avería de los puntos de acceso, porque el caudal real debe igualar siempre la velocidad nominal.
- b) Que se debe a que la red Wi-Fi funciona en modo dúplex y reparte la velocidad entre emisión y recepción.
- c) Que es normal: el medio es compartido y semidúplex, cada trama se confirma y CSMA/CA consume tiempo.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 4 · §2.3

Un caudal real en torno a la mitad o menos de la velocidad nominal es el funcionamiento normal del Wi-Fi, no una avería.

### Caso 2 — Equipos de interconexión, topología y una tormenta de difusión

#### Enunciado

La red de la Oficina de Atención a la Ciudadanía se encuentra, tras años de crecimiento sin plan, en el siguiente estado:

- Un **encaminador de frontera** con **3 interfaces activas** conecta con el CPD del IAM.
- De la primera interfaz cuelga un **conmutador de 24 puertos** con 24 equipos, **sin VLAN**.
- De la segunda cuelga un **concentrador antiguo de 8 puertos** que sobrevive en el archivo, con 8 equipos.
- De la tercera cuelga un **conmutador de 12 puertos** en el que se han configurado **3 VLAN**.
- Toda la red comparte **un mismo espacio de direccionamiento** salvo en el último conmutador.
- Un lunes por la mañana, un técnico conecta **un latiguillo entre dos puertos libres del conmutador de 24 puertos** por error. En pocos segundos, **toda la red de la oficina deja de funcionar**, incluidos los equipos que no estaban comunicándose con nadie. La actividad de la interfaz del encaminador se dispara al 100 %.

#### Cuestiones

**Cuestión 1 — Recuento de dominios (2 puntos).** Calcule cuántos **dominios de colisión** y cuántos **dominios de difusión** hay en la red descrita, detallando el razonamiento.

**Cuestión 2 — Diagnóstico del incidente (3 puntos).** Explique **qué ha ocurrido** el lunes por la mañana, **por qué** un solo latiguillo puede tumbar toda la red y por qué el mismo error en la capa 3 no tendría ese efecto de forma indefinida.

**Cuestión 3 — Remedios (2 puntos).** Proponga **tres medidas** de distinta naturaleza para que el incidente no se repita, indicando en qué equipo se aplica cada una.

**Cuestión 4 — Rediseño (3 puntos).** Proponga el rediseño de la red indicando: **topología** objetivo y por qué; qué hacer con el **concentrador**; y qué **equipo de interconexión** resuelve cada una de estas tres necesidades: (a) separar el tráfico de las cámaras del de los puestos de trabajo, (b) llegar al CPD y (c) integrar un sistema de control de accesos que habla un protocolo propietario no IP.

#### Solución orientativa

- **C1**: (§4.2.1)

**Dominios de colisión.** Cada puerto activo de un conmutador es un dominio; el concentrador entero es **uno solo**, porque no segmenta.

- Conmutador de 24 puertos: **24** puertos con equipo **+ 1** puerto de subida al encaminador = **25**.
- Concentrador: **1** (los 8 equipos y el enlace al encaminador comparten el medio).
- Conmutador de 12 puertos: **12 + 1** = **13**.
- **Total: 25 + 1 + 13 = 39 dominios de colisión.**

**Dominios de difusión.** Uno por interfaz de encaminador, salvo que haya VLAN, que multiplican.

- Interfaz 1 (conmutador plano, sin VLAN): **1**.
- Interfaz 2 (concentrador): **1**.
- Interfaz 3 (conmutador con 3 VLAN): **3**.
- **Total: 5 dominios de difusión.**

La lectura que se espera: el **concentrador es un desastre en colisiones** pero indiferente en difusión; el **conmutador arregla lo primero y no toca lo segundo**; y solo las **VLAN** y el **encaminador** actúan sobre la difusión.

- **C2**: (§4.2.1, §6.2.1)
  - **Qué ha ocurrido**: el latiguillo ha creado un **bucle de nivel 2** en el conmutador de 24 puertos, y con él una **tormenta de difusión**.
  - **Por qué tumba toda la red**: una única trama de difusión —basta una petición ARP o un DHCP— entra en el bucle y **se multiplica en cada vuelta**, porque el conmutador la inunda por todos los puertos menos el de entrada. La causa técnica de que no se detenga es que **la trama Ethernet no tiene campo TTL**. En segundos el enlace se satura, y como **toda la interfaz 1 es un único dominio de difusión**, la avalancha alcanza a los 24 equipos, que además **procesan cada trama en su CPU**. De ahí que caigan también los equipos que no estaban comunicándose: no es que su tráfico no pase, es que **su procesador está ocupado descartando difusión**.
  - **Por qué en capa 3 no ocurre lo mismo**: el paquete **IP sí tiene TTL**, que el encaminador **decrementa** en cada salto y descarta al llegar a cero. Un bucle de encaminamiento produce paquetes perdidos y rutas subóptimas, pero **no una multiplicación indefinida**.
  - Conviene señalar que el incidente **no fue una avería del equipo ni un ataque**: fue un error de operación que la arquitectura de red **permitía** que fuese catastrófico. Ese es el fallo de fondo.

&nbsp;

- **C3**: (§4.2.1, §6.2.1) Tres medidas de naturaleza distinta:

1.  **Activar STP o, preferiblemente, RSTP** en todos los conmutadores. Es el remedio directo: detecta el camino redundante y **bloquea lógicamente** uno de los enlaces, reactivándolo automáticamente si falla el principal. Se aplica en **los conmutadores**.
2.  **Segmentar en VLAN** toda la red, no solo el último conmutador. No evita el bucle, pero **acota el dominio de difusión** y, con él, el alcance del desastre: la tormenta quedaría confinada a una VLAN en lugar de tumbar la oficina entera. Se aplica en **los conmutadores** y exige encaminamiento entre VLAN.
3.  **Control de tormentas por puerto** (*storm control*), que limita el porcentaje de tráfico de difusión y multidifusión admitido y desactiva el puerto al superarlo. Se aplica en **los conmutadores**, puerto a puerto.

- Como medidas complementarias de buena práctica: **protección de puerto de acceso** frente a la aparición de tramas de gestión de STP donde no debe haberlas, **desactivar administrativamente los puertos no usados** y etiquetar el patchado.

&nbsp;

- **C4**: (§4.2, §5.2)
  - **Topología objetivo: árbol (estrella jerárquica)**, con conmutadores de **acceso** en cada planta que suben a un **conmutador de capa 3** de edificio, y este al **encaminador de frontera**. Es la topología adecuada porque (a) el fallo de un enlace o de un puesto **solo afecta a ese puesto**; (b) el diagnóstico es sencillo, al concentrarse la gestión; y (c) escala añadiendo ramas. Su punto débil conocido es el **nodo superior**, que se mitiga con equipo redundante o al menos con repuesto y configuración guardada. Hacia el CPD conviene mantener el **doble camino** —fibra y radioenlace—, que introduce una **malla parcial mínima** de dos enlaces y responde al riesgo real de corte de fibra por obra en la vía pública.
  - **Qué hacer con el concentrador: retirarlo**, sin matices. Es un equipo de **capa 1** que (a) mantiene ocho equipos en **un único dominio de colisión** compartiendo el ancho de banda, (b) obliga a **semidúplex** y (c) —lo más grave— permite que **cualquier equipo conectado vea el tráfico de todos los demás** poniendo su interfaz en modo promiscuo, lo que es incompatible con la confidencialidad exigible a un sistema municipal. Se sustituye por un conmutador gestionable.
  - **Equipo para cada necesidad**:

| Necesidad | Equipo | Por qué |
|----|----|----|
| **(a)** Separar el tráfico de las cámaras del de los puestos | **Conmutador gestionable con VLAN**, y encaminamiento entre VLAN en el **conmutador de capa 3** | Cada VLAN es un **dominio de difusión** distinto; el aislamiento entre ellas exige pasar por capa 3, donde se aplica la política de acceso |
| **(b)** Llegar al CPD del IAM | **Encaminador de frontera** (capa 3) | Une **redes distintas**, decide la ruta por dirección IP, detiene la difusión y aporta las funciones de frontera (calidad de servicio, listas de acceso, terminación del circuito) |
| **(c)** Integrar el control de accesos con protocolo propietario no IP | **Pasarela (*gateway*)** | Es el único equipo que, operando en **capas superiores**, **traduce entre arquitecturas o protocolos distintos**. Ni un conmutador ni un encaminador pueden hacerlo: no entienden ese protocolo |

#### Criterios de evaluación

| Criterio | Puntos |
|----|----|
| Recuento correcto de los 39 dominios de colisión y los 5 de difusión, con razonamiento | 2 |
| Diagnóstico del bucle y la tormenta, **citando la ausencia de TTL en la trama Ethernet** | 2 |
| Explicación de por qué caen equipos que no se comunicaban (procesamiento de la difusión en la CPU) | 1 |
| Tres remedios de naturaleza distinta, correctamente ubicados en el equipo | 2 |
| Topología en árbol justificada y retirada razonada del concentrador | 1,5 |
| Los tres equipos correctos, especialmente la **pasarela** para el protocolo propietario | 1,5 |

------------------------------------------------------------------------

#### Preguntas tipo test sobre este caso

##### 1. En el supuesto planteado, ¿cuántos dominios de colisión hay en la red de la oficina?

- a) 37: 24 en el conmutador de 24 puertos, 1 en el concentrador y 12 en el de 12 puertos.
- b) 39: 25 en el conmutador de 24 puertos, 1 en el concentrador y 13 en el de 12 puertos.
- c) 47: 25 en el conmutador de 24 puertos, 9 en el concentrador y 13 en el de 12 puertos.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §4.2.1

Cada puerto activo de un conmutador es un dominio, incluido el de subida al encaminador; el concentrador no segmenta y es uno solo.

##### 2. ¿Cuántos dominios de difusión hay en esa misma red?

- a) 5: uno por cada interfaz del encaminador, salvo la tercera, cuyas 3 VLAN cuentan como 3.
- b) 3: uno por cada interfaz del encaminador, porque las VLAN no separan la difusión.
- c) 39: uno por cada dominio de colisión, porque cada puerto aísla también la difusión.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §4.2.1

El conmutador divide la colisión pero no la difusión; solo el encaminador y las VLAN actúan sobre ella: 1 + 1 + 3 = 5.

##### 3. ¿Qué ocurrió cuando el técnico conectó un latiguillo entre dos puertos libres del conmutador de 24 puertos?

- a) Provocó un bucle de encaminamiento en el encaminador de frontera.
- b) Duplicó una dirección IP, que bloqueó la tabla ARP del encaminador.
- c) Creó un bucle de nivel 2 y, con él, una tormenta de difusión.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §4.2.1, §6.2.1

Una sola trama de difusión entra en el bucle y se multiplica en cada vuelta, porque el conmutador la inunda por todos los puertos menos el de entrada.

##### 4. ¿Por qué la tormenta no se detiene por sí sola, mientras que un bucle de encaminamiento en capa 3 no se perpetúa?

- a) Porque el conmutador prioriza la difusión, mientras que el encaminador la descarta siempre.
- b) Porque la trama Ethernet no tiene campo TTL, y el paquete IP sí lo tiene y se descarta al llegar a cero.
- c) Porque las tramas Ethernet se reenvían más rápido que los paquetes IP en cualquier tipo de red.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §6.2.1

El encaminador decrementa el TTL en cada salto y descarta el paquete al llegar a cero; la trama Ethernet carece de ese campo y da vueltas indefinidamente.

##### 5. ¿Por qué dejaron de funcionar también los equipos que no estaban comunicándose con nadie?

- a) Porque el conmutador apagó sus puertos para protegerlos de la tormenta.
- b) Porque el encaminador les retiró la dirección IP al saturarse su interfaz.
- c) Porque su procesador quedó ocupado procesando y descartando la difusión.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §4.2.1

Toda la interfaz 1 es un único dominio de difusión: la avalancha llega a los 24 equipos, que procesan cada trama en su CPU.

##### 6. ¿Cuál es el remedio directo para que un bucle accidental como este no vuelva a tumbar la red, y dónde se aplica?

- a) Activar STP o, mejor, RSTP en todos los conmutadores, que bloquean lógicamente el camino redundante.
- b) Sustituir el encaminador de frontera por otro con más capacidad en la interfaz que da a la oficina.
- c) Reducir el tiempo de concesión DHCP de los equipos, para que las direcciones se renueven más a menudo.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §6.2.1

El árbol de expansión detecta el camino redundante, bloquea uno de los enlaces y lo reactiva automáticamente si falla el principal.

##### 7. ¿Qué efecto tendría segmentar en VLAN toda la red frente a un incidente como este?

- a) Evitaría por completo el bucle, porque las VLAN impiden conectar dos puertos del mismo conmutador.
- b) Ninguno, porque las VLAN solo separan el tráfico de voz y no afectan al tráfico de difusión.
- c) No evitaría el bucle, pero confinaría la tormenta a una VLAN en lugar de tumbar toda la oficina.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §4.2.1

Cada VLAN es un dominio de difusión distinto: acotar el dominio acota el alcance del desastre. Exige encaminamiento entre VLAN.

##### 8. ¿Qué debe hacerse con el concentrador de 8 puertos que sobrevive en el archivo?

- a) Mantenerlo, porque no afecta a la difusión y solo genera colisiones entre esos ocho equipos.
- b) Retirarlo y sustituirlo por un conmutador gestionable, porque además deja ver el tráfico ajeno.
- c) Conectarlo al conmutador de 24 puertos, para que comparta el mismo dominio de colisión.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §4.2.1

Es un equipo de capa 1: un único dominio de colisión, semidúplex y, lo más grave, cualquier equipo en modo promiscuo ve el tráfico de los demás, incompatible con la confidencialidad.

##### 9. ¿Qué equipo permite integrar el sistema de control de accesos, que habla un protocolo propietario no IP?

- a) Una pasarela, que traduce entre protocolos o arquitecturas distintos.
- b) Un conmutador gestionable, configurando una VLAN propia para ese sistema.
- c) Un encaminador, que decide la ruta por la dirección IP de cada paquete.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §4.2.2

Ni el conmutador ni el encaminador entienden un protocolo que no es IP; la pasarela opera en capas superiores y traduce entre arquitecturas.

##### 10. ¿Qué topología objetivo conviene para el rediseño de la red de la oficina?

- a) Un bus único que recorra las tres plantas, porque reduce el cableado y simplifica la gestión.
- b) Un árbol o estrella jerárquica, con acceso por planta, conmutador de capa 3 de edificio y encaminador.
- c) Una malla completa entre todos los equipos de la oficina, para que ningún fallo aísle a un puesto.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §5.2

En árbol, el fallo de un enlace o de un puesto solo afecta a ese puesto, el diagnóstico es sencillo y la red escala añadiendo ramas; su punto débil, el nodo superior, se mitiga con redundancia.

### Caso 3 — Despliegue inalámbrico y móvil, seguridad y marco normativo

#### Enunciado

El distrito quiere completar la reforma con cuatro actuaciones:

1.  **Wi-Fi corporativo** en las tres plantas del edificio, para los puestos móviles, las tabletas de los inspectores y los teléfonos de voz sobre wifi del personal de atención.
2.  **Wi-Fi de cortesía para la ciudadanía** en la sala de espera y, en una segunda fase, **en las tres plazas públicas del distrito**.
3.  **Sensores** de ocupación de aparcamiento, llenado de contenedores y calidad del aire repartidos por el distrito, incluidos algunos en sótanos y arquetas.
4.  Un **radioenlace propio** en banda licenciada entre el edificio de la oficina y un polideportivo municipal cercano.

El sistema de tramitación al que se accede desde esa red está categorizado en el ENS como de **categoría MEDIA**, con confidencialidad MEDIO e integridad y autenticidad ALTO.

#### Cuestiones

**Cuestión 1 — Diseño inalámbrico interior (3 puntos).** Proponga el diseño del Wi-Fi del edificio: número y finalidad de los SSID, mecanismo de autenticación y cifrado de cada uno, y segmentación. Justifique cada decisión citando la **medida del ENS** aplicable.

**Cuestión 2 — Medidas ineficaces (1 punto).** El responsable del edificio propone «ocultar el SSID y permitir solo las direcciones MAC de los equipos municipales». Valore la propuesta.

**Cuestión 3 — Tecnología para los sensores (2 puntos).** Elija la tecnología de comunicación para los sensores del distrito y **justifique** la elección, valorando expresamente los sensores situados en sótanos y arquetas. Indique la disyuntiva de fondo que hay que resolver.

**Cuestión 4 — Encaje normativo (4 puntos).** Analice el régimen jurídico de las cuatro actuaciones: (a) el Wi-Fi corporativo, (b) el Wi-Fi de cortesía en la sala de espera y en las plazas públicas, (c) los sensores y (d) el radioenlace en banda licenciada. Cite los preceptos de la **Ley 11/2022** aplicables.

#### Solución orientativa

- **C1**: (§7.1, §9.1) Diseño de **tres SSID sobre los mismos puntos de acceso**, cada uno en su propia VLAN:

| SSID | Finalidad | Autenticación y cifrado | Segmentación |
|----|----|----|----|
| **Corporativo** | Puestos móviles, tabletas y teléfonos del personal | **WPA3-Enterprise** con **802.1X / EAP-TLS** contra el directorio municipal | VLAN de usuarios, con acceso a los servicios internos según perfil |
| **Dispositivos** | Impresoras, pantallas de turnos, sensores de edificio | WPA3-Personal con clave larga y rotada, o **certificado de dispositivo** donde sea posible | VLAN propia, **sin acceso** a la red de servicios y con listas de control de acceso estrictas |
| **Cortesía** | Público de la sala de espera | Red abierta con **OWE** (*Wi-Fi Enhanced Open*), portal cautivo y aislamiento entre clientes | VLAN **totalmente aislada**, con **salida directa a internet** y ninguna ruta hacia la red municipal |

**Justificación normativa**, que es lo que se valora:

- **`mp.com.4.2`** del anexo II del ENS: *«si se emplean comunicaciones inalámbricas, será en un segmento separado»*. Es el respaldo directo de la decisión de VLAN independiente para todo lo inalámbrico.
- **`mp.com.4` con refuerzo R1**: al ser el sistema de **categoría MEDIA**, la medida aplica con `+[R1 o R2 o R3]`. El **R1** implementa los segmentos mediante **VLAN**, con un mínimo de tres subredes: **usuarios, servicios y administración**. El diseño propuesto lo cumple y lo supera.
- **`mp.com.2`** (confidencialidad, nivel **MEDIO** en este sistema): VPN cifrada cuando la comunicación salga del dominio propio, **más el refuerzo R1**, algoritmos y parámetros **autorizados por el CCN**.
- **`mp.com.3`** (integridad y autenticidad, nivel **ALTO**): exige `+R1+R2+R3+R4`, el nivel de exigencia más alto de las tres medidas en este sistema, precisamente porque la autenticidad del acto administrativo es lo que está en juego.
- **`mp.com.1`**: perímetro seguro, aplicable en las **tres categorías**; todo el tráfico debe atravesarlo y los flujos deben estar previamente autorizados.
- **Trazabilidad**: la elección de **802.1X con credencial individual** frente a una clave compartida no es una preferencia técnica, sino un **requisito de imputabilidad**: con clave precompartida no se puede saber quién hizo qué, y además revocar a una persona obliga a cambiar la clave a toda la organización.
- Se espera además la advertencia final: **el enlace radio es una capa más**. Los servicios municipales deben ir sobre **TLS** de extremo a extremo por encima de él, en aplicación del principio de **defensa en profundidad**.
- Elementos complementarios que suman: **802.11r** para que la itinerancia no corte las llamadas de voz sobre wifi, **802.11w** para neutralizar los ataques de desautenticación, **desactivar WPS**, planificar canales y potencias —emitir con más potencia de la necesaria amplía la superficie de exposición sin mejorar el servicio— y **detección continua de puntos de acceso no autorizados** desde el controlador.

&nbsp;

- **C2**: (§9.1) La propuesta **debe rechazarse**, y no por exceso de celo sino porque **ninguna de las dos medidas aporta seguridad real**:
  - **Ocultar el SSID** no lo oculta: el nombre de la red **viaja en claro** en las tramas de asociación de cualquier cliente que se conecte, de modo que basta con esperar. Y además complica la operación y genera incidencias de conexión.
  - **Filtrar por dirección MAC** no filtra: las direcciones MAC circulan **en claro** en todas las tramas y **se clonan trivialmente**; el atacante solo tiene que copiar una autorizada.
  - Lo relevante es el argumento de fondo: **son medidas cosméticas que dan una falsa sensación de protección**, que es lo peor que puede hacer una medida de seguridad, porque desplaza la atención de lo que sí protege —**cifrado robusto (WPA3) y autenticación por usuario (802.1X)**—. Cabe aceptarlas como complemento cosmético, nunca como sustituto.

&nbsp;

- **C3**: (§7.2)
  - **Elección: NB-IoT** (tecnología **3GPP** sobre espectro licenciado del operador) para los sensores en **sótanos y arquetas**, y **LoRaWAN** admisible para los sensores en superficie si se opta por red propia.
  - **Justificación**: los sensores son el caso de uso canónico de **LPWAN** —muy pocos datos, muy de vez en cuando, mucho alcance y años de batería—, y por tanto quedan descartados tanto el **Wi-Fi** (alcance insuficiente y consumo incompatible con años de pila) como una red celular convencional. Entre las LPWAN, el criterio decisivo lo da el enunciado: **los sensores de sótano y arqueta** exigen la **penetración en interiores profundos** que caracteriza a **NB-IoT**, que además se beneficia de la cobertura del operador ya desplegada. En 5G, este tipo de tráfico corresponde a la familia **mMTC** (comunicaciones masivas entre máquinas).
  - **La disyuntiva de fondo que hay que enunciar**: **espectro sin licencia frente a espectro licenciado**. **LoRaWAN** permite al Ayuntamiento **desplegar red propia** sin depender de un operador ni pagar por dispositivo, pero **sin garantía de calidad ni de ausencia de interferencias** y asumiendo la operación de las pasarelas. **NB-IoT** ofrece cobertura y calidad **garantizadas por contrato**, pero el servicio —y la dependencia— son del operador. Una respuesta completa señala que **la decisión no es técnica sino de modelo de servicio**, y que cabe una solución mixta.

&nbsp;

- **C4**: (§9.2)

| Actuación | Régimen aplicable |
|----|----|
| **(a) Wi-Fi corporativo** | Banda **ISM de uso común**: basta con respetar las condiciones técnicas y los límites de potencia; **no hace falta título habilitante individual** ni se devenga tasa por reserva. Y como es una **red privada de usuario final** —el Ayuntamiento no la ofrece al público—, **no entra en el art. 13** de la Ley 11/2022 |
| **(b) Wi-Fi de cortesía** | Aquí **sí aparece el art. 13**, porque se estaría prestando un servicio **disponible al público**. Hay que valorar el **principio de inversor privado**, la **separación de cuentas** y los principios de **neutralidad, transparencia, no distorsión de la competencia y no discriminación**, además de la normativa de **ayudas de Estado** (arts. 107 y 108 del TFUE), y en su caso la comunicación al **Registro de operadores**. La respuesta completa distingue los dos supuestos del enunciado: en la **sala de espera** el servicio es claramente **accesorio** a la atención presencial y de escaso riesgo competitivo; en **tres plazas públicas** el análisis es más exigente, y lo prudente es delimitar el servicio (caudal y usos acotados, sin sustituir a la oferta comercial), **documentar esa delimitación** y recabar informe jurídico. Se añaden las obligaciones de **protección de datos** del portal cautivo |
| **(c) Sensores** | Si se opta por **LoRaWAN**, banda de **uso común**: mismo régimen que (a), sin título individual. Si se opta por **NB-IoT**, el Ayuntamiento actúa como **cliente de un operador**, sin obligaciones de espectro propias. En ninguno de los dos casos hay prestación de servicio al público |
| **(d) Radioenlace en banda licenciada** | **Uso privativo del dominio público radioeléctrico**: exige **título habilitante** —autorización individual o concesión, según la banda— otorgado por el **Ministerio** competente, y devenga **tasa por reserva del dominio público radioeléctrico** (título V y título VII de la Ley 11/2022). Fundamento: el art. **85.1** declara que el espectro es **bien de dominio público**, cuya **titularidad y administración corresponden al Estado** |

Conviene cerrar con la observación transversal: en las cuatro actuaciones el Ayuntamiento sigue siendo **responsable del cumplimiento del ENS** sobre sus sistemas, mientras que las obligaciones de **integridad y seguridad de las redes** del **art. 63** —incluida la notificación de incidentes de impacto significativo— pesan sobre **los operadores** que le prestan servicio. Esa exigencia debe trasladarse **por contrato**.

#### Criterios de evaluación

| Criterio | Puntos |
|----|----|
| Tres SSID con su autenticación, cifrado y segmentación correctos | 1,5 |
| Cita correcta de `mp.com.4.2` y del refuerzo R1 aplicable a categoría MEDIA | 1 |
| Justificación de 802.1X por **trazabilidad**, no por preferencia técnica | 0,5 |
| Rechazo razonado de ocultar el SSID y del filtrado MAC | 1 |
| Elección de LPWAN con justificación de la penetración en sótanos y enunciado de la disyuntiva licenciado/no licenciado | 2 |
| Régimen de uso común frente a uso privativo, con cita del art. 85 y de la tasa | 1,5 |
| Aplicación correcta del **art. 13** al wifi de cortesía, distinguiendo sala de espera y plazas públicas | 2 |
| Observación final sobre el reparto de responsabilidades ENS / art. 63 y su traslado contractual | 0,5 |

#### Preguntas tipo test sobre este caso

##### 1. En el supuesto planteado, ¿qué autenticación y cifrado corresponden al SSID corporativo de puestos móviles, tabletas y teléfonos del personal?

- a) WPA3-Personal con una clave compartida por toda la plantilla municipal.
- b) Red abierta con portal cautivo, como la de la sala de espera de la oficina.
- c) WPA3-Enterprise con 802.1X/EAP-TLS contra el directorio municipal.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §7.1, §9.1

Cada actuación queda imputada a un empleado concreto mediante su credencial individual contra el directorio.

##### 2. ¿Por qué no basta en la red corporativa con una clave precompartida, aunque sea larga?

- a) Porque WPA3 prohíbe las claves precompartidas en cualquier red que dé acceso a servicios públicos.
- b) Porque impide saber quién hizo qué, y revocar a una persona obliga a cambiar la clave a todos.
- c) Porque una clave precompartida reduce el caudal de la red a la mitad de la velocidad nominal.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §9.1

802.1X con credencial individual no es una preferencia técnica, sino un requisito de imputabilidad (trazabilidad).

##### 3. ¿Cómo debe configurarse el SSID de cortesía de la sala de espera?

- a) Red abierta con OWE, portal cautivo y aislamiento entre clientes, en una VLAN sin ruta hacia la red municipal.
- b) Red WPA3-Enterprise en la misma VLAN que los puestos, para que el público acceda a los servicios municipales.
- c) Red abierta sin cifrado ni portal, en la VLAN de dispositivos junto a impresoras y pantallas de turnos.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §9.1

OWE cifra aunque la red sea abierta; la VLAN totalmente aislada solo tiene salida directa a internet.

##### 4. ¿Qué medida del ENS respalda que todo lo inalámbrico vaya en un segmento propio, y qué añade su refuerzo R1 en un sistema de categoría MEDIA?

- a) mp.com.4: las comunicaciones inalámbricas van en un segmento separado, y el R1 lo implanta con VLAN, con un mínimo de tres subredes.
- b) mp.if.6: las redes inalámbricas se protegen frente a inundaciones, y el R1 exige ubicar los puntos de acceso en planta alta.
- c) op.exp.1: los puntos de acceso deben estar inventariados, y el R1 exige que el SSID corporativo no se anuncie en la baliza.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §9.1 (mp.com.4.2 y R1)

mp.com.4.2 dice que, si se emplean comunicaciones inalámbricas, será en un segmento separado; el R1 implementa los segmentos con VLAN: usuarios, servicios y administración.

##### 5. El responsable del edificio propone ocultar el SSID y permitir solo las direcciones MAC municipales. ¿Cómo debe valorarse?

- a) Debe aceptarse, porque juntas sustituyen con ventaja al cifrado WPA3 y a la autenticación 802.1X.
- b) Debe aceptarse solo en la red de cortesía, porque en ella el público no puede averiguar el nombre.
- c) Debe rechazarse como protección: el SSID viaja en claro al asociarse y las MAC se copian con facilidad.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §9.1

Son medidas cosméticas que dan una falsa sensación de protección y desplazan la atención de lo que sí protege: WPA3 y 802.1X.

##### 6. ¿Qué enmienda de 802.11 evita que las llamadas de voz sobre wifi del personal se corten al cambiar de punto de acceso?

- a) 802.11w, que protege las tramas de gestión.
- b) 802.11r, que agiliza la itinerancia entre celdas.
- c) 802.11e, que define la calidad de servicio WMM.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §7.1

La itinerancia rápida de 802.11r es esencial para la voz sobre wifi; 802.11w neutraliza los ataques de desautenticación.

##### 7. ¿Qué tecnología conviene para los sensores situados en sótanos y arquetas?

- a) Wi-Fi, desplegando puntos de acceso cerca de cada sensor.
- b) Una red celular convencional, con una línea de datos por sensor.
- c) NB-IoT, por su penetración en interiores profundos.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §7.2

Son el caso canónico de LPWAN: pocos datos, mucho alcance y años de batería. Entre las LPWAN, NB-IoT aporta la penetración en interiores profundos y la cobertura del operador ya desplegada.

##### 8. ¿Cuál es la disyuntiva de fondo entre LoRaWAN y NB-IoT para los sensores del distrito?

- a) Espectro sin licencia y red propia sin garantías, frente a espectro licenciado con calidad contratada al operador.
- b) Cobertura en interiores frente a cobertura en exteriores, porque LoRaWAN solo funciona dentro de los edificios.
- c) Bajo consumo frente a alto consumo, porque NB-IoT exige alimentación de red eléctrica en cada sensor.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §7.2

LoRaWAN permite red propia sin pagar por dispositivo, pero sin garantía y asumiendo la operación; NB-IoT garantiza calidad por contrato, con dependencia del operador. Es una decisión de modelo de servicio.

##### 9. ¿Qué régimen jurídico tiene el radioenlace propio en banda licenciada entre la oficina y el polideportivo?

- a) Uso común, como el Wi-Fi: basta con respetar los límites de potencia, sin título ni tasa.
- b) Uso privativo: título habilitante del Ministerio y tasa por reserva del dominio radioeléctrico.
- c) Ninguno, porque el Ayuntamiento es Administración y no necesita títulos para usar el espectro.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §9.2 (art. 85.1 y títulos V y VII Ley 11/2022)

El espectro es bien de dominio público cuya titularidad y administración corresponden al Estado (art. 85.1); su uso privativo exige autorización individual o concesión y devenga tasa.

##### 10. ¿Por qué el Wi-Fi de cortesía queda sujeto al artículo 13 de la Ley 11/2022 y el corporativo no?

- a) Porque el de cortesía presta un servicio disponible al público, y el corporativo es una red privada de usuario final.
- b) Porque el de cortesía usa banda licenciada, y el corporativo, una banda ISM de uso común sin título habilitante.
- c) Porque el de cortesía carece de cifrado, y el artículo 13 regula la seguridad de las redes inalámbricas abiertas.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 4 · §9.2 (art. 13 Ley 11/2022)

Al ofrecer el servicio al público hay que valorar el principio de inversor privado, la no distorsión de la competencia y las ayudas de Estado; en las plazas públicas el análisis es más exigente que en la sala de espera.

## Fuentes

### Tier 1 — Normativa, estándares y teoría canónica

| ID | Referencia |
|----|----|
| `[LGT]` | [Ley **11/2022, de 28 de junio, General de Telecomunicaciones**](https://www.boe.es/buscar/act.php?id=BOE-A-2022-10757) (BOE núm. 155, de 29 de junio de 2022; en vigor desde el 30 de junio de 2022). **8 títulos, 114 artículos, 30 disposiciones adicionales, 7 transitorias, 1 derogatoria, 6 finales y 3 anexos**. Art. 2 (servicios de interés general), art. 3 (objetivos), art. 4 (servicios de telecomunicaciones para la seguridad nacional, la defensa, la seguridad pública, la seguridad vial y la protección civil: **los únicos que son servicio público**), art. 13 (redes y servicios prestados por las Administraciones públicas), arts. 35-43 (obligaciones de servicio público; **art. 37** servicio universal), arts. 44-55 (derechos de ocupación e infraestructuras), art. 58 (secreto de las comunicaciones), art. 60 (protección de datos), art. 62 (cifrado), **art. 63** (integridad y seguridad de las redes), arts. 85-97 (**dominio público radioeléctrico**), arts. 98-100 (administración de las telecomunicaciones y **CNMC**), **anexo II** (definiciones) y **anexo III** (conjunto mínimo de servicios del servicio universal). Texto consolidado del BOE. |
| `[ENS]` | [Real Decreto **311/2022, de 3 de mayo**](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191), por el que se regula el **Esquema Nacional de Seguridad** (BOE núm. 106, de 4 de mayo de 2022). En este tema se citan del anexo II: **`mp.com.1`** perímetro seguro, **`mp.com.2`** protección de la confidencialidad (dimensión C), **`mp.com.3`** protección de la integridad y de la autenticidad (dimensiones I y A) y **`mp.com.4`** separación de flujos de información en la red (con sus refuerzos R1 VLAN, R2 VPN, R3 medios físicos y R4 puntos de interconexión), además de `op.acc.5`, `op.mon.1` y `mp.if.1`. Ver Tema 39. |
| `[UIT-R]` | **Unión Internacional de Telecomunicaciones**, Sector de Radiocomunicaciones. **Reglamento de Radiocomunicaciones** y Recomendación **UIT-R V.431** (nomenclatura de las bandas de frecuencias: de VLF a EHF, en bandas decádicas). La UIT es el organismo especializado de Naciones Unidas para las telecomunicaciones y la autoridad de atribución internacional del espectro; sus Conferencias Mundiales de Radiocomunicaciones (**CMR**) revisan las atribuciones. |
| `[UIT-T]` | **UIT**, Sector de Normalización. Recomendaciones **G.703** y **G.704** (jerarquía plesiócrona: **E0 = 64 kbit/s**, **E1 = 2,048 Mbit/s** con **32 intervalos de tiempo**), **G.707** (jerarquía digital síncrona, **SDH**: STM-1 = 155,52 Mbit/s), **G.652** y **G.657** (fibra óptica monomodo), **G.984** (**GPON**) y **G.9807.1** (**XGS-PON**), serie **V** (interfaces de módem sobre línea telefónica), serie **X** (**X.25**, **X.21**) y serie **I** (RDSI). |
| `[SHANNON]` | Shannon, C. E. *A Mathematical Theory of Communication*, Bell System Technical Journal, 1948. Modelo canónico de sistema de comunicación (fuente, transmisor, canal con ruido, receptor, destino) y **teorema de la capacidad del canal ruidoso**: `C = B · log₂(1 + S/N)`. |
| `[NYQUIST]` | Nyquist, H. *Certain Topics in Telegraph Transmission Theory*, 1928, y Shannon, C. E. (1949). **Capacidad de un canal sin ruido**: `C = 2 · B · log₂(M)`. **Teorema del muestreo**: la frecuencia de muestreo debe ser **al menos el doble** de la frecuencia máxima de la señal (`fm ≥ 2·fmax`). |
| `[IEEE802.3]` | IEEE **802.3**. Ethernet. Familias **10BASE-T**, **100BASE-TX**, **1000BASE-T**, **10GBASE-T** sobre par trenzado y **1000BASE-SX/LX**, **10GBASE-SR/LR** y superiores sobre fibra; límite de **100 m** del enlace de cobre. **802.3af** (PoE, 15,4 W), **802.3at** (PoE+, 30 W) y **802.3bt** (PoE++ o 4PPoE, hasta **90-100 W** en el equipo fuente). Ver Tema 37. |
| `[IEEE802.11]` | IEEE **802.11**. Redes de área local inalámbricas. Enmiendas **a**, **b**, **g**, **n** (Wi-Fi 4), **ac** (Wi-Fi 5), **ax** (Wi-Fi 6 y 6E) y **be** (**Wi-Fi 7**, *Extremely High Throughput*, **publicada el 22 de julio de 2025**); **802.11i** (WPA2), **802.11e** (calidad de servicio), **802.11r** (traspaso rápido), **802.11k/v** (gestión de radio y de itinerancia) y **802.11s** (malla). En desarrollo: **802.11bn** (**Wi-Fi 8**, *Ultra High Reliability*), con publicación prevista en **2028**. Acceso al medio **CSMA/CA** con **DCF**. |
| `[IEEE802.1]` | IEEE **802.1**. **802.1Q** (VLAN y etiquetado de tramas), **802.1D** y **802.1w** (**STP** y **RSTP**, prevención de bucles de nivel 2), **802.1s** (MSTP), **802.1X** (control de acceso a red basado en puertos, base del Wi-Fi empresarial), **802.1AX** (agregación de enlaces) y **802.1AB** (**LLDP**, descubrimiento de vecinos). |
| `[IEEE802.15]` | IEEE **802.15**. Redes de área personal inalámbricas: **802.15.1** (base histórica de **Bluetooth**), **802.15.4** (capa física y de acceso al medio de **Zigbee**, **Thread** y **6LoWPAN**) y **802.15.6** (redes de área corporal). |
| `[IEEE802.16]` | IEEE **802.16**. **WiMAX**, red de área metropolitana inalámbrica de banda ancha. Perfil fijo (802.16d, 2004) y móvil (**802.16e**, 2005). Tecnología hoy **residual** en Europa, desplazada por LTE y 5G, pero de cita obligada al clasificar las redes inalámbricas por cobertura. |
| `[BT-CORE]` | **Bluetooth SIG**. *Bluetooth Core Specification*. Banda **ISM de 2,4 GHz**, **salto en frecuencia adaptativo (AFH)**, topología en **piconet** (un maestro y hasta **siete** esclavos activos) y **scatternet**; clases de potencia y alcance; **BR/EDR** frente a **Bluetooth LE**. Versiones **5.x** (mayor alcance y velocidad en LE, radiobalizas y **LE Audio** con el códec **LC3** desde la 5.2) y **6.x** (**Channel Sounding**, medición precisa de distancia); versión vigente del núcleo en agosto de 2026: **6.3**, publicada el 6 de mayo de 2026. |
| `[ISO-NFC]` | **ISO/IEC 18092** (NFCIP-1) e **ISO/IEC 14443** (tarjetas de proximidad). **NFC**: **13,56 MHz**, alcance operativo **≈ 10 cm**, modos lectura/escritura, emulación de tarjeta y **punto a punto**. |
| `[ISO11801]` | **ISO/IEC 11801** y su equivalente europeo **UNE-EN 50173**. Cableado estructurado genérico: subsistemas, **categorías** de cable de par trenzado (**Cat 5e, 6, 6A, 7, 7A y 8**) y **clases** de enlace (D, E, EA, F, FA, I y II), longitudes máximas y parámetros de certificación. Equivalente estadounidense: **ANSI/TIA-568**. |
| `[OM-OS]` | **ISO/IEC 11801** y **TIA-492**. Designación de fibras **multimodo OM1, OM2, OM3, OM4 y OM5** (núcleo de 62,5 o **50 µm**) y **monomodo OS1 y OS2** (núcleo **≈ 9 µm**). Ventanas de trabajo en **850 nm**, **1.310 nm** y **1.550 nm**. |
| `[RFC791]` | IETF. *[RFC 791](https://www.rfc-editor.org/rfc/rfc791): Internet Protocol* y **[RFC 919](https://www.rfc-editor.org/rfc/rfc919)/922** (difusión en IPv4: **255.255.255.255** limitada y difusión dirigida a subred). Ver Tema 34. |
| `[RFC1112]` | IETF. *[RFC 1112](https://www.rfc-editor.org/rfc/rfc1112): Host Extensions for IP Multicasting* y **[RFC 3376](https://www.rfc-editor.org/rfc/rfc3376)** (**IGMPv3**). Multidifusión IPv4 en el rango **224.0.0.0/4** y su correspondencia con las direcciones MAC **01:00:5E:…**. |
| `[RFC4291]` | IETF. *[RFC 4291](https://www.rfc-editor.org/rfc/rfc4291): IP Version 6 Addressing Architecture*. IPv6 define **unidifusión**, **multidifusión** y **anydifusión** (*anycast*) y **suprime la difusión**; el grupo `ff02::1` (todos los nodos del enlace) hace sus veces. Suscripción con **MLD** ([RFC 3810](https://www.rfc-editor.org/rfc/rfc3810)). |
| `[RFC826]` | IETF. *[RFC 826](https://www.rfc-editor.org/rfc/rfc826): An Ethernet Address Resolution Protocol* (**ARP**). Ejemplo canónico de uso legítimo de la difusión de nivel 2 (`FF:FF:FF:FF:FF:FF`). Ver Tema 34. |
| `[3GPP]` | **3GPP** (*3rd Generation Partnership Project*). Especificaciones de **GSM/GPRS/EDGE**, **UMTS/HSPA**, **LTE/LTE-Advanced** y **5G NR**. Arquitectura del **núcleo de red 5G (5GC)** basada en servicios, **separación entre plano de control y plano de usuario (CUPS)**, ***network slicing*** y modos de despliegue **NSA** (no autónomo, apoyado en el núcleo 4G) y **SA** (autónomo). |
| `[UIT-IMT]` | **UIT-R**, recomendaciones **IMT-2000** (3G), **IMT-Advanced** (4G) e **IMT-2020** (5G). IMT-2020 define las tres familias de casos de uso —**eMBB**, **URLLC** y **mMTC**— y los objetivos de **20 Gbit/s** de pico descendente, **1 ms** de latencia en la interfaz radio y **10⁶ dispositivos/km²**. Marco **IMT-2030** para 6G en elaboración. |
| `[ETSI-TETRA]` | **ETSI EN 300 392**. **TETRA** (*TErrestrial Trunked RAdio*). Radio móvil profesional troncal, digital, con **modo semidúplex** de pulsar para hablar, comunicaciones de **grupo**, llamada de **emergencia** con prioridad y **modo directo** sin infraestructura. Es el objeto del **Tema 38**. |
| `[RD391-2019]` | [Real Decreto **391/2019, de 21 de junio**](https://www.boe.es/buscar/act.php?id=BOE-A-2019-9513), por el que se aprueba el **Plan Técnico Nacional de la Televisión Digital Terrestre** y se regulan determinados aspectos para la **liberación del segundo dividendo digital**. Libera la banda de **694-790 MHz (banda de 700 MHz)** para comunicaciones móviles de banda ancha; la migración de la TDT debía completarse antes del **31 de octubre de 2020**. La banda **470-694 MHz** queda garantizada para TDT **al menos hasta 2030**. |
| `[L13-2022]` | [Ley **13/2022, de 7 de julio, General de Comunicación Audiovisual**](https://www.boe.es/buscar/act.php?id=BOE-A-2022-11311) (en vigor desde el 9 de julio de 2022; deroga la [Ley 7/2010](https://www.boe.es/buscar/act.php?id=BOE-A-2010-5292)). Marco de los servicios de comunicación audiovisual y de las plataformas de intercambio de vídeos; define el **múltiple digital o múltiplex** como la señal compuesta transmitida en una frecuencia que, mediante tecnología digital, permite incorporar las señales de **varios** servicios de comunicación audiovisual y de comunicaciones electrónicas. |
| `[REG2015-2120]` | [Reglamento (UE) **2015/2120**](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32015R2120), por el que se establecen medidas en relación con el **acceso a una internet abierta** (neutralidad de la red: tratamiento equitativo del tráfico, prohibición de bloqueo y estrangulamiento salvo excepciones tasadas, y régimen de los servicios especializados). Modificado por el [Reglamento (UE) **2022/612**](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32022R0612) sobre **itinerancia** en la Unión. |
| `[RD346-2011]` | [Real Decreto **346/2011, de 11 de marzo**](https://www.boe.es/buscar/act.php?id=BOE-A-2011-5834), por el que se aprueba el Reglamento regulador de las **infraestructuras comunes de telecomunicaciones (ICT)** para el acceso a los servicios de telecomunicación en el interior de las edificaciones, dictado en desarrollo de lo que hoy es el **art. 55** de la [Ley 11/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-10757). |
| `[L40-2015]` | [Ley **40/2015, de 1 de octubre**](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566), de Régimen Jurídico del Sector Público. **Art. 156**: Esquema Nacional de Interoperabilidad y Esquema Nacional de Seguridad. Fundamento legal del ENI y del ENS, y marco de las redes de comunicaciones de las Administraciones. Ver Tema 39. |

### Tier 2 — Manuales de referencia y documentación técnica sectorial

| ID | Referencia |
|----|----|
| `[TANENBAUM]` | Tanenbaum, A. S. y Wetherall, D. J. *Computer Networks*, 5.ª ed. Manual canónico: capa física, medios de transmisión, conmutación de circuitos frente a paquetes, redes inalámbricas y satélite. |
| `[STALLINGS]` | Stallings, W. *Data and Computer Communications*, 10.ª ed. Referencia clásica para transmisión de datos, codificación, multiplexación, control de errores y de flujo. |
| `[KUROSE]` | Kurose, J. F. y Ross, K. W. *Computer Networking: A Top-Down Approach*, 8.ª ed. Enfoque descendente; capítulos de capa de enlace, redes locales inalámbricas y móviles. |
| `[FOROUZAN]` | Forouzan, B. A. *Data Communications and Networking*, 5.ª ed. Especialmente útil por su tratamiento sistemático de modos de transmisión, topologías y multiplexación. |
| `[WIFI-ALLIANCE]` | **Wi-Fi Alliance**. Programas de certificación y nomenclatura comercial de generaciones (**Wi-Fi 4** a **Wi-Fi 7**), **Wi-Fi 6E** para la banda de **6 GHz**, y certificaciones de seguridad **WPA2**, **WPA3** (con **SAE** y **OWE**) y **Wi-Fi Enhanced Open**. |
| `[GSMA]` | **GSMA**. Documentación de referencia del ecosistema móvil: evolución 2G-5G, arquitectura de itinerancia, **eSIM** y estado de despliegue de **5G SA**. |
| `[LORA]` | **LoRa Alliance**. Especificación **LoRaWAN**: clases A, B y C de dispositivo final, bandas ISM sin licencia (**868 MHz** en Europa), arquitectura de estrella de estrellas con pasarelas y servidor de red. Contrapunto con **NB-IoT** y **LTE-M**, que sí usan espectro licenciado (3GPP). |
| `[CCN-STIC-816]` | **Centro Criptológico Nacional**. Guías de la serie 800 aplicables a redes: **CCN-STIC-816** (seguridad en redes inalámbricas en el marco del ENS), **CCN-STIC-807** (criptología de empleo en el ENS) y guías de bastionado de electrónica de red de las series 500 y 600. |
| `[ONTSI]` | Observatorio Nacional de Tecnología y Sociedad y **Ministerio para la Transformación Digital y de la Función Pública**. Informes de cobertura de banda ancha y datos de despliegue de fibra hasta el hogar y de 5G en España; programas **UNICO** de extensión de banda ancha. |
| `[RED-SARA]` | **Red SARA** (Sistemas de Aplicaciones y Redes para las Administraciones). Red de interconexión de las Administraciones públicas españolas, gestionada por la Secretaría General de Administración Digital; sustrato de comunicaciones de los servicios comunes de administración electrónica. Contexto del Tema 39. |

### Tier 3 — Contexto administrativo municipal (no citado como contenido técnico)

| ID | Referencia |
|----|----|
| `[BOAM-10032]` | Bases específicas de la convocatoria de Técnico Auxiliar de Informática del Ayuntamiento de Madrid (BOAM 10.032). **Enunciado oficial del Tema 33** y de los temas con los que limita: **T30**, **T34**, **T35**, **T36**, **T37**, **T38** y **T39**. |
| `[IAM]` | **Informática del Ayuntamiento de Madrid (IAM)**, organismo autónomo responsable de los sistemas y las comunicaciones municipales. Contexto de los ejemplos y de los tres casos prácticos: red municipal, sedes de distrito, oficinas de atención a la ciudadanía y despliegues inalámbricos en edificios municipales. |
| `[MADRID-DIGITAL]` | Portal de transparencia y sede electrónica del Ayuntamiento de Madrid. Contexto de los servicios municipales citados en los ejemplos (sede electrónica, Padrón, tramitación de expedientes). |
