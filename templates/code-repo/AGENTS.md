# AGENTS.md - {{REPO}}

Contexto canónico para cualquier agente de código o LLM. `CLAUDE.md` solo contiene
`@AGENTS.md`; el resto de herramientas leen este archivo directamente.

## Antes de nada: las specs están en `../{{PROYECTO}}-specs`

Este repo se trabaja dentro de un workspace (carpeta normal, sin git) con el repo de
specs como hermano. Si `../{{PROYECTO}}-specs` no existe, clónalo ahí antes de hacer nada:

```bash
cd .. && git clone {{URL_SPECS}}
```

Lee, en este orden: `../{{PROYECTO}}-specs/AGENTS.md`, `../{{PROYECTO}}-specs/docs/constitution.md`
y la spec activa.

## Qué es este repo

{{DESCRIPCION: qué pieza es, stack decidido (cita el ADR de stack), qué datos posee, cómo se despliega}}

## Spec activa

{{Spec NNN y estado de su plan.md y tasks.md, o "ninguna todavía"}}

## Comandos

```bash
{{instalar, desarrollo, lint, tipos, tests, build}}
```

## Skills

`.agents/skills/` contiene las skills SDD (enlaces simbólicos relativos por skill al repo de
specs, por ejemplo `sdd-plan -> ../../../{{PROYECTO}}-specs/.agents/skills/sdd-plan`) y
`ponytail` (reglas para escribir el mínimo código que funciona; MIT). `.claude/skills` y
`.opencode/skill` son enlaces a `.agents/skills`.

## Documentación actualizada de librerías (Context7)

Usa el servidor MCP Context7 para consultar la documentación de la versión exacta de cada
librería antes de escribir código que la use. Configuración versionada para Claude Code
(`.mcp.json`) y Cursor (`.cursor/mcp.json`). Para otras herramientas, añade a tu configuración
de usuario un servidor MCP llamado `context7` con el comando `npx -y @upstash/context7-mcp`.
La clave de API es opcional y va en tu entorno local, nunca en el repo.

## Reglas

1. Nada se implementa fuera de una tarea de `tasks.md` de la spec activa. Sin plan y tareas
   aprobados, este repo solo recibe infraestructura.
2. Cada test lleva en su nombre el id del RF que cubre; la suite roja bloquea el merge. CI corre
   en cada push y pull request.
3. Nunca datos personales reales en código, tests, fixtures ni logs.
4. Secretos solo en variables de entorno (`.env` ignorado; `.env.example` documenta las claves).
5. Commits en inglés que citan spec y RF: `spec 001 RF-12: ...`. Sin trailers de atribución.
6. Al terminar una tarea, marca la casilla en `tasks.md` del repo de specs solo si su
   "Hecho cuando" se cumple, y anota el commit de este repo.
