-- [채점] 정답 (문제문 기준)
-- organic/social/email + is_premium = true, 채널·user_id 오름차순이 문제와 일치한다.
-- 현재 Master Dataset의 채널값은 대문자라 실행 결과가 비어 있을 수 있다.

SELECT
    user_id,
    user_name,
    acquisition_channel,
    is_premium
FROM users
WHERE acquisition_channel IN ('organic', 'social', 'email')
  AND is_premium = TRUE
ORDER BY
    acquisition_channel ASC,
    user_id ASC;
