#Process类属性使用
from multiprocessing import Process
from time import ctime,sleep

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())
    
p = Process(target = tm,name ='abc')
p.daemon = True #必须在start前使用
        #    默认为False 表示主进程退出不会影响子进程执行
        #    如果设置为True 表示主进程退出时子进程也会退出
        #    * 必须在start前使用
p.start()
print("进程名称:",p.name)
print("进程PID:",p.pid)
print("进程状态:",p.is_alive())

#
# p.join()