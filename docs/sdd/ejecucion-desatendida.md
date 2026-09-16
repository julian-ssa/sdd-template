# Ejecución desatendida de tareas (VPS, noche, sin nadie delante)

Cómo dejar que un agente avance lotes de tareas sin supervisión y cómo comprobar por la
mañana que lo hecho está bien. La skill que lo formaliza es [`sdd-run`](../../.agents/skills/sdd-run/SKILL.md);
la regla de una tarea y parar ([`sdd-implement`](../../.agents/skills/sdd-implement/SKILL.md)) sigue
siendo la norma cuando hay una persona delante.

## Principios

1. **Rama, nunca `develop` ni `main`.** Cada lote trabaja en `spec-NNN/Ta-Tb`, creada desde
   `develop`, y termina en un pull request contra `develop` (entorno de pruebas). `main` es
   producción y solo recibe un pull request de `develop` cuando el propietario libera.
2. **CI es la puerta.** Una tarea cuenta como hecha solo con CI en verde en su commit
   (constitución 10). El agente no mezcla PR.
3. **Parar es correcto.** Ante un fallo persistente, una tarea `[H]` o `[M]`, un hueco en la spec
   o un secreto que falta, el agente se detiene y lo deja escrito en el PR. Un lote parado a
   tiempo vale más que uno terminado a la fuerza.
4. **Lotes cortos al principio.** Cinco o seis tareas por noche hasta ver cómo se comporta y
   cuánto cuesta en tokens; después, lo que la experiencia aconseje.

## Modelo y esfuerzo (Claude Code)

Reparto decidido por el propietario (2026-09-16) para gastar tokens donde rinden:
- **Fable 5.1** para pensar y juzgar: `sdd-spec`, `sdd-plan`, `sdd-validate`, `sdd-change` y la
  revisión de pull requests. Esfuerzo `high`.
- **Opus 5** para ejecutar: `sdd-implement` y `sdd-run`. Esfuerzo `medium` por defecto; `high`
  solo en tareas de cifrado, sesiones, migraciones o permisos.

Cómo se aplica: cada skill lleva en su cabecera `model: fable` o `model: opus`, así Claude Code
cambia de modelo al invocarla aunque la sesión esté en otro. La sesión del servidor arranca con
`claude --model opus --effort medium` (o con `"model": "opus"` en el `settings.json` del usuario que
ejecuta el agente); dentro de una sesión, `/model` y `/effort` lo cambian al momento. El campo
`model:` es una indicación para Claude Code; otras herramientas lo ignoran y eligen su modelo.

## Cómo lanzarlo

Desde una sesión de Claude Code (u otro agente) **en el VPS**, dentro del repo de código:

```
sdd-run NNN Ta Tb
```

La sesión vive en el servidor: cerrar el portátil no la interrumpe. Con Remote Control se
puede seguir desde el teléfono.

## Qué revisar por la mañana (en este orden)

1. **El pull request de la rama**: commits (uno por tarea, con el RF), el diff y el informe del
   lote (tareas hechas, dónde paró y por qué, consultas de Context7, dependencias añadidas).
2. **CI en verde en el PR.** Si está en rojo, no se mezcla; el informe dice qué falló.
3. **`tasks.md`** de la spec en el repo de specs: casillas marcadas con commit y evidencia. Es el
   resumen, no la prueba.
4. **Revisión con más atención** en lo que el informe señale como sensible: cifrado y claves,
   sesiones y cookies, migraciones y políticas de seguridad por filas, permisos por rol.
5. **Al cerrar una spec**: `sdd-validate NNN` (veredicto RF por RF con el test que lo cubre) y la
   demo manual de "Criterios de finalización". Esa es la confirmación de que funciona como se
   esperaba.

## Preparación del VPS (una vez, usuario que ejecuta el agente)

- Workspace: `mkdir <workspace> && cd <workspace>` y `git clone` de el repo de specs y los repos de código como hermanos. El servicio del agente arranca con
  `WorkingDirectory` en esa carpeta.
- Identidad de git a nombre del propietario (`git config --global user.name` y `user.email`):
  los commits salen a su nombre. `gh auth login` con un token limitado a esos repos.
- Los runtimes del stack (Node, Python, Docker para las bases de los tests de integración; `docker compose up -d db` en el repo que lo necesite).
- Context7 registrado a nivel de usuario con su clave; `enableAllProjectMcpServers` en la
  configuración de usuario si se quiere evitar la aprobación manual por repo.
- Ningún secreto real en el VPS: solo el `.env` del Postgres local. Las credenciales de servicios externos no hacen falta para las tareas `[A]`; las `[M]` que las necesiten paran el lote.

## Comprobación previa a cada lote

```bash
cd ~/<workspace>/<repo> && git status --short && git pull -q && <instalar> && <servicios locales> && <tests>
```

Si cualquiera de esos pasos falla, no se lanza el lote.
