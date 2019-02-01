from threading import Thread
from socket import *
import sys

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))

s.listen(10)

def handler(c):
    print('客户端:',c.getpeername())
    while True:
        try:
            data = c.recv(1024)
            if not data:
                print("客户端退出")
                break
            print(data.decode())
            c.send(b'ok')
        except Exception as e:
            print(e)
    c.close()
    


while True:
    print("等待连接:")
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print('Error',e)
        continue
    
    thread_handler = Thread(target=handler,args=(c,))
    thread_handler.setDaemon(True)
    thread_handler.start()
