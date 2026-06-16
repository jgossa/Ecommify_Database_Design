"""
Construye la colección product_review_buckets aplicando Bucket Pattern.

Uso:
  export MONGODB_URI="mongodb+srv://usuario:password@cluster.mongodb.net/?retryWrites=true&w=majority"
  python mongodb/queries/build_product_review_buckets.py

Notas:
- No modifica product_reviews.
- Reconstruye únicamente la colección derivada product_review_buckets.
- Agrupa reseñas por product_id + bucket_period + bucket_sequence.
- Genera evidencias CSV/JSON en mongodb/evidence/bucket_pattern/.
"""

import csv
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path

import certifi
from pymongo import ASCENDING, DESCENDING, MongoClient
from pymongo.server_api import ServerApi


DATABASE_NAME = os.getenv("MONGODB_DATABASE", "ecommify_mongodb")
SOURCE_COLLECTION = "product_reviews"
TARGET_COLLECTION = "product_review_buckets"
BUCKET_SIZE = int(os.getenv("BUCKET_SIZE", "50"))

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
EVIDENCE_DIR = REPO_ROOT / "mongodb" / "evidence" / "bucket_pattern"
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)


def pick_existing_field(document, candidates):
    """Retorna el primer campo candidato que exista en el documento."""
    for field in candidates:
        if field in document:
            return field
    return None


def safe_float(value):
    """Convierte un valor a float cuando sea posible."""
    if value is None:
        return None

    try:
        return float(value)
    except Exception:
        return None


def get_bucket_period(value):
    """Obtiene periodo YYYY-MM desde una fecha."""
    if isinstance(value, datetime):
        return value.strftime("%Y-%m")

    return "unknown"


def write_csv(path, rows, fieldnames):
    """Escribe un archivo CSV simple."""
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main():
    mongodb_uri = os.getenv("MONGODB_URI")

    if not mongodb_uri:
        raise RuntimeError(
            "Falta la variable de entorno MONGODB_URI. "
            "Ejemplo: export MONGODB_URI='mongodb+srv://usuario:password@cluster.mongodb.net/?retryWrites=true&w=majority'"
        )

    client = MongoClient(
        mongodb_uri,
        tls=True,
        tlsCAFile=certifi.where(),
        server_api=ServerApi("1"),
        serverSelectionTimeoutMS=30000
    )

    db = client[DATABASE_NAME]
    source = db[SOURCE_COLLECTION]
    target = db[TARGET_COLLECTION]

    client.admin.command("ping")
    print("Conexión exitosa a MongoDB Atlas.")

    sample_review = source.find_one()

    if not sample_review:
        raise RuntimeError("La colección product_reviews no tiene documentos.")

    review_id_field = pick_existing_field(sample_review, ["review_id", "id"])
    order_id_field = pick_existing_field(sample_review, ["order_id"])
    product_id_field = pick_existing_field(sample_review, ["product_id"])
    review_score_field = pick_existing_field(sample_review, ["review_score", "score", "rating"])
    review_date_field = pick_existing_field(sample_review, ["review_creation_date", "review_created_at", "created_at"])
    review_comment_field = pick_existing_field(sample_review, ["review_comment_message", "comment", "message"])

    if not product_id_field:
        raise RuntimeError("No se encontró product_id en product_reviews.")

    projection = {
        "_id": 1,
        product_id_field: 1
    }

    for field in [
        review_id_field,
        order_id_field,
        review_score_field,
        review_date_field,
        review_comment_field
    ]:
        if field:
            projection[field] = 1

    reviews = []

    for doc in source.find({}, projection):
        product_id = doc.get(product_id_field)

        if not product_id:
            continue

        review_date = doc.get(review_date_field) if review_date_field else None
        review_score = safe_float(doc.get(review_score_field)) if review_score_field else None
        comment_value = doc.get(review_comment_field) if review_comment_field else None

        reviews.append({
            "mongo_id": str(doc.get("_id")),
            "review_id": doc.get(review_id_field) if review_id_field else str(doc.get("_id")),
            "order_id": doc.get(order_id_field) if order_id_field else None,
            "product_id": product_id,
            "review_score": review_score,
            "review_date": review_date,
            "bucket_period": get_bucket_period(review_date),
            "comment_excerpt": comment_value[:150] if isinstance(comment_value, str) else None
        })

    reviews.sort(
        key=lambda item: (
            str(item["product_id"]),
            str(item["bucket_period"]),
            str(item["review_date"])
        )
    )

    grouped = {}

    for review in reviews:
        key = (review["product_id"], review["bucket_period"])
        grouped.setdefault(key, []).append(review)

    now_utc = datetime.now(timezone.utc)
    bucket_documents = []

    for (product_id, bucket_period), group_reviews in grouped.items():
        total_chunks = math.ceil(len(group_reviews) / BUCKET_SIZE)

        for bucket_sequence in range(total_chunks):
            start = bucket_sequence * BUCKET_SIZE
            end = start + BUCKET_SIZE
            chunk = group_reviews[start:end]

            review_scores = [
                item["review_score"]
                for item in chunk
                if item.get("review_score") is not None
            ]

            embedded_reviews = []

            for item in chunk:
                embedded_reviews.append({
                    "review_id": item.get("review_id"),
                    "order_id": item.get("order_id"),
                    "review_score": item.get("review_score"),
                    "review_date": item.get("review_date"),
                    "comment_excerpt": item.get("comment_excerpt")
                })

            bucket_documents.append({
                "bucket_id": f"{product_id}_{bucket_period}_{bucket_sequence}",
                "product_id": product_id,
                "bucket_period": bucket_period,
                "bucket_sequence": bucket_sequence,
                "bucket_size_limit": BUCKET_SIZE,
                "review_count": len(embedded_reviews),
                "avg_review_score": round(sum(review_scores) / len(review_scores), 2) if review_scores else None,
                "min_review_score": min(review_scores) if review_scores else None,
                "max_review_score": max(review_scores) if review_scores else None,
                "reviews": embedded_reviews,
                "pattern": "Bucket Pattern",
                "source_collection": SOURCE_COLLECTION,
                "schema_version": 1,
                "created_at": now_utc,
                "updated_at": now_utc
            })

    target.delete_many({})

    if bucket_documents:
        target.insert_many(bucket_documents)

    target.create_index(
        [
            ("product_id", ASCENDING),
            ("bucket_period", DESCENDING),
            ("bucket_sequence", ASCENDING)
        ],
        name="idx_review_buckets_product_period_sequence",
        unique=True
    )

    target.create_index(
        [
            ("bucket_period", DESCENDING),
            ("avg_review_score", ASCENDING)
        ],
        name="idx_review_buckets_period_score"
    )

    total_buckets = target.count_documents({})

    evidence = [{
        "pattern": "Bucket Pattern",
        "source_collection": SOURCE_COLLECTION,
        "target_collection": TARGET_COLLECTION,
        "grouping_strategy": "product_id + bucket_period + bucket_sequence",
        "bucket_size_limit": BUCKET_SIZE,
        "source_reviews": len(reviews),
        "bucket_documents": total_buckets,
        "generated_at": datetime.now(timezone.utc).isoformat()
    }]

    write_csv(
        EVIDENCE_DIR / "u5_etapa2_mongodb_bucket_pattern_evidence.csv",
        evidence,
        [
            "pattern",
            "source_collection",
            "target_collection",
            "grouping_strategy",
            "bucket_size_limit",
            "source_reviews",
            "bucket_documents",
            "generated_at"
        ]
    )

    indexes_rows = []

    for index in target.list_indexes():
        indexes_rows.append({
            "index_name": index.get("name"),
            "keys": json.dumps(dict(index.get("key", {})), ensure_ascii=False),
            "unique": index.get("unique", False)
        })

    write_csv(
        EVIDENCE_DIR / "u5_etapa2_mongodb_bucket_indexes.csv",
        indexes_rows,
        ["index_name", "keys", "unique"]
    )

    sample_bucket = target.find_one({}, {"_id": 0})

    with open(EVIDENCE_DIR / "product_review_buckets_sample.json", "w", encoding="utf-8") as file:
        json.dump(sample_bucket, file, indent=2, default=str, ensure_ascii=False)

    print("Bucket Pattern implementado correctamente.")
    print(json.dumps(evidence[0], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
