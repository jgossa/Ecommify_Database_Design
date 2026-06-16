# Estructura del documento técnico evaluativo - U5 Etapa 2

Este archivo define la estructura del documento técnico final de la Unidad 5, Etapa 2: Implementación técnica completa en PostgreSQL y MongoDB.

El documento final debe cubrir únicamente lo solicitado por la guía y la rúbrica, sin agregar secciones innecesarias.

## Portada

Contenido:

- Nombre del entregable.
- Proyecto: Ecommify.
- Unidad 5, Etapa 2.
- Equipo E21.
- Integrantes.
- Programa académico.
- Docente.
- Fecha.
- Enlace al repositorio GitHub actualizado.
- Enlace al video de demostración, cuando esté disponible.

## 1. Resumen ejecutivo

Objetivo:

Presentar de forma breve qué se implementó y qué resultados se obtuvieron.

Debe incluir:

- síntesis de la implementación realizada;
- arquitectura híbrida PostgreSQL + MongoDB;
- principales optimizaciones aplicadas;
- resultados cuantitativos destacados;
- ubicación de evidencias en el repositorio.

Evidencias base:

- README.md
- postgresql/README.md
- mongodb/README.md
- mongodb/evidence/explain_before_after/
- postgresql/evidence/explain_before_after/
- docs/u5_etapa2/

## 2. Alcance y continuidad con Ecommify

Objetivo:

Explicar que la Etapa 2 consolida la implementación técnica completa, sin romper la continuidad de las unidades anteriores.

Debe incluir:

- PostgreSQL como núcleo transaccional;
- MongoDB como complemento documental y analítico;
- uso de Supabase, MongoDB Atlas y Google Colab;
- límites del prototipo académico;
- relación con documentos previos de diseño.

Evidencias base:

- docs/Documento_Tecnico_Diseno_Ecommify.pdf
- README.md
- docs/u5_etapa2/documento_tecnico_fuentes.md

## 3. Implementación PostgreSQL en Supabase

Objetivo:

Documentar la implementación relacional/transaccional.

Debe incluir:

- esquema core;
- tablas principales;
- scripts DDL ejecutados;
- constraints;
- tipos avanzados;
- extensiones;
- triggers;
- vistas materializadas;
- particionamiento de core.orders;
- validación final ejecutada en Supabase.

Evidencias base:

- postgresql/schema/
- postgresql/queries/
- postgresql/evidence/validation/
- postgresql/README.md

## 4. Optimización PostgreSQL

Objetivo:

Documentar la estrategia de optimización aplicada sobre PostgreSQL.

Debe incluir:

- consultas críticas Q01-Q09;
- medición base con EXPLAIN ANALYZE BUFFERS;
- índices especializados;
- particionamiento declarativo;
- medición posterior;
- comparación antes/después;
- interpretación del impacto.

Evidencias base:

- postgresql/schema/05_indexes.sql
- postgresql/schema/07_partitioning_orders.sql
- postgresql/evidence/explain_before_after/
- documento U4 Etapa 2 PostgreSQL

## 5. Implementación MongoDB en Atlas

Objetivo:

Documentar la implementación documental.

Debe incluir:

- colecciones product_catalog, product_reviews y product_review_buckets;
- esquema documental;
- JSON Schema aplicado a product_catalog;
- Attribute Pattern;
- Extended Reference Pattern;
- Bucket Pattern;
- decisiones de embedding y referencing;
- evidencias de validación.

Evidencias base:

- mongodb/README.md
- mongodb/schema/
- mongodb/evidence/json_schema/
- mongodb/evidence/bucket_pattern/
- mongodb/queries/build_product_review_buckets.py

## 6. Optimización MongoDB

Objetivo:

Documentar la optimización de consultas y pipelines en MongoDB.

Debe incluir:

- consultas críticas Q01-Q07;
- línea base con explain executionStats;
- índices compuestos;
- índices parciales;
- índice de texto reutilizado;
- comparación antes/después;
- pipeline base y pipeline optimizado;
- interpretación de métricas.

Evidencias base:

- mongodb/indexes/mongodb_indexes.py
- mongodb/evidence/explain_before_after/
- mongodb/evidence/bucket_pattern/u5_etapa2_mongodb_bucket_explain_summary.csv
- notebooks/Ecommify_U5_Etapa1_MongoDB.ipynb

## 7. Evidencias cuantitativas consolidadas

Objetivo:

Presentar en una sola sección los resultados de rendimiento.

Debe incluir:

- tabla PostgreSQL antes/después;
- tabla MongoDB antes/después;
- métricas de executionTimeMillis;
- documentos examinados;
- llaves examinadas;
- efficiency ratios;
- explicación de mejoras observadas y casos sin mejora significativa.

Evidencias base:

- postgresql/evidence/explain_before_after/
- mongodb/evidence/explain_before_after/
- mongodb/evidence/bucket_pattern/
- docs/u5_etapa2/Ecommify_U5_Etapa1_Optimizacion_MongoDB.pdf

## 8. Sincronización entre PostgreSQL y MongoDB

Objetivo:

Explicar cómo se relacionan ambos motores dentro de la arquitectura.

Debe incluir:

- PostgreSQL como fuente transaccional principal;
- MongoDB como vista documental/analítica;
- flujo batch o ETL académico desde datos Olist;
- uso de identificadores compartidos como product_id, order_id y seller_id;
- uso de campos updated_at;
- estrategia de consistencia eventual;
- limitaciones de no tener sincronización productiva real.

Evidencias base:

- Documento técnico de diseño Ecommify.
- README.md.
- notebooks/Ecommify_U5_Etapa1_MongoDB.ipynb.

## 9. Sharding y replica sets

Objetivo:

Documentar la estrategia teórica de escalabilidad MongoDB.

Debe incluir:

- análisis de shard keys candidatas;
- decisión para product_catalog;
- decisión para product_reviews;
- simulación de distribución;
- estrategia de replica set;
- read preferences;
- read concern;
- write concern;
- limitaciones del entorno Atlas académico.

Evidencias base:

- mongodb/sharding/sharding_replica_set_design.md
- mongodb/evidence/explain_before_after/
- docs/u5_etapa2/Ecommify_U5_Etapa1_Optimizacion_MongoDB.pdf

## 10. Repositorio GitHub actualizado

Objetivo:

Evidenciar que el repositorio quedó organizado y reproducible.

Debe incluir:

- enlace al repositorio;
- estructura general;
- scripts PostgreSQL;
- scripts MongoDB;
- notebooks;
- evidencias;
- README raíz;
- README PostgreSQL;
- README MongoDB;
- checklist del video.

Evidencias base:

- README.md
- postgresql/README.md
- mongodb/README.md
- evidence/video/video_demo_checklist.md

## 11. Lecciones aprendidas

Objetivo:

Documentar obstáculos y soluciones aplicadas.

Debe incluir:

- conexión TLS/SSL desde Colab a MongoDB Atlas;
- validación de IP y certificados;
- conflictos por índices equivalentes en MongoDB;
- campos None en pipelines dinámicos;
- limitaciones de Atlas/Supabase free tier;
- decisión de no habilitar sharding real;
- importancia de sanitizar notebooks antes de subirlos a GitHub.

Evidencias base:

- notebooks/Ecommify_U5_Etapa1_MongoDB.ipynb
- mongodb/evidence/
- postgresql/evidence/
- repo GitHub actualizado

## 12. Conclusiones

Objetivo:

Cerrar el documento con resultados y cumplimiento.

Debe incluir:

- cumplimiento de PostgreSQL;
- cumplimiento de MongoDB;
- cumplimiento de optimización;
- cumplimiento de repositorio;
- relación con video;
- alcance real del prototipo.

## 13. Referencias

Debe incluir:

- guía de actividades Unidad 5;
- documentos técnicos previos de Ecommify;
- documentación oficial PostgreSQL;
- documentación oficial MongoDB;
- fuentes bibliográficas de la Unidad 5.

## Anexos

Anexo A. Matriz de cumplimiento de rúbrica.

Anexo B. Inventario de archivos del repositorio.

Anexo C. Evidencias PostgreSQL.

Anexo D. Evidencias MongoDB.

Anexo E. Guion del video de demostración.
