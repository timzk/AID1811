from test import * 
import multiprocessing as mp
import time 

def io():
    write()
    read()

jobs = []
t = time.time()
for i in range(10):
    p  = mp.Process(target=count,args=(1,1))
    
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
print("Thread io:",time.time()-t)