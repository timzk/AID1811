from multiprocessing import Process
from time import sleep
import os 

def f1():
    sleep(5)
    print("吃饭")
    print(os.getppid(),'---',os.getpid())

def f2():
    sleep(3)
    print("睡觉")
    print(os.getppid(),'---',os.getpid())

def f3():
    sleep(4)
    print("学习Python")
    print(os.getppid(),'---',os.getpid())

things = [f1,f2,f3]
proc = []
for f in things:
    p = Process(target = f)
    
    p.start()
    print("进程名称:",p.name)
    print("进程状态:",p.is_alive())

#保留进程对象,一起回收
for i in proc:
    i.join()