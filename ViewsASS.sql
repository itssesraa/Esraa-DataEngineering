#1. Create a view that shows customer_id, full name, and total payments made by each customer.
use sakila;
create view cus_total_payments  AS         
select  c.customer_id  ,   concat(c.first_name , ' ' , c.last_name) as fullname  ,  SUM(amount) AS total_payments
from customer c 
join payment p on c.customer_id =p.customer_id 
Group BY    c.customer_id, c.first_name, c.last_name ;
SELECT * FROM cus_total_payments;
##########################################################
#2. Create a view that shows film titles and the number of times they were rented.
use sakila;
create view  film_rented as 
select  f.film_id , f.title  ,  COUNT(r.rental_id) AS times_rented
from film f 
join inventory i  on f.film_id =i.film_id 
join rental r on r.inventory_id = i.inventory_id
group by  f.title , f.film_id  ;
select * from film_rented ;
##########################################################
#3. Create a view to list total sales per store using staff and payment tables.
use sakila ;
create view total_sales as
select   s.store_id , sum(p.amount)as total_sales1
from staff s
join payment p  on s.staff_id =p.staff_id 
group by  s.store_id;
select * from total_sales ;
##########################################################
#4. Drop an existing view named 'CustomerRentals' and recreate it with additional email column.
DROP VIEW IF EXISTS CustomerRentals;
CREATE VIEW CustomerRentals AS
SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS fullname,
c.email, COUNT(r.rental_id) AS total_rentals
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, fullname, c.email;

##########################################################

#5. Select top 10 rows from the view you created in question 1.
create  view top10_row as
select   c.customer_id  ,  concat(c.first_name , ' ' , c.last_name) as fullname  ,  SUM(amount) AS total_payments 
from customer c 
join payment p on c.customer_id =p.customer_id 
Group BY    c.customer_id, c.first_name, c.last_name
limit 10 ;
select * from top10_row;
################# orrrr#############5:
SELECT * 
FROM cus_total_payments
ORDER BY total_payments DESC
LIMIT 10;
