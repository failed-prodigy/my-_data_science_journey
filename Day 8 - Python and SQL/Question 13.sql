select  category_name, sum(total) from ( select payment_id , sum(amount) as total , c.name as category_name from payment p
join rental r on r.rental_id = p.rental_id
join inventory i on i.inventory_id = r.inventory_id
join film_category fc on fc.film_id = i.film_id
join category c on c.category_id = fc.category_id
group by c.name , payment_id
order by c.name , payment_id )
group by category_name


-- Extra Question ------

select  payment_id , sum(total) from ( select payment_id , sum(amount) as total , c.name as category_name from payment p
join rental r on r.rental_id = p.rental_id
join inventory i on i.inventory_id = r.inventory_id
join film_category fc on fc.film_id = i.film_id
join category c on c.category_id = fc.category_id
group by c.name , payment_id
order by c.name , payment_id )
where category_name = 'Action'
group by payment_id

