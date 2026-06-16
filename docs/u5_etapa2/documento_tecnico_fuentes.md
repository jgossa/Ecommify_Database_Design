# Fuentes del documento técnico - U5 Etapa 2

Este archivo lista los insumos que alimentan el documento técnico evaluativo de la Unidad 5, Etapa 2.

## Documento técnico requerido por la guía

El documento final debe cubrir:

- resumen ejecutivo;
- implementación PostgreSQL;
- implementación MongoDB;
- evidencias cuantitativas de mejoras de rendimiento;
- sincronización entre sistemas;
- lecciones aprendidas;
- referencia al repositorio GitHub actualizado;
- referencia al video de demostración.

## Insumos PostgreSQL

| Insumo | Ruta en repo | Uso en documento |
|---|---|---|
| README PostgreSQL | postgresql/README.md | Describir estructura, scripts y alcance PostgreSQL. |
| Scripts DDL | postgresql/schema/ | Evidenciar esquema, extensiones, tablas, índices, triggers, particionamiento y vistas materializadas. |
| Seed data | postgresql/seed_data/10_seed_data.sql | Documentar carga o datos semilla si aplica. |
| Queries de validación | postgresql/queries/11_validation_queries.sql | Sustentar validaciones del esquema core. |
| Queries de monitoreo | postgresql/queries/12_monitoring_queries.sql | Sustentar monitoreo PostgreSQL. |
| Evidencia de validación | postgresql/evidence/validation/ | Evidenciar validación final de Supabase/PostgreSQL. |
| Evidencia EXPLAIN | postgresql/evidence/explain_before_after/ | Referenciar análisis antes/después documentado en U4 Etapa 2. |

## Insumos MongoDB

| Insumo | Ruta en repo | Uso en documento |
|---|---|---|
| README MongoDB | mongodb/README.md | Describir modelo documental, colecciones y scripts. |
| JSON Schema | mongodb/schema/product_catalog_json_schema_validator.json | Evidenciar validación de esquema para product_catalog. |
| Script JSON Schema | mongodb/schema/apply_product_catalog_json_schema.py | Evidenciar reproducibilidad del validator. |
| Script índices | mongodb/indexes/mongodb_indexes.py | Documentar índices creados/reutilizados. |
| Script Bucket Pattern | mongodb/queries/build_product_review_buckets.py | Evidenciar Bucket Pattern. |
| Diseño sharding/replica set | mongodb/sharding/sharding_replica_set_design.md | Documentar escalabilidad teórica. |
| Evidencias JSON Schema | mongodb/evidence/json_schema/ | Evidenciar prueba de validación documental. |
| Evidencias Bucket Pattern | mongodb/evidence/bucket_pattern/ | Evidenciar colección product_review_buckets. |
| Evidencias explain MongoDB | mongodb/evidence/explain_before_after/ | Sustentar comparación antes/después y pipeline. |

## Insumos de notebooks y documentos previos

| Insumo | Ruta en repo | Uso en documento |
|---|---|---|
| Notebook U5 MongoDB | notebooks/Ecommify_U5_Etapa1_MongoDB.ipynb | Trazabilidad de implementación MongoDB por hitos. |
| Documento U5 Etapa 1 | docs/u5_etapa2/Ecommify_U5_Etapa1_Optimizacion_MongoDB.pdf | Base documental para optimización MongoDB. |
| Documento diseño Ecommify | docs/Documento_Tecnico_Diseno_Ecommify.pdf | Continuidad arquitectónica. |
| Presentación ejecutiva previa | docs/Presentacion_Ejecutiva_Ecommify.pdf | Contexto del proyecto. |

## Insumos de video

| Insumo | Ruta en repo | Uso en documento |
|---|---|---|
| Checklist video | evidence/video/video_demo_checklist.md | Referencia para guion de demostración. |

## Pendientes antes de generar el documento final

- Confirmar enlace final del repositorio GitHub en main.
- Confirmar enlace final del video cuando esté grabado.
- Confirmar si se agregarán CSV reales adicionales de PostgreSQL EXPLAIN.
- Generar documento final en Word y PDF.
- Copiar documento final a docs/u5_etapa2/.
