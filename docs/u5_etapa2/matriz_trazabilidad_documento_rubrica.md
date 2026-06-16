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
