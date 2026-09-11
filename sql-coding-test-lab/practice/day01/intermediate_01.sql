select
	product_id
  , product_name
  , price
  , status
	from products
	where status = 'ACTIVE'
	order by
		price desc, product_id  asc
	limit 10;