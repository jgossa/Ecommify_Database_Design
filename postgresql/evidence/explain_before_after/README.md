# Evidencias PostgreSQL - EXPLAIN antes/después

Esta carpeta reúne la evidencia de rendimiento PostgreSQL usada para la Unidad 5 Etapa 2.

La optimización PostgreSQL fue desarrollada previamente en la Unidad 4 Etapa 2 sobre Supabase, usando el esquema `core` de Ecommify.

## Evidencias documentadas

La implementación PostgreSQL incluyó:

- definición de consultas críticas Q01-Q09;
- medición base con `EXPLAIN (ANALYZE, BUFFERS)`;
- análisis de planes base;
- optimizaciones SQL;
- creación de índices especializados;
- medición posterior con `EXPLAIN (ANALYZE, BUFFERS)`;
- comparación antes/después;
- validación de particionamiento declarativo de `core.orders`.

## Referencia principal

La evidencia detallada se encuentra documentada en el entregable:

`Ecommify_U4_Etapa2_Implementacion_Optimizacion_PostgreSQL.pdf`

## Archivos esperados si se exportan desde Colab

Cuando estén disponibles los CSV del notebook U4, pueden agregarse aquí con nombres como:

- pg_baseline_explain_summary.csv
- pg_post_optimization_explain_summary.csv
- pg_before_after_comparison.csv
- pg_partitioning_comparison.csv
- pg_index_size_summary.csv

## Nota de alcance

Esta carpeta no reconstruye las métricas manualmente. Su propósito es organizar la evidencia PostgreSQL de rendimiento y dejar trazabilidad hacia el documento y notebook donde se ejecutaron las mediciones.
