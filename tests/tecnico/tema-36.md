# Test del tema 36. Seguridad y protección en redes de comunicaciones

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-36.html>

## Batería de preguntas

### 1. ¿Cuántas dimensiones de seguridad contempla el Esquema Nacional de Seguridad y cuáles son?

- a) Tres: confidencialidad, integridad y disponibilidad
- b) Cinco: confidencialidad, integridad, trazabilidad, autenticidad y disponibilidad
- c) Cuatro: confidencialidad, integridad, disponibilidad y no repudio

**Respuesta correcta:** b) · **Referencia:** §1.1 [ENS]

La nemotécnica es <strong>CITAD</strong>. La opción A recoge la tríada clásica CIA, que es la formulación teórica internacional, pero el marco español añade <strong>trazabilidad</strong> y <strong>autenticidad</strong>, y de cada dimensión se predica un <strong>nivel</strong> que determina qué medidas son exigibles.

### 2. Un sistema tiene confidencialidad MEDIA, integridad MEDIA, trazabilidad BAJA, autenticidad MEDIA y disponibilidad ALTA. ¿Cuál es su categoría?

- a) MEDIA, porque es el nivel que más se repite
- b) BÁSICA, porque hay una dimensión en nivel BAJO
- c) ALTA, porque basta con que una dimensión sea de nivel ALTO

**Respuesta correcta:** c) · **Referencia:** §1.1 [ENS]

La categoría se deriva de la <strong>dimensión más exigente</strong>: si alguna es ALTO, el sistema es de categoría ALTA; si ninguna es ALTO pero alguna es MEDIO, es MEDIA; y en el resto de casos, BÁSICA. No se calcula por promedio ni por moda.

### 3. El artículo 9 del ENS, «existencia de líneas de defensa», es el fundamento normativo de:

- a) La defensa en profundidad: varias capas independientes, de modo que el compromiso de una no comprometa el sistema entero
- b) La obligación de cifrar toda la información en tránsito por redes públicas
- c) La diferenciación entre el responsable de la seguridad y el responsable del sistema

**Respuesta correcta:** a) · **Referencia:** §1.1 [ENS]

El artículo 9 exige «múltiples capas de seguridad» de naturaleza <strong>organizativa, física y lógica</strong>. La opción B corresponde al art. 22 y a <code>mp.com.2</code>; la opción C, al art. 11.

### 4. Sobre los conceptos de amenaza, vulnerabilidad y riesgo, señale la afirmación correcta.

- a) La amenaza es una debilidad del propio sistema que se puede corregir aplicando parches
- b) El riesgo se elimina por completo si se implantan todas las medidas del anexo II del ENS
- c) Sobre la amenaza no se puede actuar: el riesgo solo se reduce actuando sobre la vulnerabilidad o sobre el impacto

**Respuesta correcta:** c) · **Referencia:** §1.2 [MAGERIT]

La amenaza existe con independencia de la organización. La debilidad propia es la <strong>vulnerabilidad</strong> (opción A, que invierte los términos), y siempre queda un <strong>riesgo residual</strong> que la dirección debe aceptar formalmente (opción B).

### 5. Según el informe ENISA Threat Landscape 2025, ¿cuál es el vector de acceso inicial dominante en los incidentes analizados?

- a) El phishing, con aproximadamente el 60 % de los accesos iniciales
- b) La explotación de vulnerabilidades, con aproximadamente el 60 %
- c) El acceso mediante credenciales robadas en la red oscura, con el 45 %

**Respuesta correcta:** a) · **Referencia:** §1.2 [ENISA-ETL]

Le sigue la <strong>explotación de vulnerabilidades con el 21,3 %</strong>. Entre las dos explican más de ocho de cada diez intrusiones, lo que justifica que las dos medidas más rentables sean la <strong>formación</strong> y el <strong>parcheado</strong>.

### 6. Sobre los ataques de denegación de servicio distribuida, el ETL 2025 concluye que:

- a) Son minoritarios en número pero provocan la mayor parte de las interrupciones de servicio
- b) Representan el 77 % de los incidentes notificados, pero solo el 2 % provocó una interrupción real del servicio
- c) Han desaparecido prácticamente como amenaza gracias a los servicios de mitigación en la nube

**Respuesta correcta:** b) · **Referencia:** §1.2 [ENISA-ETL]

Es el ataque <strong>más frecuente y menos dañino</strong>: la mayoría son acciones hacktivistas de bajo nivel. El ransomware, en cambio, es la amenaza de <strong>mayor impacto</strong> en la Unión Europea.

### 7. Un ataque pasivo se caracteriza porque:

- a) Solo escucha, no altera nada y por ello es muy difícil de detectar: se combate previniéndolo con cifrado
- b) Interrumpe el servicio y se detecta de inmediato por la caída de disponibilidad
- c) Inyecta información espuria en la comunicación para suplantar al origen legítimo

**Respuesta correcta:** a) · **Referencia:** §1.2 [ENS]

Las opciones B y C describen ataques <strong>activos</strong>. El propio ENS enumera como ataques activos, en <code>mp.com.3.2</code>, la alteración de la información en tránsito, la inyección de información espuria y el secuestro de la sesión.

### 8. El envenenamiento de la caché ARP es un ataque que actúa en la capa de enlace. ¿Cuál es la contramedida adecuada?

- a) Una regla de denegación en el cortafuegos perimetral que bloquee el tráfico ARP saliente
- b) Cifrar el tráfico con TLS extremo a extremo, que impide la asociación falsa de direcciones
- c) Inspección dinámica de ARP y seguridad de puerto en el conmutador, más 802.1X y segmentación

**Respuesta correcta:** c) · **Referencia:** §1.2 y §1.3.1 [ENS]

El cortafuegos perimetral <strong>no ve</strong> este tráfico, porque nunca sale del segmento (opción A). TLS protegería el contenido, pero no impediría el ataque ni sus efectos sobre el tráfico no cifrado (opción B). La regla general: <strong>un ataque de capa 2 no lo para un dispositivo de capa 3</strong>.

### 9. ¿Qué mecanismo proporciona cifrado e integridad salto a salto en la propia trama Ethernet?

- a) IPsec en modo transporte
- b) MACsec, normalizado como IEEE 802.1AE
- c) DTLS sobre UDP

**Respuesta correcta:** b) · **Referencia:** §1.3.1 [IEEE8021AE]

Protege el enlace entre dos equipos contiguos —entre conmutadores, o entre el puesto y el conmutador—. IPsec actúa en la capa de red y DTLS en la de transporte: ninguno de los dos protege la trama.

### 10. Sobre el estado de TLS en 2026, señale la afirmación correcta.

- a) TLS 1.0 y 1.1 están prohibidos por el RFC 8996, y la especificación vigente de TLS 1.3 es el RFC 9846, que obsoleta el RFC 8446
- b) TLS 1.1 sigue siendo admisible si se configura con suites de cifrado modernas
- c) El RFC 8446 continúa siendo la especificación vigente de TLS 1.3 y no ha sido sustituido

**Respuesta correcta:** a) · **Referencia:** §1.3.2 [RFC9846]

El RFC 9846, de <strong>julio de 2026</strong>, reedita TLS 1.3 y obsoleta también el RFC 5246 (TLS 1.2). SSL 3.0 quedó deprecado por el RFC 7568. Hoy solo son admisibles <strong>TLS 1.2 bien configurado y TLS 1.3</strong>.

### 11. ¿Cuál de estas afirmaciones sobre seguridad del DNS es correcta?

- a) DNSSEC cifra las consultas y por tanto aporta confidencialidad
- b) DoH y DoT firman las respuestas y garantizan la autenticidad de la zona
- c) DNSSEC firma las respuestas y aporta autenticidad e integridad, mientras que DoT y DoH cifran y aportan confidencialidad

**Respuesta correcta:** c) · **Referencia:** §1.3.2 [RFC9846]

Son mecanismos <strong>complementarios</strong>, no alternativos. Las opciones A y B intercambian exactamente las funciones de uno y otro.

### 12. En agosto de 2026, ¿cuál es la situación de la Directiva (UE) 2022/2555 (NIS2) en España?

- a) Está plenamente en vigor y es directamente aplicable a todas las entidades locales
- b) Sigue pendiente de transposición: el anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad continúa en tramitación y no se ha publicado en el BOE
- c) Fue transpuesta mediante el Real Decreto 311/2022, que aprueba el Esquema Nacional de Seguridad

**Respuesta correcta:** b) · **Referencia:** §1.4 [NIS2]

El anteproyecto se aprobó en Consejo de Ministros el <strong>14 de enero de 2025</strong>; España incumplió el plazo del 17 de octubre de 2024 y recibió dictamen motivado de la Comisión. La norma exigible hoy a las Administraciones sigue siendo el <strong>ENS</strong>, que es anterior a NIS2 y no la transpone.

### 13. ¿Qué exige literalmente la medida <code>mp.com.1</code> del ENS?

- a) Un sistema de protección perimetral que separe la red interna del exterior, por el que todo el tráfico debe pasar, con todos los flujos autorizados previamente
- b) El cifrado de todas las comunicaciones que discurran por redes fuera del dominio de seguridad propio
- c) La segregación del tráfico en, al menos, tres subredes: usuarios, servicios y administración

**Respuesta correcta:** a) · **Referencia:** §1.4 y §2.1 [ENS]

La opción B es <code>mp.com.2.1</code> y la opción C es el refuerzo <code>mp.com.4.r1.2</code>. <code>mp.com.1</code> <strong>aplica en las tres categorías</strong>, incluida la BÁSICA.

### 14. La medida <code>mp.com.4</code>, separación de flujos de información en la red, tiene una particularidad en su tabla de aplicación:

- a) Aplica en las tres categorías con el mismo contenido
- b) No aplica en categoría BÁSICA; en MEDIA exige <code>+ [R1 o R2 o R3]</code> y en ALTA <code>+ [R2 o R3] + R4</code>
- c) Solo aplica en categoría ALTA, y exige separación física de los medios

**Respuesta correcta:** b) · **Referencia:** §1.4 y §2.4.1 [ENS]

Obsérvese que en categoría <strong>ALTA la VLAN sola (R1) ya no basta</strong>: hay que llegar a VPN (R2) o separación física (R3), y añadir el control de los puntos de interconexión (R4).

### 15. La medida <code>mp.com.1</code> remite a una Instrucción Técnica de Seguridad de Interconexión de Sistemas de Información. ¿Cuál es su situación?

- a) Fue publicada en el BOE en 2018, junto con la ITS de Auditoría
- b) Fue publicada en 2016, junto con la ITS de Conformidad
- c) No está publicada: a agosto de 2026 solo hay cuatro ITS en el BOE — Conformidad e Informe del Estado de la Seguridad, de 2016, y Auditoría y Notificación de Incidentes, de 2018

**Respuesta correcta:** c) · **Referencia:** §1.4 [ITS]

Tampoco están publicadas la ITS de <strong>Criptología</strong> ni la de <strong>Adquisición de productos de seguridad</strong>, aunque el ENS también las anuncia. En su ausencia, la referencia práctica son las <strong>guías CCN-STIC</strong>.

### 16. ¿Qué artículo del ENS constituye la base legal específica de la seguridad perimetral?

- a) El artículo 20, mínimo privilegio
- b) El artículo 22, protección de información almacenada y en tránsito
- c) El artículo 23, prevención ante otros sistemas de información interconectados

**Respuesta correcta:** c) · **Referencia:** §1.4 [ENS]

Dispone que «se protegerá el <strong>perímetro</strong> del sistema de información, especialmente, si se conecta a redes públicas», y exige analizar los riesgos de la <strong>interconexión</strong> y controlar su <strong>punto de unión</strong>. No debe confundirse con <code>mp.com.1</code>, que es la <strong>medida</strong> del anexo II que lo desarrolla.

### 17. La política de denegación por defecto en un cortafuegos consiste en:

- a) Prohibir todo el tráfico y autorizar únicamente lo imprescindible, mediante una regla final que deniega y registra
- b) Permitir todo el tráfico y bloquear las amenazas conocidas mediante listas negras actualizadas
- c) Denegar el tráfico entrante y permitir sin restricciones todo el tráfico saliente

**Respuesta correcta:** a) · **Referencia:** §2.1 y §2.2.1 [ENS]

Es la traducción operativa de <code>mp.com.1.2</code>. La opción B describe la política contraria —lista negra—, que obliga a enumerar amenazas, que son infinitas, en lugar de necesidades, que son finitas. La opción C es el error más habitual en la vida real: permite que un equipo comprometido exfiltre por cualquier puerto.

### 18. ¿Cuál es la diferencia esencial entre un filtro de paquetes sin estado y un cortafuegos con estado?

- a) El filtro de paquetes actúa en capa 7 y el cortafuegos con estado en capas 3 y 4
- b) El cortafuegos con estado mantiene una tabla de conexiones, de modo que acepta el tráfico de vuelta sin necesidad de una regla explícita en sentido contrario
- c) El cortafuegos con estado identifica la aplicación y el usuario, mientras que el filtro de paquetes solo ve puertos

**Respuesta correcta:** b) · **Referencia:** §2.2.1 [CCN-408]

La opción C describe el <strong>NGFW</strong>. La consecuencia de seguridad de esa tabla: es un recurso finito, y agotarla es exactamente el objetivo de un <strong>SYN flood</strong>.

### 19. En el perímetro externo, ante un paquete no autorizado, ¿qué es preferible y por qué?

- a) Descartarlo silenciosamente, porque no responder no confirma al atacante que hay un sistema y ralentiza los escaneos
- b) Rechazarlo con un mensaje de error, porque es más rápido para el usuario legítimo y facilita el diagnóstico
- c) Es indiferente: ambas acciones producen exactamente el mismo efecto de seguridad

**Respuesta correcta:** a) · **Referencia:** §2.2.1 [CCN-408]

El <strong>rechazo</strong> con mensaje de error es más cortés y útil en redes internas, pero en el perímetro externo revela información. En ambos casos, la regla de cierre debe <strong>registrar</strong>, porque sin registro no hay trazabilidad (<code>op.exp.8</code>).

### 20. El cortafuegos de aplicaciones web (WAF):

- a) Sustituye al cortafuegos perimetral en las arquitecturas de nueva generación
- b) Es la denominación moderna del cortafuegos con estado
- c) Protege una aplicación web concreta frente a ataques como la inyección SQL o el XSS, y no sustituye al desarrollo seguro

**Respuesta correcta:** c) · **Referencia:** §2.2.1 [ENS]

Protege <strong>la aplicación</strong>, no la red, y es una mitigación, no una corrección. La medida del ENS que lo ampara es <strong><code>mp.s.2</code></strong>, que ya en categoría <strong>BÁSICA</strong> exige <code>+ [R1 o R2]</code>.

### 21. ¿Qué elemento se sitúa delante de los servidores publicados, termina el TLS, equilibra la carga y oculta la topología interna?

- a) Un proxy inverso
- b) Un proxy directo
- c) Un cortafuegos con estado en modo transparente

**Respuesta correcta:** a) · **Referencia:** §2.2.2 [ENS]

El <strong>proxy directo</strong> (opción B) hace lo contrario: se sitúa delante de los <strong>clientes internos</strong> que salen a internet y aplica <code>mp.s.3</code>. La medida del ENS asociada al proxy inverso es <code>mp.s.2</code>.

### 22. Sobre la inspección del tráfico cifrado en el proxy corporativo, el ENS establece que:

- a) Está prohibida en todo caso por afectar al secreto de las comunicaciones
- b) Puede realizarse libremente, sin más requisitos, siempre que el equipo sea corporativo
- c) El refuerzo <code>mp.s.3.r1.2</code>, exigible en categoría ALTA, la permite indicando qué se analiza, qué se registra, cuánto tiempo se retienen los registros y qué uso se prevé hacer de ellos

**Respuesta correcta:** c) · **Referencia:** §2.2.2 [ENS]

El propio refuerzo admite excepciones para «destinos de confianza». En cualquier caso hay que <strong>informar previamente</strong> y respetar los límites de protección de datos.

### 23. ¿Cuál es la diferencia fundamental entre un IDS y un IPS?

- a) El IDS detecta ataques conocidos por firmas y el IPS solo detecta anomalías de comportamiento
- b) El IDS se sitúa fuera de línea y solo alerta; el IPS se sitúa en línea y además bloquea
- c) El IDS protege una máquina concreta y el IPS protege un segmento de red completo

**Respuesta correcta:** b) · **Referencia:** §2.3 [ENS]

Los métodos de detección —firmas y anomalías— son independientes del tipo de dispositivo (opción A), y la distinción entre máquina y red corresponde a la pareja <strong>HIDS/NIDS</strong> (opción C).

### 24. ¿Cuál es la consecuencia más grave de un falso positivo en un IPS que protege una sede electrónica?

- a) Que se corta tráfico legítimo y ciudadanos no pueden completar sus trámites, con impacto en la disponibilidad
- b) Que se genera una alerta innecesaria que consume tiempo del equipo de análisis
- c) Que el ataque real pasa desapercibido al quedar oculto entre las alertas

**Respuesta correcta:** a) · **Referencia:** §2.3 [ENS]

Como el IPS está <strong>en línea</strong>, su falso positivo no es ruido, es un corte. La opción B describe la consecuencia en un <strong>IDS</strong>, y la opción C describe el efecto de la <strong>fatiga de alertas</strong>, que es real pero indirecto.

### 25. Sobre la detección por firmas y la detección por anomalías, señale la afirmación correcta.

- a) La detección por anomalías es más precisa y genera menos falsos positivos que la detección por firmas
- b) La detección por firmas es precisa pero no ve el ataque de día cero; la detección por anomalías puede verlo, a costa de más falsos positivos
- c) Ambas detectan igual de bien los ataques desconocidos, y la diferencia está solo en el rendimiento

**Respuesta correcta:** b) · **Referencia:** §2.3 [ENS]

La detección por anomalías necesita además un periodo de aprendizaje, y si aprende con la red ya comprometida, <strong>aprende que el ataque es normal</strong>.

### 26. La medida <code>op.mon.1</code>, detección de intrusión, del ENS:

- a) No aplica en categoría BÁSICA, y en MEDIA exige un IPS en línea
- b) Solo es exigible en categoría ALTA, con procedimientos de respuesta automática
- c) Aplica ya en categoría BÁSICA; en MEDIA añade el refuerzo R1, detección basada en reglas; y en ALTA el R2, procedimientos de respuesta a las alertas

**Respuesta correcta:** c) · **Referencia:** §2.3 [ENS]

La medida habla de «herramientas de detección <strong>o prevención</strong> de intrusiones», sin imponer cuál. Existe además un R3 de acciones automáticas de respuesta que la tabla <strong>no exige ni siquiera en ALTA</strong>.

### 27. ¿Qué medida del ENS constituye el fundamento de un SIEM?

- a) <code>op.exp.8</code>, registro de la actividad, en su redacción base
- b) <code>op.mon.3</code>, vigilancia, en su refuerzo R1, que exige un sistema automático de recolección de eventos que permita la correlación
- c) <code>op.mon.2</code>, sistema de métricas, en su refuerzo R2

**Respuesta correcta:** b) · **Referencia:** §2.3 [ENS]

La recolección automática sin correlación es la redacción base de <code>op.mon.3</code>, exigible en BÁSICA; la <strong>correlación</strong> —el SIEM— llega con el R1, exigible desde MEDIA. <code>op.exp.8</code> genera los registros, pero no los correlaciona.

### 28. La regla direccional que define una DMZ establece que:

- a) Desde la DMZ no se puede iniciar ninguna conexión hacia la red interna; desde la red interna sí se puede iniciar hacia la DMZ
- b) Desde la red interna no se puede iniciar ninguna conexión hacia la DMZ, para evitar la fuga de información
- c) La DMZ solo admite conexiones entrantes desde internet, y ninguna otra en ningún sentido

**Respuesta correcta:** a) · **Referencia:** §2.4.1 [ENS]

Si un servidor de la DMZ puede abrir sesiones contra la base de datos interna, <strong>eso no es una DMZ</strong>: es red interna con otro nombre. Cuando la DMZ necesita un dato de dentro, la conexión debe originarse en la red interna o resolverse con un elemento intermedio en la propia DMZ.

### 29. ¿Cuál es la ventaja principal de la arquitectura de doble cortafuegos frente a la de tres patas?

- a) Reduce el coste y simplifica la gestión al concentrar una única política
- b) Permite prescindir de la DMZ, porque los dos cortafuegos ya la sustituyen
- c) Aporta defensa en profundidad real, sobre todo si los dos equipos son de fabricantes distintos, de modo que una vulnerabilidad del primero no afecta al segundo

**Respuesta correcta:** c) · **Referencia:** §2.4.1 [ENS]

La opción A describe la ventaja de la arquitectura <strong>de tres patas</strong>, cuyo inconveniente es que un solo dispositivo separa internet de la red interna.

### 30. ¿Qué segmentación mínima exige el refuerzo <code>mp.com.4.r1.2</code> del ENS?

- a) Dos subredes: interna y DMZ
- b) Al menos tres subredes: usuarios, servicios y administración
- c) Una subred por cada unidad organizativa del organismo

**Respuesta correcta:** b) · **Referencia:** §2.4.1 [ENS]

Y <code>mp.com.4.2</code> añade una obligación independiente: si se emplean <strong>comunicaciones inalámbricas</strong>, será <strong>en un segmento separado</strong>. Ambas son texto literal del anexo II.

### 31. Según la publicación NIST SP 800-207, uno de los siete principios de la confianza cero establece que:

- a) La red interna se considera de confianza siempre que esté segmentada mediante VLAN
- b) El acceso se concede de forma permanente una vez validada la identidad del usuario
- c) El acceso a los recursos se concede por sesión y se determina mediante política dinámica, que valora identidad, aplicación, estado del dispositivo y contexto

**Respuesta correcta:** c) · **Referencia:** §2.4.2 [NIST-ZT]

Las opciones A y B contradicen frontalmente el modelo: desaparece la confianza implícita por ubicación y <strong>no existe la sesión indefinidamente confiable</strong>.

### 32. En una arquitectura de confianza cero, ¿qué componente está en el camino del tráfico y deja pasar o no?

- a) El Punto de Aplicación de Políticas (PEP)
- b) El Motor de Políticas (PE)
- c) El Administrador de Políticas (PA)

**Respuesta correcta:** a) · **Referencia:** §2.4.2 [NIST-ZT]

El <strong>Motor (PE)</strong> decide y el <strong>Administrador (PA)</strong> ejecuta la decisión; ambos forman el <strong>punto de decisión (PDP)</strong>, que no está en el camino del tráfico. Esa separación entre quien decide y quien ejecuta es lo que permite que la decisión sea dinámica.

### 33. Señale la afirmación correcta sobre la relación entre confianza cero y el modelo perimetral en España.

- a) La confianza cero deroga la obligación de disponer de perímetro, por ser un modelo superado
- b) La confianza cero complementa al modelo perimetral, que sigue siendo obligatorio por <code>mp.com.1</code> en las tres categorías
- c) Ambos modelos son incompatibles, y el ENS obliga a elegir uno de los dos en la política de seguridad

**Respuesta correcta:** b) · **Referencia:** §2.4.2 [NIST-ZT]

Lo que la confianza cero sustituye es la idea de <strong>red interna de confianza</strong>, no el perímetro. Además, <code>op.acc.4</code> y <code>mp.com.4</code> son, leídos hoy, principios de confianza cero escritos en 2022.

### 34. ¿Qué requisito del ENS hay que citar necesariamente en una pregunta sobre acceso remoto?

- a) <code>mp.com.1.1</code>, que obliga a que todo el tráfico atraviese el sistema de protección perimetral
- b) <code>op.exp.8</code>, que obliga a registrar la actividad de los usuarios
- c) <code>op.acc.4.5</code>, que obliga a establecer una política específica de acceso remoto requiriendo autorización expresa

**Respuesta correcta:** c) · **Referencia:** §3.1 [ENS]

Está dentro de <code>op.acc.4</code>, que <strong>aplica en las tres categorías</strong>. Las otras dos medidas son también aplicables, pero no son específicas de acceso remoto.

### 35. ¿Qué establece <code>mp.eq.3.3</code> del ENS respecto a un portátil que se conecta desde una red no controlada por la organización?

- a) Que el ámbito de operación del servidor limitará la información y los servicios accesibles a los mínimos imprescindibles, con autorización previa de los responsables
- b) Que el portátil deberá llevar necesariamente el disco cifrado, con independencia del nivel de confidencialidad
- c) Que solo se permitirá la conexión desde redes previamente registradas por su dirección IP pública

**Respuesta correcta:** a) · **Referencia:** §3.1 [ENS]

Es decir: <strong>el teletrabajador no debe ver la misma red que si estuviera en la oficina</strong>. La opción B corresponde al refuerzo <code>mp.eq.3.r1</code>, que se activa cuando la confidencialidad es de nivel MEDIO.

### 36. ¿Cuál es la base legal del teletrabajo en las Administraciones Públicas españolas?

- a) El Real Decreto 311/2022, que aprueba el Esquema Nacional de Seguridad
- b) El artículo 14 de la Ley 39/2015, sobre el derecho a relacionarse electrónicamente
- c) El artículo 47 bis del TREBEP, introducido por el Real Decreto-ley 29/2020, de 29 de septiembre

**Respuesta correcta:** c) · **Referencia:** §3.1 [TREBEP]

Configura el teletrabajo como <strong>expresamente autorizado</strong>, <strong>voluntario y reversible</strong> y compatible con la modalidad presencial, y obliga a la Administración a <strong>proporcionar los medios tecnológicos</strong> necesarios — que es el fundamento de que el equipo sea corporativo y gestionado.

### 37. En una autenticación 802.1X, ¿qué papel desempeña el conmutador de red?

- a) El de suplicante, porque solicita la autenticación en nombre del equipo conectado
- b) El de autenticador: no decide nada, transporta el diálogo EAP y aplica el resultado
- c) El de servidor de autenticación, porque valida las credenciales contra el directorio

**Respuesta correcta:** b) · **Referencia:** §3.2.2 [RFC3748]

El <strong>suplicante</strong> es el software del equipo que se conecta, y el <strong>servidor de autenticación</strong> —normalmente RADIUS— es quien decide. Hasta que la autenticación tiene éxito, el puerto solo deja pasar <strong>EAPOL</strong>: ni siquiera se obtiene dirección IP.

### 38. ¿Cuál de estas combinaciones constituye autenticación multifactor en sentido estricto?

- a) Certificado en tarjeta criptográfica más el PIN que la desbloquea
- b) Contraseña de acceso al sistema más PIN de acceso a la aplicación
- c) Contraseña más respuesta a una pregunta de seguridad

**Respuesta correcta:** a) · **Referencia:** §3.2.1 [ENS]

Combina «algo que se tiene» con «algo que se sabe». Las opciones B y C combinan <strong>dos factores de la misma categoría</strong> —ambos «algo que se sabe»—, y por tanto <strong>no son MFA</strong>.

### 39. Un organismo categorizado MEDIA autoriza el teletrabajo con VPN cifrada y contraseña robusta de doce caracteres. ¿Cumple <code>op.acc.5</code>?

- a) Sí, porque la longitud y la complejidad de la contraseña compensan la ausencia de segundo factor
- b) No: en nivel MEDIO la tabla exige <code>+ [R2 o R3 o R4] + R5</code>, de modo que la contraseña sola (R1) deja de estar disponible y es obligatorio registrar accesos con éxito y fallidos
- c) Sí, siempre que la contraseña se cambie cada noventa días y se registren los accesos correctos

**Respuesta correcta:** b) · **Referencia:** §3.2.1 [ENS]

El matiz: <strong>la longitud de la contraseña es irrelevante para la conformidad</strong>; lo que la norma exige es un <strong>segundo factor</strong>. En nivel BAJO sí bastaría <code>+ [R1 o R2 o R3 o R4]</code>.

### 40. Señale la afirmación correcta sobre los protocolos de gestión remota.

- a) Telnet puede utilizarse siempre que la conexión se limite a la red interna, porque el tráfico no sale del perímetro
- b) SFTP y FTPS son dos nombres del mismo protocolo, y ambos emplean el puerto 990
- c) SSH sustituye a Telnet y a rlogin en el puerto TCP 22, y sobre él viajan SFTP y SCP; SNMPv1 y v2c no ofrecen seguridad real y solo SNMPv3 autentica y cifra

**Respuesta correcta:** c) · **Referencia:** §3.3 [RFC4251]

Telnet transmite las credenciales <strong>en claro</strong> y no se usa jamás, tampoco en la red interna (opción A). <strong>SFTP</strong> es un subsistema de SSH y <strong>FTPS</strong> es FTP envuelto en TLS: no son lo mismo (opción B). Y las interfaces de gestión fuera de banda deben vivir en una <strong>red de administración separada</strong>, que es una de las tres subredes mínimas de <code>mp.com.4.r1.2</code>.

### 41. Señale tres diferencias correctas entre RADIUS y TACACS+.

- a) RADIUS usa UDP 1812 y 1813, cifra solo la contraseña y junta autenticación y autorización; TACACS+ usa TCP 49, cifra todo el cuerpo del mensaje y separa las tres funciones
- b) RADIUS usa TCP 49 y cifra todo el mensaje; TACACS+ usa UDP y solo cifra la contraseña
- c) Ambos usan UDP, pero RADIUS separa las tres funciones y TACACS+ las combina

**Respuesta correcta:** a) · **Referencia:** §3.2.2 [RFC2865]

De ahí el reparto práctico: <strong>RADIUS</strong> para el acceso de usuarios a la red (Wi-Fi, 802.1X, VPN) y <strong>TACACS+</strong> para la administración de equipos de red, donde interesa autorizar comando a comando. Dos novedades recientes: el <strong>RFC 9887</strong> (diciembre de 2025) lleva TACACS+ sobre <strong>TLS 1.3</strong>, y el <strong>RFC 9765</strong> (abril de 2025) define <strong>RADIUS/1.1</strong>, que elimina MD5 mediante ALPN.

### 42. En un entorno sujeto al ENS, ¿qué configuración de túnel es la correcta por defecto en una VPN de acceso remoto y por qué?

- a) Túnel dividido, porque mejora el rendimiento y descarga el enlace de la sede central
- b) Túnel completo, porque hace que toda la navegación pase por la organización y quede sujeta a <code>mp.s.3</code>, y evita que el equipo quede con un pie en cada red
- c) Es indiferente, porque en ambos casos el tráfico corporativo viaja cifrado

**Respuesta correcta:** b) · **Referencia:** §4.1.2 [ENS]

El <strong>túnel dividido</strong> es una excepción que hay que justificar y acotar. Además de romper el control de la navegación, compromete el art. 9 al convertir el equipo en puente potencial entre dos redes.

### 43. ¿Qué convierte un túnel en una red privada virtual?

- a) La encapsulación: cualquier protocolo que meta un paquete dentro de otro crea ya una VPN
- b) El uso de direccionamiento privado conforme al RFC 1918 en ambos extremos del túnel
- c) El cifrado: GRE encapsula pero no cifra, y MPLS aísla el tráfico entre clientes del operador pero tampoco lo cifra

**Respuesta correcta:** c) · **Referencia:** §4.1 [RFC2784]

La MPLS del operador ofrece privacidad <strong>administrativa</strong>, no criptográfica, y por sí sola <strong>no cumple <code>mp.com.2.1</code></strong>, que exige redes privadas virtuales <strong>cifradas</strong> cuando el tráfico sale del dominio de seguridad propio. La solución conforme es cifrar por encima con IPsec.

### 44. ¿Qué diferencia el modo túnel del modo transporte de IPsec?

- a) El modo transporte cifra el paquete IP completo y el modo túnel solo la carga útil
- b) El modo transporte conserva la cabecera IP original y protege solo la carga; el modo túnel cifra el paquete IP completo y añade una cabecera IP nueva, ocultando el direccionamiento interno
- c) El modo túnel solo se puede usar con AH, y el modo transporte solo con ESP

**Respuesta correcta:** b) · **Referencia:** §4.2.1 [RFC4301]

Regla: <strong>VPN de sitio a sitio implica ESP en modo túnel</strong>. En ese modo, un observador en internet solo ve las direcciones de las dos <strong>pasarelas</strong>, no las de los equipos internos.

### 45. Sobre AH y ESP, los dos protocolos de seguridad de IPsec, señale la afirmación correcta.

- a) AH proporciona integridad y autenticación del origen pero NO cifra, y usa el protocolo IP 51; ESP cifra y además autentica, y usa el protocolo IP 50
- b) AH cifra la carga útil y ESP solo comprueba la integridad; AH usa el protocolo IP 50 y ESP el 51
- c) Ambos cifran, y la diferencia está en que AH trabaja en modo túnel y ESP en modo transporte

**Respuesta correcta:** a) · **Referencia:** §4.2.1 [RFC4303]

Como ESP hace casi todo lo que hace AH, en la práctica <strong>se usa ESP y AH está en desuso</strong>. Son <strong>números de protocolo IP</strong>, no puertos: AH y ESP van directamente sobre IP y no tienen puertos, y eso es lo que les da problemas con NAT.

### 46. Sobre las asociaciones de seguridad (SA) de IPsec, señale la afirmación correcta.

- a) Una SA es bidireccional y basta con una por cada conexión establecida
- b) Una SA se identifica únicamente por el SPI, que es un valor globalmente único
- c) Una SA es unidireccional, de modo que una comunicación bidireccional requiere dos, y se identifica por el trío SPI, dirección IP de destino y protocolo de seguridad

**Respuesta correcta:** c) · **Referencia:** §4.2.1 [RFC4301]

Las SA vivas se guardan en la <strong>SAD</strong>, y la política que decide qué tráfico se protege, en la <strong>SPD</strong>, cuyas tres acciones posibles son descartar, omitir IPsec o aplicar IPsec.

### 47. Un túnel IPsec se negocia correctamente pero no cursa tráfico. El extremo remoto está detrás de un dispositivo que hace NAT y el cortafuegos solo permite UDP 500. ¿Cuál es la causa más probable?

- a) Que falta abrir UDP 4500: con NAT en medio, IKEv2 conmuta a la travesía de NAT y encapsula ESP en UDP 4500 conforme al RFC 3948
- b) Que el modo túnel no es compatible con la traducción de direcciones y hay que cambiar a modo transporte
- c) Que el tiempo de vida de la asociación de seguridad es demasiado corto y expira antes de cursar datos

**Respuesta correcta:** a) · **Referencia:** §4.2.1 [RFC3948]

Es exactamente el síntoma descrito: la negociación inicial funciona por el 500 —el túnel «se levanta»— pero los datos no pasan. Si además se estuviera usando <strong>AH</strong>, habría un segundo problema: AH es <strong>incompatible con NAT</strong> porque autentica campos de la cabecera IP.

### 48. ¿Cuál es la razón principal del éxito de las VPN basadas en SSL/TLS en escenarios de movilidad?

- a) Que ofrecen mejor rendimiento bruto por encapsular TCP dentro de TCP
- b) Que no requieren autenticar al usuario, lo que simplifica el despliegue
- c) Que usan TCP 443, indistinguible del tráfico HTTPS ordinario, y por tanto atraviesan cortafuegos ajenos que bloquean IPsec

**Respuesta correcta:** c) · **Referencia:** §4.2.2 [RFC9846]

Su contrapartida es precisamente el <strong>rendimiento</strong>: encapsular TCP dentro de TCP provoca el llamado derretimiento de TCP, con dos controles de congestión superpuestos. Por eso los productos modernos prefieren transportar el túnel sobre DTLS o QUIC y dejar el 443 como respaldo.

### 49. ¿Cuál es la situación normativa de IKEv1 e IKEv2?

- a) IKEv1 sigue siendo la versión recomendada por su mayor compatibilidad entre fabricantes
- b) IKEv1 fue declarado obsoleto por el RFC 9395, de abril de 2023; IKEv2 es la versión vigente y tiene la categoría de Internet Standard (STD 79)
- c) Ambas versiones están obsoletas y han sido sustituidas por el protocolo IKEv3

**Respuesta correcta:** b) · **Referencia:** §4.2.1 [RFC7296]

Ventajas de IKEv2: menos mensajes para establecer el túnel, detección de par muerto integrada, soporte nativo de <strong>EAP</strong> —y por tanto de MFA—, travesía de NAT normalizada y <strong>MOBIKE</strong>, que permite cambiar de red sin que se caiga el túnel.

### 50. Sobre los protocolos de tunelización de nivel de enlace, señale la afirmación correcta.

- a) L2TP no cifra por sí solo, y por eso se despliega como L2TP/IPsec, con IPsec en modo transporte; PPTP está criptográficamente roto y no debe usarse
- b) L2TP incorpora cifrado propio equivalente a ESP y puede usarse de forma autónoma
- c) PPTP es la opción recomendada por su integración nativa en los sistemas operativos de escritorio

**Respuesta correcta:** a) · **Referencia:** §4.2.3 [RFC2661]

L2TP usa <strong>UDP 1701</strong>. En la combinación L2TP/IPsec, IPsec trabaja en <strong>modo transporte</strong> porque el túnel ya lo aporta L2TP. PPTP se descifra en horas: su autenticación MS-CHAPv2 y su cifrado MPPE están rotos.

### 51. ¿Qué es la amenaza de «cosecha ahora, descifra después» y por qué afecta especialmente a las VPN?

- a) Es la captura de credenciales en redes públicas para reutilizarlas más adelante, y afecta a las VPN porque muchas siguen usando contraseña
- b) Es el almacenamiento de copias de seguridad sin cifrar por parte del proveedor de nube, y se combate exigiendo productos del CPSTIC
- c) Es la grabación hoy del tráfico cifrado para descifrarlo cuando existan ordenadores cuánticos, y afecta a las VPN porque protegen información de vida útil larga

**Respuesta correcta:** c) · **Referencia:** §4.2.1 [PQC-EU]

Respuestas normalizadas: en IKEv2, los <strong>RFC 8784 y 9370</strong>; en TLS 1.3, el <strong>RFC 10024</strong>, de agosto de 2026. Calendario de la <strong>hoja de ruta coordinada de la UE</strong> (Grupo de Cooperación NIS, 23-6-2025): <strong>31-12-2026</strong> planes nacionales, <strong>31-12-2030</strong> casos de alto riesgo y <strong>31-12-2035</strong> transición completa.

### 52. ¿Qué exige literalmente la medida <code>op.exp.6</code> del ENS respecto al software de protección frente a código dañino?

- a) Que se instale exclusivamente en los puestos de usuario, por ser el punto de entrada habitual
- b) Que se instale en todos los equipos: puestos de usuario, servidores y elementos perimetrales, con las bases de detección permanentemente actualizadas y protección en tiempo real
- c) Que se instale en los servidores y en el perímetro, quedando los puestos cubiertos por el cortafuegos personal

**Respuesta correcta:** b) · **Referencia:** §5.2.1 [ENS]

Es texto literal de <code>op.exp.6.2</code>, <code>op.exp.6.4</code> y <code>op.exp.6.5</code>. Añade además <code>op.exp.6.3</code>: <strong>todo fichero procedente de fuentes externas será analizado antes de trabajar con él</strong>.

### 53. ¿Cuál es la diferencia esencial entre una plataforma de protección del punto final (EPP) y una solución de detección y respuesta (EDR)?

- a) El EPP previene bloqueando lo que reconoce como malo; el EDR asume que algo entrará y aporta telemetría de comportamiento para investigar, además de permitir aislar el equipo en red desde la consola
- b) El EPP actúa en el servidor y el EDR en el puesto de usuario
- c) El EPP usa detección por anomalías y el EDR se limita a las firmas del fabricante

**Respuesta correcta:** a) · **Referencia:** §5.2.1 [ENS]

El <strong>aislamiento remoto</strong> —dejar el equipo sin comunicación salvo con la consola— es la capacidad más característica del EDR y la que un antivirus no puede ofrecer. El <strong>XDR</strong> amplía la correlación a red, correo, identidad y nube; el <strong>MDR</strong> es el mismo servicio operado por un tercero.

### 54. En categoría ALTA, ¿qué añade la tabla de aplicación de <code>op.exp.6</code> respecto a la categoría MEDIA?

- a) Nada: la medida se aplica igual en MEDIA y en ALTA
- b) Los refuerzos R3 y R4: lista blanca de aplicaciones —solo se ejecuta lo previamente autorizado— y herramientas EDR, que el ENS nombra expresamente por su sigla
- c) Únicamente el refuerzo R1, escaneo periódico de todo el sistema

**Respuesta correcta:** b) · **Referencia:** §5.2.1 [ENS]

La tabla completa es: <strong>BÁSICA</strong> la medida; <strong>MEDIA</strong> <code>+ R1 + R2</code> (escaneo periódico y revisión de funciones críticas al arranque); <strong>ALTA</strong> <code>+ R1 + R2 + R3 + R4</code>. Es uno de los pocos lugares donde el ENS cita una tecnología concreta con su nombre comercial habitual.

### 55. Sobre el cifrado de disco completo del portátil corporativo, señale la afirmación correcta.

- a) Impide que el ransomware cifre los ficheros, porque estos ya están cifrados por el sistema
- b) Solo es exigible en categoría ALTA y en ningún otro caso
- c) Protege exclusivamente frente al acceso físico al equipo apagado; con la sesión iniciada el disco está descifrado para el sistema y también para cualquier proceso malicioso

**Respuesta correcta:** c) · **Referencia:** §5.2.2 [ENS]

La medida que lo exige es <strong><code>mp.eq.3.r1</code></strong>, cuando el nivel de <strong>confidencialidad</strong> de la información almacenada es <strong>MEDIO</strong> (opción B, incorrecta). Y hay que custodiar centralmente las <strong>claves de recuperación</strong>, o una medida de confidencialidad acaba dañando la disponibilidad.

### 56. ¿Cuál de estas medidas de protección del puesto NO es exigible en un sistema cuyo nivel de autenticidad es BAJO?

- a) <code>mp.eq.2</code>, bloqueo del puesto de trabajo, que no aplica en nivel BAJO y empieza a exigirse en MEDIO
- b) <code>mp.eq.1</code>, puesto de trabajo despejado, que solo se exige desde categoría MEDIA
- c) <code>mp.eq.3</code>, protección de dispositivos portátiles, que solo se exige en categoría ALTA

**Respuesta correcta:** a) · **Referencia:** §5.1 [ENS]

En nivel ALTO añade el refuerzo <strong>R1</strong>, que obliga a <strong>cancelar las sesiones abiertas</strong> pasado un tiempo mayor. <code>mp.eq.1</code> y <code>mp.eq.3</code> sí aplican desde categoría <strong>BÁSICA</strong>, por lo que las opciones B y C son falsas.

### 57. ¿Qué obligaciones establece <code>mp.eq.3</code>, protección de dispositivos portátiles?

- a) Únicamente el cifrado del disco duro y el bloqueo automático por inactividad
- b) Inventario de portátiles con persona responsable y control regular, procedimiento para informar de pérdidas o sustracciones, limitación a los mínimos imprescindibles desde redes no controladas y evitar que el equipo contenga claves de acceso remoto no imprescindibles
- c) La prohibición de sacar equipos de las instalaciones sin autorización del responsable de seguridad

**Respuesta correcta:** b) · **Referencia:** §5.1 [ENS]

Son los cuatro requisitos base, <code>mp.eq.3.1</code> a <code>mp.eq.3.4</code>. Los refuerzos, exigibles en categoría <strong>ALTA</strong>, son <strong>R1</strong> (cifrado del disco) y <strong>R2</strong> (entornos protegidos, «a salvo de hurtos y miradas indiscretas»).

### 58. Un organismo mantiene en producción puestos con un sistema operativo cuyo soporte terminó el 14 de octubre de 2025. ¿Cómo se valora?

- a) Es aceptable si el antivirus está actualizado, porque compensa la ausencia de parches
- b) Es aceptable si los equipos están segmentados en una VLAN propia sin salida a internet
- c) Es un incumplimiento directo de <code>op.exp.4</code>: un sistema fuera de soporte no recibe parches y ninguna otra medida lo compensa; el programa de pago ESU solo prolonga las actualizaciones críticas e importantes hasta el 12 de octubre de 2027

**Respuesta correcta:** c) · **Referencia:** §5.3 [ENS]

El antivirus no tapa una vulnerabilidad del núcleo (opción A) y la segmentación reduce el impacto pero no la vulnerabilidad (opción B). Es un hallazgo sistemático en las auditorías del ENS, en relación también con el <strong>art. 21</strong>.

### 59. ¿Cuál es la justificación técnica del cortafuegos personal en un puesto que ya está detrás de un cortafuegos perimetral?

- a) Que el cortafuegos perimetral no ve el tráfico entre dos puestos de la misma VLAN, de modo que el personal es la única defensa frente al movimiento lateral y la única existente cuando el portátil está fuera de la organización
- b) Que duplica las reglas del perimetral y así se dispone de una copia de seguridad de la política
- c) Que sustituye al antimalware en los equipos que no pueden ejecutar un agente EDR

**Respuesta correcta:** a) · **Referencia:** §5.2.2 [ENS]

Es por tanto una <strong>capa independiente</strong> en el sentido del art. 9 del ENS, no una redundancia. Además permite reglas <strong>por aplicación</strong> y perfiles distintos para «en la oficina» y «fuera».

### 60. ¿Qué obliga a recordar periódicamente la medida <code>mp.per.3</code>, concienciación, del ENS?

- a) Únicamente la política de contraseñas y el procedimiento de bloqueo del puesto, y solo en categoría ALTA
- b) La normativa de buen uso de los equipos y las técnicas de ingeniería social más habituales, la identificación de incidentes o comportamientos sospechosos, y el procedimiento para informar sobre incidentes de seguridad, sean reales o falsas alarmas
- c) El contenido íntegro del anexo II del ENS, mediante una acción formativa anual obligatoria

**Respuesta correcta:** b) · **Referencia:** §5.4 [ENS]

Son los tres apartados literales de <code>mp.per.3</code>, y la medida <strong>aplica en las tres categorías</strong>, incluida la BÁSICA. El inciso <strong>«sean reales o falsas alarmas»</strong> es el más importante: si notificar conlleva reproche, el empleado deja de notificar y se pierde el sensor más rápido de la organización. <code>mp.per.4</code> añade la <strong>formación</strong> y exige <strong>evaluar su eficacia</strong>.

## Preguntas sobre los casos prácticos

### Caso 1. Rediseño del perímetro y la red de una oficina de distrito

#### 1. En la oficina del supuesto, los puestos de tramitación comparten VLAN con un punto de acceso Wi-Fi abierto al público. ¿Por qué es este el riesgo más inmediato?

- a) Porque cualquier ciudadano de la sala de espera queda en la misma red que los puestos y puede envenenar ARP o hacerse intermediario.
- b) Porque el Wi-Fi abierto consume el ancho de banda del enlace y deja sin capacidad a los puestos de tramitación de la oficina.
- c) Porque el punto de acceso impide aplicar autenticación 802.1X en las rosetas cableadas de la zona de tramitación.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.4.1

Compartir dominio de difusión con el público permite escanear la red, envenenar ARP y colocarse como intermediario del tráfico de los puestos, que tratan datos personales.

#### 2. ¿Qué exige el ENS respecto al Wi-Fi público de la oficina y con qué carácter?

- a) mp.com.4.r1.2 lo plantea como refuerzo opcional, que solo resulta exigible cuando el sistema es de categoría ALTA.
- b) mp.com.4.2 obliga, como requisito base y no como refuerzo, a llevar la comunicación inalámbrica a un segmento separado.
- c) mp.com.1.1 obliga a cifrar el Wi-Fi, pero permite mantenerlo en el mismo segmento que los puestos de tramitación.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §1.3.1 · mp.com.4.2 ENS

«Si se emplean comunicaciones inalámbricas, será en un segmento separado» (mp.com.4.2): es una obligación literal de la medida, no un refuerzo. El Wi-Fi público sale a una VLAN propia sin ruta hacia la red municipal.

#### 3. ¿Qué propuesta de segmentación cumple la segregación mínima que exige mp.com.4.r1.2 en esta oficina?

- a) Una VLAN para los puestos y otra única para el resto, que agrupe Wi-Fi público, cámaras y administración de red.
- b) Una VLAN por cada puesto de tramitador, manteniendo la administración de los equipos de red en la VLAN de cámaras.
- c) VLAN de puestos, de dispositivos (impresoras, turnos y cámaras), de administración de los equipos de red y de invitados.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.4.1 · mp.com.4.r1.2 ENS

El refuerzo mp.com.4.r1.2 exige segregar como mínimo en usuarios, servicios y administración; además, el Wi-Fi público debe ir en su propio segmento.

#### 4. El sistema está categorizado MEDIA. ¿Qué exige la tabla de aplicación de mp.com.4 en esa categoría?

- a) + [R2 o R3] + R4, de modo que la separación mediante VLAN deja de ser suficiente.
- b) + [R1 o R2 o R3], de modo que basta con separar los segmentos mediante VLAN (R1).
- c) Nada, porque mp.com.4 solo empieza a aplicarse cuando el sistema es de categoría ALTA.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §1.4 · mp.com.4 ENS

mp.com.4 no aplica en BÁSICA y en MEDIA exige + [R1 o R2 o R3]: la VLAN (R1) basta. En ALTA el R1 deja de ser suficiente.

#### 5. La Junta conectó un encaminador 4G de respaldo a un puerto del conmutador «por si se cae la línea principal». ¿Qué medida del ENS vulnera directamente?

- a) mp.com.1.1, porque todo el tráfico debe atravesar el perímetro y el 4G abre una salida que no pasa por él.
- b) mp.s.4, porque un enlace 4G no garantiza la disponibilidad de la oficina frente a ataques volumétricos.
- c) op.exp.10, porque el encaminador 4G no custodia las claves criptográficas del túnel con el CPD central.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §2.1 · mp.com.1.1 ENS

mp.com.1.1 exige que «todo el tráfico deberá atravesar» el sistema de protección perimetral: si existe un camino que no pasa por el perímetro, el perímetro no existe. Además vulnera los arts. 21 y 23 del ENS.

#### 6. ¿Qué debe proponer el informe sobre ese encaminador 4G?

- a) Retirarlo sin sustituirlo, porque el ENS no admite que una oficina disponga de un enlace de respaldo con el CPD.
- b) Mantenerlo en el conmutador de la oficina, limitándose a inscribirlo en el inventario de activos de la Junta.
- c) Integrarlo: que termine en el mismo equipo perimetral, con la misma política, conmutación automática y el túnel cifrado.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.1

La redundancia es legítima y deseable por disponibilidad; lo que falla es que eluda el perímetro. Debe terminar en el mismo equipo perimetral, con la misma política y con el túnel cifrado levantándose también sobre él.

#### 7. ¿Cómo debe corregirse la regla del cortafuegos del CPD que permite todo desde 10.30.7.0/24 hacia la red de servidores?

- a) Con reglas explícitas desde la VLAN de puestos a servidores y puertos concretos, y una regla final que deniega y registra.
- b) Manteniéndola, pero limitándola al horario de apertura al público de la Oficina de Atención a la Ciudadanía.
- c) Sustituyéndola por otra que permita todo desde la oficina hacia los servidores, salvo el tráfico de las cámaras.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 2 · §2.1 · mp.com.1.2 ENS

mp.com.1.2 exige que todos los flujos estén autorizados previamente; con la denegación por defecto y el mínimo privilegio (art. 20 ENS), solo se permite lo imprescindible: origen, destino y puertos concretos, y regla final de denegar y registrar.

#### 8. El pliego del operador asegura que en la «VPN MPLS» «el tráfico viaja aislado del de otros clientes». ¿Cumple ese enlace la medida mp.com.2 del ENS?

- a) Sí: el aislamiento entre clientes que garantiza el pliego es lo que exige mp.com.2.1 para salir del dominio propio.
- b) Sí, siempre que el operador figure en el catálogo CPSTIC del CCN como prestador de servicios de comunicaciones.
- c) No: MPLS aísla el tráfico entre clientes pero no lo cifra, y la red del operador es un dominio de seguridad ajeno.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 3 · §4.2.3 · mp.com.2.1 ENS

mp.com.2.1 exige «redes privadas virtuales cifradas cuando la comunicación discurra por redes fuera del propio dominio de seguridad». MPLS da privacidad administrativa, no criptográfica.

#### 9. ¿Qué solución conforme procede sobre el enlace MPLS de la oficina?

- a) Un túnel GRE entre las pasarelas de la oficina y del CPD, que encapsula el tráfico y basta para cumplir mp.com.2.1.
- b) Un túnel IPsec en modo túnel con ESP entre pasarelas, autenticado por certificados y con algoritmos autorizados por el CCN.
- c) Un túnel IPsec con AH en modo transporte entre pasarelas, autenticado mediante una clave precompartida.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 3 · §4.2.1 · mp.com.2 ENS

Hay que cifrar por encima del MPLS. ESP cifra (AH no) y GRE solo encapsula. En categoría MEDIA aplica mp.com.2 + R1: algoritmos y parámetros autorizados por el CCN (CCN-STIC-807). Se autentica por certificados, no por clave precompartida.

#### 10. ¿Dónde y con qué reglas debe publicarse el nuevo servicio de cita previa?

- a) En una DMZ, con acceso desde internet solo por TCP 443 y sin que la DMZ pueda iniciar conexiones hacia la red interna.
- b) En la red de servidores del CPD, abriendo el TCP 443 desde internet y restringiendo las conexiones salientes del servidor.
- c) En una DMZ, desde la que el servidor consulte directamente el calendario de la red interna cuando lo necesite.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §2.4.1

Al ser alcanzable desde internet, el servicio debe estar en una DMZ: internet → DMZ solo por 443, y desde la DMZ no puede iniciarse ninguna conexión hacia la red interna. Si necesita el calendario, la conexión se origina en la red interna o en un servicio intermedio de la DMZ.

### Caso 2. Acceso remoto y VPN para 900 empleados en teletrabajo

#### 1. La mesa técnica sostiene que una contraseña de 12 caracteres con caducidad de 90 días es suficiente para la VPN, siendo la confidencialidad de nivel MEDIO. ¿Qué debe responderse?

- a) Que sí: en nivel MEDIO op.acc.5 se cumple con una contraseña de al menos 12 caracteres y caducidad periódica.
- b) Que no: en nivel MEDIO la contraseña sola (R1) deja de estar disponible, por robusta que sea; falta un segundo factor.
- c) Que no: en nivel MEDIO la contraseña debe tener 16 caracteres y caducar cada 60 días para cumplir op.acc.5.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §3.2.1 · op.acc.5 ENS

Con nivel MEDIO, op.acc.5 exige + [R2 o R3 o R4] + R5: la opción de contraseña sola desaparece. La longitud y la caducidad son irrelevantes para la conformidad.

#### 2. ¿Cuál es el mínimo que debe añadirse a la autenticación de la VPN para cumplir op.acc.5 en nivel MEDIO?

- a) Solo el refuerzo R5: registrar los accesos con éxito y fallidos e informar al usuario de cuándo fue su último acceso.
- b) Solo el refuerzo R2, la contraseña de un solo uso por SMS, sin necesidad de registrar los accesos con éxito y fallidos.
- c) Un factor R2 (contraseña de un solo uso) o R3/R4 (certificado cualificado con segundo factor), más R5 (registro de accesos).

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §3.2.1 · op.acc.5 ENS

La fórmula es + [R2 o R3 o R4] + R5: un segundo factor de cualquiera de esas opciones y, en todo caso, el registro de accesos con éxito y fallidos e información al usuario de su último acceso.

#### 3. Para los proveedores externos se propone una cuenta por empresa, compartida entre sus técnicos. ¿Cómo debe valorarse?

- a) Está prohibida: op.acc.1.3 exige un identificador singular por entidad, y la cuenta compartida destruye la trazabilidad.
- b) Es admisible si la empresa proveedora designa por escrito a un responsable único que conteste por el uso de la cuenta.
- c) Es admisible para personal externo, porque op.acc.1 solo exige identificadores singulares al personal municipal.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 1 · §3.2 · op.acc.1.3 ENS

Con una cuenta compartida ninguna acción es atribuible a una persona. Lo correcto es una cuenta nominal por técnico, con certificado propio, ventana temporal acotada y acceso solo al servidor de salto.

#### 4. La propuesta sitúa la pasarela VPN en la red interna, publicada mediante una redirección de puertos. ¿Dónde debe ubicarse y por qué?

- a) En la red interna, como se propone, siempre que la redirección de puertos se limite al puerto que utiliza el servicio VPN.
- b) En la red de administración de sistemas, para que solo los administradores puedan modificar su configuración.
- c) En la DMZ, con la superficie mínima, porque si la pasarela se compromete el atacante no debe quedar ya dentro de la red interna.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §4.1.2

Con la pasarela en la red interna, comprometerla deja al atacante dentro sin cruzar ninguna otra frontera, lo que contradice el art. 23 del ENS y la lógica de mp.com.1.

#### 5. Se propone túnel dividido «para no saturar el enlace de la sede central con el vídeo de las reuniones y la navegación personal». ¿Qué configuración procede?

- a) Túnel dividido como regla general, porque la navegación personal del empleado queda fuera del ámbito del ENS.
- b) Túnel completo; el dividido solo como excepción justificada y acotada, por ejemplo para la videoconferencia corporativa.
- c) Túnel dividido para todo el tráfico, porque el art. 9 del ENS exige separar el tráfico corporativo del personal.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 2 · §4.1.2 · mp.s.3 ENS

Con el túnel dividido la navegación escapa al control corporativo y mp.s.3 deja de ser aplicable, y el equipo queda con un pie en cada red, como puente potencial, lo que compromete el art. 9 (líneas de defensa).

#### 6. Una vez conectado, ¿qué alcance de red debe tener el empleado en teletrabajo?

- a) Un segmento de teletrabajo propio, con acceso solo a lo imprescindible (expedientes, correo, intranet e impresión).
- b) La misma VLAN de puestos que en la oficina, porque la VPN ya cifra el tráfico y todo le funcionará igual.
- c) Acceso completo a la red interna, incluida la de administración, mientras se mantenga abierta la sesión VPN.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §3.1 · mp.eq.3.3 ENS

mp.eq.3.3 obliga a limitar la información y los servicios accesibles a los mínimos imprescindibles cuando la conexión llega por redes no controladas: el teletrabajador no debe alcanzar la red de administración, la de videovigilancia ni otros puestos.

#### 7. Los empleados usarían su equipo personal «porque no hay presupuesto para 900 portátiles». ¿Qué objeción jurídica plantea?

- a) Que el art. 47 bis del TREBEP solo permite el teletrabajo a los empleados que dispongan de equipo propio.
- b) Que el art. 47 bis del TREBEP dispone que la Administración proporcionará los medios tecnológicos necesarios.
- c) Que el art. 32 del RGPD prohíbe tratar datos personales desde cualquier dispositivo portátil del empleado.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §5 · art. 47 bis TREBEP

Conforme al artículo 47 bis del TREBEP, la Administración proporcionará a la persona los medios tecnológicos necesarios para el teletrabajo: la propuesta traslada al empleado una obligación de la Administración.

#### 8. Si de verdad no hubiera presupuesto para equipos corporativos, ¿qué alternativa es la más defendible?

- a) Un escritorio virtual (VDI): el dato no sale del CPD y el equipo personal actúa solo como terminal.
- b) La VPN con cliente en el equipo personal, porque al cifrar el canal protege también los dos extremos.
- c) Una VPN SSL/TLS sin cliente para los 900 empleados, con acceso completo a toda la red interna.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §5 · §3.1

La VPN protege el canal, no los extremos: un equipo no controlado lleva el problema al centro de la red. Con VDI el dato no sale del CPD, con el portapapeles y la redirección de unidades deshabilitados.

#### 9. ¿Qué tecnología de VPN procede para el acceso de los 900 teletrabajadores?

- a) L2TP sin IPsec, por ser el protocolo de tunelización más compatible con los encaminadores domésticos.
- b) IPsec solo con AH, por ser el protocolo de seguridad de IPsec que mejor atraviesa el NAT doméstico.
- c) VPN con cliente que use IKEv2 (con MOBIKE) como camino principal y TLS sobre TCP 443 como respaldo.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §4.2

IKEv2 rinde mejor y MOBIKE permite pasar del Wi-Fi doméstico a la red móvil sin cortar el túnel; TLS sobre 443 sirve de respaldo en redes que bloquean IPsec. L2TP no cifra por sí solo y AH no cifra y es incompatible con NAT.

#### 10. Para el enlace permanente con el centro de proceso de respaldo se elige IPsec en modo túnel con ESP. ¿Qué debe permitir el cortafuegos para que el túnel curse tráfico?

- a) Solo UDP 500, que es el puerto que utiliza IKEv2.
- b) UDP 500 y 4500 y el protocolo IP 50, que es el de ESP.
- c) Solo TCP 443, el mismo puerto que las VPN SSL/TLS.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §4.2.1

IKEv2 usa UDP 500 y UDP 4500 con travesía de NAT, y ESP es el protocolo IP 50. Abrir solo el 500 es el error clásico: el túnel se negocia pero no cursa tráfico.

### Caso 3. Incidente: ransomware entrado por un portátil municipal

#### 1. Reconstruida la cadena del incidente, ¿en qué eslabón un control habría cortado el ataque aun con la credencial ya en poder del atacante?

- a) En el movimiento lateral: el antivirus por firmas actualizado en los servidores, conforme a op.exp.6.
- b) En las copias de seguridad: el cifrado de los ficheros de copia en el servidor, conforme a mp.info.6.
- c) En la entrada por la VPN: un segundo factor de autenticación, exigible por op.acc.5 en categoría ALTA.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §3.2 · op.acc.5 ENS

La VPN solo pedía usuario y contraseña. En categoría ALTA op.acc.5 exige + [R2 o R3 o R4] + R5, y un segundo factor habría detenido el ataque aunque la contraseña ya estuviera robada.

#### 2. La empleada detectó a los diez minutos que la página era falsa, pero no avisó «por apuro». ¿Cómo debe valorarse ese eslabón?

- a) Como un fallo de cultura organizativa: debe existir un procedimiento para informar de incidentes, sean reales o falsas alarmas.
- b) Como una falta individual de la empleada, que el ENS obliga a sancionar conforme a op.acc.5 en categoría ALTA.
- c) Como un hecho irrelevante, porque las credenciales robadas no se usaron hasta el sábado por la mañana.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §5 · mp.per.3.3 ENS

mp.per.3.3 exige un procedimiento para informar de incidentes, «sean reales o falsas alarmas». Diez minutos de aviso el viernes habrían permitido bloquear la cuenta antes de que se usara.

#### 3. El antivirus de los servidores estaba actualizado y no detectó el movimiento lateral, hecho con herramientas legítimas del sistema. ¿Qué lo explica y qué medida lo habría visto?

- a) Las firmas estaban desfasadas; bastaba con forzar una actualización diaria de las firmas del antivirus.
- b) El antivirus por firmas es ciego ante el malware sin fichero; lo habría visto un EDR (op.exp.6.r4).
- c) El cifrado de disco ocultaba los ficheros al antivirus; bastaba con desactivarlo durante el análisis.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §5.2.1 · op.exp.6.r4 ENS

Con herramientas legítimas del sistema no hay fichero malicioso que reconocer por firma. El EDR, exigible en categoría ALTA (op.exp.6.r4), detecta el comportamiento y el movimiento lateral.

#### 4. Las copias de seguridad estaban en un recurso montado permanentemente en el servidor de copias y fueron cifradas. ¿Qué requisito incumplía esa configuración?

- a) Guardar al menos una copia separada, de modo que un incidente no afecte a la vez al original y a la copia (mp.info.6.r2).
- b) Cifrar las copias de seguridad, ya que estaban almacenadas en claro en el recurso compartido del servidor de copias.
- c) Emplear productos del catálogo CPSTIC para el servidor de copias, como exige op.pl.5 en categoría ALTA.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §5 · mp.info.6.r2 ENS

En nivel ALTO, mp.info.6.r2.1 exige que al menos una copia se almacene de forma separada, en lugar diferente, para que un incidente no pueda afectar a la vez al repositorio original y a la copia. Es literalmente lo que ocurrió.

#### 5. Activado el procedimiento de gestión de incidentes y constituido el equipo (op.exp.7), ¿cuál debe ser la siguiente acción?

- a) Restaurar los servidores cifrados desde la copia más reciente, para recuperar cuanto antes el servicio.
- b) Redactar el comunicado interno al personal y a los responsables sobre el alcance del incidente.
- c) Cortar el acceso remoto: deshabilitar la cuenta comprometida y, si es necesario, suspender la VPN.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §2.3

Primero se cierra el camino por el que el atacante sigue entrando; después se aísla y se segmenta. Restaurar antes de conocer el vector lleva a que los sistemas se vuelvan a cifrar.

#### 6. Al aislar en red los servidores afectados, ¿por qué NO deben apagarse?

- a) Porque al apagarlos el ransomware cifra de inmediato el resto de la red interna.
- b) Porque apagarlos destruye la memoria volátil, que es la evidencia más valiosa.
- c) Porque el ENS prohíbe apagar sin autorización un sistema de categoría ALTA.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §5.2.1

El aislamiento se hace con el EDR o desconectando el puerto del conmutador; apagar el equipo destruye la memoria volátil y, con ella, evidencia necesaria para el análisis.

#### 7. Antes de plantear cualquier restauración, ¿qué debe hacerse?

- a) Pagar el rescate si su importe es inferior al coste estimado de reconstruir los siete servidores afectados.
- b) Restaurar sobre los mismos servidores y analizar el vector de entrada después, con el servicio ya en marcha.
- c) Localizar la copia más reciente no comprometida, incluidas las fuera de línea, y haber determinado el vector de entrada.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §2.3

Hay que verificar el estado real de las copias antes de restaurar. No se paga el rescate, y restaurar sobre los mismos sistemas sin conocer el vector hace que se vuelvan a cifrar.

#### 8. Los servidores cifrados contienen expedientes con datos personales. ¿Qué notificaciones concurren?

- a) Solo a la AEPD, porque la notificación al CCN-CERT es voluntaria para las entidades locales.
- b) Al CCN-CERT por el ENS (art. 33 e ITS de Notificación de Incidentes) y a la AEPD por el RGPD.
- c) Solo al CCN-CERT, que traslada de oficio la notificación a la AEPD y a los interesados afectados.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 3 · §1.1 · art. 33 ENS · art. 33 RGPD

Concurren dos obligaciones por vías distintas: la del ENS ante el CCN-CERT, con la clasificación y plazos de la ITS de Notificación de Incidentes, y la del RGPD ante la AEPD al afectar a datos personales.

#### 9. ¿En qué plazo debe notificarse la violación de seguridad a la AEPD?

- a) En 72 horas como máximo desde que se tuvo conocimiento de ella.
- b) En 72 horas desde el acceso inicial, el viernes a las 19:10.
- c) En un mes desde que concluya el análisis forense del incidente.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · art. 33 RGPD

Conforme al artículo 33 del RGPD, el plazo máximo es de 72 horas desde que se tuvo conocimiento de la violación; si el riesgo para los interesados es alto, se les comunica también (art. 34).

#### 10. En el plan de mejora, ¿qué indicadores reflejan mejor la cultura de notificación del programa de concienciación?

- a) Solo el porcentaje de clics en las simulaciones, que debe quedar por debajo del 5 % de la plantilla.
- b) El número de expedientes disciplinarios abiertos al personal que pincha en las simulaciones de phishing.
- c) El porcentaje de notificaciones, que debe subir, y el tiempo hasta la primera notificación, que debe bajar.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §5 · mp.per.4 ENS

Un organismo donde muchos pinchan pero la mayoría avisa en minutos está mejor protegido que otro donde pincha poca gente y nadie avisa. Estos indicadores alimentan op.mon.2, y mp.per.4 exige evaluar la eficacia de la formación.
