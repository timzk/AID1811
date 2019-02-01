from multiprocessing import Process,Array
import time
 
#创建共享内存
# shm = Array('i',[1,2,3,4]) #开辟共享内存空间,存入整数型的列表
# shm = Array('i',4)#表示开辟共享内存空间,开辟5个int空间,初始化为0
shm = Array('c',b'hello') #存入字符串
def fun():
    for i in shm:
        print(i)
    shm[0] = b'c' #修改第一项内容
p = Process(target = fun)
p.start()
p.join()

for i in shm:
    print(i)
#可以通过value属性,直接全部打印出来
print(shm.value)