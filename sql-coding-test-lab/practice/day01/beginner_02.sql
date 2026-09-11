select
	product_id
  , product_name
  , price
  , status
	from products
	where status = 'ACTIVE'
	order by
		product_id asc;