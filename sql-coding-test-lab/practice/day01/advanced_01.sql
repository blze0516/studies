select 
	product_id
  , product_name
  , price
  , status
	from products
	where
		(status = 'ACTIVE' and price >= 300000)
	   or
		(status = 'SOLD_OUT' and price between 100000 and 200000)
	order by
		status asc
	  , price desc
	  , product_id asc;