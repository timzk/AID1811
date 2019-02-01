#多进程并发
from socket import * 
import os,sys

#客户端处理函数
def client_handler(c):
    print("客户端:",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Thank you!')
    c.close()  


#创建套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

s = socket() #创建TCP套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(10)

#循环等待接收客户端连接请求
print("Listen to the port 888...")
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print("Error:",e)
        continue
    #创建新的子进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        print("一级子进程aa:",os.getpid())
        print("一级子进程的父进程",os.getppid())
        p = os.fork()
        if p == 0: #二级子进程
            s.close() #子进程里不需要用到s,关闭后对父进程不影响
            client_handler(c) #处理具体请求
            sys.exit(0) #子进程处理完请求即退出
        else:
            print("二级子进程PID",os.getpid())
            os._exit(0)
    #父进程或者创建进程失败都继续等待下一个客户端连接
    else:
        c.close()#父进程中不需要用到c,关闭后对子进程不影响
        print("一级子进程PID",os.getpid())
        # os.wait()