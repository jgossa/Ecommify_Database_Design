-- ============================================================
-- Ecommify Database Design
-- Script: 00_extensions.sql
-- Purpose: Enable PostgreSQL extensions required by the project
-- ============================================================

CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS postgis;