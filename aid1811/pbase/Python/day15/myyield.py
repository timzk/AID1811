# #此示例示意生成器函数的创建和调用

def myyield():
    yield 2 #一旦使用yield便是一个生成器函数
    print("即将生成3")
    yield 3
    yield 5
    yield 7  
    print("生成器生成结果")

gen = myyield() #调用生成器函数生成一个生成器
print(gen)#generator

it = iter(gen) #从生成器中获取一个迭代器
print(next(it)) #向迭代器要数据,此时生成器函数才会执行一步 ,打印2
print(next(it))
# def myyield():
#     yield 2 #一旦使用yield便是一个生成器函数
#     yield 3
#     yield 5
#     yield 7  
#     print("生成器生成结束")

# gen = myyield() #调用生成器函数生成一个生成器
# for x in gen:#generator
#     print(x)
