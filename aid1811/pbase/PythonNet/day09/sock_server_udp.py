from socketserver import *

#创建服务器类,多进程UDP服务器
class Server(ForkingMixIn,UDPServer):
    pass


#具体请求处理类,数据报套接字
class Handler(DatagramRequestHandler):
    #具体处理方法
    def handle(self):
        print("Connect from",self.client_address)
        while True:
            #接收消息
            data = self.rfile.read(4096)
            if not data:
                break
            print(data.decode())
            #发送消息
            self.wfile.write(b'OK')

#创建服务器对象,绑定处理类
server_addr = ('0.0.0.0',8888)
server = Server(server_addr,Handler)
server.serve_forever()#启动服务
