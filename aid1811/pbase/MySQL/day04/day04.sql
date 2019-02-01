create table customer 
   select * from eshop.customer;
select acct.acct_num,acct.acct_name,customer.tel_no
from acct,customer