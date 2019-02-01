from threading import Event,Thread
from time import sleep

s = None #设置为通信变量
e = Event()
def bar():
    print("Bar 拜山头")
    sleep(1)
    global s
    s = "天王盖地虎"
    e.set()

b = Thread(target=bar)
b.start()
print("说对口令就是自己人")
e.wait() #阻塞等待,分支线程set
if s == '天王盖地虎':
    print("确认过眼神,你是对的人")
else:
    print("打死他")
b.join()
# #创建事件对象
# e = Event()
# e.set() #设置e的set()状态
# e.clear() #清楚e的set()状态
# print(e.is_set()) #返回False
# e.wait()
# print("********************************")