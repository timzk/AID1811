from socket import * 


#执行函数中处理客户请求
def handle(connfd):
    print("connect from",connfd.getpeername())
    request = connfd.recv(4096) #获取http请求
    #将请求按照行切割
    request_lines = request.splitlines()
    # print(request)
    for line in request_lines:
        print(line)
    #给浏览器客户端返回响应
    try:
        f = open('index.html')
    except IOError:
        response = 'HTTP/1.1 404 NOT found\r\n'
        response += '\r\n'
        response += 'Error'
        
    else:
        response = 'HTTP/1.1 200 OK \r\n'
        response += '\r\n'
        response += f.read()
    finally:
        #将结果发送给客户端
        connfd.send(response.encode())
        f.close()
#在主函数中创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(10)
    print("Listen to the port 8000...")
    while True:
        connfd,addr = sockfd.accept()
        #处理客户端请求
        handle(connfd)
        connfd.close()

if __name__ == "__main__":
    main()