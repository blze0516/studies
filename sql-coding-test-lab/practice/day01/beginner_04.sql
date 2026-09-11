select
	product_id
  , product_name
  , price
	from products
	where price between 50000 and 100000
	order by 
		price asc
	  , product_id asc;