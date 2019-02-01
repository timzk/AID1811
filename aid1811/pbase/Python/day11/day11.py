# for x in map(pow,range(1,10),(2)):
#     # i = 0
#     # i += int(x)
#     print(x)
# i = 0
# for x in map(pow,range(9,0,-1),range(1,10)):
#     i += x
# print(i)

# i = sum(map(lambda x:x**2,range(1,10))):
# print(sum(map(lambda x:x**2,range(1,10))))
# L = list(filter(lambda x:x%2 ==0,range(10)))
# print(L)

# s = 0
# def y(i):
#     for x in 
#     i%2 ==0
#     s+=1
# if s <=2:
#     return i
# L = list(filter(lambda x:x%2 ==0,range(101)))
# print(L)
#此示例示意L列表中的元组的第二个数的从大到小排序
# L = [(1,5),(3,9),(4,1),(3,6),(5,3)]
# def second_value(t):
#     return t[1] 
# L2 = sorted(L,key = second_value,reverse=True)　#把L里面的每个元组一次传给函数sencond_value，然后在函数sencond_value
#                                                  #里把每个元组的第二个元素拿到,再用sorted来排序
# print(L2)
# def fx(n):
#     print("递归进入第",n,'层')
#     if n==3:
#         return
#     fx(n+1)
#     print("递归退出第",n,'层')
# fx(1)
# print('程序结束')
#求100以内的每个数的和
# def mysum(n):
#     if n ==1:
#         return 1
#     return n+mysum(n-1)
# print(mysum(100))
# 1. 已知有列表：
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数 print_list(lst) 打印出所有的数字
#        如:
#          print_list(L)  # 打印 3 5 8 10 13 14
#     2) 写一个函数 sum_list(lst) 返回这个列表中所有数字的和
#        如:
#          print(sum_list(L))  # 106
#     注:
#       type(x) 函数可以返回一个对象的类型
#       如: type(20) is int  # True
#           type([1, 2, 3]) is list  # True
# L = [[3,5,8],10,[[13,14],15,18],20]
# def second_value(L):
#     for t in L:
#         if type(t) is int:
#             L3.append(t)
#         else:
#             for i in t:
#                 if type(i) is int:
#                     L3.append(i)
#                 else:
#                     for x in i:
#                         if type(x) is int:
#                             L3.append(x)
# L3 = [] 
# second_value(L)
# print(L3)
#-----------用递归------------

# L = [[3,5,8],10,[[13,14],15,18],20]
# L1 = []
# def second_value_value(L):
#     for x in L: #x为当前for循环的每个元素
#         if type(x) is int:
#             L1.append(x)
#         else:
#             second_value_value(x)#如果不满足，就继续调用此函数本身,然后把当前参数作为值传入函数

# print(second_value_value(L),sum(L1))
#2.  写程序求出1~20的阶乘的和
#      即:  1!+2!+3!+....+20!


def myfac(x):
    if x == 0:
        return 1
    s = x * myfac(x-1)
    return s

print(sum(map(myfac,range(1,21))))

















