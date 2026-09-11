-- [채점] 정답
-- SEOUL/BUSAN, CANCELLED 제외, 금액 구간, 금액·order_id 내림차순, LIMIT 50이 문제와 일치한다.

SELECT
    order_id,
    user_id,
    status,
    shipping_region,
    total_amount,
    order_date
FROM orders
WHERE shipping_region IN ('SEOUL', 'BUSAN')
  AND status <> 'CANCELLED'
  AND total_amount BETWEEN 100000 AND 500000
ORDER BY
    total_amount DESC,
    order_id DESC
LIMIT 50;
