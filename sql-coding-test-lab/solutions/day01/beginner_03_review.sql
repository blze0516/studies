-- [채점] 정답
-- PAID/SHIPPED를 IN으로 묶고 order_id ASC가 문제와 일치한다.

SELECT
    order_id,
    user_id,
    order_date,
    status
FROM orders
WHERE status IN ('PAID', 'SHIPPED')
ORDER BY order_id ASC;
