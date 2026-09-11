select
	order_id
  , user_id
  , order_date
  , status
	from orders
	where status in ('PAID', 'SHIPPED')
	order by 
		order_id asc;