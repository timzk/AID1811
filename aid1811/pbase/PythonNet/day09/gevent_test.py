import gevent
from time import sleep
def foo(a,b):
    print("Running foo",a,b)
    gevent.sleep(2)
    print("Running foo again")

def bar():
    print("Running bar")
    gevent.sleep(3)
    print("Running bar again")


#创建协程对象
f = gevent.spawn(foo,1,2)
g = gevent.spawn(bar)

gevent.joinall([f,b])