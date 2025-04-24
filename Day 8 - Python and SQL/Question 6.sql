select * from address a 
left join customer c on a.address_id = c.address_id
where c.address_id is Null