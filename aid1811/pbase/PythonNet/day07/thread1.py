#线程示例
import threading
from time import sleep
import os

a = 1
# 线程函数
def music():
    global a
    print("a=",a)
    a = 10000
    for i in range(5):
        sleep(2)
        print("播放好嗨哟")

# 创建线程对象
t = threading.Thread(target=music)
t.start()

#主线程运行
for i in range(5):
    sleep(2)
    print("播放听说",os.getpid())
t.join()

print("main a:",a)