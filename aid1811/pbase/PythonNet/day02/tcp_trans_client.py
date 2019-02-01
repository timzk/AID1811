from socket import *
sockfd = socket()
server_addr = (('127.0.0.1',2335))
sockfd.connect((server_addr))
try:
    fd = open('./22222.jpg','rb')
    # s = fd.read()
    while True:
        s = fd.read(1024)
        if not s:
            break
        sockfd.send(s)
    # data_server = sockfd.recv(65535)
    # print(data_server.decode())
    fd.close()
    sockfd.close()
except EOFError:
    print("打开失败")
