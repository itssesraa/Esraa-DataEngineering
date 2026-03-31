use sakila ;
select   concat(c.first_name,' ' ,c.last_name ) as costomer_name , c.customer_id  ,ca.city as city_name 
 from customer c
inner join address a on c.address_id = a.address_id
inner join  city ca on a.city_id = ca.city_id 
order by city_name,costomer_name  ,customer_id desc;


