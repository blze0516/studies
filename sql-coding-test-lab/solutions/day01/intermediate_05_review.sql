-- [채점] 정정
-- 판매 가능 상태 ACTIVE/SOLD_OUT과 가격 150000~300000, 정렬 status/price/product_id.

SELECT
    product_id,
    product_name,
    price,
    status
FROM products
WHERE status IN ('ACTIVE', 'SOLD_OUT')
  AND price BETWEEN 150000 AND 300000
ORDER BY
    status ASC,
    price DESC,
    product_id ASC;
