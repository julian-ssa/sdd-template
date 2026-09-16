# El método SDD en este repositorio

Spec-Driven Development (SDD), variante **spec-anchored**: la spec acompaña al
código siempre y se mantiene sincronizada. Origen: el método de Brais Moure
(`hello-sdd`), adaptado a productos multi-repo y a equipos que usan distintos
agentes de IA.

## El ciclo

```
0. Constitución     una vez por producto        docs/constitution.md
1. Spec             el QUÉ y el POR QUÉ          specs/NNN-nombre/spec.md   (EARS, RF-n)
2. Clarificación    bucle de preguntas           misma spec, marcadores [NECESITA ACLARACIÓN] → 0
3. Plan             el CÓMO                      specs/NNN-nombre/plan.md
4. Tareas           pasos pequeños verificables  specs/NNN-nombre/tasks.md  ([A]/[H]/[M])
5. Implementación   una tarea, tests primero     repo de código
6. Validación       criterios vs código          veredicto RF por RF
7. Cambio           primero la spec, luego el código
```

Reglas de oro:

- Si no está en la spec, no se implementa. Si falta una decisión, se pregunta.
- Un hueco visible (`[NECESITA ACLARACIÓN]`) es información; una suposición silenciosa es deuda.
- Las tareas humanas existen: etiquétalas. Un agente no puede crear una cuenta en un proveedor ni firmar un contrato.

## Cómo ejecutar cada fase desde cualquier agente

Las instrucciones canónicas de cada fase están en `.agents/skills/<nombre>/SKILL.md`
(formato *Agent Skills*: Markdown con frontmatter `name` y `description`). Son texto
plano sin comandos propietarios, así que sirven de tres formas:

| Herramienta | Cómo |
|---|---|
| Claude Code | `.claude/skills/` enlaza a las canónicas → `/sdd-spec 003`, `/sdd-plan 003`… |
| opencode | `.opencode/skill/` enlaza a las canónicas → misma invocación. |
| Codex, Cursor, Gemini CLI, Jules, otros con soporte de skills | Apunta la herramienta a `.agents/skills/` (o crea un enlace simbólico a esa carpeta en la ruta que espere). |
| Cualquier LLM sin skills (chat web, xAI, API propia) | Pega [`AGENTS.md`](../../AGENTS.md), [`docs/constitution.md`](../constitution.md) y el `SKILL.md` de la fase, o el prompt corto de [`docs/sdd/prompts.md`](prompts.md). |

Adaptadores nuevos: un enlace simbólico por herramienta, añadido aquí. Nunca se
copia el contenido de una skill: `SKILL.md` en `.agents/skills/` es la única fuente.

> **Una sola copia.** `.claude/skills/sdd-*` y `.opencode/skill/sdd-*` son enlaces
> simbólicos (`ls -la` los muestra con `->`). Edita siempre `.agents/skills/<nombre>/SKILL.md`;
> los enlaces reflejan el cambio al instante y git los guarda como enlaces, no como copias.
> Si un sistema de archivos no admite enlaces (Windows sin `core.symlinks`), borra las
> carpetas de adaptador y configura la herramienta para leer `.agents/skills/` directamente.

## Skills

| Skill | Fase(s) | Entrada | Salida |
|---|---|---|---|
| `sdd-spec` | Spec + clarificación | idea o `NNN` existente; `--aclarar` para el pase de QA | `spec.md`, [`specs/README.md`](../../specs/README.md) |
| `sdd-plan` | Plan + tareas | `NNN` con spec aprobada; [ADR-0002](../decisions/ADR-0002-stack.md) decidido | `plan.md`, `tasks.md` |
| `sdd-implement` | Implementación | `NNN Tn` | código + tests; `tasks.md` marcada |
| `sdd-run` | Lote de tareas sin supervisión | `NNN Ta Tb`; autorización explícita | rama + pull request con informe; ver [`ejecucion-desatendida.md`](ejecucion-desatendida.md) |
| `sdd-validate` | Validación | `NNN` | informe RF → test → resultado; estado en [`specs/README.md`](../../specs/README.md) |
| `sdd-change` | Cambio | `NNN` + nuevo requisito | spec actualizada (diff), luego plan/tareas |

## Checklist de calidad (mecánica)

Ejecuta lo que aplique al terminar una tarea. Desde la raíz del repo:

```bash
# Secciones obligatorias en cada spec
for f in specs/[0-9]*/spec.md; do for h in "## Contexto y objetivo" "## Actores" "## Historias de usuario" "## Requisitos funcionales" "## Requisitos no funcionales" "## Casos límite" "## Fuera de alcance" "## Dependencias" "## Criterios de finalización" "## Dudas abiertas"; do grep -q "^$h" "$f" || echo "FALTA '$h' en $f"; done; done
# RF únicos por spec
for f in specs/[0-9]*/spec.md; do grep -oE "^- RF-[0-9]+" "$f" | sort | uniq -d | sed "s|^|DUPLICADO en $f: |"; done
# Todo RF en EARS
grep -nE "^- RF-[0-9]+:" specs/[0-9]*/spec.md | grep -vE "CUANDO|SI .*ENTONCES|MIENTRAS|DONDE|EL SISTEMA" || true
# Sin stack en specs
grep -rniE "postgres|react|next\.js|prisma|express|nest|fastapi|python|streamlit|typescript|node\.js" specs/ || true
# Sin datos personales
grep -rnE "<patrón de identificadores o teléfonos reales del proyecto>" docs specs .agents || true
# Marcadores por spec (debe coincidir con specs/README.md)
grep -c "NECESITA ACLARACIÓN" specs/[0-9]*/spec.md
# Enlaces: rotos y referencias a archivos sin enlace (`--fix` los convierte en enlaces relativos)
python3 tools/links.py --check
```

## Convenciones de nombres

- `specs/NNN-nombre-en-kebab-case/` - tres dígitos, la siguiente libre.
- `docs/decisions/ADR-NNNN-tema.md` - cuatro dígitos. Estados: `propuesta`, `aceptada`, `pendiente`, `reemplazada por ADR-x`.
- Ids: `RF-n` (funcional, por spec), `RNF-n` (no funcional, catálogo global), `H-n` (historia), `T-n` / `P-n` (tarea / prerrequisito).
