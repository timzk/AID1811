import pymysql

try:
    #建立连接
    conn = pymysql.connect('localhost','root','123456','bank',charset = 'utf8')
    #获取游标
    cursor = conn.cursor()
    
    sql = '''update acct set balance = balance+500 where acct_num='622345000011'
    '''
    print(sql)
    cursor.execute(sql)  #执行
    conn.commit() #提交事务
    print("修改笔数:%d" % cursor.rowcount)
except Exception as e:
    print(e)
    print("修改失败")
finally:
    cursor.close()
    #关闭服务器连接
    conn.close()