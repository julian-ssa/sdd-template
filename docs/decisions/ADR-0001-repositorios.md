# ADR-0001 - Organización de repositorios; las specs como repo hermano en el workspace

Estado: propuesta · Fecha: {{FECHA}}

## Contexto
{{Qué piezas de código tendrá el producto y qué repos ya existen.}}

## Decisión
- Un repositorio git por pieza de código. La carpeta local de trabajo (**workspace**) es
  una carpeta normal, sin git, con los repos clonados uno al lado del otro:

  ```
  {{workspace}}/
  ├── {{PROYECTO}}-specs/      specs, ADRs, docs, skills (este repo)
  ├── {{PROYECTO}}-api/        repos de código, uno por pieza
  └── reference/               material local, nunca versionado
  ```
- `{{PROYECTO}}-specs` es la fuente de verdad del producto (constitución, specs, ADRs,
  docs, skills). No contiene código y **no es dependencia de construcción ni de
  despliegue** de ningún repo de código.
- Cada repo de código lleva un `AGENTS.md` propio (por ejemplo `{{PROYECTO}}-api/AGENTS.md`) que dice "las specs están en
  `../{{PROYECTO}}-specs`; si la carpeta no existe, clónala ahí", y enlaza las skills con
  `.agents/skills -> ../../{{PROYECTO}}-specs/.agents/skills` (enlace simbólico relativo).
- Trazabilidad: `plan.md` y `tasks.md` viven en el repo de specs; cada tarea marcada anota
  el commit del repo de código que la implementó, y los mensajes de commit citan spec y RF.
- Los repos externos no se copian ni se clonan en el workspace; su contrato se documenta
  en `docs/reference/*-contract.md` con el commit leído.
- El backlog vive en [`docs/product/roadmap.md`](../product/roadmap.md).

## Consecuencias
- Despliegue simple: cada repo de código se construye solo, sin credenciales para otro repo.
- Cambiar una spec es un commit en el repo de specs, sin tocar los repos de código; la
  referencia es siempre `main` del repo de specs y la trazabilidad se lleva en `tasks.md`.
- Un agente que trabaje en un repo de código necesita el hermano clonado; el `AGENTS.md` de ese repo lo dice.

## Alternativas descartadas
- **Monorepo**: {{motivo}}.
- **Copiar repos externos**: quedan obsoletos al primer cambio.
- **Specs como submódulo git en cada repo de código**: fija la versión por commit, pero
  mete en cada repo algo que el build no usa, obliga a `clone --recurse-submodules` y a un
  commit por cada cambio de spec, y los constructores alojados suelen fallar al clonar
  submódulos privados.
