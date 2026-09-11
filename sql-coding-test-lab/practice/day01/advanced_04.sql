select
	user_id
  , user_name
  , signup_date
  , region
  , acquisition_channel
  , is_premium
	from users
	where 
		is_premium = true
	order by 
		signup_date desc
	  , user_id desc
	limit 25;