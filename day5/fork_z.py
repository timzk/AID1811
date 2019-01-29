import os 
from time import sleep 

pid = os.fork()

if pid == 0:
    print("Child PID:",os.getpid())
    os._exit(0)
else:
    print("parent process")
    while True:
        sleep(2)