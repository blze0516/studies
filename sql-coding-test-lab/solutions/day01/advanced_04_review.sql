-- [채점] 정답
-- premium만 남기고 가입일 최신순, 동률은 user_id DESC, LIMIT 25가 문제와 일치한다.

SELECT
    user_id,
    user_name,
    signup_date,
    region,
    acquisition_channel,
    is_premium
FROM users
WHERE is_premium = TRUE
ORDER BY
    signup_date DESC,
    user_id DESC
LIMIT 25;
