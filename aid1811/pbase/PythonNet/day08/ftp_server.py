from socket import * 
import os,sys
import time

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

#获取文件夹下的文件及目录
FILES = '/home/tarena/aid1811/pbase/abc/'
# l = os.listdir(f) #文件夹下的所有文件及目录
# os.path.isfile('')#判断文件是否为普通文件

#将文件处理功能封装
class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
    def do_list(self):
        print("执行查看文件")
        #获取文件列表
        file_list = os.listdir(FILES) 
        #文件目录为空则不允许获取
        if not file_list:
            wenjian = '文件列表为空'
            self.connfd.send(wenjian.encode())
            time.sleep(0.1)
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILES + file):
                files = files + file + '#'
        #将拼接好的文件字符串发送
        self.connfd.send(files.encode())
    def do_get(self,filename):
        try:
            fd = open(FILES + filename,'rb')
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        self.connfd.send(b'OK')
        time.sleep(0.1)
        #发送文件内容
        while True:
            data = fd.read(1024)
            #到文件结尾
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)
    def do_put(self,filename):
        if os.path.exists(FILES + filename):
            self.connfd.send("文件存在".encode())
            return
        try:
            fd = open(FILES + filename,'wb')
        except:
            self.connfd.send("上传失败!!".encode())
            return
        self.connfd.send(b'OK')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()

#封装并发网络模型
def main():
    #创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(10)
    while True:
        try:
            print("Listen 8888 ")
            c,addr = s.accept()
            
        except KeyboardInterrupt:
            s.close()
            sys.exit("退出服务器")
        except Exception as e:
            print("Error",e)
            continue
        print("连接客户端:",addr)
        pid = os.fork()
        if pid == 0:
            p = os.fork()#创建二级子进程
            if p == 0:
                s.close()#子进程里不需要用到s,关闭后对父进程不影响
                ftp = FtpServer(c) #创建对象
                #根据不同的请求执行操作
                while True:
                    data = c.recv(1024).decode()
                    if not data or data[0] == 'Q':
                        
                        c.close()#关闭连接
                        sys.exit("客户端退出")#子进程退出
                    elif data[0] == '1':
                        ftp.do_list()
                    elif data[0] == 'G':
                        filename = data.split(' ')[1]
                        ftp.do_get(filename)
                    elif data[0] == 'P':
                        filename = data.split(' ')[1]
                        ftp.do_put(filename)    
            else:
                os._exit(0)#子进程处理完请求即退出
        else:
            c.close()#父进程中不需要用到c,关闭后对子进程不影响
            os.wait()

main()

