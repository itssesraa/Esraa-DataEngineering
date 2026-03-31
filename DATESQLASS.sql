
#1. Write a query to extract the year, month, and day from the rental_date in the rental table.

use sakila ;
select year(rental_date ) as yearss ,monthname(rental_date) as months ,day(rental_date) as days
   from rental ;

                                            ###########################

#2. Write a query to calculate the number of days between rental_date and return_date.
use sakila ;
select 
datediff(return_date,rental_date) as day_diff 
from rental ;

                                            ###########################
 #3. Write a query to find all rentals made in the last 7 days using MAX(rental_date).
 
 use sakila ;
 select count(*) as last7day 
 from rental 
 where rental_date >= (select   max(rental_date )  - INTERVAL 7 DAY  
  from rental
) ;

                                             ###########################
# 4. Write a query to count how many rentals took more than 5 days to return.
use sakila ;
select count(*) as last5day 
from rental 
where return_date  is not null and datediff(return_date,rental_date) >5 
;
                                               ###########################
 # 5. Write a query to extract the hour and minute from the rental_date.
 use sakila ;
 select hour(rental_date) as hours_rental ,minute(rental_date) as minute_rental 
 from rental
 group by hours_rental,  minute_rental ;

                                               ################################
