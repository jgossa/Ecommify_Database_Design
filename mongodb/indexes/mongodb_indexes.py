"""
Crea o reutiliza índices MongoDB para Ecommify.

Uso:
  export MONGODB_URI="mongodb+srv://usuario:password@cluster.mongodb.net/?retryWrites=true&w=majority"
  python mongodb/indexes/mongodb_indexes.py

Notas:
- No elimina colecciones.
- No recarga datos.
- Evita duplicar índice de texto si ya existe.
- Registra evidencia en mongodb/evidence/indexes/mongodb_index_creation_log.csv.
"""

import csv
import json
import os
from datetime import datetime, timezone
from pathlib import Path

import certifi
from pymongo import ASCENDING, DESCENDING, TEXT, MongoClient
from pymongo.errors import OperationFailure
from pymongo.server_api import ServerApi


DATABASE_NAME = os.getenv("MONGODB_DATABASE", "ecommify_mongodb")

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
EVIDENCE_DIR = REPO_ROOT / "mongodb" / "evidence" / "indexes"
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

INDEX_LOG_FILE = EVIDENCE_DIR / "mongodb_index_creation_log.csv"


def flatten_keys(document, parent_key="", separator="."):
    keys = []

    if isinstance(document, dict):
        for key, value in document.items():
            new_key = f"{parent_key}{separator}{key}" if parent_key else key
            keys.append(new_key)

            if isinstance(value, dict):
                keys.extend(flatten_keys(value, new_key, separator))

            elif isinstance(value, list) and value and isinstance(value[0], dict):
                keys.extend(flatten_keys(value[0], new_key, separator))

    return keys


def pick_field(available_fields, candidates):
    for field in candidates:
        if field in available_fields:
            return field
    return None


def create_index_safely(log_rows, collection, keys, name, index_type, purpose, **options):
    try:
        index_name = collection.create_index(keys, name=name, **options)
        status = "OK"
        error = None

    except OperationFailure as exc:
        message = str(exc)

        if "already exists" in message or "equivalent index already exists" in message:
            index_name = name
            status = "REUSED_OR_EXISTING"
            error = message
        else:
            index_name = name
            status = "ERROR"
            error = message

    log_rows.append({
        "collection": collection.name,
        "index_name": index_name,
        "keys": json.dumps(keys, ensure_ascii=False),
        "index_type": index_type,
        "purpose": purpose,
        "status": status,
        "error": error,
        "created_at": datetime.now(timezone.utc).isoformat()
    })

    print(f"{status} - {collection.name}.{index_name}")


def text_index_exists(collection):
    for index in collection.list_indexes():
        keys = dict(index.get("key", {}))
        if keys.get("_fts") == "text":
            return index

    return None


def category_index_exists(collection, category_field):
    for index in collection.list_indexes():
        keys = dict(index.get("key", {}))
        if category_field in keys:
            return index

    return None


def write_csv(path, rows):
    fieldnames = [
        "collection",
        "index_name",
        "keys",
        "index_type",
        "purpose",
        "status",
        "error",
        "created_at"
    ]

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main():
    mongodb_uri = os.getenv("MONGODB_URI")

    if not mongodb_uri:
        raise RuntimeError(
            "Falta MONGODB_URI. "
            "Ejemplo: export MONGODB_URI='mongodb+srv://usuario:password@cluster.mongodb.net/?retryWrites=true&w=majority'"
        )

    client = MongoClient(
        mongodb_uri,
        tls=True,
        tlsCAFile=certifi.where(),
        server_api=ServerApi("1"),
        serverSelectionTimeoutMS=30000
    )

    client.admin.command("ping")
    print("Conexión exitosa a MongoDB Atlas.")

    db = client[DATABASE_NAME]

    product_catalog = db["product_catalog"]
    product_reviews = db["product_reviews"]
    product_review_buckets = db["product_review_buckets"]

    sample_catalog = product_catalog.find_one()
    sample_review = product_reviews.find_one()

    if not sample_catalog:
        raise RuntimeError("product_catalog no tiene documentos.")

    if not sample_review:
        raise RuntimeError("product_reviews no tiene documentos.")

    catalog_fields = set(flatten_keys(sample_catalog))
    review_fields = set(flatten_keys(sample_review))

    category_field = pick_field(catalog_fields, [
        "category.name_translated",
        "category.name",
        "category"
    ])

    price_field = pick_field(catalog_fields, [
        "price_summary.avg_price",
        "price_summary.average_price",
        "price_summary.mean_price",
        "price_summary.min_price",
        "price_summary.max_price",
        "price_summary.price"
    ])

    sales_field = pick_field(catalog_fields, [
        "sales_summary.total_sales",
        "sales_summary.total_orders",
        "sales_summary.units_sold",
        "sales_summary.count"
    ])

    review_score_field = pick_field(review_fields, [
        "review_score",
        "score",
        "rating"
    ])

    review_date_field = pick_field(review_fields, [
        "review_creation_date",
        "review_created_at",
        "created_at"
    ])

    log_rows = []

    if category_field and sales_field:
        create_index_safely(
            log_rows,
            product_catalog,
            [(category_field, ASCENDING), (sales_field, DESCENDING)],
            "idx_catalog_category_sales",
            "compound",
            "Optimizar navegación de catálogo por categoría y ventas."
        )

    if category_field and price_field:
        create_index_safely(
            log_rows,
            product_catalog,
            [(category_field, ASCENDING), (price_field, ASCENDING)],
            "idx_catalog_category_price",
            "compound_esr",
            "Optimizar filtro por categoría y precio."
        )

    create_index_safely(
        log_rows,
        product_catalog,
        [("seller_summary.seller_id", ASCENDING), ("name", ASCENDING)],
        "idx_catalog_seller_name",
        "compound",
        "Optimizar consulta de productos por vendedor."
    )

    existing_text_index = text_index_exists(product_catalog)

    if existing_text_index:
        log_rows.append({
            "collection": product_catalog.name,
            "index_name": existing_text_index.get("name"),
            "keys": json.dumps(dict(existing_text_index.get("key", {})), ensure_ascii=False),
            "index_type": "text_existing",
            "purpose": "Reutilizar índice de texto existente para búsqueda full-text.",
            "status": "REUSED",
            "error": None,
            "created_at": datetime.now(timezone.utc).isoformat()
        })
        print(f"REUSED - {product_catalog.name}.{existing_text_index.get('name')}")
    else:
        create_index_safely(
            log_rows,
            product_catalog,
            [("name", TEXT), ("search_keywords", TEXT)],
            "idx_catalog_text_search",
            "text",
            "Optimizar búsqueda textual en catálogo."
        )

    if category_field:
        existing_category_index = category_index_exists(product_catalog, category_field)

        if existing_category_index:
            log_rows.append({
                "collection": product_catalog.name,
                "index_name": existing_category_index.get("name"),
                "keys": json.dumps(dict(existing_category_index.get("key", {})), ensure_ascii=False),
                "index_type": "category_existing",
                "purpose": "Reutilizar índice existente para análisis por categoría.",
                "status": "REUSED",
                "error": None,
                "created_at": datetime.now(timezone.utc).isoformat()
            })
            print(f"REUSED - {product_catalog.name}.{existing_category_index.get('name')}")
        else:
            create_index_safely(
                log_rows,
                product_catalog,
                [(category_field, ASCENDING)],
                "idx_catalog_category",
                "single_field",
                "Optimizar análisis por categoría."
            )

    if review_date_field:
        create_index_safely(
            log_rows,
            product_reviews,
            [("product_id", ASCENDING), (review_date_field, DESCENDING)],
            "idx_reviews_product_date",
            "compound",
            "Optimizar consulta de reseñas por producto y fecha."
        )
    else:
        create_index_safely(
            log_rows,
            product_reviews,
            [("product_id", ASCENDING)],
            "idx_reviews_product",
            "single_field",
            "Optimizar consulta de reseñas por producto."
        )

    if review_score_field:
        create_index_safely(
            log_rows,
            product_reviews,
            [(review_score_field, ASCENDING), ("product_id", ASCENDING)],
            "idx_reviews_low_score_partial",
            "partial",
            "Optimizar análisis de reseñas con baja calificación.",
            partialFilterExpression={review_score_field: {"$lte": 2}}
        )

    create_index_safely(
        log_rows,
        product_review_buckets,
        [("product_id", ASCENDING), ("bucket_period", DESCENDING), ("bucket_sequence", ASCENDING)],
        "idx_review_buckets_product_period_sequence",
        "compound_unique",
        "Optimizar consulta de buckets por producto y periodo.",
        unique=True
    )

    create_index_safely(
        log_rows,
        product_review_buckets,
        [("bucket_period", DESCENDING), ("avg_review_score", ASCENDING)],
        "idx_review_buckets_period_score",
        "compound",
        "Optimizar análisis de buckets por periodo y calificación."
    )

    write_csv(INDEX_LOG_FILE, log_rows)

    print("Archivo de evidencia generado:")
    print(INDEX_LOG_FILE)


if __name__ == "__main__":
    main()
