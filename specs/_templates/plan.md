# Plan técnico - Spec NNN

> Requiere: ADR-0002 (stack) decidido. Cubre: RF-1..RF-n de `spec.md`.

## Estructura de módulos
<Módulos/paquetes/servicios y qué RF cubre cada uno. Respeta "Dominio sin interfaz" (constitución).>

## Modelo de datos
<Entidades, campos, claves naturales, alcance por organización. Ejemplo concreto. Migración como código.>

## Contratos
<API interna/externa, eventos, formatos de archivo. Qué RF cubre cada contrato.>

## Algoritmos y cálculos
<Pseudocódigo. Cada fórmula referencia `docs/reference/computations.md`. Fecha de valoración (`as_of`) explícita.>

## Decisiones técnicas
<Cada decisión con su justificación y la alternativa descartada. Cita el principio de la constitución o el ADR que la respalda.>

## Estrategia de tests
<Unitarios del dominio con fechas inyectadas, contratos, integración, golden tests. Mapa RF → test.>

## Cobertura de requisitos
| RF | Módulo | Test previsto |
|---|---|---|
| RF-1 | | |
