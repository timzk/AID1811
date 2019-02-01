#coding=utf-8
#聊天室服务端
from socket import *
import os,sys 

def do_quit(s,user,name):
    msg = "\n%s 退出了聊天室" % name 
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    #删除该用户
    del user[name]

#接收并处理请求
def do_request(s):
    #存储结构 {'姓名':('127.0.0.1',9999)}
    user ={}
    while True:
        msg, addr = s.recvfrom(1024)
        # print('发送过来的msg信息为',msg.decode())
        
        msgList = msg.decode().split(' ')#拆分传输过来的用户名,用空格分开存入列表
        #此时msgList里面存储的是字典,第0个是字母L,第一个是姓名
        #区分请求类别
        #如果是L打头代表是用户登录
        if msgList[0] == 'L':
            do_login(s,user,msgList[1],addr)
        #如果接收到的内容是C开头,执行消息发送
        elif msgList[0] == 'C':
            msg = ' '.join(msgList[2:])
            do_chat(s,user,msgList[1],msg)
        #如果接收到的内容是Q开头shilihua行给其他用户发送退出消息
        elif msgList[0] == 'Q':
            do_quit(s,user,msgList[1])

def do_chat(s,user,name,msg):
    msg = "\n%s 说: %s"%(name,msg) 
    #循环发送给所有人,除了自己
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i]) #('127.0.0.1',9999)
            
def do_login(s,user,name,addr):
    if (name in user) or name  == '管理员':
        s.sendto('\n该用户已存在'.encode(),addr)
        return
    else:
        s.sendto(b'ok',addr)
    #先通知其他人
    msg = '\n欢迎 %s 进入聊天室' %name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户插入
    user[name] = addr

#创建网络连接
def main():
    ADDR = ('0.0.0.0',7776)
    #创建UDP套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    #创建多进程,一个处理客户端请求,另一个发送管理员消息
    pid = os.fork()
    if pid < 0:
        print("Create process failed")
        return 
    #子进程发送管理员消息
    elif pid == 0:
        while True:
            msg = input("\n管理员消息:")
            msg = 'C 管理员 ' + msg
            s.sendto(msg.encode(),ADDR)
    #父进程处理客户端请求
    else:
        do_request(s)

main()