1-待付款  2-待发货  3-已发货   4-已收货   5-申请退货    6-已退货    9-已废弃
1.创建库eshop,模拟电子商务平台  ,并指定编码为utf8
    create database eshop default charset=utf8;
2.创建订单表(orders,utf8编码),包含如下字段:
    create table orders(
        order_id varchar(32),
        cust_id varchar(32), 
        orger_date datetime,
        status enum('1','2','3','4','5','6','9'), 
        products_num int,
        amt decimal(16,2)
        )default charset=utf8;

3.至少插入5笔数据(要求数据库看上去尽可能真实)
    insert into orders values
        ("2019010200001","JD000001","2018-09-20 12:15:34","1",2,2156.6),
        ("2019010200002","JD000002","2018-5-10 22:5:4","2",5,2296.6),
        ("2019010200003","JD000003",now(),"1",9,8825.21),
        ("2019010200004","JD000004","2017-01-10 10:10:52","4",12,6622.1),
        ("2019010200010","JD000004","2018-11-13 09:20:52","4",2,750),
        ("2019010200005","JD000005","2018-6-12 23:08:15","3",4,901.1),
        ("2019010200006","JD000006","2018-11-11 13:30:42","4",6,1563),
        ("2019010200007","JD000007","2018-09-29 15:27:42","5",4,852),
        ("2019010200008","JD000008","2018-10-11 14:31:42","6",3,1112),
        ("2019010200009","JD000009","2018-11-20 11:30:42","9",1,120);

4.编写如下SQL语句
  1)查找所有待付款订单
  select * from orders where status =1 ;
  2)查找所有已发货/已收货/申请退货订单
  select * from orders where status = 3 or status = 4 or status = 5;
  -- select * from orders where status in ('3','4','5');
  3)查找某个客户的待发货订单
  select * from orders where status = 2;
  4)根据订单编号,查找订单下单日期/订单状态
  select * from orders where order_id = '2019010200004';
  5)查找某个客户所有订单,并按照下单时间倒序排序
  select * from orders where cust_id = 'JD000004' order by orger_date desc;
  6)统计每种状态的订单数量
  select count(*) '数量',status '状态' from orders group by status;
  7)查询所有订单最大值/最小值/平均值,所有订单总金额
  select max(amt),min(amt),avg(amt),sum(amt) from orders;
  8)查询金额最大的前3笔订单
  select * from orders order by amt desc limit 3;
  9)在表的最后,添加两个字段:
    invoice        开票状态,整数
    invoice_date   开票日期,DateTime类型
    alter table orders add invoice int;
    alter table orders add invoice_date datetime;
  10)修改某个订单状态为"已收货"
    update orders set status = 4 where cust_id ='JD000003';
  11)删除已废弃的订单
  delete from orders where status = 9;

    