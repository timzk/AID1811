#mydeco1.py
# import math
# import time
# #定义装饰器函数,并装饰myfunc
# #装饰器的原理是替换被装饰函数的变量绑定关系

def mydeco(fn):
    def fx():
        print('++++++++++++')
        fn()
        print('------------')
    return fx #返回的自身
@mydeco  #等同于myfunc = mydeco(myfunc) 
def myfunc():
    print("myfunc被调用")
myfunc = mydeco(myfunc)  #绑定的局部变量fx(),形成闭包
myfunc()
# myfunc()
# myfunc()

# #模拟银行业务需求,用装饰器来扩展新功能
# #银行:存钱,取钱

# def privileged_check(fn): #权限验证功能的装饰器
#     def fx(n,x):
#         print("权限验证中...")
#         fn(n,x)
#     return fx

# def send_message(fx): #实现业务操作完成后发送短消息的功能
#     def fy(n,x):
#         fn(n,x)
#         print('正在发短消息给:',n,'...')
#     return fy

# @privileged_check
# def savemoney(name,x):
#     print("权限验证...检查操作用户的权限")
#     print(name,'存钱',x,'元')

# @send_message
# @privileged_check
# def withdraw(name,x):
#     print(name,'取钱',x,'元')

# savemoney('小王',200)
# savemoney('小赵',400)
# withdraw('小李',500)



#此示例示意函数的缺省参数lst=[]列表会在def语句执行时创建,并一直绑定,不会被释放,因此可能会引起函数不可重入问题
#改进方法

# L = [1,2,3]
# def f(n=0,lst=[]):  #因为缺省参数是一装饰器变数据类型,[]
#     lst.append(n)
#     print(lst)
# f(4,L) #1,2,3,4
# f(5,L) #1,2,3,4,5
# f(100) #100
# f(200) #lst一直存在,所以打印的是,100,200

#改进
# L = [1,2,3]
# def f(n=0,lst=None): 
#     if lst is None:
#         lst = []
#     lst.append(n)源码
#     print(lst)
# f(4,L)
# f(5,L)
# f(100)
# f(200) #200 此时是重新定义的lst，所以打印的是200

# r = float(input("请输入半径"))
# a = math.pi * r**2
# print("面积为",a)

# a2 = float(input("请输入面积"))
# r2 = math.sqrt(a2/math.pi)
# print("半径为",a2)


# s = time.time()
# tm_year = (1990,12,18,0,0,0,0,0,0)
# m=time.mktime(tm_year)
# s_m = s-m
# print("你出生了",s-m,'秒')
# print('出生了',s_m//60/60//24,'天')

# tup_ = time.localtime(m)
# print("你出生那天是星期",tup_[6]+1)

# now_h = time.localtime(s)

# def tim_():
#     fmt = "%02d:%02d:%02d"
#     while True:
#         s = time.time()
#         now_h = time.localtime(s)
#         time.sleep(1)
#         print(fmt % (now_h[3],now_h[4],now_h[5]),sep='',end='\r')
# tim_()        
# m = s-time.mktime(tm_year)
# print("你出生了",m,'秒')
# print('出生了',m/3600//24,'天')

# birth_day=time.localtime(m)
# print('你出生那天是星期',birth_day[6])

# def run_alarm(hour,minute):
#     import time
#     while True:
#         t = time.localtime()
#         print("%02d:%02d:%02d" % t[3:6],end='\r')
#         if t[3:5] == (hour,minute):
#             return
#         time.sleep(1)

# sleep_houre = int(input("请设置闹钟\n请设置时钟:"))
# sleep_sceond = int(input("n请设置分钟:"))
# run_alarm(sleep_houre,sleep_sceond)
# print('时间到,程序结束')

# 3. 编写函数fun 基功能是计算下列多项式的和
#     Sn = 1 + 1/1! + 1/2! + 1/3! + .... + 1/n!
#     (建议用数学模块中的factorial)
# #       求当n得20时 Sn的值
# print(fun(20))  # 2.718281828...
#方法1
# def fun(x):
#     s= 1
#     for i in range(1,x+1):
#         s = 1/math.factorial(i)+s
#     return s
# print(fun(20))

#方法2
# for num in range(10):
#     if(num % 2 == 1):
#         continue
# print(num)
# L = [1, 2, 3]
# def func(a):
#     a = [4, 5, 6]
# func(L)
# print(L)
# class A:
#     v =100
#     def __init__(self):
#         self.v = 200
# a1 = A()
# a2 = A()
# del a2.v
# print(a1)