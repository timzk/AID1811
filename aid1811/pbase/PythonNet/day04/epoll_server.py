from socket import *
from select import *

#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(10)

#创建EPOLL对象
p = epoll()

#建立查找字典
fdmap = {s.fileno():s}
print(fdmap)
#注册关注IO
p.register(s,EPOLLIN|EPOLLERR)

while True:
    #监控所有IO事件
    events = p.poll()
    print('这是events', events)
    for fd,event in events: #events 是一个列表,返回所有就绪的IO [(fileno,event),...]
        print(type(fd))
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from:",addr)
            #添加新的关注事件 添加边缘触发IO事件
            p.register(c,EPOLLIN|EPOLLHUP|EPOLLERR|EPOLLET)
            fdmap[c.fileno()] = c  # fdmap的键c.fileno,值c
        #通过按位与判断是否是某个事件就绪
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                #客户端退出则取消关注,从字典删除
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("Receive:",data.decode())
                fdmap[fd].send(b'ok')