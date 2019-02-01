import os
from time import sleep
# 进程特征:
#     1.进程可以使用计算机的多核资源
#     2.进程是计算机分配资源的最小单位
#     3.进程之间运行互不影响,各自独立
#     4.每个进程空间独立,各自占有资源,互不干扰
# pid = os.fork()
#   功能:创建新的进程
#   返回值:失败  返回一个负数
#         成功  在原进程中返回新进程的PID号,在新进程中返回0
# pid = os.fork()
# #此时在内存空间中开辟了一个新的空间,创建了一个跟父进程一模一样的的子进程,而且两个进程同时执行,谁先抢占了时间片谁先执行
# if pid < 0 :
#     print("Create process error")
# elif pid == 0:
#     sleep(2)
#     print("New process新进程",pid)
# else:
#     sleep(3)
#     print("The old process父进程",pid)

# print("fork test end...")

print("***********************")
a = 1
pid = os.fork()

if pid < 0:
    print("创建失败")
elif pid == 0:
    print("a=",a)
    print("new pid子进程",pid)
    a = 10000 #子进程连同fork之前开辟的空间也会复制,但是父子进程各自空间独立,操作各自空间内容,互不影响
else :
    sleep(1)
    print("parent a=:",a)
    print("父进程 pid=",pid)

#打印4句
#--> The old process
#--> fork test end...
#--> New process
#--> fork test end...