---
name: sdd-spec
description: Usa esta skill cuando el usuario pida crear, redactar, revisar o clarificar la especificación (spec) de una funcionalidad. Guía una entrevista de requisitos y produce o corrige specs/NNN-nombre/spec.md en notación EARS siguiendo la plantilla del repositorio. Con "--aclarar" ejecuta el pase de QA y resuelve los marcadores [NECESITA ACLARACIÓN].
model: fable
---

# sdd-spec - redactar y clarificar una spec

Convierte una idea vaga en una especificación acordada. La spec es el contrato:
si algo no está aquí, no se implementa.

Argumentos: `NNN` (número de spec existente o el siguiente libre) y, opcionalmente,
`--aclarar` para el modo clarificación.

## Antes de empezar

0. `git checkout main && git pull` en el repo de specs y crea una rama (`spec-NNN/...` o `docs/...`);
   el resultado se entrega como pull request contra `main`, nunca directo.

1. Lee [`AGENTS.md`](../../../AGENTS.md), [`docs/constitution.md`](../../../docs/constitution.md), [`docs/product/glossary.md`](../../../docs/product/glossary.md) y
   [`docs/product/requisitos-transversales.md`](../../../docs/product/requisitos-transversales.md).
2. Lee las specs previas de `specs/` para respetar convenciones y no contradecir lo acordado.
3. Si el dominio depende de un sistema externo, lee su contrato en `docs/reference/`.

## Modo redacción (sin `--aclarar`)

1. **Entrevista.** Preguntas de **UNA en UNA**, máximo 6, esperando respuesta antes
   de la siguiente. Céntrate en casos límite, comportamiento ante errores, permisos
   por rol y qué queda fuera. No propongas soluciones técnicas: si el usuario
   pregunta "¿cómo lo harías?", redirige al QUÉ. Prioriza preguntas cuya respuesta
   cambie lo que hay que construir; descarta las de respuesta obvia.
2. **Número y carpeta.** Usa `specs/NNN-<nombre-en-kebab-case>/spec.md` con el
   siguiente número libre de tres dígitos.
3. **Redacta** con [`specs/_templates/spec.md`](../../../specs/_templates/spec.md) sin saltarte secciones. Criterios de
   aceptación **siempre en EARS**, numerados RF-1, RF-2… sin reiniciar entre grupos.
   Cada requisito debe ser verificable: si no se te ocurre cómo comprobarlo, está
   mal escrito. Usa solo términos del glosario.
4. **Marca lo que no sepas** como `[NECESITA ACLARACIÓN: pregunta concreta]` y
   lístalo en "Dudas abiertas" con quién debe responder. Nunca rellenes un hueco
   inventando.
5. **Actualiza [`specs/README.md`](../../../specs/README.md)**: fila de la spec, estado, dependencias y número de marcadores.
6. **Pide aprobación explícita.** No pases al plan ni escribas código sin ella.

## Modo clarificación (`--aclarar`)

No reescribas la spec de entrada. Primero **detecta y lista**, numerado, en cinco bloques:
(1) ambigüedades, (2) contradicciones entre RF, (3) casos límite no cubiertos,
(4) conflictos con la constitución, (5) términos fuera del glosario.
Después, para cada marcador `[NECESITA ACLARACIÓN]`, pregunta al usuario de una en
una. Con cada respuesta: edita el RF afectado, elimina el marcador, anota la
decisión en "Cambios" si la spec ya estaba aprobada. Termina actualizando el
recuento de marcadores en la cabecera de la spec y en [`specs/README.md`](../../../specs/README.md).

## Reglas

- La spec describe **QUÉ** y **POR QUÉ**. Prohibido incluir stack, arquitectura,
  nombres de archivos, tablas, endpoints, algoritmos o firmas: eso va en el plan.
- Incluye **siempre** "Fuera de alcance" y enlaza cada exclusión al roadmap o a otra spec.
- Un requisito, una frase. Si necesitas un "y" para unir dos comportamientos, son dos requisitos.
- Sin adjetivos no medibles: "rápido", "intuitivo", "robusto" no son requisitos. Escribe el umbral o no lo escribas.
- Los requisitos no funcionales se citan por id `RNF-n`; no se redactan de nuevo.
- Todo dato de ejemplo es ficticio. Nunca identificadores, nombres, teléfonos ni correos reales de personas u organizaciones.
- Idioma: el de la constitución (español para specs).

## Notación EARS

| Patrón | Forma | Cuándo |
|---|---|---|
| Ubicuo | EL SISTEMA \<hará\> | siempre cierto |
| Dirigido por evento | CUANDO \<disparador\>, EL SISTEMA \<hará\> | responde a algo |
| Estado | MIENTRAS \<estado\>, EL SISTEMA \<hará\> | durante una condición |
| Opcional | DONDE \<característica\>, EL SISTEMA \<hará\> | solo si está presente |
| No deseado | SI \<condición\>, ENTONCES EL SISTEMA \<hará\> | errores y casos límite |

Bien escrito:

> RF-4: SI el archivo importado pertenece a una cuenta que no está vinculada a ningún cliente de la organización del usuario, ENTONCES EL SISTEMA rechazará la importación y registrará el intento con fecha, usuario e identificador de la cuenta.

Mal escrito:

> ~~RF-4: El sistema debe manejar bien los archivos ajenos y ser seguro.~~
> Sin patrón EARS, sin criterio verificable, dos ideas en una frase y un adjetivo no medible.

## Al terminar

Ejecuta la "Checklist de calidad" de [`docs/sdd/README.md`](../../../docs/sdd/README.md) sobre la spec tocada y
resume: archivo, número de RF, marcadores abiertos y qué necesita el humano.
