#模拟filter高阶函数
#方法1----------------------------------
# def myfilter(func,iterable):
#     it  = iter(iterable) #先拿到可迭代对象的迭代器
#     while True:
#         try:
#             x = next(it)
#             if func(x):
#                 yield x
#         except StopIteration:
#             return
# for i in myfilter(lambda x%2 ==1,range(10)):
#     print(i)
# #方法2-----------------------------
# def myfilter(func,iterable):
#     for x in iterable:
#         if func(x):
#             yield x

# for i in myfilter(lambda x%2 ==1,range(10)):
#     print(i)

L = [2,3,5,7]
A = [x*10 for x in L]
it = iter(A)
print(next(it))  #20
L[1] = 333
print(next(it))  #30

# gen = (x**2 for x in range(1,5))
# it = iter(gen)
# next(it) #1  等同于next(gen)
# next(it) #4
# next(it) #9
# next(it) #16
# next(it)  #StopIteration
# print(next(gen))

# L = [2,3,5,7]
# A = (x*10 for x in L)
# it = iter(A)
# print(next(it)) #20
# L[1] = 333
# print(next(it)) #3330