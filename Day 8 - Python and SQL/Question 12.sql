select dis , avg(total) from (
select  district as dis, sum(amount) total from customer c
join address a on a.address_id = c.address_id
join payment p on p.customer_id = c.customer_id
group by district,c.customer_id)
group by dis
order by avg(total) desc

