select
	user_id
  , user_name
  , signup_date
  , region
  , acquisition_channel
	from
		users
	where 
		signup_date between '2026-01-01' and '2026-03-31'
	order by
		signup_date asc
	  , user_id asc;