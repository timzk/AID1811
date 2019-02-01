from socket import *
import os,sys

#具体请求功能
class Ftp_connect:
    def __init__(self,sockfd):
        self.sockfd = sockfd
    def select_file(self):
        self.i = 1
        self.sockfd.send(b'1')#发送请求
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            self.files = data.split('#')
            
            for file in self.files:
                print(self.i,':',file)
                self.i += 1
        else:
            print(data)#打印无法操作的原因
        return 1
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用!")
    def do_down(self,file_no,file_name):
        #发送文件名称
        self.sockfd.send(('G '+self.files[file_no - 1]).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK' :
            fd = open(file_name,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("复制成功")
        else:
            print(data)
    def do_put(self,file_name):
        try:
            f = open(file_name,'rb')
        except Exception:
            print("没有找到文件")
            return
    #     self.sockfd.send('P ' +)

def main():
    #创建TCP套接字
    sockfd = socket()
    HOST = '127.0.0.1'
    PORT = 8888
    ADDR = (HOST,PORT)
    sockfd.connect(ADDR)
    ftp_con = Ftp_connect(sockfd) #创建对象
    #打印菜单
    while True:
        print("---------------------")
        print("请选择菜单:")
        print("1.查看有哪些文件")
        print("2.下载文件")
        print("3.上传文件")
        print("4.退出")
        s = input("请输入:")
        
        if s == '1':
            ftp_con.select_file()

        elif s == '2' and ftp_con.select_file(): 
            try:
                file_no = int(input("请输入要复制的文件编号:"))
            except Exception:
                print("请输入正确的编号!!!!!")
                continue
            if file_no < len(ftp_con.files):
                file_name = input("-->请输入文件名:")
                ftp_con.do_down(file_no,file_name)
            else:
                print("此编号没有对应的文件!!!!!!!!")
                continue
            
        elif s == '3':
            ftp_con.do_put()
        elif s.strip() == '4':
            ftp_con.do_quit()
        else:
            print("输入错误")

main()