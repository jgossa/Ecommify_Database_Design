-- ============================================================
-- Script: 12_monitoring_queries.sql
-- Purpose: Preliminary monitoring queries for OLTP/OLAP
-- ============================================================

EXPLAIN ANALYZE
SELECT *
FROM core.orders
WHERE order_id = '00000000-0000-0000-0000-000000000000';

EXPLAIN ANALYZE
SELECT *
FROM core.orders
WHERE customer_id = '00000000-0000-0000-0000-000000000000'
ORDER BY purchase_date DESC;

SELECT
    schemaname,
    relname,
    indexrelname,
    idx_scan
FROM pg_stat_user_indexes
WHERE schemaname IN ('core', 'analytics')
ORDER BY idx_scan DESC;

SELECT
    schemaname,
    relname,
    n_live_tup,
    n_dead_tup
FROM pg_stat_user_tables
WHERE schemaname IN ('core', 'analytics')
ORDER BY n_live_tup DESC;