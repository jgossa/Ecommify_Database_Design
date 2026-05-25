-- ============================================================
-- Script: 03_tables_core.sql
-- Purpose: Create master/core business tables
-- ============================================================

CREATE TABLE IF NOT EXISTS core.geolocation (
    zip_code_prefix TEXT PRIMARY KEY,
    latitude NUMERIC(10,7) NOT NULL,
    longitude NUMERIC(10,7) NOT NULL,
    city TEXT NOT NULL,
    state CHAR(2) NOT NULL,
    location GEOGRAPHY(Point, 4326)
);

CREATE TABLE IF NOT EXISTS core.customers (
    customer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_unique_id TEXT NOT NULL,
    zip_code_prefix TEXT REFERENCES core.geolocation(zip_code_prefix),
    city TEXT NOT NULL,
    state CHAR(2) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS core.sellers (
    seller_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    zip_code_prefix TEXT REFERENCES core.geolocation(zip_code_prefix),
    city TEXT NOT NULL,
    state CHAR(2) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS core.product_categories (
    category_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category_name TEXT UNIQUE NOT NULL,
    category_name_en TEXT
);

CREATE TABLE IF NOT EXISTS core.products (
    product_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category_id UUID REFERENCES core.product_categories(category_id),
    product_name TEXT,
    specifications JSONB,
    photos TEXT[],
    promotion_period TSTZRANGE,
    weight_g NUMERIC(10,2) CHECK (weight_g >= 0),
    length_cm NUMERIC(10,2) CHECK (length_cm >= 0),
    height_cm NUMERIC(10,2) CHECK (height_cm >= 0),
    width_cm NUMERIC(10,2) CHECK (width_cm >= 0),
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);