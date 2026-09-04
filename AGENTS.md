# AGENTS.md — {{PROYECTO}}-specs

Contexto canónico para cualquier agente de código o LLM (Claude Code, Codex, Cursor,
Gemini CLI, opencode, Jules, xAI, chat plano…). `CLAUDE.md` solo contiene `@AGENTS.md`;
el resto de herramientas leen este archivo directamente. Si tu herramienta no lo carga
sola, pega su contenido al inicio de la sesión.

## Proyecto

**{{PROYECTO}}** — {{DESCRIPCIÓN EN 2–3 FRASES: qué es, para quién, qué problema resuelve}}.
Visión, actores y alcance: `docs/product/overview.md`. Modelo de dominio: `docs/product/domain-model.md`.

Este repositorio es la **fuente de verdad del producto**: constitución, specs, decisiones
y documentación. No contiene código de aplicación.

## Estado del proyecto ({{FECHA}})

- Fase: **solo specs**. Stack de implementación **pendiente** → `docs/decisions/ADR-0002-stack.md`.
- Prohibido crear `apps/`, `packages/`, `src/` o cualquier código aquí.
- Prohibido ejecutar la fase de plan (`sdd-plan`) mientras ADR-0002 esté `pendiente`.
- Tras la decisión de stack se crearán los repos de código (ver ADR-0001); cada uno tendrá
  este repo como submódulo en `sdd/`.

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
| `docs/constitution.md` | Principios innegociables. Léelo antes de cualquier tarea. |
| `docs/sdd/` | El método: `README.md` (cómo trabajar), `prompts.md` (prompts por fase, para cualquier LLM), `recursos-externos.md` (accesos y quién los tiene). |
| `docs/product/` | Visión, glosario, modelo de dominio, requisitos transversales (RNF), roadmap/backlog. |
| `docs/reference/` | Lo que ya existe y se porta o integra: sistemas previos, fórmulas, contratos externos. |
| `docs/decisions/` | ADRs. Una decisión por archivo. |
| `specs/` | Una carpeta por funcionalidad: `NNN-nombre/spec.md` (+ `plan.md`, `tasks.md` cuando toque). Índice y estado en `specs/README.md`. |
| `.agents/skills/` | Skills SDD canónicas (formato Agent Skills: `SKILL.md` con `name`/`description`). `.claude/skills` y `.opencode/skill` son enlaces simbólicos a ellas. |

## Convenciones de specs

- Carpeta `specs/NNN-nombre-en-kebab-case/`, numeración de tres dígitos, la siguiente libre.
- `spec.md` sigue `specs/_templates/spec.md` sin saltar secciones.
- Requisitos funcionales numerados `RF-n` (únicos dentro de la spec) en notación **EARS**:
  `CUANDO … , EL SISTEMA …` · `SI … , ENTONCES EL SISTEMA …` · `MIENTRAS … , EL SISTEMA …` ·
  `DONDE … , EL SISTEMA …` · `EL SISTEMA …`.
- Un requisito, una frase, verificable. Sin adjetivos no medibles.
- Lo que no se sabe se marca `[NECESITA ACLARACIÓN: pregunta concreta]` y se lista en "Dudas abiertas".
- Requisitos no funcionales: se citan por id `RNF-n` desde `docs/product/requisitos-transversales.md`.
- Términos de dominio: los del glosario `docs/product/glossary.md`. No inventes sinónimos.
- La spec describe el QUÉ y el POR QUÉ. Nada de stack, arquitectura, tablas, endpoints ni nombres de archivo.
- Idiomas: specs, docs y mensajes al usuario en **{{idioma de specs}}**; identificadores, esquema y commits de código en **inglés**.
- `tasks.md` etiqueta cada tarea `[A]` (agente), `[H]` (humano) o `[M]` (mixta) y abre con "Prerrequisitos humanos".

## Flujo SDD

Fases y skill que las ejecuta (detalle en `docs/sdd/README.md`; prompt equivalente en `docs/sdd/prompts.md`):

| Fase | Skill | Produce |
|---|---|---|
| Spec y clarificación | `sdd-spec` | `specs/NNN-*/spec.md` |
| Plan y tareas | `sdd-plan` | `plan.md` + `tasks.md` (bloqueado hasta ADR-0002) |
| Implementación de una tarea | `sdd-implement` | código + tests, en el repo de código |
| Validación de una spec | `sdd-validate` | veredicto RF por RF |
| Cambio de requisito | `sdd-change` | spec actualizada primero, luego plan y tareas |

## Recursos externos

Registro completo con propietario y si un agente puede usarlo: `docs/sdd/recursos-externos.md`.
Si una tarea necesita una credencial, cuenta o acceso que no tienes, **no la simules**:
márcala `[H]` o `[M]` y párate.

## Reglas

1. Lee `docs/constitution.md` y la spec activa antes de escribir nada.
2. No inventes stack ni arquitectura mientras ADR-0002 esté pendiente.
3. No modifiques el material de referencia del workspace. Es solo lectura.
4. Nunca copies a este repo datos personales reales. Los ejemplos usan valores ficticios.
5. Si un marcador `[NECESITA ACLARACIÓN]` bloquea un requisito, pregunta; no rellenes el hueco con una suposición silenciosa.
6. Toda decisión que cambie el modelo de dominio o los permisos requiere un ADR nuevo, no una edición silenciosa.
7. Actualiza `specs/README.md` (estado y número de marcadores) cada vez que toques una spec.

## Al terminar cualquier tarea

- Ejecuta las comprobaciones de `docs/sdd/README.md` → "Checklist de calidad" que apliquen.
- Resume en tu respuesta qué archivos cambiaste y qué marcadores quedan abiertos.
