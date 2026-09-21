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

## Reglas de autoría y estilo (para toda persona y agente, en cualquier herramienta)

- Los commits, pull requests y archivos van únicamente a nombre de la persona que los hace. **Nunca** se añaden trailers `Co-Authored-By`, `Claude-Session`, líneas "Generated with Claude Code" ni ninguna otra atribución a una herramienta o modelo. El CI rechaza los commits que las lleven.
- **Nunca el guion largo** (em dash, U+2014) en ningún texto. Se usa "-". El CI lo comprueba en todo texto propio; queda fuera el texto de terceros vendido tal cual (skills `ponytail` e `impeccable`, bloque que genera Next.js).
- Estas reglas viven en el repositorio (este archivo, `.claude/settings.json` y el CI) para que apliquen a cualquiera que lo clone, sin depender de configuración local.

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

## Economía de contexto (tokens): para toda persona y agente

Cada turno reenvía todo el historial; lo que se lee una vez se paga en cada turno siguiente. Reglas:

- **Modelo y esfuerzo al empezar, nunca a mitad de tarea.** El repo fija por defecto `opus` con esfuerzo `medium` en `.claude/settings.json` (Fable solo lo cargan las skills SDD de diseño: `sdd-spec`, `sdd-plan`, `sdd-validate`, `sdd-change`). Cambiar de modelo a mitad de sesión reprocesa todo el historial sin caché.
- **Abre la sesión dentro del repo**, no en la carpeta padre del workspace: la caché es por directorio y los ajustes del proyecto solo aplican dentro del repo.
- **Nunca vuelques archivos grandes al contexto**: casos dorados `docs/reference/golden/*.json` (hasta 180 KB cada uno), exports, volcados, `package-lock`, salidas de `git log -p`. Resume con `jq`, `head`, `wc` o `grep`, o delega la lectura a un subagente y quédate con la conclusión.
- **Revisar un PR**: primero `gh pr view N --json files`, después el diff por archivo y sin datos: `git diff base...rama -- . ":!docs/reference/golden"`. Los JSON dorados están marcados en `.gitattributes` para no aparecer en los diffs; míralos a propósito con `git diff --text` solo cuando toque.
- **Compacta en los límites naturales** (`/compact` al cerrar una tarea), no cuando salte la compactación automática a mitad de una.
- **Comprueba el consumo** con `/usage` (línea "Prompt cache (main)": ratio de aciertos y causa probable del último fallo) y `/context`.
