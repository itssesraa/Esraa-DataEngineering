#1. Write a query using a subquery to find the top 5 films with the highest rental revenue.

use sakila ;
select f.film_id ,f.title ,
( select sum(p.amount)
from payment p 
join rental r on p.rental_id = r.rental_id
join inventory i  on i.inventory_id =r.inventory_id
where i.film_id =f.film_id 
) as total_revenue 
from film f
order by total_revenue  desc limit 5 ;

#############################################################################
#2. Use a subquery to retrieve the list of customers who have rented the most films from the 'rental' table.

use sakila ;
SELECT c.customer_id, c.first_name, c.last_name
FROM customer c
WHERE c.customer_id IN (
    SELECT customer_id
    FROM rental
    GROUP BY customer_id
    HAVING COUNT(*) = (
        SELECT MAX(rental_count)
        FROM (
            SELECT customer_id, COUNT(*) AS rental_count
            FROM rental
            GROUP BY customer_id) AS sub));
####################################################################

#3. Write a subquery to get the average rental duration for each customer, and filter customers who rented for more than the average.
use sakila ;
SELECT customer_id, AVG(DATEDIFF(return_date, rental_date)) AS avg_duration
FROM rental
GROUP BY customer_id
HAVING AVG(DATEDIFF(return_date, rental_date)) > (
    SELECT AVG(DATEDIFF(return_date, rental_date))
    FROM rental
);

####################################################################
#4. Use a subquery to find all employees who have processed more than 10 rentals.
SELECT staff_id, first_name, last_name
FROM staff
WHERE staff_id IN (
    SELECT staff_id
    FROM rental
    GROUP BY staff_id
    HAVING COUNT(*) > 10
);

####################################################################
#5. Retrieve a list of films that have never been rented using a subquery in the WHERE clause.
SELECT film_id, title
FROM film
WHERE film_id NOT IN (
    SELECT i.film_id
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
);





