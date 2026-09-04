# Spec NNN - <Nombre de la funcionalidad>

> Estado: borrador | en clarificación | aprobada | implementada · Depende de: <specs> · Marcadores abiertos: <n>

## Contexto y objetivo
<Qué problema resuelve y por qué merece la pena. Un párrafo. Cita el glosario para los términos de dominio.>

## Actores
<Quién lo usa y con qué rol: administrador de organización, asesor, inversor, sistema externo…>

## Historias de usuario
- H1: Como <rol> quiero <acción> para <beneficio>.

## Requisitos funcionales (criterios de aceptación en EARS)
<Agrupa por historia con `### Título (H1)`. Numera RF-1, RF-2… sin reiniciar. Un requisito, una frase, verificable.>

### <Grupo> (H1)
- RF-1: CUANDO <evento>, EL SISTEMA <respuesta> (<resultado observable>).
- RF-2: SI <condición no deseada>, ENTONCES EL SISTEMA <respuesta>.
- RF-3: MIENTRAS <estado>, EL SISTEMA <respuesta>.
- RF-4: DONDE <característica opcional>, EL SISTEMA <respuesta>.
- RF-5: EL SISTEMA <comportamiento permanente>.

## Requisitos no funcionales aplicables
<Solo ids del catálogo `docs/product/requisitos-transversales.md`, p. ej. RNF-1, RNF-4. Añade aquí únicamente los específicos de esta spec.>

## Casos límite
<Vacíos, duplicados, datos corruptos, límites, concurrencia, permisos. Cada uno apunta al RF que lo cubre.>
- <caso> → RF-n.

## Fuera de alcance
<Lo que explícitamente NO se hace en esta iteración y dónde queda registrado (roadmap, otra spec).>

## Dependencias
<Specs, contratos externos (`docs/reference/*-contract.md`) y recursos externos (`docs/sdd/recursos-externos.md`) de los que depende.>

## Criterios de finalización
<Ej.: todos los RF con test en verde + demo manual del flujo principal + marcadores a cero.>

## Dudas abiertas
- [NECESITA ACLARACIÓN: <pregunta concreta>] - quién responde: <persona/organización>.

## Cambios
<Historial de cambios de requisitos tras la aprobación: fecha, RF afectados, motivo.>
