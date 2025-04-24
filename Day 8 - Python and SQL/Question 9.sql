select staff_id , avg(total) from (
select staff_id,customer_id,sum(amount) total from payment group by staff_id, customer_id )
group by staff_id
