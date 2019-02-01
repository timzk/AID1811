import multiprocessing as mulp
from time import sleep
#编写进程函数
a = 1
def fun():
    sleep(2)
    global a
    print("修改前a =",a)
    a = 10000
    print("子进程事件")
# 使用multiprocessing创建进程,同样子进程复制父进程的全部代码段,
# 父子进程执行互不影响,各自有各自的运行空间,子进程只执行函数部分

#创建进程对象
p = mulp.Process(target = fun)

#启动进程
p.start()
sleep(4)
print("父进程事件")
#回收进程,阻塞等待函数,避免产生僵尸进程
p.join()

print("Parent a:",a)
while True:
    pass
