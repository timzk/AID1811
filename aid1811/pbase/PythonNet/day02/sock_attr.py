from socket import *
s = socket()
#设置端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
print(s.type) #套接字类型 SOCK_STREAM
print(s.family) #套接字地址族类型 AF_INET
s.bind(('127.0.0.1',8888))
print(s.getsockname) #获取绑定地址
print(s.fileno())
s.listen(3)
c,addr = s.accept()
print("addr:",c.getpeername())

data = c.recv(1024)
c.close()
s.close()