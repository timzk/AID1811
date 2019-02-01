from socket import *
from threading import Thread
import sys


class Http_Server(object):
    def __init__(self,server_addr,static_dir):
        self.server_addr = server_addr
        self.static = static_dir
        self.creat_server()

    def creat_server(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_addr)
        self.sockfd.listen(10)
    
    def serv_server(self):
        while True:
            try:
                #创建套接字对象
                c,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                sys.exit("服务器退出")
            except Exception:
                print("ERROR")
                continue
            #创建多线程
            thr = Thread(target=self.client_handler,args=(c,))
            thr.setDaemon(True)
            thr.start()
    #子进程客户端处理函数
    def client_handler(self,connfd):
        request = connfd.recv(4096)
        #客户端断开,服务器连接即断开
        if not request:
            connfd.close()
            return
        



if __name__ == "__main__":
    server_addr = ('0.0.0.0',8888)
    static_dir = './static'
    httpd = Http_Server(server_addr,static_dir)
    httpd.serv_server()
    