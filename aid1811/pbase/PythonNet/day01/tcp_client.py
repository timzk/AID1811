from socket import *
#创建套接字
sockfd = socket() #默认值socket.AF_INET,socket.SOCK_STREAM

#发起连接请求
server_addr = (('127.0.0.1',8888)) #服务器地址
sockfd.connect(server_addr)

#消息收发
while True:
    
    data = input('--请输入->>')
    if not data:
        sockfd.close()
        break
    sockfd.send(data.encode())
    data_server = sockfd.recv(1024)
    if not data_server:
        sockfd.close()
        break 
    print(data_server.decode())
   
sockfd.close()
        
        
        
