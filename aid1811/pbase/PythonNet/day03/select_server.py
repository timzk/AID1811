from select import select
from socket import *
import sys,time
#创建要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
std = sys.stdin
#添加关注列表
rlist = [s,std]
wlist = []
xlist = []
f = open('./a.txt','wb')
# rs, ws, xs = select(rlist,wlist,xlist) 
while True:
    print("套接字地址族类型是:",s.family)
    print("请输入-->")

    rs, ws, xs = select(rlist, wlist, xlist) 
    #遍历三个列表确定哪个IO发生

    for r in rs:
        #如果遍历到s说明s就绪则有客户端发起连接
        if r is s:
            c,addr = r.accept()
            print("地址:",addr)
            print("getsockname()是:",c.getsockname())
            print("getpeername()是:",c.getpeername())
            print("getfamily()是:",c.family)

            rlist.append(c)

        #接收终端输入,存储到文件中
        elif r is std:
            # print("请输入-->")
            ab = r.readline()
            f.write(time.ctime().encode() + b' ' + ab.encode())
            f.flush() #清理缓存,立即将缓冲区内容放入到文件中
        #客户端连接套接字就绪,则接收消息
        else:
            data = r.recv(1024)
            if not data:
                #客户端退出从关注列表移除
                rlist.remove(r) 
                r.close()
                continue
            print("Receive from %s:%s"%(r.getpeername(),data.decode()))
            f.write(time.ctime().encode() + b' ' + data)
            f.flush()#清理缓存,立即将缓冲区内容放入到文件中
            # r.send(b'ok')
            wlist.append(r)

    for w in ws:
        w.send('收到来自服务端的消息!'.encode())
        wlist.remove(w)
    for x in xs:
        x.close()
        raise EOFError

# 作业：  1. 熟练select 服务端程序
#         2. 熟练httpserver
# 	3. 复习 类 （继承，super，__init__）
# 	4. 编写一个select服务，监听客户端的连接，客户端发送的内容，以及从终端输入的内容。将客户端发送过
#      来的内容和终端输入的内容全部备份到一个文件里

# 	sys.stdin  标准输入流
 
