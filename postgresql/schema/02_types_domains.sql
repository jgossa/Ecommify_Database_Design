-- ============================================================
-- Script: 02_types_domains.sql
-- Purpose: Define controlled types and reusable domains
-- ============================================================

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'order_status_type') THEN
        CREATE TYPE core.order_status_type AS ENUM (
            'created',
            'approved',
            'invoiced',
            'shipped',
            'delivered',
            'canceled',
            'unavailable'
        );
    END IF;
END$$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'payment_type_enum') THEN
        CREATE TYPE core.payment_type_enum AS ENUM (
            'credit_card',
            'boleto',
            'voucher',
            'debit_card',
            'not_defined'
        );
    END IF;
END$$;

CREATE DOMAIN core.positive_money AS NUMERIC(12,2)
CHECK (VALUE >= 0);

CREATE DOMAIN core.positive_quantity AS INTEGER
CHECK (VALUE >= 0);