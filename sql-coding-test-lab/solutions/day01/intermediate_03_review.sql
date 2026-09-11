-- [채점] 정답
-- 가입일 2026-01-01~2026-03-31 BETWEEN과 signup_date, user_id 오름차순이 문제와 일치한다.

SELECT
    user_id,
    user_name,
    signup_date,
    region,
    acquisition_channel
FROM users
WHERE signup_date BETWEEN DATE '2026-01-01' AND DATE '2026-03-31'
ORDER BY
    signup_date ASC,
    user_id ASC;
