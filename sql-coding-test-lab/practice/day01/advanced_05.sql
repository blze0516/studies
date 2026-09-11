select
	order_id
  , user_id
  , status
  , shipping_region
  , total_amount
  , order_date
	from orders
	where 
		shipping_region in ('SEOUL', 'BUSAN')
	  and 
	  	status != 'CANCELLED'
	  and
	  	total_amount between 100000 and 500000
	order by
		total_amount desc
	  , order_id desc
	limit 50;