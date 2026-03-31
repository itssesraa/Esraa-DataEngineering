##. LEFT JOIN Questions (Sakila Database)   :

#1. Write a query to retrieve all customers and their rental details using a LEFT JOIN between the 'customer' and 'rental' tables. 
use sakila;
select concat(c.first_name , ' ' , c.last_name) as fullname , c.customer_id , r.rental_id ,r.rental_date ,
r.inventory_id ,r.customer_id ,
 r.return_date ,r.last_update
from customer c 
left join rental r on c.customer_id =r.customer_id 
order by r.inventory_id ,r.customer_id DESC ;


#######################################################################



#2. Retrieve all films and their corresponding categories, even if they don't have any category  assigned, using LEFT JOIN.
use sakila;
select f.film_id ,f.title  , ca.category_id ,ca.name
from film f
left join film_category fc on f.film_id =fc.film_id 
left join  category ca on  fc.category_id = ca.category_id  
order by f.film_id ;

#######################################################################


#3. Get a list of all actors and their films, including actors who haven't acted in any film, using a LEFT JOIN.
use sakila ;
select f.film_id, f.title  ,a.actor_id ,CONCAT(a.first_name, ' ', a.last_name) AS actor_name 
from actor a
left join film_actor fa on a.actor_id =fa.actor_id
left join film f on   fa.film_id =f.film_id
order by a.actor_id ,f.title;

#######################################################################

#4. Write a query to find all stores and their inventories, even if the inventory is missing for some products, using LEFT JOIN.
use sakila;
select s.store_id ,s.manager_staff_id ,i.inventory_id ,i.film_id ,i.last_update 
from store s
left join inventory i on s.store_i.d =i.store_id ;


#5. Retrieve the rental dates of all films, including films that were not rented, using a LEFT JOIN between the 'film' and 'rental' tables

use sakila;
select f.film_id ,f.title ,f.rental_rate , r.rental_date
from film f 
left join inventory i on i.film_id =f.film_id 
left join rental r on r.inventory_id =i.inventory_id 
order by film_id ,f.title ;

#######################################################################


