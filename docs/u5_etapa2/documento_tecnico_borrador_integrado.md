# Documento técnico de implementación - Unidad 5 Etapa 2

Proyecto: Ecommify  
Entregable: Implementación técnica completa en PostgreSQL y MongoDB  
Equipo: E21  
Repositorio GitHub: pendiente de confirmar enlace final  
Video de demostración: pendiente de grabación y enlace final  

## 1. Resumen ejecutivo

La Etapa 2 de la Unidad 5 consolida la implementación técnica completa del proyecto Ecommify en PostgreSQL/Supabase y MongoDB Atlas.

PostgreSQL se mantiene como núcleo transaccional de la arquitectura, encargado de datos estructurados, integridad referencial, restricciones, particionamiento, consultas críticas e índices especializados.

MongoDB Atlas complementa la arquitectura como módulo documental y analítico, orientado a catálogo enriquecido, reseñas, búsqueda textual, agregaciones, validación documental y patrones de modelado como Attribute Pattern, Extended Reference Pattern y Bucket Pattern.

La implementación integra evidencias de optimización, scripts reproducibles, notebooks, validaciones, documentación técnica y estructura final del repositorio GitHub.

## 2. Alcance y continuidad con Ecommify

Esta entrega mantiene continuidad con los entregables previos del proyecto Ecommify.

La arquitectura seleccionada corresponde a un enfoque transaccional-analítico:

- PostgreSQL/Supabase como fuente transaccional principal.
- MongoDB Atlas como componente documental y analítico.
- Google Colab como entorno de validación, carga y análisis.
- GitHub como repositorio central de scripts, evidencias y documentación.

La etapa no reemplaza el diseño anterior. Lo consolida y lo complementa con evidencias técnicas de implementación y optimización.

## 3. Implementación PostgreSQL en Supabase

La implementación PostgreSQL se organiza en la carpeta postgresql/.

El esquema principal es core e incluye tablas como:

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

Los scripts principales se encuentran en postgresql/schema/ e incluyen:

- extensiones;
- esquemas;
- tipos y dominios;
- tablas core;
- tablas transaccionales;
- índices;
- triggers updated_at;
- particionamiento de core.orders;
- vistas materializadas.

La validación final de PostgreSQL quedó documentada en postgresql/evidence/validation/.

## 4. Optimización PostgreSQL

La optimización PostgreSQL se apoya en el trabajo desarrollado previamente en la Unidad 4.

Se documentaron consultas críticas Q01-Q09, mediciones base con EXPLAIN ANALYZE BUFFERS, análisis de planes, creación de índices especializados, medición posterior y comparación antes/después.

Las técnicas utilizadas incluyen:

- índices B-tree;
- índices GIN;
- índices asociados a pg_trgm;
- índices BRIN;
- particionamiento declarativo de core.orders por purchase_date;
- validación de planes con EXPLAIN ANALYZE BUFFERS.

La evidencia organizada para esta etapa se encuentra en postgresql/evidence/explain_before_after/.

## 5. Implementación MongoDB en Atlas

La implementación MongoDB se organiza en la carpeta mongodb/.

Las colecciones principales son:

- product_catalog;
- product_reviews;
- product_review_buckets.

product_catalog contiene el catálogo enriquecido de productos. Incluye información de categoría, precios, especificaciones, vendedores, rating, ventas, palabras clave y campos de auditoría.

product_reviews contiene reseñas referenciadas por producto.

product_review_buckets es una colección derivada creada para evidenciar Bucket Pattern, agrupando reseñas por product_id, bucket_period y bucket_sequence.

Se aplicó JSON Schema sobre product_catalog y se generó evidencia de validación en mongodb/evidence/json_schema/.

## 6. Optimización MongoDB

La optimización MongoDB se desarrolló sobre consultas críticas Q01-Q07.

Se aplicaron o reutilizaron índices para:

- navegación de catálogo por categoría;
- filtros por categoría y precio;
- consulta por vendedor;
- búsqueda textual;
- reseñas por producto;
- reseñas críticas;
- análisis por categoría;
- consulta de buckets por producto y periodo.

Las evidencias principales están en mongodb/evidence/explain_before_after/ y mongodb/evidence/bucket_pattern/.

La optimización incluyó:

- explain con executionStats;
- índices compuestos;
- índice parcial;
- índice de texto reutilizado;
- pipeline de agregación base y optimizado;
- comparación antes/después.

## 7. Evidencias cuantitativas consolidadas

Las evidencias cuantitativas se consolidan desde dos fuentes:

PostgreSQL:

- manifiesto de EXPLAIN antes/después;
- validaciones de esquema;
- evidencia de particionamiento;
- documento técnico U4 Etapa 2 como soporte de optimización relacional.

MongoDB:

- hito3_baseline_explain_summary.csv;
- hito5_optimized_explain_summary.csv;
- hito5_before_after_comparison.csv;
- hito6_pipeline_comparison.csv;
- hito6_pipeline_improvement.csv;
- u5_etapa2_mongodb_bucket_explain_summary.csv.

En el documento final se deben presentar tablas resumidas y no todos los CSV completos.

## 8. Sincronización entre PostgreSQL y MongoDB

La arquitectura mantiene PostgreSQL como fuente transaccional principal y MongoDB como vista documental/analítica.

La integración entre ambos motores se entiende como un flujo batch o ETL académico basado en identificadores compartidos:

- product_id;
- order_id;
- seller_id;
- customer_id, cuando aplica.

MongoDB almacena documentos derivados o enriquecidos para consultas flexibles, mientras PostgreSQL conserva la integridad transaccional.

La sincronización productiva en tiempo real no hace parte del alcance del prototipo académico. Se documenta como una limitación y una ruta futura.

## 9. Sharding y replica sets

La estrategia de sharding y replica sets se documentó de forma teórica/simulada.

Para product_catalog se propuso:

- category + hashed product_id.

Para product_reviews se propuso:

- hashed product_id.

La estrategia de replica set considera:

- primary para escrituras;
- secondaries para lecturas no críticas;
- write concern majority para cargas y actualizaciones;
- read preference secondaryPreferred para analítica;
- primaryPreferred para lecturas que requieren datos recientes.

La evidencia está documentada en mongodb/sharding/sharding_replica_set_design.md.

## 10. Repositorio GitHub actualizado

El repositorio GitHub fue actualizado en main con:

- README raíz actualizado;
- README PostgreSQL;
- README MongoDB;
- scripts SQL;
- scripts Python MongoDB;
- JSON Schema;
- evidencias CSV/JSON;
- notebook U5 MongoDB sanitizado;
- documento de soporte U5 Etapa 1;
- checklist del video de demostración.

La estructura final permite reproducir y auditar la implementación.

## 11. Lecciones aprendidas

Durante la implementación se identificaron y resolvieron varios aspectos técnicos:

- conexión TLS/SSL desde Colab a MongoDB Atlas;
- uso de certifi para certificados;
- validación de IP y credenciales en Atlas;
- manejo de índices equivalentes en MongoDB;
- reutilización de índices existentes para evitar sobreindexación;
- construcción dinámica de pipelines para evitar campos None;
- aplicación segura de JSON Schema;
- sanitización de notebooks antes de subirlos a GitHub;
- documentación de sharding como diseño teórico, sin modificar el cluster real.

## 12. Conclusiones

La Etapa 2 consolida la implementación técnica completa de Ecommify en PostgreSQL y MongoDB.

PostgreSQL cubre el componente transaccional, estructurado y optimizado mediante índices, particionamiento, constraints y validaciones.

MongoDB cubre el componente documental y analítico, con colecciones especializadas, JSON Schema, Bucket Pattern, índices, pipelines y diseño de escalabilidad.

El repositorio queda actualizado y organizado para soportar el documento técnico evaluativo y el video de demostración.

## 13. Referencias

Pendiente de completar en el documento final:

- Guía de actividades Unidad 5.
- Fuentes bibliográficas Unidad 5.
- Documentación oficial PostgreSQL.
- Documentación oficial MongoDB.
- Documentos técnicos previos de Ecommify.
- Notebook y evidencias del repositorio.

## Anexos

Anexo A. Matriz de trazabilidad documento-rúbrica.

Anexo B. Inventario de archivos del repositorio.

Anexo C. Evidencias PostgreSQL.

Anexo D. Evidencias MongoDB.

Anexo E. Guion del video de demostración.


---

# Sección de soporte cuantitativo integrada

Las siguientes tablas consolidan las evidencias PostgreSQL y MongoDB disponibles en el repositorio para alimentar el documento técnico final.

Estas tablas no reemplazan el análisis narrativo del documento; sirven como base para seleccionar los resultados más relevantes que se incluirán en la versión Word/PDF.

---

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


---

# Tablas resumen MongoDB - U5 Etapa 2

Este archivo consolida las principales evidencias MongoDB que serán usadas en el documento técnico evaluativo.

## 1. Comparación antes/después de consultas MongoDB

| query_code | execution_time_ms_before | execution_time_ms_after | execution_time_improvement_pct | total_docs_examined_before | total_docs_examined_after | docs_examined_improvement_pct | plan_classification_before | plan_classification_after | technical_interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q01 | 1 | 5 | -400.0 | 2 | 2 | 0.0 | IXSCAN - Uso de índice | IXSCAN - Uso de índice | No se observa mejora significativa o la consulta ya estaba optimizada. |
| Q02 | 0 | 0 |  | 1 | 1 | 0.0 | IXSCAN - Uso de índice | IXSCAN - Uso de índice | No se observa mejora significativa o la consulta ya estaba optimizada. |
| Q03 | 0 | 3 |  | 1 | 1 | 0.0 | IXSCAN - Uso de índice | IXSCAN - Uso de índice | No se observa mejora significativa o la consulta ya estaba optimizada. |
| Q04 | 4 | 20 | -400.0 | 1000 | 1000 | 0.0 | COLLSCAN - Revisión completa de colección | IXSCAN - Uso de índice | Cambió de escaneo completo a uso de índice. |
| Q05 | 0 | 6 |  | 1 | 1 | 0.0 | IXSCAN - Uso de índice | IXSCAN - Uso de índice | No se observa mejora significativa o la consulta ya estaba optimizada. |
| Q06 | 42 | 106 | -152.38095238095238 | 15275 | 15275 | 0.0 | IXSCAN - Uso de índice | IXSCAN - Uso de índice | No se observa mejora significativa o la consulta ya estaba optimizada. |
| Q07 | 4 | 3 | 25.0 | 0 | 0 |  | IXSCAN - Uso de índice | IXSCAN - Uso de índice | Redujo tiempo de ejecución. |

## 2. Pipeline de agregación: base vs optimizado

| version | execution_time_ms | total_docs_examined | total_keys_examined | n_returned | indexes_used |
| --- | --- | --- | --- | --- | --- |
| BASE | 1 | 3 | 3 | 2 | ['idx_catalog_category_price', 'idx_catalog_category_sales', 'idx_category_name_translated... |
| OPTIMIZED | 1 | 3 | 3 | 2 | ['idx_catalog_category_price', 'idx_catalog_category_sales', 'idx_category_name_translated... |

## 3. Mejora porcentual del pipeline

| execution_time_improvement_pct | docs_examined_improvement_pct |
| --- | --- |
| 0.0 | 0.0 |

## 4. Stages del pipeline optimizado

| stage_order | stage | purpose |
| --- | --- | --- |
| 1 | $match | Filtrar temprano por categoría para reducir documentos procesados. |
| 2 | $project | Reducir campos antes de hacer lookup y agrupaciones. |
| 3 | $lookup | Unir productos del catálogo con sus reseñas. |
| 4 | $unwind | Descomponer el arreglo de reseñas para calcular métricas. |
| 5 | $group | Agrupar por categoría y calcular métricas agregadas. |
| 6 | $project | Formatear la salida final del análisis. |
| 7 | $sort | Ordenar categorías por desempeño comercial. |

## 5. Evidencia JSON Schema

| collection | validation_level | validation_action | validator_defined | validated_at |
| --- | --- | --- | --- | --- |
| product_catalog | moderate | error | True | 2026-06-16T11:43:38 |

## 6. Prueba de validación JSON Schema

| test | expected_result | actual_result | error_message | tested_at |
| --- | --- | --- | --- | --- |
| invalid_document_insert | REJECTED | REJECTED | Document failed validation, full error: {'index': 0, 'code': 121, 'errmsg': 'Document fail... | 2026-06-16T11:41:10 |

## 7. Evidencia Bucket Pattern

| pattern | source_collection | target_collection | grouping_strategy | bucket_size_limit | source_reviews | bucket_documents | purpose |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bucket Pattern | product_reviews | product_review_buckets | product_id + bucket_period + bucket_sequence | 50 | 102172 | 33038 | Agrupar reseñas por producto y periodo para reducir dispersión documental y facilitar cons... |

## 8. Índices de product_review_buckets

| index_name | keys | unique |
| --- | --- | --- |
| _id_ | {'_id': 1} | False |
| idx_review_buckets_product_period_sequence | {'product_id': 1, 'bucket_period': -1, 'bucket_sequence': 1} | True |
| idx_review_buckets_period_score | {'bucket_period': -1, 'avg_review_score': 1} | False |

## 9. Explain de consulta sobre product_review_buckets

| query_code | collection_name | operation | winning_plan_stage | index_name | total_docs_examined | total_keys_examined | execution_time_millis | result_returned_count | is_covered | is_sort_in_memory |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BKT01 | product_review_buckets | find | FETCH | idx_review_buckets_product_period_sequence | 1 | 1 | 0 | 1 | False | False |



---

# Anexo A. Matriz de trazabilidad documento-rúbrica

# Matriz de trazabilidad documento-rúbrica - U5 Etapa 2

Esta matriz relaciona las secciones del documento técnico evaluativo con los criterios de la guía/rúbrica y las evidencias disponibles en el repositorio.

| Sección del documento | Criterio de rúbrica | Evidencia en repo | Estado | Acción |
|---|---|---|---|---|
| 1. Resumen ejecutivo | Documento técnico de implementación | README.md; docs/u5_etapa2/; postgresql/README.md; mongodb/README.md | Pendiente redacción final | Resumir implementación completa PostgreSQL + MongoDB y resultados principales. |
| 2. Alcance y continuidad con Ecommify | Coherencia arquitectónica y continuidad del proyecto | docs/Documento_Tecnico_Diseno_Ecommify.pdf; README.md | Con evidencia | Explicar arquitectura híbrida transaccional-analítica. |
| 3. Implementación PostgreSQL en Supabase | Implementación PostgreSQL completa | postgresql/schema/; postgresql/queries/; postgresql/evidence/validation/ | Con evidencia | Documentar esquema core, tablas, constraints, extensiones, triggers y particionamiento. |
| 4. Optimización PostgreSQL | Optimización PostgreSQL con EXPLAIN, índices y particionamiento | postgresql/schema/05_indexes.sql; postgresql/schema/07_partitioning_orders.sql; postgresql/evidence/explain_before_after/ | Con evidencia documental | Usar manifiesto y documento U4 como soporte; agregar CSV reales si se recuperan. |
| 5. Implementación MongoDB en Atlas | Implementación MongoDB, patrones documentales y JSON Schema | mongodb/README.md; mongodb/schema/; mongodb/evidence/json_schema/; mongodb/evidence/bucket_pattern/ | Con evidencia | Documentar product_catalog, product_reviews, product_review_buckets, JSON Schema y patrones. |
| 6. Optimización MongoDB | Índices, explain executionStats y aggregation pipeline | mongodb/indexes/; mongodb/evidence/explain_before_after/; notebooks/Ecommify_U5_Etapa1_MongoDB.ipynb | Con evidencia | Documentar Q01-Q07, índices, comparación antes/después y pipeline optimizado. |
| 7. Evidencias cuantitativas consolidadas | Resultados cuantitativos de mejora | mongodb/evidence/explain_before_after/; postgresql/evidence/explain_before_after/ | Con evidencia parcial | Consolidar tablas de MongoDB y referenciar PostgreSQL U4; complementar si aparecen CSV reales. |
| 8. Sincronización entre PostgreSQL y MongoDB | Sincronización o integración entre sistemas | README.md; notebooks/; docs/Documento_Tecnico_Diseno_Ecommify.pdf | Pendiente redacción final | Explicar flujo batch/ETL académico, IDs compartidos y consistencia eventual. |
| 9. Sharding y replica sets | Escalabilidad MongoDB y replica sets | mongodb/sharding/sharding_replica_set_design.md | Con evidencia | Documentar shard keys candidatas, decisión final y limitaciones del entorno. |
| 10. Repositorio GitHub actualizado | Repositorio reproducible, README, scripts, notebooks y evidencias | README.md; postgresql/README.md; mongodb/README.md; notebooks/; evidence/video/ | Con evidencia | Incluir enlace final del repo y explicar estructura. |
| 11. Lecciones aprendidas | Lecciones, obstáculos y decisiones técnicas | notebooks/; mongodb/evidence/; postgresql/evidence/ | Pendiente redacción final | Documentar TLS, índices equivalentes, pipeline dinámico, free tier y sanitización de notebooks. |
| 12. Conclusiones | Cierre evaluativo | Todo el repositorio actualizado | Pendiente redacción final | Cerrar cumplimiento PostgreSQL, MongoDB, optimización, repo y video. |
| 13. Referencias | Uso de fuentes bibliográficas | Guía U5; fuentes Unidad 5; documentos previos del proyecto | Pendiente redacción final | Incluir guía, fuentes MongoDB/PostgreSQL y documentos previos. |
| Anexos | Evidencias complementarias | docs/u5_etapa2/; postgresql/evidence/; mongodb/evidence/; evidence/video/ | Con evidencia | Agregar matriz, inventario de archivos, evidencias y guion de video. |


---

# Anexo B. Inventario de archivos del repositorio

# Inventario de archivos del repositorio - U5 Etapa 2

Este archivo resume los artefactos disponibles en el repositorio para soportar el documento técnico evaluativo.

## Resumen por categoría

| Categoría | Total archivos |
|---|---:|
| Capturas | 1 |
| Documentación | 9 |
| MongoDB - evidencias | 16 |
| MongoDB - otros | 1 |
| MongoDB - queries/scripts | 2 |
| MongoDB - schema | 5 |
| MongoDB - sharding/replica set | 2 |
| MongoDB - índices | 2 |
| Notebooks | 3 |
| PostgreSQL - evidencias | 6 |
| PostgreSQL - otros | 3 |
| PostgreSQL - queries | 2 |
| PostgreSQL - scripts DDL | 9 |
| README raíz | 1 |
| Video | 2 |

## Inventario detallado

| Ruta | Categoría | Extensión | Tamaño bytes |
|---|---|---|---:|
| README.md | README raíz | .md | 4683 |
| docs/.gitkeep | Documentación | sin_extension | 0 |
| docs/Documento_Tecnico_Diseno_Ecommify.pdf | Documentación | .pdf | 649301 |
| docs/Presentacion_Ejecutiva_Ecommify.pdf | Documentación | .pdf | 272253 |
| docs/u5_etapa2/.gitkeep | Documentación | sin_extension | 0 |
| docs/u5_etapa2/Ecommify_U5_Etapa1_Optimizacion_MongoDB.pdf | Documentación | .pdf | 589705 |
| docs/u5_etapa2/documento_tecnico_estructura.md | Documentación | .md | 7292 |
| docs/u5_etapa2/documento_tecnico_fuentes.md | Documentación | .md | 3583 |
| docs/u5_etapa2/matriz_trazabilidad_documento_rubrica.csv | Documentación | .csv | 3506 |
| docs/u5_etapa2/matriz_trazabilidad_documento_rubrica.md | Documentación | .md | 3894 |
| evidence/screenshots/.gitkeep | Capturas | sin_extension | 0 |
| evidence/video/.gitkeep | Video | sin_extension | 0 |
| evidence/video/video_demo_checklist.md | Video | .md | 2918 |
| mongodb/README.md | MongoDB - otros | .md | 4325 |
| mongodb/evidence/bucket_pattern/.gitkeep | MongoDB - evidencias | sin_extension | 0 |
| mongodb/evidence/bucket_pattern/product_review_buckets_sample.json | MongoDB - evidencias | .json | 735 |
| mongodb/evidence/bucket_pattern/u5_etapa2_mongodb_bucket_explain_summary.csv | MongoDB - evidencias | .csv | 283 |
| mongodb/evidence/bucket_pattern/u5_etapa2_mongodb_bucket_indexes.csv | MongoDB - evidencias | .csv | 241 |
| mongodb/evidence/bucket_pattern/u5_etapa2_mongodb_bucket_pattern_evidence.csv | MongoDB - evidencias | .csv | 346 |
| mongodb/evidence/bucket_pattern/u5_etapa2_mongodb_bucket_query_sample.csv | MongoDB - evidencias | .csv | 215 |
| mongodb/evidence/explain_before_after/.gitkeep | MongoDB - evidencias | sin_extension | 0 |
| mongodb/evidence/explain_before_after/hito3_baseline_explain_summary.csv | MongoDB - evidencias | .csv | 1798 |
| mongodb/evidence/explain_before_after/hito5_before_after_comparison.csv | MongoDB - evidencias | .csv | 2689 |
| mongodb/evidence/explain_before_after/hito5_optimized_explain_summary.csv | MongoDB - evidencias | .csv | 1821 |
| mongodb/evidence/explain_before_after/hito6_pipeline_comparison.csv | MongoDB - evidencias | .csv | 461 |
| mongodb/evidence/explain_before_after/hito6_pipeline_improvement.csv | MongoDB - evidencias | .csv | 69 |
| mongodb/evidence/explain_before_after/hito6_pipeline_stages.csv | MongoDB - evidencias | .csv | 464 |
| mongodb/evidence/json_schema/.gitkeep | MongoDB - evidencias | sin_extension | 0 |
| mongodb/evidence/json_schema/u5_etapa2_mongodb_json_schema_evidence.csv | MongoDB - evidencias | .csv | 133 |
| mongodb/evidence/json_schema/u5_etapa2_mongodb_json_schema_validation_test.csv | MongoDB - evidencias | .csv | 1154 |
| mongodb/indexes/.gitkeep | MongoDB - índices | sin_extension | 0 |
| mongodb/indexes/mongodb_indexes.py | MongoDB - índices | .py | 10202 |
| mongodb/queries/.gitkeep | MongoDB - queries/scripts | sin_extension | 0 |
| mongodb/queries/build_product_review_buckets.py | MongoDB - queries/scripts | .py | 9188 |
| mongodb/schema/apply_product_catalog_json_schema.py | MongoDB - schema | .py | 2562 |
| mongodb/schema/customer_events_schema.json | MongoDB - schema | .json | 1471 |
| mongodb/schema/product_catalog_json_schema_validator.json | MongoDB - schema | .json | 2327 |
| mongodb/schema/product_catalog_schema.json | MongoDB - schema | .json | 1666 |
| mongodb/schema/product_reviews_schema.json | MongoDB - schema | .json | 1627 |
| mongodb/sharding/.gitkeep | MongoDB - sharding/replica set | sin_extension | 0 |
| mongodb/sharding/sharding_replica_set_design.md | MongoDB - sharding/replica set | .md | 4790 |
| notebooks/.gitkeep | Notebooks | sin_extension | 0 |
| notebooks/EcommifyActividad1_Olist.ipynb | Notebooks | .ipynb | 657910 |
| notebooks/Ecommify_U5_Etapa1_MongoDB.ipynb | Notebooks | .ipynb | 863502 |
| postgresql/README.md | PostgreSQL - otros | .md | 3608 |
| postgresql/evidence/explain_before_after/.gitkeep | PostgreSQL - evidencias | sin_extension | 0 |
| postgresql/evidence/explain_before_after/README.md | PostgreSQL - evidencias | .md | 842 |
| postgresql/evidence/explain_before_after/pg_explain_before_after_manifest.csv | PostgreSQL - evidencias | .csv | 636 |
| postgresql/evidence/validation/.gitkeep | PostgreSQL - evidencias | sin_extension | 0 |
| postgresql/evidence/validation/pg_validation_checklist.csv | PostgreSQL - evidencias | .csv | 975 |
| postgresql/evidence/validation/pg_validation_summary.md | PostgreSQL - evidencias | .md | 1343 |
| postgresql/indexes/.gitkeep | PostgreSQL - otros | sin_extension | 0 |
| postgresql/queries/11_validation_queries.sql | PostgreSQL - queries | .sql | 719 |
| postgresql/queries/12_monitoring_queries.sql | PostgreSQL - queries | .sql | 773 |
| postgresql/schema/00_extensions.sql | PostgreSQL - scripts DDL | .sql | 371 |
| postgresql/schema/01_schemas.sql | PostgreSQL - scripts DDL | .sql | 312 |
| postgresql/schema/02_types_domains.sql | PostgreSQL - scripts DDL | .sql | 1008 |
| postgresql/schema/03_tables_core.sql | PostgreSQL - scripts DDL | .sql | 1863 |
| postgresql/schema/04_tables_transactions.sql | PostgreSQL - scripts DDL | .sql | 2846 |
| postgresql/schema/05_indexes.sql | PostgreSQL - scripts DDL | .sql | 1234 |
| postgresql/schema/06_triggers_updated_at.sql | PostgreSQL - scripts DDL | .sql | 984 |
| postgresql/schema/07_partitioning_orders.sql | PostgreSQL - scripts DDL | .sql | 673 |
| postgresql/schema/08_materialized_views.sql | PostgreSQL - scripts DDL | .sql | 1790 |
| postgresql/seed_data/10_seed_data.sql | PostgreSQL - otros | .sql | 657 |

