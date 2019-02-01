#tcp_server.py
import socket
#创建TCP套接字连接
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)


sockfd.bind(('127.0.0.1',8887))

#设置监听
sockfd.listen(10)

#等待处理客户端连接
print("connect")

# print("connect from",addr)

#消息收发
while True:
    connfd,addr = sockfd.accept()
    while True:
        data = connfd.recv(1024) #设置一次性接收多少字节
        
        if not data:
            print('这是空的值',data)    
        
            break
        print("客户端发送的是:",data.decode())
        connfd.send(b"I see")
        
    connfd.close()

sockfd.close()    
 