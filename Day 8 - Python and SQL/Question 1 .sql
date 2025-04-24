select count(*),

case
	when   replacement_cost between 9.99 and 19.99   then 'low'
	when   replacement_cost between 20.00 and 24.99   then 'medium'
	when   replacement_cost between 25.00 and 29.99   then 'high'
end as category

from film
group by category

-- extra question 

select count(*),

case
	when   replacement_cost between 9.99 and 19.99   then 'low'
	when   replacement_cost between 20.00 and 24.99   then 'medium'
	when   replacement_cost between 25.00 and 29.99   then 'high'
end as category

from film
where replacement_cost between 9.99 and 19.99

group by category
