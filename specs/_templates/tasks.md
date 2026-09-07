# Tareas - Spec NNN

> Leyenda: `[A]` la hace el agente · `[H]` la hace un humano · `[M]` mixta (el agente necesita algo de un humano: credencial, cuenta, acceso, decisión).
> Cada tarea: < 30 min, ordenada por dependencia, con los RF que cubre y una línea "Hecho cuando:" verificable.
> Consulta [`docs/sdd/recursos-externos.md`](../../docs/sdd/recursos-externos.md) antes de etiquetar: si una tarea toca un recurso externo, es `[H]` o `[M]`.

## Prerrequisitos humanos
<Todo lo que debe existir ANTES de empezar. Sin esto el trabajo se para.>
- [ ] P1. [H] <credencial / cuenta / acceso / decisión> - quién: <persona> - necesario para: T?, T?.

## Tareas
- [ ] T1. [A] <qué>. (RF-x) Hecho cuando: <condición verificable>.
- [ ] T2. [M] <qué>. (RF-y) Humano: <qué aporta y cuándo>. Hecho cuando: <condición verificable>.
- [ ] T3. [H] <qué>. (RF-z) Hecho cuando: <condición verificable>.

## Tareas transversales fijas
- [ ] TX-1. [A] Todo texto visible pasa por la capa de i18n (RNF-i18n). Hecho cuando: no hay cadenas de UI literales en el código.
- [ ] TX-2. [A] Cada RF aparece en el nombre o descripción de al menos un test. Hecho cuando: `sdd-validate` no reporta RF sin test.
