# jl = {'曹操','刘备','孙权'}
# jsy = {'曹操','孙权','张飞','关羽'}

# print("即使经理也是技术员的",jl & jsy)  #即使经理也是技术员的

# print("是技术,但不是经理",jsy - jl) #利用补集，是技术,但不是经理

# print("是经理但不是技术",jl - jsy) #利用补集，是经理但不是技术

# if '张飞' in jl:
#     print("张飞是经理")
# print("张飞不是经理")

# print("身兼一职的人",jl ^ jsy )

# print("经理和技术共有多少人",len(jl | jsy))

# def say_hello()：
#     print("hello world")

# def mymax(a,b): #形参列表
#     if a>b:
#         print("最大值",a)
#     else:
#         print("最大值",b)

# mymax(100,200) #最大值是:200
# mymax("ABC","abc")　#最大值abc

# def myadd(x,y):
#     print(x+y)

# myadd(100,200)
# myadd("ABC","123") 

# def print_even(n):
#     for x in range(0,n,2):
#         print(x)

# print_even(100)

# def say_hello2():
#     print("hello")x,y):
#     print(x+y)

# myadd(100,200)
# myadd("ABC","123") 

# def print_even(n):
#     for x in range(0,n,2):
#         print(x)

# print_even(100)

# def say_hello2():
#     print("hello")
#     return  #不会执行return后面的语句
#     print("abc")因为前面ab已经确定来是关键字传参，所以后面必须也使用关键字传参(位置参数跟随了关键字传参)
[2,3,6,7,1]
# v=say_hello2()
# print("v=" ,v)  因为前面ab已经确定来是关键字传参，所以后面必须也使用关键字传参(位置参数跟随了关键字传参)
#     return  #不会执行return后面的语句
#     print("abc")

# v=say_hello2()
# print("v=" ,v)   

# def mymax(a,b):
#    return  max(a,b)
# print(mymax(100,200))
    
# def myadd (x,y):
#     return x + y

# a = int(input("请输入第一个数:"))
# b = int(input("请输入第二个数:"))
# print(a,'+',b,'的和是',myadd(a,b))

# L = []
# def input_number(x):
#     for i in x:
#          L.append(x)
        

# def input_number():
#     lst = []
#     while True:
#         x = int(input("请输入整数(小于零结束): "))
#         if x < 0:
#             break
#         lst.append(x)  # lst += [x]
#     return lst
# L = input_number()
# print("用户输入的最大值是:", max(L))
# print("用户输入的最小值是:", min(L))
# print("用户输入的全部数的和是:", sum(L))

# 1. 写一个函数 get_chinese_char_count ,此函数实现的功能是
#     给定一个字符串,返回这个字符串中中文字符的个数
#       def get_chinese_char_count(s):
#           ...  # 此处自己实现

#       s = input('请输入中英文字混合的字符串:')
#       print("您输入的中文字符的个数是:",
#             get_chinese_char_count(s))   
#     注: 中文字符的编码范围是: 0x4E00 ~ 0x9FA5(包含)
# def get_chinese_char_count(s):
#     l=0
#     lst = []
#     for h in s:
#         lst.append(h)
#     for x in lst:
#         if 0x4E00<=ord(x)<=0x9FA5:
#             l+=1
#     return l
# s = input('请输入中英文字混合的字符串:')
# print("你输入的中文字符个数是:",get_chinese_char_count(s))

# 2. 定义两个函数:
#      sum3(a, b, c)   用于返回三个数的和
#      pow3(x)         用于返回x的三次方
#     用以下函数计算:
#        1)  计算1的立方 + 2的立方 + 3的立方的和
#        2)  计算1+2+3的和的立方
#        即:1**3+2**3+3**3 和 (1+2+3) ** 3
# def sum3(a,b,c):
#     x=a**3
#     y=b**3
#     z=c**3
#     return x+y+z
# print("1,2,3立方和",sum3(1,2,3))

# def pow3(x):
#     x=1
#     y=2
#     z=3
#     x = 
    
# print("1+2+3的立方",)


# 3. 编写函数fun ,其功能是计算并返回下列多项式的值
#     Sn = 1 + 1/2 + 1/3 + 1/4 + .... + 1/n
#       def fun(n):
#           ...
#       print(fun(2))   # 1.5
#       print(fun(3))   # 1.8333333333333
#       print(fun(10))  # ????
def fun(n):
    x = 0
    x1=0
    for y in range(1,n+1):
        x = 1/y
        x1+=x
    return x1
print(fun(3))

def fun(n):
    sn = 0
    for d in range(1,n+1) #d代表分母
        sn +=1/d
    return sn
print(fun(2))