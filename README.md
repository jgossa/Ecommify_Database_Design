# Ecommify Database Design

Repositorio académico para el diseño conceptual y lógico de la base de datos del proyecto **Ecommify**, una plataforma e-commerce multivendedor orientada a productos tecnológicos.

# Integrantes

Nestor Alejandro Rodriguez Benavides - nestorrobe@unisabana.edu.co

Carlos Daniel Sandoval - carlossandpar@unisabana.edu.co

Peter Alexander Palacios Garnica - peterpaga@unisabana.edu.co

Juan Guillermo Ossa Sánchez - juanossa@unisabana.edu.co

## Enfoque arquitectónico

El proyecto utiliza la **Opción 1: Arquitectura Transaccional-Analítica**:

- **PostgreSQL / Supabase** para el módulo transaccional: pedidos, pagos, inventario, clientes, vendedores y productos maestros.
- **MongoDB Atlas** para el módulo documental/analítico: catálogo enriquecido, reseñas, comportamiento de usuarios y snapshots analíticos.

## Objetivo del repositorio

Centralizar los artefactos técnicos del entregable:

- Documento técnico de diseño.
- Presentación ejecutiva.
- Scripts SQL preliminares para PostgreSQL.
- Esquemas preliminares para MongoDB.
- Consultas de validación y monitoreo.
- Notebook de análisis exploratorio del dataset Brazilian E-Commerce / Olist.

## Estructura del repositorio

```text
Ecommify_Database_Design/
├── README.md
├── docs/
│   ├── Documento_Tecnico_Diseno.pdf
│   └── Presentacion_Ejecutiva.pdf
├── postgresql/
│   ├── schema/
│   │   ├── 00_extensions.sql
│   │   ├── 01_schemas.sql
│   │   ├── 02_types_domains.sql
│   │   ├── 03_tables_core.sql
│   │   ├── 04_tables_transactions.sql
│   │   ├── 05_indexes.sql
│   │   ├── 06_triggers_updated_at.sql
│   │   ├── 07_partitioning_orders.sql
│   │   └── 08_materialized_views.sql
│   ├── seed_data/
│   │   └── 10_seed_data.sql
│   └── queries/
│       ├── 11_validation_queries.sql
│       └── 12_monitoring_queries.sql
├── mongodb/
│   └── schema/
│       ├── product_catalog_schema.json
│       ├── product_reviews_schema.json
│       └── customer_events_schema.json
└── notebooks/
    └── Data_Exploration_Analysis.ipynb