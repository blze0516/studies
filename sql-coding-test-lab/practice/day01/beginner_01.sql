select
	user_id
  , user_name
  , email
  , region
	FROM users
	WHERE 	
		region = 'BUSAN'
	ORDER BY 
		user_id ASC;