-- [채점] 정정
-- DISTINCT만으로는 순서가 정해지지 않으므로 ORDER BY region ASC를 넣는다.

SELECT DISTINCT
    region
FROM users
ORDER BY region ASC;
