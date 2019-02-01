from socket import *
from time import sleep,ctime 

#创建套接子
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(3)

#设置sockfd为非阻塞
# sockfd.setblocking(False)

#设置sockfd的超时时间
sockfd.settimeout(5)

n = 0
while True:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept() #阻塞等待
    except timeout:
        print("等不起啊.......")
    except BlockingIOError:
        sleep(2)
        n += 2
        print("等待连接%d sec"%n,ctime())
    else: 
        print("Connect from",addr)
        data = connfd.recv(1024)
        print("Receive:",data.decode())
        n = 0