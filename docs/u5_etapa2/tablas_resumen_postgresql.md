# Tablas resumen PostgreSQL - U5 Etapa 2

Este archivo consolida las principales evidencias PostgreSQL que serán usadas en el documento técnico evaluativo.

## 1. Validación final PostgreSQL/Supabase

| validation_item | status | evidence | notes |
| --- | --- | --- | --- |
| schema_core_exists | OK | Consulta sobre information_schema.schemata | El esquema core existe en Supabase PostgreSQL. |
| core_tables_exist | OK | Consulta sobre pg_tables | Las tablas principales del modelo Ecommify existen en core. |
| row_estimates_available | OK | Consulta sobre pg_class y pg_namespace | Las tablas tienen conteos estimados disponibles. |
| extensions_checked | OK | Consulta sobre pg_extension | Se validaron extensiones relevantes para el modelo. |
| constraints_checked | OK | Consulta sobre information_schema.table_constraints | Se validaron primary keys foreign keys check constraints y otros constraints. |
| orders_partitioning_checked | OK | Consulta sobre pg_partitioned_table | La tabla core.orders aparece particionada por purchase_date. |
| indexes_inventory_checked | OK | Consulta sobre pg_indexes | Se validó inventario de índices del esquema core. |
| explain_control_query_executed | OK | EXPLAIN ANALYZE BUFFERS | La consulta crítica de control ejecutó correctamente. |

## 2. Manifiesto de evidencias EXPLAIN antes/después

| evidence_item | status | description | source_reference |
| --- | --- | --- | --- |
| baseline_explain | documented | Medición base de Q01-Q09 con EXPLAIN ANALYZE BUFFERS | U4 Etapa 2 Hito 4 |
| post_optimization_explain | documented | Medición posterior después de optimizaciones e índices | U4 Etapa 2 Hito 8 |
| before_after_comparison | documented | Comparación antes/después con reducción de tiempo y bloques leídos cuando aplica | U4 Etapa 2 Hito 8 |
| specialized_indexes | documented | Índices B-tree parcial GIN pg_trgm y BRIN documentados | U4 Etapa 2 Hito 7 |
| partitioning_validation | documented | Validación de particionamiento declarativo de core.orders por purchase_date | U4 Etapa 2 Hito 9 |

## 3. Inventario de scripts PostgreSQL

| category | file_path | file_name | size_bytes |
| --- | --- | --- | --- |
| schema | postgresql/schema/00_extensions.sql | 00_extensions.sql | 371 |
| schema | postgresql/schema/01_schemas.sql | 01_schemas.sql | 312 |
| schema | postgresql/schema/02_types_domains.sql | 02_types_domains.sql | 1008 |
| schema | postgresql/schema/03_tables_core.sql | 03_tables_core.sql | 1863 |
| schema | postgresql/schema/04_tables_transactions.sql | 04_tables_transactions.sql | 2846 |
| schema | postgresql/schema/05_indexes.sql | 05_indexes.sql | 1234 |
| schema | postgresql/schema/06_triggers_updated_at.sql | 06_triggers_updated_at.sql | 984 |
| schema | postgresql/schema/07_partitioning_orders.sql | 07_partitioning_orders.sql | 673 |
| schema | postgresql/schema/08_materialized_views.sql | 08_materialized_views.sql | 1790 |
| queries | postgresql/queries/11_validation_queries.sql | 11_validation_queries.sql | 719 |
| queries | postgresql/queries/12_monitoring_queries.sql | 12_monitoring_queries.sql | 773 |
| seed_data | postgresql/seed_data/10_seed_data.sql | 10_seed_data.sql | 657 |

## Nota de alcance

Las métricas detalladas de EXPLAIN antes/después fueron desarrolladas en la Unidad 4 Etapa 2. Para la Unidad 5 Etapa 2, esta carpeta conserva el manifiesto de trazabilidad y las validaciones finales del componente PostgreSQL/Supabase. Si se recuperan CSV completos del notebook U4, deben agregarse a `postgresql/evidence/explain_before_after/`.
