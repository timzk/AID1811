#acct_manage.py
#账户管理系统,实现账户增删改查
import pymysql

db_conn = None
#main()
def main():
    #连接数据库
    if conn_database() < 0:
        return
    #循环打印菜单,根据菜单的选择执行不同函数
    while True:
        print_menu()
        oper = input("请选择操作:")
        if not oper: #未输入值
            continue
        if oper == '1': #查询
            query_acct()
        elif oper == '2': #新建
            new_acct()
        elif oper == '3': #修改
            update_acct()
        elif oper == '4': #删除
            delete_acct()
        elif oper == '5': #退出
            break
        else:
            print("请输入正确的值")
    #关闭数据库
    close_database()

#连接数据库函数
def conn_database():
    global db_conn
    db_conn = pymysql.connect('localhost','root','123456','bank',charset='utf8')
    if not db_conn: #连接失败
        print("连接数据库失败")
        return -1
    else:  #连接成功
        return 0
def print_menu():
    menu = '''
    --------------账户管理系统--------------
        1 - 查询账户信息
        2 - 新建账户
        3 - 修改账户
        4 - 删除账户
        5 - 退出
    '''
    print(menu)
    return

#关闭数据库连接
def close_database():  
    global db_conn
    if db_conn: #判断是否连接成功,对象是否为None
        db_conn.close()
def query_acct():
    acct_no = input("请输入账户账号:")
    if acct_no and acct_no !='':#查询账户,如果用户输入账户,则以账号为条件进行查询
            sql = '''
            select * from acct
            where acct_num = '%s'
        ''' % acct_no 
    else: #用户未输入账户,查询所有
        sql = "select * from acct"
    global db_conn
    cursor = db_conn.cursor() #获取游标
    try:
        cursor.execute(sql) #执行SQL语句
        result = cursor.fetchall() #获取所有数据,fetchone获取一条,fetchmany获取指定
        if cursor.rowcount == 0:  #判断sql语句是否查到了数据,如果未查到值,则表明账号输入错误,rwocount代表影响行数
            print('没有此账号')
        for r in result: #遍历,打印
            acct_no = r[0]  #账号
            acct_name = r[1] #户名
            if r[6]:
                balance = float(r[6]) #余额
            print("账户:%s,户名:%s,余额:%.2f" %(acct_name,acct_no,balance))
    except Exception as e:
        print("查询异常")
        print(e)
    return

def new_acct(): #新增账户
    try:
        acct_no = input("请输入账号:")
        acct_name = input("请输入户名:")
        cust_no = input("请输入客户编:")
        acct_type = input("请选择账户类型: 1-借记卡  2-理财卡")
        balance  = float(input("请输入开户金额:"))
        assert acct_type in ['1','2']  #判断acct_type是否合法
        assert balance >= 10.00
        
        #拼装SQL语句,执行插入
        sql  = '''insert into acct values
        ('%s','%s','%s',%s,date(now()),1,%.2f)  
        ''' % (acct_no,acct_name,cust_no,acct_type,balance) 
        
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql) #执行
        db_conn.commit() #提交
        print("插入成功")
    except Exception as e:
        db_conn.rollback() #回滚事务
        print("插入操作失败")
        print(e)
    return

def update_acct():
    global db_conn
    try:
        acct_num = input("请输入账号")
        balance_dp = input('请选择: 1-存钱  2-取钱')
        balance = input('请输入金额:')
        if balance_dp == '1':
            sql = '''update acct set balance=balance + %s where acct_num = '%s' 
            '''% (balance,acct_num)
        elif balance_dp == '2':
            sql = '''update acct set balance=balance - %s where acct_num = '%s' 
            '''% (balance,acct_num)
        else:
            print("输入错误")
        print(sql)
        cursor = db_conn.cursor() #获取游标
        cursor.execute(sql)  #执行
        db_conn.commit() #提交事务
        if cursor.rowcount == 0:  #判断sql语句是否查到了数据,如果未查到值,则表明账号输入错误,rwocount代表影响行数
            print('没有此账号')
        else:
            print('成功')
    except Exception as e:
        db_conn.rollback()
        print("失败")
    return

def delete_acct():
    global db_conn
    try:
        acc_num = input("请输入要注销的账号")
        if acc_num and acc_num != '':
            sql = ''' select balance from acct where balance <= 0 and acct_num = '%s'
            ''' % acc_num
        else:
            print('请输入账号')
        cursor = db_conn.cursor() #获取游标
        cursor.execute(sql)  #执行
        # db_conn.commit() #提交事务
        if cursor.rowcount == 0:  #判断sql语句是否查到了数据,如果未查到值,则表明账号输入错误,rwocount代表影响行数
            print('此账号还有钱')
        else:
            sql_del = '''delete from acct where acct_num ='%s' ''' % acc_num
            cursor.execute(sql_del)  #执行
            db_conn.commit() #提交事务
            print("注销账号成功!")
    except Exception as e:
        print("失败")
        

#主函数
if __name__ == "__main__":
    main()


