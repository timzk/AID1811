#pymysql_test.py
#pymysql查询示例
# 第一步:导入pymysql模块
# 第二步:建立到数据库服务器的连接
# 第三步:创建游标对象(cursor),通过调用数据库连接对象获得游标
# 第四步:利用cursor对象,执行SQL语句
# 第五步:提交事务(如果需要)
# 第六步:关闭游标对象
# 第七步:关闭数据库连接对象
import pymysql
host = 'localhost'  #服务器地址
user = 'root'  #用户名
password = '123456'  
dbname = 'bank'  #库名称
#建立到数据库服务器的连接,创建连接对象
conn = pymysql.connect(host,user,password,dbname,charset='utf8')
print(conn)
cursor = conn.cursor() #游标
sql = 'select * from acct'
cursor.execute(sql) #执行SQL语句
#取出查询结果,并打印
result = cursor.fetchall()  #获取表中所有数据,返回的是一个元组对象
for r in result:
    acct_no = r[0]
    acct_name = r[1]
    if r[6]: #判断是否为空NULL
        balance = float(r[6]) #余额
    print('账号:%s,户名%s,余额:%.2f' % (acct_no,acct_name,balance))

#关闭游标对象
cursor.close()
#关闭数据库连接对象
conn.close()