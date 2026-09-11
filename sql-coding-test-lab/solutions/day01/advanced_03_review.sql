-- [채점] 정답
-- 전체 상품 가격 내림차순, 동률은 product_id ASC, LIMIT 15가 문제와 일치한다.

SELECT
    product_id,
    product_name,
    price,
    status,
    created_at
FROM products
ORDER BY
    price DESC,
    product_id ASC
LIMIT 15;
