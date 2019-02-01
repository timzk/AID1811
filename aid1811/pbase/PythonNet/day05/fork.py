import os
from time import sleep

print("***********************")
a = 1
#创建进程
pid = os.fork()

if pid < 0:
    print("创建失败")
elif pid == 0:
    print("a=",a)
    print("child process子进程",os.getpid(),os.getppid())
    a = 10000#子进程连同fork之前开辟的空间也会复制,但是父子进程各自空间独立,操作各自空间内容,互不影响
else :
    sleep(0.5)
    print("parent a=:",a)
    print("父进程parent pid=",os.getpid())
    print("子进程PID:",pid)