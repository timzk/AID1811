-- day01.dql
-- MySQL第一天的SQL语句
-- 创建表acct(账户)
create table acct (
    acct_num varchar(32),
    acct_name varchar(128)
) default charset=utf8;

-- 删除
drop table acct;
-- 重新创建acct
create table acct(
    acct_num varchar(32),-- 账号,字符串,32字节
    acct_name varchar(128), -- 户名,字符串,128字节
    cust_num varchar(32), -- 账号编号,字符串,32字节
    acct_type int,  -- 账户类型,整数型
    reg_date date, -- 开户日期,日期类型
    status int, -- 账户状态,整数型
    balance decimal(16,2) -- 数字类型,最长16位,小数点后2位
) default charset=utf8;
-- 插入
insert into acct
values('622345000001', 'Jerry', 'C0001', 1, now(), 1, 1000.00);
-- 插入多笔数据
insert into acct
values('622345000002', 'Tom', 'C0002', 1, now(), 1, 2000.00),
('622345000003', 'tim', 'C0003', 1, now(), 1, 30000.00),
('622345000004', '周大哥', 'C0004', 1, now(), 1, 888888888.00);
-- 指定字段插入
insert into acct(acct_num,acct_name)
values('622345000005','Emma')
-- 查询
select * from acct;
select acct_no "账号",-- 双引号中间为别名
	       acct_name "户名", 
	       balance / 10000 "余额(万元)"
	from acct;

      - 示例5：带条件的查询
	-- 带两个条件的查询, 两个条件同时满足
	select * from acct
	where acct_no = '622345000001'
	  and acct_name = 'Jerry';

	-- 带两个条件的查询, 两个条件满足一个
	select acct_no, acct_name, balance
	from acct 
	where acct_name = 'Jerry'
	   or acct_name = 'Tom';