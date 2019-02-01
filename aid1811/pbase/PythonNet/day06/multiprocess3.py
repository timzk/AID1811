from multiprocessing import Process
from time import sleep

#带参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working....")

#按照位置传递参数
# p = Process(target = worker,args = (2,'周老板'))
#按照键的名称传递参数
p = Process(target = worker,kwargs = {'sec':2,'name':'周老板'})
#也可以两种传参方式混用args=(2,)元组传参,如果只有一个参数,必须后面跟逗号
p = Process(target = worker,args = (2,),kwargs = {'name':'周老板'})
p.start()
print('进程名称',p.name
print('进程PID',p.pid)
p.join()