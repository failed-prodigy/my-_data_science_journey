select title, length , 
case
	when   replacement_cost between 9.99 and 19.99   then 'low'
	when   replacement_cost between 20.00 and 24.99   then 'medium'
	when   replacement_cost between 25.00 and 29.99   then 'high'
end as category
from film f1
where length > ( select avg(length) from film f2 
where f1.replacement_cost = f2.replacement_cost)
order by length 

