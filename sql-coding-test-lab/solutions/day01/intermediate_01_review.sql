-- [채점] 정답
-- ACTIVE 상품을 가격 내림차순, 동률은 product_id ASC, LIMIT 10이 문제와 일치한다.

SELECT
    product_id,
    product_name,
    price,
    status
FROM products
WHERE status = 'ACTIVE'
ORDER BY
    price DESC,
    product_id ASC
LIMIT 10;
