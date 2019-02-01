from socket import *
from multiprocessing import Process
import os,sys
import pymysql
import time
import signal


def do_child(c,db):
    print("Connect from :",c.getpeername())
    while True:
        data = c.recv(128).decode()
        if (not data) or data[0] == 'E':
            c.close()
            sys.exit("客户端退出")
        elif data[0] == 'R':
            do_register(c,db,data)
        elif data[0] == 'L':
            do_login(c,db,data)
        elif data[0] == 'D':
            do_select(c,db,data)
        elif data[0] == 'H':
            do_history(c,db,data)

def do_history(c,db,data):
    l = data.split(' ')
    his_name = l[1]
    cursor = db.cursor()
    sql = "select hist.word,words.interpret ,hist.time  from hist left join words on hist.word=words.word where hist.name ='%s' order by time desc limit 10"%his_name
    cursor.execute(sql)
    r = cursor.fetchall()
    if r == ():
        c.send(b'FAIL')
    elif r != None:
        y = 0
        for i in r :
            dict_word = ''
            for x in i:
                dict_word += (x+'##')
            if y < len(r):
                c.send(dict_word.encode())
                y += 1
                time.sleep(0.02)
            if y == len(r) :
                c.send(b'#')
                y += 1
            time.sleep(0.02)
            
def do_select(c,db,data):
    l = data.split(' ')
    sel_word = l[1]
    sel_name = l[2]
    cursor = db.cursor()
    sql = "select * from words where word ='%s'"%sel_word
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b'FAIL')
    elif r != None:
        c.send(r[2].encode())
        insert_word = "insert into hist(name,word,time) values('%s','%s','%s')"%(sel_name,sel_word,time.ctime())
        cursor.execute(insert_word)
        db.commit()
        print("插入单词成功!")

def do_register(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()    
    sql = "select * from user where name = '%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()

    if r != None:
        c.send(b'EXISTS')
        return
    sql = "insert into user (name,passwd) values ('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except Exception:
        db.rollback()
        c.send(b'FAIL')

def do_login(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()    
    sql = "select * from user where name = '%s' and passwd='%s'"%(name,passwd)
    cursor.execute(sql)
    r = cursor.fetchone()
    
    if r == None:
        c.send(b'EXISTS')
        return
    c.send(b'OK')
    print("登录成功")

def main():
    db = pymysql.connect('localhost','root','123456','dict')
    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("Error:",e)
            continue

        pid = Process(target=do_child,args=(c,db))
        pid.daemon = True
        pid.start()


if __name__ == "__main__":
    ADDR = ('0.0.0.0',8888)
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(10)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    main()