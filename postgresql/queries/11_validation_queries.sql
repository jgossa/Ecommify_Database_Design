-- ============================================================
-- Script: 11_validation_queries.sql
-- Purpose: Validate schema integrity and basic relationships
-- ============================================================

SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema IN ('core', 'analytics')
ORDER BY table_schema, table_name;

SELECT COUNT(*) AS total_customers
FROM core.customers;

SELECT COUNT(*) AS total_orders
FROM core.orders;

SELECT
    o.order_id,
    c.customer_unique_id,
    o.order_status,
    o.purchase_date
FROM core.orders o
JOIN core.customers c
    ON c.customer_id = o.customer_id
LIMIT 10;

SELECT *
FROM analytics.mv_sales_by_category_monthly
LIMIT 10;