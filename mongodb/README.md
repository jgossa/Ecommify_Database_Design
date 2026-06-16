# MongoDB - Implementación documental Ecommify

Esta carpeta contiene la implementación MongoDB del proyecto Ecommify para la Unidad 5.

MongoDB se usa como complemento documental y analítico del modelo transaccional en PostgreSQL. Su objetivo es soportar consultas flexibles sobre catálogo enriquecido, reseñas, búsqueda textual, agregaciones y patrones de modelado documental.

## Colecciones principales

### product_catalog

Colección documental para catálogo enriquecido de productos.

Incluye información como:

* product_id
* name
* category
* price_summary
* specifications
* seller_summary
* rating_summary
* sales_summary
* search_keywords
* created_at
* updated_at

Esta colección aplica principalmente:

* Attribute Pattern, mediante `specifications`.
* Extended Reference, mediante resúmenes como `seller_summary` y referencias por `product_id`.
* Computed Pattern, mediante campos agregados como `rating_summary` y `sales_summary`.

### product_reviews

Colección referenciada de reseñas por producto.

Se usa para consultas de reseñas, análisis de satisfacción y construcción de estructuras derivadas.

### product_review_buckets

Colección derivada creada para evidenciar Bucket Pattern.

Agrupa reseñas por:

* product_id
* bucket_period
* bucket_sequence

Cada bucket contiene varias reseñas embebidas y métricas precalculadas como:

* review_count
* avg_review_score
* min_review_score
* max_review_score

## Estructura de carpetas

```text
mongodb/
├── README.md
├── schema/
│   ├── product_catalog_json_schema_validator.json
│   └── apply_product_catalog_json_schema.py
├── indexes/
│   └── mongodb_indexes.py
├── queries/
│   └── build_product_review_buckets.py
├── sharding/
├── evidence/
│   ├── json_schema/
│   ├── bucket_pattern/
│   ├── explain_before_after/
│   └── indexes/
```

## Scripts principales

### Aplicar JSON Schema

```bash
export MONGODB_URI="mongodb+srv://usuario:password@cluster.mongodb.net/?retryWrites=true&w=majority"
python mongodb/schema/apply_product_catalog_json_schema.py
```

Este script aplica el validador JSON Schema sobre `product_catalog`.

### Crear índices MongoDB

```bash
export MONGODB_URI="mongodb+srv://usuario:password@cluster.mongodb.net/?retryWrites=true&w=majority"
python mongodb/indexes/mongodb_indexes.py
```

Este script crea o reutiliza índices para:

* product_catalog
* product_reviews
* product_review_buckets

### Construir Bucket Pattern

```bash
export MONGODB_URI="mongodb+srv://usuario:password@cluster.mongodb.net/?retryWrites=true&w=majority"
python mongodb/queries/build_product_review_buckets.py
```

Este script reconstruye la colección derivada `product_review_buckets` a partir de `product_reviews`.

## Evidencias disponibles

### JSON Schema

Ubicación:

```text
mongodb/evidence/json_schema/
```

Archivos:

* u5_etapa2_mongodb_json_schema_evidence.csv
* u5_etapa2_mongodb_json_schema_validation_test.csv

### Bucket Pattern

Ubicación:

```text
mongodb/evidence/bucket_pattern/
```

Archivos:

* u5_etapa2_mongodb_bucket_pattern_evidence.csv
* u5_etapa2_mongodb_bucket_indexes.csv
* u5_etapa2_mongodb_bucket_query_sample.csv
* u5_etapa2_mongodb_bucket_explain_summary.csv
* product_review_buckets_sample.json

### Índices

Ubicación:

```text
mongodb/evidence/indexes/
```

Archivo esperado:

* mongodb_index_creation_log.csv

## Sharding y replica sets

El sharding se maneja como diseño teórico y simulación, no como cambio real sobre el clúster Atlas.

La estrategia propuesta para `product_catalog` es:

```text
category + hashed product_id
```

La estrategia propuesta para `product_reviews` es:

```text
hashed product_id
```

La estrategia de replica set considera:

* primary para escrituras;
* secondaries para lecturas no críticas;
* write concern `majority` para cargas o actualizaciones;
* read preference `secondaryPreferred` para analítica tolerante a latencia.

## Notas de alcance

* No se reemplaza PostgreSQL.
* No se recargan datos fuente.
* No se elimina `product_catalog` ni `product_reviews`.
* `product_review_buckets` es una colección derivada para evidenciar Bucket Pattern.
* El sharding se documenta de forma teórica/simulada, sin modificar el cluster real de Atlas.
