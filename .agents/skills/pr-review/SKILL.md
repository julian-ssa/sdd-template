---
name: pr-review
description: Usa esta skill para revisar un pull request o auditar un repo de código de forma independiente y sin modificar archivos (por ejemplo "pr-review: PR 20, base origin/develop" o "pr-review en modo auditoría, áreas 1 a 4"). Pensada para un modelo distinto del que escribió el código, como GPT-6.1 Sol con esfuerzo xhigh en Codex, para evitar el sesgo de revisarse a sí mismo. Contrasta el diff con la spec, el plan, la constitución y los ADR, consulta Context7 y aplica Ponytail, y entrega un informe con formato fijo que otro agente pueda verificar hallazgo por hallazgo.
---

# pr-review - revisión independiente de un pull request

Segunda opinión sobre el trabajo de otro agente o persona. La hace un modelo distinto del que
escribió el código: si lo revisa el mismo modelo, comparte sus puntos ciegos. La revisión **no
modifica nada**: lee, ejecuta comprobaciones que no escriben y entrega un informe. Corregir es
otra tarea, en la rama del PR, después de verificar cada hallazgo.

## Cómo lanzarla (Codex con GPT-6.1 Sol, esfuerzo xhigh)

Una vez por máquina, en `~/.codex/config.toml` (configuración de la persona, nunca en el repo):

```toml
[profiles.review]
model = "gpt-6.1-sol"
model_reasoning_effort = "xhigh"

[mcp_servers.context7]
url = "https://mcp.context7.com/mcp"
bearer_token_env_var = "CONTEXT7_API_KEY"
startup_timeout_sec = 20
tool_timeout_sec = 120
```

`CONTEXT7_API_KEY` debe estar exportada en la terminal que lanza Codex (`echo ${CONTEXT7_API_KEY:+definida}`).

Cada revisión, desde la carpeta del repo de código, con `../{{PROYECTO}}-specs` actualizado:

```bash
git -C ../{{PROYECTO}}-specs fetch origin && git -C ../{{PROYECTO}}-specs checkout main && git -C ../{{PROYECTO}}-specs pull
git fetch origin && git checkout <rama del PR> && git pull
codex exec -p review --sandbox read-only -o ~/review-<N>.md "Usa la skill pr-review: PR <N>, base origin/<rama base>"
```

- **Base**: la rama contra la que se mezclará el PR. Si la rama del PR salió de otra rama que aún no
  está mezclada, la base es esa otra (`origin/<rama>`), para revisar solo lo propio.
- **Auditoría del repo entero**: `"Usa la skill pr-review en modo auditoría, áreas 1 a 4"` y, en otra
  ejecución, `"áreas 5 a 9"`. Partirla en dos evita agotar la cuota en planes con límite por ventana.
- `--sandbox read-only` deja el repo intacto y sin red para los comandos; Context7 funciona porque
  es un servidor MCP que lanza Codex, fuera del sandbox. Por eso la base la da la persona: sin red
  no se puede consultar GitHub.
- El informe (`-o`) se entrega al agente que corrige, que verifica cada hallazgo contra el código
  antes de cambiar nada.

## Entrada

- **Modo PR**: `PR <N>, base origin/<rama>`. Alcance: `git diff origin/<rama>...HEAD`.
- **Modo auditoría**: `auditoría, áreas <a> a <b>`. Alcance: todo el código de la rama actual.
- Si falta la base en modo PR, no la adivines: indícalo al principio del informe y usa
  `origin/develop`, diciendo que lo supusiste.

## Antes de revisar

1. Estado: `git status` (debe estar limpio), `git branch --show-current`, `git rev-parse --short HEAD`.
   En modo PR: `git log --oneline <base>..HEAD` y `git diff --stat <base>...HEAD`.
2. Contexto, en este orden: `AGENTS.md` del repo; [`AGENTS.md` del repo de specs](../../../AGENTS.md);
   [`docs/constitution.md`](../../../docs/constitution.md); la spec, el plan y `tasks.md` de las
   tareas que cita la rama o sus commits (`spec NNN Tn`); los ADR que esos documentos citen. Un repo
   sin `AGENTS.md` se rige por el de specs y por su contrato en `docs/reference/`.
3. **Copia de specs desactualizada**: si una tarea citada en los commits no aparece en `tasks.md`,
   o aparece sin marcar cuando los commits dicen que se hizo, la copia de `../{{PROYECTO}}-specs`
   puede estar atrasada o la casilla puede estar en un PR de specs sin mezclar. Dilo en
   "Limitaciones"; no lo cuentes como hallazgo.
4. Lee el diff archivo por archivo, sin datos ni locks:
   `git diff <base>...HEAD -- . ":!pnpm-lock.yaml" ":!package-lock.json" ":!uv.lock" ":!docs/reference/golden"`.
   En modo auditoría, lee los archivos fuente, migraciones, tests, Dockerfile y CI.

## Qué revisar, en este orden

1. **Aislamiento de datos**: si el producto separa datos por cliente u organización, toda
   consulta lleva esa separación (filtro de la aplicación y de la base), claves foráneas, roles de
   base, migraciones.
2. **Datos personales y secretos**: nada personal en claro en base, logs, errores, URLs ni
   auditoría; cifrado y claves según los ADR; secretos solo en variables de entorno.
3. **Autenticación, sesiones y permisos**: cookies, tokens, revocación, bloqueo por intentos,
   suplantación, permisos por rol aplicados en el servidor.
4. **Concurrencia**: leer y después escribir sin bloqueo ni condición bajo READ COMMITTED
   (contadores, "último administrador", enlaces de un solo uso, revocaciones). Busca cada camino
   que no use la escritura condicional o el bloqueo que el repo ya emplea.
5. **Cumplimiento de la spec**: cada RF tocado hace lo que dice; lo que la spec no pide (alcance de
   más) y lo que el plan dice y el código no hace; el "Hecho cuando" de cada tarea marcada.
6. **Tests**: el RF en el nombre de cada test; casos límite de la spec sin test; tests que dependen
   del orden o del estado que deja otro; regresión para cada corrección.
7. **Ponytail** (usa la skill `ponytail` si el repo la tiene): código, abstracciones o dependencias
   que sobran; dos implementaciones de la misma regla.
8. **Dependencias, migraciones y CI**: versiones contra la sección "Versiones" de `AGENTS.md`
   (última estable, excepciones anotadas, tiempo mínimo desde la publicación), migraciones,
   Dockerfile, acciones de CI.
9. **Lo propio del repo**: lo que su `AGENTS.md` y los ADR exijan, por ejemplo interfaz con
   `impeccable` y accesibilidad, precisión numérica y casos dorados, o contratos con sistemas externos.

No cuentes como defecto lo que pertenece a una tarea pendiente de `tasks.md`: menciónalo aparte.

## Context7 y Ponytail, obligatorios

- Antes de juzgar el uso de una librería, `resolve-library-id` y luego `query-docs` con la versión
  del manifiesto (`package.json`, `pyproject.toml`). Nunca de memoria.
- Si Context7 no responde, dilo en "Limitaciones" y marca como no verificados los hallazgos que
  dependan de esa API. No lo sustituyas por búsquedas web ni por memoria.

## Reproducir

- Puedes ejecutar lint, typecheck y tests unitarios si no escriben fuera del sandbox. No ejecutes
  nada que escriba en una base de datos ni en servicios externos.
- Distingue en cada hallazgo si la reproducción fue **ejecutada** o **deducida** del código.

## Formato del informe (fijo)

Español, sin el guion largo (U+2014), rutas relativas al repo (`src/app/auth.ts:95`), nunca rutas
absolutas de la máquina.

1. **Resumen**: número de hallazgos por gravedad, modo, base, rama y commit revisados.
2. **Hallazgos**, numerados y del más grave al menos grave, cada uno con:
   - `### N. <Alta|Media|Baja>: <título>`
   - **Archivo**: `ruta:línea` (uno o varios).
   - **Regla**: RF, RNF, principio de la constitución, ADR o regla de `AGENTS.md` que incumple.
   - **Problema**: qué pasa y por qué importa.
   - **Reproducción** (ejecutada o deducida): pasos concretos o test que fallaría.
   - **Corrección propuesta**: la mínima que lo resuelve.
3. **Tabla resumen** por área (alta, media, baja).
4. **Lo revisado que estaba bien**.
5. **Context7**: biblioteca, versión del manifiesto, consulta hecha (o "no disponible").
6. **Limitaciones**: lo que no se pudo verificar y por qué.

## Prohibido

Modificar archivos, hacer commits o push, comentar en GitHub, cambiar de rama durante la revisión,
inventar hallazgos sin archivo y línea, y presentar como ejecutada una reproducción deducida.
