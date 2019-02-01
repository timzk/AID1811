#此示例示意僵尸进程
import os
from time import sleep

pid = os.fork()
if pid == 0:
    print("Child PID:",os.getpid())
    os._exit(0)
    #子进程在父进程还未退出之前退出,就成为了僵尸进程
else:
    print("parent printcess")
    while True:
        sleep(2)
    #父进程一直在循环,未结束

