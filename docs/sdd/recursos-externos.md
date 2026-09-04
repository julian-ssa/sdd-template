# Recursos externos

Registro de todo lo que vive fuera de este repo y que una tarea puede necesitar.
Sirve para etiquetar tareas `[H]`/`[M]` en `tasks.md`: si un recurso dice
"agente: no", la tarea que lo necesita no es `[A]`.

| Recurso | Para qué | Propietario | ¿Agente puede usarlo? | Notas |
|---|---|---|---|---|
| GitHub - repos `{{PROYECTO}}-*` | Código, PRs, CI | {{persona}} | Con `gh` autenticado, sí | Crear remoto y proteger `main` es `[H]`. |
| {{Hosting}} | | | | |
| {{Base de datos}} | | | Solo con credencial en `.env` | |
| {{Proveedor de correo}} | | | No | |
| {{Sistema externo del que se leen datos}} | | | | Contrato en `docs/reference/`. |
| Datos personales de {{cliente}} | | {{responsable del tratamiento}} | No; nunca en repos ni logs | {{ley aplicable}}. |
