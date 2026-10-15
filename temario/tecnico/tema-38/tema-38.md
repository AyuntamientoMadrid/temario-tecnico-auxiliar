# Tema 38. El sistema de radiocomunicación TETRA

**Bloque:** técnico  
**Enunciado oficial** (BOAM n.º 10.032, de 23 de diciembre de 2025): Sistema de radiocomunicación Trans European Trunked Radio o TEerrestrial Trunked RAdio (TETRA).

Versión web: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-38.html> · PDF: [tema-38.pdf](tema-38.pdf) · Test: [../../../tests/tecnico/tema-38.md](../../../tests/tecnico/tema-38.md)

## Índice

- 1. Introducción y fundamentos de los sistemas móviles de radiocomunicación
  - 1.1. Concepto y evolución de la radiocomunicación móvil privada (PMR)
  - 1.2. Sistemas trunked o troncalizados: concepto y ventajas
  - 1.3. Estandarización de TETRA por el ETSI: Trans European / Terrestrial Trunked Radio
- 2. Arquitectura y componentes de la red TETRA
  - 2.1. Infraestructura de conmutación y gestión (SwMI)
  - 2.2. Terminales de usuario
  - 2.3. Interfaces estándar de TETRA
- 3. Capa física y transmisión radio en TETRA
  - 3.1. Espectro radioeléctrico y asignación de frecuencias
  - 3.2. Técnica de acceso múltiple por división de tiempo (TDMA)
  - 3.3. Modulación digital π/4-DQPSK
  - 3.4. Estructura de trama radio y canales lógicos
- 4. Servicios y seguridad en sistemas TETRA
  - 4.1. Servicios de voz y comunicaciones de grupo
  - 4.2. Servicios de datos
  - 4.3. Mecanismos de seguridad
- 5. Ámbito público, normativa y evolución tecnológica
  - 5.1. Uso de TETRA en servicios de emergencia y seguridad pública
  - 5.2. Marco normativo y regulación del espectro radioeléctrico
  - 5.3. Requisitos de disponibilidad, resiliencia y calidad de servicio (QoS)
  - 5.4. Evolución hacia TEDS y coexistencia con redes de banda ancha crítica
- Los ocho datos que no se pueden fallar

### Conceptos clave para memorizar

| Concepto | Dato clave |
|----|----|
| Significado de las siglas | **TE**rrestrial **TRA**nked **RA**dio (nombre actual). El original fue *Trans European Trunked Radio*, cambiado por el ETSI cuando el estándar dejó de ser solo europeo |
| Organismo que lo normaliza | **ETSI** (European Telecommunications Standards Institute). Serie **EN 300 392** (V+D), **EN 300 396** (DMO), **EN 300 394** (conformidad), **EN 300 395** (códec de voz) |
| Acceso al medio | **FDMA + TDMA**: portadoras de **25 kHz** con **4 intervalos de tiempo** (*time slots*) por portadora |
| Modulación (Release 1) | **π/4-DQPSK**, **18.000 símbolos/s**, 2 bits por símbolo → **36 kbit/s** brutos por portadora |
| Duración del intervalo | **14,167 ms** · trama = 4 intervalos = **56,67 ms** · multitrama = 18 tramas = **1,02 s** · hipertrama = 60 multitramas = **61,2 s** |
| Trama de control | La **trama 18** de cada multitrama se reserva para señalización (*control frame*) |
| Códec de voz | **ACELP**, **137 bits cada 30 ms** = **4,567 kbit/s** netos; **7,2 kbit/s** por intervalo con protección de errores |
| Radio de célula máximo | **58 km** en TETRA Release 1 (límite impuesto por la estructura de intervalos) |
| Bandas en España (emergencias) | **380-385 / 390-395 MHz**, reservadas por la **nota UN-28** del CNAF a las FCSE y a los servicios de emergencia |
| Bandas en España (TETRA civil) | **410-415,3 / 420-425,3 MHz**, que la **nota UN-31** destina literalmente a «sistemas digitales de acceso aleatorio de canales (**TETRA** y otros)» con canalización de 25 kHz y separación dúplex de **10 MHz** |
| CNAF vigente | **Orden TDF/732/2026, de 10 de julio** (BOE núm. 173, de 17-7-2026). **Sustituye** a la Orden ETD/1449/2021 con efectos de **18 de julio de 2026** |
| Título habilitante de un ayuntamiento | **Afectación demanial** — art. **88.5.b)** de la Ley 11/2022: la autorización individual para autoprestación no vale para las Administraciones públicas |
| Modos de operación | **TMO** (a través de la infraestructura) y **DMO** (terminal a terminal, sin red) |
| Elementos que amplían el DMO | **DM-REP** (repetidor, tipo 1A, 1B o 2) y **DM-GATE** (pasarela hacia la red V+D); el **DM-REP/GATE** hace las dos cosas |
| Interfaces normalizadas | **I1** aire (TMO) · **I2** línea (LSI/LNI) · **I3** **ISI** entre sistemas · **I4** terminal (**PEI**) · **I5** gestión de red · **I6** aire en modo directo |
| Tiempo de establecimiento | **\< 300 ms** en llamada de grupo, frente a varios segundos en telefonía celular |
| Cifrado de interfaz aire | Clases de seguridad **SC1** (sin cifrar) · **SC2** (clave estática **SCK**) · **SC3** (clave derivada **DCK** + **CCK**), con la variante **SC3G** cuando se usa **GCK** |
| Algoritmos de cifrado | **TEA set A**: TEA1-TEA4 (2 de exportación libre, 2 restringidos). **TEA set B**: **TEA5, TEA6 y TEA7** (octubre de 2022), con claves extendidas y autenticación **TAA2** |
| Vulnerabilidades publicadas | **TETRA:BURST** (agosto de 2023, 5 CVE; **TEA1 con clave reducida a ~32 bits**) y **2TETRA:2BURST** (7 de agosto de 2025, Black Hat USA), que alcanza al **cifrado extremo a extremo** |
| Datos de banda ancha | **TEDS** (TETRA Release 2): canales de **25, 50, 100 y 150 kHz** con π/8-D8PSK, 4-QAM, 16-QAM y 64-QAM |
| Evolución | **MCPTT**, normalizado por el **3GPP en la Release 13** (2016); banda **700 MHz** para PPDR de banda ancha en el CNAF |
| La red del Estado NO es TETRA | **SIRDEE** usa **TETRAPOL** (FDMA, 12,5 kHz, GMSK), no TETRA. Es la confusión más penalizada del tema |

## Contenido

### Convenciones del documento

Este tema incluye cuatro tipos de **cajas callout** para facilitar el estudio:

> **Dato clave.** Información de alta densidad memorística: cifras de la capa física, siglas, números de norma, bandas de frecuencia y preceptos legales.

> **Ejercicio resuelto.** Problema con solución paso a paso: calcular una capacidad, dimensionar una cobertura, decidir un modo de operación, leer una tabla del CNAF.

> **Ejemplo de aplicación en el ayto.** Aplicación real de la teoría al entorno municipal (la red DIMETRA-TETRA del Ayuntamiento, el CISEM, la Policía Municipal, SAMUR-Protección Civil, Bomberos y el IAM).

> **Relación con otros temas.** Enlace conceptual a otros temas del temario oficial.

**Aviso sobre el enunciado, y conviene empezar por él.** El título oficial de este tema es el único de los cuarenta que se dedica **a un solo sistema concreto**. Los demás temas técnicos describen familias de tecnologías —sistemas operativos, bases de datos, redes locales—; aquí se pide **una tecnología con nombre propio, un fabricante de norma con nombre propio (el ETSI) y un conjunto cerrado de especificaciones**. Eso tiene dos consecuencias prácticas para quien estudia:

1.  **El tema exige retener el detalle numérico.** En un tema de «redes locales» el número exacto de bits de una ráfaga es secundario; en un tema de TETRA son datos centrales cuántos intervalos hay por portadora, cuánto dura una multitrama o qué banda reserva el CNAF a los servicios de emergencia. **Este es un tema de datos exactos.**
2.  **El enunciado incluye la traducción de las siglas y lo hace mal a propósito.** Dice «*Trans European Trunked Radio* **o** *TErrestrial Trunked RAdio*» porque **ambas expansiones han sido oficiales en momentos distintos**, y conviene saber cuál es la vigente y por qué cambió. Se explica en §1.3.

**Fronteras con otros temas.** TETRA toca materias que el temario reparte en otros enunciados. El criterio seguido aquí es el siguiente:

| Materia | Dónde se estudia | Qué se hace en este tema |
|----|----|----|
| Medios de transmisión, modos de comunicación, comunicaciones móviles e inalámbricas en general | **Tema 33** | Se da por sabido. Aquí se aplica a un sistema concreto |
| Modelo OSI y pila TCP/IP | **Tema 34** | Solo se usa para situar las tres capas del interfaz aire de TETRA y el transporte de datos IP |
| Redes locales, tipología, técnicas de transmisión y métodos de acceso | **Tema 37** | El **acceso múltiple** (FDMA, TDMA) se explica aquí en lo que TETRA lo usa, no como teoría general |
| Seguridad perimetral, acceso remoto seguro y VPN | **Tema 36** | Aquí solo la seguridad **propia del interfaz aire** de TETRA y el cifrado extremo a extremo |
| Criptografía, firma electrónica y amenazas | **Tema 32** | Se dan por sabidos los conceptos de clave simétrica, autenticación y AES |
| Principios del ENS y del ENI | **Tema 39** | Aquí se citan las medidas concretas que un servicio de radio crítico debe cumplir |
| Videoconferencia y trabajo en grupo | **Tema 40** | Fuera de alcance |

**Y la advertencia que más puntos cuesta.** La red de radiocomunicaciones de emergencia **del Estado español**, el **SIRDEE**, **no es una red TETRA**: está construida sobre **TETRAPOL**, una tecnología distinta, propietaria en su origen, de acceso **FDMA** y canalización de **12,5 kHz**. Quien confunda ambas cosas responderá mal cualquier pregunta que cruce «TETRA» con «Fuerzas y Cuerpos de Seguridad del Estado». Se desarrolla en §5.1, y la comparación técnica está en §3.2.

Las fuentes se citan con etiquetas breves tipo `[EN392-2]`, `[CNAF]` o `[ENS]`; el registro completo está en la pestaña Fuentes. **Las bandas de frecuencia y los preceptos legales de este tema se han verificado sobre el PDF del BOE**, no sobre fuentes secundarias, y de esa verificación salió un dato que casi ningún material recoge todavía: **el Cuadro Nacional de Atribución de Frecuencias vigente ya no es el de 2021**.

**Caso de referencia usado en todo el tema** (contexto Ayuntamiento de Madrid, supuesto simplificado): la **red DIMETRA-TETRA municipal**, gobernada desde el **Centro Integrado de Seguridad y Emergencias (CISEM)** de la calle Rufino Blanco, que da servicio a Policía Municipal, Bomberos, SAMUR-Protección Civil, Agentes de Movilidad, SAMUR Social y Parques y Jardines. Ese sistema único concentra todas las materias del tema: tiene **estaciones base y una infraestructura de conmutación** (§2), ocupa **espectro atribuido por el CNAF** (§3.1 y §5.2), transporta **voz de grupo y datos** (§4.1 y §4.2), está **cifrado y autenticado** (§4.3), debe **seguir funcionando cuando todo lo demás falla** (§5.3) y tiene por delante una **transición hacia la banda ancha crítica** (§5.4).

------------------------------------------------------------------------

### 1. Introducción y fundamentos de los sistemas móviles de radiocomunicación

#### 1.1. Concepto y evolución de la radiocomunicación móvil privada (PMR)

**Qué es la PMR y en qué se diferencia de un teléfono móvil.** La **radiocomunicación móvil privada** —**PMR**, del inglés *Private Mobile Radio*, también llamada *Professional Mobile Radio* y, en Estados Unidos, *Land Mobile Radio* (**LMR**)— es el conjunto de sistemas de radio diseñados para que **un colectivo cerrado de usuarios profesionales** se comunique entre sí, normalmente **en grupo**, sobre una red **propia** o dedicada. La diferencia con la telefonía celular pública no es de tecnología sino de **finalidad**, y de ella se derivan todas las decisiones de diseño:

- **La unidad de comunicación es el grupo, no el par.** En telefonía, lo natural es que A llame a B. En PMR, lo natural es que un agente hable **a todos los que están en su grupo** —una patrulla, una dotación de bomberos, el turno de una oficina—, que escuchan simultáneamente. La llamada individual existe, pero es la excepción.
- **La comunicación es *push-to-talk* y semidúplex.** Se aprieta un botón, se habla y se suelta; mientras uno habla, los demás escuchan. Esto no es una limitación: es lo que permite que un mando **oiga a todos sus efectivos** y que todos oigan lo que se ordena.
- **El establecimiento debe ser inmediato.** En una emergencia, esperar cinco segundos a que se establezca una llamada es inaceptable. El objetivo de diseño es **menos de 300 milisegundos**.
- **La red es propia y su disponibilidad es un requisito, no una expectativa.** El operador de una red PMR decide dónde pone las estaciones base, cuánta batería les instala y a quién da prioridad. Una red pública no ofrece ninguna de esas tres cosas.
- **El terminal es un instrumento de trabajo, no un objeto de consumo.** Robusto, con botón de emergencia, manejable con guantes, con autonomía de una jornada larga y audible en un entorno ruidoso.

> **Dato clave.** Las cuatro diferencias que definen la PMR frente a la telefonía celular pública: **(1) comunicación de grupo** como modo principal, **(2)** *push-to-talk* **semidúplex**, **(3) establecimiento de llamada inferior a 300 ms** y **(4) red propia con disponibilidad y prioridad garantizadas por su titular**. A ellas se añade una quinta, propia de los sistemas digitales modernos: **(5) funcionamiento sin infraestructura** (modo directo), imposible en telefonía celular.

**Las cuatro generaciones de la PMR.** La evolución de estos sistemas se cuenta bien en cuatro etapas, y cada una resuelve el problema que la anterior dejaba abierto.

**Primera etapa: la radio analógica convencional (desde los años treinta).** Cada colectivo tiene asignado **un canal fijo**, es decir, una pareja de frecuencias. Todos los equipos del colectivo están sintonizados en él permanentemente. La modulación es **analógica** —AM primero, **FM** después— y el sistema es de una sencillez absoluta: si el canal está libre, se habla; si está ocupado, se espera. Las limitaciones son igual de evidentes: **el canal está asignado aunque nadie hable** (el espectro se desperdicia), **no hay privacidad** (cualquiera con un receptor escucha), **no hay identificación** del que habla más allá de su voz y **no hay forma de hablar con otro colectivo** que esté en otro canal.

**Segunda etapa: el *trunking* analógico (años setenta y ochenta).** Se introduce la idea que da nombre al tema y que se explica en §1.2: en lugar de asignar un canal fijo a cada grupo, se crea una **bolsa común de canales** que el sistema reparte dinámicamente entre todos los grupos según quien vaya necesitando hablar. Aparecen sistemas como **MPT-1327**, norma británica que se difundió por Europa. Se gana muchísima eficiencia espectral, pero la voz sigue siendo analógica, con sus mismos problemas de calidad, privacidad e integración con datos.

**Tercera etapa: el *trunking* digital (años noventa).** La voz se **digitaliza** con un códec de baja tasa, y con ella llegan tres cosas que la radio analógica no podía dar: **cifrado real**, **integración de voz y datos** en la misma portadora y **mayor eficiencia espectral** —varios canales de conversación en el mismo ancho de banda—. Es la etapa en la que nacen **TETRA** en Europa (ETSI), **TETRAPOL** en Francia y **APCO Project 25 (P25)** en Estados Unidos, y algo más tarde **DMR** (*Digital Mobile Radio*), también del ETSI, para el segmento profesional de menor exigencia.

**Cuarta etapa: la banda ancha crítica (desde 2016).** Las funciones de misión crítica —el *push-to-talk* de grupo, la prioridad, el desalojo, el modo directo— se llevan a redes de **banda ancha** basadas en LTE y 5G mediante los estándares **MCPTT**, **MCData** y **MCVideo** del **3GPP**. No sustituyen a TETRA de un día para otro: conviven con él durante años. Se desarrolla en §5.4.

> **Dato clave.** Secuencia de las cuatro etapas de la PMR: **analógica convencional → *trunking* analógico (MPT-1327) → *trunking* digital (TETRA, TETRAPOL, P25, DMR) → banda ancha crítica (MCPTT del 3GPP)**. TETRA pertenece a la **tercera**. Conviene saber situar TETRA en esta escala e identificar el sistema **analógico** de la segunda: es **MPT-1327**, no TETRA.

**Un matiz de vocabulario.** Junto a **PMR** aparece **PAMR** (*Public Access Mobile Radio*): es la misma tecnología, pero explotada por **un operador comercial** que vende el servicio a terceros, en lugar de por el propio colectivo usuario. La distinción es jurídica más que técnica y tiene consecuencias directas en el título habilitante que hace falta para usar el espectro (§5.2). En el CNAF español ambas aparecen juntas, como «**sistemas móviles digitales de banda estrecha PMR/PAMR**» `[CNAF]`.

> **Relación con otros temas.** El **Tema 33** («Comunicaciones… comunicaciones móviles e inalámbricas») presenta el panorama general de los sistemas móviles, incluida la telefonía celular. Este tema **no repite** esa panorámica: entra directamente en el sistema que el enunciado nombra. Los conceptos de modulación digital y de multiplexación que aquí se dan por conocidos están en el **Tema 33**; los de capa física y capa de enlace, en el **Tema 34**.

**Dónde se usa hoy la PMR digital.** Conviene tener presente el mapa de usuarios, porque explica por qué el estándar tiene las funciones que tiene: **seguridad pública** (policía, bomberos, emergencias sanitarias, protección civil), **transporte** (metros, ferrocarriles, aeropuertos, puertos, autobuses urbanos, taxis), **energía y agua** (redes eléctricas, gasistas, empresas de abastecimiento), **industria** (minería, petroquímica, grandes plantas), **defensa** y **grandes eventos y recintos** (estadios, ferias, hospitales, centros comerciales). Según la **TCCA**, TETRA está desplegado en **más de 124 países** `[TCCA-GLOBAL]`.

#### 1.2. Sistemas *trunked* o troncalizados: concepto y ventajas

**El problema que resuelve.** Imaginemos un ayuntamiento con **ocho colectivos** que necesitan radio: policía, bomberos, emergencias sanitarias, movilidad, limpieza, parques, obras y transporte. En un sistema **convencional**, a cada colectivo se le asigna **un canal fijo**: hacen falta ocho canales, y cada canal solo puede usarlo su colectivo. El resultado es doblemente malo: cuando el canal de la policía está saturado, el agente espera **aunque siete canales estén vacíos**; y cuando el canal de parques lleva dos horas en silencio, ese espectro está **inmovilizado** sin que nadie pueda aprovecharlo.

**La solución.** Un sistema **troncalizado** (*trunked*) mantiene los ocho canales, pero **no los asigna a nadie de forma permanente**. Los reúne en una **bolsa común** y los reparte **conversación a conversación**: cuando un agente aprieta el botón, un **canal de control** —una portadora que el sistema dedica exclusivamente a señalización— recibe la petición, comprueba a qué grupo pertenece el usuario, busca un canal de tráfico libre y **se lo asigna solo mientras dura esa transmisión**. Al soltar el botón, el canal **vuelve a la bolsa**.

> **Dato clave.** *Trunking* significa **asignación dinámica de canales bajo demanda desde una bolsa común**, gestionada por un **canal de control** dedicado. La palabra procede de la telefonía: un *trunk* es una **línea troncal** compartida entre muchos abonados. La traducción española normalizada es **«troncalización»** o «concentración de enlaces»; el CNAF usa la expresión «sistemas multicanales de **acceso aleatorio de frecuencias con concentración de enlaces (*trunking*)**» `[CNAF]`.

**Por qué funciona: el efecto de agrupamiento.** La ganancia no es una cuestión de mera comodidad, sino de **teoría de colas**. Un conjunto de recursos compartidos atiende mucha más demanda que la suma de recursos aislados equivalentes, porque los picos de unos coinciden con los valles de otros. Es el mismo principio por el que una cola única ante diez cajeros es más eficiente que diez colas de un cajero cada una. Aplicado a la radio, **ocho canales compartidos entre ocho colectivos dan un grado de servicio muy superior al de un canal dedicado por colectivo**, y permiten atender a **muchos más usuarios** con el mismo espectro.

> **Ejercicio resuelto.** **Comparar la capacidad de un despliegue convencional y uno troncalizado.** Un servicio municipal dispone de **4 portadoras** de 25 kHz en una zona. En **TETRA**, cada portadora se divide en **4 intervalos de tiempo**, de modo que ofrece **4 canales físicos**. La configuración estándar dedica **un intervalo al canal de control principal**. **Planteamiento convencional analógico**: 4 portadoras = **4 canales de voz**, cada uno asignado en exclusiva a un colectivo. Cuatro colectivos servidos, y ninguno puede usar el canal de otro. **Planteamiento troncalizado TETRA**: 4 portadoras × 4 intervalos = **16 canales físicos**; se resta **1** para el canal de control → **15 canales de tráfico simultáneos**, repartidos dinámicamente entre **todos** los colectivos y todos los grupos de conversación que se definan. **Resultado**: con el mismo espectro se pasa de **4 conversaciones simultáneas rígidas** a **15 conversaciones simultáneas flexibles**, casi **cuatro veces más**, y además el número de **grupos** que pueden definirse no está limitado por el número de canales: pueden existir decenas o centenares de grupos de conversación, porque un grupo **solo consume canal mientras alguien habla**. Esa última frase es la clave del modelo.

**Las ventajas del *trunking*, ordenadas.** Conviene memorizarlas como lista cerrada:

1.  **Eficiencia espectral**: se sirve a muchos más usuarios con el mismo número de frecuencias.
2.  **Reducción del tiempo de espera**: la probabilidad de encontrar todos los canales ocupados baja drásticamente respecto al canal dedicado.
3.  **Número de grupos ilimitado en la práctica**: los grupos son una **entidad lógica** del sistema, no una frecuencia física.
4.  **Reconfiguración desde el centro de control**: se pueden crear, modificar o disolver grupos **en caliente** (la función **DGNA**, §4.1.1), algo imposible en radio convencional, donde habría que reprogramar cada equipo.
5.  **Gestión de prioridades**: el sistema sabe quién pide el canal y puede **desalojar** a un usuario de menor prioridad para atender una emergencia (§4.1.2).
6.  **Privacidad y control de acceso**: cada terminal se identifica ante el sistema; el que no está dado de alta no entra.
7.  **Registro y trazabilidad**: toda transmisión queda asociada a una identidad y puede grabarse y auditarse.
8.  **Integración de voz y datos** sobre la misma infraestructura.

**Y los inconvenientes.** El *trunking* introduce **dependencia de la infraestructura**: si cae el canal de control, o cae el nodo de conmutación, el sistema deja de asignar canales. Por eso todos los sistemas troncalizados serios incorporan **modos degradados**: el **repliegue local** (*fallback* o *local site trunking*), en el que una estación base aislada del resto de la red sigue dando servicio troncalizado **dentro de su propia célula**, y el **modo directo** (§2.2.2), en el que los terminales hablan entre sí **sin ninguna infraestructura**. También añade **complejidad y coste**: un sistema troncalizado necesita conmutación, gestión de abonados, canal de control y planificación, frente a la simplicidad de un repetidor convencional.

> **Ejemplo de aplicación en el ayto.** La red municipal es el ejemplo de manual de esta ventaja. Sobre **una única infraestructura**, el Ayuntamiento sirve a colectivos con necesidades muy distintas —**Policía Municipal**, **Bomberos**, **SAMUR-Protección Civil**, **Agentes de Movilidad**, **SAMUR Social** y **Parques y Jardines**— y a **más de 3.000 efectivos** `[TELEFONICA-2026]`. En un esquema convencional habrían hecho falta seis redes separadas, seis conjuntos de frecuencias y ninguna posibilidad de que un bombero y un sanitario hablaran entre sí en una intervención conjunta. Con troncalización, todos comparten los mismos canales físicos y el CISEM puede **crear sobre la marcha un grupo mixto** para una emergencia concreta.

#### 1.3. Estandarización de TETRA por el ETSI: *Trans European* / *Terrestrial Trunked Radio*

**Quién hace la norma.** **TETRA es un estándar abierto del ETSI**, el *European Telecommunications Standards Institute*, el organismo europeo de normalización de las telecomunicaciones, con sede en Sophia Antipolis (Francia). El trabajo arrancó a finales de los años ochenta dentro de un comité técnico específico, y las primeras normas se publicaron en **1995**, con el despliegue comercial iniciándose a partir de **1997**.

**Lo que significa que sea «abierto», y por qué importa.** Un estándar abierto del ETSI define **interfaces**, no productos. Cualquier fabricante puede implementar la norma, y los equipos de fabricantes distintos deben entenderse. Esa es la diferencia decisiva frente a **TETRAPOL**, que nació como desarrollo **propietario** de una empresa francesa —hoy integrada en Airbus— y que solo más tarde se documentó públicamente. Para una Administración, la consecuencia es directa y muy citable en un pliego: con un estándar abierto **no queda cautiva de un proveedor**, puede licitar terminales e infraestructura por separado y puede sustituir un fabricante por otro. Para que esa promesa sea real, el ETSI publica además una norma de **pruebas de conformidad**, la **EN 300 394** `[EN394]`, y la industria organiza pruebas de interoperabilidad entre fabricantes.

> **Dato clave.** **TETRA = estándar abierto del ETSI. TETRAPOL = tecnología de origen propietario (Matra/EADS, hoy Airbus).** Es la diferencia principal después de la del acceso al medio (TDMA frente a FDMA). El resto de sistemas: **P25** es norma de la **APCO** estadounidense; **DMR** es también del **ETSI**, pero orientado al segmento profesional de menor exigencia.

**Las dos expansiones de las siglas.** El enunciado oficial del tema recoge las dos, y esa duplicidad tiene una explicación histórica precisa:

- La denominación original fue **Trans European Trunked Radio**, «radio troncal transeuropea», coherente con un proyecto concebido para dar a Europa un sistema **común** de radio profesional, del mismo modo que el GSM le había dado un sistema común de telefonía móvil.
- Cuando el estándar empezó a adoptarse **fuera de Europa** —hoy, más de 124 países `[TCCA-GLOBAL]`—, el adjetivo «transeuropeo» dejó de tener sentido, y el ETSI pasó a expandir las siglas como **TErrestrial TRunked RAdio**, «radio troncal terrestre». El acrónimo se conservó; cambió lo que significa.

> **Dato clave.** **La expansión vigente es *TErrestrial Trunked RAdio*.** *Trans European Trunked Radio* es la **histórica**, y se abandonó por la difusión mundial del estándar. El adjetivo «terrestre» tiene además un valor descriptivo: distingue estos sistemas de los **móviles por satélite**.

**La familia de normas, que hay que saber nombrar.** El estándar no es un documento, sino una **serie**. Las piezas principales son estas:

| Serie | Contenido | Observaciones |
|----|----|----|
| **EN 300 392** | **TETRA V+D** (*Voice plus Data*): el modo troncalizado completo | Es el núcleo. La **parte 1** es el diseño general de red; la **parte 2**, el **interfaz aire**; la **parte 3**, la **ISI**; la **parte 4**, las pasarelas a PSTN/RDSI; la **parte 5**, el **PEI**; la **parte 7**, la **seguridad**; las partes 9 a 12, los **servicios suplementarios** |
| **EN 300 396** | **TETRA DMO** (*Direct Mode Operation*): el modo directo | Incluye el **repetidor DM-REP** y la **pasarela DM-GATE** |
| **EN 300 394** | **Pruebas de conformidad** | Lo que hace verificable la interoperabilidad multifabricante |
| **EN 300 395** | **Códec de voz** | Define el **ACELP** de TETRA |
| **EN 300 812** | **Módulo de identidad (SIM) de TETRA** | Equivalente funcional de la SIM de GSM |
| **TR 102 580** | **TEDS**, el servicio de datos mejorado de **TETRA Release 2** | Guía del diseñador de la alta velocidad de datos |
| **TS 104 053** | **Especificación de los algoritmos de cifrado** del interfaz aire | Su **parte 1** publicó en **febrero de 2025** el **TEA set A**, hasta entonces confidencial (§4.3.2) |

> **Dato clave.** Las dos series que hay que distinguir sin dudar: **EN 300 392 = V+D, modo troncalizado**; **EN 300 396 = DMO, modo directo**. Y dentro de la primera, las dos partes más citadas: **la parte 2 (interfaz aire)** y **la parte 7 (seguridad)**.

**Las dos *releases* del estándar.** TETRA se estructura en dos grandes revisiones funcionales:

- **TETRA Release 1** (la original, de 1995 en adelante) define **V+D**, el **modo directo**, los servicios suplementarios, la seguridad y los datos de baja velocidad. Es lo que está desplegado en la práctica totalidad de las redes en servicio, incluida la del Ayuntamiento de Madrid.
- **TETRA Release 2** (a partir de 2005-2007) añade tres bloques: **TEDS** (*TETRA Enhanced Data Service*), que multiplica la capacidad de datos con canales más anchos y modulaciones de orden superior; **códecs de voz mejorados** (AMR y códecs de banda ancha); y **mejoras de alcance**, para superar el límite de **58 km** de radio de célula heredado de la estructura de intervalos de la Release 1. Se desarrolla en §5.4.

> **Ejemplo de aplicación en el ayto.** Que TETRA sea un estándar abierto tiene una consecuencia contractual muy concreta en Madrid. La red municipal está construida sobre la plataforma **DIMETRA**, la implementación de TETRA de un fabricante, pero **el mantenimiento y la evolución del sistema se licitan como servicio**: en marzo de 2026, el Ayuntamiento adjudicó a Telefónica Soluciones el **mantenimiento integral y la evolución tecnológica de la infraestructura DIMETRA-TETRA**, por **cinco años**, con **disponibilidad 24×7** y una arquitectura que unifica el despacho y la grabación de las comunicaciones en una plataforma de alta disponibilidad `[TELEFONICA-2026]`. La norma abierta es lo que permite que el titular de la red y el operador del servicio sean entidades distintas, y que el segundo pueda cambiar sin cambiar la primera.

> **Relación con otros temas.** La lógica de la **normalización abierta frente a la solución propietaria** y sus efectos sobre la contratación pública aparece también en el **Tema 39**, a propósito del principio de **neutralidad tecnológica** del Esquema Nacional de Interoperabilidad, y en el **Tema 31**, a propósito de la dependencia de proveedor en servicios en la nube.

------------------------------------------------------------------------

### 2. Arquitectura y componentes de la red TETRA

**Visión de conjunto antes de entrar en detalle.** Una red TETRA tiene **tres grandes bloques** y **un conjunto de interfaces normalizadas** que los unen:

1.  La **SwMI** (*Switching and Management Infrastructure*), es decir, **toda la infraestructura fija**: estaciones base, nodos de conmutación, registros de abonados, gestión de red y despacho. Desde el punto de vista del terminal, **la SwMI es «la red»**.
2.  Los **terminales de usuario** o **estaciones móviles** (**MS**, *Mobile Station*), en sus distintos formatos, más los elementos que extienden su alcance (repetidores y pasarelas de modo directo).
3.  Los **equipos y sistemas conectados** a la red por línea: consolas de despacho, grabadores, sistemas de gestión de flotas, pasarelas telefónicas y aplicaciones de datos.

Y los une un **modelo de interfaces** que es la clave de la interoperabilidad y que se explica en §2.3.

> **Dato clave.** **SwMI** = *Switching and Management Infrastructure*, la infraestructura de conmutación y gestión. Es **el término oficial del estándar** para designar todo lo que no es terminal. **MS** = *Mobile Station*, el terminal. La comunicación entre ambos se produce por el **interfaz aire (I1)**.

#### 2.1. Infraestructura de conmutación y gestión (SwMI)

La SwMI no es un equipo, sino un **subsistema completo** con funciones de radio, de conmutación, de bases de datos y de gestión. El estándar define su comportamiento **hacia fuera** —cómo se comporta en el interfaz aire, en la ISI y en la interfaz de gestión— pero deja a cada fabricante la libertad de organizarla internamente. De ahí que los nombres comerciales varíen: lo que importa son las **funciones**, no los productos.

##### 2.1.1. Estaciones base (BS)

**Qué es y qué hace.** La **estación base** (**BS**, *Base Station*, también llamada **TBS** o *radio site*) es el punto donde la red pasa del cable a la radio. Contiene los **transceptores** (uno por portadora), los **amplificadores**, el **sistema radiante** (antenas, cables, combinadores y filtros) y la electrónica de control que gestiona el enlace con los terminales de su **célula**.

**Sus funciones concretas en TETRA:**

- **Radiar y recibir en las portadoras asignadas**, con la estructura TDMA de cuatro intervalos que se describe en §3.
- **Mantener el canal de control principal** (*Main Control Channel*, **MCCH**), la portadora e intervalo por los que difunde continuamente la información del sistema y por los que los terminales piden recursos. Un terminal recién encendido **busca ese canal** y se sincroniza con él.
- **Difundir la información de sistema** (SYSINFO): identidad de la red, de la célula, parámetros de acceso, clase de seguridad soportada, umbrales de reselección.
- **Asignar los canales de tráfico** que le indique el nodo de conmutación y gestionar el acceso aleatorio de los terminales.
- **Aplicar el cifrado de interfaz aire** (§4.3.2): el cifrado del interfaz aire se produce **entre la estación base y el terminal**, y por tanto **es la estación base la que cifra y descifra**.
- **Gestionar la movilidad dentro de su cobertura** y participar en el **traspaso** (*handover*) hacia células vecinas.
- **Sostener el modo de repliegue** (*local site trunking*) si pierde la conexión con el resto de la red: sigue dando servicio troncalizado **a los usuarios de su célula**, aunque sin acceso a los grupos ni a los servicios que dependen del núcleo.

> **Dato clave.** El **canal de control principal (MCCH)** es lo que distingue a un sistema troncalizado. Se transmite en el **intervalo 1 de la portadora principal** de cada célula (la denominada *main carrier*), y es por donde se difunde la información del sistema y se cursan las peticiones de recurso. **Sin canal de control no hay troncalización**; por eso los sistemas prevén el repliegue local y el modo directo.

**Configuraciones típicas.** Una BS puede tener **una sola portadora** (4 canales físicos, de los que uno es el de control → **3 de tráfico**) o **varias**. Cada portadora adicional aporta **4 canales de tráfico** más, porque el canal de control ya está servido. En emplazamientos de mucha carga se instalan cuatro, seis u ocho portadoras.

**Planificación de la cobertura.** El emplazamiento y la potencia de las estaciones base determinan la cobertura, y en un servicio de emergencia la cobertura **no se negocia**: hay que cubrir el 100 % del territorio de responsabilidad, y no solo al aire libre. Los tres problemas clásicos son:

- **La cobertura en interiores** (*indoor*), que en una ciudad es la mayoritaria: sótanos, aparcamientos, galerías de servicio, plantas bajas de edificios con estructura metálica.
- **La cobertura en túneles y subterráneos**, que exige soluciones específicas: **cable radiante** (*leaky feeder*), repetidores dedicados o estaciones base internas.
- **La cobertura de borde y la superposición** entre células, necesaria para que el traspaso sea limpio y para que la caída de una estación base no deje un agujero.

> **Ejemplo de aplicación en el ayto.** El caso del **subsuelo** es especialmente ilustrativo en Madrid, porque hay dos redes distintas que resolver. La red **municipal** debe dar servicio a Policía Municipal, Bomberos y SAMUR en aparcamientos, galerías y estaciones; y la **Comunidad de Madrid** ha ido desplegando **TETRA en la red de Metro**, con actuaciones específicas por tramos —en 2020 se adjudicó la instalación del sistema en el tramo Paco de Lucía-Puerta de Arganda de la **línea 9**, con **5,2 millones de euros** de inversión, para comunicar el Puesto de Mando con el personal de estaciones y los conductores `[METRO]`—. Que sean dos redes distintas plantea justo el problema que resuelve la **ISI** (§2.3.2): cómo hablan entre sí.

##### 2.1.2. Nodos de conmutación y control de red

**El corazón del sistema.** Por encima de las estaciones base se sitúa el **nodo de conmutación**, que los fabricantes llaman *switch*, **MSO** (*Mobile Switching Office*), **DXT** o de otras formas, y cuyas funciones el estándar atribuye genéricamente a la SwMI. Es donde se decide **quién habla con quién**.

**Funciones principales:**

- **Conmutación de las comunicaciones**: encaminar el audio de una llamada de grupo **a todas las células donde haya miembros de ese grupo afiliados**, y solo a ésas. Este punto es más sutil de lo que parece y merece detenerse: un grupo puede tener 400 miembros repartidos por toda la ciudad, pero si en un momento dado solo hay miembros afiliados en cuatro células, **solo se ocupan canales en esas cuatro**. El resto de la red queda libre.
- **Gestión de la movilidad**: registro de los terminales, seguimiento de en qué célula está cada uno, control del **traspaso** entre células y entre nodos.
- **Bases de datos de abonados y grupos**: el registro de identidades, sus atributos, sus permisos, su prioridad y su pertenencia a grupos. Es el equivalente funcional del HLR de la telefonía móvil.
- **Autenticación y gestión de claves**: el **centro de autenticación**, que custodia las claves maestras de los terminales y ejecuta el desafío de autenticación (§4.3.1), y la infraestructura de **distribución de claves por el aire** (**OTAR**).
- **Gestión de prioridades y de desalojo**: decidir a quién se le quita el canal cuando entra una emergencia.
- **Pasarelas** hacia la red telefónica pública, hacia la centralita corporativa y hacia redes de datos.
- **Interconexión con otras redes TETRA** por la **ISI**.

> **Dato clave.** En una llamada de grupo, **la red solo ocupa canal de tráfico en las células donde hay miembros del grupo afiliados**. Es la razón por la que un sistema TETRA puede soportar cientos de grupos con pocas portadoras, y una de las diferencias esenciales frente a la radio convencional, donde el grupo **es** una frecuencia y ocupa el canal siempre.

**Arquitectura distribuida y redundancia.** En redes grandes hay **varios nodos de conmutación** interconectados, de forma que la caída de uno no deja sin servicio a toda la red. La topología del transporte entre nodos y estaciones base —fibra propia, radioenlaces, líneas alquiladas— es una decisión de diseño crítica: **un sistema de radio crítico es tan disponible como su red de transporte**. En §5.3 se desarrollan los requisitos de disponibilidad.

> **Relación con otros temas.** El diseño de la red de transporte que une las estaciones base con los nodos —radioenlaces, fibra, topologías en anillo— pertenece al **Tema 33**; los mecanismos de redundancia y continuidad, al **Tema 26** (copias de seguridad y recuperación) y al **Tema 39** (medidas `op.cont` del ENS).

##### 2.1.3. Centros de gestión y administración del sistema

Este tercer bloque es el que más se olvida al estudiar y el que más aparece en los casos prácticos, porque es **donde trabajan las personas**.

**El sistema de gestión de red (NMS).** Supervisa el estado de todos los elementos: alarmas de estaciones base, ocupación de canales, calidad de los enlaces, estado de las baterías y de los grupos electrógenos, temperatura de los emplazamientos. Es el sistema desde el que se detecta que una estación base ha perdido el enlace **antes** de que un agente se quede sin cobertura. Se comunica con la SwMI por la **interfaz de gestión de red (I5)**.

**La gestión de abonados y de la flota.** Alta y baja de terminales, asignación de identidades, definición y modificación de **grupos de conversación**, perfiles de usuario, prioridades, y —función crítica— la **inhabilitación remota** de un terminal robado o perdido (*stun* temporal o *kill* permanente).

**Las consolas de despacho.** Son los puestos de operador de los centros de mando: permiten escuchar varios grupos a la vez, hablar en cualquiera de ellos, lanzar llamadas individuales, ver la **posición de los terminales** sobre un plano y atender las **alarmas de emergencia**. Se conectan a la SwMI por la **interfaz de línea** (§2.3.3).

**El registro y la grabación.** Todas las comunicaciones de un servicio de emergencia se **graban**, con su marca de tiempo y su identidad de origen, tanto por razones operativas (reconstruir una intervención) como jurídicas (prueba en un procedimiento). El grabador es un elemento de la infraestructura, no un añadido.

**La gestión de claves criptográficas.** Generación, custodia, distribución y renovación de las claves de cifrado, incluida la **distribución por el aire (OTAR)**. Es una función de seguridad de primer orden que el ENS recoge expresamente en la medida **`op.exp.10`, «protección de claves criptográficas»** `[ENS]`.

> **Ejemplo de aplicación en el ayto.** El **CISEM** —Centro Integrado de Seguridad y Emergencias, en la calle Rufino Blanco 2— es exactamente este tercer bloque hecho edificio. Desde él se coordinan **Policía Municipal (092), Bomberos, SAMUR-Protección Civil y Agentes de Movilidad**, con del orden de **3.000 incidentes diarios** `[CISEM]`. Y en el contrato de 2026 aparece explícitamente la evolución de esta capa: una arquitectura que **unifica el despacho y la grabación de comunicaciones en una plataforma de alta disponibilidad** `[TELEFONICA-2026]`. Obsérvese que lo que se moderniza no es la radio, sino **la capa de gestión y despacho**: es donde está el valor operativo del sistema.

> **Relación con otros temas.** La **grabación de las comunicaciones** y la **geolocalización de los terminales** son tratamientos de **datos personales** de empleados públicos: exigen base jurídica, información previa, plazos de conservación y medidas de seguridad. El marco está en el **Tema 6** (transparencia y acceso) y en el **Tema 32** (seguridad de la información); la protección de datos como tal no tiene tema propio en el temario oficial.

#### 2.2. Terminales de usuario

##### 2.2.1. Equipos portátiles, móviles y fijos

**Los tres factores de forma.** El estándar habla genéricamente de **MS** (*Mobile Station*), pero en la práctica se distinguen tres:

| Tipo | Descripción | Potencia típica | Uso característico |
|----|----|----|----|
| **Portátil** (*handheld*, *portable*) | El equipo de mano, alimentado por batería, con antena corta | **1 W** o **3 W** | El agente a pie, el bombero, el sanitario |
| **Móvil** (*mobile*, embarcado) | Instalado en un vehículo, alimentado del sistema eléctrico y con antena exterior | **3 W** o **10 W** | Patrullas, ambulancias, autobombas |
| **Fijo** (*fixed station*, *desktop*) | De sobremesa, en una dependencia, con antena exterior y alimentación de red | **10 W** o más | Oficinas, retenes, puestos de mando avanzados |

> **Dato clave.** Las **clases de potencia** normalizadas para el terminal TETRA son **clase 1 = 30 W**, **clase 2 = 10 W**, **clase 3 = 3 W** y **clase 4 = 1 W** (existen clases adicionales de menor potencia). En la práctica, **portátiles de 1 y 3 W** y **móviles de 3 y 10 W**. La diferencia de potencia entre un portátil y un móvil explica por qué, en el borde de la cobertura, **el vehículo llega y el agente a pie no**: es el argumento técnico que justifica el uso de **pasarelas** (§2.2.3).

**Elementos comunes a todos ellos:**

- **Botón PTT** (*push-to-talk*), el elemento definitorio.
- **Botón de emergencia**, normalmente de color naranja o rojo y en posición destacada, que lanza una **alarma de emergencia** con prioridad máxima (§4.1.2).
- **Selector de grupo de conversación**, para moverse entre los grupos a los que el usuario está autorizado.
- **Pantalla y teclado**, para mensajes de estado, SDS y menús.
- **Receptor GNSS** integrado, que permite enviar la posición a la consola de despacho mediante SDS (§4.2.1).
- **Módulo de identidad y material criptográfico**, con las identidades del usuario y las claves.
- **Robustez ambiental** certificada (grados **IP** de estanqueidad, resistencia a caídas, rango de temperatura) y, en usos con riesgo de atmósfera explosiva, **certificación ATEX**.
- **Interfaz de datos (PEI)** para conectar un ordenador embarcado o una aplicación (§2.3.3).

**Las identidades del terminal.** TETRA maneja un esquema de identidades propio:

- La **ITSI** (*Individual TETRA Subscriber Identity*) es la identidad individual completa del abonado. Se compone de la **MNI** (*Mobile Network Identity*, la identidad de la red, formada a su vez por el **MCC** —código de país— y el **MNC** —código de red—) más la **ISSI** (*Individual Short Subscriber Identity*), que es la parte corta que identifica al abonado **dentro** de su red.
- La **GTSI** (*Group TETRA Subscriber Identity*) es la identidad de **grupo**, y su parte corta es la **GSSI** (*Group Short Subscriber Identity*).
- La **TSI** (*TETRA Subscriber Identity*) es el término genérico que engloba a las anteriores.
- Sobre ellas puede aplicarse el **cifrado de identidades**: la **ESI** (*Encrypted Short Identity*), que sustituye la identidad corta por una versión cifrada en el aire para evitar el seguimiento de los usuarios (§4.3.2).
- Y, además de la identidad numérica, un **alias** alfanumérico legible («PM-Centro-12», «SAMUR-Jefe de Guardia») que es lo que se ve en la pantalla.

> **Dato clave.** **ITSI = MNI + ISSI**, donde **MNI = MCC + MNC**. La identidad **individual** corta es la **ISSI**; la de **grupo**, la **GSSI**. La **ESI** es la identidad corta **cifrada**, y es justamente el mecanismo cuyo diseño débil denunció la investigación **TETRA:BURST** en 2023 (§4.3.2).

##### 2.2.2. Modos de operación: modo troncalizado (TMO) y modo directo (DMO)

Este es **el epígrafe central de toda la sección** y conviene fijarlo con precisión.

**Modo troncalizado — TMO (*Trunked Mode Operation*).** Es el modo normal: el terminal **se comunica a través de la infraestructura**. Habla con una estación base, la estación base lo conecta con el nodo de conmutación y éste distribuye la comunicación a quien corresponda. Está normalizado en la serie **EN 300 392** (V+D).

- **Ventajas**: cobertura extensa (toda la red), acceso a **todos los grupos** y a todos los servicios, gestión de prioridades, grabación, despacho, geolocalización centralizada, interconexión telefónica y trazabilidad completa.
- **Requisito**: que haya **cobertura de la red**. Sin estación base al alcance, no hay TMO.

**Modo directo — DMO (*Direct Mode Operation*).** El terminal se comunica **directamente con otro terminal, sin infraestructura ninguna**, usando una frecuencia simplex acordada. Está normalizado en la serie **EN 300 396** `[EN396]`.

- **Ventajas**: funciona **allí donde no llega la red** —el interior de un edificio, un sótano, un túnel, una zona rural, una emergencia que ha dejado la infraestructura fuera de servicio— y **no consume recursos** de la red.
- **Limitaciones**: el alcance es el que da la potencia del terminal (**centenares de metros en ciudad, unos pocos kilómetros en campo abierto**); **no hay despacho ni grabación centralizada**; **no hay prioridades gestionadas** por la red; el grupo de conversación es el que se haya programado en los equipos; y la seguridad depende de **claves estáticas precargadas**, no de la autenticación con la red.

> **Dato clave.** **TMO = a través de la infraestructura (EN 300 392). DMO = terminal a terminal, sin infraestructura (EN 300 396).** El modo directo es una de las diferencias funcionales de fondo entre la PMR y la telefonía celular: un teléfono móvil **no puede** hablar con otro si cae la red; un terminal TETRA **sí**. Es exactamente por esto por lo que un servicio de emergencia no puede sustituir su red de radio por teléfonos móviles.

**El uso operativo real.** Un servicio de emergencia usa **los dos modos a la vez**, y no de forma alternativa:

- El **mando y la coordinación general** van por **TMO**: es donde está el despacho, la grabación y el resto de la organización.
- La **coordinación dentro de la intervención** —la dotación que entra en un edificio en llamas, el equipo que baja a una galería— va por **DMO**, porque allí no hay cobertura y porque, aunque la hubiera, no tiene sentido ocupar canales de la red para hablar entre personas que están a veinte metros unas de otras.
- Muchos terminales permiten **vigilar el canal TMO mientras se opera en DMO**, o cambiar entre modos con un botón.

**El punto de fricción.** El DMO tiene un problema evidente: **quien está en DMO desaparece del sistema**. El despacho no lo oye, no puede llamarlo, no ve su posición y no queda grabado. La solución a ese problema es el objeto del epígrafe siguiente.

##### 2.2.3. Funciones de repetición y pasarela (*repeater* y *gateway*)

La norma **EN 300 396** define dos figuras que amplían el modo directo, y **hay que distinguirlas con precisión porque hacen cosas distintas**.

**El repetidor de modo directo — DM-REP.** Es un equipo que **recibe en una frecuencia de modo directo y retransmite en otra (o en la misma) con más potencia y desde mejor posición**, ampliando el alcance de una comunicación DMO. **No conecta con la red**: lo que entra en DMO sigue siendo DMO, solo que llega más lejos.

La norma distingue tipos `[EN396]`:

- **DM-REP de tipo 1**: capaz de soportar **una sola llamada** en el interfaz aire. Se subdivide en **tipo 1A**, que trabaja sobre **una única portadora**, y **tipo 1B**, que trabaja sobre **un par de portadoras separadas en dúplex**.
- **DM-REP de tipo 2**: capaz de soportar **dos llamadas** simultáneas en el interfaz aire.

**La pasarela de modo directo — DM-GATE.** Es un equipo que **une el mundo DMO con la red troncalizada**: recibe en modo directo y **reinyecta la comunicación en la red V+D**, y viceversa. Con ella, la dotación que trabaja en DMO dentro de un edificio **vuelve a ser visible y audible** para el despacho, y el mando puede hablar con ella desde el CISEM.

**Y el equipo que hace las dos cosas — DM-REP/GATE**, que combina la función de repetidor y la de pasarela.

> **Dato clave.** **DM-REP = repetidor: amplía el alcance dentro del modo directo, sin tocar la red.** **DM-GATE = pasarela: conecta el modo directo con la red troncalizada.** **DM-REP/GATE** hace ambas. Los tipos de repetidor son **1A** (una portadora, una llamada), **1B** (par de portadoras dúplex, una llamada) y **2** (dos llamadas). Confundir repetidor con pasarela es el error clásico de este epígrafe.

**Dónde se materializan estas funciones.** Normalmente **en el terminal móvil de un vehículo**: los equipos embarcados de gama profesional pueden configurarse para actuar como DM-REP o DM-GATE. Eso convierte al vehículo aparcado en la puerta de un edificio en **el nodo que da cobertura y conectividad a los que están dentro** —y explica por qué, en la práctica operativa, la ubicación del vehículo de mando no es una decisión menor—. También existen repetidores y pasarelas **transportables**, que se despliegan sobre el terreno en incidentes de larga duración.

> **Ejercicio resuelto.** **Elegir el modo y el equipo en una intervención real.** **Supuesto**: incendio en el sótano de un edificio de oficinas del distrito de Salamanca. Intervienen dos dotaciones de **Bomberos**, una **UVI móvil del SAMUR** y una unidad de la **Policía Municipal** que corta el tráfico. El sótano **no tiene cobertura** de la red municipal. **Paso 1 — Coordinación general.** El mando del incidente, el CISEM y las unidades en superficie trabajan en **TMO**, en el grupo de conversación creado para el incidente. Es donde hay despacho, grabación y visión de posiciones. **Paso 2 — Dentro del sótano.** Las dotaciones que descienden pasan a **DMO**, porque no hay cobertura. Entre ellas se oyen, pero el CISEM no. **Paso 3 — Recuperar el enlace.** El vehículo de bomberos aparcado en el portal se configura como **DM-GATE**. A partir de ese momento, lo que se habla en DMO en el sótano **entra en la red** y llega al mando y al CISEM, y lo que dice el mando llega al sótano. La intervención vuelve a estar grabada y coordinada. **Paso 4 — Si el sótano fuera muy extenso.** Si el alcance del modo directo no bastara para cubrir toda la planta, se añadiría un **DM-REP** —o se usaría un equipo **DM-REP/GATE**— para ampliar el alcance dentro del subsuelo **antes** de reinyectar en la red. **Conclusión y trampa habitual**: si en el paso 3 se hubiera puesto un **DM-REP** en lugar de un **DM-GATE**, la dotación se oiría mejor entre sí, **pero el CISEM seguiría sin enterarse de nada**. Repetidor y pasarela **no** son intercambiables.

#### 2.3. Interfaces estándar de TETRA

**El modelo de referencia.** La guía del diseñador del ETSI `[ETR300-1]` define **seis puntos de referencia**, numerados de **I1 a I6**, que son los que hacen de TETRA un estándar abierto: cada uno delimita una frontera en la que dos elementos de fabricantes distintos deben entenderse.

| Interfaz | Denominación | Qué une | Norma principal |
|----|----|----|----|
| **I1** | **Interfaz aire** (*radio air interface*) | Terminal ↔ estación base, en **modo troncalizado** | **EN 300 392-2** |
| **I2** | **Interfaz de línea** (*line station interface*, LSI/LNI) | Estaciones y equipos conectados por línea ↔ SwMI | EN 300 392 |
| **I3** | **ISI** (*Inter-System Interface*) | Red TETRA ↔ **otra red TETRA** | **EN 300 392-3** |
| **I4** | **Interfaz de equipo terminal** (**PEI**, *Peripheral Equipment Interface*) | Terminal ↔ equipo de datos del usuario | **EN 300 392-5** |
| **I5** | **Interfaz de gestión de red** | SwMI ↔ sistema de gestión (NMS) | EN 300 392 |
| **I6** | **Interfaz aire de modo directo** | Terminal ↔ terminal, **sin red** | **EN 300 396** |

> **Dato clave.** Las seis interfaces, en orden: **I1 aire (TMO)**, **I2 línea**, **I3 ISI**, **I4 terminal/PEI**, **I5 gestión de red**, **I6 aire en modo directo**. Las **dos interfaces aire** son la **I1** (troncalizado) y la **I6** (directo), y están en normas distintas. A esto se añaden las **pasarelas a PSTN y RDSI** de la **EN 300 392-4**, que no son un punto I sino un elemento funcional.

##### 2.3.1. Interfaz aire (*air interface*)

**Es la norma central del estándar** y el objeto de la **EN 300 392-2** `[EN392-2]`. Define **todo lo que ocurre entre el terminal y la estación base**, y se organiza en tres capas, siguiendo el modelo de referencia de ISO:

1.  **Capa física (capa 1)**: la portadora de **25 kHz**, la modulación **π/4-DQPSK**, la tasa de **18.000 símbolos por segundo**, la estructura **TDMA de cuatro intervalos**, los tipos de **ráfaga**, la sincronización, el control de potencia y la corrección de errores. Se desarrolla entera en **§3**.
2.  **Capa de enlace de datos (capa 2)**: subdividida en **MAC** (*Medium Access Control*), que gestiona el acceso al medio y multiplexa los canales lógicos sobre los físicos, y **LLC** (*Logical Link Control*), que da el servicio de enlace fiable o no fiable a la capa superior. Aquí residen el **acceso aleatorio con resolución de colisiones** y el **cifrado de interfaz aire**.
3.  **Capa de red (capa 3)**: donde viven los protocolos de **gestión de la movilidad** (**MM**), de **control de llamada** (**CMCE**, *Circuit Mode Control Entity*, para voz y datos por circuito), de **datos por paquetes** (**SNDCP**) y de **gestión del propio interfaz** (**MLE**).

> **Dato clave.** El interfaz aire de TETRA se estructura en **tres capas**: **física**, **enlace (MAC + LLC)** y **red (MM, CMCE, SNDCP, MLE)**. El **cifrado de interfaz aire se aplica en la capa 2**, entre terminal y estación base; el **cifrado extremo a extremo**, por encima, entre terminal y terminal (§4.3.3). Esa diferencia de nivel es la que explica **qué protege cada uno**.

> **Relación con otros temas.** La correspondencia entre estas tres capas y las siete del **modelo OSI** —y las cuatro de **TCP/IP**— es materia del **Tema 34**. Aquí basta con retener que TETRA implementa las tres capas inferiores y que, por encima de ellas, transporta **IP** cuando presta servicio de datos por paquetes (§4.2.2).

##### 2.3.2. Interfaz de interconexión entre sistemas (ISI)

**Qué problema resuelve.** Una red TETRA de un ayuntamiento y otra de una comunidad autónoma son **dos sistemas independientes**: distinta MNI, distintos abonados, distintas claves, distintos centros de mando. Cuando hay una emergencia que afecta a los dos, alguien tiene que poder hablar con alguien. La **ISI** (*Inter-System Interface*), normalizada en la **EN 300 392-3** `[EN392-3]`, es el punto de referencia que permite **interconectar dos redes TETRA** de forma normalizada.

**Qué permite:**

- **Llamadas individuales y de grupo entre abonados de redes distintas.**
- **Itinerancia** (*roaming*): que un terminal de la red A obtenga servicio en la cobertura de la red B, con las autorizaciones que se hayan acordado.
- **Transferencia de mensajes cortos** entre redes.
- **Servicios suplementarios** limitados a través de la interconexión.

**El problema práctico, que conviene decir con franqueza.** La ISI es la parte del estándar cuya **implantación real ha sido más desigual**. Durante años, los fabricantes la implementaron de forma parcial o con extensiones propias, de modo que muchas interconexiones entre redes se resolvieron con **pasarelas de audio** o **acoplamientos a nivel de despacho** —consolas que puentean grupos de dos redes— en lugar de con una ISI completa. Es un punto sensible en cualquier pliego: **conviene exigir la interconexión con requisitos funcionales verificables**, no con una simple mención a la norma.

> **Ejemplo de aplicación en el ayto.** En el territorio del municipio conviven, como mínimo, **tres sistemas de radiocomunicación de emergencia de titularidad distinta**: el **municipal** (DIMETRA-TETRA del Ayuntamiento), el **autonómico** (la red TETRA de la Comunidad de Madrid, con **113 estaciones base** y **5.316 terminales**, gestionada por la **ASEM 112** `[CM-TETRA]`) y el **estatal** (**SIRDEE**, que además **no es TETRA sino TETRAPOL** `[SIRDEE]`). Los dos primeros son interconectables por **ISI**, al menos en teoría; con el tercero **la ISI no sirve**, porque es otra tecnología, y la interoperabilidad tiene que resolverse forzosamente por **pasarelas** o por **acoplamiento de grupos en los centros de mando**. Es la razón técnica por la que la coordinación multiadministración en una emergencia grande sigue apoyándose en los centros 112 y no en la radio.

##### 2.3.3. Interfaz de línea (LNI) e interfaces de datos

**La interfaz de línea (I2).** Es el punto por el que se conectan a la SwMI **los equipos fijos que no llegan por radio**: consolas de despacho, estaciones fijas de dependencias, grabadores, pasarelas telefónicas y sistemas de gestión. Se la denomina **LSI** (*Line Station Interface*) o **LNI** (*Line connected Network Interface*) según la fuente; el enunciado del tema usa la segunda forma. Funcionalmente, permite que un operador del centro de mando tenga en su puesto **las mismas capacidades que un terminal de radio** —hablar en grupos, lanzar llamadas, recibir alarmas— pero con la ergonomía de un puesto de trabajo y sin ocupar recursos radio.

**La interfaz de equipo periférico — PEI (I4).** Normalizada en la **EN 300 392-5** `[EN392-5]`, es la que conecta **el terminal con un equipo de datos del usuario**: el ordenador embarcado de un vehículo, una impresora de denuncias, un lector de matrículas, un sensor de telemetría o una aplicación de gestión de flotas. Se basa en un juego de **comandos AT** extendidos —herencia directa del mundo de los módems— más los protocolos de transporte de datos. Es lo que convierte al terminal en un **módem de datos** además de en una radio.

**Y las pasarelas hacia otras redes.** La **EN 300 392-4** `[EN392-4]` define las pasarelas hacia la **red telefónica pública conmutada (PSTN)** y hacia **RDSI**, que permiten que un terminal de radio llame a un teléfono fijo o móvil, y al revés, con las restricciones de tarificación y autorización que fije el operador de la red.

> **Ejemplo de aplicación en el ayto.** El **PEI** es lo que hace posible una función cotidiana en la Policía Municipal: que el terminal embarcado transmita, sin intervención del agente, la **posición del vehículo** al sistema de gestión de flotas del CISEM, y que el ordenador del coche patrulla curse consultas a sistemas de información —matrículas, requisitorias— **usando la radio como canal de datos** cuando no hay cobertura de datos comercial o cuando se exige que el tráfico vaya por la red propia. La capacidad es modesta en TETRA Release 1 (§4.2.2), lo bastante para texto y consultas breves, y es justo el límite que **TEDS** (§5.4) vino a ampliar.

> **Relación con otros temas.** El uso del terminal como canal de datos para aplicaciones de gestión enlaza con el **Tema 24** (desarrollo para dispositivos móviles) y con el **Tema 22** (arquitecturas cliente/servidor y servicios web); la protección del tráfico de esas aplicaciones, con el **Tema 36**.

------------------------------------------------------------------------

### 3. Capa física y transmisión radio en TETRA

**Advertencia de estudio.** Esta es la sección **más rentable en puntos por palabra** de todo el tema y la que exige memorización literal. Todo lo que sigue está en la **EN 300 392-2** `[EN392-2]`, y las bandas de frecuencia, en el **CNAF** `[CNAF]`. Conviene estudiarla con el **D9** (espectro), el **D10** (FDMA + TDMA), el **D11** (modulación) y el **D12** (jerarquía temporal) delante.

#### 3.1. Espectro radioeléctrico y asignación de frecuencias

**El principio de partida.** El espectro radioeléctrico es un **bien de dominio público** cuya titularidad y administración corresponden al **Estado** —art. **85** de la Ley 11/2022 `[LGTel]`—. Ninguna Administración, ni siquiera un ayuntamiento, «tiene» frecuencias: **las usa al amparo de un título habilitante** otorgado por el Estado, con las condiciones que fije el CNAF. El régimen jurídico completo se desarrolla en §5.2; aquí interesa **qué bandas usa TETRA y con qué características técnicas**.

**Las bandas de TETRA en el mundo.** El estándar no está atado a una banda concreta: la **EN 300 392-2** define parámetros de capa física y la parte correspondiente de la serie **TS 100 392** enumera las bandas y separaciones dúplex admitidas. En la práctica, TETRA se despliega en:

| Rango | Uso característico |
|----|----|
| **380-400 MHz** | **Servicios de emergencia y seguridad pública en Europa** (banda armonizada) |
| **410-430 MHz** | **Uso civil, PMR/PAMR, transporte, industria y servicios públicos** |
| **450-470 MHz** | Uso civil y PPDR según país |
| **806-870 MHz** | Uso comercial y de transporte, principalmente fuera de Europa |

**Y ahora la parte española.** El **Cuadro Nacional de Atribución de Frecuencias** es la norma que reparte el espectro en España. Y aquí hay que empezar por un dato que casi ningún material recoge todavía:

> **Dato clave.** **El CNAF vigente es el aprobado por la Orden TDF/732/2026, de 10 de julio** (BOE núm. 173, de **17 de julio de 2026**, 349 páginas). **Sustituye al anterior —Orden ETD/1449/2021, de 16 de diciembre— con efectos de 18 de julio de 2026**, y su motivo declarado es incorporar las previsiones de la **Conferencia Mundial de Radiocomunicaciones de 2023 (CMR-23)**, en vigor en su mayoría desde el **1 de enero de 2025**. Quien haya estudiado con material anterior al verano de 2026 citará una orden **derogada**.

**Las dos notas del CNAF que hay que conocer.** Las condiciones concretas de uso de cada banda están en las **notas de utilización nacional (UN)**. Dos de ellas son directamente materia de este tema.

**Nota UN-28 — la banda de las emergencias.** Dice literalmente que la banda **235-399,9 MHz** está destinada a **uso exclusivo del Estado para sistemas del Ministerio de Defensa**, *con excepción* de las subbandas **380-385 MHz y 390-395 MHz** que, **de conformidad con la Decisión de la CEPT ECC/DEC(08)05**, «se destinan para **redes de servicios de seguridad de las Fuerzas y Cuerpos de Seguridad del Estado y redes de servicios de emergencia en todo el territorio nacional**» `[CNAF]`. Obsérvese la estructura: son **dos subbandas de 5 MHz separadas 10 MHz**, es decir, un **par dúplex**: 380-385 MHz para un sentido y 390-395 MHz para el otro. La nota añade un dato operativo interesante: por problemas de **saturación en entornos urbanos de alta densidad**, las solicitudes de asignación deben incluir «un exhaustivo **plan de reutilización** que minimice las necesidades de espectro».

**Nota UN-31 — la banda de TETRA civil, donde el CNAF nombra la tecnología.** Estructura la banda **406-470 MHz** en subbandas. La que interesa es la **410-430 MHz**, «reservada a aplicaciones del servicio móvil y fijo de banda estrecha bajo la modalidad **dúplex con una separación Tx/Rx de 10 MHz**». Y dentro de ella, textualmente: «Las subbandas de frecuencias **410 a 415,3 MHz y 420 a 425,3 MHz** \[…\] se destinan a **sistemas digitales de acceso aleatorio de canales (TETRA y otros)** con anchura de banda de emisión correspondiente a una **canalización de 25 kHz**» `[CNAF]`. El resto de la banda 410-430 MHz se destina a comunicaciones dúplex con canalización de **12,5 kHz**.

> **Dato clave.** Las dos cifras que hay que saber de memoria: **380-385 / 390-395 MHz** para las redes de **seguridad del Estado y emergencias** (nota **UN-28**, decisión **ECC/DEC(08)05**); y **410-415,3 / 420-425,3 MHz** para **TETRA civil**, con **canalización de 25 kHz** y **separación dúplex de 10 MHz** (nota **UN-31**). El CNAF **cita TETRA por su nombre** en esta segunda nota: es la única mención expresa de la tecnología en la norma española del espectro, y por eso es un dato de primer orden.

**Un tercer dato del CNAF, para la evolución.** La misma nota **UN-31** reserva los bloques pareados **452-457,5 / 462-467,5 MHz**, en aplicación de la Decisión **ECC/DEC(16)02**, «a sistemas de **protección pública y operaciones de socorro en caso de catástrofe PPDR** de **banda ancha**, preferentemente para el sistema de ámbito nacional» `[CNAF]`. Y en la banda de **700 MHz**, el CNAF destina **733-736 / 788-791 MHz** al sistema PPDR de **ámbito nacional** y **698-703 / 753-758 MHz** a las **redes de ámbito autonómico y local** `[CNAF]`. Ese último bloque es, literalmente, **el espectro que la norma española reserva para una futura red de banda ancha crítica de una comunidad autónoma o de un ayuntamiento** (§5.4).

> **Ejercicio resuelto.** **Leer el CNAF y decidir en qué banda encaja un despliegue.** **Supuesto**: un ayuntamiento quiere ampliar su red TETRA para dar servicio, además de a policía y bomberos, a los servicios de limpieza y de parques y jardines. **Paso 1 — ¿Sirve la banda de 380-400 MHz?** La nota **UN-28** la reserva a «redes de servicios de seguridad de las FCSE y redes de servicios de emergencia». Un servicio de **limpieza viaria** no es ninguna de las dos cosas. **No encaja** por la vía de la UN-28. **Paso 2 — ¿Y la banda de 410-430 MHz?** La nota **UN-31** destina 410-415,3 / 420-425,3 MHz a «sistemas digitales de acceso aleatorio de canales (TETRA y otros)» con canalización de **25 kHz**, sin restringirlo a emergencias. **Encaja**. **Paso 3 — ¿Cuántas frecuencias hacen falta?** La subbanda útil es de **5,3 MHz** en cada sentido; a **25 kHz** por portadora, caben **212 portadoras** teóricas en el conjunto del territorio nacional, que se reutilizan geográficamente. El ayuntamiento pedirá **las portadoras concretas** que necesite su plan de reutilización, no la subbanda entera. **Paso 4 — ¿Qué título habilitante?** Uso **privativo** para **autoprestación** por una Administración pública → **afectación demanial**, art. **88.5.b)** de la Ley 11/2022 (§5.2). **Conclusión**: la respuesta no es «la banda de emergencias porque somos un ayuntamiento», sino «la banda que corresponda **al servicio**, según lo que diga la nota UN». Es el error más frecuente en este tipo de supuesto.

**Reutilización de frecuencias y planificación celular.** Como en cualquier sistema celular, las mismas portadoras se reutilizan en células suficientemente alejadas. El **patrón de reutilización** debe garantizar una relación señal-interferencia suficiente; en TETRA se manejan patrones más conservadores que en telefonía celular porque el requisito de **calidad de voz en el borde de la célula** es más exigente. La contrapartida es que la red necesita **menos capacidad por célula** que una red comercial: el tráfico de un servicio de emergencia es de baja ocupación media y picos muy acusados.

#### 3.2. Técnica de acceso múltiple por división de tiempo (TDMA)

**Los tres accesos múltiples, en una frase cada uno.** Para situar TETRA hay que tener claros los tres esquemas clásicos:

- **FDMA** (*Frequency Division Multiple Access*): a cada usuario se le da **una frecuencia distinta**. Es lo que hace la radio analógica convencional y lo que hace **TETRAPOL**.
- **TDMA** (*Time Division Multiple Access*): varios usuarios **comparten la misma frecuencia** turnándose en el tiempo, en **intervalos** (*time slots*) periódicos. Es lo que hace **TETRA** —y lo que hacía GSM—.
- **CDMA** (*Code Division Multiple Access*): todos transmiten a la vez en la misma banda, separados por **códigos ortogonales**. No se usa en TETRA.

**Lo que hace TETRA es una combinación.** El espectro se divide primero en **portadoras de 25 kHz** —eso es **FDMA**— y cada portadora se divide después en **4 intervalos de tiempo** —eso es **TDMA**—. El resultado es que **una sola pareja de frecuencias de 25 kHz sostiene cuatro canales físicos**.

> **Dato clave.** **TETRA usa FDMA + TDMA 4:1**: portadoras de **25 kHz** con **4 intervalos** cada una. Ésta es **la** cifra del tema. De ella se derivan las demás: 4 canales por portadora, uno de ellos normalmente de control, y **tres de tráfico** en una estación base de una sola portadora.

**Por qué esto importa tanto en la comparación con TETRAPOL.** Es la diferencia estructural entre los dos sistemas y el eje de la comparación:

|  | **TETRA** | **TETRAPOL** |
|----|----|----|
| Origen | **Estándar abierto del ETSI** | Desarrollo **propietario** (Matra/EADS, hoy Airbus) |
| Acceso múltiple | **TDMA** (4 intervalos) | **FDMA** |
| Canalización | **25 kHz** | **12,5 kHz** |
| Modulación | **π/4-DQPSK** | **GMSK** |
| Canales por par de frecuencias | **4** | **1** |
| Eficiencia por canal de voz | 25 kHz / 4 = **6,25 kHz por canal** | **12,5 kHz por canal** |
| Uso en España | Redes **autonómicas y municipales** (Madrid, entre otras) | **SIRDEE**, la red del **Estado** |

> **Dato clave.** **TETRA = TDMA, 25 kHz, 4 canales por portadora, π/4-DQPSK. TETRAPOL = FDMA, 12,5 kHz, 1 canal por portadora, GMSK.** En **eficiencia espectral por canal de voz**, TETRA obtiene **6,25 kHz/canal** frente a los **12,5 kHz/canal** de TETRAPOL: **el doble**. A cambio, el esquema FDMA de TETRAPOL da algo más de alcance por canal en condiciones de propagación difíciles, que es el argumento clásico de sus defensores para el despliegue rural. Y, sobre todo: **el SIRDEE español es TETRAPOL, no TETRA**.

**Las consecuencias prácticas del TDMA.** El esquema de intervalos no es solo una forma de repartir: habilita funciones que el FDMA no tiene fáciles.

1.  **Menos hardware en la estación base.** Cuatro canales de conversación caben en **un transceptor**, no en cuatro. Menos amplificadores, menos combinadores, menos consumo, menos espacio y menos coste por canal.
2.  **Agregación de intervalos para datos.** Si un usuario necesita más capacidad, el sistema puede darle **dos, tres o los cuatro intervalos** de la portadora, multiplicando su tasa (§4.2.2). En FDMA habría que darle varias frecuencias, con la complejidad que eso supone en el terminal.
3.  **Modo dúplex sin duplexor completo.** El terminal transmite en un intervalo y recibe en otro **desplazado en el tiempo**, lo que simplifica el diseño de radiofrecuencia.
4.  **Ahorro de batería.** El terminal solo transmite y recibe en sus intervalos; el resto del tiempo puede reducir consumo. Es una de las razones de la buena autonomía de los portátiles TETRA.

**Y su limitación característica: el alcance.** La estructura de intervalos impone un **tiempo de guarda** finito entre transmisiones consecutivas. Si un terminal está muy lejos, su ráfaga llega tan retrasada que **invadiría el intervalo siguiente**. Ese razonamiento fija el **radio máximo de célula de TETRA Release 1 en 58 km**. No es una limitación de potencia, sino **de tiempo**: es el mismo fenómeno que limitaba el alcance de las células GSM.

> **Dato clave.** El **radio máximo de célula en TETRA Release 1 es de 58 km**, y la causa es **la estructura temporal de los intervalos TDMA**, no la potencia. TETRA Release 2 incorporó mejoras de alcance para superar ese límite en despliegues rurales, marítimos y militares.

#### 3.3. Modulación digital π/4-DQPSK

**Qué modulación usa TETRA y cómo se lee su nombre.** La modulación del interfaz aire de TETRA Release 1 es la **π/4-DQPSK**, *differential quaternary phase shift keying* con desplazamiento de π/4. Se descompone así:

- **PSK** (*Phase Shift Keying*): la información se codifica en la **fase** de la portadora, no en su amplitud ni en su frecuencia.
- **Q** de *quaternary*: hay **cuatro** estados de fase posibles, de modo que **cada símbolo transporta 2 bits** (2² = 4).
- **D** de *differential*: lo que se codifica **no es la fase absoluta**, sino **el cambio de fase respecto al símbolo anterior**. Eso permite una **detección diferencial** que no necesita recuperar una referencia de fase absoluta en el receptor, lo que simplifica el terminal y lo hace más robusto frente a los desplazamientos de fase que provoca el movimiento.
- **π/4**: entre dos símbolos consecutivos se introduce un **desplazamiento adicional de 45°**, de manera que las transiciones nunca pasan por el **origen de la constelación**.

**Por qué ese detalle del origen es importante.** Pasar por el origen significa que la **envolvente de la señal cae a cero**, y una señal con variaciones muy bruscas de amplitud obliga a usar amplificadores muy lineales, que son **caros e ineficientes en consumo**. Al evitar el paso por cero, la π/4-DQPSK mantiene una **relación pico-media moderada**, lo que permite amplificadores más eficientes: en un terminal alimentado por batería, eso se traduce directamente en **más horas de autonomía**.

> **Dato clave.** **π/4-DQPSK**: **4 estados de fase → 2 bits por símbolo**; **codificación diferencial** (se codifica el **cambio** de fase, no la fase absoluta); y **desplazamiento de π/4** que evita el paso por el origen y, con él, las caídas de envolvente a cero. Comparar con la **GMSK** de TETRAPOL y de GSM, que es de **envolvente constante** y **1 bit por símbolo**.

**Las cifras que se derivan.** La tasa de símbolo del interfaz aire es de **18.000 símbolos por segundo (18 kbaudios)** en un canal de **25 kHz**, con filtrado de **coseno alzado en raíz** de factor de caída (*roll-off*) **α = 0,35**. Como cada símbolo lleva **2 bits**:

**18.000 símbolos/s × 2 bits/símbolo = 36.000 bits/s = 36 kbit/s brutos por portadora.**

Y como la portadora se divide en **4 intervalos**, a cada uno le corresponden **9 kbit/s brutos**, de los que —descontadas la sincronización, las cabeceras y la protección de errores— quedan **7,2 kbit/s netos** disponibles por intervalo para el usuario.

> **Dato clave.** La cadena de cifras que hay que saber encadenar: **25 kHz → 18 kbaudios → 2 bits/símbolo → 36 kbit/s brutos por portadora → 4 intervalos → 7,2 kbit/s netos por intervalo**. Con los **cuatro intervalos** agregados: **28,8 kbit/s** netos. Es la cifra que define el techo de datos de TETRA Release 1 y la razón de ser de **TEDS**.

**El códec de voz.** La voz se digitaliza con un códec **ACELP** (*Algebraic Code Excited Linear Prediction*), definido en la **EN 300 395** `[EN395]`. Sus cifras:

- Trabaja sobre **tramas de voz de 30 ms**, muestreadas a **8 kHz** (240 muestras por trama).
- Produce **137 bits por trama**, lo que da **137 / 0,030 = 4.567 bits/s ≈ 4,567 kbit/s** netos de voz.
- A esos bits se les añade **codificación de canal** (protección frente a errores), hasta ocupar los **7,2 kbit/s** del intervalo.

> **Dato clave.** Códec **ACELP** de TETRA: **137 bits cada 30 ms = 4,567 kbit/s** de voz neta; con protección de errores, **7,2 kbit/s** por intervalo. La diferencia entre ambas cifras —casi el 37 % del caudal dedicado a **corregir errores**— es lo que permite que la voz siga siendo inteligible en el borde de la cobertura, y es una de las ventajas de fondo de la radio digital sobre la analógica: en analógico, la degradación es **progresiva** (ruido creciente); en digital, la corrección de errores mantiene la calidad **constante** hasta que se cae de golpe.

**La protección de errores.** TETRA aplica una cadena clásica: **codificación convolucional** con distintas tasas según la importancia de los bits (los bits más significativos de la voz se protegen más que los menos), **entrelazado** (*interleaving*) para repartir en el tiempo los errores en ráfaga típicos del desvanecimiento, y **comprobación de redundancia cíclica (CRC)** para detectar tramas irrecuperables. Para datos existen tres niveles: **sin protección (7,2 kbit/s)**, **protección baja (4,8 kbit/s)** y **protección alta (2,4 kbit/s)** por intervalo.

> **Relación con otros temas.** Los fundamentos de la modulación digital, la relación entre ancho de banda y tasa binaria y las técnicas de detección y corrección de errores se tratan en el **Tema 33**. Aquí se aplican a un caso concreto y con cifras concretas.

#### 3.4. Estructura de trama radio y canales lógicos

**La jerarquía temporal, que hay que memorizar entera.** El tiempo en el interfaz aire de TETRA está organizado en cuatro niveles anidados:

| Unidad                                | Composición        | Duración      |
|---------------------------------------|--------------------|---------------|
| **Intervalo de tiempo** (*time slot*) | Unidad básica      | **14,167 ms** |
| **Trama TDMA** (*frame*)              | **4 intervalos**   | **56,67 ms**  |
| **Multitrama** (*multiframe*)         | **18 tramas**      | **1,02 s**    |
| **Hipertrama** (*hyperframe*)         | **60 multitramas** | **61,2 s**    |

> **Dato clave.** **1 intervalo = 14,167 ms · 1 trama = 4 intervalos = 56,67 ms · 1 multitrama = 18 tramas = 1,02 s · 1 hipertrama = 60 multitramas = 61,2 s.** Y el detalle clave: **la trama 18 de cada multitrama es la trama de control**, reservada a señalización. Por eso el usuario dispone de **17 de cada 18 tramas** para su tráfico, y no de las 18.

**Por qué existe la trama de control.** Reservar una trama de cada dieciocho para señalización permite que la red envíe información a un terminal **mientras éste está en conversación**, sin interrumpirla: avisos de llamada entrante, actualizaciones de estado, cambios de clave, órdenes de traspaso. Es lo que hace posible la función de **entrada tardía** (*late entry*): un terminal que se afilia a un grupo con la conversación ya empezada **se entera de que hay una llamada en curso** y se incorpora a ella.

**La hipertrama y la criptografía.** La hipertrama de **61,2 s** no es un capricho: el **número de hipertrama** interviene en la generación del flujo de clave del cifrado de interfaz aire, junto con el **tiempo de red** difundido por la estación base. Este detalle, aparentemente menor, es exactamente el que la investigación **TETRA:BURST** convirtió en vulnerabilidad: **si el tiempo de red se difunde sin autenticar, un atacante puede manipularlo y forzar la reutilización del flujo de clave** (§4.3.2).

**Los tipos de ráfaga (*burst*).** Cada intervalo se ocupa con una **ráfaga** cuyo formato depende del sentido y de la función:

- **Enlace descendente** (estación base → terminal): **ráfaga normal descendente** (*normal downlink burst*, con **432 bits útiles** en dos bloques de 216), **ráfaga de sincronización** (*synchronisation burst*, que porta la información de temporización y de trama) y **ráfaga de linealización descendente**.
- **Enlace ascendente** (terminal → estación base): **ráfaga normal ascendente** (**336 bits útiles**, en dos bloques de 168), **ráfaga de control ascendente** (**168 bits**, que ocupa un **subintervalo** y se usa para el acceso aleatorio) y **ráfaga de linealización ascendente**.

> **Dato clave.** La ráfaga **descendente** es **continua** —la estación base transmite sin interrupción, lo que da a los terminales una referencia permanente de sincronismo— mientras que la **ascendente** es **discontinua**, porque cada terminal solo transmite en su intervalo. La **ráfaga de control ascendente** ocupa **medio intervalo** (*subslot*) y es la que se usa para el **acceso aleatorio**, es decir, para pedir recurso al sistema; por eso las colisiones se resuelven ahí y no en los canales de tráfico.

**Los canales lógicos.** Sobre esa estructura física, la capa MAC define **canales lógicos**, que son los que transportan cada tipo de información. Se agrupan en dos familias:

**Canales de control (CCH):**

| Canal | Nombre | Función |
|----|----|----|
| **BCCH** | *Broadcast Control Channel* | Difusión de la información del sistema, en dos variantes: **BNCH** (información de red) y **BSCH** (información de sincronización) |
| **LCH** | *Linearisation Channel* | Linealización de los amplificadores |
| **SCH** | *Signalling Channel* | Señalización punto a punto y de acceso: **SCH/F** (completo), **SCH/HD** (medio, descendente), **SCH/HU** (medio, ascendente, el del acceso aleatorio) |
| **ACCH** | *Associated Control Channel* | Señalización **asociada** a una llamada en curso: **FACCH** (rápido, roba capacidad al tráfico) y **SACCH** (lento, usa la trama de control) |
| **STCH** | *Stealing Channel* | Señalización urgente que «roba» capacidad al canal de tráfico |

**Canales de tráfico (TCH):**

| Canal       | Función                                                   |
|-------------|-----------------------------------------------------------|
| **TCH/S**   | Tráfico de **voz** (*speech*), a 7,2 kbit/s por intervalo |
| **TCH/7,2** | Datos **sin protección**, 7,2 kbit/s                      |
| **TCH/4,8** | Datos con **protección baja**, 4,8 kbit/s                 |
| **TCH/2,4** | Datos con **protección alta**, 2,4 kbit/s                 |

> **Dato clave.** Distinguir **canal físico** (un intervalo de una portadora) de **canal lógico** (el tipo de información que se transporta sobre él). Y dentro de los lógicos, las dos familias: **de control (CCH)** y **de tráfico (TCH)**. El **canal de control principal (MCCH)** es el canal lógico de control que la estación base mantiene permanentemente activo en el **intervalo 1 de la portadora principal**.

> **Ejercicio resuelto.** **Calcular la capacidad real de una estación base municipal.** **Supuesto**: una estación base con **3 portadoras** de 25 kHz da cobertura al centro de la ciudad. **Paso 1 — Canales físicos brutos**: 3 portadoras × 4 intervalos = **12 canales físicos**. **Paso 2 — Descontar el control**: la configuración estándar dedica **1 intervalo al MCCH** → **11 canales de tráfico**. **Paso 3 — Traducirlo a conversaciones**: cada llamada de grupo o individual ocupa **un canal de tráfico** mientras alguien está hablando → hasta **11 conversaciones simultáneas** en esa célula. **Paso 4 — ¿Y cuántos grupos caben?** **Todos los que se quiera.** Un grupo no ocupa canal por existir, sino **solo cuando alguien transmite en él**. Con 11 canales de tráfico pueden convivir decenas de grupos de conversación afiliados en la célula, siempre que no hablen once más uno a la vez. **Paso 5 — Ancho de banda ocupado**: 3 portadoras × 25 kHz = **75 kHz** en cada sentido, **150 kHz** contando el par dúplex. **Comparación**: para dar 11 canales de voz simultáneos con radio convencional analógica de 12,5 kHz harían falta **11 parejas de frecuencias**, es decir, **137,5 kHz en cada sentido**, y además **rígidamente asignadas**. Es la ventaja del *trunking* y del TDMA sumadas.

> **Ejemplo de aplicación en el ayto.** Estas cifras explican por qué la red municipal puede atender simultáneamente a **más de 3.000 efectivos** `[TELEFONICA-2026]` con un número modesto de portadoras: en un momento cualquiera, la inmensa mayoría de esos efectivos **están escuchando, no hablando**, y escuchar **no consume canal en su célula si nadie de su grupo transmite allí**. El dimensionado de una red de emergencia no se hace por número de usuarios, sino por **número de transmisiones simultáneas previstas en la hora punta de la célula más cargada**, con un margen holgado para el escenario de gran emergencia, en el que todo el mundo quiere hablar a la vez.

------------------------------------------------------------------------

### 4. Servicios y seguridad en sistemas TETRA

**Cómo clasifica el estándar sus servicios.** El ETSI, siguiendo la tradición de las normas de telecomunicación, ordena lo que TETRA ofrece en tres familias:

1.  **Teleservicios**: los que el sistema presta de extremo a extremo, con el terminal incluido. En TETRA, básicamente **la voz**.
2.  **Servicios portadores** (*bearer services*): los que ofrecen **transporte de información** entre dos puntos, dejando al usuario la aplicación. En TETRA, los servicios de **datos** por circuito y por paquetes.
3.  **Servicios suplementarios**: los que **modifican o complementan** a los anteriores. Es la familia más rica de TETRA y la que le da su carácter de sistema profesional: prioridad, desalojo, escucha ambiente, escucha discreta, DGNA, identificación, desvío, inclusión, entrada tardía, inhabilitación remota.

> **Dato clave.** Las tres familias del estándar: **teleservicios** (voz), **servicios portadores** (datos) y **servicios suplementarios** (las funciones profesionales). Los **servicios suplementarios** están normalizados en las **partes 9 a 12 de la EN 300 392**, y son **más de una treintena**. Que existan **normalizados** —y no como extensiones de fabricante— es una de las razones del éxito de TETRA.

#### 4.1. Servicios de voz y comunicaciones de grupo

##### 4.1.1. Llamadas individuales, de grupo y de difusión

**Los tipos de llamada, uno a uno.**

**Llamada de grupo (*group call*).** Es **el modo natural de TETRA**. Un usuario aprieta el PTT y su voz llega **a todos los miembros del grupo de conversación** que estén afiliados y en cobertura. Características:

- Es **semidúplex** (*half-duplex*): habla uno, escuchan todos; el canal se libera al soltar el PTT.
- Es **punto a multipunto**: la red replica el audio hacia todas las células donde haya afiliados, ocupando **un canal en cada una de ellas**, no uno por usuario.
- El **grupo es una entidad lógica**, identificada por su **GSSI**, no una frecuencia.
- Admite **entrada tardía** (*late entry*): quien se afilia o recupera cobertura con la llamada ya iniciada **se incorpora a ella**.
- Puede ser **abierta** (*open channel*), un canal permanentemente establecido en el que basta apretar el PTT sin señalización previa, muy usado en operativos.

**Llamada individual (*individual call*).** De un usuario a otro. Puede ser:

- **Semidúplex**, con PTT, como una llamada de grupo de dos personas.
- **Dúplex completo** (*full duplex*), como una llamada telefónica convencional: ambos hablan y escuchan a la vez. Consume **dos intervalos** (uno en cada sentido) y por eso se usa con moderación.

**Llamada de difusión (*broadcast call*).** Es una llamada **unidireccional de uno a muchos**: el emisor habla y los destinatarios **solo escuchan**, sin posibilidad de responder. Se usa para avisos generales del centro de mando a toda una flota o a todos los usuarios de la red. La clave es la **unidireccionalidad**.

**Llamada telefónica (*PABX/PSTN call*).** A través de las pasarelas de la **EN 300 392-4**, un terminal puede llamar a la centralita corporativa o a la red telefónica pública, y recibir llamadas de ellas, con las autorizaciones que fije el operador de la red.

> **Dato clave.** Los cuatro tipos: **grupo** (uno a muchos, **bidireccional**, semidúplex), **individual** (uno a uno, semidúplex o **dúplex completo**), **difusión** (uno a muchos, **unidireccional**: los receptores no pueden contestar) y **telefónica** (hacia PSTN/PABX). La diferencia entre **grupo** y **difusión** es que en la primera **cualquiera puede tomar la palabra** y en la segunda **no**.

**La gestión de grupos, que es donde está la potencia operativa.**

- **Afiliación**: un terminal se **afilia** a los grupos que tiene programados y autorizados; la red sabe en qué célula está cada afiliado y solo replica el audio donde hace falta.
- **Grupo seleccionado y grupos de escucha**: el usuario tiene **un grupo seleccionado** —en el que habla al apretar el PTT— y puede además **escuchar** otros en segundo plano (*scanning*), con prioridades entre ellos.
- **DGNA** (*Dynamic Group Number Assignment*), **asignación dinámica de número de grupo**: el centro de mando puede **crear un grupo nuevo y cargarlo en los terminales seleccionados por el aire**, sin tocar los equipos. Es la función que permite montar en segundos un grupo mixto para una emergencia concreta —policía, bomberos y sanitarios de un incidente— y disolverlo al terminar.
- **Grupos por patrón geográfico**: los grupos pueden asociarse a zonas, de modo que un terminal se afilie automáticamente al grupo del distrito en el que se encuentra.

> **Dato clave.** **DGNA = asignación dinámica de grupos por el aire desde el centro de control.** Es la función que hace impensable volver a la radio convencional: en convencional, cambiar la organización de grupos obliga a **reprogramar físicamente cada equipo**; con DGNA se hace desde una consola, en caliente y sobre los terminales elegidos.

**Los servicios suplementarios de voz que hay que saber nombrar:**

- **Escucha ambiente** (*ambience listening*): el centro de mando activa remotamente el micrófono de un terminal **sin que su portador lo sepa ni intervenga**, para oír lo que ocurre alrededor. Pensada para el agente que no responde o que está incapacitado.
- **Escucha discreta** (*discreet listening*): un usuario autorizado escucha una conversación en curso **sin que los participantes lo perciban**.
- **Inclusión** (*call inclusion*): un supervisor **se incorpora** a una llamada en curso.
- **Identificación de la parte llamante**: en pantalla aparece el **alias** de quien habla, algo que la radio analógica no podía dar.
- **Inhabilitación remota**: **desactivación temporal** (*stun*) o **permanente** (*kill*) de un terminal robado o extraviado, ordenada desde el centro de gestión.

> **Ejemplo de aplicación en el ayto.** La **escucha ambiente** y la **inhabilitación remota** son ejemplos de funciones con un **impacto directo en derechos** que exigen procedimiento escrito, autorización y registro. Un terminal municipal es un instrumento de trabajo entregado a un empleado público, y activar su micrófono a distancia o dejarlo inservible son actuaciones que deben estar **previstas, motivadas y trazadas**. En términos de la normativa de seguridad, la traza queda amparada por las medidas de **registro de actividad** del ENS; en términos de protección de datos, requieren información previa a la persona trabajadora y una base jurídica clara. El examen puede preguntar por la función técnica; el caso práctico, por la garantía que la rodea.

##### 4.1.2. Gestión de prioridades y llamadas de emergencia

**El principio.** En una red de emergencia, **no todas las comunicaciones valen lo mismo**. El sistema debe garantizar que, cuando el recurso escasea, se sirve primero a quien más lo necesita. TETRA lo resuelve con tres mecanismos escalonados.

**1. Prioridad de acceso (*priority call*).** Cada usuario y cada tipo de llamada llevan asociado un **nivel de prioridad**. Cuando varias peticiones compiten por el mismo canal libre, **se atiende primero la de mayor prioridad**; las demás quedan **en cola**, no rechazadas.

**2. Prioridad con desalojo (*pre-emptive priority call*).** Si **no hay ningún canal libre**, una llamada de prioridad suficiente puede **desalojar** una conversación en curso de prioridad inferior, que se corta para liberar el recurso. Es el mecanismo que garantiza que **una emergencia siempre entra**, aunque la red esté saturada.

**3. Llamada de emergencia (*emergency call*).** Es el nivel máximo. Se lanza con el **botón de emergencia** del terminal y desencadena, típicamente:

- Establecimiento **inmediato** en el grupo de emergencia, con **la máxima prioridad y desalojo**.
- **Alarma visual y sonora** en la consola de despacho, con la **identidad** y, si el terminal la envía, la **posición** del usuario.
- Apertura de un **canal de voz abierto** desde ese terminal, en algunas configuraciones sin necesidad de que el agente pulse el PTT —de modo que, si está incapacitado, el centro de mando **oye igualmente lo que ocurre**—.

> **Dato clave.** Los tres escalones: **prioridad de acceso** (ordena la cola) → **prioridad con desalojo** (*pre-emption*, **corta** una llamada en curso de menor prioridad) → **llamada de emergencia** (máxima prioridad, alarma en despacho, identidad y posición). La diferencia entre los dos primeros es exactamente la que hay entre **esperar mejor** y **echar a otro**.

**Las funciones asociadas al agente en riesgo.** Los terminales profesionales incorporan detecciones automáticas que disparan la alarma sin intervención del usuario:

- **«Hombre caído»** (*man down*): un acelerómetro detecta que el terminal ha quedado en posición horizontal e inmóvil durante un tiempo.
- **Alarma de inactividad** (*lone worker*): el terminal pide confirmación periódica y, si no la recibe, avisa.
- **Botón de emergencia oculto**, activable sin sacar el equipo.

> **Ejemplo de aplicación en el ayto.** El **CISEM** coordina Policía Municipal, Bomberos, SAMUR-Protección Civil y Agentes de Movilidad, con del orden de **3.000 incidentes diarios** `[CISEM]`. Sobre ese volumen, la gestión de prioridades no es un refinamiento teórico: es lo que asegura que una **alarma de agente en riesgo** entre por delante de las decenas de comunicaciones rutinarias que puedan estar cursándose en el mismo instante en la misma célula. Y la razón por la que ese comportamiento **no se puede replicar con teléfonos móviles comerciales**: en una red pública, el Ayuntamiento **no decide** a quién se desaloja.

#### 4.2. Servicios de datos

**El encuadre.** TETRA Release 1 nació con capacidades de datos modestas —recuérdese: **7,2 kbit/s netos por intervalo, 28,8 kbit/s agregando los cuatro**— pero muy bien pensadas para lo que un servicio de campo necesita: **mensajes cortos, estados y posiciones**, no navegación web ni vídeo. Conviene tenerlo presente para no juzgar el sistema con la vara equivocada.

##### 4.2.1. Servicio de mensajes cortos (SDS)

**Qué es el SDS.** El **SDS** (*Short Data Service*) es el servicio de **mensajería corta** de TETRA, equivalente funcional del SMS de la telefonía móvil pero mucho más versátil, porque se usa tanto para texto como para **telemetría, posiciones y órdenes máquina a máquina**. Sus mensajes viajan por los **canales de control**, sin necesidad de establecer un canal de tráfico, lo que los hace **muy rápidos y muy baratos en recursos**.

**Los tipos normalizados:**

| Tipo | Longitud de datos | Uso característico |
|----|----|----|
| **Mensaje de estado** (*status*) | **16 bits** precodificados | Estados operativos: «en ruta», «en el lugar», «disponible», «fuera de servicio». Se envía con una tecla |
| **SDS tipo 1** | **16 bits** | Datos muy breves definidos por el usuario |
| **SDS tipo 2** | **32 bits** | Ídem |
| **SDS tipo 3** | **64 bits** | Ídem |
| **SDS tipo 4** | **hasta 2.047 bits** definidos por el usuario | **Texto libre**, posiciones GNSS, mensajes de aplicación. Es el que se usa en la práctica |

Sobre el tipo 4 se define además el **SDS-TL** (*SDS Transport Layer*), una capa de transporte que añade **identificación del protocolo de aplicación, acuse de recibo y encadenamiento**, y que es la base sobre la que funcionan la mensajería de texto real, el envío de posición y las aplicaciones de gestión.

> **Dato clave.** **Estado = 16 bits precodificados**; **SDS tipo 1 = 16 bits, tipo 2 = 32 bits, tipo 3 = 64 bits, tipo 4 = hasta 2.047 bits** definidos por el usuario. La distinción **estado / SDS tipo 4** es la más importante: el **estado** es un código de una lista cerrada que se envía con una tecla y consume casi nada; el **tipo 4** es carga útil libre. El **SDS-TL** es la capa que le añade acuse de recibo y encadenamiento.

**El uso masivo del SDS: la localización.** La aplicación que más tráfico SDS genera en una red real es el **envío periódico de la posición GNSS** de cada terminal al sistema de gestión de flotas. Se transporta en SDS tipo 4 mediante el **protocolo de información de localización (LIP)** normalizado por el ETSI, que define cómo se codifican coordenadas, precisión, velocidad y rumbo, y **bajo qué condiciones se emite** (por tiempo, por distancia recorrida, por cambio de estado o a petición).

> **Ejercicio resuelto.** **Dimensionar el tráfico de localización de una flota municipal.** **Supuesto**: **1.500 terminales** envían su posición **cada 60 segundos** mediante SDS tipo 4. **Paso 1 — Mensajes por segundo**: 1.500 / 60 = **25 mensajes por segundo** en el conjunto de la red. **Paso 2 — ¿Es mucho?** Los SDS viajan por **canales de control**, que están permanentemente activos y **no consumen canal de tráfico**. Pero la capacidad de señalización de una célula **no es infinita**: si esos 25 mensajes por segundo se concentran en pocas células —el centro de la ciudad—, pueden competir con la señalización de establecimiento de llamada. **Paso 3 — Qué se hace en la práctica**: (a) **espaciar** el intervalo de emisión cuando el vehículo está parado y acortarlo cuando se mueve; (b) usar emisión **por distancia recorrida** en lugar de por tiempo; (c) distribuir en el tiempo los envíos para evitar que todos los terminales emitan en el mismo segundo; y (d) reservar capacidad de señalización para el establecimiento de llamada, que **siempre** tiene prioridad sobre la telemetría. **Conclusión y trampa**: la respuesta «no consume nada porque va por el canal de control» es **incorrecta**. Consume **capacidad de señalización**, que es un recurso finito y compartido con el establecimiento de llamadas. Es el error de diseño más común en despliegues de localización sobre TETRA.

##### 4.2.2. Transmisión de datos por paquetes y circuitos

**Datos por circuito (*circuit mode data*).** Se **reserva un canal de tráfico** para el usuario durante toda la sesión, igual que en una llamada de voz. Las tasas por intervalo dependen del nivel de protección de errores elegido:

| Protección          | Tasa por intervalo | Con los 4 intervalos |
|---------------------|--------------------|----------------------|
| **Sin protección**  | **7,2 kbit/s**     | **28,8 kbit/s**      |
| **Protección baja** | **4,8 kbit/s**     | 19,2 kbit/s          |
| **Protección alta** | **2,4 kbit/s**     | 9,6 kbit/s           |

Es un modo **ineficiente** para tráfico a ráfagas —el canal está reservado aunque no se transmita nada— pero **predecible**, y por eso se usa cuando hace falta un caudal garantizado: transferencia de un fichero, una imagen o una sesión de telemetría continua.

**Datos por paquetes (*packet data*, PD).** El terminal comparte los recursos con otros y **solo consume canal cuando hay paquetes que enviar**. TETRA transporta **IP** sobre este servicio mediante el protocolo **SNDCP** (*Subnetwork Dependent Convergence Protocol*) de la capa 3, de modo que, desde el punto de vista de la aplicación, **el terminal es un dispositivo IP más**. Es el modo adecuado para consultas a sistemas de información, mensajería de aplicación y sincronización de datos.

> **Dato clave.** **Circuito = recurso reservado, tasa garantizada, ineficiente para tráfico a ráfagas. Paquetes = recurso compartido, transporte de IP mediante SNDCP, eficiente para tráfico a ráfagas.** Y el techo de TETRA Release 1, que es la cifra que hay que retener: **28,8 kbit/s** con los cuatro intervalos y sin protección de errores. Ese techo es la razón de ser de **TEDS** (§5.4).

**Qué se puede y qué no se puede hacer con esas cifras.** Con 28,8 kbit/s en el mejor de los casos —y realistamente con 7,2 o 14,4 kbit/s— se pueden hacer: mensajería de texto, envío de posiciones, consultas a bases de datos con respuestas breves, formularios, telemetría, envío de una fotografía comprimida en decenas de segundos y actualización de datos operativos. **No** se pueden hacer: vídeo, transmisión de planos o imágenes grandes en tiempo real, acceso a aplicaciones web modernas ni transferencia de ficheros de tamaño ordinario.

> **Ejemplo de aplicación en el ayto.** Ese límite explica una realidad muy visible en la operativa municipal: los servicios de emergencia trabajan con **dos canales de datos en paralelo**. La **radio TETRA** transporta lo crítico y lo breve —estados, posiciones, órdenes, avisos— con disponibilidad garantizada; y una **conexión de datos comercial** (4G/5G) transporta lo voluminoso —imágenes, historia clínica, cartografía, vídeo— **sin garantía de disponibilidad**. La consecuencia operativa es clara y conviene tenerla presente en cualquier caso práctico: **lo que no puede fallar va por la radio propia; lo que aporta valor pero puede esperar va por la red comercial**. La convergencia de ambos mundos es lo que persigue la banda ancha crítica (§5.4).

> **Relación con otros temas.** El transporte de **IP** sobre un enlace de radio de baja capacidad, el efecto del retardo y de la pérdida sobre TCP y los mecanismos de compresión de cabeceras se tratan en el **Tema 34**. El diseño de aplicaciones que funcionen sobre enlaces así —peticiones pequeñas, tolerancia a la desconexión, sincronización diferida— es materia del **Tema 24**.

#### 4.3. Mecanismos de seguridad

**El planteamiento.** La seguridad de TETRA se apoya en **cuatro pilares**, y conviene tenerlos separados desde el principio porque cada uno protege de una cosa distinta:

1.  **Autenticación**: garantizar que el terminal es quien dice ser y —en la autenticación mutua— que la red también lo es.
2.  **Cifrado de la interfaz aire (AIE)**: proteger lo que viaja **entre el terminal y la estación base**.
3.  **Cifrado extremo a extremo (E2EE)**: proteger lo que viaja **entre terminal y terminal**, atravesando la infraestructura sin que ésta pueda leerlo.
4.  **Protección de identidades**: evitar que un observador pueda **identificar y seguir** a los usuarios.

A ellos se añaden la **inhabilitación remota** de terminales (§4.1.1) y la **gestión de claves**, incluida su distribución **por el aire (OTAR)**.

> **Dato clave.** La distinción decisiva del apartado: **el cifrado de interfaz aire protege el tramo radio y se descifra en la estación base**; **el cifrado extremo a extremo protege el contenido de punta a punta y la infraestructura no puede leerlo**. Son **complementarios**, no alternativos. Todo lo demás de esta sección se ordena alrededor de esa frase.

##### 4.3.1. Autenticación de usuarios y terminales

**El esquema, en cuatro pasos.** TETRA usa un mecanismo de **desafío-respuesta** con **clave simétrica**, normalizado en la **EN 300 392-7** `[EN392-7]` con los algoritmos del conjunto **TAA1** (*TETRA Authentication Algorithm set 1*):

1.  Cada terminal comparte con el **centro de autenticación** de la red una **clave de autenticación secreta**, denominada **K**, que **nunca viaja por el aire**.
2.  Cuando el terminal se registra, la red le envía un **desafío** (un número aleatorio).
3.  El terminal calcula una **respuesta** aplicando el algoritmo a la clave y al desafío, y la envía.
4.  La red hace el mismo cálculo por su cuenta y **compara**. Si coincide, el terminal queda autenticado.

**La autenticación mutua.** El mismo mecanismo puede ejecutarse **en sentido contrario**, de modo que **el terminal verifique a la red**. Es esencial: sin autenticación de la red, un atacante puede montar una **estación base falsa** que atraiga a los terminales de la zona —el equivalente radioeléctrico de un punto de acceso *rogue*— y desde ella degradar la seguridad, capturar tráfico o inyectar mensajes.

> **Dato clave.** La autenticación de TETRA es **simétrica, de desafío-respuesta**, con la clave **K** que **no se transmite nunca**, y **puede ser mutua**. La autenticación mutua es la defensa contra la **estación base falsa**. La familia de algoritmos original es **TAA1**; el conjunto nuevo, asociado al TEA set B, es **TAA2**, y trabaja con una clave de autenticación denominada **K2** `[TTR001-11]`.

**Y el subproducto más importante de la autenticación: la clave de sesión.** Del proceso de autenticación se **deriva** una clave de cifrado propia de ese terminal y de esa sesión, la **DCK** (*Derived Cipher Key*). Es decir: **autenticar y cifrar están encadenados**. Una red que no autentica no puede usar claves derivadas y tiene que conformarse con claves estáticas precargadas, mucho más débiles porque **son las mismas para todos y durante mucho tiempo**.

**La jerarquía de claves.**

| Clave | Nombre | Qué protege | Cómo se obtiene |
|----|----|----|----|
| **K** | *Authentication Key* | Es la raíz: **no cifra tráfico**, solo autentica | Precargada de forma segura; nunca viaja |
| **DCK** | *Derived Cipher Key* | Tráfico **individual** de ese terminal | **Se deriva de la autenticación** |
| **CCK** | *Common Cipher Key* | Tráfico y señalización **dirigidos a grupo** dentro de un área de localización | La genera la red y la distribuye **cifrada con la DCK**, por OTAR |
| **SCK** | *Static Cipher Key* | Tráfico, en redes **sin autenticación** y en **modo directo** | **Precargada**; es la opción más débil |
| **GCK** | *Group Cipher Key* | Un **grupo concreto**, con independencia de la célula | No se usa directamente en el aire: se combina con CCK o SCK para dar la **MGCK** |
| **MGCK** | *Modified Group Cipher Key* | La que efectivamente cifra el tráfico de grupo protegido | **GCK modificada** por CCK o SCK |

**OTAR** (*Over The Air Re-keying*), **la distribución de claves por el aire**, es lo que hace manejable todo lo anterior: permite **renovar las claves de miles de terminales sin recogerlos**, algo imprescindible cuando una clave se compromete o cuando se da de baja a un usuario. Las claves viajan **selladas** con otra clave, nunca en claro.

> **Relación con otros temas.** Los conceptos de **clave simétrica**, **desafío-respuesta**, **derivación de claves** y **gestión del ciclo de vida de las claves** se desarrollan en el **Tema 32**. La obligación jurídica de proteger el material criptográfico está en la medida **`op.exp.10`, «protección de claves criptográficas», del ENS** `[ENS]`, y es directamente aplicable a la gestión de claves de una red TETRA municipal.

##### 4.3.2. Cifrado en la interfaz aire

**Qué protege y qué no.** El **cifrado de interfaz aire** (**AIE**, *Air Interface Encryption*) cifra **todo lo que viaja por radio entre el terminal y la estación base**: la voz, los datos, la señalización y —si se activa el cifrado de identidades— las propias identidades. Se aplica en la **capa 2** del interfaz aire. **Se descifra en la estación base**: a partir de ahí, la comunicación circula por la infraestructura del operador de la red **en claro**, salvo que se aplique cifrado adicional en el transporte o cifrado extremo a extremo.

> **Dato clave.** El AIE **no protege frente al propio operador de la red**, porque el tráfico se descifra en la estación base. Protege frente a **quien escucha el aire**. Es exactamente la razón por la que los usuarios más exigentes añaden **cifrado extremo a extremo** (§4.3.3).

**Las clases de seguridad.** El estándar define tres, y hay que saberlas `[TTR001-11]`:

| Clase | Denominación | Qué usa | Comentario |
|----|----|----|----|
| **SC1** | Clase de seguridad 1 | **Sin cifrado** del interfaz aire | Puede usarse autenticación y cifrado de identidades (ESI), pero el tráfico va **en claro** |
| **SC2** | Clase de seguridad 2 | **Clave estática, SCK** | Cifrado con clave precargada. **No exige autenticación**. Es también la clase del **modo directo** |
| **SC3** | Clase de seguridad 3 | **Clave derivada (DCK) + clave común (CCK)** | Exige **autenticación**; la clave es distinta por terminal y se renueva. Es la configuración recomendada |
| **SC3G** | Clase 3 con **GCK** | DCK + CCK + **GCK/MGCK** | Añade cifrado propio por grupo |

El informe técnico de la TCCA recoge además un detalle operativo relevante: la red puede usar **SC2 como modo de repliegue** para células que temporalmente **no pueden sostener SC3** —por ejemplo, porque han perdido el enlace con el centro de autenticación—, con notificación anticipada del cambio de clase `[TTR001-11]`.

**El cifrado de identidades.** Para evitar que un observador identifique y siga a los usuarios, TETRA cifra las identidades cortas: la **ESI** (*Encrypted Short Identity*) sustituye la identidad por una versión cifrada, y el TEA set B añade la **MAE** (*MAC Address Encryption*) `[TTR001-11]`.

**Los algoritmos: TEA set A.** El cifrado se realiza con generadores de flujo de clave denominados **TEA** (*TETRA Encryption Algorithm*). El conjunto original, **TEA set A**, tiene cuatro:

| Algoritmo | Destinatario previsto | Régimen de exportación |
|----|----|----|
| **TEA1** | **Uso civil general e infraestructuras críticas**, con exportación mundial | **Longitud de clave efectiva reducida** para cumplir controles de exportación |
| **TEA2** | **Servicios de emergencia europeos** (esquema Schengen) | Restringido |
| **TEA3** | Servicios de emergencia y militares **fuera de Europa**, en países afines | Restringido |
| **TEA4** | Uso civil general, variante de TEA1 | Restringido |

> **Dato clave.** **TEA1 y TEA4** son los de uso **civil y exportación amplia**; **TEA2** es el de las **redes de emergencia europeas**; **TEA3**, el de emergencia y militar **extraeuropeo**. La clave nominal de todos ellos es de **80 bits**, pero **TEA1 tiene una reducción deliberada de la longitud efectiva**. Los algoritmos fueron **secretos** durante casi treinta años; el ETSI publicó la especificación del **TEA set A** en la **TS 104 053-1** en **febrero de 2025** `[TS104053]`.

**TETRA:BURST: la investigación que cambió el escenario.** En **agosto de 2023**, el equipo neerlandés **Midnight Blue** publicó, tras un proceso de divulgación coordinada y con un artículo revisado en **USENIX Security 2023**, cinco vulnerabilidades bautizadas como **TETRA:BURST** `[TETRABURST]`. Las cuatro citables son:

- **CVE-2022-24402 — la puerta trasera de TEA1.** La clave de **80 bits** de TEA1 se **comprime deliberadamente** a una longitud efectiva de **unos 32 bits**, lo que permite **romperla por fuerza bruta en minutos con un ordenador doméstico**. La TCCA ha confirmado que la reducción fue intencionada y la justifica en el cumplimiento del **Acuerdo de Wassenaar** de control de exportación de tecnología criptográfica `[TCCA-RD]`.
- **CVE-2022-24401 — el oráculo de descifrado.** El generador del flujo de clave del AIE depende del **tiempo de red**, que la estación base **difunde sin autenticar**. Manipulándolo, un atacante puede forzar la **reutilización del flujo de clave** y descifrar comunicaciones.
- **CVE-2022-24403 — desanonimización.** El esquema de ofuscación de identidades tiene un diseño débil que permite **identificar y seguir** a los usuarios.
- **CVE-2022-24404 — maleabilidad.** La falta de autenticación del texto cifrado permite **alterar el mensaje cifrado** sin ser detectado.

**La respuesta del ETSI: TEA set B.** En **octubre de 2022** —antes de la publicación de la investigación, con la que la divulgación estaba coordinada— el ETSI liberó un **nuevo conjunto de algoritmos**, el **TEA set B**, con tres piezas `[TCCA-B]`:

| Nuevo | Sustituye a | Destinatario |
|----|----|----|
| **TEA5** | TEA2 | **Redes de emergencia europeas** |
| **TEA6** | TEA3 | Redes de emergencia y militares extraeuropeas afines |
| **TEA7** | TEA1 | **Infraestructuras críticas y uso civil general** — es el único del set B disponible para uso civil amplio |

El TEA set B trabaja con **claves extendidas** —SCKX, DCKX, CCKX, GCKX— y con el nuevo conjunto de autenticación **TAA2** y su clave **K2** `[TTR001-11]`. Según la TCCA, **TEA5 y TEA6 usan claves de 192 bits**, mientras que **TEA7 conserva una reducción de la longitud efectiva a 56 bits** por las mismas razones de control de exportación que en su día afectaron a TEA1 `[TCCA-RD]`.

> **Dato clave.** **TEA set B = TEA5, TEA6 y TEA7, liberado en octubre de 2022.** Correspondencias: **TEA5 ← TEA2**, **TEA6 ← TEA3**, **TEA7 ← TEA1**. Y el matiz clave: **TEA7, el civil, sigue teniendo una longitud de clave efectiva reducida (56 bits)** por el régimen de exportación, mientras que TEA5 y TEA6 llevan **192 bits**. La lección de fondo, muy citable: **la debilidad de TEA1 no fue un error de diseño, sino una decisión de política de exportación**.

**2TETRA:2BURST (agosto de 2025).** El mismo equipo presentó en **Black Hat USA el 7 de agosto de 2025** una segunda tanda `[2TETRA]`, y su alcance es mayor porque **llega al cifrado extremo a extremo**:

- **CVE-2025-52944** — **el protocolo TETRA carece de autenticación de mensajes**, lo que permite **inyectar mensajes arbitrarios**. Es la más estructural de todas.
- **CVE-2025-52943** — en redes **multicifrado**, admitir **TEA1** junto a otros algoritmos permite **recuperar la clave** también de los demás. Traducción operativa: **no basta con dejar de usar TEA1; hay que dejar de soportarlo**.
- **MBPH-2025-001** — la corrección publicada por el ETSI para **CVE-2022-24401** **no impide** la recuperación del flujo de clave.
- **CVE-2025-52940, 52941 y 52942** — afectan al **cifrado extremo a extremo** y se tratan en §4.3.3.

> **Dato clave.** Dos hallazgos de 2025 con consecuencia práctica inmediata para un gestor de red: **(1) soportar TEA1 «por compatibilidad» compromete también a los algoritmos fuertes de la misma red** (CVE-2025-52943); y **(2) el protocolo no autentica los mensajes** (CVE-2025-52944), de modo que la integridad depende de las capas superiores. La primera es la que convierte «desactivar TEA1» en una **decisión de configuración obligatoria**, no en una recomendación.

**Cómo debe leerse todo esto, sin alarmismo y sin complacencia.** Tres precisiones que conviene sostener en un examen o en un informe:

1.  **Ninguna de estas vulnerabilidades hace inútil a TETRA.** Explotarlas exige proximidad radioeléctrica, equipamiento específico y capacidad técnica alta; el perfil de atacante es de gama alta, no oportunista.
2.  **Pero sí obligan a decisiones concretas**: usar **SC3** con **autenticación mutua**, **no soportar TEA1**, migrar a **TEA set B** y **TAA2** cuando el parque lo permita, activar el **cifrado de identidades**, aplicar los parches del fabricante y **añadir cifrado extremo a extremo** en las comunicaciones sensibles.
3.  **Y dejan una lección de método**: la seguridad por oscuridad falló. Los algoritmos estuvieron **secretos treinta años** y su debilidad se descubrió **en cuanto se pudieron examinar**. La publicación del TEA set A en 2025 es el reconocimiento implícito de ese principio.

> **Ejemplo de aplicación en el ayto.** Para una red municipal, la traducción de lo anterior a un pliego es directa y es exactamente lo que un examinador espera ver: exigir **clase de seguridad SC3** con **autenticación mutua** como configuración por defecto; **prohibir expresamente TEA1** en la red, no solo «no usarlo»; exigir **capacidad de migración a TEA set B y TAA2** en los terminales que se adquieran a partir de ahora; exigir **OTAR** para poder renovar claves sin recoger 4.500 equipos; y exigir **procedimiento documentado de inhabilitación remota** de terminales perdidos. Todo ello con respaldo normativo en el ENS: **`mp.com.2`** (confidencialidad), **`mp.com.3`** (integridad y autenticidad), **`mp.si.2`** (criptografía) y **`op.exp.10`** (protección de claves criptográficas) `[ENS]`.

##### 4.3.3. Cifrado extremo a extremo (E2EE)

**Qué añade.** El **cifrado extremo a extremo** (**E2EE**) cifra la información **en el terminal emisor** y la descifra **en el terminal receptor**, de modo que **atraviesa toda la infraestructura sin que ésta pueda leerla**. Es una capa **superior e independiente** del cifrado de interfaz aire, y se aplica **sobre la carga útil** —la voz codificada o el SDS— antes de que ésta entre en la pila de protocolos.

**De qué protege que el AIE no proteja:**

- Del **operador de la red**, si es un tercero (una empresa que presta el servicio, otra Administración que aloja la infraestructura).
- Del **personal técnico** con acceso a los equipos de conmutación o a las grabaciones.
- De un **compromiso de la infraestructura**, incluidas las estaciones base y los enlaces de transporte.
- De la **interconexión con otras redes**, donde el tráfico pasa por sistemas ajenos.

**Cómo se implementa.** El ETSI **no impone un algoritmo** de E2EE: define el **marco** —cómo se sincroniza, cómo se transporta el material cifrado dentro de la trama de voz, cómo se gestionan las claves— y deja que cada comunidad de usuarios elija su criptografía. Históricamente se usó **IDEA**; hoy predomina **AES**, en variantes de 128 o 256 bits. La gestión de claves E2EE es **independiente** de la de la red: normalmente se apoya en un **centro de gestión de claves propio del usuario final**, con distribución por OTAR o por carga física, y las claves **no las conoce el operador**.

**El coste que hay que asumir.** El E2EE tiene tres contrapartidas honestas que un informe debe recoger:

1.  **La red no puede procesar lo que no entiende.** Las pasarelas telefónicas, la grabación centralizada en claro y la interconexión con redes de otra tecnología **dejan de funcionar** sobre el tráfico cifrado extremo a extremo, salvo que se prevean puntos de descifrado autorizados.
2.  **La gestión de claves es responsabilidad del usuario**, y su complejidad crece con el tamaño de la flota y con la necesidad de interoperar con otros organismos.
3.  **Consume capacidad**: la sincronización del cifrado ocupa bits que salen del caudal de voz, con un impacto pequeño pero no nulo.

> **Dato clave.** **AIE = terminal ↔ estación base; se descifra en la red. E2EE = terminal ↔ terminal; la red no puede leerlo.** Se usan **juntos**. El ETSI **no normaliza el algoritmo de E2EE**, solo el marco de transporte y sincronización; el algoritmo predominante hoy es **AES**.

**El hallazgo de 2025 sobre el E2EE.** La segunda tanda de Midnight Blue alcanzó precisamente a esta capa `[2TETRA]`:

- **CVE-2025-52941** — se identificó una **variante debilitada de AES-128** en la que la **entropía efectiva se reduce a 56 bits** en lugar de 128. Es, funcionalmente, **el mismo patrón que el de TEA1**, ahora en la capa que se suponía la última línea de defensa.
- **CVE-2025-52940** — la voz cifrada extremo a extremo es vulnerable a **ataques de repetición** e **inyección de voz**.
- **CVE-2025-52942** — los **SDS** cifrados extremo a extremo **carecen de protección antirrepetición**, de modo que un mensaje capturado puede reinyectarse tal cual.

> **Dato clave.** El **E2EE no es una garantía automática**: depende del algoritmo **concreto** que se haya implantado y de si incorpora **protección antirrepetición** y **autenticación del mensaje**. La lección para un pliego es que **no basta con exigir «cifrado extremo a extremo»**: hay que exigir **algoritmo y longitud de clave nombrados**, **protección frente a repetición** y **autenticación del contenido**, y reservarse el derecho de auditar la implementación.

> **Relación con otros temas.** La distinción entre **cifrado en tránsito por tramos** y **cifrado extremo a extremo**, y la razón por la que el segundo no sustituye al primero, es la misma que aparece en el **Tema 35** a propósito de TLS y en el **Tema 36** a propósito de las VPN. Los conceptos de **entropía de clave**, **ataque de repetición** y **autenticación de mensaje** están en el **Tema 32**.

------------------------------------------------------------------------

### 5. Ámbito público, normativa y evolución tecnológica

> **Material complementario.** El enunciado oficial de este tema no nombra este apartado. Se mantiene porque sitúa la materia en el Ayuntamiento y en la normativa que le aplica, pero lo exigible es lo que enumera el título del tema.

#### 5.1. Uso de TETRA en servicios de emergencia y seguridad pública

**Por qué TETRA se impuso en este sector.** Las funciones descritas en §4 no son adornos: cada una responde a una necesidad operativa que la telefonía comercial no cubre. Puestas en fila, explican la elección:

| Necesidad operativa | Lo que aporta TETRA | Lo que ofrece un móvil comercial |
|----|----|----|
| Hablar **a todo un equipo** a la vez | **Llamada de grupo** nativa, con un botón | Grupos de mensajería o multiconferencia, con establecimiento lento |
| **Inmediatez** | Establecimiento **\< 300 ms** | Segundos |
| **Garantía de acceso** en saturación | **Prioridad y desalojo** decididos por el titular de la red | Ninguna; el operador no da prioridad al ayuntamiento |
| Funcionar **sin infraestructura** | **Modo directo (DMO)** | Imposible |
| Funcionar **cuando cae la luz** | Emplazamientos con **baterías y grupos electrógenos** dimensionados por el titular | Depende del respaldo de un tercero |
| **Confidencialidad** de la comunicación operativa | **AIE + E2EE** con claves propias | Cifrado del operador, sin control del usuario |
| **Trazabilidad** | Grabación e identidad en todas las transmisiones | No integrada |
| **Terminal de trabajo** | Robusto, con PTT, botón de emergencia, «hombre caído» | Terminal de consumo |

> **Dato clave.** Las **cinco** razones que justifican una red propia de radio frente a la telefonía comercial, y que conviene saber enumerar de corrido: **grupo, inmediatez, prioridad garantizada, funcionamiento sin infraestructura y control de la disponibilidad por su titular**. Ninguna de ellas es una cuestión de calidad de audio ni de cobertura: son cuestiones de **control**.

**El mapa español, que es donde está la trampa del tema.** En España conviven tres niveles de red de emergencia, y **no todos usan la misma tecnología**:

| Nivel | Red | Tecnología | Usuarios |
|----|----|----|----|
| **Estatal** | **SIRDEE** | **TETRAPOL** | Fuerzas y Cuerpos de Seguridad del Estado, Defensa y, con terminales cedidos, otros servicios de emergencia |
| **Autonómico** | Redes propias de las comunidades autónomas | **TETRA** en la mayoría de los casos | Bomberos autonómicos, agentes forestales, emergencias sanitarias, 112, protección civil, policías locales adheridas |
| **Local** | Redes municipales de las grandes ciudades | **TETRA** | Policía local, bomberos municipales, emergencias, servicios urbanos |

> **Dato clave.** **El SIRDEE —Sistema de Radiocomunicaciones Digitales de Emergencia del Estado, en servicio desde el año 2000— está construido sobre TETRAPOL, no sobre TETRA** `[SIRDEE]`. Es **la** confusión del tema. La razón histórica es que su despliegue se decidió a finales de los años noventa, cuando TETRA aún no estaba maduro comercialmente y TETRAPOL sí. Las redes **autonómicas y municipales**, decididas más tarde, se hicieron en su mayoría **con TETRA**. La consecuencia práctica es que **la interoperabilidad entre el nivel estatal y los otros dos no puede resolverse con la ISI**, sino con pasarelas o con acoplamiento en los centros de mando (§2.3.2).

**La red autonómica madrileña.** La Comunidad de Madrid opera su propia red TETRA, gestionada por la **Agencia de Seguridad y Emergencias Madrid 112 (ASEM 112)**, con **113 estaciones base** y **5.316 terminales** `[CM-TETRA]`. Da servicio al **Cuerpo de Bomberos**, **Agentes Forestales**, brigadas forestales, **ERIVE** de protección civil, personal sanitario del **SUMMA 112**, grupos de protección civil, **policías locales** adheridas a la estrategia de seguridad autonómica y la **Dirección General de Carreteras**. La red permite además la **geolocalización de cada terminal**, cuya posición se envía al centro de control del servicio correspondiente. Los datos económicos recientes: casi **40 millones de euros a cinco años** para su modernización y gestión (agosto de 2025) y **6,1 millones** en el ejercicio 2025, con **2.263 terminales nuevos** repartidos entre Bomberos (1.600), Agentes Forestales (412), Protección Civil (140), Carreteras (66) y Madrid 112 (45) `[CM-TETRA]`.

**Y un dato de 2026 que vale por toda una argumentación.** En **mayo de 2026**, la Comunidad de Madrid dotó de un terminal TETRA a **53 municipios pequeños** que no lo tenían, para garantizar su contacto con el 112. El motivo declarado es el análisis del **apagón del 28 de abril de 2025**: el estudio posterior constató que **las redes TETRA mantuvieron su operatividad durante el corte de suministro**, porque los repetidores cuentan con **baterías de respaldo**, mientras la telefonía convencional y el acceso a internet se degradaron `[CM-TETRA]`.

> **Dato clave.** El **apagón peninsular del 28 de abril de 2025** es el argumento empírico más potente a favor de una red de radio propia: **la red TETRA siguió funcionando cuando la telefonía comercial no**, gracias al **respaldo energético de los emplazamientos**. La lección de fondo no es sobre radio, sino sobre **dependencias**: un servicio crítico solo es resiliente si lo son **todas** sus dependencias, empezando por la energía.

> **Ejemplo de aplicación en el ayto.** La red municipal, sobre plataforma **DIMETRA-TETRA**, da servicio a **Policía Municipal, Bomberos, SAMUR-Protección Civil, Agentes de Movilidad, SAMUR Social y Parques y Jardines**, coordinando a **más de 3.000 efectivos**, y su mantenimiento integral y evolución tecnológica se adjudicaron en **marzo de 2026** por **cinco años**, con **disponibilidad 24×7** `[TELEFONICA-2026]`. En **julio de 2026**, la Junta de Gobierno aprobó además el contrato de **operación, gestión, supervisión y mantenimiento de las infraestructuras, equipos y redes de radiocomunicaciones** de la Dirección General de Policía Municipal, con **933.000 euros** de presupuesto plurianual y **tres años** de duración prorrogables `[AYTO-CONTR]`. Obsérvese que son **dos contratos distintos**: uno sobre **la plataforma** y otro sobre **la operación y las redes de un cuerpo concreto**. Distinguir el objeto de cada uno es exactamente el tipo de precisión que se pide en un caso práctico.

**Otros usos de TETRA que conviene citar.** Fuera de la seguridad pública, TETRA se emplea en **transporte** (metros, ferrocarriles, aeropuertos, puertos, flotas de autobuses), **energía y agua** (redes de distribución, telemando), **industria** (minería, petroquímica), **grandes recintos** y **defensa**. El caso más visible en Madrid es el **Metro**, con despliegues de TETRA por tramos para comunicar el Puesto de Mando con estaciones y trenes `[METRO]`.

> **Relación con otros temas.** El encuadre de estas redes como **infraestructura crítica** —con las obligaciones de la **Ley 8/2011** y de la futura transposición de **NIS2**— enlaza con el **Tema 32** (seguridad de los sistemas de información) y con el **Tema 39** (ENS). La coordinación entre administraciones en emergencias es materia de la **Ley 17/2015** del Sistema Nacional de Protección Civil.

#### 5.2. Marco normativo y regulación del espectro radioeléctrico

**El punto de partida: el espectro es dominio público.** El art. **85.1** de la Ley 11/2022 lo dice sin matices: «**El espectro radioeléctrico es un bien de dominio público, cuya titularidad y administración corresponden al Estado**» `[LGTel]`. De ahí se deducen tres consecuencias: **(1)** nadie es propietario de una frecuencia; **(2)** su uso requiere **título habilitante** estatal; y **(3)** ese título está **sujeto a condiciones**, tiene **plazo** y puede **modificarse o revocarse**.

**La pirámide normativa del espectro, de arriba abajo:**

1.  **Reglamento de Radiocomunicaciones de la UIT**, tratado internacional que reparte el espectro entre servicios y **regiones** (España está en la **Región 1**), revisado por las **Conferencias Mundiales de Radiocomunicaciones**; la última incorporada es la **CMR-23**.
2.  **Derecho de la Unión Europea**: decisiones de armonización de la Comisión y **decisiones y recomendaciones de la CEPT/ECC**, que son las que fijan bandas comunes europeas. Las tres relevantes aquí: **ECC/DEC(08)05** (emergencias en 380-385/390-395 MHz), **ECC/DEC(06)06** (PMR/PAMR digital de banda estrecha) y **ECC/DEC(16)02** (PPDR de banda ancha).
3.  **Ley 11/2022, General de Telecomunicaciones**, título V, arts. 85 y siguientes.
4.  **Real Decreto 123/2017**, Reglamento sobre el uso del dominio público radioeléctrico, cuyo **art. 6** ordena aprobar el CNAF.
5.  **CNAF**, aprobado por **Orden TDF/732/2026, de 10 de julio**, con sus **notas de utilización nacional (UN)**.

**Las tres modalidades de uso, art. 88.1 de la Ley 11/2022** `[LGTel]`:

| Modalidad | Definición legal | Ejemplos |
|----|----|----|
| **Común** | **No precisa título habilitante**; se realiza en las bandas y con las características que se establezcan | Wi-Fi, mandos a distancia, dispositivos de corto alcance |
| **Especial** | Bandas habilitadas para **explotación compartida**, **sin limitación de número** de operadores o usuarios | Radioafición, banda ciudadana |
| **Privativo** | Explotación **en exclusiva o por un número limitado de usuarios** de determinadas frecuencias en un mismo ámbito físico | Telefonía móvil, radiodifusión y **las redes TETRA de emergencia** |

**Las cuatro formas de título habilitante, art. 88.3:** **autorización general**, **autorización individual**, **afectación** y **concesión** administrativas. Y ahora el precepto que hay que saber literalmente:

> **Dato clave.** **Art. 88.5.b) de la Ley 11/2022**: el derecho de uso **privativo para autoprestación** se otorga mediante **autorización individual**, «**salvo en el caso de Administraciones públicas, que requerirán de afectación demanial**» `[LGTel]`. Es decir: **la red TETRA de un ayuntamiento se ampara en una AFECTACIÓN DEMANIAL, no en una concesión ni en una autorización individual**. Y una **concesión administrativa** exige además, según el art. 88.6, que el solicitante **ostente la condición de operador de comunicaciones electrónicas**, que no es el caso de un ayuntamiento que se autopresta el servicio. Éste es el dato jurídico más específico del tema y el que distingue una respuesta buena de una excelente.

**La duración.** El art. **94.1** fija que los derechos de uso privativo **sin limitación de número** se otorgan «por un período que finalizará el **31 de diciembre del año natural en que cumplan su quinto año de vigencia**», **renovables por períodos de cinco años** en función de las disponibilidades y de la planificación `[LGTel]`. Es decir: **cinco años, con renovación periódica**, no indefinido.

**Las condiciones asociadas.** El art. **91** somete el título a condiciones sobre uso efectivo y eficiente, características técnicas, prevención de interferencias, límites de exposición y pago de la **tasa por reserva del dominio público radioeléctrico**. El incumplimiento puede llevar a la **modificación, extinción o revocación** del título (art. 95).

**Y la calificación jurídica del servicio.** El art. **4.1** de la Ley 11/2022 contiene una declaración con mucho recorrido: «**Sólo tienen la consideración de servicio público los servicios regulados en este artículo**», y el artículo se titula precisamente «**Servicios de telecomunicaciones para la seguridad nacional, la defensa nacional, la seguridad pública, la seguridad vial y la protección civil**» `[LGTel]`. Es decir: en un ordenamiento que declara las telecomunicaciones **servicios de interés general prestados en libre competencia**, las comunicaciones para **seguridad pública y protección civil** son la **excepción** expresamente calificada como servicio público.

> **Dato clave.** **Art. 4.1 de la Ley 11/2022**: los servicios de telecomunicaciones para la **seguridad nacional, la defensa, la seguridad pública, la seguridad vial y la protección civil** son **los únicos** que tienen la consideración de **servicio público**. Es el fundamento jurídico de fondo de todo este tema y encaja con el art. **2**, que declara al resto de las telecomunicaciones servicios **de interés general en régimen de libre competencia**.

> **Ejercicio resuelto.** **Determinar el régimen jurídico completo de la red TETRA de un ayuntamiento.** **Pregunta**: un ayuntamiento explota una red TETRA propia para sus servicios de seguridad y emergencias. ¿Qué modalidad de uso del espectro es, qué título habilitante necesita, cuánto dura y qué obligaciones asume? **Paso 1 — Modalidad de uso.** Emplea **frecuencias determinadas en exclusiva** en su ámbito físico → **uso privativo** (art. 88.1). **Paso 2 — ¿Autoprestación o prestación a terceros?** La red sirve **a los propios servicios municipales**, no se vende a terceros → **autoprestación**. **Paso 3 — Título habilitante.** Uso privativo + autoprestación + **Administración pública** → **afectación demanial** (art. **88.5.b**). **No** es autorización individual (que sería la de un particular en autoprestación) ni concesión (que exigiría ser operador, art. 88.6). **Paso 4 — Duración.** Régimen general del art. **94.1**: hasta el **31 de diciembre del quinto año**, **renovable por períodos de cinco años**. **Paso 5 — Bandas.** Según el servicio: **380-385 / 390-395 MHz** si es red de servicios de emergencia (nota **UN-28**); **410-415,3 / 420-425,3 MHz** si es TETRA civil (nota **UN-31**), con canalización de **25 kHz** y dúplex de **10 MHz**. **Paso 6 — Obligaciones.** Condiciones del art. **91** (uso eficaz y eficiente, características técnicas, no interferencia, exposición radioeléctrica), **tasa por reserva del dominio público radioeléctrico**, y —por ser un sistema de información del sector público— las medidas del **ENS** que le apliquen según su categoría. **Paso 7 — Y una precisión final.** Si el ayuntamiento **cediera capacidad excedente** de su red a terceros, cambiaría la calificación de la actividad y entrarían en juego las obligaciones de la Ley 11/2022 sobre redes de las Administraciones públicas. La autoprestación **pura** es lo que sostiene el régimen anterior.

**El ENS aplicado a una red de radio.** Un sistema de radiocomunicaciones municipal es un **sistema de información del sector público** y le aplica el **Esquema Nacional de Seguridad**. Las medidas más directamente pertinentes `[ENS]`:

- **`mp.com.1` — Perímetro seguro**, **`mp.com.2` — Protección de la confidencialidad** y **`mp.com.3` — Protección de la integridad y de la autenticidad**: dan cobertura normativa al cifrado y a la autenticación del interfaz aire.
- **`mp.com.4` — Separación de flujos de información en la red**, con su requisito **`mp.com.4.2`**: «**si se emplean comunicaciones inalámbricas, será en un segmento separado**». Es la medida que exige que la red radio **no comparta segmento** con la ofimática municipal. Sus refuerzos: **R1** segmentación lógica con **VLAN** (con subredes mínimas de usuarios, servicios y administración), **R2** con **VPN**, **R3** con **medios físicos separados** y **R4** control en los **puntos de interconexión**. Obsérvese que **no aplica en categoría BÁSICA**, y que en MEDIA exige **\[R1 o R2 o R3\]**.
- **`mp.if.1` a `mp.if.7` — Protección de las instalaciones**: áreas separadas con control de acceso, identificación de personas, acondicionamiento de los locales, **`mp.if.4` energía eléctrica**, incendios, inundaciones y registro de entrada y salida de equipamiento. Se aplican a **cada emplazamiento de estación base**, no solo al CPD.
- **`op.cont.1` a `op.cont.4` — Continuidad del servicio**: análisis de impacto, plan de continuidad, pruebas periódicas y **medios alternativos**.
- **`mp.si.2` — Criptografía** y **`op.exp.10` — Protección de claves criptográficas**.

> **Dato clave.** **`mp.com.4.2` del ENS: «si se emplean comunicaciones inalámbricas, será en un segmento separado»** `[ENS]`. Es el precepto que se cita cuando alguien propone conectar la consola de despacho a la red ofimática general o dar salida a internet desde el segmento de la red radio. Y **`mp.if.4`, energía eléctrica**, es el que respalda exigir baterías y grupos electrógenos en los emplazamientos: aplica **ya en categoría BÁSICA**, con refuerzo **R1** en MEDIA y ALTA.

#### 5.3. Requisitos de disponibilidad, resiliencia y calidad de servicio (QoS)

**El nivel de exigencia.** En una red de emergencia, la disponibilidad no se expresa en «tres nueves»: se expresa en **99,99 %** o superior, y se acompaña de un requisito adicional que las redes ordinarias no tienen: **la red debe seguir funcionando precisamente cuando el entorno falla**, porque es entonces cuando más se necesita. Una red comercial se degrada con la emergencia; una red de emergencia debe resistirla.

**Las capas de resiliencia, de fuera adentro:**

**1. Energía.** Es la primera y la que el apagón de abril de 2025 puso a prueba. Cada emplazamiento debe tener **baterías** dimensionadas para varias horas y, en los principales, **grupo electrógeno** con combustible y procedimiento de reposición. El ENS lo respalda en **`mp.if.4`** `[ENS]`.

**2. Transporte.** El enlace entre estaciones base y nodos debe estar **duplicado por caminos físicamente diversos**, y conviene que las tecnologías sean distintas (fibra + radioenlace), para que un mismo suceso no corte las dos.

**3. Nodos.** Conmutación **redundante**, preferiblemente **geográficamente distribuida**, de modo que la pérdida de un centro no deje sin servicio a la red.

**4. Radio.** **Solapamiento de cobertura** entre células, de forma que la caída de una estación base degrade el servicio en lugar de anularlo, y **redundancia de portadoras** en los emplazamientos críticos.

**5. Modos degradados.** Son la especialidad de TETRA y lo que la distingue de una red IP convencional:

- **Repliegue local** (*local site trunking*): la estación base aislada del núcleo **sigue troncalizando** dentro de su célula.
- **Modo directo (DMO)**: aunque caiga toda la red, los terminales **siguen hablando entre sí**.
- **Repliegue de clase de seguridad**: si se pierde el enlace con el centro de autenticación, la célula puede pasar de **SC3 a SC2** para seguir cifrando con clave estática `[TTR001-11]`.

**6. Procedimientos y personas.** Plan de continuidad probado, guardia 24×7, repuestos, y **ejercicios periódicos**. El ENS lo exige en **`op.cont.2`** (plan de continuidad), **`op.cont.3`** (**pruebas periódicas**) y **`op.cont.4`** (medios alternativos) `[ENS]`.

> **Dato clave.** Los **tres modos degradados** de TETRA, ordenados de menos a más severo: **repliegue local de la estación base** (pierde el núcleo, conserva la troncalización en su célula) → **modo directo** (pierde toda la red, conserva la comunicación terminal a terminal) → **repliegue de clase de seguridad SC3 → SC2** (pierde la autenticación, conserva el cifrado con clave estática). Que un sistema **degrade en escalones** en lugar de caer de golpe es el rasgo de diseño que define a las comunicaciones críticas.

**La calidad de servicio operativa.** Además de la disponibilidad, hay parámetros que se miden y se contratan:

| Parámetro | Objetivo típico |
|----|----|
| **Tiempo de establecimiento** de llamada de grupo | **\< 300 ms** |
| **Probabilidad de bloqueo** en hora punta | Muy baja, con dimensionado para el escenario de gran emergencia |
| **Cobertura** | Porcentaje de la superficie y de la **población servida en interiores**, no solo en exteriores |
| **Inteligibilidad de la voz** | Medida en el borde de la célula, no en el centro |
| **Retardo de extremo a extremo** | Acotado, para que el diálogo sea natural |
| **Disponibilidad del servicio** | **≥ 99,99 %**, con penalizaciones contractuales |

> **Ejemplo de aplicación en el ayto.** El contrato municipal de 2026 refleja exactamente este lenguaje: **disponibilidad 24×7** de la infraestructura crítica y **tiempos de respuesta casi inmediatos ante incidencias técnicas** `[TELEFONICA-2026]`. Traducido a la práctica, eso significa guardia permanente, repuestos en almacén, procedimientos escritos y compromisos medibles. Y explica por qué el mantenimiento de una red de radio de emergencia se contrata como **servicio con niveles de servicio**, y no como una simple asistencia técnica.

> **Relación con otros temas.** Los conceptos de **plan de continuidad**, **análisis de impacto en el negocio**, **RTO y RPO** y **medios alternativos** se desarrollan en el **Tema 26**; su exigencia normativa, en el **Tema 39**. La **gestión de incidencias** y los acuerdos de nivel de servicio, en el **Tema 29**.

#### 5.4. Evolución hacia TEDS y coexistencia con redes de banda ancha crítica

**El problema.** TETRA resuelve la **voz crítica** de forma insuperable, pero su techo de datos —**28,8 kbit/s** en el mejor de los casos— es incompatible con lo que hoy se pide a un servicio de emergencia: **vídeo del lugar del incidente**, **planos y cartografía**, **imagen médica**, **acceso a bases de datos con fotografía**, **cámaras corporales**. La evolución tiene dos caminos, y **no son alternativos sino sucesivos**.

**Camino 1: TEDS, dentro de TETRA.** El **TETRA Enhanced Data Service** es la aportación de datos de **TETRA Release 2**, descrita en el **TR 102 580** `[TR102580]`. Su idea es sencilla: **mantener todo lo que TETRA hace bien y ampliar el canal**. Para ello introduce:

- **Cuatro anchos de canal**: **25, 50, 100 y 150 kHz** (frente a los 25 kHz únicos de la Release 1).
- **Modulaciones de orden superior** además de la π/4-DQPSK: **π/8-D8PSK**, **4-QAM**, **16-QAM** y **64-QAM**.
- **Adaptación al enlace**: el sistema elige la modulación **según la calidad de la señal**, de modo que se usan modulaciones densas cerca de la estación base y robustas en el borde de la célula (el **4-QAM** está pensado precisamente para el borde de cobertura).
- **Negociación de calidad de servicio** para las aplicaciones, con atributos de caudal, retardo, prioridad y fiabilidad.

El resultado es un salto de **uno o dos órdenes de magnitud** en la capacidad de datos —del orden de decenas a **algunos centenares de kbit/s** de caudal útil, según ancho de canal, modulación y condiciones de propagación—, manteniendo la misma red, los mismos grupos y la misma voz crítica.

> **Dato clave.** **TEDS = TETRA Release 2**, con **cuatro anchos de canal (25, 50, 100 y 150 kHz)** y **modulaciones π/8-D8PSK, 4-QAM, 16-QAM y 64-QAM** con **adaptación al enlace**. Es una **mejora dentro de TETRA**, no una tecnología distinta: sigue siendo banda estrecha en el sentido regulatorio, y **no compite con LTE**. Su adopción real ha sido limitada, entre otras razones porque exige **más espectro por canal** —y el espectro de 380-400 MHz está saturado en entornos urbanos, como reconoce la propia nota UN-28 del CNAF— y porque, cuando TEDS llegó al mercado, la banda ancha comercial ya ofrecía mucho más.

**Camino 2: la banda ancha crítica, fuera de TETRA.** La solución de fondo es llevar las funciones de misión crítica a redes de **banda ancha** LTE y 5G. El **3GPP** las normalizó:

| Servicio | Qué es | Release |
|----|----|----|
| **MCPTT** | *Mission Critical Push To Talk*: la **voz de grupo con PTT, prioridad y desalojo** sobre LTE | **Release 13** (culminada en **2016**); etapa 1 en la **TS 22.179** |
| **MCVideo** | Vídeo de misión crítica | Release 14 |
| **MCData** | Datos de misión crítica | Release 14 |

Y se apoya en tres habilitadores previos del propio 3GPP: **GCSE** (comunicaciones de grupo), **eMBMS** (difusión eficiente a muchos receptores sobre la misma portadora, imprescindible para que una llamada de grupo no consuma un canal por usuario) y **ProSe** (comunicación de proximidad, el equivalente conceptual del **modo directo**).

> **Dato clave.** **MCPTT se normalizó en la Release 13 del 3GPP, culminada en 2016**, con la **TS 22.179** como especificación de requisitos. **MCVideo y MCData** llegaron en la **Release 14**. El habilitador que hace viable la llamada de grupo sobre LTE es **eMBMS**; el que aspira a replicar el modo directo es **ProSe**.

**Por qué la transición es lenta.** Las razones son cuatro y conviene saberlas defender:

1.  **Cobertura y control.** Una red TETRA municipal está dimensionada por su titular para cubrir el 100 % del término municipal, incluidos interiores y subsuelo. Replicar esa cobertura con LTE **propio** es carísimo; usar LTE **comercial** significa renunciar al control de la disponibilidad y de la prioridad.
2.  **El modo directo.** **ProSe no ha alcanzado en la práctica la madurez del DMO de TETRA**, y el modo directo es innegociable para bomberos y equipos de rescate.
3.  **Consumo y autonomía.** Un terminal de banda ancha consume mucho más que uno de banda estrecha; la autonomía de jornada completa no es trivial.
4.  **Amortización y parque instalado.** Hay miles de terminales en servicio, personal formado y procedimientos escritos alrededor de ellos.

**El modelo que se impone: la coexistencia.** La respuesta práctica del sector no es sustituir, sino **operar dos redes complementarias**: **TETRA para la voz crítica y los datos cortos garantizados**, y **banda ancha (LTE/5G, propia o comercial con prioridad contratada) para todo lo que necesita caudal**, con **terminales híbridos** que integran ambas y con **interconexión entre el mundo MCPTT y el mundo TETRA** en los centros de mando. La migración se plantea **por fases y por servicios**, no de golpe.

> **Ejemplo de aplicación en el ayto.** El caso español ilustra bien este modelo. El **SIRDEE**, en servicio desde el año 2000 sobre TETRAPOL, inició en **julio de 2024** un proyecto piloto de **migración a banda ancha LTE** de la mano de Telefónica, **manteniendo la red de banda estrecha durante la transición** y usando la red pública como cobertura de respaldo donde no llega la red dedicada `[SIRDEE]`. En paralelo, el CNAF ya tiene **reservado el espectro** para ese futuro: **452-457,5 / 462-467,5 MHz** para PPDR de banda ancha y, en la banda de 700 MHz, **733-736 / 788-791 MHz** para el sistema de **ámbito nacional** y **698-703 / 753-758 MHz** para las redes de **ámbito autonómico y local** `[CNAF]`. Ese último bloque es, literalmente, **el espectro que la norma española reserva para una eventual red de banda ancha crítica de la Comunidad de Madrid o del Ayuntamiento**. Que exista la reserva no significa que exista la red: significa que **la decisión está pendiente y el recurso, apartado**.

> **Dato clave.** El reparto de espectro PPDR de banda ancha del CNAF: **733-736 / 788-791 MHz → ámbito NACIONAL**; **698-703 / 753-758 MHz → ámbito AUTONÓMICO y LOCAL**; y **452-457,5 / 462-467,5 MHz**, «preferentemente para el sistema de ámbito nacional» `[CNAF]`. Un supuesto que cruce «banda ancha PPDR» con «ámbito local» se resuelve con el segundo par.

> **Relación con otros temas.** La arquitectura de las redes móviles de banda ancha (LTE, 5G) es materia del **Tema 33**; el transporte IP sobre ellas, del **Tema 34**; los servicios de vídeo y colaboración que justifican el salto de capacidad, del **Tema 40**; y la seguridad del acceso remoto que exigirán las aplicaciones móviles de misión crítica, del **Tema 36**.

------------------------------------------------------------------------

### Los ocho datos que no se pueden fallar

Si de todo el tema hubiera que retener solo ocho cosas, serían éstas:

1.  **TETRA es un estándar abierto del ETSI**, serie **EN 300 392** (modo troncalizado, V+D) y **EN 300 396** (modo directo, DMO). La expansión vigente de las siglas es **TErrestrial TRunked RAdio**; *Trans European Trunked Radio* es la histórica.
2.  **Capa física**: portadora de **25 kHz**, **FDMA + TDMA con 4 intervalos**, modulación **π/4-DQPSK** a **18 kbaudios** → **36 kbit/s brutos** por portadora y **7,2 kbit/s netos** por intervalo. Códec **ACELP**, **4,567 kbit/s**.
3.  **Jerarquía temporal**: intervalo **14,167 ms** → trama **56,67 ms** (4 intervalos) → multitrama **1,02 s** (18 tramas, la **18.ª es la de control**) → hipertrama **61,2 s** (60 multitramas).
4.  **TMO frente a DMO**: el modo troncalizado va por la infraestructura; el **modo directo funciona sin ella**, y es lo que un teléfono móvil no puede hacer. El **DM-REP** amplía el alcance del modo directo; el **DM-GATE** lo conecta con la red. **No son lo mismo.**
5.  **Bandas en España**: **380-385 / 390-395 MHz** para redes de seguridad del Estado y emergencias (nota **UN-28**); **410-415,3 / 420-425,3 MHz** para **TETRA civil** (nota **UN-31**, que **cita TETRA por su nombre**), con **25 kHz** de canalización y **10 MHz** de separación dúplex. El CNAF vigente es la **Orden TDF/732/2026, de 10 de julio**.
6.  **Régimen jurídico**: el espectro es **dominio público estatal** (art. 85). Una red municipal es **uso privativo en autoprestación** y su título es una **afectación demanial** (art. **88.5.b**), por **cinco años renovables** (art. 94.1). Y las comunicaciones para **seguridad pública y protección civil** son **los únicos servicios de telecomunicación calificados como servicio público** (art. **4.1**).
7.  **Seguridad**: clases **SC1** (sin cifrar), **SC2** (clave estática **SCK**) y **SC3** (clave derivada **DCK** + **CCK**, con autenticación). **TEA set A = TEA1-TEA4**; **TEA set B = TEA5, TEA6 y TEA7** (octubre de 2022). **TEA1 tiene la clave reducida a ~32 bits efectivos** (**CVE-2022-24402**), y **soportarlo en la red compromete también a los demás algoritmos** (**CVE-2025-52943**). El **cifrado de interfaz aire se descifra en la estación base**; el **extremo a extremo, no**.
8.  **Y la trampa del tema**: **el SIRDEE, la red de emergencia del Estado, es TETRAPOL —FDMA, 12,5 kHz, GMSK— y no TETRA**. Las redes **autonómicas y municipales** españolas, incluidas la de la Comunidad de Madrid y la del Ayuntamiento, sí son **TETRA**.

## Diagramas

### Índice de diagramas

| ID | Título | Sección | Tipo |
|----|----|----|----|
| D1 | Cuatro generaciones de radio profesional | §1.1 | Línea temporal |
| D2 | Radio convencional frente a sistema troncalizado | §1.2 | Comparativa de reparto |
| D3 | La familia de normas TETRA del ETSI | §1.3 | Mapa de normas |
| D4 | Arquitectura de una red TETRA | §2.1 | Topología |
| D5 | La SwMI por dentro: qué hace cada bloque | §2.1.2 · §2.1.3 | Bloques funcionales |
| D6 | Terminales: factores de forma y clases de potencia | §2.2.1 | Comparativa |
| D7 | TMO, DMO y las dos figuras que los unen | §2.2.2 · §2.2.3 | Escenario operativo |
| D8 | Las seis interfaces normalizadas (I1 a I6) | §2.3 | Modelo de referencia |
| D9 | El espectro de TETRA en España según el CNAF | §3.1 | Mapa de bandas |
| D10 | FDMA + TDMA: cuatro conversaciones en 25 kHz | §3.2 | Estructura |
| D11 | Modulación π/4-DQPSK | §3.3 | Constelación + cifras |
| D12 | Jerarquía temporal: intervalo, trama, multitrama e hipertrama | §3.4 | Estructura anidada |
| D13 | Canales lógicos: control y tráfico | §3.4 | Clasificación |
| D14 | Tipos de llamada y escalones de prioridad | §4.1 | Comparativa + escalera |
| D15 | Servicios de datos: estados, SDS, circuito y paquetes | §4.2 | Tabla comparada |
| D16 | Cadena de seguridad: autenticación, claves y clases | §4.3.1 · §4.3.2 | Flujo + jerarquía |
| D17 | Interfaz aire frente a extremo a extremo, y qué rompió cada divulgación | §4.3.2 · §4.3.3 | Capas + cronología |
| D18 | De TETRA a la banda ancha crítica | §5.4 | Evolución + espectro |

------------------------------------------------------------------------

### D1 · Cuatro generaciones de radio profesional

**Sección**: §1.1 — Concepto y evolución de la radiocomunicación móvil privada (PMR) **Propósito**: Situar TETRA en la **tercera** generación y fijar qué problema resuelve cada etapa.

![Línea del tiempo con las cuatro generaciones de la radio móvil privada: la analógica convencional con un canal fijo por colectivo, el trunking analógico con MPT mil trescientos veintisiete, el trunking digital al que pertenecen TETRA, TETRAPOL, P25 y DMR, y la banda ancha crítica con MCPTT del 3GPP. Debajo se indica qué deja sin resolver cada etapa y se concluye que TETRA pertenece a la tercera generación](diagramas/diagrama-01.svg)

------------------------------------------------------------------------

### D2 · Radio convencional frente a sistema troncalizado

**Sección**: §1.2 — Sistemas *trunked* o troncalizados: concepto y ventajas **Propósito**: Mostrar con números por qué el mismo espectro rinde varias veces más cuando se troncaliza, y fijar la idea de que **un grupo solo consume canal mientras alguien habla**.

![Comparación entre radio convencional y sistema troncalizado. En la convencional cada colectivo tiene un canal fijo asignado, de modo que cuatro portadoras dan cuatro canales rígidos. En el sistema troncalizado TETRA las cuatro portadoras se dividen en cuatro intervalos cada una, dan dieciséis canales físicos, uno se dedica al canal de control y quedan quince canales de tráfico repartidos dinámicamente entre todos los grupos](diagramas/diagrama-02.svg)

------------------------------------------------------------------------

### D3 · La familia de normas TETRA del ETSI

**Sección**: §1.3 — Estandarización de TETRA por el ETSI **Propósito**: Ordenar las series de normas para poder responder «qué norma regula qué».

![Mapa de la familia de normas TETRA del ETSI. La serie EN 300 392 regula el modo troncalizado voz más datos, con la parte 1 de diseño general, la parte 2 del interfaz aire, la parte 3 de la interfaz entre sistemas, la parte 4 de pasarelas, la parte 5 del interfaz de equipo periférico, la parte 7 de seguridad y las partes 9 a 12 de servicios suplementarios. La serie EN 300 396 regula el modo directo. Además, EN 300 394 de pruebas de conformidad, EN 300 395 del códec de voz, EN 300 812 del módulo de identidad, TR 102 580 de TEDS y TS 104 053 de los algoritmos de cifrado](diagramas/diagrama-03.svg)

------------------------------------------------------------------------

### D4 · Arquitectura de una red TETRA

**Sección**: §2.1 — Infraestructura de conmutación y gestión (SwMI) **Propósito**: Fijar de un vistazo qué es la SwMI, qué queda fuera de ella y por dónde entra cada elemento.

![Topología de una red TETRA. En el centro, la infraestructura de conmutación y gestión o SwMI, que contiene el nodo de conmutación, las bases de datos de abonados y grupos, el centro de autenticación y las estaciones base. A la izquierda, los terminales portátiles, móviles y fijos, que se conectan por el interfaz aire I1. A la derecha, las consolas de despacho, el grabador y el sistema de gestión de red, conectados por las interfaces de línea I2 y de gestión I5. Abajo, la pasarela hacia la red telefónica y la interfaz entre sistemas I3 hacia otra red TETRA](diagramas/diagrama-04.svg)

------------------------------------------------------------------------

### D5 · La SwMI por dentro: qué hace cada bloque

**Sección**: §2.1.2 — Nodos de conmutación y control de red · §2.1.3 — Centros de gestión **Propósito**: Separar las tres capas de la infraestructura fija —radio, conmutación y gestión— porque la tercera es la que se olvida.

![Las tres capas de la infraestructura fija de una red TETRA. La capa de radio, con las estaciones base, el canal de control principal, el traspaso entre células y el repliegue local. La capa de conmutación y control, con el encaminamiento de llamadas de grupo, la gestión de movilidad, las bases de datos de abonados, el centro de autenticación y la gestión de prioridades. Y la capa de gestión y despacho, con el sistema de gestión de red, la gestión de abonados y grupos, las consolas de despacho, la grabación y la gestión de claves criptográficas](diagramas/diagrama-05.svg)

------------------------------------------------------------------------

### D6 · Terminales: factores de forma y clases de potencia

**Sección**: §2.2.1 — Equipos portátiles, móviles y fijos **Propósito**: Fijar las clases de potencia normalizadas y las identidades del terminal, que son dos bloques de datos memorizables.

![Los tres factores de forma del terminal TETRA con sus potencias típicas: portátil de uno o tres vatios para el agente a pie, móvil embarcado de tres o diez vatios para patrullas y ambulancias, y fijo de diez vatios o más para dependencias. Debajo, las clases de potencia normalizadas: clase uno treinta vatios, clase dos diez vatios, clase tres tres vatios y clase cuatro un vatio. Y a la derecha, el esquema de identidades: ITSI igual a MNI más ISSI, donde MNI es MCC más MNC, la identidad de grupo GSSI y la identidad corta cifrada ESI](diagramas/diagrama-06.svg)

------------------------------------------------------------------------

### D7 · TMO, DMO y las dos figuras que los unen

**Sección**: §2.2.2 — Modos de operación · §2.2.3 — Repetidor y pasarela **Propósito**: Resolver de una vez la confusión entre **DM-REP** y **DM-GATE** sobre un escenario operativo real.

![Escenario operativo que compara el modo troncalizado y el modo directo. Arriba, el modo troncalizado: los terminales en superficie hablan con la estación base y con el centro de mando. En el centro, el sótano sin cobertura, donde las dotaciones trabajan en modo directo y el centro de mando no las oye. Abajo, las dos soluciones: el repetidor DM-REP amplía el alcance dentro del modo directo pero sigue sin llegar al centro de mando, y la pasarela DM-GATE reinyecta la comunicación en la red y devuelve la visibilidad al despacho](diagramas/diagrama-07.svg)

------------------------------------------------------------------------

### D8 · Las seis interfaces normalizadas (I1 a I6)

**Sección**: §2.3 — Interfaces estándar de TETRA **Propósito**: Memorizar las seis interfaces y su norma, distinguiendo las **dos interfaces aire** (I1 y I6), que es donde se falla.

![Las seis interfaces normalizadas de TETRA. I1 es el interfaz aire en modo troncalizado, entre terminal y estación base, norma EN 300 392-2. I2 es la interfaz de línea entre la infraestructura y los equipos conectados por cable. I3 es la interfaz entre sistemas o ISI, hacia otra red TETRA, norma EN 300 392-3. I4 es la interfaz de equipo periférico o PEI, entre terminal y equipo de datos, norma EN 300 392-5. I5 es la interfaz de gestión de red. I6 es el interfaz aire en modo directo, entre terminales, norma EN 300 396](diagramas/diagrama-08.svg)

------------------------------------------------------------------------

### D9 · El espectro de TETRA en España según el CNAF

**Sección**: §3.1 — Espectro radioeléctrico y asignación de frecuencias **Propósito**: Reunir en un solo cuadro las bandas y las notas UN que el CNAF vigente dedica a estos sistemas. Es el diagrama con más datos literales del tema.

![Mapa de las bandas de frecuencia que el Cuadro Nacional de Atribución de Frecuencias español dedica a estos sistemas. La banda 380-385 y 390-395 megahercios, según la nota UN-28, se reserva a redes de seguridad de las Fuerzas y Cuerpos de Seguridad del Estado y a redes de servicios de emergencia. Las subbandas 410-415,3 y 420-425,3 megahercios, según la nota UN-31, se destinan a sistemas digitales de acceso aleatorio de canales, TETRA y otros, con canalización de 25 kilohercios y separación dúplex de 10 megahercios. Los bloques 452-457,5 y 462-467,5 megahercios se reservan a banda ancha para protección pública y socorro. Y en la banda de 700 megahercios, 733-736 y 788-791 para el ámbito nacional y 698-703 y 753-758 para el ámbito autonómico y local](diagramas/diagrama-09.svg)

------------------------------------------------------------------------

### D10 · FDMA + TDMA: cuatro conversaciones en 25 kHz

**Sección**: §3.2 — Técnica de acceso múltiple por división de tiempo **Propósito**: Visualizar la doble división —en frecuencia y en tiempo— y encadenar las cifras de la capa física.

![Esquema del acceso múltiple de TETRA. Primero se divide el espectro en portadoras de 25 kilohercios, lo que es FDMA. Después cada portadora se divide en cuatro intervalos de tiempo, lo que es TDMA. El resultado son cuatro canales físicos por portadora, uno de los cuales suele ser el canal de control. Debajo, la cadena de cifras: 18.000 símbolos por segundo, dos bits por símbolo, 36 kilobits por segundo brutos por portadora y 7,2 kilobits por segundo netos por intervalo, o 28,8 agregando los cuatro](diagramas/diagrama-10.svg)

------------------------------------------------------------------------

### D11 · Modulación π/4-DQPSK

**Sección**: §3.3 — Modulación digital π/4-DQPSK **Propósito**: Explicar de dónde salen los 2 bits por símbolo y por qué el desplazamiento de π/4 evita el paso por el origen, que es la parte que suele quedar sin entender.

![Explicación de la modulación pi cuartos DQPSK de TETRA. A la izquierda, una constelación con cuatro estados de fase y el detalle de que las transiciones nunca pasan por el origen, lo que evita que la envolvente caiga a cero. A la derecha, el desglose del nombre: PSK codifica en la fase, la cuarta parte quiere decir cuatro estados y por tanto dos bits por símbolo, la D indica codificación diferencial del cambio de fase y el desplazamiento de pi cuartos evita el paso por el origen. Abajo, la comparación con la modulación GMSK que usan TETRAPOL y GSM](diagramas/diagrama-11.svg)

------------------------------------------------------------------------

### D12 · Jerarquía temporal: intervalo, trama, multitrama e hipertrama

**Sección**: §3.4 — Estructura de trama radio y canales lógicos **Propósito**: Es el bloque de cifras central del tema. El diagrama las anida de menor a mayor y señala la trama 18.

![Jerarquía temporal del interfaz aire de TETRA. El intervalo de tiempo dura 14,167 milisegundos. Cuatro intervalos forman una trama de 56,67 milisegundos. Dieciocho tramas forman una multitrama de 1,02 segundos, y la trama número 18 se reserva para señalización. Sesenta multitramas forman una hipertrama de 61,2 segundos, cuyo número interviene en la generación del flujo de clave del cifrado del interfaz aire](diagramas/diagrama-12.svg)

------------------------------------------------------------------------

### D13 · Canales lógicos: control y tráfico

**Sección**: §3.4 — Estructura de trama radio y canales lógicos **Propósito**: Separar canal **físico** de canal **lógico** y ordenar las dos familias.

![Clasificación de los canales lógicos de TETRA. La familia de canales de control incluye el BCCH de difusión con sus variantes BNCH de red y BSCH de sincronización, el LCH de linealización, el SCH de señalización con sus variantes completa y de medio intervalo, el ACCH asociado a una llamada en curso con las variantes rápida y lenta, y el STCH que roba capacidad al tráfico. La familia de canales de tráfico incluye el TCH de voz a 7,2 kilobits por segundo y los de datos a 7,2 sin protección, 4,8 con protección baja y 2,4 con protección alta](diagramas/diagrama-13.svg)

------------------------------------------------------------------------

### D14 · Tipos de llamada y escalones de prioridad

**Sección**: §4.1 — Servicios de voz y comunicaciones de grupo **Propósito**: Distinguir los cuatro tipos de llamada —y sobre todo grupo frente a difusión— y fijar los tres escalones de prioridad.

![Los cuatro tipos de llamada de TETRA y los tres escalones de prioridad. Los tipos son: llamada de grupo, de uno a muchos y bidireccional; llamada individual, de uno a uno, semidúplex o dúplex completo; llamada de difusión, de uno a muchos pero unidireccional, en la que los receptores no pueden contestar; y llamada telefónica hacia la red pública. Los escalones de prioridad son: prioridad de acceso, que ordena la cola; prioridad con desalojo, que corta una llamada en curso de menor prioridad; y llamada de emergencia, con la máxima prioridad, alarma en el despacho, identidad y posición del usuario](diagramas/diagrama-14.svg)

------------------------------------------------------------------------

### D15 · Servicios de datos: estados, SDS, circuito y paquetes

**Sección**: §4.2 — Servicios de datos **Propósito**: Fijar los tamaños de los SDS y la diferencia entre datos por circuito y por paquetes, junto con el techo real de capacidad.

![Los servicios de datos de TETRA. Arriba, la mensajería corta: el mensaje de estado con 16 bits precodificados, el SDS tipo 1 con 16 bits, el tipo 2 con 32, el tipo 3 con 64 y el tipo 4 con hasta 2047 bits definidos por el usuario, sobre el que se define la capa de transporte SDS-TL con acuse de recibo y encadenamiento. Abajo, la comparación entre datos por circuito, que reserva un canal con tasas de 7,2, 4,8 o 2,4 kilobits por segundo por intervalo, y datos por paquetes, que comparte recursos y transporta IP mediante SNDCP](diagramas/diagrama-15.svg)

------------------------------------------------------------------------

### D16 · Cadena de seguridad: autenticación, claves y clases

**Sección**: §4.3.1 — Autenticación · §4.3.2 — Cifrado en la interfaz aire **Propósito**: Encadenar autenticación → clave derivada → clase de seguridad, que es la relación que explica por qué una red sin autenticación es estructuralmente más débil.

![Cadena de seguridad de TETRA. Primero, la autenticación por desafío y respuesta con la clave secreta K, que nunca viaja por el aire y que puede ejecutarse en sentido inverso para que el terminal verifique a la red y evitar así una estación base falsa. De la autenticación se deriva la clave DCK. Después, la jerarquía de claves: K de autenticación, DCK derivada individual, CCK común de área, SCK estática precargada, y GCK de grupo que se combina para dar la MGCK. Finalmente, las clases de seguridad: SC1 sin cifrar, SC2 con clave estática y SC3 con clave derivada y común, más la variante SC3G con clave de grupo](diagramas/diagrama-16.svg)

------------------------------------------------------------------------

### D17 · Interfaz aire frente a extremo a extremo, y qué rompió cada divulgación

**Sección**: §4.3.2 — Cifrado en la interfaz aire · §4.3.3 — Cifrado extremo a extremo **Propósito**: Fijar de una vez qué protege cada capa de cifrado y situar en ellas los hallazgos de 2023 y de 2025.

![Comparación entre el cifrado de interfaz aire y el cifrado extremo a extremo. El cifrado de interfaz aire protege el tramo entre terminal y estación base y se descifra en la estación base, de modo que no protege frente al operador de la red. El cifrado extremo a extremo protege de terminal a terminal y la infraestructura no puede leerlo. Debajo, la cronología de las divulgaciones: en octubre de 2022 el ETSI libera el conjunto de algoritmos TEA set B con TEA5, TEA6 y TEA7; en agosto de 2023 se publica TETRA:BURST con cinco vulnerabilidades incluida la reducción de clave de TEA1; en febrero de 2025 el ETSI publica la especificación del TEA set A; y en agosto de 2025 se presenta 2TETRA:2BURST, que alcanza al cifrado extremo a extremo](diagramas/diagrama-17.svg)

------------------------------------------------------------------------

### D18 · De TETRA a la banda ancha crítica

**Sección**: §5.4 — Evolución hacia TEDS y coexistencia con redes de banda ancha crítica **Propósito**: Separar los dos caminos de evolución —TEDS dentro de TETRA, MCPTT fuera— y mostrar que la respuesta real es la coexistencia.

![Los dos caminos de evolución de TETRA. El primero es TEDS, dentro de TETRA, que es la aportación de datos de la Release 2 con anchos de canal de 25, 50, 100 y 150 kilohercios y modulaciones pi octavos D8PSK, 4-QAM, 16-QAM y 64-QAM con adaptación al enlace. El segundo es la banda ancha crítica del 3GPP, con MCPTT normalizado en la Release 13 de 2016 y MCVideo y MCData en la Release 14, apoyados en los habilitadores GCSE, eMBMS y ProSe. Abajo, las cuatro razones por las que la transición es lenta y el modelo de coexistencia que se impone](diagramas/diagrama-18.svg)

## Casos prácticos

Los tres casos giran sobre el supuesto de referencia del tema (ver la pestaña Contenido, «Convenciones»): la **red DIMETRA-TETRA municipal**, gobernada desde el **CISEM**. El **Caso 1** trabaja la **operación sobre el terreno** —modos, cobertura, grupos y prioridades—; el **Caso 2**, la **seguridad** de la red frente a las vulnerabilidades divulgadas y el respaldo del ENS; y el **Caso 3**, el **régimen jurídico del espectro** y la decisión de evolución hacia la banda ancha crítica.

------------------------------------------------------------------------

### Caso 1 — Incidente en un aparcamiento subterráneo del distrito de Salamanca

#### Enunciado

A las 03:40 se recibe en el **CISEM** un aviso de incendio en el **nivel −3 de un aparcamiento subterráneo**. Se movilizan **dos dotaciones de Bomberos**, una **UVI móvil del SAMUR-Protección Civil** y una unidad de **Policía Municipal** que corta el tráfico en superficie. Los primeros datos técnicos son:

- La cobertura de la red municipal en el nivel −3 es **nula**; en el nivel −1 es marginal.
- El vehículo de mando de Bomberos queda estacionado en la rampa de acceso, con **cobertura buena**.
- El operador del CISEM ha creado el grupo `INC-0340-SALAMANCA` y lo ha cargado en los terminales de las unidades intervinientes.
- Los agentes de Policía Municipal en superficie llevan **portátiles de 1 W**; los equipos embarcados son de **10 W**.
- Durante la intervención, la red del centro de la ciudad registra una ocupación alta por otro operativo simultáneo.

Se pide un informe técnico-operativo.

#### Cuestiones

**Cuestión 1 — Modos de operación y cobertura (3 puntos).** Indique en qué modo debe trabajar cada colectivo y por qué, y qué equipo hay que desplegar para que el CISEM no pierda a las dotaciones que descienden al nivel −3. Distinga con precisión entre las dos figuras que la norma prevé para ampliar el modo directo.

**Cuestión 2 — Grupos de conversación (2 puntos).** Explique qué función del estándar ha usado el operador del CISEM para crear y cargar `INC-0340-SALAMANCA`, por qué esa función es imposible en radio convencional y qué ocurre con un terminal que se afilia al grupo cuando la conversación ya ha empezado.

**Cuestión 3 — Prioridades y saturación (3 puntos).** Con la red del centro saturada por otro operativo, explique los tres escalones de prioridad que garantizan que este incidente entre igualmente, y qué sucede exactamente si un bombero pulsa el botón de emergencia.

**Cuestión 4 — Dimensionado (2 puntos).** Si la estación base que cubre la zona tiene **3 portadoras** y dedica un intervalo al canal de control, ¿cuántas conversaciones simultáneas admite en esa célula? Razone por qué el número de **grupos** que pueden convivir no está limitado por esa cifra.

#### Solución orientativa

- **C1**: (§2.2.2, §2.2.3) El **mando del incidente, la Policía Municipal en superficie y el CISEM** trabajan en **TMO**, que es donde hay despacho, grabación y visión de posiciones. Las **dotaciones que descienden al nivel −3** deben pasar a **DMO**, porque no hay cobertura de red; entre ellas se oirán, pero el CISEM no. Para recuperar el enlace hay que configurar el **vehículo de mando estacionado en la rampa como DM-GATE**, es decir, **pasarela**: recibe en modo directo y **reinyecta la comunicación en la red troncalizada**, devolviendo al CISEM la audición, la posibilidad de hablar con el interior y la grabación. Si el alcance del modo directo no bastara para cubrir todo el nivel −3, se añadiría un **DM-REP** —o se emplearía un equipo **DM-REP/GATE**— para ampliar el alcance **dentro** del modo directo antes de reinyectar. **La distinción es la clave de la cuestión**: un **DM-REP** solo haría que las dotaciones se oyeran más lejos entre sí, **sin que el CISEM se enterara de nada**. Debe mencionarse además que el **portátil de 1 W** del agente tiene bastante menos alcance que el **equipo embarcado de 10 W**, lo que refuerza el papel del vehículo como nodo.
- **C2**: (§4.1.1) La función es la **DGNA** (*Dynamic Group Number Assignment*): permite **crear un grupo nuevo y cargarlo por el aire** en los terminales seleccionados desde la consola, sin tocar los equipos. Es imposible en radio convencional porque allí **el grupo es una frecuencia física** y cambiar la organización obligaría a **reprogramar equipo por equipo**. En TETRA el grupo es una **entidad lógica** identificada por su **GSSI**. Un terminal que se afilia con la llamada ya iniciada se incorpora a ella gracias a la **entrada tardía** (*late entry*), posible porque la **trama 18 de cada multitrama** está reservada a señalización y permite avisar al terminal sin interrumpir el tráfico.
- **C3**: (§4.1.2) Los tres escalones son: **(1) prioridad de acceso**, que ordena la **cola** cuando varias peticiones compiten por el mismo canal, sin cortar a nadie; **(2) prioridad con desalojo** (*pre-emptive priority*), que **corta** una comunicación en curso de prioridad inferior cuando **no hay ningún canal libre**; y **(3) llamada de emergencia**, el nivel máximo. Al pulsar el botón de emergencia se produce: establecimiento **inmediato** en el grupo de emergencia con máxima prioridad y desalojo; **alarma visual y sonora** en la consola del CISEM con la **identidad** del usuario y, si el terminal la envía, su **posición**; y apertura de un **canal de voz abierto** que, en las configuraciones habituales, no exige que el agente pulse el PTT, de modo que si está incapacitado el centro **oye igualmente** lo que ocurre. Conviene añadir que este comportamiento **no se puede replicar con telefonía móvil comercial**, porque en una red pública el Ayuntamiento no decide a quién se desaloja.
- **C4**: (§1.2, §3.4) **3 portadoras × 4 intervalos = 12 canales físicos**; menos **1** dedicado al canal de control principal → **11 conversaciones simultáneas** en esa célula. El número de **grupos** no está limitado por esa cifra porque un grupo **solo consume canal mientras alguien transmite**, y solo en las **células donde hay afiliados**: pueden convivir decenas de grupos afiliados mientras no hablen más de once a la vez. Se valorará que se mencione que el dimensionado de una red de emergencia se hace por **transmisiones simultáneas previstas en la hora punta de la célula más cargada**, con margen para el escenario de gran emergencia, y no por número de usuarios.

#### Criterios de evaluación

| Cuestión | Elemento | Puntos |
|----|----|----|
| 1 | Asignar TMO a superficie y DMO al subsuelo, con justificación | 1,0 |
| 1 | Identificar el **DM-GATE** como la solución, y explicar por qué el DM-REP **no** resuelve el problema | 1,5 |
| 1 | Mencionar el DM-REP/GATE o la diferencia de alcance entre 1 W y 10 W | 0,5 |
| 2 | Identificar la **DGNA** y explicar el contraste con la radio convencional | 1,0 |
| 2 | Explicar la **entrada tardía** y el papel de la trama de control | 1,0 |
| 3 | Enumerar y distinguir los **tres escalones** de prioridad | 1,5 |
| 3 | Describir el efecto completo del **botón de emergencia** | 1,0 |
| 3 | Señalar que la prioridad no es replicable en una red comercial | 0,5 |
| 4 | Cálculo correcto: 12 canales físicos − 1 de control = **11** | 1,0 |
| 4 | Razonar que el grupo solo consume canal al transmitir, y solo donde hay afiliados | 1,0 |
|  | **Total** | **10** |

------------------------------------------------------------------------

#### Preguntas tipo test sobre este caso

##### 1. En el supuesto planteado, la cobertura de la red municipal en el nivel −3 del aparcamiento es nula. ¿En qué modo deben trabajar las dotaciones que descienden a ese nivel?

- a) En modo troncalizado (TMO), porque la cobertura marginal del nivel −1 basta para llegar al −3.
- b) En modo directo (DMO), porque no hay cobertura de red; se oirán entre ellas, pero el CISEM no.
- c) En modo troncalizado con prioridad con desalojo, que amplía la cobertura de la célula al subsuelo.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.2.2

El modo directo funciona sin infraestructura: los terminales se comunican entre sí. La contrapartida es que la comunicación no llega a la red y, por tanto, el CISEM no la oye.

##### 2. ¿En qué modo deben trabajar el mando del incidente, la Policía Municipal en superficie y el CISEM?

- a) En modo troncalizado (TMO), que es donde hay despacho, grabación y visión de posiciones.
- b) En modo directo (DMO), para no consumir canales en una red del centro que está saturada.
- c) En modo directo a través de un DM-REP, que permite al CISEM grabar las comunicaciones.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.2.2

Quien tiene cobertura debe trabajar en TMO: la red aporta el despacho desde el centro, la grabación y la localización. El DM-REP no conecta con la red.

##### 3. ¿Qué función debe configurarse en el vehículo de mando estacionado en la rampa para que el CISEM no pierda a las dotaciones del nivel −3?

- a) DM-REP (repetidor), que retransmite el modo directo con más potencia hasta la consola del CISEM.
- b) Repliegue local de la estación base, que enlaza el modo directo con el núcleo de la red troncalizada.
- c) DM-GATE (pasarela), que recibe en modo directo y reinyecta la comunicación en la red troncalizada.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.2.3

La pasarela DM-GATE une el modo directo con la red troncalizada y devuelve al CISEM la audición, la posibilidad de hablar con el interior y la grabación.

##### 4. Si en la rampa se desplegara únicamente un DM-REP, ¿qué ocurriría?

- a) Las dotaciones se oirían más lejos entre sí, pero el CISEM seguiría sin enterarse de nada.
- b) El CISEM oiría a las dotaciones del nivel −3, pero no podría hablar con ellas ni grabarlas.
- c) Las dotaciones volverían automáticamente a TMO al quedar dentro del alcance del repetidor.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.2.3

El repetidor de modo directo amplía el alcance dentro del modo directo sin tocar la red: lo que entra en DMO sale en DMO. Solo la pasarela conecta con la red.

##### 5. ¿Por qué conviene que la pasarela sea el equipo embarcado del vehículo y no el portátil de un agente?

- a) Porque los portátiles de 1 W no admiten el modo directo, exclusivo de los embarcados.
- b) Porque el equipo embarcado de 10 W tiene bastante más alcance que el portátil de 1 W.
- c) Porque solo los equipos de 10 W pueden afiliarse a grupos creados desde la consola.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.2.3

Los equipos embarcados de gama profesional pueden actuar como DM-REP o DM-GATE, y su mayor potencia les da más alcance, lo que convierte al vehículo en el nodo de la intervención.

##### 6. ¿Qué función ha usado el operador del CISEM para crear el grupo INC-0340-SALAMANCA y cargarlo en los terminales de las unidades?

- a) La DGNA, que asigna al grupo una frecuencia física exclusiva programada en cada terminal.
- b) La ISI, que reprograma el grupo en cada terminal a través de su interfaz de datos PEI.
- c) La DGNA, que crea el grupo como entidad lógica y lo carga por el aire en los terminales.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §4.1.1

La asignación dinámica de grupos crea el grupo y lo carga desde la consola sin tocar los equipos. En TETRA el grupo es una entidad lógica (GSSI), no una frecuencia; en radio convencional habría que reprogramar equipo por equipo.

##### 7. Un terminal se afilia a INC-0340-SALAMANCA cuando la conversación del grupo ya ha empezado. ¿Qué ocurre?

- a) Debe esperar a que termine la conversación, porque la red solo avisa a los terminales al iniciarse cada llamada.
- b) Se incorpora a ella por la entrada tardía, posible porque la trama 18 de cada multitrama se reserva a señalización.
- c) Se incorpora gracias a la hipertrama, que repite la llamada de grupo completa cada 61,2 segundos de duración.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 2 · §4.1.1

La trama de control (la 18.ª de cada multitrama) permite a la red avisar a un terminal sin interrumpir el tráfico; por eso quien se afilia con la llamada iniciada se incorpora a ella.

##### 8. Con la red del centro saturada por otro operativo y sin ningún canal libre, ¿qué escalón de prioridad permite que una llamada del incidente corte otra de prioridad inferior?

- a) La prioridad de acceso, que ordena la cola de espera.
- b) La entrada tardía, que libera el canal más antiguo.
- c) La prioridad con desalojo (pre-emptive priority).

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §4.1.2

La prioridad de acceso solo ordena la cola sin cortar a nadie; la prioridad con desalojo corta una comunicación en curso de prioridad inferior cuando no hay canal libre. Por encima está la llamada de emergencia.

##### 9. Un bombero del nivel −1 pulsa el botón de emergencia de su terminal. ¿Qué se produce?

- a) Establecimiento inmediato con máxima prioridad y desalojo, alarma con su identidad en el CISEM y canal de voz abierto sin pulsar el PTT.
- b) Envío de un mensaje de estado al CISEM, que lo encola por prioridad de acceso sin cortar ninguna de las llamadas en curso.
- c) Paso automático del terminal a modo directo, para que las dotaciones cercanas le oigan sin depender de la red.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §4.1.2

La llamada de emergencia es el nivel máximo: entra con desalojo en el grupo de emergencia, alerta a la consola con la identidad y, si se envía, la posición, y abre un canal de voz para que el centro oiga lo que ocurre aunque el agente esté incapacitado.

##### 10. La estación base que cubre la zona tiene 3 portadoras y dedica un intervalo al canal de control. ¿Cuántas conversaciones simultáneas admite esa célula?

- a) 12: el intervalo de control también cursa voz cuando la célula se satura.
- b) 11: 3 portadoras × 4 intervalos son 12 canales físicos, menos 1 de control.
- c) 9: cada portadora reserva un intervalo a señalización, y quedan 3 × 3.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §1.2 · §3.4

Cada portadora de 25 kHz se divide en 4 intervalos TDMA: 12 canales físicos. Solo uno se dedica al canal de control principal, de modo que quedan 11 para tráfico.

### Caso 2 — Informe de seguridad sobre una oferta de renovación de terminales

#### Enunciado

El Ayuntamiento licita la renovación de **1.200 terminales** de la red municipal. Una de las ofertas presenta las siguientes características, y se solicita informe técnico de la unidad TIC:

- Los terminales soportan **TEA1 y TEA2**, y se propone **configurar TEA1** «por ser el de exportación libre y estar disponible en todo el parque actual, dejando TEA2 activo por compatibilidad».
- La red operaría en **clase de seguridad SC2**, «para simplificar, evitando la carga del centro de autenticación».
- **No** se ofrece cifrado extremo a extremo. El fabricante alega que «el cifrado de interfaz aire ya protege la comunicación de punta a punta».
- **No** se incluye la capacidad de **distribución de claves por el aire**: la renovación de claves se haría recogiendo los terminales en el almacén una vez al año.
- El sistema se ha categorizado **MEDIA** conforme al ENS.
- Se propone conectar las **consolas de despacho** al mismo segmento de red que la ofimática municipal, «para simplificar el cableado».

#### Cuestiones

**Cuestión 1 — Algoritmos de cifrado (3 puntos).** Valore la propuesta de configurar TEA1 y de mantener TEA2 «por compatibilidad». Cite las vulnerabilidades divulgadas que resultan aplicables y explique qué exigencia concreta debe incorporarse al pliego.

**Cuestión 2 — Clase de seguridad y gestión de claves (3 puntos).** Analice la elección de SC2 y la ausencia de distribución de claves por el aire. Indique qué clase debe exigirse y por qué, y qué relación existe entre autenticación y cifrado en TETRA.

**Cuestión 3 — Cifrado extremo a extremo (2 puntos).** Rebata la afirmación del fabricante. Explique qué protege cada capa y qué debe exigirse si finalmente se decide implantar cifrado extremo a extremo.

**Cuestión 4 — Respaldo normativo (2 puntos).** Cite las medidas del **ENS** que amparan cada una de las correcciones anteriores, incluida la relativa al segmento de red de las consolas.

#### Solución orientativa

- **C1**: (§4.3.2) La propuesta es **inaceptable en sus dos extremos**. Primero, **TEA1 tiene una reducción deliberada de la longitud efectiva de clave a unos 32 bits** —de los 80 nominales—, lo que permite **romperla por fuerza bruta en minutos con hardware doméstico** (**CVE-2022-24402**, divulgada en agosto de 2023 dentro de **TETRA:BURST**); la TCCA ha confirmado que la reducción fue **intencionada**, para cumplir el **Acuerdo de Wassenaar** de control de exportación. Segundo, y más grave para esta oferta, la divulgación de **agosto de 2025** (**2TETRA:2BURST**, Black Hat USA, 7 de agosto) demostró con la **CVE-2025-52943** que, en redes **multicifrado**, **soportar TEA1 junto a otros algoritmos permite recuperar también la clave de los demás**: mantener TEA2 «por compatibilidad» con TEA1 activo **no salva nada**. La exigencia concreta del pliego debe ser **prohibir expresamente TEA1** —no desaconsejarlo— y exigir **capacidad de migración a TEA set B (TEA5, TEA6 y TEA7) y al conjunto de autenticación TAA2** en los terminales que se adquieran. Se valorará mencionar que **TEA5 y TEA6 usan claves de 192 bits** y que **TEA7, el civil, conserva una reducción efectiva a 56 bits** por el mismo régimen de exportación.
- **C2**: (§4.3.1, §4.3.2) **SC2 cifra con clave estática (SCK) precargada y no exige autenticación**: la misma clave para todos y durante mucho tiempo. Debe exigirse **SC3**, que emplea **clave derivada (DCK) más clave común (CCK)** y **requiere autenticación**, preferiblemente **mutua**. La relación entre ambas cosas es el núcleo de la respuesta: **la DCK se deriva del propio proceso de autenticación**, de modo que **una red que no autentica no puede usar claves derivadas** y queda condenada a la clave estática. Además, la **autenticación mutua** es la defensa frente a una **estación base falsa**. La ausencia de **OTAR** es igualmente inaceptable: renovar claves recogiendo 1.200 terminales una vez al año hace **inviable** reaccionar ante un compromiso de clave o ante la baja de un usuario, y contradice cualquier plan de gestión del ciclo de vida del material criptográfico. Debe exigirse **OTAR** y un **procedimiento documentado de inhabilitación remota** (*stun* y *kill*) para terminales perdidos o robados.
- **C3**: (§4.3.2, §4.3.3) La afirmación es **falsa**. El **cifrado de interfaz aire (AIE)** protege el tramo **terminal ↔ estación base** y **se descifra en la estación base**; a partir de ahí la comunicación circula por la infraestructura **en claro**, salvo cifrado adicional. Por tanto **no protege frente al operador de la red, frente al personal técnico con acceso a los equipos o a las grabaciones, ni frente a un compromiso de la infraestructura o de los enlaces de transporte**. El **cifrado extremo a extremo (E2EE)** cifra **en el terminal emisor y descifra en el receptor**, atravesando la red sin que ésta pueda leerlo; son **complementarios**, no alternativos. Si se implanta, **no basta con exigir «cifrado extremo a extremo»**: la **CVE-2025-52941** identificó una **variante debilitada de AES-128 con entropía efectiva reducida a 56 bits**, la **CVE-2025-52940** describió **repetición e inyección de voz** y la **CVE-2025-52942**, la **falta de protección antirrepetición en los SDS**. Hay que exigir, por tanto: **algoritmo y longitud de clave nombrados**, **protección frente a repetición**, **autenticación del contenido** y **derecho de auditoría de la implementación**. Debe advertirse también del coste honesto del E2EE: inutiliza las pasarelas telefónicas, la grabación centralizada en claro y la interconexión, salvo que se prevean puntos de descifrado autorizados.
- **C4**: (§5.2) Respaldo normativo en el **RD 311/2022 (ENS)**: **`mp.com.2`** (protección de la **confidencialidad**) y **`mp.com.3`** (protección de la **integridad y de la autenticidad**) amparan la exigencia de cifrado y autenticación del interfaz aire; **`mp.si.2`** (**criptografía**) y **`op.exp.10`** (**protección de claves criptográficas**) amparan la exigencia de OTAR y de una gestión de claves con ciclo de vida; y **`mp.com.4`** (**separación de flujos de información en la red**) **prohíbe** conectar las consolas al segmento ofimático: su requisito **`mp.com.4.2`** establece que «**si se emplean comunicaciones inalámbricas, será en un segmento separado**», y al estar el sistema categorizado **MEDIA** la medida exige además **\[R1 o R2 o R3\]**, es decir, segmentación lógica con **VLAN**, con **VPN** o con **medios físicos separados** —obsérvese que en categoría **BÁSICA** esta medida **no aplicaría**—. Se valorará mencionar `mp.com.1` (perímetro seguro) y `mp.eq.4` (otros dispositivos conectados a la red).

#### Criterios de evaluación

| Cuestión | Elemento | Puntos |
|----|----|----|
| 1 | Identificar la reducción de clave de **TEA1** (CVE-2022-24402) y su origen en Wassenaar | 1,0 |
| 1 | Señalar que **soportar TEA1 compromete a los demás algoritmos** (CVE-2025-52943) | 1,0 |
| 1 | Exigencia de pliego: prohibir TEA1 y exigir migración a **TEA set B / TAA2** | 1,0 |
| 2 | Rechazar SC2 y exigir **SC3** con autenticación mutua | 1,0 |
| 2 | Explicar que la **DCK se deriva de la autenticación** | 1,0 |
| 2 | Exigir **OTAR** e inhabilitación remota, con justificación operativa | 1,0 |
| 3 | Distinguir con precisión **AIE** (se descifra en la BS) de **E2EE** | 1,0 |
| 3 | Exigencias concretas de E2EE y mención de los hallazgos de 2025 | 1,0 |
| 4 | Citar `mp.com.2`, `mp.com.3`, `mp.si.2` y `op.exp.10` | 1,0 |
| 4 | Citar `mp.com.4` con su requisito `.2` y el refuerzo exigible en categoría MEDIA | 1,0 |
|  | **Total** | **10** |

------------------------------------------------------------------------

#### Preguntas tipo test sobre este caso

##### 1. La oferta propone configurar TEA1 «por ser el de exportación libre». ¿Por qué es inaceptable?

- a) Porque su clave de 80 bits se reduce deliberadamente a unos 32 bits efectivos y se rompe en minutos (CVE-2022-24402).
- b) Porque su clave de 128 bits es incompatible con los terminales de exportación libre del parque municipal actual.
- c) Porque es un algoritmo sin clave que solo cifra la señalización y deja la voz del interfaz aire en claro.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §4.3.2

La clave de 80 bits de TEA1 se comprime a unos 32 bits efectivos, lo que permite romperla por fuerza bruta en minutos con un ordenador doméstico. La TCCA ha confirmado que la reducción fue intencionada (Acuerdo de Wassenaar).

##### 2. La oferta deja además TEA2 activo «por compatibilidad». ¿Mejora eso la seguridad de la red si TEA1 sigue soportado?

- a) Sí: los terminales negocian siempre el algoritmo más fuerte disponible, de modo que TEA1 nunca llegaría a usarse.
- b) Sí: TEA2 no tiene ninguna relación con TEA1, y basta con reservarlo para los grupos de conversación sensibles.
- c) No: en redes multicifrado, soportar TEA1 permite recuperar también la clave de los demás algoritmos (CVE-2025-52943).

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §4.3.2

La divulgación de agosto de 2025 demostró que admitir TEA1 junto a otros algoritmos compromete también a estos. No basta con dejar de usar TEA1: hay que dejar de soportarlo.

##### 3. ¿Qué exigencia concreta sobre algoritmos debe incorporarse al pliego de los 1.200 terminales?

- a) Desaconsejar TEA1 y exigir que los terminales lo conserven solo como algoritmo de reserva ante fallos.
- b) Prohibir expresamente TEA1 y exigir capacidad de migración a TEA set B (TEA5, TEA6 y TEA7) y a TAA2.
- c) Exigir TEA7 en sustitución de TEA2, por ser el algoritmo civil de 192 bits del TEA set B de la TCCA.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §4.3.2

TEA1 debe prohibirse, no desaconsejarse. En el TEA set B, TEA5 sustituye a TEA2, TEA6 a TEA3 y TEA7 a TEA1; TEA5 y TEA6 usan claves de 192 bits y TEA7 conserva una reducción efectiva a 56 bits.

##### 4. La red operaría en clase SC2 «para evitar la carga del centro de autenticación». ¿Qué clase debe exigirse?

- a) SC1, que evita la carga del centro de autenticación sin renunciar al cifrado del interfaz aire.
- b) SC2 con una clave estática más larga, que da la misma protección que SC3 sin autenticar.
- c) SC3, con clave derivada (DCK) y clave común (CCK), que exige autenticación, preferiblemente mutua.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §4.3.1

SC2 cifra con una clave estática precargada, la misma para todos y durante mucho tiempo; SC1 no cifra. SC3 usa una clave distinta por terminal que se renueva, y la autenticación mutua protege frente a una estación base falsa.

##### 5. ¿Por qué una red TETRA que no autentica queda condenada a la clave estática?

- a) Porque la DCK se deriva del propio proceso de autenticación: sin autenticación no hay clave derivada.
- b) Porque la DCK se distribuye cifrada con la SCK, que solo existe en las redes que no autentican.
- c) Porque la clave K viaja por el aire durante la autenticación y sin ella no se puede generar la CCK.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §4.3.1

Autenticar y cifrar están encadenados: del proceso de autenticación se deriva la DCK, propia de cada terminal y sesión. La clave K nunca se transmite por el aire.

##### 6. La oferta no incluye distribución de claves por el aire: se renovarían recogiendo los terminales en el almacén una vez al año. ¿Qué debe exigirse?

- a) Una renovación semestral en el almacén, que es la periodicidad mínima que fija el ENS para las claves.
- b) OTAR y un procedimiento de inhabilitación remota (stun y kill) para terminales perdidos o robados.
- c) Claves estáticas de mayor longitud, que no necesitan renovarse durante la vida útil de los terminales.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.3.1

Recoger 1.200 terminales impide reaccionar ante un compromiso de clave o la baja de un usuario. OTAR permite renovar las claves de miles de terminales sin recogerlos.

##### 7. El fabricante alega que «el cifrado de interfaz aire ya protege la comunicación de punta a punta». ¿Qué debe responderse?

- a) Que es falso: ese cifrado se descifra en la estación base y desde ahí la comunicación circula en claro por la infraestructura.
- b) Que es cierto: el cifrado de interfaz aire acompaña a la comunicación hasta que la descifra el terminal receptor.
- c) Que es cierto si la red trabaja en SC3, porque esa clase extiende el cifrado hasta la consola del centro de despacho.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §4.3.2 · §4.3.3

El cifrado de interfaz aire protege el tramo terminal ↔ estación base. El cifrado extremo a extremo cifra en el terminal emisor y descifra en el receptor; son complementarios, no alternativos.

##### 8. ¿Frente a quién NO protege el cifrado de interfaz aire de la red municipal?

- a) Frente a quien escuche con un receptor el tramo radio entre el terminal y la estación base.
- b) Frente al operador de la red y al personal con acceso a los equipos o a las grabaciones.
- c) Frente a quien capte por radio la señalización que intercambian el terminal y la red.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §4.3.3

Como se descifra en la estación base, no protege frente a quien accede a la infraestructura: el operador, el personal técnico, las grabaciones o un compromiso de los enlaces de transporte. Sí protege el tramo radio.

##### 9. Si finalmente se implanta cifrado extremo a extremo, ¿qué debe exigir el pliego?

- a) Basta exigir «cifrado extremo a extremo», porque el ETSI impone un único algoritmo común a todos los fabricantes.
- b) Basta exigir AES-128, que garantiza por sí solo 128 bits de entropía efectiva en cualquier implementación.
- c) Algoritmo y longitud de clave nombrados, protección frente a repetición, autenticación del contenido y derecho de auditoría.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §4.3.3

El ETSI no impone algoritmo de cifrado extremo a extremo. La CVE-2025-52941 halló una variante de AES-128 con entropía efectiva de 56 bits, y otras CVE de 2025 describen repetición e inyección de voz.

##### 10. Se propone conectar las consolas de despacho al segmento de la ofimática municipal. ¿Qué medida del ENS lo impide y qué exige en categoría MEDIA?

- a) mp.com.4, separación de flujos de información en la red, que en MEDIA exige [R1 o R2 o R3].
- b) mp.com.4, separación de flujos de información en la red, que en MEDIA todavía no se aplica.
- c) op.exp.10, protección de claves criptográficas, que exige que las consolas estén en otro edificio.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 4 · §5.2 · mp.com.4 ENS

mp.com.4 obliga a segregar el tráfico; en MEDIA exige uno de los refuerzos (segmentación lógica con VLAN, VPN o medios físicos separados), y en BÁSICA no aplicaría.

### Caso 3 — Renovación del título habilitante y decisión de evolución

#### Enunciado

El Área de Gobierno competente en seguridad y emergencias plantea a la unidad TIC tres asuntos que llegan a la vez:

1.  **Vence el título habilitante** que ampara el uso de las frecuencias de la red municipal y hay que tramitar su renovación. Un informe interno afirma que «el Ayuntamiento tiene concedidas esas frecuencias a perpetuidad por su condición de Administración pública».
2.  Se quiere **ampliar la red** para dar servicio también a los **servicios de limpieza viaria y de parques y jardines**, y se propone hacerlo «en la banda de emergencias, que es la nuestra».
3.  Un proveedor propone **sustituir íntegramente la red TETRA por teléfonos móviles comerciales con una aplicación de *push-to-talk***, argumentando que «da mejor cobertura, más caudal y cuesta menos».

Además, se recuerda que durante el **apagón del 28 de abril de 2025** la red municipal de radio **siguió operativa** mientras otros servicios se degradaban.

#### Cuestiones

**Cuestión 1 — Régimen jurídico del espectro (3 puntos).** Corrija la afirmación del informe interno. Determine la modalidad de uso, el título habilitante que corresponde, su fundamento legal exacto y su duración.

**Cuestión 2 — Elección de banda (2 puntos).** Valore la propuesta de dar servicio a limpieza y a parques en la banda de emergencias. Indique qué notas del CNAF resuelven la cuestión y qué banda correspondería.

**Cuestión 3 — Sustitución por telefonía comercial (3 puntos).** Elabore la respuesta técnica a la propuesta del proveedor, con al menos cinco argumentos, y sitúe el episodio del apagón en el razonamiento.

**Cuestión 4 — Evolución realista (2 puntos).** Proponga la vía de evolución que sí es defendible, citando los estándares aplicables y el espectro que la normativa española tiene reservado para ello.

#### Solución orientativa

- **C1**: (§5.2) La afirmación es **incorrecta en los dos extremos**. El **espectro radioeléctrico es un bien de dominio público cuya titularidad y administración corresponden al Estado** (**art. 85.1** de la Ley 11/2022): el Ayuntamiento **no tiene concedidas** frecuencias, sino **derecho de uso** sometido a título habilitante. La modalidad es **uso privativo** (art. 88.1: explotación en exclusiva o por un número limitado de usuarios de determinadas frecuencias en un mismo ámbito físico) en régimen de **autoprestación**. El título habilitante que corresponde es la **afectación demanial**, conforme al **art. 88.5.b)**, que otorga el uso privativo para autoprestación mediante autorización individual «**salvo en el caso de Administraciones públicas, que requerirán de afectación demanial**»; **no** cabe la **concesión**, que además exigiría **ostentar la condición de operador de comunicaciones electrónicas** (art. 88.6). Y **no es a perpetuidad**: el **art. 94.1** fija que los derechos de uso privativo sin limitación de número se otorgan «hasta el **31 de diciembre del año natural en que cumplan su quinto año de vigencia**», **renovables por períodos de cinco años**. Deben citarse también las **condiciones asociadas** del art. 91 (uso eficaz y eficiente, características técnicas, no interferencia, exposición radioeléctrica) y la **tasa por reserva del dominio público radioeléctrico**.
- **C2**: (§3.1) La propuesta **no encaja**. La **nota UN-28** del CNAF reserva las subbandas **380-385 y 390-395 MHz** —excepción a la reserva de la banda 235-399,9 MHz al Ministerio de Defensa— a «**redes de servicios de seguridad de las Fuerzas y Cuerpos de Seguridad del Estado y redes de servicios de emergencia**», de conformidad con la Decisión CEPT **ECC/DEC(08)05**. Un servicio de **limpieza viaria** o de **parques y jardines** no es ninguna de las dos cosas. La banda que corresponde es la de la **nota UN-31**: las subbandas **410-415,3 y 420-425,3 MHz**, que el CNAF destina a «**sistemas digitales de acceso aleatorio de canales (TETRA y otros)**» con **canalización de 25 kHz** y **separación dúplex de 10 MHz**. El criterio a retener, y que la pregunta busca, es que **la banda la determina el SERVICIO, no la condición del solicitante**. Debe añadirse que el CNAF vigente es la **Orden TDF/732/2026, de 10 de julio**, que sustituyó a la Orden ETD/1449/2021 con efectos de **18 de julio de 2026**, y que la propia nota UN-28 exige un **plan exhaustivo de reutilización** por la saturación de la banda en entornos urbanos densos.
- **C3**: (§5.1, §5.3) La sustitución **no es defensible**, y los argumentos son al menos estos seis: **(1) Prioridad.** En una red comercial el Ayuntamiento **no decide a quién se desaloja**; TETRA ofrece prioridad de acceso, **prioridad con desalojo** y llamada de emergencia gobernadas por el titular de la red. **(2) Modo directo.** Un teléfono móvil **no puede** comunicarse con otro si cae la red; el **DMO** de TETRA sí, y es innegociable para bomberos y equipos de rescate. **(3) Inmediatez.** Establecimiento de llamada de grupo por debajo de **300 ms**, frente a segundos. **(4) Disponibilidad y control.** El titular decide dónde pone las estaciones base, cuánta batería instala y qué solapamiento de cobertura mantiene; con una red comercial se depende del respaldo de un tercero. **(5) Comunicación de grupo nativa**, con afiliación, DGNA y entrada tardía, frente a grupos de mensajería o multiconferencias de establecimiento lento. **(6) Terminal de trabajo**, con PTT, botón de emergencia, detección de «hombre caído», robustez y autonomía de jornada. El **apagón del 28 de abril de 2025** es la evidencia empírica que cierra el argumento: la red TETRA **siguió operativa** gracias al **respaldo energético de los emplazamientos** —baterías en los repetidores— mientras la telefonía convencional se degradaba, hasta el punto de que la Comunidad de Madrid, tras analizarlo, dotó en **mayo de 2026** de un terminal TETRA a **53 municipios pequeños** para garantizar su contacto con el 112. Se valorará que se enuncie la lección de fondo: **un servicio crítico solo es resiliente si lo son todas sus dependencias, empezando por la energía**, y que ello está respaldado por la medida **`mp.if.4`** del ENS.
- **C4**: (§5.4) La vía defendible es la **coexistencia por fases**, no la sustitución. Dos caminos complementarios: **(a) TEDS**, la aportación de datos de **TETRA Release 2** (**TR 102 580**), con anchos de canal de **25, 50, 100 y 150 kHz** y modulaciones **π/8-D8PSK, 4-QAM, 16-QAM y 64-QAM** con adaptación al enlace, que amplía la capacidad **manteniendo la misma red**, aunque exige más espectro por canal en una banda ya saturada; y **(b) la banda ancha crítica** del **3GPP**: **MCPTT**, normalizado en la **Release 13** culminada en **2016** (**TS 22.179**), más **MCVideo** y **MCData** de la Release 14, apoyados en **GCSE**, **eMBMS** y **ProSe**. El modelo operativo sería el que ya se aplica de hecho: **TETRA para la voz crítica y los datos cortos garantizados**, y **banda ancha para lo que necesita caudal** (vídeo, cartografía, imagen médica), con **terminales híbridos** e **interconexión en el centro de mando**. Y el dato que remata la respuesta: el **CNAF ya tiene reservado el espectro** para ello — **733-736 / 788-791 MHz** para el sistema PPDR de **ámbito nacional** y **698-703 / 753-758 MHz** para las redes de **ámbito autonómico y local**, además de **452-457,5 / 462-467,5 MHz** en aplicación de la Decisión **ECC/DEC(16)02**, «**preferentemente para el sistema de ámbito nacional**» (nota UN-31 del CNAF), de modo que para una red municipal el bloque de referencia sigue siendo el de 698-703 / 753-758 MHz. Es decir: **el recurso está apartado; lo que está pendiente es la decisión**. Se valorará citar el precedente del **SIRDEE**, que desde julio de 2024 pilota su migración a **LTE manteniendo la red de banda estrecha** durante la transición.

#### Criterios de evaluación

| Cuestión | Elemento | Puntos |
|----|----|----|
| 1 | Corregir la idea de «frecuencias concedidas»: dominio público estatal (art. 85.1) | 0,75 |
| 1 | Identificar **uso privativo en autoprestación** | 0,75 |
| 1 | Identificar la **afectación demanial** y citar el **art. 88.5.b)** | 1,0 |
| 1 | Duración del art. 94.1 (cinco años, renovables) | 0,5 |
| 2 | Descartar la banda de emergencias citando la **nota UN-28** | 1,0 |
| 2 | Proponer 410-415,3 / 420-425,3 MHz citando la **nota UN-31**, con 25 kHz y dúplex de 10 MHz | 1,0 |
| 3 | Aportar al menos cinco argumentos técnicos sólidos | 2,0 |
| 3 | Usar el apagón del 28-4-2025 como evidencia y enunciar la lección sobre dependencias | 1,0 |
| 4 | Describir **TEDS** con sus anchos de canal y modulaciones | 0,75 |
| 4 | Citar **MCPTT / Release 13 / TS 22.179** y el modelo de coexistencia | 0,75 |
| 4 | Citar el espectro PPDR reservado, distinguiendo el bloque **autonómico y local** | 0,5 |
|  | **Total** | **10** |

#### Preguntas tipo test sobre este caso

##### 1. Un informe interno afirma que el Ayuntamiento tiene concedidas las frecuencias «a perpetuidad por su condición de Administración pública». ¿Cuál es el punto de partida para corregirlo?

- a) El espectro es dominio público municipal dentro del término del Ayuntamiento, aunque su uso esté sujeto a inscripción registral.
- b) Las frecuencias solo se conceden a perpetuidad a la Administración General del Estado, y no a las entidades locales.
- c) El espectro es dominio público cuya titularidad corresponde al Estado: el Ayuntamiento solo tiene un derecho de uso con título habilitante.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §5.2 · art. 85.1 Ley 11/2022

Conforme al artículo 85.1 de la Ley 11/2022, el espectro radioeléctrico es un bien de dominio público cuya titularidad y administración corresponden al Estado.

##### 2. ¿Qué modalidad de uso del espectro corresponde a la red de radio municipal?

- a) Uso común, como el de las redes Wi-Fi abiertas.
- b) Uso privativo en régimen de autoprestación.
- c) Uso especial, por ser el titular una Administración.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §5.2 · art. 88.1 Ley 11/2022

El uso privativo es la explotación en exclusiva o por un número limitado de usuarios de determinadas frecuencias en un mismo ámbito físico (art. 88.1); la red municipal la explota el propio Ayuntamiento para sus servicios, es decir, en autoprestación.

##### 3. Para la renovación, alguien propone solicitar una concesión. ¿Es correcto?

- a) No: la concesión exige ser operador (art. 88.6); a una Administración en autoprestación le corresponde la afectación demanial.
- b) Sí: la concesión demanial es el título propio de las Administraciones públicas para el uso privativo del espectro.
- c) No: lo que procede es una autorización individual, como a cualquier otro usuario en régimen de autoprestación.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §5.2 · art. 88.5.b) Ley 11/2022

Conforme al artículo 88.5.b) de la Ley 11/2022, el uso privativo para autoprestación se otorga por autorización individual «salvo en el caso de Administraciones públicas, que requerirán de afectación demanial».

##### 4. ¿Qué duración tiene el derecho de uso privativo que se renueva?

- a) Indefinida, mientras el Ayuntamiento siga pagando la tasa por reserva del dominio público radioeléctrico.
- b) Hasta el 31 de diciembre del año en que cumpla su quinto año de vigencia, renovable por periodos de cinco años.
- c) Diez años improrrogables, tras los cuales hay que solicitar un título habilitante completamente nuevo.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §5.2 · art. 94.1 Ley 11/2022

El artículo 94.1 de la Ley 11/2022 fija la duración de los derechos de uso privativo sin limitación de número: hasta el 31 de diciembre del año natural en que cumplan su quinto año de vigencia, renovables por periodos de cinco años.

##### 5. Se propone dar servicio a limpieza viaria y a parques y jardines «en la banda de emergencias, que es la nuestra». ¿Es posible?

- a) Sí: la banda de emergencias corresponde al Ayuntamiento por su condición de Administración pública titular de la red.
- b) Sí, siempre que limpieza y parques usen grupos de conversación distintos de los de Policía Municipal y Bomberos.
- c) No: la nota UN-28 reserva 380-385 / 390-395 MHz a redes de seguridad del Estado y de emergencias, y esos servicios no lo son.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §3.1 · nota UN-28 CNAF

La banda la determina el servicio que se presta, no la condición del solicitante. La nota UN-28 reserva esas subbandas a redes de seguridad de las Fuerzas y Cuerpos de Seguridad del Estado y a redes de servicios de emergencia.

##### 6. ¿Qué banda correspondería a la red de limpieza viaria y de parques y jardines?

- a) 410-415,3 / 420-425,3 MHz (nota UN-31), con canalización de 25 kHz y separación dúplex de 10 MHz.
- b) 698-703 / 753-758 MHz, el bloque PPDR de banda ancha reservado al ámbito autonómico y local.
- c) 380-385 / 390-395 MHz, con canalización de 12,5 kHz para los servicios que no son de emergencia.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 2 · §3.1 · nota UN-31 CNAF

La nota UN-31 destina esas subbandas a «sistemas digitales de acceso aleatorio de canales (TETRA y otros)». El bloque de 698-703 / 753-758 MHz es para banda ancha PPDR, no para servicios municipales generales.

##### 7. Un proveedor propone sustituir la red TETRA por teléfonos comerciales con una aplicación de push-to-talk. ¿Cuál de estos argumentos rebate correctamente la propuesta?

- a) TETRA ofrece mucho más caudal de datos que las redes móviles comerciales de banda ancha para vídeo y cartografía.
- b) La telefonía móvil comercial no admite ningún tipo de comunicación de grupo entre varios usuarios a la vez.
- c) En una red comercial el Ayuntamiento no decide a quién se desaloja, y un móvil no se comunica con otro si cae la red.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 3 · §5.1 · §5.3

TETRA ofrece prioridad y desalojo gobernados por el titular de la red y modo directo sin infraestructura. Su punto débil es el caudal (28,8 kbit/s en Release 1), y la telefonía comercial sí tiene grupos, aunque de establecimiento lento.

##### 8. ¿Qué tiempo de establecimiento de llamada de grupo ofrece TETRA, frente a la telefonía comercial?

- a) Por debajo de 300 ms, frente a segundos.
- b) Por debajo de 3 s, frente a varios minutos.
- c) Por debajo de 30 ms, frente a unos 300 ms.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §5.1

El establecimiento de la llamada de grupo por debajo de 300 ms es uno de los rasgos que distinguen la radiocomunicación móvil privada de la telefonía celular pública.

##### 9. Durante el apagón del 28 de abril de 2025 la red municipal de radio siguió operativa. ¿Qué lección de fondo debe extraerse?

- a) Que la red TETRA no depende de la energía eléctrica, porque sus terminales portátiles funcionan con batería.
- b) Que un servicio crítico solo es resiliente si lo son todas sus dependencias, empezando por la energía (mp.if.4 ENS).
- c) Que la telefonía comercial es igual de resiliente si se contratan tarifas con prioridad para emergencias.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §5.3 · mp.if.4 ENS

La red siguió operativa gracias al respaldo energético de los emplazamientos (baterías en los repetidores). Cada emplazamiento debe tener baterías para varias horas y, en los principales, grupo electrógeno, con respaldo en mp.if.4.

##### 10. ¿Qué vía de evolución es defendible y qué espectro tiene reservado el CNAF para las redes locales?

- a) Sustitución inmediata de TETRA por MCPTT, con el bloque de 733-736 / 788-791 MHz reservado al ámbito local.
- b) Sustitución de TETRA por TEDS, que no necesita más espectro por canal y libera la banda TETRA del Ayuntamiento.
- c) Coexistencia: TETRA para la voz crítica y banda ancha (MCPTT, Release 13) para el caudal, con 698-703 / 753-758 MHz.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §5.4

El modelo es de coexistencia por fases. El CNAF reserva 733-736 / 788-791 MHz al sistema PPDR nacional y 698-703 / 753-758 MHz a las redes autonómicas y locales. TEDS amplía TETRA, pero exige más espectro por canal.

## Fuentes

### Tier 1 — Normativa y estándares

#### Normativa española

| ID | Referencia |
|----|----|
| `[CNAF]` | **[Orden TDF/732/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-15661), de 10 de julio**, por la que se aprueba el **Cuadro Nacional de Atribución de Frecuencias** (BOE núm. 173, de 17 de julio de 2026, págs. 100980 a 101328). **Sustituye a la [Orden ETD/1449/2021](https://www.boe.es/buscar/act.php?id=BOE-A-2021-21346), de 16 de diciembre, con efectos de 18 de julio de 2026.** Incorpora las previsiones de la **Conferencia Mundial de Radiocomunicaciones de 2023**, en vigor en su mayoría desde el 1 de enero de 2025. Notas de utilización nacional citadas en este tema: **UN-28** (banda 235-399,9 MHz, con la excepción de 380-385 y 390-395 MHz para FCSE y servicios de emergencia), **UN-31** (banda 406-470 MHz; la subbanda 410-430 MHz con dúplex de 10 MHz y los tramos 410-415,3 / 420-425,3 MHz para «sistemas digitales de acceso aleatorio de canales (**TETRA** y otros)» con canalización de 25 kHz; y los bloques 452-457,5 / 462-467,5 MHz para PPDR de banda ancha), **UN-27** (223-235 MHz, *trunking* con canalización de 12,5 kHz), **UN-77** (datos en 400 MHz) y la nota de la banda de **700 MHz** (703-733 / 758-788 MHz para banda ancha, con **733-736 / 788-791 MHz** para PPDR de ámbito nacional y **698-703 / 753-758 MHz** para PPDR autonómico y local). |
| `[LGTel]` | **[Ley 11/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-10757), de 28 de junio, General de Telecomunicaciones**. Preceptos citados, verificados sobre el texto consolidado del BOE: **art. 4** (servicios para la seguridad nacional, la defensa nacional, la **seguridad pública**, la seguridad vial y la **protección civil**; su apartado 1 declara que «**sólo tienen la consideración de servicio público los servicios regulados en este artículo**»), **art. 85** (el espectro es **bien de dominio público** de titularidad y administración estatal), **art. 88** (uso **común, especial o privativo**; títulos habilitantes en forma de **autorización general, autorización individual, afectación o concesión**; y el apartado **88.5.b)**, que somete a las Administraciones públicas a **afectación demanial**), **art. 91** (condiciones asociadas a los títulos habilitantes), **art. 94** (duración general de **cinco años**, hasta el 31 de diciembre del año natural en que se cumplan, renovable por períodos de cinco) y **art. 74** (comunicaciones de emergencia y número **112**). |
| `[RD123-2017]` | **[Real Decreto 123/2017](https://www.boe.es/buscar/act.php?id=BOE-A-2017-2460), de 24 de febrero**, por el que se aprueba el Reglamento sobre el uso del dominio público radioeléctrico. Su **art. 6** es el que ordena aprobar el CNAF; regula además el procedimiento de los títulos habilitantes, la inspección y la protección activa del espectro. |
| `[ENS]` | **[Real Decreto 311/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191), de 3 de mayo**, por el que se regula el **Esquema Nacional de Seguridad** (BOE núm. 106, de 4 de mayo de 2022). Medidas citadas, verificadas contra el PDF del BOE: **`mp.com.1`** (perímetro seguro), **`mp.com.2`** (protección de la confidencialidad), **`mp.com.3`** (protección de la integridad y de la autenticidad), **`mp.com.4`** (**separación de flujos de información en la red**, con `mp.com.4.2`: «si se emplean comunicaciones inalámbricas, será en un segmento separado», y los refuerzos R1 VLAN, R2 VPN, R3 medios físicos y R4 puntos de interconexión), **`mp.if.1`** a **`mp.if.7`** (áreas separadas, identificación de personas, acondicionamiento de locales, **energía eléctrica**, incendios, inundaciones y registro de equipamiento), **`mp.si.2`** (criptografía), **`mp.eq.4`** (otros dispositivos conectados a la red), **`op.cont.1`** a **`op.cont.4`** (análisis de impacto, plan de continuidad, pruebas periódicas y **medios alternativos**), **`op.exp.10`** (protección de claves criptográficas) y **`op.acc.5`** y **`op.acc.6`**. |
| `[L17-2015]` | **[Ley 17/2015](https://www.boe.es/buscar/act.php?id=BOE-A-2015-7730), de 9 de julio, del Sistema Nacional de Protección Civil**. Marco de la actuación de los servicios de emergencia y de la interoperabilidad entre administraciones; es la norma a la que remite el art. 4.5 de la [Ley 11/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-10757) junto con la [Ley 8/2011](https://www.boe.es/buscar/act.php?id=BOE-A-2011-7630) de infraestructuras críticas. |
| `[L8-2011]` | **[Ley 8/2011](https://www.boe.es/buscar/act.php?id=BOE-A-2011-7630), de 28 de abril**, por la que se establecen medidas para la **protección de las infraestructuras críticas**, y su reglamento ([RD 704/2011](https://www.boe.es/buscar/act.php?id=BOE-A-2011-8849)). Encuadra la red de radiocomunicaciones de emergencia como infraestructura a proteger. |
| `[L40-2015]` | **[Ley 40/2015](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566), de 1 de octubre**, de Régimen Jurídico del Sector Público. **Art. 156**, fundamento legal del ENS y del ENI. Ver Tema 39. |
| `[LCSP]` | **[Ley 9/2017](https://www.boe.es/buscar/act.php?id=BOE-A-2017-12902), de 8 de noviembre, de Contratos del Sector Público**. Marco de la contratación del mantenimiento y la evolución de la red municipal; relevante para los contratos de servicios plurianuales de comunicaciones críticas. |
| `[NIS2]` | **[Directiva (UE) 2022/2555](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32022L2555)** (NIS2), que incluye entre los sectores de alta criticidad las **infraestructuras digitales** y la **administración pública**. Pendiente de transposición en España a agosto de 2026. |
| `[RGPD]` | [Reglamento (UE) **2016/679**](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679), General de Protección de Datos, y **[Ley Orgánica 3/2018](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673)**. Relevantes por la **geolocalización de los terminales** y la **grabación de las comunicaciones** en los centros de despacho. |

#### Especificaciones del ETSI (serie TETRA)

| ID | Referencia |
|----|----|
| `[EN392-1]` | **ETSI EN 300 392-1**, *TETRA; Voice plus Data (V+D); Part 1: General network design*. Modelo de referencia, entidades funcionales y **interfaces I1 a I6**. La versión V1.6.1 es de abril de 2020. |
| `[EN392-2]` | **ETSI EN 300 392-2**, *TETRA; V+D; Part 2: Air Interface (AI)*. Es **la norma central del tema**: capa física, capa de enlace y capa de red del interfaz aire. Define la portadora de 25 kHz, los **cuatro intervalos TDMA**, la modulación **π/4-DQPSK** a 18 kbaudios, los tipos de ráfaga y los canales lógicos. |
| `[EN392-3]` | **ETSI EN 300 392-3**, *TETRA; V+D; Part 3: Interworking at the Inter-System Interface (**ISI**)*. Interconexión entre redes TETRA de operadores u organismos distintos. |
| `[EN392-4]` | **ETSI EN 300 392-4**, *TETRA; V+D; Part 4: Gateways*. Pasarelas hacia la red telefónica pública (PSTN) y hacia RDSI. |
| `[EN392-5]` | **ETSI EN 300 392-5**, *TETRA; V+D and DMO; Part 5: **Peripheral Equipment Interface (PEI)***. Interfaz entre el terminal y un equipo de datos (ordenador embarcado, terminal de despacho, sensor). Es la **I4** del modelo de referencia. |
| `[EN392-7]` | **ETSI EN 300 392-7**, *TETRA; V+D; Part 7: **Security***. Arquitectura de seguridad: autenticación mutua, **clases de seguridad**, gestión de claves (SCK, DCK, CCK, GCK), **OTAR** y cifrado de identidades (ESI). |
| `[EN392-9]` | **ETSI EN 300 392-9 a -12**, *Supplementary services stage 1/2/3*. Servicios suplementarios: prioridad de acceso, **prioridad con desalojo** (*pre-emptive priority call*), escucha ambiente, escucha discreta, **DGNA**, identificación de llamante, desvío e inclusión. |
| `[EN394]` | **ETSI EN 300 394**, *TETRA; Conformance testing specification*. Pruebas de conformidad de terminales e infraestructura; es la pieza que hace real la interoperabilidad multifabricante. |
| `[EN395]` | **ETSI EN 300 395**, *TETRA; Speech codec for full-rate traffic channel*. Códec **ACELP**: 137 bits por trama de voz de 30 ms → **4,567 kbit/s** netos. |
| `[EN396]` | **ETSI EN 300 396**, *TETRA; **Direct Mode Operation (DMO)***, partes 1 a 10. Define el modo directo, el **DM-REP** (repetidor de **tipo 1A**, **1B** y **tipo 2**), el **DM-GATE** (pasarela) y el **DM-REP/GATE**, además de la seguridad en modo directo. La parte 4 (V1.4.1, 2011) es la de tipos de repetidor. |
| `[TS392-7]` | **ETSI TS 100 392-7**, versión técnica de la parte de seguridad, con el detalle de los algoritmos de autenticación **TAA1** y **TAA2** y de las claves. |
| `[TS104053]` | **ETSI TS 104 053**, *TETRA Air Interface Security, Algorithms Specifications*. La **parte 1** (V1.2.1, febrero de 2025) publica el **TEA set A** (TEA1 a TEA4), hasta entonces confidencial; la publicación fue consecuencia directa de la divulgación de 2023. |
| `[TR102580]` | **ETSI TR 102 580**, *TETRA Release 2; Designer's Guide; TETRA High-Speed Data (HSD); **TETRA Enhanced Data Service (TEDS)***. Anchos de canal de **25, 50, 100 y 150 kHz** y modulaciones **π/8-D8PSK, 4-QAM, 16-QAM y 64-QAM** con adaptación al enlace. |
| `[ETR300-1]` | **ETSI ETR 300-1** (mayo de 1997), *TETRA; Designers' guide; Part 1: Overview, technical description and radio aspects*. Fuente del **modelo de interfaces I1-I6** que sigue usándose para explicar la arquitectura. |
| `[TTR001-11]` | **TCCA / TETRA Association, TTR 001-11 v4.1.0** (17 de agosto de 2023), *Air Interface Encryption*. Documento libre que describe el servicio de cifrado de interfaz aire, las **clases de seguridad SC1, SC2, SC3 y SC3G**, las claves estándar (SCK, DCK, CCK, GCK) frente a las **claves extendidas** (SCKX, DCKX, CCKX, GCKX) del **TEA set B**, el **modo de repliegue** de SC3 a SC2 y el cifrado de identidades **ESI** y **MAE**. |

#### Especificaciones de otras organizaciones

| ID | Referencia |
|----|----|
| `[ECC0805]` | **Decisión ECC/DEC(08)05** de la CEPT, sobre bandas armonizadas para sistemas digitales de **redes de emergencia** de banda estrecha y ancha (**380-385 / 390-395 MHz** y 380-470 MHz). Es la decisión europea que el CNAF traspone en su **nota UN-28**. |
| `[ECC0606]` | **Decisión ECC/DEC(06)06** de la CEPT, sobre **sistemas móviles digitales de banda estrecha PMR/PAMR** en VHF y UHF (68-87,5, 146-174, 406,1-410, **410-430**, 440-450 y 450-470 MHz). |
| `[ECC1602]` | **Decisión ECC/DEC(16)02** de la CEPT, sobre condiciones técnicas armonizadas y bandas para sistemas de **banda ancha PPDR** (452-457,5 / 462-467,5 MHz). Recogida en la nota **UN-31** del CNAF. |
| `[DEC2016-687]` | **Decisión de Ejecución (UE) 2016/687** de la Comisión, de 28 de abril de 2016, sobre la armonización de la banda de **694-790 MHz**. Es la base de los bloques de PPDR de banda ancha del CNAF. |
| `[3GPP-MC]` | **3GPP, servicios de misión crítica**. **MCPTT** (*Mission Critical Push To Talk*) se normalizó en la **Release 13**, culminada en 2016; la etapa 1 es la **TS 22.179** y la etapa 2, la TS 23.179 (renumerada como **TS 23.379**). En la Release 14 se añadieron **MCVideo** y **MCData**. Habilitadores previos: **GCSE** (comunicaciones de grupo), **eMBMS** (difusión) y **ProSe** (proximidad, el equivalente al modo directo). |
| `[UIT-RR]` | **Unión Internacional de Telecomunicaciones**, *Reglamento de Radiocomunicaciones*, y las **Conferencias Mundiales de Radiocomunicaciones**; la **CMR-2023** es la que incorpora el CNAF de 2026. Define el reparto internacional del espectro en tres **Regiones** (España está en la **Región 1**). |
| `[UIT-M2014]` | **UIT-R, Informe M.2014**, *Spectrum efficient digital land mobile systems for dispatch traffic*. Descripción comparada de los sistemas digitales de despacho, entre ellos TETRA y TETRAPOL. |

------------------------------------------------------------------------

### Tier 2 — Informes, investigación y datos de despliegue

| ID | Referencia |
|----|----|
| `[TETRABURST]` | **Midnight Blue**, *TETRA:BURST* (agosto de 2023) y el artículo académico *All cops are broadcasting: TETRA under scrutiny*, **USENIX Security 2023**. Cinco vulnerabilidades: **CVE-2022-24401** (el generador de flujo de clave del cifrado de interfaz aire depende del **tiempo de red**, que se difunde sin autenticar → oráculo de descifrado), **CVE-2022-24402** (**puerta trasera en TEA1**: la clave de 80 bits se reduce a una longitud efectiva de **unos 32 bits**, forzable en minutos con hardware doméstico), **CVE-2022-24403** (el esquema de ofuscación de identidades permite **desanonimizar y seguir** a los usuarios), **CVE-2022-24404** (falta de autenticación del texto cifrado → ataques de maleabilidad) y una quinta de menor gravedad. |
| `[2TETRA]` | **Midnight Blue**, *2TETRA:2BURST*, presentado en **Black Hat USA el 7 de agosto de 2025** y en WHY2025 el 11 de agosto. Seis hallazgos: **CVE-2025-52940** (repetición e inyección de voz en el cifrado **extremo a extremo**), **CVE-2025-52941** (variante **debilitada de AES-128** con entropía efectiva reducida a **56 bits**), **CVE-2025-52942** (los **SDS** cifrados extremo a extremo no tienen protección antirrepetición), **CVE-2025-52943** (en redes multicifrado, admitir **TEA1** junto a otros algoritmos permite recuperar la clave), **CVE-2025-52944** (**el protocolo TETRA carece de autenticación de mensajes**, lo que permite inyectar mensajes arbitrarios) y **MBPH-2025-001** (la corrección del ETSI para CVE-2022-24401 **no impide** la recuperación del flujo de clave). |
| `[TCCA-RD]` | **TCCA**, *Research Disclosures*, posición oficial sobre ambas divulgaciones. Reconoce la reducción de clave de **TEA1** («fue necesaria para cumplir el **Acuerdo de Wassenaar**» de control de exportaciones) y la debilidad del cifrado de identidades del set A; considera **TEA2 y TEA3** seguros, con **80 bits** sin reducción; describe el **TEA set B** (**TEA5 y TEA6 con claves de 192 bits**; **TEA7** con reducción efectiva a **56 bits** por las mismas razones de exportación) y recomienda migrar a **TAA2** y desplegar cifrado extremo a extremo. |
| `[TCCA-B]` | **TCCA**, *New Additional TETRA Security Algorithms* (webinar de junio de 2023) y la publicación del **TEA set B**, liberado en **octubre de 2022**: **TEA5** sucede a TEA2 para redes de emergencia europeas, **TEA6** sucede a TEA3 para redes militares y de emergencia extraeuropeas afines, y **TEA7** sucede a TEA1 como el único disponible para infraestructuras críticas y usos civiles generales. |
| `[TCCA-GLOBAL]` | **TCCA**, *TETRA Home* y actualizaciones de Critical Communications World. TETRA se usa en **más de 124 países**, en seguridad pública, transporte, energía, minería, puertos, aeropuertos, metros y grandes eventos. |
| `[TELEFONICA-2026]` | **Telefónica**, nota de prensa de **23 de marzo de 2026**: Telefónica Soluciones se adjudica el **mantenimiento integral y la evolución tecnológica de la infraestructura de radiocomunicaciones móviles digitales DIMETRA-TETRA del Ayuntamiento de Madrid**, con **cinco años** de duración, **disponibilidad 24×7** y una arquitectura que unifica el despacho y la grabación de comunicaciones en una plataforma de alta disponibilidad. Da servicio a **más de 3.000 efectivos** de **Policía Municipal, Bomberos, SAMUR-Protección Civil, Agentes de Movilidad, SAMUR Social y Parques y Jardines**. |
| `[AYTO-CONTR]` | **Ayuntamiento de Madrid**, acuerdo de la Junta de Gobierno de **30 de julio de 2026**: cuatro contratos de seguridad y emergencias por más de **6,3 millones de euros**, entre ellos el de **operación, gestión, supervisión y mantenimiento de las infraestructuras, equipos y redes de radiocomunicaciones** de la Dirección General de Policía Municipal, con presupuesto plurianual de **933.000 euros** y **tres años** de duración prorrogables. |
| `[CISEM]` | **Ayuntamiento de Madrid**, *Centro Integrado de Seguridad y Emergencias (CISEM)*, calle Rufino Blanco 2 (distrito de Salamanca). Coordina **Policía Municipal (092), Bomberos, SAMUR-Protección Civil y Agentes de Movilidad**, con del orden de **3.000 incidentes diarios**. |
| `[CM-TETRA]` | **Comunidad de Madrid**, notas de prensa de **30 de octubre de 2024**, **2 de agosto de 2025** y **11 de mayo de 2026**. Red TETRA autonómica de **113 estaciones base** y **5.316 terminales**, gestionada por la **ASEM 112**; da servicio al Cuerpo de Bomberos, Agentes Forestales, BRIF, ERIVE, SUMMA 112, Protección Civil, policías locales adheridas a la ESICAM y la D. G. de Carreteras. Inversión de casi **40 millones de euros a cinco años** para su modernización; **6,1 millones** en 2025 con **2.263 terminales nuevos** (1.600 Bomberos, 412 Agentes Forestales, 140 Protección Civil, 66 Carreteras y 45 Madrid 112). En **mayo de 2026** se dotó de un terminal TETRA a **53 municipios pequeños** tras comprobar, en el **apagón del 28 de abril de 2025**, que la red **siguió operativa** gracias a las baterías de respaldo de los repetidores. |
| `[SIRDEE]` | **Ministerio del Interior**, *Sistema de Radiocomunicaciones Digitales de Emergencia del Estado (SIRDEE)*. En servicio desde el **año 2000**, construido sobre **TETRAPOL** —no sobre TETRA—, con cobertura nacional para las Fuerzas y Cuerpos de Seguridad del Estado y Defensa, más terminales de policías locales, protección civil y servicios de emergencia. Desde **julio de 2024** hay en marcha un proyecto piloto de **migración a banda ancha LTE** con Telefónica, manteniendo la red de banda estrecha durante la transición. |
| `[METRO]` | **Metro de Madrid** y **Comunidad de Madrid**, nota de **18 de marzo de 2020**: adjudicación de la instalación del sistema de radiotelefonía digital **TETRA** en el tramo Paco de Lucía-Puerta de Arganda de la **línea 9**, con una inversión de **5,2 millones de euros**. La tecnología comunica al Puesto de Mando con el personal de estaciones y los conductores y permite llamadas de grupo en emergencia. |
| `[W3C-MERCADO]` | Informes de mercado del sector de comunicaciones críticas (2025-2026), citados únicamente para dimensionar la vigencia comercial de TETRA frente a la banda ancha crítica. Dato ilustrativo, **no memorizable**. |

------------------------------------------------------------------------

### Tier 3 — Contexto municipal

| ID | Referencia |
|----|----|
| `[MADRID-ORG]` | **Ayuntamiento de Madrid**, Reglamento Orgánico del Gobierno y de la Administración (ROGA, 2004) y organigrama vigente: Área de Gobierno competente en seguridad y emergencias, Dirección General de Policía Municipal, Dirección General de Emergencias y Protección Civil, y el **Organismo Autónomo Informática del Ayuntamiento de Madrid (IAM)**. Ver Temas 3 y 4. |
| `[MADRID-SAMUR]` | **SAMUR-Protección Civil**, portal municipal: Central de Comunicaciones y su encaje en el CISEM. |
| `[MADRID-TRANSP]` | **Portal de transparencia y de contratación del Ayuntamiento de Madrid**: perfil del contratante, del que proceden los datos de los contratos de radiocomunicaciones citados. |

------------------------------------------------------------------------
