-- ============================================================
-- Script: 04_tables_transactions.sql
-- Purpose: Create transactional tables for Ecommify
-- ============================================================

CREATE TABLE IF NOT EXISTS core.orders (
    order_id UUID NOT NULL DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL REFERENCES core.customers(customer_id),
    order_status core.order_status_type NOT NULL DEFAULT 'created',
    purchase_date TIMESTAMPTZ NOT NULL,
    approved_at TIMESTAMPTZ,
    delivered_carrier_at TIMESTAMPTZ,
    delivered_customer_at TIMESTAMPTZ,
    estimated_delivery_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (order_id, purchase_date),
    CHECK (
        delivered_customer_at IS NULL
        OR delivered_customer_at >= purchase_date
    )
) PARTITION BY RANGE (purchase_date);

CREATE TABLE IF NOT EXISTS core.order_items (
    order_item_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID NOT NULL,
    purchase_date TIMESTAMPTZ NOT NULL,
    product_id UUID NOT NULL REFERENCES core.products(product_id),
    seller_id UUID NOT NULL REFERENCES core.sellers(seller_id),
    shipping_limit_date TIMESTAMPTZ,
    price core.positive_money NOT NULL CHECK (price > 0),
    freight_value core.positive_money NOT NULL DEFAULT 0,
    FOREIGN KEY (order_id, purchase_date)
        REFERENCES core.orders(order_id, purchase_date)
);

CREATE TABLE IF NOT EXISTS core.payments (
    payment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID NOT NULL,
    purchase_date TIMESTAMPTZ NOT NULL,
    payment_sequential INTEGER NOT NULL,
    payment_type core.payment_type_enum NOT NULL,
    payment_installments INTEGER NOT NULL CHECK (payment_installments >= 1),
    payment_value NUMERIC(12,2) NOT NULL CHECK (payment_value > 0),
    FOREIGN KEY (order_id, purchase_date)
        REFERENCES core.orders(order_id, purchase_date)
);

CREATE TABLE IF NOT EXISTS core.inventory (
    inventory_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_id UUID NOT NULL REFERENCES core.products(product_id),
    seller_id UUID NOT NULL REFERENCES core.sellers(seller_id),
    stock_quantity core.positive_quantity NOT NULL DEFAULT 0,
    reserved_quantity core.positive_quantity NOT NULL DEFAULT 0,
    updated_at TIMESTAMPTZ DEFAULT now(),
    UNIQUE (product_id, seller_id),
    CHECK (reserved_quantity <= stock_quantity)
);

CREATE TABLE IF NOT EXISTS core.reviews_ref (
    review_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID NOT NULL,
    purchase_date TIMESTAMPTZ NOT NULL,
    review_score INTEGER CHECK (review_score BETWEEN 1 AND 5),
    review_creation_date TIMESTAMPTZ,
    FOREIGN KEY (order_id, purchase_date)
        REFERENCES core.orders(order_id, purchase_date)
);