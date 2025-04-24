select title , length , c.name as category from film f
join film_category fc on fc.film_id = f.film_id
join category c on c.category_id = fc.category_id
where c.name in ('Drama','Sports')
order by length desc 


-- for extra question

limit 1