-- ============================================================
-- Script: 07_partitioning_orders.sql
-- Purpose: Create initial monthly partitions for orders
-- ============================================================

CREATE TABLE IF NOT EXISTS core.orders_2024_01
PARTITION OF core.orders
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE IF NOT EXISTS core.orders_2024_02
PARTITION OF core.orders
FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

CREATE TABLE IF NOT EXISTS core.orders_2024_03
PARTITION OF core.orders
FOR VALUES FROM ('2024-03-01') TO ('2024-04-01');

CREATE TABLE IF NOT EXISTS core.orders_default
PARTITION OF core.orders
DEFAULT;