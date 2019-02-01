from multiprocessing import Pool, Queue
import time

# def fun(n):
#     time.sleep(1)
#     return n**2

# pool = Pool()
# #使用map将事件放入进程池

# r = pool.map(fun,[1,2,3,4,5])
# pool.close()
# pool.join()
# print(r)

q = Queue()
q.put(2)
print(q.empty())
print(q.get())
