#1. Create a procedure that takes a customer_id and returns total
use sakila ;
DELIMITER //
create procedure customer_returns_total(in cod int)
BEGIN
select 
c.customer_id ,sum(p.amount) as returns_total ,CONCAT(c.first_name, ' ', c.last_name) AS full_name
from 
customer c
join payment p on p.customer_id =c.customer_id 
where c.customer_id = cod 
GROUP BY c.customer_id, c.first_name, c.last_name ;
 END //
DELIMITER ;
CALL customer_returns_total(5 );
#############################################################################
#2. Create a procedure that returns rental records between two input dates
use sakila ;
DELIMITER //
create procedure returns_rental_records (
IN   start_data  date ,
in end_date  date  )
begin 
select r.rental_date ,r.customer_id ,r.return_date ,p.payment_date ,  r.return_date
from rental r 
join payment p on p.rental_id =r.rental_id 
where r.rental_date between start_data and end_date
;end //
DELIMITER ;
CALL returns_rental_records('2005-05-01', '2005-06-01');
#DROP PROCEDURE IF EXISTS returns_rental_records;

####################################################################################################

#3. Create a procedure to return top 5 rented films by payment amount :
use sakila ;
DELIMITER //
create procedure Films_payment() 
begin 
select f.title ,f.film_id , sum( p.amount ) as total_payments 
from film f
join  inventory i on i.film_id =f.film_id 
join  rental r  on r.inventory_id =i.inventory_id 
join payment p on p.rental_id = r.rental_id 
group by f.title ,f.film_id 
order by total_payments desc
limit 5 ;
end // 
DELIMITER ;
call Films_payment();
#########################################################
#4. Create a procedure that calculates total payments by film category.
use sakila ;
DELIMITER //
create procedure film_category()
begin 
select   c.name AS category_name ,  SUM(p.amount) AS total_payments
FROM category c
    JOIN film_category fc ON fc.category_id = c.category_id
    JOIN film f ON f.film_id = fc.film_id
    JOIN inventory i ON i.film_id = f.film_id
    JOIN rental r ON r.inventory_id = i.inventory_id
    JOIN payment p ON p.rental_id = r.rental_id
    GROUP BY c.name
   ORDER BY SUM(p.amount) DESC
    LIMIT 5;
end // 
DELIMITER ;
CALL film_category();
#DROP PROCEDURE IF EXISTS film_category;
###############################################################
#5. Drop a procedure named GetCustomerPayments if it exists.

DROP PROCEDURE IF EXISTS GetCustomerPayments;




