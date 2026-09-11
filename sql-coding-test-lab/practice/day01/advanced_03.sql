select 
	product_id
  , product_name
  , price
  , status
  , created_at
	from products
	order by
		price desc
	  , product_id asc
	limit 15;