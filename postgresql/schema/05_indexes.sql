-- ============================================================
-- Script: 05_indexes.sql
-- Purpose: Create indexes for OLTP and analytical queries
-- ============================================================

CREATE INDEX IF NOT EXISTS idx_customers_unique_id
ON core.customers (customer_unique_id);

CREATE INDEX IF NOT EXISTS idx_customers_location
ON core.customers (zip_code_prefix);

CREATE INDEX IF NOT EXISTS idx_sellers_location
ON core.sellers (zip_code_prefix);

CREATE INDEX IF NOT EXISTS idx_products_category
ON core.products (category_id);

CREATE INDEX IF NOT EXISTS idx_products_specifications_gin
ON core.products USING GIN (specifications);

CREATE INDEX IF NOT EXISTS idx_products_name_trgm
ON core.products USING GIN (product_name gin_trgm_ops);

CREATE INDEX IF NOT EXISTS idx_orders_customer_purchase
ON core.orders (customer_id, purchase_date DESC);

CREATE INDEX IF NOT EXISTS idx_order_items_product
ON core.order_items (product_id);

CREATE INDEX IF NOT EXISTS idx_order_items_seller
ON core.order_items (seller_id);

CREATE INDEX IF NOT EXISTS idx_payments_order
ON core.payments (order_id, purchase_date);

CREATE INDEX IF NOT EXISTS idx_geolocation_location
ON core.geolocation USING GIST (location);