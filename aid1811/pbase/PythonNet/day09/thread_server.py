from threading import Thread
from socket import *
import sys

#客户端处理函数
def handler(c):
    print("Connect from ",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Thank you')
    c.close()

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

#接收客户端请求
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print("服务器异常:",e)
        continue
    #创建线程
    t = Thread(target=handler,args=(c,))
    t.setDaemon(True) #主线程退出,其他线程即退出
    t.start()
