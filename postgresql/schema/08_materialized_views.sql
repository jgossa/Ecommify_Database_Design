-- ============================================================
-- Script: 08_materialized_views.sql
-- Purpose: Create analytical materialized views
-- ============================================================

CREATE MATERIALIZED VIEW IF NOT EXISTS analytics.mv_sales_by_category_monthly AS
SELECT
    date_trunc('month', o.purchase_date) AS year_month,
    pc.category_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(oi.order_item_id) AS total_items,
    SUM(oi.price) AS gross_sales,
    SUM(oi.freight_value) AS total_freight
FROM core.orders o
JOIN core.order_items oi
    ON oi.order_id = o.order_id
   AND oi.purchase_date = o.purchase_date
JOIN core.products p
    ON p.product_id = oi.product_id
JOIN core.product_categories pc
    ON pc.category_id = p.category_id
GROUP BY 1, 2;

CREATE UNIQUE INDEX IF NOT EXISTS ux_mv_sales_by_category_monthly
ON analytics.mv_sales_by_category_monthly (year_month, category_name);

CREATE MATERIALIZED VIEW IF NOT EXISTS analytics.mv_customer_segments AS
SELECT
    c.customer_id,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COALESCE(SUM(pay.payment_value), 0) AS total_spent,
    MAX(o.purchase_date) AS last_purchase_date,
    CASE
        WHEN COUNT(DISTINCT o.order_id) = 1 THEN 'new'
        WHEN COALESCE(SUM(pay.payment_value), 0) >= 1000 THEN 'high_value'
        WHEN MAX(o.purchase_date) < now() - INTERVAL '180 days' THEN 'inactive'
        ELSE 'recurrent'
    END AS customer_segment
FROM core.customers c
LEFT JOIN core.orders o
    ON o.customer_id = c.customer_id
LEFT JOIN core.payments pay
    ON pay.order_id = o.order_id
   AND pay.purchase_date = o.purchase_date
GROUP BY c.customer_id;

CREATE UNIQUE INDEX IF NOT EXISTS ux_mv_customer_segments
ON analytics.mv_customer_segments (customer_id);