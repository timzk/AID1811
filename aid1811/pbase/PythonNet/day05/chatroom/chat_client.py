#coding:utf-8
#聊天室客户端
from socket import *
import os,sys,time

#接收服务器发送过来的消息,显示出来
def recv_msg(s):
    while True:
        data, addr = s.recvfrom(1024)
        #服务器发来EXIT表示要退出
        if data.decode() == 'EXIT':
            sys.exit(0)
        print(time.ctime(),'-->',data.decode() +'\n消息:',end ='')


def send_msg(s,name,addr):
    while True:
        text = input("消息:-->")
        if text == '##':
            msg = 'Q ' + name
            s.sendto(msg.encode(),addr)
            sys.exit('退出聊天室')
        msg = "C %s %s" %(name,text)
        s.sendto(msg.encode(),addr)

#创建套接字
def main():
    #从命令行输入IP
    if len(sys.argv) < 3:
        print("argv is error!!")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    #创建UDP套接字
    s = socket(AF_INET,SOCK_DGRAM)

    while True:
        name = input("请输入姓名:")
        msg = 'L ' + name
        s.sendto(msg.encode(),ADDR)
        #等待回应
        data,addr = s.recvfrom(128)
        if data.decode() == 'ok':
            print("已进入聊天室")
            break
        else:
            print(data.decode())
    #创建父子进程
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败!")
    elif pid == 0: #子进程发消息
        send_msg(s,name,ADDR)
    else: #父进程收消息
        recv_msg(s) #接收消息

main()