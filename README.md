# Ecommify Database Design

Repositorio académico del proyecto Ecommify, una plataforma e-commerce multivendedor orientada a productos tecnológicos.

Este repositorio consolida el diseño e implementación técnica de una arquitectura híbrida con PostgreSQL/Supabase y MongoDB Atlas, incluyendo modelo relacional, modelo documental, optimización de consultas, evidencias de rendimiento y documentación técnica.

## Integrantes

- Nestor Alejandro Rodriguez Benavides - nestorrobe@unisabana.edu.co
- Carlos Daniel Sandoval - carlossandpar@unisabana.edu.co
- Peter Alexander Palacios Garnica - peterpaga@unisabana.edu.co
- Juan Guillermo Ossa Sánchez - juanossa@unisabana.edu.co

## Enfoque arquitectónico

El proyecto utiliza la Opción 1: Arquitectura Transaccional-Analítica.

- PostgreSQL / Supabase se usa como núcleo transaccional para pedidos, pagos, inventario, clientes, vendedores y productos maestros.
- MongoDB Atlas se usa como módulo documental y analítico para catálogo enriquecido, reseñas, búsqueda textual, patrones documentales y consultas flexibles.

MongoDB no reemplaza PostgreSQL; lo complementa para escenarios donde el modelo documental ofrece mayor flexibilidad.

## Objetivo del repositorio

Centralizar los artefactos técnicos del proyecto Ecommify:

- Documentación técnica de diseño e implementación.
- Scripts SQL para PostgreSQL.
- Scripts Python y JSON para MongoDB.
- Notebooks de implementación y validación.
- Evidencias de rendimiento antes/después.
- Evidencias de JSON Schema y Bucket Pattern.
- Documentación de sharding y replica sets.
- Material de soporte para video de demostración.

## Estructura del repositorio

Ecommify_Database_Design/
- README.md
- docs/
  - u5_etapa2/
- postgresql/
  - README.md
  - schema/
  - seed_data/
  - queries/
  - indexes/
  - evidence/
    - validation/
    - explain_before_after/
- mongodb/
  - README.md
  - schema/
  - indexes/
  - queries/
  - sharding/
  - evidence/
    - json_schema/
    - bucket_pattern/
    - explain_before_after/
    - indexes/
- notebooks/
- evidence/
  - screenshots/
  - video/

## PostgreSQL

La carpeta postgresql/ contiene la implementación relacional y transaccional del proyecto.

Incluye:

- extensiones PostgreSQL;
- esquemas;
- tipos y dominios;
- tablas principales;
- tablas transaccionales;
- índices;
- triggers;
- particionamiento de core.orders;
- vistas materializadas;
- consultas de validación y monitoreo.

Para más detalle, revisar:

postgresql/README.md

## MongoDB

La carpeta mongodb/ contiene la implementación documental del proyecto.

Incluye:

- JSON Schema para product_catalog;
- scripts de índices MongoDB;
- construcción de product_review_buckets;
- evidencias de Bucket Pattern;
- evidencias de explain antes/después;
- documentación de sharding y replica sets.

Para más detalle, revisar:

mongodb/README.md

## Notebooks

La carpeta notebooks/ contiene notebooks de análisis, carga, validación y optimización usados durante el proyecto.

Los notebooks deben estar documentados por hitos para facilitar trazabilidad con los documentos técnicos.

## Evidencias

Las evidencias se organizan por motor.

### PostgreSQL

Ubicación:

postgresql/evidence/

Incluye validaciones del esquema core, tablas, índices, constraints, particionamiento y ejecución de consultas con EXPLAIN ANALYZE.

### MongoDB

Ubicación:

mongodb/evidence/

Incluye evidencias de:

- JSON Schema;
- Bucket Pattern;
- índices;
- explain antes/después;
- pipeline de agregación.

## Ejecución general

### PostgreSQL

Los scripts SQL se encuentran en:

postgresql/schema/

Deben ejecutarse en orden numérico cuando se reconstruya el entorno.

### MongoDB

Los scripts principales se ejecutan usando la variable de entorno MONGODB_URI.

Ejemplo:

export MONGODB_URI="mongodb+srv://usuario:password@cluster.mongodb.net/?retryWrites=true&w=majority"
python mongodb/indexes/mongodb_indexes.py

Por seguridad, las credenciales no deben guardarse en el repositorio.

## Entregables Unidad 5 - Etapa 2

La Etapa 2 corresponde a la implementación técnica completa en PostgreSQL y MongoDB.

Los entregables asociados son:

1. Documento técnico de implementación.
2. Repositorio GitHub actualizado.
3. Video de demostración.

Observación
- [Documento técnico U5 Etapa 2 - Implementación técnica completa en PostgreSQL y MongoDB](docs/u5_etapa2/Ecommify_U5_Etapa2_Imp_Completa_PostgreSQL_MongoDB.pdf)

## Alcance y limitaciones

- El repositorio mantiene continuidad con entregas anteriores del proyecto.
- PostgreSQL conserva el rol de fuente transaccional principal.
- MongoDB se usa como complemento documental y analítico.
- El sharding se documenta de forma teórica/simulada, sin modificar el clúster Atlas real.
- Las evidencias corresponden al entorno académico usado durante la implementación.
