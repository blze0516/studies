-- Master Dataset for sql-coding-test-lab
-- Target: PostgreSQL 18.6 / schema interview_lab
-- Re-running this script DROPS and recreates interview_lab.

BEGIN;

DROP SCHEMA IF EXISTS interview_lab CASCADE;
CREATE SCHEMA interview_lab;
SET search_path TO interview_lab;

CREATE TABLE categories (
    category_id     BIGINT PRIMARY KEY,
    category_name   TEXT NOT NULL
);

CREATE TABLE users (
    user_id              BIGINT PRIMARY KEY,
    user_name            TEXT NOT NULL,
    email                TEXT NOT NULL,
    signup_date          DATE NOT NULL,
    region               TEXT NOT NULL,
    acquisition_channel  TEXT NOT NULL,
    birth_year           INT NOT NULL,
    is_premium           BOOLEAN NOT NULL
);

CREATE TABLE products (
    product_id    BIGINT PRIMARY KEY,
    category_id   BIGINT NOT NULL REFERENCES categories (category_id),
    product_name  TEXT NOT NULL,
    price         NUMERIC(12, 2) NOT NULL,
    status        TEXT NOT NULL CHECK (status IN ('ACTIVE', 'SOLD_OUT', 'DISCONTINUED')),
    created_at    TIMESTAMP NOT NULL,
    attributes    JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE orders (
    order_id         BIGINT PRIMARY KEY,
    user_id          BIGINT NOT NULL REFERENCES users (user_id),
    order_date       TIMESTAMP NOT NULL,
    status           TEXT NOT NULL,
    shipping_region  TEXT NOT NULL,
    coupon_code      TEXT,
    total_amount     NUMERIC(12, 2) NOT NULL
);

CREATE TABLE order_items (
    order_item_id  BIGINT PRIMARY KEY,
    order_id       BIGINT NOT NULL REFERENCES orders (order_id),
    product_id     BIGINT NOT NULL REFERENCES products (product_id),
    quantity       INT NOT NULL,
    unit_price     NUMERIC(12, 2) NOT NULL
);

INSERT INTO categories (category_id, category_name)
VALUES
    (1, 'Electronics'),
    (2, 'Books'),
    (3, 'Fashion'),
    (4, 'Home'),
    (5, 'Food'),
    (6, 'Sports'),
    (7, 'Beauty'),
    (8, 'Kids');

INSERT INTO users (
    user_id,
    user_name,
    email,
    signup_date,
    region,
    acquisition_channel,
    birth_year,
    is_premium
)
SELECT
    i,
    format('User %s', lpad(i::text, 3, '0')),
    format('user%s@example.com', lpad(i::text, 3, '0')),
    DATE '2024-01-01' + ((i % 600) * INTERVAL '1 day'),
    (ARRAY['SEOUL', 'BUSAN', 'INCHEON', 'DAEGU', 'GWANGJU'])[1 + (i % 5)],
    (ARRAY['ORGANIC', 'PAID_SEARCH', 'SOCIAL', 'REFERRAL', 'EMAIL'])[1 + (i % 5)],
    1980 + (i % 25),
    (i % 7 = 0)
FROM generate_series(1, 300) AS s(i);

INSERT INTO products (
    product_id,
    category_id,
    product_name,
    price,
    status,
    created_at,
    attributes
)
SELECT
    i,
    1 + (i % 8),
    format('Product %s', lpad(i::text, 3, '0')),
    (5000 + (i * 2500))::numeric,
    (ARRAY['ACTIVE', 'ACTIVE', 'ACTIVE', 'SOLD_OUT', 'DISCONTINUED'])[1 + (i % 5)],
    TIMESTAMP '2025-01-01 09:00:00' + ((i % 400) * INTERVAL '1 day'),
    jsonb_build_object('color', (ARRAY['red', 'blue', 'black'])[1 + (i % 3)])
FROM generate_series(1, 120) AS s(i);

INSERT INTO orders (
    order_id,
    user_id,
    order_date,
    status,
    shipping_region,
    coupon_code,
    total_amount
)
SELECT
    i,
    1 + (i % 300),
    TIMESTAMP '2026-01-01 10:00:00' + ((i % 240) * INTERVAL '1 hour') + ((i % 17) * INTERVAL '1 minute'),
    (ARRAY['PAID', 'SHIPPED', 'COMPLETED', 'CANCELLED'])[1 + (i % 4)],
    (ARRAY['SEOUL', 'BUSAN', 'INCHEON', 'DAEGU', 'GWANGJU'])[1 + (i % 5)],
    CASE WHEN i % 6 = 0 THEN format('COUPON-%s', i % 20) ELSE NULL END,
    (12000 + (i % 50) * 1000)::numeric
FROM generate_series(1, 2500) AS s(i);

-- Tie-breaker rows: same order_date, different order_id
INSERT INTO orders (
    order_id,
    user_id,
    order_date,
    status,
    shipping_region,
    coupon_code,
    total_amount
)
VALUES
    (2501, 32, TIMESTAMP '2026-08-28 17:31:00', 'CANCELLED', 'SEOUL', NULL, 18000),
    (2502, 232, TIMESTAMP '2026-08-28 17:31:00', 'PAID', 'BUSAN', 'COUPON-7', 22000);

INSERT INTO order_items (
    order_item_id,
    order_id,
    product_id,
    quantity,
    unit_price
)
SELECT
    row_number() OVER (ORDER BY o.order_id, g.n),
    o.order_id,
    1 + ((o.order_id + g.n) % 120),
    1 + ((o.order_id + g.n) % 3),
    p.price
FROM orders AS o
CROSS JOIN generate_series(1, 2) AS g(n)
JOIN products AS p
    ON p.product_id = 1 + ((o.order_id + g.n) % 120);

ANALYZE;

SELECT 'users' AS table_name, COUNT(*) AS row_count FROM users
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'orders', COUNT(*) FROM orders
UNION ALL
SELECT 'categories', COUNT(*) FROM categories
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items
ORDER BY table_name;

COMMIT;
