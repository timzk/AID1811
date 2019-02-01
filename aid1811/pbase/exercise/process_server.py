from socket import *
from multiprocessing import Process
import sys
import signal

def handler(c,addr):
    print('ADDRESS:',addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()    
    sys.exit("退出")
    

#创建套接字对象
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(10)

signal.signal(signal.SIGCHLD,signal.SIG_IGN)
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue
    
    p = Process(target=handler,args=(c,addr))
    p.daemon = True
    p.start()