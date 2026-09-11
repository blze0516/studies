select 
	order_id
  , user_id
  , order_date
  , status
  , shipping_region
  , total_amount
	from orders
	where 
		status in ('COMPLETED', 'SHIPPED')
	order by
		order_date desc
	  , order_id desc
	limit 30;