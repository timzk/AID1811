#自定义进程类
from multiprocessing import Process
import time

class ClockProcess(Process):
    def __init__(self,value,name):
        self.value = value
        #通过传参把name传入到父类的__init__里,
        #就实现了修改名称的功能
        super().__init__(name=name)

    #重写run方法
    def run(self):
        for i in range(5):
            print('-->',time.ctime())
            time.sleep(self.value)

#创建自定义类进程对象
p = ClockProcess(2,name='cp')
p.start() #调用run()
print("获取进程名称",p.name)
print("获取进程PID号:",p.pid)
# p.join