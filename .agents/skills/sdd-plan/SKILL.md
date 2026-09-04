---
name: sdd-plan
description: Usa esta skill cuando el usuario pida el plan técnico o las tareas de una spec aprobada. Genera specs/NNN-nombre/plan.md y tasks.md en un solo pase, etiquetando cada tarea como [A] agente, [H] humano o [M] mixta, y escribiendo primero los prerrequisitos humanos. Se niega a ejecutarse si la decisión de stack (ADR-0002) sigue pendiente.
---

# sdd-plan — plan técnico y tareas

Argumento: `NNN` (spec con estado `aprobada` y cero marcadores abiertos).

## Antes de empezar

1. Lee `AGENTS.md`, `docs/constitution.md` y `docs/decisions/ADR-0002-stack.md`.
   **Si ADR-0002 está `pendiente`, párate** y dilo: sin stack no hay plan.
2. Lee `specs/NNN-*/spec.md`. Si tiene marcadores `[NECESITA ACLARACIÓN]` o no está
   aprobada, párate y propón ejecutar `sdd-spec NNN --aclarar` primero.
3. Lee `docs/product/domain-model.md`, `docs/reference/computations.md` (si hay
   cálculos), los contratos externos que la spec cite y `docs/sdd/recursos-externos.md`.
4. Lee los `plan.md` de las specs de las que esta depende para reutilizar módulos y no duplicar.

## Plan (`plan.md`)

Usa `specs/_templates/plan.md`. Sin código. Contiene:

- Estructura de módulos con los RF que cubre cada uno. Respeta "Dominio sin interfaz".
- Modelo de datos con alcance por organización en toda entidad de negocio, claves
  naturales, y la migración como código.
- Contratos (API, eventos, archivos) con los RF que cubren.
- Algoritmos en pseudocódigo, con fecha de valoración explícita y referencia a la fórmula documentada.
- Decisiones técnicas justificadas, **cada una con la alternativa descartada** y el
  principio o ADR que la respalda.
- Estrategia de tests: unitarios de dominio con fechas inyectadas, contratos, golden tests.
- Tabla de cobertura RF → módulo → test. Ningún RF puede quedar sin fila.

## Tareas (`tasks.md`)

Usa `specs/_templates/tasks.md`.

1. **Primero "Prerrequisitos humanos"**: recorre `docs/sdd/recursos-externos.md` y
   la spec; todo acceso, credencial, cuenta, dato de prueba o decisión que no
   exista aún es un `P-n [H]` con responsable y las tareas que bloquea.
2. Divide el plan en tareas de **menos de 30 minutos**, en orden de dependencia,
   cada una con sus RF y una línea "Hecho cuando:" verificable (un test en verde,
   un comando que devuelve X, un archivo que existe).
3. Etiqueta cada tarea:
   - `[A]` el agente la completa solo con lo que hay en el repo y en el entorno de desarrollo.
   - `[H]` la hace una persona (crear una cuenta, registrar un dominio, aprobar un texto legal, obtener un export real).
   - `[M]` el agente hace su parte pero necesita algo de una persona (una credencial en `.env`, una decisión, un dato real). Indica qué aporta el humano y cuándo.
   Si dudas entre `[A]` y `[M]`, es `[M]`: la tarea que se bloquea a mitad cuesta más que la que se anuncia.
4. Mantén las tareas transversales fijas de la plantilla (i18n, RF ↔ test).

## Al terminar

- Actualiza `specs/README.md` (estado `planificada`, número de tareas y de `[H]`/`[M]`).
- Pide aprobación explícita antes de implementar nada.
