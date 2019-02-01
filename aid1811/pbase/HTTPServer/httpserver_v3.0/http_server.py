#coding=utf-8
'''
AID httpserver v3.0
'''

from socket import *
import sys
from threading import Thread
from settings import *

def connect_frame(request_lines):
    s  = socket()
    try:
        s.connect(frame_address)#连接webFrame
    except Exception as e:
        print(e)
        return
    s.send(request_lines.encode())
    response = s.recv(4096*20).decode()
    s.close()
    return response


#将httpserver封装为类
class HTTPServer(object):
    def __init__(self,address):
        self.address = address
        self.create_socket()
        self.bind(address)
    
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def bind(self,address):
        self.ip = address[0]
        self.port = address[1]
        self.sockfd.bind(address)

    def serve_forever(self):
        self.sockfd.listen(10)
        print("Listen the port %d..."%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            print("Connect from ",addr)
        
            handle_client = Thread(target=self.handle,args=(connfd,))
            handle_client.setDaemon(True)
            handle_client.start()

    def handle(self,connfd):
        request = connfd.recv(1024)
        if not request:
            connfd.close()
            return
        request_lines = request.splitlines()
        #获取到请求行
        request_lines = request_lines[0].decode('utf-8')
        print("请求:",request_lines)
        #向webFrame发送
        response_boby = connect_frame(request_lines)
        if response_boby == "404":
            response_headlers = "HTTP/1.1 404 NOT Found\r\n"
            response_boby = "<h1>Not Found</h1>"
        else:
            response_headlers = "HTTP/1.1 200 OK\r\n"
        response_headlers += "\r\n"


        
        response = response_headlers + response_boby 
        connfd.send(response.encode())
        connfd.close()

        
# from views import *
if __name__ == "__main__":
    
    httpd = HTTPServer(ADDR)
    httpd.serve_forever() #启动http服务
    