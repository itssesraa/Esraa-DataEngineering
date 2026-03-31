use sakila ;
select 
 concat(c.first_name ,' ', c.last_name ) as customer_name, c.email , 
 r.rental_id,
 r.rental_date,
 r.return_date,  r.last_update
from rental r
inner join customer c  
on  c.customer_id = r.customer_id 
group by customer_name , r.rental_id

order by  r.return_date  desc ;



