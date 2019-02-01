from test import * 
import multiprocessing as mp
import time 

def io():
    write()
    read()

jobs = []
t = time.time()
for i in range(10):
    p = mp.Process(target=io)
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
print("Process io:",time.time() - t)