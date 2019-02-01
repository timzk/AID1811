#pymysql删除示例
import pymysql

try:
    #建立连接
    conn = pymysql.connect('localhost','root','123456','bank',charset = 'utf8')
    #获取游标
    cursor = conn.cursor()
    
    sql = '''delete from acct  where acct_num='622345000011'
    '''
    print(sql)
    cursor.execute(sql)  #执行
    conn.commit() #提交事务
    print("删除笔数:%d" % cursor.rowcount)
except Exception as e:
    print(e)
    print("删除失败")
finally:
    cursor.close()
    #关闭服务器连接
    conn.close()