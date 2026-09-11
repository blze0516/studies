-- [채점] 정답
-- COMPLETED/SHIPPED, 최신순, 동률은 order_id DESC, LIMIT 30이 문제와 일치한다.

SELECT
    order_id,
    user_id,
    order_date,
    status,
    shipping_region,
    total_amount
FROM orders
WHERE status IN ('COMPLETED', 'SHIPPED')
ORDER BY
    order_date DESC,
    order_id DESC
LIMIT 30;
