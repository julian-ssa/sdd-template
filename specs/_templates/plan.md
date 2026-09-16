# Plan técnico - Spec NNN

> Requiere: [ADR-0002](../../docs/decisions/ADR-0002-stack.md) (stack) decidido. Cubre: RF-1..RF-n de [`spec.md`](spec.md).

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

## Herramientas obligatorias del agente
<Context7 antes de usar cada librería (lista las librerías y versiones de este plan), Ponytail en cada tarea, impeccable en toda interfaz. Ver `AGENTS.md` del repo de código.>

## Estrategia de tests
<Unitarios del dominio con fechas inyectadas, contratos, integración, golden tests. Mapa RF → test.>

## Cobertura de requisitos
| RF | Módulo | Test previsto |
|---|---|---|
| RF-1 | | |
