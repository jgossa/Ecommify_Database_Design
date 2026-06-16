# Video de demostración - Unidad 5 Etapa 2

Duración máxima: 5 minutos.

Objetivo: demostrar la implementación técnica completa en PostgreSQL/Supabase y MongoDB Atlas, mostrando evidencias concretas del repositorio, consultas optimizadas y decisiones técnicas principales.

## Guion sugerido

### 0:00 - 0:25 | Contexto del proyecto

Presentar brevemente Ecommify.

Mensaje clave:

Ecommify usa una arquitectura híbrida:
- PostgreSQL/Supabase como núcleo transaccional.
- MongoDB Atlas como módulo documental y analítico.

### 0:25 - 1:20 | PostgreSQL/Supabase

Mostrar en Supabase o en el repo:

- esquema core;
- tablas principales;
- particionamiento de core.orders;
- scripts en postgresql/schema;
- validaciones en postgresql/evidence/validation.

Mensaje clave:

PostgreSQL concentra integridad transaccional, constraints, particionamiento, índices y consultas críticas.

### 1:20 - 2:25 | MongoDB Atlas

Mostrar en Atlas o en el repo:

- product_catalog;
- product_reviews;
- product_review_buckets;
- JSON Schema aplicado a product_catalog;
- Bucket Pattern con product_review_buckets.

Mensaje clave:

MongoDB complementa PostgreSQL con catálogo enriquecido, reseñas, búsqueda textual y patrones documentales.

### 2:25 - 3:25 | Optimización y evidencias

Mostrar en el repo:

- mongodb/evidence/explain_before_after;
- comparación antes/después;
- índices MongoDB;
- pipeline optimizado;
- evidencia de Bucket Pattern con explain.

Mensaje clave:

Se validó rendimiento con explain, índices compuestos, parciales, texto y pipeline optimizado.

### 3:25 - 4:15 | Decisiones técnicas

Explicar 3 decisiones:

1. PostgreSQL se mantiene como fuente transaccional principal.
2. MongoDB se usa para flexibilidad documental y consultas analíticas.
3. Sharding se documentó de forma teórica/simulada, sin modificar el cluster real de Atlas.

### 4:15 - 4:50 | Repositorio y cierre

Mostrar estructura final del repo:

- README.md;
- postgresql/README.md;
- mongodb/README.md;
- docs/u5_etapa2;
- notebooks;
- evidence.

Mensaje de cierre:

La implementación queda reproducible mediante scripts, notebooks, evidencias y documentación técnica.

## Checklist de grabación

Antes de grabar:

- Tener abierto el repo local o GitHub.
- Tener abierto Supabase.
- Tener abierto MongoDB Atlas.
- Tener lista una tabla de evidencia MongoDB antes/después.
- Tener lista una validación PostgreSQL.
- No mostrar passwords, connection strings ni credenciales.
- No mostrar variables de entorno con valores reales.

Durante la grabación:

- Mostrar máximo una evidencia PostgreSQL.
- Mostrar máximo dos evidencias MongoDB.
- No navegar demasiado entre carpetas.
- No leer todo el README.
- Priorizar resultados y decisiones.

Después de grabar:

- Verificar que dura menos de 5 minutos.
- Verificar que no aparecen credenciales.
- Subir enlace del video al documento final y al README si aplica.
