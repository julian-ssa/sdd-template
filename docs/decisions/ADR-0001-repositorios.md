# ADR-0001 - Organización de repositorios; las specs como submódulo

Estado: propuesta · Fecha: {{FECHA}}

## Contexto
{{Qué piezas de código tendrá el producto y qué repos ya existen.}}

## Decisión
- Un repositorio git por pieza de código. La carpeta local de trabajo es un workspace, no un repo.
- `{{PROYECTO}}-specs` es la fuente de verdad del producto (constitución, specs, ADRs, docs, skills). No contiene código.
- Cada repo de aplicación incorpora `{{PROYECTO}}-specs` como **submódulo git** en `sdd/` y enlaza `.agents/skills` → `sdd/.agents/skills`, de modo que cualquier agente en cualquier repo ve la misma spec y las mismas skills, fijadas a un commit.
- Los repos externos no se copian ni se clonan en el workspace; su contrato se documenta en `docs/reference/*-contract.md` con el commit leído.
- El backlog vive en `docs/product/roadmap.md`.

## Consecuencias
- Cambiar una spec es un commit en el repo de specs y un bump del submódulo en cada repo de código: la desincronización es visible.
- Coste: aprender dos comandos de submódulo.

## Alternativas descartadas
- **Monorepo**: {{motivo}}.
- **Copiar repos externos**: quedan obsoletos al primer cambio.
