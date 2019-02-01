-- customer非空约束
create table customer(
    cust_no varchar(32) not null,
    cust_name varchar(128) not null,
    tel_no varchar(32)not null
);
-- 插入数据,tel_no 字段违反非空约束
insert into customer(cust_no,cust_name)
values('C0001','Jerry');

-- 唯一约束示例:
create table customer(
    cust_no varchar(32) unique, -- 唯一约束
    cust_name varchar(128) not null,
    tel_no varchar(32)not null
);

-- 主键约束
create table customer(
    cust_no varchar(32) primary key, -- 唯一约束
    cust_name varchar(128) not null,
    tel_no varchar(32)not null
    status int default 0
);
insert into customer values("C0001","Jerry",'131313')


insert into customer(cust_no,cust_name,tel_no) values ('C0003','TOM','13131');

-- 外键
create table account(
    acct_no varchar(32) primary key,
    cust_no varchar(32) not null,
    -- 在当前表的cust_no上添加外键约束
    -- 参照customer表的cust_no字段
    constraint foreign key(cust_no)
    references customer(cust_no)
);
-- 插入customer表中存在的客户
-- 参照完整性正确,可以插入
insert into account values('0001','C0001');
insert into account values('0004','C01')--插入报错,参照完整性错误,因为C01在customer里面不存在

-- 账户交易明细表,交易流水号上创建唯一索引
create table acct_trans_detail (
    trans_sn varchar(32)  not null,        -- 交易流水号
    trans_date datetime not null,         -- 交易时间
    acct_no varchar(32)  not null,        -- 交易账号
    trans_type int,                       -- 交易类型(存款/取款/刷卡/结息)
    amt decimal(16,2) not null,           -- 交易金额   
    unique(trans_sn),                     -- 在trans_sn上创建唯一索引 
    index(trans_date)                     -- 在trans_date上创建普通索引
);

-- 查看索引
show index from acct_trans_detail;
-- 插入数据
insert into acct_trans_detail
values('2018010100001',now(),'622345000001',1,2000),
('2018010100002',now(),'622345000004',1,5000),
('2018010100003',now(),'622345000002',1,12000),
('2018010100004',now(),'622345000005',1,99900);


-- 查询时索引字段作为条件,就会使用到索引
select * from acct_trans_detail
where trans_sn = '2018010100001';
-- 创建索引
create index trans_date
on acct_trans_detail(trans_date);

-- 修改索引
alter table acct_trans_detail
add unique index trans_sn(trans_sn);

-- 删除索引
drop index 索引名称 on 表名
e.g. drop index trans_date on acct_trans_detail 