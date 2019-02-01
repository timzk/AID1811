from socket import *
from time import sleep
import sys
import getpass

def do_register(s):
    #判断用户名密码是否合法
    while True:
        name = input("User:")
        passwd = getpass.getpass()
        passwd1 = getpass.getpass("Again:")
        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不能有空格")
            continue
        if passwd != passwd1:
            print("两次密码不一致")
            continue
        msg = "R %s %s"%(name,passwd)
        #发送请求
        s.send(msg.encode())
        #等待回复
        data = s.recv(128).decode()
        if data == 'OK':
            print("注册成功")
            login(s,name)#注册成功直接进入二级界面
        elif data == 'EXISTS':
            print("用户已存在")
        else:
            print("注册失败!")
        return

def do_login(s):
    while True:
        name = input("User:")
        passwd = getpass.getpass("请输入密码")
        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不能有空格")
            continue
        msg = "L %s %s"%(name,passwd)
        s.send(msg.encode())
        #等待回复
        data = s.recv(128).decode()
        if data == 'OK':
            print("登录成功!")
            login(s,name)
        elif data  == 'EXISTS':
            print("用户名密码错误!请重新输入!")
            continue
        return

def login(s,name):
    while True:
        print('''
        =============查询界面=============
        1.查询       2历史记录       3.返回
        ''')
        try:
            cmd = input("-->请输入选项:")
        except KeyboardInterrupt:
            sys.exit("客户端退出")
        if cmd not in ['1','2','3']:
            print("请输入正确选项!!")
            sys.stdin.flush()#清楚标准输入
            continue
        elif cmd == '1':
            select_dict(s,name)
        elif cmd == '2':
            history_words(s,name)
        elif cmd == '3':
            return

def history_words(s,name):
    msg = "H %s"%name
    s.send(msg.encode())
    print("|       单词      |                                   解释                                 |                  查询时间                |")
    
    while True: 
        data = s.recv(1024).decode()
        if data == 'FAIL':
            print('没有查询记录')
            break
        l = data.split('##')
        # print(l)
        if data == '#':
            break
        print('|',l[0].center(15),'|',l[1].center(70),'|',l[2].center(40),'|')
    

def select_dict(s,name):
    while True:
        try:
            select_word = input("请输入要查找的单词-->")
        except KeyboardInterrupt:
            sys.exit("客户端退出!")
        if (' ' in select_word):
            print("请输入单词,不是词组!")
            continue
        elif select_word == '2':
            history_words(s,name)
        elif select_word == '3':
            return
        msg = "D %s %s"%(select_word,name)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        if data == 'FAIL':
            print("没有查到到你要的单词!!")
        elif data != 'FAIL':
            print("解释为:-->",data)
            
def main():
    s = socket()
    s.connect(('127.0.0.1',8888))
    while True:   
        print('''
        ===========Welcome===========
        ----1.注册  2.登录 3.退出----
        =============================
        ''')
        try:
            cmd = input("-->请输入选项:")
        except KeyboardInterrupt:
            sys.exit("客户端退出")
        if cmd not in ['1','2','3']:
            print("请输入正确选项!!")
            sys.stdin.flush()#清楚标准输入
            continue
        elif cmd == '1':
            do_register(s) #注册功能
        elif cmd == '2':
            do_login(s) #登录操作
        elif cmd == '3':
            s.send(b'E')
            sys.exit("退出")
    s.close()

main()
