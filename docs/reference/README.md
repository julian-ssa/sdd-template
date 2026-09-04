# Referencia

Aquí se documenta lo que ya existe y condiciona las specs: sistemas previos que se
portan, fórmulas o reglas de negocio heredadas, y contratos de sistemas externos.

Reglas:
- Cada archivo abre con `Fuente: <repo o sistema> @ <commit o versión> (<fecha>)` para que la obsolescencia sea visible.
- No se copia código de otros repos al workspace; se leen bajo demanda y se documenta el contrato.
- Sin datos personales reales: ejemplos ficticios o agregados.

Archivos típicos:
- `legacy-<sistema>.md` — mapa del sistema anterior: qué se mantiene, qué se elimina, deudas conocidas.
- `computations.md` — catálogo de fórmulas con un ejemplo dorado para golden tests.
- `<sistema>-contract.md` — qué entrega o consume un sistema externo, formato, códigos de error, qué no asumir.
