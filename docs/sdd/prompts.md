# Prompts por fase (para cualquier LLM)

Equivalentes cortos de las skills de `.agents/skills/`. Úsalos cuando la herramienta
no soporte skills. Antes de cualquiera de ellos, carga [`AGENTS.md`](../../AGENTS.md) y
[`docs/constitution.md`](../constitution.md) en el contexto.

| Fase | Prompt |
|---|---|
| Constitución (una vez) | "Proponme [`docs/constitution.md`](../constitution.md) para este producto: entre 6 y 12 principios cortos y verificables sobre spec↔código, dominio sin interfaz, datos y determinismo, permisos, tests, idiomas y seguridad (añade los propios del dominio). Cada principio termina con una línea 'Se verifica: …'. Espera mi aprobación." |
| Spec (entrevista) | "NO escribas código. Vamos a redactar `specs/NNN-<nombre>/spec.md`. Lee [`docs/constitution.md`](../constitution.md), [`docs/product/glossary.md`](../product/glossary.md) y las specs previas. Hazme preguntas de UNA en UNA (máx. 6) sobre casos límite, errores y alcance. Después genera la spec con la plantilla [`specs/_templates/spec.md`](../../specs/_templates/spec.md): RF numerados en EARS, RNF citados por id, casos límite, fuera de alcance, dependencias, criterios de finalización y dudas marcadas `[NECESITA ACLARACIÓN]`. Solo el QUÉ y el POR QUÉ. Actualiza [`specs/README.md`](../../specs/README.md)." |
| Clarificación | "Revisa `specs/NNN-*/spec.md` como un QA profesional: (1) ambigüedades, (2) contradicciones entre RF, (3) casos límite ausentes, (4) conflictos con [`docs/constitution.md`](../constitution.md), (5) términos que no están en el glosario. Solo detecta, numerado. No propongas soluciones." |
| Plan | "Lee la constitución, [`docs/decisions/ADR-0002-stack.md`](../decisions/ADR-0002-stack.md) (debe estar decidido) y la spec. Sin código: genera `plan.md` con la plantilla: módulos, modelo de datos con alcance por organización, contratos, algoritmos con `as_of` explícito, decisiones justificadas con la alternativa descartada, estrategia de tests y tabla RF → módulo → test." |
| Tareas | "Divide el plan en `tasks.md` con la plantilla: tareas < 30 min, orden de dependencia, RF que cubre, 'Hecho cuando:' verificable. Etiqueta cada tarea `[A]`, `[H]` o `[M]` consultando [`docs/sdd/recursos-externos.md`](recursos-externos.md), y escribe primero el bloque 'Prerrequisitos humanos'." |
| Implementación | "Implementa SOLO la tarea Tn de `specs/NNN-*/tasks.md`, siguiendo `plan.md` y la constitución. Si es `[H]`, párate y dímelo. Si es `[M]`, haz tu parte y lista exactamente qué necesito hacer yo. Tests primero. Ejecuta la suite y muéstrame el resultado. Marca Tn solo si su 'Hecho cuando' se cumple. PÁRATE." |
| Validación | "Recorre `spec.md` RF por RF: qué test cubre cada uno y su resultado. Comprueba los 'Se verifica' de la constitución que apliquen. Veredicto: ¿spec cumplida? Actualiza el estado en [`specs/README.md`](../../specs/README.md)." |
| Cambio | "Nuevo requisito: <X>. NO toques código. Actualiza primero `spec.md` (nuevo RF en EARS + casos límite + entrada en 'Cambios') y muéstrame el diff. Solo después, plan y tareas." |
