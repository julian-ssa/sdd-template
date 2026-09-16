---
name: sdd-run
description: Usa esta skill cuando el usuario pida ejecutar varias tareas seguidas de una spec sin supervisión (por ejemplo "sdd-run 001 T2 T10", "avanza las tareas esta noche", "sigue con el lote"). Recorre las tareas en orden aplicando sdd-implement a cada una, siempre en una rama y nunca en main, con CI en verde como puerta y condiciones de parada estrictas; termina abriendo un pull request con el informe del lote.
model: opus
---

# sdd-run - un lote de tareas, sin supervisión

Argumentos: `NNN Ta Tb` (spec y rango de tareas, inclusive). Se ejecuta desde el **repo de
código**, con el repo de specs como hermano en `../<proyecto>-specs`. Solo se usa con
autorización explícita del propietario para ese lote; la regla por defecto de `sdd-implement`
(una tarea y parar) sigue vigente fuera de esta skill.

## Antes de empezar

1. Lee `AGENTS.md` y `docs/constitution.md` del repo de specs, el `AGENTS.md` del repo de código,
   `specs/NNN-*/plan.md` y `tasks.md`. El plan debe estar aprobado.
2. Comprueba que el árbol está limpio y `main` al día: `git status`, `git pull`.
3. Crea la rama `spec-NNN/Ta-Tb` desde `main`. **Nunca escribas en `main`.**
4. Comprueba que las dependencias de `Ta` están marcadas. Si no, párate.

## Por cada tarea, en orden

1. Si la tarea es `[H]`: párate. Si es `[M]`: haz la parte del agente, deja escrito qué falta de la
   persona, no la marques y párate. Solo las `[A]` continúan el lote.
2. Aplica **`sdd-implement`** completa: Context7 antes de cada librería (cita la consulta en el
   commit), Ponytail, tests primero con el id del RF, implementación mínima, suite completa.
3. Commit en la rama con el formato `spec NNN Tn (RF-x): <qué>` y push. Espera el resultado de CI
   del commit (`gh run watch` o consulta periódica).
4. CI en verde: marca la tarea en `tasks.md` del repo de specs (commit y evidencia), haz commit y
   push de ese cambio en el repo de specs, y pasa a la siguiente.
5. CI en rojo: analiza y corrige **como máximo dos veces**. Si sigue en rojo, párate.

## Condiciones de parada (obligatorias)

Detente, sin marcar la tarea, cuando ocurra cualquiera de estas:
- CI o la suite en rojo tras dos intentos de corrección.
- La siguiente tarea es `[H]` o `[M]`.
- La spec o el plan no cubren algo que la tarea necesita: no improvises; propón `sdd-change`.
- Una tarea exige un secreto, credencial o servicio externo que no está en el entorno.
- Un cambio tocaría algo fuera de la tarea (otro módulo, otra spec, la constitución).
- Se alcanzó `Tb`.

## Al terminar (por parada o por fin de lote)

1. Abre un **pull request** de la rama contra `main` con este informe:
   - Tareas completadas, con su commit y la evidencia del "Hecho cuando".
   - Tarea en la que se detuvo y el motivo exacto (salida del test o de CI, decisión que falta).
   - Consultas hechas en Context7 (biblioteca y tema) y dependencias añadidas, con su justificación.
   - Qué debe revisar la persona con más atención (cifrado, sesiones, migraciones, permisos).
2. No mezcles el PR. Lo mezcla el propietario tras revisarlo.
3. Deja `tasks.md` del repo de specs coherente con el PR: marcadas solo las tareas con CI en verde.

## Prohibido en este modo

Escribir en `main`; marcar tareas sin evidencia; saltar tareas; cambiar la spec, el plan o la
constitución; añadir dependencias sin justificación; ejecutar `[H]` o `[M]` como si fueran `[A]`;
tocar `.env` con secretos reales; continuar tras una condición de parada.
