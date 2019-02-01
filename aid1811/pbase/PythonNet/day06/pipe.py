from multiprocessing import Process,Pipe
import os,time

#创建管道对象
fd1,fd2 = Pipe()

def fun(name):
    time.sleep(3)
    fd1.send(name)

jobs = []
for i in range(5):
    p = Process(target = fun,args = (i,))
    jobs.append(p)
    p.start()

#父进程从管道读取消息
for i in range(5):
    data = fd2.recv()
    print(data)

for i in jobs:
    i.join()