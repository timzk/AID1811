#进程池创建
from multiprocessing import Pool
from time import sleep,ctime

#创建事件函数
def worker(msg):
    print("ac",flush=True)
    sleep(2)
    print(msg,flush=True)
result = []
#创建进程池,默认系统自动设置
pool = Pool()
#向进程池添加事件
for i in range(10):
    msg = 'hello %d' %i
    #异步执行:多个一同执行
    r = pool.apply_async(func=worker,args=(msg,))
    result.append(r)
#关闭进程池-
pool.close()
#回收进程
pool.join()

for i in result:
    print(i.get()) #获取函数返回值
