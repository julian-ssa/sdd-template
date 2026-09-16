#!/usr/bin/env python3
"""Enlaces entre archivos markdown del repo.

    python3 tools/links.py --check   # lista enlaces rotos y referencias sin enlace (salida 1 si hay alguno)
    python3 tools/links.py --fix     # convierte las referencias sin enlace en enlaces relativos

Regla (AGENTS.md): toda referencia a otro archivo del repo es un enlace markdown relativo.
Se reconocen tres formas de referencia: una ruta entre acentos graves (`docs/x.md`, o solo el
nombre si es único en el repo), `ADR-NNNN` y `spec NNN`. Se ignoran los bloques de código,
los encabezados, los archivos que no existen y las referencias de un archivo a sí mismo.
Solo usa la biblioteca estándar.
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

FILES = [f for f in subprocess.check_output(["git", "ls-files", "*.md"], text=True).split()
         if not f.startswith("templates/")]  # las plantillas se copian a otros repos: sus rutas no son de este
ALL = subprocess.check_output(["git", "ls-files"], text=True).split()
ADRS = {m.group(1): p for p in glob.glob("docs/decisions/ADR-*.md")
        if (m := re.match(r"ADR-(\d{4})", os.path.basename(p)))}
SPECS = {m.group(1): os.path.join(d, "spec.md") for d in glob.glob("specs/[0-9][0-9][0-9]-*")
         if (m := re.match(r"(\d{3})-", os.path.basename(d))) and os.path.isfile(os.path.join(d, "spec.md"))}
BASENAMES = {}
for p in ALL:
    BASENAMES.setdefault(os.path.basename(p), []).append(p)
# Nombres genéricos: solo se enlazan si están en la misma carpeta (nunca por nombre único).
GENERIC = {"spec.md", "plan.md", "tasks.md", "SKILL.md", "README.md", "AGENTS.md", "CLAUDE.md"}

PATH_RE = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|xlsx|txt|csv))`")
ADR_RE = re.compile(r"\bADR-(\d{4})\b(?![-\w])")
SPEC_RE = re.compile(r"\b([Ss]pec) (\d{3})\b(?![-\w])")
PROTECT_RE = re.compile(r"\[[^\]]*\]\([^)]*\)|`[^`]*`")  # enlaces existentes y código en línea
LINK_RE = re.compile(r"\]\(([^)#\s]+)")


def rel(target, src):
    return os.path.relpath(target, os.path.dirname(src) or ".")


def resolve(path, src):
    """Ruta desde la raíz, desde la carpeta del archivo, o nombre único en el repo."""
    if os.path.isfile(path) and ("/" in path or path not in GENERIC or os.path.dirname(src) == ""):
        return os.path.normpath(path)
    if "/" not in path:
        same = os.path.normpath(os.path.join(os.path.dirname(src), path))
        if os.path.isfile(same):
            return same
        hits = BASENAMES.get(path, [])
        if len(hits) == 1 and path not in GENERIC:
            return hits[0]
    return None


def linkify(src, text):
    """Devuelve (texto nuevo, lista de referencias sin enlace encontradas)."""
    out, found, fence = [], [], False
    for n, line in enumerate(text.split("\n"), 1):
        if line.strip().startswith("```"):
            fence = not fence
        if fence or line.lstrip().startswith("#") or line.strip().startswith("```"):
            out.append(line)
            continue
        pos, buf = 0, []

        def free(seg):
            def adr(m):
                t = ADRS.get(m.group(1))
                if t and t != src:
                    found.append((n, m.group(0)))
                    return f"[{m.group(0)}]({rel(t, src)})"
                return m.group(0)

            def spec(m):
                t = SPECS.get(m.group(2))
                if t and t != src:
                    found.append((n, m.group(0)))
                    return f"[{m.group(0)}]({rel(t, src)})"
                return m.group(0)
            return SPEC_RE.sub(spec, ADR_RE.sub(adr, seg))

        for m in PROTECT_RE.finditer(line):
            buf.append(free(line[pos:m.start()]))
            seg = m.group(0)
            if seg.startswith("`"):
                pm = PATH_RE.fullmatch(seg)
                tgt = pm and resolve(pm.group(1), src)
                if tgt and tgt != src:
                    found.append((n, seg))
                    seg = f"[{seg}]({rel(tgt, src)})"
            buf.append(seg)
            pos = m.end()
        buf.append(free(line[pos:]))
        out.append("".join(buf))
    return "\n".join(out), found


def broken_links(src, text):
    d, fence = os.path.dirname(src), False
    for n, line in enumerate(text.split("\n"), 1):
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        line = re.sub(r"`[^`]*`", "", line)  # los ejemplos en código en línea no son enlaces
        for target in LINK_RE.findall(line):
            if target.startswith(("http://", "https://", "mailto:")) or "{{" in target:
                continue
            if not os.path.exists(os.path.normpath(os.path.join(d, target))):
                yield n, target


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    problems = 0
    for f in FILES:
        old = open(f, encoding="utf-8").read()
        for n, target in broken_links(f, old):
            print(f"ENLACE ROTO {f}:{n}: {target}")
            problems += 1
        new, found = linkify(f, old)
        if mode == "--fix":
            if new != old:
                open(f, "w", encoding="utf-8").write(new)
                print(f"{f}: {len(found)} referencias enlazadas")
        else:
            for n, ref in found:
                print(f"SIN ENLACE {f}:{n}: {ref}")
            problems += len(found)
    if mode == "--check":
        print("OK: sin enlaces rotos ni referencias sin enlace" if not problems else f"{problems} problemas")
        sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
