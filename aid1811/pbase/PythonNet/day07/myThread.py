from threading import Thread
from time import sleep,ctime

#自定义线程类
class MyThread(Thread):
    def __init__(self,target,args,kwargs,name='Tedu'):
        super().__init__(name=name)
        self.target = target
        self.args = args
        self.kwargs = kwargs
        
        
    def run(self):
        self.target(*self.args,**self.kwargs)

def player(sec,song):
    for i in range(2):
        print("Playing %s:%s"%(song,ctime()))
        sleep(sec)

t = MyThread(target=player,args=(3,),kwargs={'song':'凉凉'},name = 'Tedu')
t.start()
print(t.getName())
t.join()