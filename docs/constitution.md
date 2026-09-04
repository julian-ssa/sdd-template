# Constitución - {{PROYECTO}}

Principios innegociables. Toda spec, plan, tarea y línea de código debe cumplirlos.
Cada principio termina con cómo se verifica, para que `sdd-validate` pueda comprobarlo.
Cambiar un principio requiere un ADR aceptado. Entre 6 y 12 principios; borra los que no
apliquen y añade los propios del dominio.

1. **La spec manda.** Ningún comportamiento se implementa si no está en la spec activa y
   aprobada. Si falta una decisión o un marcador `[NECESITA ACLARACIÓN]` bloquea un RF, el
   trabajo se detiene y se pregunta.
   *Se verifica:* cada tarea de `tasks.md` cita al menos un RF; cada RF tiene un test con su id.

2. **Dominio sin interfaz.** La lógica de negocio vive en un paquete puro, sin dependencias
   de HTTP, interfaz gráfica ni base de datos, y es testeable con datos en memoria. Cada
   regla o fórmula relevante está documentada en `docs/reference/`.
   *Se verifica:* el paquete de dominio no importa módulos de red, UI ni base de datos; sus tests corren sin servicios externos.

3. **Determinismo.** Todo cálculo recibe sus entradas de forma explícita (incluida la fecha
   o el reloj cuando importe); los mismos datos producen siempre el mismo resultado.
   *Se verifica:* ninguna función de dominio llama al reloj ni a generadores no inyectados; los tests son reproducibles.

4. **Datos tipados.** {{Ajusta: importes como decimal exacto con moneda; fechas de negocio como fecha de calendario; zona horaria de presentación explícita; identificadores opacos.}}
   *Se verifica:* el esquema no usa tipos ambiguos para esos datos; hay un test de redondeo/formato solo en presentación.

5. **{{Alcance de datos / tenencia.}}** {{Si el producto sirve a varias organizaciones o usuarios: toda entidad de negocio pertenece a exactamente un propietario y ninguna consulta cruza propietarios; el alcance se aplica en la capa de acceso a datos.}}
   *Se verifica:* test que demuestra que un usuario de A no lee datos de B.

6. **Permisos en el servidor.** Lo que cada rol puede ver y hacer se aplica en el servidor,
   no en la interfaz. {{Lista los roles.}}
   *Se verifica:* test por rol que intenta lo prohibido y recibe denegación.

7. **Operaciones idempotentes.** {{Importaciones, sincronizaciones o reintentos producen el mismo estado al repetirse y nunca destruyen historial.}}
   *Se verifica:* test de doble ejecución sin cambios.

8. **Cambios de esquema como código.** Las migraciones son archivos versionados y se aplican
   de forma automatizada, nunca a mano.
   *Se verifica:* existe un directorio de migraciones versionado y la integración continua las aplica.

9. **Tests como puerta.** Cada RF aparece en el nombre o la descripción de al menos un test
   automático. Una suite en rojo bloquea la integración. No se avanza a la siguiente tarea
   con tests en rojo.
   *Se verifica:* la integración continua falla si algún test falla; `sdd-validate` no reporta RF sin test.

10. **Idiomas.** Specs, documentación y mensajes al usuario en {{idioma}}; identificadores,
    esquema, nombres de archivo de código y commits de los repos de código en inglés. Ningún
    texto visible al usuario se escribe literal en el código: pasa por la capa de
    internacionalización.
    *Se verifica:* grep de cadenas de UI literales en el código devuelve vacío.

11. **Honestidad.** {{Si el producto muestra estimaciones, puntuaciones o predicciones: los avisos que explican sus límites son requisitos, no adornos.}}
    *Se verifica:* cada pantalla afectada tiene un RF que exige el aviso y un test que lo comprueba.

12. **Seguridad y datos personales.** Secretos solo en variables de entorno; sesiones
    revocables desde el servidor; toda acción administrativa queda en un registro de
    auditoría con quién, cuándo y sobre qué. Los datos personales nunca aparecen en logs ni
    en repositorios; los ejemplos son ficticios. Existe un camino para borrar o anonimizar a
    una persona a petición ({{ley aplicable}}).
    *Se verifica:* grep de datos reales en docs, specs y código devuelve vacío; hay test de auditoría por acción administrativa; existe el borrado/anonimización con test.
