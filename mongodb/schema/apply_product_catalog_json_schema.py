"""
Aplica el validador JSON Schema sobre la colección product_catalog.

Uso:
  export MONGODB_URI="mongodb+srv://usuario:password@cluster.mongodb.net/?retryWrites=true&w=majority"
  python mongodb/schema/apply_product_catalog_json_schema.py

Notas:
- No elimina documentos.
- No recarga datos.
- Aplica collMod con validationLevel=moderate y validationAction=error.
- El archivo product_catalog_json_schema_validator.json debe existir en mongodb/schema/.
"""

import json
import os
from pathlib import Path

import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi


DATABASE_NAME = os.getenv("MONGODB_DATABASE", "ecommify_mongodb")
COLLECTION_NAME = "product_catalog"

SCRIPT_DIR = Path(__file__).resolve().parent
VALIDATOR_FILE = SCRIPT_DIR / "product_catalog_json_schema_validator.json"


def main():
    mongodb_uri = os.getenv("MONGODB_URI")

    if not mongodb_uri:
        raise RuntimeError(
            "Falta la variable de entorno MONGODB_URI. "
            "Ejemplo: export MONGODB_URI='mongodb+srv://usuario:password@cluster.mongodb.net/?retryWrites=true&w=majority'"
        )

    if not VALIDATOR_FILE.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo requerido: {VALIDATOR_FILE}"
        )

    with open(VALIDATOR_FILE, "r", encoding="utf-8") as file:
        validator = json.load(file)

    client = MongoClient(
        mongodb_uri,
        tls=True,
        tlsCAFile=certifi.where(),
        server_api=ServerApi("1"),
        serverSelectionTimeoutMS=30000
    )

    db = client[DATABASE_NAME]

    client.admin.command("ping")
    print("Conexión exitosa a MongoDB Atlas.")

    result = db.command({
        "collMod": COLLECTION_NAME,
        "validator": validator,
        "validationLevel": "moderate",
        "validationAction": "error"
    })

    print("Validador JSON Schema aplicado correctamente.")
    print(json.dumps(result, indent=2, default=str, ensure_ascii=False))

    collection_info = list(
        db.list_collections(filter={"name": COLLECTION_NAME})
    )

    options = collection_info[0].get("options", {}) if collection_info else {}

    summary = {
        "database": DATABASE_NAME,
        "collection": COLLECTION_NAME,
        "validator_exists": "validator" in options,
        "validationLevel": options.get("validationLevel"),
        "validationAction": options.get("validationAction")
    }

    print("Resumen de validación:")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
