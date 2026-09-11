-- [채점] 정답
-- ACTIVE 고가와 SOLD_OUT 중가를 괄호로 나눠 OR 했고, 정렬이 문제와 일치한다.

SELECT
    product_id,
    product_name,
    price,
    status
FROM products
WHERE (status = 'ACTIVE' AND price >= 300000)
   OR (status = 'SOLD_OUT' AND price BETWEEN 100000 AND 200000)
ORDER BY
    status ASC,
    price DESC,
    product_id ASC;
