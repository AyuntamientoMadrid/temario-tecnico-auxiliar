# Test del tema 25. Accesibilidad, seguridad del puesto y desarrollo seguro

60 preguntas con tres opciones y una sola correcta. Calificación como en el examen: +1 por acierto, −1/3 por error, 0 en blanco.

Versión interactiva: <https://ayuntamientomadrid.github.io/temario-tecnico-auxiliar/temas/tema-25.html>

## Batería de preguntas

### 1. Según la norma ISO 9241-11:2018, la usabilidad se define como el grado en que un sistema permite a usuarios específicos alcanzar objetivos específicos con:

- a) Eficacia, eficiencia y satisfacción en un contexto de uso específico
- b) Accesibilidad, disponibilidad y confidencialidad
- c) Corrección, completitud y pertinencia funcional

**Respuesta correcta:** a) · **Referencia:** §1.1 [ISO9241-11]

Los tres atributos van siempre acompañados de la referencia al contexto de uso: la usabilidad no es una propiedad absoluta del producto.

### 2. ¿Cuál de estas afirmaciones describe correctamente la relación entre accesibilidad y usabilidad?

- a) Son sinónimos: un sitio accesible es siempre usable
- b) La accesibilidad es una condición de partida exigible por ley; la usabilidad es un grado de calidad de uso no exigible con carácter general
- c) La usabilidad es exigible por el RD 1112/2018 y la accesibilidad solo se recomienda

**Respuesta correcta:** b) · **Referencia:** §1 [RD1112-2018] [ISO9241-11]

Un sitio puede cumplir WCAG AA y ser poco usable, y viceversa. Lo que el RD 1112/2018 impone es la accesibilidad, no la usabilidad.

### 3. El diseño universal se define en la Convención de la ONU sobre los derechos de las personas con discapacidad como el diseño de productos y entornos utilizables por todas las personas:

- a) Siempre que se disponga de una versión alternativa accesible del producto
- b) Mediante adaptaciones individuales realizadas a petición del interesado
- c) En la mayor medida posible, sin necesidad de adaptación ni diseño especializado

**Respuesta correcta:** c) · **Referencia:** §1.2 [CDPD] [TRLGDPD]

Es la definición literal del artículo 2 de la Convención, recogida también por el RDL 1/2013 con la denominación «diseño para todas las personas».

### 4. Los ajustes razonables, en la normativa española de discapacidad:

- a) Sustituyen al diseño universal cuando este resulta costoso
- b) Son medidas individualizadas y subsidiarias, que se aplican cuando el diseño universal no resuelve la situación de una persona concreta
- c) Son obligatorios con independencia de que impongan una carga desproporcionada

**Respuesta correcta:** b) · **Referencia:** §1.2 [TRLGDPD] [CDPD]

La secuencia correcta es diseño universal, tecnología de apoyo compatible y, solo entonces, ajuste razonable; y estos no pueden imponer una carga desproporcionada.

### 5. ¿Cuántos principios formuló el Center for Universal Design en 1997 y cuál de los siguientes es uno de ellos?

- a) Siete principios, entre ellos la tolerancia al error
- b) Cuatro principios, entre ellos la robustez
- c) Diez principios, entre ellos la visibilidad del estado del sistema

**Respuesta correcta:** a) · **Referencia:** §1.2 [CUD]

Los cuatro principios (POUR) corresponden a WCAG y las diez heurísticas a Nielsen; los siete principios del diseño universal son de Ronald L. Mace y su equipo.

### 6. En el modelo de calidad del producto software ISO/IEC 25010:2023, el contenido que la edición de 2011 recogía como subcaracterística «accesibilidad» se cubre con:

- a) Una característica independiente, al mismo nivel que la fiabilidad
- b) La subcaracterística de confidencialidad, dentro de la seguridad
- c) Las subcaracterísticas de inclusividad y asistencia al usuario, dentro de la capacidad de interacción

**Respuesta correcta:** c) · **Referencia:** §1.3 [ISO25010]

La edición de 2023 ya no recoge la accesibilidad como subcaracterística. En el mismo modelo, la disponibilidad es subcaracterística de la fiabilidad y la confidencialidad lo es de la seguridad: las tres piezas que dan título a este tema están en tres características distintas.

### 7. ¿Qué distingue el objeto de la serie ISO 9241 del de la familia ISO/IEC 25000 (SQuaRE)?

- a) ISO 9241 regula la seguridad y SQuaRE la accesibilidad
- b) Ambas miden lo mismo, pero SQuaRE es la versión europea
- c) ISO 9241 es una norma de ergonomía centrada en el proceso y la interacción; SQuaRE mide la calidad del producto software

**Respuesta correcta:** c) · **Referencia:** §1.3 [ISO9241-11] [ISO25000]

La usabilidad aparece en ambas familias, pero con perspectivas distintas: como resultado del contexto de uso en ISO 9241-11 y como característica medible del producto en ISO/IEC 25010, que en su edición de 2023 la denomina capacidad de interacción.

### 8. El diseño centrado en las personas de ISO 9241-210 exige que el proceso sea:

- a) Iterativo y con evaluación frente a los requisitos realizada con usuarios reales
- b) Lineal, con una única evaluación de expertos al finalizar el desarrollo
- c) Automatizado mediante herramientas de análisis de la interfaz

**Respuesta correcta:** a) · **Referencia:** §1.1 [ISO9241-210]

Sus cuatro actividades son comprender el contexto de uso, especificar requisitos, producir soluciones de diseño y evaluar frente a los requisitos, repitiendo el ciclo.

### 9. Un formulario municipal muestra un mensaje de error que dice únicamente «Error 0x8007». ¿Qué heurística de Nielsen se incumple de forma más evidente?

- a) Flexibilidad y eficiencia de uso
- b) Ayuda a reconocer, diagnosticar y recuperarse de los errores
- c) Diseño estético y minimalista

**Respuesta correcta:** b) · **Referencia:** §1.1 [NIELSEN]

Los mensajes deben expresarse en lenguaje llano e indicar qué ha ocurrido y qué debe hacer la persona, no un código interno sin explicación.

### 10. ¿Qué método de evaluación de la usabilidad es una técnica de inspección que no requiere usuarios?

- a) La evaluación heurística
- b) La prueba de usabilidad con pensamiento en voz alta
- c) La prueba A/B en producción

**Respuesta correcta:** a) · **Referencia:** §1.1 [NIELSEN] [ISO9241-210]

Es una inspección realizada por personas expertas contra un catálogo de heurísticas; las otras dos requieren usuarios reales interactuando con el sistema.

### 11. Los cuatro principios de WCAG (POUR) son:

- a) Perceptible, Operable, Compatible y Reutilizable
- b) Portable, Ordenado, Comprensible y Rápido
- c) Perceptible, Operable, Comprensible y Robusto

**Respuesta correcta:** c) · **Referencia:** §2.1 [WCAG22]

De ellos cuelgan las 13 pautas y, de estas, los criterios de conformidad, que son lo único verificable y normativo.

### 12. Dentro de la estructura de WCAG 2.x, ¿qué elementos son normativos y verificables?

- a) Los principios y las pautas
- b) Únicamente los criterios de conformidad
- c) Las técnicas suficientes documentadas por el W3C

**Respuesta correcta:** b) · **Referencia:** §2.1 [WCAG22]

Las pautas son objetivos generales y las técnicas son documentación informativa: se puede cumplir un criterio con una técnica no listada, siempre que sea comprobable.

### 13. ¿Qué nivel de conformidad WCAG exige la normativa española para los sitios web del sector público?

- a) Nivel AA
- b) Nivel A
- c) Nivel AAA

**Respuesta correcta:** a) · **Referencia:** §2.1 [RD1112-2018] [WCAG22]

Lo impone el RD 1112/2018 por remisión a la norma UNE-EN 301 549. El propio W3C desaconseja exigir el nivel AAA para sitios completos porque no es alcanzable para todo tipo de contenido.

### 14. ¿Cuál de estas afirmaciones sobre WCAG 2.2 es correcta?

- a) Sustituye a WCAG 2.1, que queda derogada y sin validez
- b) Es una norma ISO desde 2012 con el código ISO/IEC 40500
- c) Es Recomendación del W3C desde octubre de 2023, añade nueve criterios y retira el criterio 4.1.1 «Análisis sintáctico»

**Respuesta correcta:** c) · **Referencia:** §2.1 [WCAG22] [WCAG20]

La norma ISO/IEC 40500:2012 corresponde a WCAG 2.0, no a la 2.2.

### 15. El criterio 1.4.3 «Contraste (mínimo)», de nivel AA, exige una relación de contraste de:

- a) 3:1 para todo el texto
- b) 4,5:1 para el texto normal y 3:1 para el texto grande
- c) 7:1 para el texto normal y 4,5:1 para el texto grande

**Respuesta correcta:** b) · **Referencia:** §2.1 [WCAG22]

Los valores 7:1 y 4,5:1 corresponden al criterio 1.4.6 «Contraste (mejorado)», que es de nivel AAA.

### 16. Una aplicación municipal marca los campos obligatorios pintando su borde de rojo, sin ningún otro indicador. ¿Qué criterio WCAG incumple?

- a) 1.4.1 Uso del color
- b) 2.1.1 Teclado
- c) 4.1.2 Nombre, función, valor

**Respuesta correcta:** a) · **Referencia:** §2.1 [WCAG22]

El color no puede ser el único medio visual para transmitir información: hace falta además un texto, un símbolo o una etiqueta.

### 17. El criterio 3.3.8 «Autenticación accesible (mínimo)», incorporado en WCAG 2.2:

- a) Obliga a implantar autenticación multifactor en todos los servicios públicos
- b) Prohíbe exigir una prueba de función cognitiva sin ofrecer un método alternativo, y obliga a permitir pegar en los campos de contraseña
- c) Exige que la contraseña tenga una longitud mínima de doce caracteres

**Respuesta correcta:** b) · **Referencia:** §2.1 [WCAG22]

Recordar una contraseña, transcribir caracteres o resolver un rompecabezas son pruebas cognitivas que deben tener alternativa accesible.

### 18. Respecto a los requisitos de conformidad de WCAG, ¿cuál de las siguientes afirmaciones es correcta?

- a) La conformidad puede declararse de las partes accesibles de una página, excluyendo las demás
- b) Basta con que sea conforme la primera pantalla de un proceso de varios pasos
- c) La conformidad se predica de páginas completas y de procesos completos

**Respuesta correcta:** c) · **Referencia:** §2.1 [WCAG22]

Si un solo paso de la solicitud de cita no es conforme, no lo es todo el proceso.

### 19. ¿Qué relación existe entre la norma EN 301 549 y las pautas WCAG?

- a) La EN 301 549 incorpora los criterios A y AA de WCAG en su capítulo sobre web y añade requisitos que WCAG no cubre
- b) La EN 301 549 sustituye a WCAG en el ámbito europeo, que queda sin aplicación
- c) Son normas independientes y sin relación: WCAG se aplica a la web y la EN 301 549 solo al hardware

**Respuesta correcta:** a) · **Referencia:** §2.2 [EN301549] [WCAG22]

Sus capítulos añaden hardware, comunicación bidireccional, documentos no web, software, documentación y servicios de apoyo, que quedan fuera del alcance de WCAG.

### 20. El Ayuntamiento licita la renovación de los tótems de autoservicio de sus oficinas de atención. ¿Qué exigencia de accesibilidad debe recoger el pliego?

- a) Únicamente la conformidad con WCAG 2.2 nivel AA
- b) Ninguna, porque el hardware queda fuera de la normativa de accesibilidad
- c) La conformidad con los capítulos aplicables de la EN 301 549, entre ellos el de hardware

**Respuesta correcta:** c) · **Referencia:** §2.2 [EN301549]

WCAG cubre el contenido web; para hardware, telefonía, documentos y software es la norma europea la que fija los requisitos, y es además la referencia de la contratación pública.

### 21. Según el RD 1112/2018, la alegación de carga desproporcionada:

- a) Exime al organismo de publicar declaración de accesibilidad
- b) Debe ser motivada, declararse expresamente y acompañarse de una alternativa accesible, y no puede fundarse en falta de prioridad, tiempo o conocimientos
- c) Puede aplicarse de forma genérica a todo el sitio web sin justificación individualizada

**Respuesta correcta:** b) · **Referencia:** §2.3 [RD1112-2018]

La valoración atiende al tamaño, los recursos y la naturaleza del organismo frente al beneficio estimado para las personas con discapacidad.

### 22. La declaración de accesibilidad de un organismo público debe indicar el grado de cumplimiento mediante una de estas tres categorías:

- a) Plenamente conforme, parcialmente conforme o no conforme
- b) Nivel A, nivel AA o nivel AAA
- c) Conforme, en revisión o exento

**Respuesta correcta:** a) · **Referencia:** §2.4 [DEC2018-1523] [RD1112-2018]

El modelo lo fija la Decisión de Ejecución (UE) 2018/1523, y la declaración debe recoger además el contenido no accesible, la fecha y el método de evaluación y el mecanismo de comunicación y reclamación.

### 23. Sobre las herramientas automáticas de evaluación de la accesibilidad, ¿qué afirmación es correcta?

- a) Detectan todos los criterios de conformidad, por lo que bastan para declarar la conformidad
- b) No tienen valor alguno y no deben emplearse en una auditoría
- c) Detectan solo una parte de los criterios, por lo que deben combinarse con revisión manual experta y con tecnologías de apoyo

**Respuesta correcta:** c) · **Referencia:** §2.4 [WCAG-EM] [OBSERVATORIO]

Una herramienta detecta que falta el atributo <code>alt</code>, pero no que su contenido sea «imagen1.jpg»: una web puede superar el 100 % de las pruebas automáticas y ser inaccesible.

### 24. Las cinco dimensiones de seguridad del Esquema Nacional de Seguridad son:

- a) Confidencialidad, integridad, disponibilidad, usabilidad y accesibilidad
- b) Disponibilidad, integridad, confidencialidad, autenticidad y trazabilidad
- c) Prevención, detección, respuesta, conservación y recuperación

**Respuesta correcta:** b) · **Referencia:** §3.1 [ENS]

Las tres primeras forman la triada clásica; autenticidad y trazabilidad son la aportación característica del esquema español.

### 25. El uso de cuentas genéricas compartidas por varias personas en un puesto de trabajo compromete principalmente:

- a) La trazabilidad, porque ninguna actuación resulta imputable a una persona concreta
- b) La disponibilidad, porque el sistema se satura con accesos simultáneos
- c) La integridad de las copias de seguridad

**Respuesta correcta:** a) · **Referencia:** §3.2.1 [ENS]

Por eso el ENS exige cuentas nominativas y proscribe las genéricas salvo justificación excepcional.

### 26. La política de «puesto de trabajo despejado y pantalla limpia» es un control de naturaleza:

- a) Tecnológica, porque depende del software de cifrado instalado
- b) De personas, porque consiste exclusivamente en formación
- c) Física y organizativa, orientada a evitar la exposición no autorizada de información en el entorno del puesto

**Respuesta correcta:** c) · **Referencia:** §3.1.1 [ISO27002] [ENS]

Se complementa con el bloqueo de sesión, los filtros de privacidad, la impresión segura y la destrucción segura de documentos.

### 27. Antes de retirar del servicio un equipo que ha manejado datos personales, la medida correcta es:

- a) Formatear el disco, ya que el formateo elimina definitivamente la información
- b) Aplicar un procedimiento de borrado seguro o de destrucción del soporte conforme a las categorías de saneamiento reconocidas
- c) Borrar las carpetas del usuario y vaciar la papelera de reciclaje

**Respuesta correcta:** b) · **Referencia:** §3.1.1 [NIST-800-88]

Formatear no es borrar: la información sigue siendo recuperable, y en unidades de estado sólido el borrado exige órdenes específicas del dispositivo o el cifrado previo del soporte.

### 28. Respecto a la información que reside en el disco local del puesto de usuario, el criterio correcto es:

- a) El puesto no debe albergar información única: el dato de trabajo debe residir en el repositorio corporativo
- b) Toda la información debe residir en el disco local para garantizar el trabajo sin conexión
- c) Es indiferente dónde resida, siempre que el disco esté cifrado

**Respuesta correcta:** a) · **Referencia:** §3.1.2 [ENS]

Esta regla resuelve a la vez la disponibilidad, el control de acceso y el cumplimiento documental: el disco local es caché de trabajo, no archivo.

### 29. ¿Qué mide el RPO (Recovery Point Objective)?

- a) El tiempo máximo que puede transcurrir hasta restablecer el servicio
- b) El tiempo medio entre fallos de un componente
- c) La cantidad máxima de información que se puede permitir perder, medida en tiempo hacia atrás desde el incidente

**Respuesta correcta:** c) · **Referencia:** §3.1.2 [ENS]

Determina la frecuencia de las copias; el tiempo de restablecimiento del servicio es el RTO, que mira hacia delante.

### 30. Un servicio con una disponibilidad comprometida del 99,9 % anual admite aproximadamente:

- a) 53 minutos de indisponibilidad al año
- b) 8,8 horas de indisponibilidad al año
- c) 3,65 días de indisponibilidad al año

**Respuesta correcta:** b) · **Referencia:** §3.1.2 [ENS]

El 99,99 % equivale a unos 53 minutos anuales y el 99 % a unos 3,65 días: cada nueve adicional divide aproximadamente por diez el tiempo admitido.

### 31. ¿Cuál de estas combinaciones constituye autenticación multifactor en sentido estricto?

- a) Contraseña más código temporal generado por una aplicación en el móvil
- b) Contraseña más pregunta de seguridad sobre datos personales
- c) Contraseña más repetición de la contraseña en un segundo campo

**Respuesta correcta:** a) · **Referencia:** §3.2.1 [NIST-800-63B]

La MFA exige dos factores de naturaleza distinta: aquí, algo que se sabe y algo que se tiene. La pregunta de seguridad es también conocimiento, por lo que no aporta un segundo factor.

### 32. ¿Qué característica hace que la autenticación con FIDO2/WebAuthn sea resistente al phishing?

- a) Que utiliza contraseñas de mayor longitud que las convencionales
- b) Que envía el segundo factor por SMS a un número verificado
- c) Que la credencial está ligada criptográficamente al dominio legítimo, por lo que no puede entregarse a un sitio suplantado

**Respuesta correcta:** c) · **Referencia:** §3.2.1 [WEBAUTHN] [NIST-800-63B]

Ni siquiera un usuario engañado puede entregarla a un sitio fraudulento; el SMS, en cambio, se considera un canal restringido por su exposición a la interceptación y al intercambio fraudulento de tarjeta SIM.

### 33. Respecto a la gestión de contraseñas, las guías actuales recomiendan:

- a) Forzar el cambio de contraseña cada 30 días para todos los usuarios
- b) Favorecer la longitud sobre las reglas rígidas de complejidad y cambiar la contraseña cuando haya indicio de compromiso, no de forma periódica sistemática
- c) Almacenar las contraseñas cifradas de forma reversible para poder recuperarlas si el usuario las olvida

**Respuesta correcta:** b) · **Referencia:** §3.2.1 [NIST-800-63B] [OWASP-CHEAT]

La caducidad periódica obligatoria degrada la calidad de las contraseñas; y en el servidor solo debe guardarse el resumen con una función diseñada para ello y sal única por usuario, nunca cifrado reversible.

### 34. El modelo de autorización basado en roles (RBAC) resulta el más adecuado en la Administración porque:

- a) Asigna los permisos a roles y las personas a roles, lo que hace la autorización auditable y estable frente a la rotación de personal
- b) Permite que cada empleado decida quién accede a los documentos que crea
- c) Calcula la decisión de acceso en función de la hora y la ubicación de cada petición

**Respuesta correcta:** a) · **Referencia:** §3.2.1 [ENS]

La opción de que decida el propietario del recurso describe el modelo discrecional (DAC) y la decisión por atributos y contexto describe el modelo ABAC.

### 35. El principio de mínimo privilegio aplicado al puesto de usuario implica, entre otras medidas, que:

- a) El usuario debe ser administrador local para poder resolver sus propias incidencias
- b) Los permisos se conceden de forma permanente para evitar interrupciones del servicio
- c) El usuario no es administrador local de su equipo y las tareas administrativas se realizan con cuentas separadas y nominativas

**Respuesta correcta:** c) · **Referencia:** §3.2.1 [SALTZER75] [ENS]

Es la medida que más eficazmente limita el alcance del código malicioso y la instalación de software no autorizado, y se completa con la revisión periódica y la retirada inmediata de permisos al cese.

### 36. El cifrado de disco completo de un portátil protege la información:

- a) En cualquier circunstancia, incluso frente a código malicioso que se ejecuta con la sesión iniciada
- b) Cuando el equipo está apagado o el disco se extrae, pero no cuando la sesión está iniciada
- c) Solo mientras el equipo permanece dentro de la red corporativa

**Respuesta correcta:** b) · **Referencia:** §3.2.2 [NIST-800-111]

Con el sistema en marcha, los ficheros se entregan descifrados a cualquier proceso autorizado: el cifrado complementa, pero no sustituye, al control de acceso y al bloqueo de sesión.

### 37. ¿Cuál es la diferencia esencial entre un virus y un gusano?

- a) El virus cifra la información y el gusano la borra
- b) El virus afecta a servidores y el gusano a puestos de usuario
- c) El virus se inserta en otro programa o fichero anfitrión, mientras que el gusano se propaga por sí mismo a través de la red

**Respuesta correcta:** c) · **Referencia:** §3.3.1 [ATTACK]

El cifrado de la información con exigencia de rescate caracteriza al ransomware, y el troyano se presenta como software legítimo sin replicarse.

### 38. Frente a un ransomware de tipo nuevo, todavía sin firma conocida, la defensa técnica más eficaz en el puesto es:

- a) El análisis de comportamiento en tiempo de ejecución, que detecta lo que el programa hace con independencia de su firma
- b) La actualización diaria del catálogo de firmas del antivirus
- c) El filtro de contenidos del navegador

**Respuesta correcta:** a) · **Referencia:** §3.3.1 [ATTACK] [ENS]

La detección por firmas es ciega ante el código nuevo o polimórfico; y, en todo caso, lo único que garantiza la recuperación tras un cifrado consumado es la copia de seguridad aislada y verificada.

### 39. Una copia de seguridad diferencial:

- a) Copia lo cambiado desde la última copia de cualquier tipo y se restaura con toda la cadena
- b) Copia lo cambiado desde la última copia completa y se restaura con dos elementos: la completa y la última diferencial
- c) Es equivalente a una instantánea del volumen

**Respuesta correcta:** b) · **Referencia:** §3.3.2 [ISO27002]

La que se mide desde la última copia de cualquier tipo y exige toda la cadena es la incremental; y la instantánea no es una copia de seguridad, porque depende del mismo almacenamiento.

### 40. La regla 3-2-1 de copias de seguridad, en su versión reforzada frente al ransomware, añade:

- a) Que las copias se realicen exclusivamente en horario nocturno
- b) Que se conserven durante un mínimo de diez años
- c) Al menos una copia inmutable o desconectada, y la verificación mediante pruebas de restauración

**Respuesta correcta:** c) · **Referencia:** §3.3.2 [ENS] [ISO27002]

Un atacante con privilegios busca primero cifrar o borrar las copias; y una copia que nunca se ha restaurado no es una copia, sino una hipótesis.

### 41. Un sistema de prevención de fuga de datos (DLP) se distingue de una copia de seguridad en que:

- a) La copia protege frente a la pérdida de la información y el DLP frente a su salida no autorizada
- b) El DLP sustituye a la copia de seguridad en los puestos portátiles
- c) La copia actúa sobre datos en tránsito y el DLP sobre datos en reposo exclusivamente

**Respuesta correcta:** a) · **Referencia:** §3.3.2 [ISO27002]

El DLP clasifica la información, vigila los canales de salida (correo, web, extraíbles, impresión) y registra, avisa, cifra o bloquea la operación.

### 42. En el Esquema Nacional de Seguridad, la categoría de un sistema:

- a) Se calcula como la media de los niveles de sus cinco dimensiones
- b) Es la correspondiente al nivel más alto alcanzado en cualquiera de sus dimensiones de seguridad
- c) La fija libremente el responsable del sistema en función del presupuesto disponible

**Respuesta correcta:** b) · **Referencia:** §3.3.3 [ENS]

El nivel (bajo, medio o alto) se predica de cada dimensión y la categoría (básica, media o alta) del sistema: una sola dimensión valorada en nivel alto convierte todo el sistema en categoría alta.

### 43. ¿Cuál de estos NO es un principio básico del Esquema Nacional de Seguridad?

- a) La gestión de la seguridad basada en los riesgos
- b) La existencia de líneas de defensa
- c) La certificación obligatoria de todos los productos por el fabricante

**Respuesta correcta:** c) · **Referencia:** §3.3.3 [ENS]

Los principios básicos son la seguridad como proceso integral, la gestión basada en riesgos, la prevención-detección-respuesta-conservación, la existencia de líneas de defensa, la vigilancia continua y reevaluación periódica y la diferenciación de responsabilidades.

### 44. El criterio de «desplazamiento a la izquierda» (shift left) en el ciclo de vida de desarrollo seguro significa que:

- a) La seguridad se introduce lo antes posible en el ciclo, porque el coste de corregir un defecto crece con la fase en que se detecta
- b) Las pruebas de seguridad se concentran exclusivamente en la fase de verificación previa al despliegue
- c) La responsabilidad de la seguridad se traslada al equipo de operaciones

**Respuesta correcta:** a) · **Referencia:** §4.1.1 [NIST-SSDF] [MS-SDL]

Ello no significa «solo al principio»: la seguridad es actividad de todas las fases, incluidas el despliegue, la operación y la retirada.

### 45. ¿Qué diferencia a OWASP SAMM de BSIMM?

- a) SAMM se aplica a aplicaciones móviles y BSIMM a aplicaciones web
- b) SAMM es un modelo prescriptivo de madurez y BSIMM es un modelo descriptivo construido observando programas reales
- c) SAMM es una norma ISO certificable y BSIMM una recomendación del NIST

**Respuesta correcta:** b) · **Referencia:** §4.1.1 [OWASP-SAMM] [BSIMM]

SAMM indica qué hacer y en qué orden madurar, con cinco funciones de negocio y tres niveles; BSIMM sirve para compararse con lo que hace el sector.

### 46. Para redactar requisitos de seguridad verificables en el pliego de una aplicación municipal, la herramienta más adecuada de OWASP es:

- a) El Top 10, porque enumera los diez riesgos más críticos
- b) SAMM, porque mide la madurez de la organización proveedora
- c) ASVS, porque es un catálogo de requisitos verificables organizado en tres niveles

**Respuesta correcta:** c) · **Referencia:** §4.1.1 [OWASP-ASVS] [OWASP-TOP10]

El Top 10 es un documento de concienciación, no una norma de verificación; SAMM mide el proceso de la organización, no el producto entregado.

### 47. En el modelo STRIDE, la elevación de privilegios (Elevation of privilege) niega la propiedad de:

- a) Autorización
- b) Autenticidad
- c) No repudio

**Respuesta correcta:** a) · **Referencia:** §4.1.2 [SHOSTACK]

La autenticidad la niega la suplantación (Spoofing) y el no repudio lo niega el repudio (Repudiation); la manipulación niega la integridad, la revelación de información la confidencialidad y la denegación de servicio la disponibilidad.

### 48. El artículo 25 del RGPD impone al responsable del tratamiento:

- a) La obligación de cifrar todos los datos personales con AES-256
- b) La protección de datos desde el diseño y por defecto, de modo que solo se traten los datos necesarios para cada finalidad sin intervención del usuario
- c) La realización de una evaluación de impacto en todos los tratamientos, sin excepción

**Respuesta correcta:** b) · **Referencia:** §4.1.2 [RGPD]

La evaluación de impacto es una obligación del artículo 35, exigible cuando el tratamiento entrañe un alto riesgo; y el artículo 32 habla de medidas apropiadas al riesgo, sin imponer un algoritmo concreto.

### 49. El principio de «diseño abierto» de Saltzer y Schroeder establece que:

- a) El código fuente de toda aplicación pública debe publicarse íntegramente
- b) Cualquier persona puede modificar la configuración de seguridad del sistema
- c) La seguridad no debe depender del secreto del diseño, sino del secreto de la clave

**Respuesta correcta:** c) · **Referencia:** §4.2.1 [SALTZER75]

Es la formulación clásica del rechazo a la seguridad por oscuridad; ocultar la versión del servidor es una medida higiénica menor, no un control de seguridad.

### 50. El principio de «mediación completa» aplicado a una aplicación web exige que:

- a) Cada acceso a cada objeto se verifique siempre, sin cachear la decisión de autorización tomada al iniciar sesión
- b) Todas las peticiones pasen obligatoriamente por un cortafuegos de aplicación
- c) La validación de datos se realice tanto en el cliente como en el servidor

**Respuesta correcta:** a) · **Referencia:** §4.2.1 [SALTZER75]

El cortafuegos de aplicación es una capa adicional, no la mediación; y la doble validación es una buena práctica distinta, en la que la del cliente cumple una función de usabilidad, no de seguridad.

### 51. Respecto a la validación de entradas, la práctica correcta es:

- a) Validar únicamente en el cliente, para reducir la carga del servidor
- b) Validar siempre en el servidor, preferir la lista blanca a la lista negra y canonicalizar antes de validar
- c) Filtrar las comillas simples y la palabra «script» en todos los campos de entrada

**Respuesta correcta:** b) · **Referencia:** §4.2.2 [OWASP-CHEAT] [OWASP-PROACTIVE]

El atacante no usa el formulario, envía la petición directamente; y las listas negras siempre quedan incompletas frente a codificaciones alternativas del mismo valor.

### 52. La defensa correcta y suficiente frente a la inyección SQL es:

- a) Escapar las comillas simples de todos los parámetros recibidos
- b) Restringir la longitud máxima de los campos de entrada del formulario
- c) Emplear consultas parametrizadas (sentencias preparadas), de modo que los valores nunca se interpreten como código

**Respuesta correcta:** c) · **Referencia:** §4.2.2 [OWASP-CHEAT] [OWASP-TOP10]

La consulta se compila con marcadores y los valores viajan aparte, sin poder alterar la estructura; el escapado manual es frágil y dependiente del motor.

### 53. Un ataque de XSS almacenado se caracteriza porque:

- a) La carga maliciosa se guarda en el servidor y afecta a todos los usuarios que visualizan el contenido
- b) La carga viaja en la petición y se devuelve en la respuesta, por lo que requiere engañar a la víctima con un enlace
- c) La carga nunca llega al servidor: el guion del cliente la toma de la URL o del almacenamiento local

**Respuesta correcta:** a) · **Referencia:** §4.2.2 [OWASP-TOP10] [OWASP-CHEAT]

Las otras dos descripciones corresponden al XSS reflejado y al XSS basado en DOM respectivamente; el almacenado es el más grave por su alcance.

### 54. ¿Qué relación hay entre OAuth 2.0 y OpenID Connect?

- a) Son dos nombres del mismo protocolo de autenticación
- b) OAuth 2.0 es un marco de autorización delegada y OpenID Connect es la capa de autenticación construida sobre él, que añade el token de identidad
- c) OpenID Connect es la versión anterior de OAuth 2.0, ya en desuso

**Respuesta correcta:** b) · **Referencia:** §4.2.3.1 [RFC6749]

Usar OAuth 2.0 «a secas» para autenticar usuarios es un error clásico de diseño.

### 55. Una aplicación permite consultar expedientes mediante la dirección <code>/expedientes/ver?id=48213</code>, y cambiar el número muestra el expediente de otra persona. Esta vulnerabilidad se clasifica como:

- a) Inyección SQL, categoría A03 del OWASP Top 10
- b) Configuración de seguridad defectuosa, categoría A05
- c) Pérdida de control de acceso con referencia directa a objeto insegura, categoría A01

**Respuesta correcta:** c) · **Referencia:** §4.2.3.1 [OWASP-TOP10]

La corrección es comprobar en el servidor, en cada petición, que el expediente solicitado pertenece al usuario autenticado; usar identificadores no predecibles es una medida complementaria, nunca sustitutiva.

### 56. Regenerar el identificador de sesión en el momento de la autenticación es la defensa frente a:

- a) La fijación de sesión (session fixation)
- b) La inyección de mandatos del sistema operativo
- c) La falsificación de peticiones del lado del servidor (SSRF)

**Respuesta correcta:** a) · **Referencia:** §4.2.3.2 [OWASP-ASVS]

En este ataque el adversario impone a la víctima un identificador de sesión que él ya conoce; si el identificador se regenera al autenticarse, el conocido deja de ser válido.

### 57. El atributo <code>HttpOnly</code> de una cookie de sesión sirve para:

- a) Forzar que la cookie viaje únicamente por HTTPS
- b) Impedir que el código de guion del cliente pueda leerla, limitando el robo de sesión mediante XSS
- c) Evitar que la cookie se envíe en peticiones de origen cruzado

**Respuesta correcta:** b) · **Referencia:** §4.2.3.2 [OWASP-CHEAT]

Forzar HTTPS es la función del atributo <code>Secure</code> y evitar el envío en peticiones de origen cruzado es la del atributo <code>SameSite</code>, que mitiga el CSRF.

### 58. Sobre el uso de JSON Web Tokens (JWT), ¿cuál de estas afirmaciones es correcta?

- a) Al ir firmados, su contenido queda cifrado y puede incluir datos personales sin riesgo
- b) El servidor debe aceptar el algoritmo que indique la cabecera del propio token para garantizar la interoperabilidad
- c) Un JWT es autocontenido y no revocable por sí mismo, por lo que exige vidas cortas y un mecanismo adicional de revocación

**Respuesta correcta:** c) · **Referencia:** §4.2.3.2 [RFC7519] [RFC8725]

Además, el JWT va firmado pero no cifrado —su contenido es legible por quien lo posea— y el servidor debe fijar de antemano el algoritmo admitido y rechazar el algoritmo <code>none</code>.

### 59. En el registro de auditoría de una aplicación, ¿qué información NO debe registrarse nunca?

- a) La identidad del usuario que realiza cada operación sobre datos sensibles
- b) Las contraseñas, los identificadores de sesión y los tokens de acceso
- c) Los intentos fallidos de autenticación y los fallos de autorización

**Respuesta correcta:** b) · **Referencia:** §4.2.4 [OWASP-CHEAT] [RGPD]

Tampoco deben registrarse claves criptográficas ni datos personales innecesarios: un registro indiscreto es una brecha de datos esperando ocurrir, y le son aplicables los principios de minimización y limitación del plazo de conservación.

### 60. ¿Cuál de estas afirmaciones sobre las técnicas de verificación de la seguridad del software es correcta?

- a) SAST analiza el código sin ejecutarlo, DAST ataca la aplicación en ejecución sin ver el código y SCA analiza las dependencias de terceros
- b) DAST analiza el código fuente y SAST ataca la aplicación desplegada
- c) Las herramientas automáticas detectan de forma fiable los fallos de lógica de negocio y de autorización

**Respuesta correcta:** a) · **Referencia:** §4.3.2 [OWASP-ASVS] [OWASP-TOP10]

Ninguna herramienta automática detecta los fallos de lógica de negocio ni de autorización: para eso hacen falta revisión manual de código y pruebas de penetración.

## Preguntas sobre los casos prácticos

### Caso 1. Auditoría de accesibilidad de la sede de cita previa

#### 1. En el portal de cita previa, los iconos de cada trámite tienen como alt el nombre del fichero («icono-01.png»). ¿Qué principio y qué pauta de WCAG se vulneran?

- a) Perceptible, pauta 1.1 Alternativas textuales: la alternativa debe ser equivalente, no un relleno.
- b) Operable, pauta 2.4 Navegable: el nombre del fichero impide saltar los bloques repetidos.
- c) Comprensible, pauta 3.1 Legible: el nombre del fichero no declara el idioma de la imagen.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.1

Todo contenido no textual necesita una alternativa textual equivalente (1.1.1, nivel A); si el icono es decorativo, alt="".

#### 2. El calendario para elegir el día solo responde al ratón. ¿Qué incumple?

- a) El principio Perceptible, pauta 1.3 Adaptable (marcado semántico de la tabla del calendario).
- b) El principio Operable, pauta 2.1 Accesible por teclado (criterio 2.1.1, nivel A).
- c) El principio Comprensible, pauta 3.2 Predecible (cambio de contexto al elegir un día).

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.1

Toda la funcionalidad debe poder usarse solo con teclado y sin trampas de foco.

#### 3. Los campos obligatorios del formulario de cita se señalan solo con el borde en rojo. ¿Qué criterio se incumple en primer término?

- a) El 2.2.1 Ajuste de tiempo (nivel A), porque el usuario tarda más en localizar los campos.
- b) El 4.1.3 Mensajes de estado (nivel AA), porque el borde rojo no se anuncia como región activa.
- c) El 1.4.1 Uso del color (nivel A), además del 3.3.2 Etiquetas o instrucciones por la falta de texto.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 1 · §2.1

No se puede transmitir información solo mediante el color; hay que añadir un texto o un icono con alternativa textual.

#### 4. La sesión del portal caduca a los cinco minutos sin aviso ni prórroga y el formulario se pierde. ¿Qué pauta de WCAG se vulnera?

- a) La 3.2 Predecible (3.2.6 Ayuda coherente): el aviso de caducidad debe aparecer siempre en el mismo sitio.
- b) La 2.2 Tiempo suficiente (2.2.1 Ajuste de tiempo): el límite debe poder desactivarse, ajustarse o prorrogarse.
- c) La 2.3 Convulsiones y reacciones físicas: el cierre brusco de la sesión provoca un destello de pantalla.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 1 · §2.1

Los límites de tiempo deben poder desactivarse, ajustarse o prorrogarse; es un criterio del principio Operable.

#### 5. El pie del portal no enlaza ninguna declaración de accesibilidad. ¿Cómo debe calificarse este hallazgo?

- a) No es un criterio de WCAG: es un incumplimiento del artículo 15 del RD 1112/2018.
- b) Es un incumplimiento del criterio 3.2.6 Ayuda coherente de WCAG 2.2, de nivel A.
- c) Es un incumplimiento del artículo 16 del RD 1112/2018, que regula la declaración.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 1 · §2.3 · art. 15 RD 1112/2018

La declaración de accesibilidad es una obligación del RD 1112/2018 (art. 15), no un criterio de conformidad de WCAG; el art. 16 regula la unidad responsable.

#### 6. ¿Qué nivel de conformidad es exigible al Ayuntamiento para el portal y en virtud de qué norma?

- a) El nivel A, por la Directiva (UE) 2019/882, transpuesta por la Ley 11/2023.
- b) El nivel AAA, por el RD 1112/2018, al tratarse de un servicio público esencial.
- c) El nivel AA de WCAG, por el RD 1112/2018, que remite a la UNE-EN 301 549 vigente.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.3

El requisito técnico del RD 1112/2018 es la conformidad con la UNE-EN 301 549, lo que supone el nivel AA de WCAG en la parte web; la Ley 11/2023 se dirige sobre todo al sector privado.

#### 7. ¿Por qué el pliego de un nuevo desarrollo debe exigir la EN 301 549 y no solo «WCAG AA»?

- a) Porque deroga los criterios de WCAG para la web y los sustituye por requisitos propios más estrictos.
- b) Porque solo la EN 301 549 obliga a alcanzar el nivel AAA en los procesos de cita previa.
- c) Porque es la norma armonizada de la contratación pública y abarca además documentos, software y hardware.

**Respuesta correcta:** c) · **Referencia:** Caso 1, cuestión 2 · §2.2

La EN 301 549 incorpora los criterios A y AA de WCAG (cap. 9) y añade documentos no web, software, hardware, comunicación bidireccional y servicios de apoyo.

#### 8. El área gestora quiere declarar el portal «plenamente conforme» porque el analizador automático no da errores. ¿Es correcto?

- a) No: los hallazgos prueban incumplimientos, y una herramienta automática solo comprueba una parte de los criterios.
- b) Sí, siempre que el analizador se base en reglas ACT y la declaración cite su nombre como método.
- c) Sí, con carácter provisional, hasta la revisión anual obligatoria de la declaración de accesibilidad.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 3 · §2.4

La evaluación válida combina revisión automática, revisión manual experta y prueba con tecnologías de apoyo; declarar un grado superior al real es en sí un incumplimiento.

#### 9. ¿Qué debe incluir, como mínimo, la declaración de accesibilidad del portal?

- a) La lista de herramientas automáticas empleadas y el porcentaje de páginas sin errores detectados.
- b) El grado de cumplimiento, el contenido no accesible, las alternativas, la fecha y el método, y la vía de reclamación.
- c) El nombre de la empresa desarrolladora, el importe del contrato y el plazo de garantía del portal.

**Respuesta correcta:** b) · **Referencia:** Caso 1, cuestión 4 · §2.4

El modelo de la Decisión (UE) 2018/1523 fija esos elementos; la declaración se enlaza desde todas las páginas y se revisa al menos cada año.

#### 10. Un vecino no puede completar la cita con su lector de pantalla y presenta una queja. ¿Quién debe atenderla?

- a) La unidad responsable de accesibilidad que el artículo 16 del RD 1112/2018 obliga a designar.
- b) El Observatorio de Accesibilidad Web de la Administración General del Estado.
- c) El delegado de protección de datos del Ayuntamiento, por tratarse de un trámite con datos personales.

**Respuesta correcta:** a) · **Referencia:** Caso 1, cuestión 4 · §2.4 · art. 16 RD 1112/2018

La unidad responsable de accesibilidad es obligatoria en cada organismo y, entre sus funciones, responde las comunicaciones y reclamaciones.

### Caso 2. Incidente en el puesto de una Oficina de Atención a la Ciudadanía

#### 1. La empleada introduce su usuario y contraseña en el enlace de un correo que suplanta al servicio informático. ¿Qué tipo de ataque ha sufrido?

- a) Un ataque de fuerza bruta contra la contraseña, que acaba con el acceso desde el extranjero.
- b) Un phishing (ingeniería social) que deriva en robo de credenciales y en un acceso no autorizado.
- c) Un ransomware que, tras cifrar el puesto, envía las credenciales al servidor del atacante.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 1 · §3.1

El ataque explota la confianza y la urgencia, no un fallo técnico: la propia empleada entrega sus credenciales.

#### 2. ¿Qué medida habría neutralizado con más eficacia este primer suceso?

- a) Un segundo factor por SMS, el canal que NIST considera más robusto frente a la interceptación.
- b) La caducidad obligatoria de la contraseña cada 30 días, que inutiliza pronto la credencial robada.
- c) La autenticación multifactor resistente al phishing (FIDO2/WebAuthn o certificado en tarjeta).

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 1 · §3.2.1

Su credencial está ligada criptográficamente al dominio legítimo y no puede entregarse a un sitio suplantado ni siquiera por un usuario engañado.

#### 3. Roban el portátil del inspector, que estaba apagado y con cifrado de disco completo. ¿Qué dimensión se ve afectada con seguridad?

- a) La disponibilidad; la confidencialidad no se compromete si la clave no era accesible para el tercero.
- b) La confidencialidad, en todo caso, porque el soporte con los expedientes ha salido del perímetro.
- c) La integridad, porque el ladrón puede modificar los expedientes aunque el disco esté cifrado.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 2 · §3.2.2

El cifrado de disco completo protege el equipo apagado: el inspector pierde su herramienta y los datos locales, pero la información es ininteligible para el tercero.

#### 4. ¿Qué problema de fondo revela el robo del portátil del inspector?

- a) Que el cifrado de disco completo no protege la información cuando el equipo está apagado.
- b) Que el inspector no tenía permisos de administrador local para cifrar sus propias carpetas.
- c) Que había información única en el disco local, cuando el dato debe vivir en el repositorio corporativo.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 2 · §3.1.2

Regla de oro: en el puesto no debe residir información única; el disco local es caché de trabajo, no archivo.

#### 5. El ransomware cifra la unidad de red y la última copia es de hace 26 horas. ¿Cuál es el dato correcto del incidente?

- a) Un RTO de 26 horas: el servicio tardará más de un día en volver a estar disponible.
- b) Un RPO efectivo de 26 horas: se pierde el trabajo de más de un día.
- c) Un RPO de cero horas, porque la unidad de red compartida estaba respaldada.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 3 · §3.1.2

El RPO mira hacia atrás y mide la información perdida desde la última copia; el RTO mide el tiempo hasta recuperar el servicio.

#### 6. Además de la frecuencia, ¿qué defecto de la política de copias de la oficina es el más grave?

- a) Que nunca se haya probado la restauración, de modo que la copia es una hipótesis y no una garantía.
- b) Que las copias estén cifradas, porque el cifrado impide restaurarlas tras un ataque de ransomware.
- c) Que se usen copias incrementales, que no pueden restaurarse si falta la copia completa más reciente.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §3.3.2

Una copia que no se ha restaurado nunca no es una copia de seguridad; la prueba periódica de restauración es requisito expreso del ENS.

#### 7. ¿Qué debe hacerse antes de dar por recuperado el servicio tras el ransomware?

- a) Desinfectar el puesto con el antivirus y restaurar la copia más reciente, aunque sea posterior a la infección.
- b) Restaurar la copia y reconectar el puesto sin cambiar credenciales, porque el cifrado ya ha terminado.
- c) Reconstruir el puesto desde imagen limpia y restaurar desde una copia anterior a la infección, verificando su integridad.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 3 · §3.3.1

Hay que erradicar y determinar el vector, reconstruir desde imagen limpia, restaurar una copia previa a la infección, rotar credenciales y revisar los registros.

#### 8. ¿Por qué disponer de copias no exime de tratar el ransomware como posible brecha de datos personales?

- a) Porque el ransomware actual practica doble extorsión: además de cifrar, exfiltra la información.
- b) Porque las copias de seguridad no pueden incluir nunca la unidad de red compartida de un área.
- c) Porque el RGPD obliga a notificar en 24 horas cualquier pérdida de disponibilidad de datos.

**Respuesta correcta:** a) · **Referencia:** Caso 2, cuestión 3 · §3.3.1

Puede haber compromiso de confidencialidad aunque la disponibilidad se recupere con las copias.

#### 9. Todos los usuarios de la oficina son administradores locales de su equipo. ¿Qué principio se vulnera y cómo se corrige?

- a) La necesidad de conocer; se corrige restringiendo las carpetas de red del área a quien de verdad las necesite.
- b) El mínimo privilegio; se retira el privilegio de la cuenta ordinaria y se usan cuentas administrativas separadas y nominativas.
- c) La segregación de funciones; se corrige exigiendo que un compañero de la oficina apruebe cada programa instalado.

**Respuesta correcta:** b) · **Referencia:** Caso 2, cuestión 4 · §3.2.1

Que el usuario no sea administrador local es la medida que más limita la instalación no autorizada y el alcance del código malicioso.

#### 10. En los puestos de atención se usa la cuenta genérica «oac-mostrador». ¿Qué dimensión se vulnera y cuál es la corrección?

- a) La disponibilidad; se crea una segunda cuenta genérica de respaldo por si la primera se bloquea.
- b) La integridad; se obliga a cambiar la contraseña de la cuenta genérica cada 30 días.
- c) La trazabilidad; se usan cuentas nominativas, con sesión individual aunque el puesto sea compartido.

**Respuesta correcta:** c) · **Referencia:** Caso 2, cuestión 4 · §3.2.1

Sin cuentas nominativas ninguna actuación es imputable a una persona; las cuentas genéricas están proscritas en el ENS salvo justificación excepcional.

### Caso 3. Contratación y verificación del desarrollo de la aplicación

#### 1. La consulta /expedientes/ver?id=48213 no comprueba en el servidor que el expediente sea del usuario. ¿En qué categoría del OWASP Top 10:2021 encaja?

- a) A07 Fallos de identificación y autenticación.
- b) A05 Configuración de seguridad defectuosa.
- c) A01 Pérdida de control de acceso.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 1 · §4.3.1

Es una referencia directa insegura a objetos (IDOR): un fallo de autorización, la primera categoría del Top 10:2021.

#### 2. El buscador construye la consulta a la base de datos concatenando el texto del usuario. ¿Qué categoría del Top 10:2021 le corresponde?

- a) A03 Inyección.
- b) A06 Componentes vulnerables y desactualizados.
- c) A08 Fallos de integridad del software y de los datos.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §4.2.2

El sistema no distingue entre datos y código: el texto introducido puede alterar la estructura de la consulta SQL.

#### 3. Ante un error, la aplicación devuelve la traza con la versión del gestor de base de datos y la ruta del servidor. ¿Cómo se clasifica?

- a) A09 Fallos de registro y monitorización; en STRIDE, R (repudio).
- b) A05 Configuración de seguridad defectuosa; en STRIDE, I (revelación de información).
- c) A02 Fallos criptográficos; en STRIDE, T (manipulación).

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 1 · §4.2.4

Las páginas de error detalladas en producción revelan información y dan al atacante el mapa del sistema.

#### 4. El JWT de sesión se guarda en el almacenamiento local y no caduca nunca. ¿Cómo se clasifica?

- a) A07 Fallos de identificación y autenticación; en STRIDE, S (suplantación).
- b) A10 Falsificación de peticiones del lado del servidor; en STRIDE, E (elevación de privilegios).
- c) A04 Diseño inseguro; en STRIDE, D (denegación de servicio).

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 1 · §4.2.3

El token equivale a la credencial: quien lo roba se hace pasar por el usuario, y una gestión de sesión deficiente es un fallo de autenticación.

#### 5. ¿Cuál es la corrección adecuada del fallo de la consulta de expedientes por identificador?

- a) Cifrar el identificador del expediente en la URL para que el vecino no pueda deducir otros números.
- b) Ocultar el enlace de consulta en el menú de los usuarios que no tengan expedientes asignados.
- c) Comprobar en el servidor, en cada petición, que el expediente es del usuario autenticado, denegando por defecto.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 2 · §4.2.3

Ocultar en el cliente no es autorizar, y cifrar el identificador es seguridad por oscuridad; los UUID solo son una medida complementaria.

#### 6. ¿Cómo se corrige la consulta del buscador construida por concatenación?

- a) Escapando las comillas del texto introducido antes de concatenarlo a la consulta.
- b) Con consultas parametrizadas (sentencias preparadas), en las que los valores viajan aparte.
- c) Con una lista negra que rechace palabras reservadas como SELECT, DROP o UNION.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §4.2.2

La consulta se compila con marcadores y los valores no pueden alterar su estructura; escapar o filtrar con listas negras siempre queda incompleto.

#### 7. ¿Qué corrección procede para el JWT sin caducidad guardado en el almacenamiento local?

- a) Alargar la vida del token y borrarlo del almacenamiento local cuando el usuario cierre la sesión.
- b) Vida corta con exp validada, token de refresco revocable con rotación y cookie HttpOnly, Secure y SameSite.
- c) Mantenerlo en el almacenamiento local, pero aceptar el algoritmo que indique el propio token.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 2 · §4.2.3

Un JWT es autocontenido y no revocable por sí mismo: exige vida corta, refresco revocable en el servidor y un almacenamiento no legible por guiones.

#### 8. ¿Qué catálogo de OWASP es el idóneo para redactar las exigencias de seguridad del pliego?

- a) OWASP ASVS, catálogo de requisitos verificables del producto.
- b) El OWASP Top 10, por ser el documento de referencia del sector.
- c) OWASP SAMM, porque mide la madurez del proceso del proveedor.

**Respuesta correcta:** a) · **Referencia:** Caso 3, cuestión 3 · §4.1.1

ASVS habla del producto y sus requisitos son verificables en la recepción; el Top 10 es de concienciación y SAMM evalúa el proceso.

#### 9. ¿Qué técnica habría detectado de forma fiable el fallo de autorización de la consulta de expedientes?

- a) El análisis de composición (SCA) integrado en la construcción.
- b) El análisis estático (SAST) ejecutado en cada confirmación.
- c) La revisión manual de código y la prueba de penetración.

**Respuesta correcta:** c) · **Referencia:** Caso 3, cuestión 4 · §4.3.2

Ninguna herramienta automática entiende la lógica de negocio ni sabe qué expediente corresponde a qué persona.

#### 10. ¿Qué debe implantar el proveedor para responder con rapidez cuando se publique una vulnerabilidad en una dependencia?

- a) Un cortafuegos de aplicación que sustituya a la actualización de la biblioteca afectada.
- b) Un SBOM en formato normalizado (SPDX o CycloneDX) y análisis SCA continuo en la construcción.
- c) Una prueba de penetración anual que incluya la revisión de las bibliotecas de terceros.

**Respuesta correcta:** b) · **Referencia:** Caso 3, cuestión 4 · §4.3.3

El inventario de dependencias permite responder en horas, y no en semanas, si la aplicación está afectada; el WAF nunca sustituye a la corrección.
