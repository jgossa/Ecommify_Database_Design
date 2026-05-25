-- ============================================================
-- Script: 06_triggers_updated_at.sql
-- Purpose: Maintain updated_at fields automatically
-- ============================================================

CREATE OR REPLACE FUNCTION core.set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_customers_updated_at
BEFORE UPDATE ON core.customers
FOR EACH ROW EXECUTE FUNCTION core.set_updated_at();

CREATE TRIGGER trg_sellers_updated_at
BEFORE UPDATE ON core.sellers
FOR EACH ROW EXECUTE FUNCTION core.set_updated_at();

CREATE TRIGGER trg_products_updated_at
BEFORE UPDATE ON core.products
FOR EACH ROW EXECUTE FUNCTION core.set_updated_at();

CREATE TRIGGER trg_orders_updated_at
BEFORE UPDATE ON core.orders
FOR EACH ROW EXECUTE FUNCTION core.set_updated_at();

CREATE TRIGGER trg_inventory_updated_at
BEFORE UPDATE ON core.inventory
FOR EACH ROW EXECUTE FUNCTION core.set_updated_at();