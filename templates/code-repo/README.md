# Plantilla de repo de código

Base común de cualquier repo de código que consume un repo de specs SDD como hermano
(ADR-0001). Cópiala a la raíz del repo nuevo y rellena los `{{…}}` de `AGENTS.md`.

Después, crea los enlaces a las skills SDD (uno por skill, relativos al repo de specs):

```bash
for s in sdd-spec sdd-plan sdd-implement sdd-validate sdd-change sdd-run; do
  ln -s ../../../<proyecto>-specs/.agents/skills/$s .agents/skills/$s
done
mkdir -p .claude .opencode && ln -s ../.agents/skills .claude/skills && ln -s ../.agents/skills .opencode/skill
```

Añade el flujo de CI del stack en `.github/workflows/ci.yml` (lint, tipos, tests en cada push
y pull request) y un `Dockerfile` si se despliega como imagen. Ejemplos reales de Node (Fastify,
Next.js) y Python (`uv`, FastAPI): repos `cuadranta-api`, `cuadranta-web`, `cuadranta-quant`.
