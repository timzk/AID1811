# 1.已知有列表:
#   L = [2,3,5,7]
# L = [2,3,5,7]
# #-----------生成器----------------------
# def x(Y):
#     for i in Y:
#         yield i**2+1
#     return 
# for i in x(L):
#     print(i)

# #---------生成器表达式-------------------------
# gen = (x ** 2+1 for x in L)
# for x in gen :
#     print(x)

# #-----------存到列表里面-------------
# def x(Y):
#     for i in Y:
#         yield i**2+1
#     return 
# even = list(x(L))
# print(even)

# 1. 实现一个python2下的xrange([start], stop, [step])
#     生成器函数,此生成函数按range规则来生成一系列整数
#     要求:
#       myxrange功能与range功能完全相同
#       不允许调用range函数和列表
#   用自己写的myxrange结果生成器表达式求 1~10以内所有奇数的
#     平方和
#   如:
#     def myxrange(start, stop=None, step=None):
#          ....以下自己实现
#     求:1 ** 2 + 3 ** 2 + 5 **2 + ...  9 ** 2
#此示例是一个从start开始到stop结束的基数的平方和函数,步数也是按照基数来递增的
# def myxrange(start,stop = None,step = 1):
#     i = []
#     x = start
#     sum1 = 0
#     sum2 = 0
#     if stop == None and start > 0 and step == 1:
#         while x:
#             if x % 2 !=0:
#                 i.append(x)
#             x-=1
#         for _ in i:
#             sum1 = _**2
#             sum2 += sum1
#         return sum2
#     elif step ==2 or step ==1 and stop !=None:
#         while x <= stop:
#             if x % 2 !=0:
#                i.append(x)
#             x+=1
#         for _ in i:
#             sum1 = _**2
#             sum2 += sum1
#         return sum2
#     elif start < stop and step > 0:
#         while x <= stop:
#             if x % 2 !=0:
#                 i.append(x)
#             x+=1
#         h = 1
#         nn = []
#         for _ in i:
#             if _ == i[0]:
#                 nn.append(_)
#             try:
#                 nn.append(i[step*h])
#                 h+=1
#             except IndexError:
#                 for hj in nn:
#                     sum2 +=hj**2
#                 return sum2
#     else:
#         pass
# print(myxrange(-5,21,5))


numbers = [10086,10000,10010,95588]
names = ['中国移动','中国电信','中国联通']
# for t in zip(numbers,names):
#     print(t)

for index,name in enumerate(names):
    print(index,name)
# if name =='中国联通'
#    del names[index]
#    break
# s = input("请输入:")
# b = s.encode()
# print("字符串转换为字节串=",b)
# print('字符串的长度为:',len(s),'字节串的长度为:',len(b))
# s2 = b.decode()
# print('字节串',b,'转为字符串是',s2)