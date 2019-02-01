from socket import * 
import sys

#从命令行传入服务器IP PORT
HOST = sys.argv[1]
PORT = sys.argv[2]
addr = (HOST,int(PORT))

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#消息收发
while True:
    data  = input('msg-->')
    if not data:
        break
    sockfd.sendto(data.encode(),addr)
    msg,addr = sockfd.recvfrom(1024)
    print("From sever:",msg)
sockfd.close()