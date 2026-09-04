---
name: sdd-change
description: Usa esta skill cuando aparezca un requisito nuevo, un cambio de alcance o una corrección sobre una spec ya aprobada. Actualiza primero la spec (RF en EARS, casos límite, sección Cambios), muestra el diff, y solo después propaga a plan y tareas. Nunca toca código.
---

# sdd-change — el cambio empieza por la spec

Argumentos: `NNN` y la descripción del cambio.

## Proceso

1. Lee `AGENTS.md`, `docs/constitution.md` y `specs/NNN-*/spec.md`.
2. Si el cambio afecta al modelo de dominio, a la tenencia multi-organización o a la
   visibilidad por rol, **primero** propone un ADR nuevo en `docs/decisions/` y
   espera aprobación.
3. Redacta el cambio en la spec:
   - Nuevos RF en EARS con el siguiente número libre (nunca renumeres los existentes).
   - RF modificados: edita el texto y anótalo.
   - RF retirados: márcalos `~~RF-n~~ (retirado el AAAA-MM-DD, ver Cambios)`; no los borres.
   - Casos límite nuevos y, si procede, "Fuera de alcance".
   - Entrada en "Cambios": fecha, RF afectados, motivo, quién lo pidió.
4. **Muestra el diff** de la spec y pide aprobación. No sigas sin ella.
5. Con aprobación: actualiza `plan.md` (módulos, cobertura RF) y `tasks.md` (tareas
   nuevas al final, etiquetadas `[A]/[H]/[M]`, sin reordenar las hechas).
6. Actualiza `specs/README.md` (estado vuelve a `aprobada`/`planificada`; marcadores).

## Reglas

- Nunca modifiques código en esta skill. La implementación va por `sdd-implement`.
- Un cambio "pequeño" sin spec es deuda: no existe la excepción.
