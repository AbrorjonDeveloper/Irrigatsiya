SELECT company_name,sum(od.quantity)
FROM public.customers as cst
JOIN public.orders as ord
ON cst.customer_id = ord.customer_id
JOIN public.order_details as od
ON ord.order_id = od.order_id
WHERE od.product_id = (
	SELECT pdid FROM(
	SELECT od.product_id as pdid, sum(quantity) as summ
	FROM public.order_details as od
	 group by od.product_id
	) AS ordp
	where summ = (
		SELECT max(summ) FROM(
	SELECT sum(quantity) as summ
	FROM public.order_details as od
	 group by od.product_id
	) AS order_product
	)
		)
	group by company_name
	order by sum desc