from socket import *
import os,sys


def client_handler(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'I see')
    c.close()


#创建客户端处理
HOST = '0.0.0.0'
POST = 8888
ADDR = (HOST,POST)


s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(10)

print("等待连接")

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print("Error",e)
        continue
    p = os.fork()
    if p == 0:
        p1 = os.fork()
        if p1 == 0:
            s.close()
            client_handler(c)
            sys.exit("子进程退出")
    else:
        c.close()
        os.wait()

    
