# #此示例示意用生成器函数生成一系列的整数
# def myinteger(n): #生成器函数
#     i = 0 
#     while i<n:
#         yield i 
#         i += 1

# for x in myinteger(10):
#     print(x)

# it =iter(myinteger(20))
# print(next(it)) #0
# print(next(it)) #1

# L = [x for x in myinteger(20) if x %2 ==1]
# print(L)

def myeven(start,stop):
    i = start
    while i<stop:
        if i% 2 == 1:
            yield i
        i+=1

even = list(myeven(10,20))
print(even) #[10,12,14,16,18]
for x in myeven(20,30):
    print(x)   #打印22,24,26,28