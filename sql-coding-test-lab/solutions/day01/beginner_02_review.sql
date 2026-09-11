-- [채점] 정답
-- ACTIVE 필터, 출력 컬럼, product_id ASC가 문제와 일치한다.

SELECT
    product_id,
    product_name,
    price,
    status
FROM products
WHERE status = 'ACTIVE'
ORDER BY product_id ASC;
