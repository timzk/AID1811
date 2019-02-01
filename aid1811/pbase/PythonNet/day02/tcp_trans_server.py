from socket import *

s = socket()
s.bind(('0.0.0.0',2335))
s.listen(10)
c,addr = s.accept()

try:
    fd = open('./PythonNet/day02/c.jpg','wb')
    while True:
        data_client = c.recv(65535)
        if not data_client:
            c.send('接收完毕'.encode())
            break
        fd.write(data_client)
    fd.close()
    c.close()
    s.close()
except EOFError:
    print("打开失败")

