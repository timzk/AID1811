#pymysql的插入示例
import pymysql

try:
    #建立连接
    conn = pymysql.connect('localhost','root','123456','bank',charset = 'utf8')
    #获取游标
    cursor = conn.cursor()
    
    sql = '''insert into acct values('62245000011','fisher','C0011',1,date(now()),2,3)
    '''
    print(sql)
    cursor.execute(sql)  #执行
    conn.commit() #提交事务
    print("插入成功")
except Exception as e:
    print(e)
    print("插入失败")
finally:
    cursor.close()
    #关闭服务器连接
    conn.close()



