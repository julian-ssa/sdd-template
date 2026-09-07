---
name: sdd-validate
description: Usa esta skill cuando el usuario pida validar, auditar o dar el veredicto de una spec implementada. Recorre cada RF, indica qué test lo cubre y su resultado, comprueba los "Se verifica" de la constitución que apliquen y actualiza el estado en specs/README.md.
---

# sdd-validate - veredicto RF por RF

Argumento: `NNN`. Se ejecuta desde el repo de código con este repo en `sdd/`.

## Proceso

1. Lee `sdd/docs/constitution.md`, `sdd/specs/NNN-*/spec.md`, `plan.md` y `tasks.md`.
2. Ejecuta la suite completa y guarda la salida.
3. Para **cada RF**, en orden: qué test lo cubre (archivo y nombre; debe contener el
   id `RF-n`), resultado (verde / rojo / sin test). Un RF sin test es un fallo, no
   una nota.
4. Para cada tarea de `tasks.md`: ¿está marcada? ¿se cumple su "Hecho cuando"? Las
   `[H]` y `[M]` pendientes se listan aparte como bloqueos humanos.
5. Recorre los principios de la constitución cuya línea "Se verifica" aplique a esta
   spec y ejecuta la comprobación (grep, consulta, test). Anota resultado.
6. Comprueba los "Criterios de finalización" de la spec y los RNF citados.
7. **Veredicto**: `cumplida`, `cumplida con bloqueos humanos` (lista) o `no cumplida` (lista de RF/tareas).

## Al terminar

- Actualiza [`specs/README.md`](../../../specs/README.md): estado (`implementada` solo con veredicto `cumplida`).
- No corrijas código en esta skill. Si hay fallos, propón la tarea o el `sdd-change` correspondiente.
