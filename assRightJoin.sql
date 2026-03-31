#1. Write a query to retrieve all payments and customer details using a RIGHT JOIN between the
use sakila ;
select p.payment_id ,p.customer_id ,
concat(c.first_name ,' ' , c.last_name  ) as fullName ,
 c.email , c.address_id ,c.create_date ,c.last_update 
 from customer c 
 right join payment p on  p.customer_id =c.customer_id 
 order by fullName , p.customer_id desc;
 
 
 ##################################################################
 
 #2. Retrieve all films and the categories, even if a category is missing for some films, using a RIGHT JOIN.
 
 use sakila;
 select f.film_id ,f.title , f.description ,ca.name
from film f
right join film_category fc on fc.film_id =  f.film_id 
right join category ca on fc.category_id =ca.category_id 
order by f.film_id ;

#########################################################################

#3. Get a list of all customers and the rental transactions they made, including customers who have not made any rentals, using RIGHT JOIN.
use sakila ;
select c.customer_id , concat(c.first_name ,' ' , c.last_name  ) as fullName ,
c.create_date ,r.rental_date
from rental r
right join customer c on  r.customer_id =c.customer_id 
order by c.customer_id ;

######################################################################################

#4. Write a query to find all films and their actors, including films with no actors, using a RIGHT JOIN.
use sakila ;
select f.film_id, f.title  ,a.actor_id ,CONCAT(a.first_name, '  ', a.last_name) AS actor_name 
from actor a
right join film_actor fa ON a.actor_id = fa.actor_id
right join film f ON fa.film_id = f.film_id
ORDER BY f.film_id;


####################################################

#5. Retrieve all film categories and the number of films in each category, including categories without films, using RIGHT JOIN.
use sakila ;
select c.name AS category_name,  COUNT(fc.film_id) AS number_of_films
from   film_category fc 
right join category c on c.category_id = fc.category_id
GROUP BY c.name
ORDER BY  number_of_films DESC ;

#######################################################################




