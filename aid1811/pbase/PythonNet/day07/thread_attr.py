from threading import Thread,currentThread
from time import sleep

def fun():
    print("当前线程:",currentThread().getName())
    sleep(3)
    print("线程属性示例")

t = Thread(target=fun,name='tedu')
#设置daemon
t.setDaemon(True)
print("Daemon:",t.isDaemon())
t.start()
#线程名称
t.setName('momo')

print("name",t.getName())
print('线程状态:',t.is_alive())

# t.join()
