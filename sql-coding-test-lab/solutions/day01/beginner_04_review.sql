-- [채점] 정답
-- BETWEEN 50000~100000은 양 끝 포함. price, product_id 오름차순이 문제와 일치한다.

SELECT
    product_id,
    product_name,
    price
FROM products
WHERE price BETWEEN 50000 AND 100000
ORDER BY
    price ASC,
    product_id ASC;
