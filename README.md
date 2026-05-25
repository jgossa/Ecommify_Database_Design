# Ecommify Database Design

Repositorio académico para el diseño conceptual y lógico de la base de datos del proyecto **Ecommify**, una plataforma e-commerce multivendedor orientada a productos tecnológicos.

## Enfoque arquitectónico

El proyecto utiliza la **Opción 1: Arquitectura Transaccional-Analítica**:

- **PostgreSQL** para el módulo transaccional: pedidos, pagos, inventario, clientes, vendedores y productos maestros.
- **MongoDB** para el módulo documental/analítico: catálogo enriquecido, reseñas, comportamiento de usuarios y snapshots analíticos.

## Estructura del repositorio

```text
Ecommify_Database_Design/
├── README.md
├── docs/
│   ├── Documento_Tecnico_Diseno.pdf
│   └── Presentacion_Ejecutiva.pdf
├── postgresql/
│   ├── schema/
│   ├── seed_data/
│   └── queries/
├── mongodb/
│   └── schema/
└── notebooks/
    └── Data_Exploration_Analysis.ipynb
