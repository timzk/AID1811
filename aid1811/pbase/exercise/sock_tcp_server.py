from socketserver import *
import sys

class Server(ThreadingTCPServer):
    pass

class Handler(StreamRequestHandler):
    try:
        def handle(self):
            while True: 
                data = self.request.recv(1024)   
                if not data:
                    print("客户端退出")
                    break
                print('--->',data.decode())
                self.request.send(b'ok')
    except KeyboardInterrupt:
        sys.exit("服务器退出")
ser_addr = ('0.0.0.0',8888)
ser = Server(ser_addr,Handler)
try:
    ser.serve_forever()
except KeyboardInterrupt:
    sys.exit("服务器退出")
