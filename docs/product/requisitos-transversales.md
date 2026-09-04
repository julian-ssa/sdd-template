# Requisitos no funcionales transversales (RNF)

Catálogo único. Las specs citan estos ids; no los redactan de nuevo. Cada RNF es
verificable; el umbral se fija aquí.

## Acceso y sesión
- **RNF-1** Sesión: caduca a las {{n}} horas de inactividad; la revocación surte efecto en la siguiente petición.
- **RNF-2** Contraseñas: mínimo {{n}} caracteres; hash de propósito específico; nunca en logs ni correos.
- **RNF-3** Toda petición autenticada se acota al propietario/organización del usuario en el servidor.
- **RNF-4** Toda acción administrativa genera una entrada de auditoría (usuario, fecha-hora, acción, entidad, id).

## Datos
- **RNF-5** {{Tipos: importes, fechas, zona horaria.}}
- **RNF-6** Toda cifra calculada expone su fecha o versión de referencia.
- **RNF-7** Ningún dato personal aparece en logs, mensajes de error ni URLs.
- **RNF-8** Existe borrado o anonimización a petición con auditoría.

## Interfaz
- **RNF-9** Responsive desde {{360}} px; contenido ancho se desplaza dentro de su contenedor.
- **RNF-10** Internacionalización: todo texto visible pasa por i18n; localización del MVP: {{es-CO}}.
- **RNF-11** Accesibilidad: contraste AA, teclado, etiquetas.
- **RNF-12** Navegadores: últimas dos versiones de Chrome, Edge, Safari y Firefox; móviles actuales.

## Rendimiento
- **RNF-13** Pantallas de consulta: < {{2}} s con {{volumen de referencia}}.
- **RNF-14** Operaciones largas: confirmación al usuario en < {{30}} s o ejecución en segundo plano con estado visible.
- **RNF-15** Cálculos pesados se precalculan; nunca por petición de usuario.

## Operación
- **RNF-16** Disponibilidad objetivo: {{99 %}} mensual.
- **RNF-17** Copia de seguridad diaria con retención de {{30}} días; restauración probada.
- **RNF-18** Migraciones como código, aplicadas por CI.
- **RNF-19** Toda integración externa falla de forma visible, nunca con datos vacíos sin explicación.
