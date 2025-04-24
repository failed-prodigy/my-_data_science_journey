select first_name, last_name , count(*) from actor a

join film_actor fa on fa.actor_id = a.actor_id
join film f on f.film_id = fa.film_id
group by first_name,last_name
order by count(*) desc