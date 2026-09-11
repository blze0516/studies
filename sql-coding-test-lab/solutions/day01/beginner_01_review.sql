-- [채점] 정답
-- 지역 BUSAN 필터, 출력 컬럼, user_id ASC가 문제와 일치한다.

SELECT
    user_id,
    user_name,
    email,
    region
FROM users
WHERE region = 'BUSAN'
ORDER BY user_id ASC;
