try:
    from BaseHTTPServer import BaseHTTPRequestHandler,BaseHTTPServer
except ImportError:
    from http.server import BaseHTTPRequestHandler,HTTPServer

#请求处理类
class RequestHandler(BaseHTTPRequestHandler):
#指定地址
    def do_GET(self):
        print(self.requestline) #请求行
        print(self.request)#套接字
        print(self.headers)#请求头
        get_file = './static'+self.requestline.split(' ')[1]
        try:
            fd = open(get_file,'rb')
        except:
            self.send_response(404) #响应码
            #响应头
            self.send_header('Type','text/html')
            self.end_headers()#响应头结束
            self.wfile.write(b"Sorry,Not Found")
        else:
            self.send_response(200) #响应码
            #响应头
            self.send_header('Type','text/html')
            self.end_headers()#响应头结束
            self.wfile.write(fd.read())
    def do_POST(self):
        pass
    def do_PUT(self):
        pass

address = ('0.0.0.0',8080)
server = HTTPServer(address,RequestHandler)
#启动服务器
server.serve_forever()
