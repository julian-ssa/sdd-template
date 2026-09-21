# AGENTS.md - {{PROYECTO}}-specs

Contexto canónico para cualquier agente de código o LLM (Claude Code, Codex, Cursor,
Gemini CLI, opencode, Jules, xAI, chat plano…). [`CLAUDE.md`](CLAUDE.md) solo contiene `@AGENTS.md`;
el resto de herramientas leen este archivo directamente. Si tu herramienta no lo carga
sola, pega su contenido al inicio de la sesión.

## Proyecto

**{{PROYECTO}}** - {{DESCRIPCION}}.
Visión, actores y alcance: [`docs/product/overview.md`](docs/product/overview.md). Modelo de dominio: [`docs/product/domain-model.md`](docs/product/domain-model.md).

Este repositorio es la **fuente de verdad del producto**: constitución, specs, decisiones
y documentación. No contiene código de aplicación.

## Estado del proyecto ({{FECHA}})

- Fase: **solo specs**. Stack de implementación **pendiente** → [`docs/decisions/ADR-0002-stack.md`](docs/decisions/ADR-0002-stack.md).
- Prohibido crear `apps/`, `packages/`, `src/` o cualquier código aquí.
- Prohibido ejecutar la fase de plan (`sdd-plan`) mientras [ADR-0002](docs/decisions/ADR-0002-stack.md) esté `pendiente`.
- Tras la decisión de stack se crearán los repos de código como hermanos de este en el
  workspace, sin submódulos (ver [ADR-0001](docs/decisions/ADR-0001-repositorios.md)); su `AGENTS.md` apunta a `../{{PROYECTO}}-specs`.

## Mapa del workspace y de los repos

```
../                       workspace local (no es repo git)
├── {{PROYECTO}}-specs/   este repo
└── {{otros repos o material de referencia, solo lectura}}
```

Repos externos (NO se clonan en el workspace; se leen bajo demanda y su contrato está
documentado con el commit leído):

| Repo | Qué es | Contrato |
|---|---|---|
| {{url}} | {{qué es}} | `docs/reference/{{nombre}}-contract.md` |

## Mapa de este repo

| Ruta | Contenido |
|---|---|
| [`docs/constitution.md`](docs/constitution.md) | Principios innegociables. Léelo antes de cualquier tarea. |
| `docs/sdd/` | El método: [`README.md`](README.md) (cómo trabajar), [`prompts.md`](docs/sdd/prompts.md) (prompts por fase, para cualquier LLM), [`recursos-externos.md`](docs/sdd/recursos-externos.md) (accesos y quién los tiene). |
| `docs/product/` | Visión, glosario, modelo de dominio, requisitos transversales (RNF), roadmap/backlog. |
| `docs/reference/` | Lo que ya existe y se porta o integra: sistemas previos, fórmulas, contratos externos. |
| `docs/decisions/` | ADRs. Una decisión por archivo. |
| `specs/` | Una carpeta por funcionalidad: `NNN-nombre/spec.md` (+ `plan.md`, `tasks.md` cuando toque). Índice y estado en [`specs/README.md`](specs/README.md). |
| [`tools/links.py`](tools/links.py) | Único script del repo: comprueba (`--check`) o corrige (`--fix`) los enlaces entre archivos markdown. No es código de aplicación. |
| `.agents/skills/` | Skills SDD canónicas (formato Agent Skills: `SKILL.md` con `name`/`description`). `.claude/skills` y `.opencode/skill` son enlaces simbólicos a ellas. |

## Convenciones de specs

- Carpeta `specs/NNN-nombre-en-kebab-case/`, numeración de tres dígitos, la siguiente libre.
- `spec.md` sigue [`specs/_templates/spec.md`](specs/_templates/spec.md) sin saltar secciones.
- Requisitos funcionales numerados `RF-n` (únicos dentro de la spec) en notación **EARS**:
  `CUANDO … , EL SISTEMA …` · `SI … , ENTONCES EL SISTEMA …` · `MIENTRAS … , EL SISTEMA …` ·
  `DONDE … , EL SISTEMA …` · `EL SISTEMA …`.
- Un requisito, una frase, verificable. Sin adjetivos no medibles.
- Lo que no se sabe se marca `[NECESITA ACLARACIÓN: pregunta concreta]` y se lista en "Dudas abiertas".
- Requisitos no funcionales: se citan por id `RNF-n` desde [`docs/product/requisitos-transversales.md`](docs/product/requisitos-transversales.md).
- Términos de dominio: los del glosario [`docs/product/glossary.md`](docs/product/glossary.md). No inventes sinónimos.
- La spec describe el QUÉ y el POR QUÉ. Nada de stack, arquitectura, tablas, endpoints ni nombres de archivo.
- Idiomas: specs, docs y mensajes al usuario en **{{idioma de specs}}**; identificadores, esquema y commits de código en **inglés**.
- `tasks.md` etiqueta cada tarea `[A]` (agente), `[H]` (humano) o `[M]` (mixta) y abre con "Prerrequisitos humanos".
- **Toda referencia a otro archivo del repo es un enlace markdown relativo** que se pueda abrir con un clic: [`docs/constitution.md`](docs/constitution.md), `[ADR-0002](docs/decisions/ADR-0002-stack.md)`, `[spec 001](specs/001-nombre/spec.md)`. Nunca una ruta suelta ni solo el nombre "[ADR-0002](docs/decisions/ADR-0002-stack.md)" o "spec 001" sin enlace. Vale para specs, docs, ADRs, skills y plantillas. `python3 tools/links.py --check` lo verifica y `--fix` lo corrige.

## Flujo SDD

Fases y skill que las ejecuta (detalle en [`docs/sdd/README.md`](docs/sdd/README.md); prompt equivalente en [`docs/sdd/prompts.md`](docs/sdd/prompts.md)):

| Fase | Skill | Produce |
|---|---|---|
| Spec y clarificación | `sdd-spec` | `specs/NNN-*/spec.md` |
| Plan y tareas | `sdd-plan` | `plan.md` + `tasks.md` (bloqueado hasta [ADR-0002](docs/decisions/ADR-0002-stack.md)) |
| Implementación de una tarea | `sdd-implement` | código + tests, en el repo de código |
| Validación de una spec | `sdd-validate` | veredicto RF por RF |
| Cambio de requisito | `sdd-change` | spec actualizada primero, luego plan y tareas |
| Lote de tareas sin supervisión | `sdd-run` | rama `spec-NNN/Ta-Tb` + pull request con informe; solo con autorización del propietario ([`docs/sdd/ejecucion-desatendida.md`](docs/sdd/ejecucion-desatendida.md)) |

## Recursos externos

Registro completo con propietario y si un agente puede usarlo: [`docs/sdd/recursos-externos.md`](docs/sdd/recursos-externos.md).
Si una tarea necesita una credencial, cuenta o acceso que no tienes, **no la simules**:
márcala `[H]` o `[M]` y párate.

## Reglas de autoría y estilo (para toda persona y agente, en cualquier herramienta)

- Los commits, pull requests y archivos van únicamente a nombre de la persona que los hace. **Nunca** se añaden trailers `Co-Authored-By`, `Claude-Session`, líneas "Generated with Claude Code" ni ninguna otra atribución a una herramienta o modelo. El CI rechaza los commits que las lleven.
- **Nunca el guion largo** (em dash, U+2014) en ningún texto. Se usa "-". El CI lo comprueba en todo texto propio; queda fuera el texto de terceros vendido tal cual (skills `ponytail` e `impeccable`, bloque que genera Next.js).
- Estas reglas viven en el repositorio (este archivo, `.claude/settings.json` y el CI) para que apliquen a cualquiera que lo clone, sin depender de configuración local.

## Reglas

1. Lee [`docs/constitution.md`](docs/constitution.md) y la spec activa antes de escribir nada.
2. No inventes stack ni arquitectura mientras [ADR-0002](docs/decisions/ADR-0002-stack.md) esté pendiente.
3. No modifiques el material de referencia del workspace. Es solo lectura.
4. Nunca copies a este repo datos personales reales. Los ejemplos usan valores ficticios.
5. Si un marcador `[NECESITA ACLARACIÓN]` bloquea un requisito, pregunta; no rellenes el hueco con una suposición silenciosa.
6. Toda decisión que cambie el modelo de dominio o los permisos requiere un ADR nuevo, no una edición silenciosa.
7. Actualiza [`specs/README.md`](specs/README.md) (estado y número de marcadores) cada vez que toques una spec.
8. **Herramientas obligatorias en todo repo de código, plan y tarea**: Context7 antes de escribir código con cualquier librería (documentación de la versión instalada, nunca de memoria), Ponytail en cada tarea (el mínimo código que funciona; ninguna dependencia sin justificar) e impeccable en toda interfaz. Cada `plan.md` lleva la sección "Herramientas obligatorias del agente" y cada `tasks.md` la tarea transversal TX-3.
9. **Ramas y pull requests, siempre**: nadie escribe directamente en `main` (este repo) ni en `develop` o `main` (repos de código). Todo cambio va en una rama (`spec-NNN/...`, `chore/...`, `docs/...`) y termina en un pull request que revisa y mezcla el propietario. En los repos de código los PR van contra `develop` (entorno de pruebas) y `develop` pasa a `main` (producción) por un PR de liberación. **Antes de cualquier cambio**: `git fetch` y `git pull` de la rama base (`main` aquí, `develop` en los repos de código) y crear la rama nueva desde ahí; si hay cambios sin commit o la rama base está por detrás, párate. Detalle en [ADR-0001](docs/decisions/ADR-0001-repositorios.md).

## Economía de contexto (tokens): para toda persona y agente

Cada turno reenvía todo el historial; lo que se lee una vez se paga en cada turno siguiente. Reglas:

- **Modelo y esfuerzo al empezar, nunca a mitad de tarea.** El repo fija por defecto `opus` con esfuerzo `medium` en `.claude/settings.json` (Fable solo lo cargan las skills SDD de diseño: `sdd-spec`, `sdd-plan`, `sdd-validate`, `sdd-change`). Cambiar de modelo a mitad de sesión reprocesa todo el historial sin caché.
- **Abre la sesión dentro del repo**, no en la carpeta padre del workspace: la caché es por directorio y los ajustes del proyecto solo aplican dentro del repo.
- **Nunca vuelques archivos grandes al contexto**: casos dorados `docs/reference/golden/*.json` (hasta 180 KB cada uno), exports, volcados, `package-lock`, salidas de `git log -p`. Resume con `jq`, `head`, `wc` o `grep`, o delega la lectura a un subagente y quédate con la conclusión.
- **Revisar un PR**: primero `gh pr view N --json files`, después el diff por archivo y sin datos: `git diff base...rama -- . ":!docs/reference/golden"`. Los JSON dorados están marcados en `.gitattributes` para no aparecer en los diffs; míralos a propósito con `git diff --text` solo cuando toque.
- **Compacta en los límites naturales** (`/compact` al cerrar una tarea), no cuando salte la compactación automática a mitad de una.
- **Comprueba el consumo** con `/usage` (línea "Prompt cache (main)": ratio de aciertos y causa probable del último fallo) y `/context`.

## Al terminar cualquier tarea

- Ejecuta las comprobaciones de [`docs/sdd/README.md`](docs/sdd/README.md) → "Checklist de calidad" que apliquen.
- Resume en tu respuesta qué archivos cambiaste y qué marcadores quedan abiertos.
