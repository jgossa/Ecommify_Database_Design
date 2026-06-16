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

