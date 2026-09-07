# sdd-template

Plantilla para arrancar cualquier proyecto de software a medida con **Spec-Driven
Development (SDD)** y agentes de IA intercambiables (Claude Code, Codex, Cursor,
opencode, Gemini CLI, chat plano…). Nace del repo `cuadranta-specs` y del método de
Brais Moure (`hello-sdd`).

Lo que trae:

| Pieza | Para qué |
|---|---|
| [`AGENTS.md`](AGENTS.md) (+ [`CLAUDE.md`](CLAUDE.md) = `@AGENTS.md`) | Contexto canónico para cualquier agente, con placeholders `{{…}}`. |
| [`docs/constitution.md`](docs/constitution.md) | Plantilla de principios verificables, cada uno con "Se verifica". |
| `docs/sdd/` | El método en una página, prompts por fase y registro de recursos externos. |
| `docs/product/` | Plantillas de visión, glosario bilingüe, modelo de dominio, RNF y roadmap. |
| `docs/reference/` | Dónde documentar sistemas previos y contratos externos (con el commit leído). |
| `docs/decisions/` | Plantilla de ADR y los dos ADR que todo proyecto necesita (repos, stack). |
| `specs/_templates/` | Plantillas de `spec.md` (EARS), `plan.md` y `tasks.md` (con `[A]/[H]/[M]`). |
| `.agents/skills/` | Cinco skills SDD canónicas; `.claude/skills` y `.opencode/skill` son enlaces. |
| `new-project.sh` | Crea un repo nuevo a partir de esta plantilla y sustituye los placeholders. |

## Crear un proyecto nuevo

```bash
./new-project.sh <nombre-kebab> <ruta-destino> ["Descripción corta"]
# ejemplo:
./new-project.sh gestor-proyectos ~/Coding/clients/acme "Herramienta de gestión de proyectos para equipos pequeños"
```

Crea `<ruta-destino>/<nombre>-specs/` con git inicializado y un primer commit. Después:

1. Rellena los `{{…}}` que queden (`grep -rn "{{" .`).
2. Escribe la constitución con el prompt de [`docs/sdd/prompts.md`](docs/sdd/prompts.md) (o edita la plantilla).
3. Rellena glosario y modelo de dominio antes de la primera spec.
4. `sdd-spec 001` para la primera funcionalidad. Plan y tareas solo cuando [`ADR-0002-stack.md`](docs/decisions/ADR-0002-stack.md) esté decidido.

## Cómo lo consumen los repos de código

Los repos de código se clonan como hermanos del repo de specs en la misma carpeta (el
workspace), sin submódulos, y enlazan las skills:

```bash
cd <workspace>
git clone <url-del-repo-specs>
git clone <url-del-repo-de-codigo>
cd <repo-de-codigo> && mkdir -p .agents && ln -s ../../<proyecto>-specs/.agents/skills .agents/skills
```

El `AGENTS.md` de cada repo de código dice que las specs están en `../<proyecto>-specs`.

## Mantener la plantilla

Las mejoras al método (skills, plantillas, checklist) se hacen aquí y se copian a los
proyectos que lo necesiten. Las skills tienen **una sola copia** en `.agents/skills/`; el
resto son enlaces.
