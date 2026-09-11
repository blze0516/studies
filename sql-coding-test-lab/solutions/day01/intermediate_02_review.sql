-- [채점] 정정
-- 같은 주문시각이면 order_id DESC로 맞춘다.

SELECT
    order_id,
    user_id,
    order_date,
    status,
    shipping_region,
    total_amount
FROM orders
WHERE shipping_region = 'SEOUL'
ORDER BY
    order_date DESC,
    order_id DESC
LIMIT 20;
