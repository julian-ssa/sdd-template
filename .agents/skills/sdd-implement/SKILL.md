---
name: sdd-implement
description: Usa esta skill cuando el usuario pida implementar una tarea concreta (Tn) de specs/NNN-nombre/tasks.md. Implementa SOLO esa tarea, tests primero, ejecuta la suite, marca la casilla únicamente si su "Hecho cuando" se cumple y se detiene. Si la tarea es [H] la devuelve al humano; si es [M] hace la parte del agente y lista lo que falta.
---

# sdd-implement - una tarea, tests primero

Argumentos: `NNN Tn` (spec y tarea). Se ejecuta desde el **repo de código**, con el
repo de specs clonado como hermano en `../<proyecto>-specs` (si no está, clónalo ahí antes).

## Antes de empezar

1. Lee en `../<proyecto>-specs`: `AGENTS.md`, `docs/constitution.md`, `specs/NNN-*/spec.md`,
   `plan.md` y `tasks.md`. Lee el `AGENTS.md` del repo de código (comandos de test, lint, estructura).
2. Comprueba que todas las tareas de las que depende Tn están marcadas. Si no, párate y dilo.
3. Mira la etiqueta de Tn:
   - `[H]`: **no la hagas**. Explica qué debe hacer la persona, con qué recurso de
     [`docs/sdd/recursos-externos.md`](../../../docs/sdd/recursos-externos.md), y párate.
   - `[M]`: haz solo la parte del agente. Al terminar, lista con precisión qué falta
     de la persona (variable, dato, decisión) y **no marques la tarea**.
   - `[A]`: continúa.

## Implementación

1. **Tests primero.** Escribe el test que demuestra el RF de la tarea; su nombre o
   descripción incluye el id `RF-n`. Ejecútalo y confirma que falla.
2. Implementa lo mínimo para ponerlo en verde, siguiendo `plan.md`. Nada que no esté
   en la spec. Si descubres que la spec o el plan no cubren algo, **párate** y
   propón `sdd-change`; no improvises.
3. Respeta la constitución: dominio sin interfaz, dinero y fechas tipados, `as_of`
   explícito, alcance por inquilino u organización en toda consulta si aplica, sin datos personales en logs.
4. Ejecuta la suite completa con el comando del [`AGENTS.md`](../../../AGENTS.md) del repo de código y
   muestra el resultado literal.

## Al terminar

- Marca `Tn` en `tasks.md` **solo si** su "Hecho cuando" se cumple de forma
  observable (pega la evidencia: salida del test o del comando).
- Indica qué RF cubre, qué archivos cambiaste y **PÁRATE**. No empieces la siguiente tarea.
