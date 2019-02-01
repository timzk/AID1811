# #位置传参------------------------------------
# def myfun1(a,b,c):
#     """这是一个有三个参数的函数"""
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# myfun1(1,2,3)
# #序列传参-----------------------------------
# def myfun1(a,b,c):
#     """这是一个有三个参数的函数"""
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# L = [1,2,3]
# myfun1(*L)#等同于myfun1(L[0],L[1],L[2]) 拆解序列
# T=(100,200,300)
# myfun1(*T)
# s="ABC"
# myfun1(*s)
# #关键字传参-----------------------------------
# def myfun1(a,#位置传参------------------------------------
# def myfun1(a,b,c):
#     """这是一个有三个参数的函数"""
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# myfun1(1,2,3)
# #序列传参-----------------------------------
# def myfun1(a,b,c):
#     """这是一个有三个参数的函数"""
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# L = [1,2,3]
# myfun1(*L)#等同于myfun1(L[0],L[1],L[2]) 拆解序列
# T=(100,200,300)
# myfun1(*T)
# s="ABC"
# myfun1(*s)
# #关键字传参-----------------------------------
# def myfun1(a,b,c):
#     """这是一个有三个参数的函数"""
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# myfun1(c=3,b=2,a=1) #b,c):
#     """这是一个有三个参数的函数"""
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# myfun1(c=3,b=2,a=1) #关键字传参,不分先后顺序,只按照关键字来一一对应
#字典关键字传参--------------------------------
# def myfun1(a,b,c):
#     """这是一个有三个参数的函数"""
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# d = {'c':33,'b':22,'a':11}
# myfun1(c=d['c'],b=d['b'],c=d['c'])
# myfun1(**d)  #字典和形参必须匹配

# a= [1,2,3]
# b=200
# def f3(x,y):
#     x= x+[y] #改变的是变量不(filter(lambda x:x%2 ==0,range(10)))
# print(L)对象,x属于局部变量不能改变外部对象

# f3(a,b)
# print(a)
# print(b)

# def county(x,y='东京'):
#     print(x,y)
# print(county(3))


# def myadd(a=0,b=0,c=0,d=0):
#     return a+b+c+d
# print(myadd(10,20))
# print(myadd(100,200,300))
# print(myadd(1,2,3,4))

# def mysum(*args):
    
#     return sum(args)
# print(mysum(1,2))
# print(mysum(1,2,3,4))

# def mymax(a,*args):
    # if a>b:
    #     return a
    # elif b>a:
    #     return b
    # elif a> args:
    #     return a
    # elif b>args:
    #     return b(filter(lambda x:x%2 ==0,range(10)))
# print(L)
    # else :
    #     x = 0
    #     for i in(filter(lambda x:x%2 ==0,range(10)))
# print(L)(args)):
    #         if a(filter(lambda x:x%2 ==0,range(10)))
# print(L)s[i+1]:
    #             (filter(lambda x:x%2 ==0,range(10)))
# print(L)x]
    #             (filter(lambda x:x%2 ==0,range(10)))
# print(L)
    #         else(filter(lambda x:x%2 ==0,range(10)))
# print(L)
    #             (filter(lambda x:x%2 ==0,range(10)))
# print(L)i+1]
    #             x += 1 
    
# print(mymax([100,200,2,90,250]))

# def mymax(*args):
#     if len(args)==1:
#         iterable = args[0] #取元组的所有值存储到iterable
#         zuida = iterable[0]
#         for x in iterable[0]:
#             if x >zuida:
#                 return x
#     elif len(args)>1:
#         zuida = args[0]
#         for x in args:
#             if x >zuida:
#                 zuida = x
#         return zuida
# print(mymax(2,3,6,7,1))


# x = int(input('请输入一个整数: '))
# if x < 2:
#     print(x, '不是素数')
# else:
#     for i in range(2, x):  # i为2,3,4,.... x-1
#         if x % i == 0:
#             print(x, '不是素数')
#             break
#     else:
#         print(x, '是素数')
# L = []
# def isprime(x):
#     if x < 2:   
#         pass
#     else:
#         for i in range(2, x):
#             if x % i == 0:
#                 continue
#             else:
#                 L.append(x)
#                 break
# L = []
# def prime_m2n(m,n): 
#     for y in range(m,n):
#         i=0
#         for x in range(1,y+1): 
#             if y % x == 0: 
#                 i+=1
#         if i == 2 :
#             L.append(x)
# print(L)


# 1. 写一个函数 isprime(x) 判断x是否是素数,如果为素数则返回
#     True, 否则返回False
# x = int(input('请输入一个整数: '))
# if x < 2:
#     print(x, '不是素数')
# else:
#     for i in range(2, x):  # i为2,3,4,.... x-1
#         if x % i == 0:
#             print(x, '不是素数')
#             break
#     else:
#         print(x, '是素数')

# 2. 写一个函数 prime_m2n(m, n) 返回从m开始,到n结束范围内
#     的素数(不包含n), 返回这些素数的列表,并打印
#     如:
#       L = prime_m2n(10, 20)
#       print(L)  # [11, 13, 17, 19]
# L = []
# def prime_m2n(m,n): 
#     for y in range(m,n):
#         i=0
#         for x in range(1,y+1): 
#             if y % x == 0: 
#                 i+=1
#         if i == 2 :
#             L.append(x)
# prime_m2n(2,10)
# print(L)

# 3. 写一个函数primes(n), 返回指定范围内n(不包含n)的全部素
#      数的列表,并打印这些素数的列表
#       L = primes(10)
#       print(L)  # [2, 3, 5, 7]
#       1) 打印100 以内的全部素数
#       2) 打印 100 ~ 200之间全部素数的和
# L = []
# def prime_m2n(m,n): 
#     for y in range(m,n):
#         i=0
#         for x in range(1,y+1): 
#             if y % x == 0: 
#                 i+=1
#         if i == 2 :
#             L.append(x)
# prime_m2n(2,10)
# print(sum(L))

# 4. 改写之前的学生信息管理程序,将程序 改为两个函数:
#       def input_student():
#           ....    # 此函数用于获取学生的信息,形成包含有字典的列表
#           然后返回此列表
#       def output_student(L):
#           ....   # 此函数以列格的形式打印学生信息的列表

#       测试(实现与之前相同的功能):
#       infos = input_student()
#       print(infos)
#       output_student(infos)
add_words={}
while True:
    print("1) 添加单词：")
    print("2) 删除单词：")
    print("3) 查找单词：")
    print("4) 退出：")
    x=int(input("请输入:"))
    if x ==1:
        while True:
            s_d =input("请输入单词:")
            if s_d == '':
                print("-------你输入了回车，请继续选择想要功能-------")
                break
            s_j = input("请输入解释:")
            add_words[s_d]=s_j
    if x ==2:
        while True:
            s_s = input("请输入要删除的单词:")
            if s_s =='':
                print("-------你输入了回车，请继续选择想要功能-------")
                break
            else: 
                if s_s in add_words:
                    pop_l=add_words.pop(s_s)
                    print("删除的单词为:",s_s,"解释为:",s_j)
                else:
                    print("-----------不好意思没有你输入的单词-----------")
    if x ==3:
        while   True:
            s_c = input("请输入要查找的单词:")
            if s_c=='':
                print("-------你输入了回车，请继续选择想要功能-------")
                break
            else:
                if s_c in add_words:
                    print("你输入的单词解释为:",add_words.get(s_c,"nn"))
                else:
                    print("-----------不好意思没有你输入的单词-----------")
    if x ==4:
        print("谢谢使用!")
        break