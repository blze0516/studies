select
	user_id
  , user_name
  , acquisition_channel
  , is_premium 
	from
		users
	where 
		acquisition_channel in ('organic', 'social', 'email')
	  and
	  	is_premium = true
	order by
		acquisition_channel asc
	  , user_id asc;