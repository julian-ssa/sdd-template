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
librería antes de escribir código que la use. La configuración está versionada y usa el
servidor remoto por HTTP (`https://mcp.context7.com/mcp`), así que no necesita Node ni `npx`
en la máquina: Claude Code lee `.mcp.json` y Cursor `.cursor/mcp.json`. Ambos toman la clave
de la variable de entorno `CONTEXT7_API_KEY`; cada persona usa su propia clave (cuenta gratuita
en context7.com) y nunca se escribe en el repo.

Cómo definir la variable según la máquina:
- macOS y Linux (incluido el VPS): `export CONTEXT7_API_KEY="..."` en `~/.zshrc` o `~/.bashrc`
  del usuario que ejecuta el agente; abre una terminal nueva.
- Windows (PowerShell, una vez): `[Environment]::SetEnvironmentVariable("CONTEXT7_API_KEY", "...", "User")`;
  abre una terminal nueva. Si usas WSL, defínela dentro de WSL como en Linux.
- Ejecuciones sin sesión interactiva (VPS, scripts): pásala en el entorno del proceso.

La primera vez que Claude Code abre el repo pide aprobar el servidor del proyecto; para no
preguntar en cada máquina puede fijarse `"enableAllProjectMcpServers": true` en la configuración
de usuario de Claude Code. Para otras herramientas, añade un servidor MCP llamado `context7` de
tipo HTTP con esa URL y la cabecera `Authorization: Bearer <clave>` (Codex: `~/.codex/config.toml`,
sección `[mcp_servers.context7]`; opencode: `opencode.json`, clave `mcp`).

## Versiones: siempre la última estable

Regla del propietario (2026-09-16): toda dependencia, imagen base, runtime y acción de CI se
instala en su **última versión estable**, comprobada en la fuente en el momento de instalarla
(`npm view <paquete> version` y `dist-tags`, PyPI, Docker Hub, releases de GitHub), nunca de
memoria. Se descartan versiones candidatas (`rc`, `beta`, `next`). Si una versión no puede
adoptarse por incompatibilidad con otra dependencia, se anota aquí con el motivo y la condición
para actualizar, y se revisa en cada cambio de dependencias.

## Reglas

00. **Ramas y pull requests, siempre**: `develop` es la rama por defecto (entorno de pruebas) y `main` es
   producción; nadie escribe directamente en ninguna. Ramas `spec-NNN/...` desde `develop`, pull request contra
   `develop` mezclado por el propietario; producción se libera con un PR de `develop` a `main`.
   Antes de cualquier cambio: `git status` limpio, `git checkout develop && git pull` y crear la rama desde ahí.
0. **Herramientas obligatorias**: Context7 antes de escribir código con cualquier librería, Ponytail en cada
   tarea, impeccable en toda interfaz (instálala con `npx impeccable install --project --no-hooks` y muévela a
   `.agents/skills/`; el binario `scripts/bin/` no se versiona).
1. Nada se implementa fuera de una tarea de `tasks.md` de la spec activa. Sin plan y tareas
   aprobados, este repo solo recibe infraestructura.
2. Cada test lleva en su nombre el id del RF que cubre; la suite roja bloquea el merge. CI corre
   en cada push y pull request.
3. Nunca datos personales reales en código, tests, fixtures ni logs.
4. Secretos solo en variables de entorno (`.env` ignorado; `.env.example` documenta las claves).
5. Commits en inglés que citan spec y RF: `spec 001 RF-12: ...`. Sin trailers de atribución.
6. Al terminar una tarea, marca la casilla en `tasks.md` del repo de specs solo si su
   "Hecho cuando" se cumple, y anota el commit de este repo.
