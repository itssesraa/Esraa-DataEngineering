use sakila ;
select sf.staff_id , s.store_id as storeId ,
  concat(sf.first_name ,' ' , sf.last_name) as staffname
from staff sf 
inner join store s  on s.store_id =sf.store_id 
order by storeId , staffname ;


