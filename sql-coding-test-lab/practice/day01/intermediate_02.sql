select
	order_id
  , user_id
  , order_date
  , status
  , shipping_region
  , total_amount
	from orders
	where
		shipping_region = 'SEOUL'
	order by
		order_date desc, order_id asc
	limit 20;