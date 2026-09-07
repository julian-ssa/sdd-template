# Glosario

Términos de dominio con su equivalente en inglés (identificadores de código). Las specs
usan **solo** estos términos. Si falta uno, se añade aquí antes de usarlo.

## Método (SDD)

| Término | Código (EN) | Definición |
|---|---|---|
| SDD | `spec-driven development` | Desarrollo dirigido por especificación: constitución → spec → clarificación → plan → tareas → implementación → validación → cambio. Guía en [`docs/sdd/README.md`](../sdd/README.md). |
| Constitución | `constitution` | Principios innegociables del producto, cada uno con su forma de verificarse. [`docs/constitution.md`](../constitution.md). |
| Spec | `spec` | Especificación de una funcionalidad: el QUÉ y el POR QUÉ, sin tecnología. `specs/NNN-nombre/spec.md`. |
| ADR | `architecture decision record` | Registro de una decisión de arquitectura o producto: contexto, decisión, consecuencias y alternativas descartadas. `docs/decisions/ADR-NNNN-tema.md`. |
| RF | `functional requirement` | Requisito funcional: una frase verificable en notación EARS, numerada `RF-n` dentro de cada spec. Las tareas y los tests citan su id. |
| RNF | `non-functional requirement` | Requisito no funcional transversal (sesión, rendimiento, accesibilidad…), numerado `RNF-n` en un catálogo único: [`docs/product/requisitos-transversales.md`](requisitos-transversales.md). |
| EARS | `EARS notation` | Patrones para escribir requisitos sin ambigüedad: CUANDO…, SI… ENTONCES…, MIENTRAS…, DONDE…, EL SISTEMA… |
| Historia de usuario | `user story` | "Como <rol> quiero <acción> para <beneficio>", numerada `H-n`; agrupa los RF. |
| Marcador de aclaración | `clarification marker` | `[NECESITA ACLARACIÓN: pregunta]`: hueco visible en una spec que alguien debe responder antes de aprobarla. |
| Plan | `plan` | El CÓMO de una spec: módulos, datos, contratos, decisiones justificadas y estrategia de tests. Solo tras decidir el stack ([ADR-0002](../decisions/ADR-0002-stack.md)). |
| Tarea | `task` | Paso de menos de 30 minutos, numerado `T-n`, con RF que cubre y "Hecho cuando". Etiquetada `[A]` agente, `[H]` humano o `[M]` mixta. |
| Prerrequisito humano | `human prerequisite` | `P-n`: credencial, cuenta, dato o decisión que debe existir antes de empezar las tareas. |
| Skill | `skill` | Instrucciones reutilizables para un agente de IA que ejecutan una fase (`sdd-spec`, `sdd-plan`, `sdd-implement`, `sdd-validate`, `sdd-change`). Una sola copia en `.agents/skills/`. |
| Golden test | `golden test` | Test que compara un cálculo con un resultado conocido y documentado (ejemplo dorado en `docs/reference/`). |

## {{Área 1}}
| Término | Código (EN) | Definición |
|---|---|---|
| {{término}} | `{{identifier}}` | {{definición en una frase}} |

## {{Área 2}}
| Término | Código (EN) | Definición |
|---|---|---|
| | | |
