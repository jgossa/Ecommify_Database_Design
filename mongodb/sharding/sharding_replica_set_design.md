# Sharding y replica sets - Diseño teórico MongoDB Ecommify

Este documento resume la estrategia teórica de sharding, replica set y concerns para el componente MongoDB de Ecommify.

La implementación real de sharding no se ejecutó sobre MongoDB Atlas, porque el alcance académico y el entorno usado no requieren modificar el clúster real. En su lugar, se realizó análisis de distribución y simulación con datos reales de `product_catalog`.

## Colecciones analizadas

| Colección | Rol | Estrategia |
|---|---|---|
| product_catalog | Catálogo enriquecido de productos | Candidata a sharding por categoría y producto |
| product_reviews | Reseñas referenciadas por producto | Candidata a sharding por product_id |
| product_review_buckets | Colección derivada para Bucket Pattern | Consulta por product_id y periodo |

## Análisis de distribución

El análisis de distribución se realizó sobre `product_catalog`, agrupando productos por categoría.

Objetivos del análisis:

- identificar concentración por categoría;
- calcular participación máxima;
- calcular HHI de concentración;
- simular distribución en tres shards;
- comparar estrategias candidatas de shard key.

## Estrategias evaluadas

| Estrategia | Ventajas | Riesgos | Decisión |
|---|---|---|---|
| category | Favorece consultas por categoría | Puede generar hotspots si una categoría concentra muchos documentos | No seleccionada como única clave |
| hashed product_id | Distribuye documentos de forma balanceada | Consultas por categoría pueden requerir fan-out | Candidata para balance |
| category + hashed product_id | Combina localidad lógica por categoría con mejor distribución | Mayor complejidad de diseño e índices compatibles | Seleccionada para product_catalog |
| hashed product_id en product_reviews | Favorece consultas de reseñas por producto | Agregaciones globales pueden consultar varios shards | Seleccionada para product_reviews |

## Shard keys propuestas

### product_catalog

Shard key teórica propuesta:

    { "category.name_translated": 1, "product_id": "hashed" }

Justificación:

- `category.name_translated` ayuda a consultas frecuentes por categoría.
- `product_id` con hash mejora la distribución.
- La combinación reduce el riesgo de concentración en un único shard.

### product_reviews

Shard key teórica propuesta:

    { "product_id": "hashed" }

Justificación:

- Las reseñas se consultan principalmente por producto.
- `product_id` es estable y de alta cardinalidad.
- El hash ayuda a distribuir reseñas entre shards.

## Comandos teóricos de sharding

Estos comandos son solo documentación técnica. No se ejecutaron en el entorno real.

    sh.enableSharding("ecommify_mongodb")

    sh.shardCollection(
      "ecommify_mongodb.product_catalog",
      { "category.name_translated": 1, "product_id": "hashed" }
    )

    sh.shardCollection(
      "ecommify_mongodb.product_reviews",
      { "product_id": "hashed" }
    )

## Estrategia de replica set

Se propone una arquitectura lógica con:

| Componente | Rol | Uso en Ecommify |
|---|---|---|
| Primary | Atiende escrituras | Actualización de catálogo, carga de reseñas y cambios controlados |
| Secondary 1 | Replica datos y atiende lecturas no críticas | Consultas analíticas o de catálogo |
| Secondary 2 | Soporta alta disponibilidad y failover | Continuidad operativa ante falla del primary |

## Read preference, read concern y write concern

| Tipo de operación | Consultas asociadas | Read preference | Read concern | Write concern | Justificación |
|---|---|---|---|---|---|
| Lectura de catálogo | Q01, Q02, Q03, Q04 | secondaryPreferred | local | No aplica | Catálogo tolera ligera latencia de réplica |
| Lectura de reseñas por producto | Q05 | primaryPreferred | majority | No aplica | Las reseñas recientes pueden requerir más consistencia |
| Análisis de reseñas críticas | Q06 | secondaryPreferred | local | No aplica | Consulta analítica tolerante a consistencia eventual |
| Carga o actualización documental | Inserts/updates | No aplica | No aplica | majority | Prioriza durabilidad de escritura |

## Decisiones finales

| Tema | Decisión |
|---|---|
| Shard key product_catalog | category + hashed product_id |
| Shard key product_reviews | hashed product_id |
| Replica set | 1 primary + 2 secondaries |
| Write concern | majority para cargas y actualizaciones |
| Read preference | secondaryPreferred para analítica; primaryPreferred para datos recientes |

## Limitaciones

- No se habilitó sharding real en Atlas.
- Los comandos de sharding son teóricos.
- La simulación se realizó con los datos disponibles del prototipo académico.
- La estrategia debe revalidarse si el volumen de datos o los patrones de consulta cambian.
