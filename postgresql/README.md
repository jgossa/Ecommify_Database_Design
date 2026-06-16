# PostgreSQL - Implementación transaccional Ecommify

Esta carpeta contiene la implementación PostgreSQL del proyecto Ecommify.

PostgreSQL se usa como núcleo transaccional de la arquitectura híbrida. Su objetivo es soportar datos estructurados, integridad referencial, restricciones, consultas críticas, particionamiento, vistas materializadas y optimización mediante índices.

## Estructura de carpetas

postgresql/
├── README.md
├── schema/
│   ├── 00_extensions.sql
│   ├── 01_schemas.sql
│   ├── 02_types_domains.sql
│   ├── 03_tables_core.sql
│   ├── 04_tables_transactions.sql
│   ├── 05_indexes.sql
│   ├── 06_triggers_updated_at.sql
│   ├── 07_partitioning_orders.sql
│   └── 08_materialized_views.sql
├── seed_data/
│   └── 10_seed_data.sql
├── queries/
│   ├── 11_validation_queries.sql
│   └── 12_monitoring_queries.sql
└── evidence/
    ├── validation/
    └── explain_before_after/

## Scripts principales

### 00_extensions.sql

Define extensiones PostgreSQL usadas por el proyecto, como soporte para UUID, búsquedas avanzadas, índices especializados y capacidades geográficas cuando aplica.

### 01_schemas.sql

Crea los esquemas lógicos del proyecto, especialmente el esquema `core`.

### 02_types_domains.sql

Define tipos, dominios o estructuras auxiliares usados por el modelo relacional.

### 03_tables_core.sql

Crea tablas maestras y entidades base del dominio Ecommify.

### 04_tables_transactions.sql

Crea tablas transaccionales como órdenes, ítems, pagos, reseñas referenciadas e inventario.

### 05_indexes.sql

Define índices para optimizar consultas críticas. Incluye índices convencionales y especializados según las necesidades del modelo.

### 06_triggers_updated_at.sql

Define triggers para mantener campos de auditoría como `updated_at`.

### 07_partitioning_orders.sql

Define la estrategia de particionamiento para la tabla `core.orders`, usando `purchase_date` como clave de particionamiento.

### 08_materialized_views.sql

Define vistas materializadas orientadas a consultas analíticas y tableros.

### 10_seed_data.sql

Contiene datos semilla o instrucciones de carga necesarias para el prototipo.

### 11_validation_queries.sql

Contiene consultas de validación para confirmar existencia de esquema, tablas, restricciones, índices, particiones y conteos.

### 12_monitoring_queries.sql

Contiene consultas de monitoreo o revisión operativa para PostgreSQL.

## Validaciones realizadas

Para la Unidad 5 Etapa 2 se validó:

- existencia del esquema `core`;
- existencia de tablas principales;
- conteos estimados de datos;
- extensiones instaladas;
- constraints por tabla;
- particionamiento de `core.orders`;
- inventario de índices;
- ejecución de consulta de control con EXPLAIN ANALYZE.

## Tablas principales

El esquema `core` incluye, entre otras, las siguientes tablas:

- core.geolocation
- core.product_categories
- core.customers
- core.sellers
- core.products
- core.orders
- core.order_items
- core.payments
- core.reviews_ref
- core.inventory

## Notas de alcance

- PostgreSQL conserva el rol de núcleo transaccional.
- MongoDB no reemplaza PostgreSQL; lo complementa para catálogo enriquecido, reseñas y análisis documental.
- La evidencia de rendimiento y validación debe ubicarse en `postgresql/evidence/`.
- Los scripts deben ejecutarse en orden numérico cuando se reconstruya el entorno.
