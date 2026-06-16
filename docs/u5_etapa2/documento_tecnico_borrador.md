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
