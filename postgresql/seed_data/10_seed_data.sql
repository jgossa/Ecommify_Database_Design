-- ============================================================
-- Script: 10_seed_data.sql
-- Purpose: Insert minimal sample data
-- ============================================================

INSERT INTO core.geolocation (
    zip_code_prefix, latitude, longitude, city, state, location
)
VALUES (
    '01001',
    -23.550520,
    -46.633308,
    'Sao Paulo',
    'SP',
    ST_SetSRID(ST_MakePoint(-46.633308, -23.550520), 4326)::geography
)
ON CONFLICT (zip_code_prefix) DO NOTHING;

INSERT INTO core.product_categories (category_name, category_name_en)
VALUES ('informatica_acessorios', 'computers_accessories')
ON CONFLICT (category_name) DO NOTHING;