# Modelo de dominio

Entidades y relaciones del producto, sin tecnología. Los nombres en código están en el
glosario. Marca ⓞ las entidades que pertenecen a un propietario/organización.

```
{{Raíz}}
├── {{Entidad}} ⓞ        {{atributos clave}}
│   └── {{Hija}}          {{atributos}}
└── {{Entidad}} ⓞ
```

## Reglas estructurales
1. {{Alcance de datos.}}
2. {{Claves naturales y unicidad.}}
3. {{Agregaciones: qué se calcula a partir de qué.}}
4. {{Auditoría y borrado.}}

## Ciclo de vida resumido
```
{{origen}} ──► {{entidad}} ──► {{proceso}} ──► {{resultado}}
```
