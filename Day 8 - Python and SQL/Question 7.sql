select c.city as city_name , sum(amount) as total_sales from payment p

join customer cr on cr.customer_id = p.customer_id
join address a on a.address_id = cr.address_id
join city c on c.city_id = a.city_id
group by c.city
order by sum(amount) desc