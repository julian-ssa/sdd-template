#!/usr/bin/env bash
# Crea un repo de specs nuevo a partir de esta plantilla.
# Uso: ./new-project.sh <nombre-kebab> <ruta-destino> ["Descripción corta"]
set -euo pipefail
NAME="${1:?nombre-kebab}"; DEST="${2:?ruta-destino}"; DESC="${3:-{{DESCRIPCION}}}"
SRC="$(cd "$(dirname "$0")" && pwd)"
TARGET="$DEST/$NAME-specs"
[ -e "$TARGET" ] && { echo "Ya existe: $TARGET" >&2; exit 1; }
mkdir -p "$DEST"
# Copia todo salvo .git y este script; conserva enlaces simbólicos.
rsync -a --exclude .git --exclude new-project.sh "$SRC/" "$TARGET/"
TODAY="$(date +%F)"
# Sustituye placeholders básicos (macOS/BSD sed y GNU sed).
find "$TARGET" -type f -name "*.md" -print0 | xargs -0 sed -i.bak \
  -e "s/{{PROYECTO}}/$NAME/g" \
  -e "s/{{FECHA}}/$TODAY/g" \
  -e "s|{{DESCRIPCION}}|$DESC|g"
find "$TARGET" -name "*.bak" -delete
( cd "$TARGET" && git init -b main -q && git add -A && git commit -q -m "Marco SDD inicial desde sdd-template" )
echo "Creado $TARGET"
echo "Placeholders pendientes:"; grep -rn "{{" "$TARGET" --include=*.md | cut -c1-120 || true
