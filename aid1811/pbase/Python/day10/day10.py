# def f1():
#     print("f1")
# def f2():
#     print("f2")
# f1,f2 = f2,f1
# f1()

# def f1():
#     print("f1函数被调用")
# def f2():
#     print("f2函数被调用")
# def fx(fn): #<function f1 at 0x7f5c1282ef28>
#     print(fn)#"f1函数被调用"
#     fn()
# fx(f1)
# fx(print) #可以的,打印的是print的内建函数地址

# def myfun(fn):
#     L=[1,3,5,7,9]
#     return fn(L)
# print(myfun(max))
# print(myfun(min))
# print(myfun(sum))
#此示例示意函数可以返回另一个函数的引用关系
# def get_function():
#     s = input("请输入你要做的操作")
#     if s == '求最大':  
#         return max    #如果成立返回的max,f绑定max，即max(L),返回10
#     elif s == '求最小':
#         return min   #如果成立返回的max,f绑定min，即min(L),返回2
#     elif s == '求和':
#         return sum   #如果成立返回的sum,f绑定sum，即sum(L),返回25
#     else :
#         return print
# L = [2,4,6,8,10]
# f = get_function() #f绑定函数get_function()函数的返回值
# print(f(L))
#-----------------------加减乘除运算
# def myadd(x,y):
#     return x + y
# def mysub(x,y):
#     return x -y
# def mymul(x,y):
#     return x * y
# def get_func(op):
#     if op == '+' or op == '加':
#         return myadd
#     elif op == '-' or op =='减':
#         return mysub
#     elif op == '*' or op =='乘':
#         return mymul
#     else :
#         print("请输入合法的")
# def main():
#     while True:
#         s = input("请输入计算公式:")
#         L = s.split(' ') #L=['10',加,'20']
#         a = int(L[0])
#         b = int(L[2])
#         fn = get_func(L[1])
#         print("结果是:",fn(a,b))
# main()
#-----------------------此示例示意函数嵌套定义
# def fn_outer():
#     print("fn_outer被调用")
#         def fn_inner(): #此函数是局部变量，在fn_outer()里面没有调用的时候不会执行此函数
#             print("fn_inner被调用")
#         print("fn_outer调用结束")
# fn_outer()
# print("程序结束")

# count = 0
# def hello(name):
#     print('你好',name)
#     global count #改变count的全局变量，然后使用
#     count += 1
# hello('小张')
# while True:
#     s = input('请输入姓名:')
#     if not s:
#         break
#     hello(s)
# print("hello函数调用的次数是",count)

#此表达式创建一个函数,判断n这个数的2次方+1能否被5整除,如果能整除返回True,否则返回False
# fx = lambda n:(n**2+1)%5 == 0
# print(fx(3))
#此函数返回两个参数的最大值
# mymax = lambda x,y:max(x,y)
# print(mymax(300,200))
# print(mymax('ABC','123'))
# s = '''
# a = 100
# print(a)
# '''
# exec(s) #打印的是100
# 1. 看懂下面的程序在做什么? 高阶函数
# def fx(f, x, y):
#     print(f(x, y),flush = True)
# fx((lambda a, b: a + b), 100, 200)
# fx((lambda a, b: a ** b), 3, 4)

#     # 程序直到此处时有几个全局变量?
#   2. 写一个函数 mysum(x) 来计算:
#      1 + 2 + 3 + 4 + .... + x 的和,并返回
#      (要求: 不允许调用sum函数)
#      如:
#         print(mysum(100))  # 5050
# 方法1:
# def mysum(x):
#     sum1 = 0
#     for i in range(1,x+1):
#         sum1 +=i
#     return sum1
# print(mysum(100))
#3. 写一个函数myfac(n) 来计算n!(n的阶乘)
#      n! = 1*2*3*4*...*n 
#      如:
# def myfac(n):
#     fac_ = 1
#     for i in range(1,n+1):
#         fac_ *= i
#     return fac_
# print(myfac(7))
#         print(myfac(5))  # 120
#递归方法

#4. 写一个函数计算 1 + 2**2 + 3**3 + ... + n**n的和
#     (注: n给个小点的数)
# def m_sum(n):
#     m = 0
#     for i in range(1,n+1):
#         m = i**i + m 
#     return m
# print(m_sum(4))
#-------函数式编程---------
# def fun(n):
#     return sum(map(lambda x:x**x,range(1,n+1)))
# print(fun(3))

#   5. 实现有界面的学生信息管理程序
#     选择菜单如下:
#       +-----------------------------+
#       | 1) 添加学生信息               |
#       | 2) 显示学生信息               |
#       | 3) 删除学生信息               |
#       | 4) 修改学生成绩               |
#       | q) 退出                      |
#       +-----------------------------+
#       请选择: 1
#     学生信息和存储方法与原程序相同: 用列表里包含来存信息
#     要求: 每个功能写一个函数与之相对应
#---------------------------------------------------
# L = []# 创建一个列表,准备放字典
# def input_student():
#     x = 0
#     while True:
#         n = input("请输入姓名: ")
#         if n == '':  # if not n:
#             break
#         a = int(input("请输入年龄: "))
#         s = int(input("请输入成绩: "))
#         nub = input("请输入编号: ")
#         d = {}  # 每次创建一个
#         d['name'] = n
#         d['age'] = a
#         d['score'] = s
#         d['nub'] = nub
#         for i in L:
#             if i['nub'] == nub:
#                 print("编号重复,请重新输入")
#                 x += 1
#         if x == 0:
#             L.append(d)
#     return L

# def output_student(L):
#     print("+---------------+----------+----------+----------+")
#     print("|    姓名       |   年龄   |   成绩   |   编号   |")
#     print("+---------------+----------+----------+----------+")   
#     print("+---------------+----------+----------+----------+") 
#     for d in L:
#         sn = d['name']
#         sa = str(d['age'])  # 转为字符串,容易居中
#         ss = str(d['score'])
#         snub = d['nub']
#         print("|%s|%s|%s|%s|" % (sn.center(14), 
#                             sa.center(10),
#                             ss.center(10),snub.center(10)))
#     print("+---------------+----------+----------+----------+")

# def del_student(s_nub):
#     x = 0
#     y = 0
#     for i in L:
#         if i['nub'] == s_nub:
#             L.pop(x)
#             print("删除成功")
#             y += 1
#         else :
#             x+=1
#     if y == 0:        
#         print("没有你输入的学生信息!")
 
# def change_student(s_chg):
#     x = 0
#     for i in L:
#         if i['nub'] == s_chg:
#             sa = input("请输入要修改的年龄:")
#             ss = input("请输入要修改的成绩:")
#             i['age'] = sa
#             i['score'] = ss
#             print("修改成功")
#             x += 1
#     if x == 0:
#         print("没有找到你学生信息")
# def output_student_by_score_desc():
#     def L_()
#         return i['score']
#     s = filter(L,key = L_)


# def main():
#     while True:
#         print('1) 添加')
#         print('2) 显示 ')
#         print('3) 删除 ')
#         print('4) 修改 ')
#         print('按学生成绩高~低显示学生信息')
#         print('按学生成绩低~高显示学生信息')
#         print('按学生年龄高~低显示学生信息')
#         print('按学生年龄低~高显示学生信息')
#         print('q) 退出')
#         s = input("请选择: ")
#         if s == '1':
#             input_student()
#         elif s == '2':
#             # 显示学生信息:
#             output_student(L)
#         elif s == '3':
#             #删除学生信息
#             s_nub = input("请输入要删除的学生编号:")
#             del_student(s_nub)    
#         elif s == '4':
#             #修改学生成绩
#             s_chg = input("请输入要修改的学生编号:")
#             change_student(s_chg)
#         elif s == '5':
#             output_student_by_score_desc()  # 分数降序
#         elif s == '6':
#             output_student_by_score_asc()  # 分数升序
#         elif s == '7':
#             output_student_by_age_desc()  # 年龄降序
#         elif s == '8':
#             output_student_by_age_asc()  # 年龄升序    
#         elif s == 'q':
#             break
# main()


#   1.  有一只小猴子,摘了很多桃.
#      第一天吃了全部桃子的一半,感觉不饱又吃了一个
#      第二天吃了剩下的一半,感觉不饱又吃了一个
#      ... 以此类推
#      到第十天,发现只剩一个了
#     请问一天摘了多少桃子?
# day10 = 1
# day09 = (day10 + 1) * 2
# day08 = (day09 + 1) * 2
# day07 = (day08 + 1) * 2
# peach = 1  # 第十天的桃子数
# for day in range(9, 0, -1):
#     peach = (peach + 1) * 2  # 算出当天的桃子数
#     print("第", day, '天有', peach, '个桃')
#原理,第９天是第十天的两倍加上一个，第８天是第９天的两倍加上一个

#   3. 改写之前的学生信息管理程序,添加如下四个功能:
#       | 5)  按学生成绩高~低显示学生信息 |
#       | 6)  按学生成绩低~高显示学生信息 |
#       | 7)  按学生年龄高~低显示学生信息 |
#       | 8)  按学生年龄低~高显示学生信息 |



# def input_student():
#     L = []   # 创建一个列表,准备放字典
#     while True:
#         n = input("请输入姓名: ")
#         if n == '':  # if not n:
#             break
#         a = int(input("请输入年龄: "))
#         s = int(input("请输入成绩: "))
#         d = {}  # 每次创建一个
#         d['name'] = n
#         d['age'] = a
#         d['score'] = s
#         L.append(d)
#     return L

# def output_student(L):
#     print("+---------------+----------+----------+")
#     print("|    姓名       |   年龄   |   成绩   |")
#     print("+---------------+----------+----------+")
#     for d in L:
#         sn = d['name']
#         sa = str(d['age'])  # 转为字符串,容易居中
#         ss = str(d['score'])
#         print("|%s|%s|%s|" % (sn.center(15), 
#                             sa.center(10),
#                             ss.center(10)))
#     print("+---------------+----------+----------+")

# def remove_student(L):
#     name = input("请输入要删除学生的姓名: ")
#     # 方法1
#     # for d in L:
#     #     if d['name'] == name:
#     #         L.remove(d)
#     #         print("删除成功")
#     #         return
#     for i in range(len(L)):  # i代表列表的索引
#         d = L[i]
#         if d['name'] == name:
#             del L[i]
#             print("删除成功")
#             return
#     print("删除失败")

# def modify_student(L):
#     name = input("请输入要修改成绩的学生姓名: ")
#     for d in L:
#         if d['name'] == name:
#             score = int(input("请输入学生成绩:"))
#             d['score'] = score
#             print("修改成功!")
#             return
#     print("修改失败！")

# def output_student_by_score_desc(L):
#     def get_score(d):
#         return d['score']
#     L2 = sorted(L, key=get_score, reverse=True)
#     output_student(L2)

# def output_student_by_score_asc(L):
#     L2 = sorted(L, key=lambda d: d['score'])
#     output_student(L2)

# def output_student_by_age_desc(L):
#     L2 = sorted(L, key=lambda d: d['age'], reverse=True)
#     output_student(L2)

# def output_student_by_age_asc(L):
#     L2 = sorted(L, key=lambda d: d['age'])
#     output_student(L2)

# def show_menu():
#     print("+---------------------------------+")
#     print("| 1)  添加学生信息                |")
#     print("| 2)  显示学生信息                |")
#     print("| 3)  删除学生信息                |")
#     print("| 4)  修改学生成绩                |")
#     print("| 5)  按学生成绩高~低显示学生信息 |")
#     print("| 6)  按学生成绩低~高显示学生信息 |")
#     print("| 7)  按学生年龄高~低显示学生信息 |")
#     print("| 8)  按学生年龄低~高显示学生信息 |")
#     print("| q)  退出                        |")
#     print("+---------------------------------+")


# def main():
#     infos = [] 
#     while True:
#         show_menu()
#         s = input("请选择: ")
#         if s == '1':
#             infos += input_student()
#         elif s == '2':
#             # 显示学生信息:
#             output_student(infos)
#         elif s == '3':
#             remove_student(infos)
#         elif s == '4':
#             modify_student(infos)
#         elif s == '5':
#             output_student_by_score_desc(infos)  # 降序
#         elif s == '6':
#             output_student_by_score_asc(infos)  # 升序
#         elif s == '7':
#             output_student_by_age_desc(infos)  # 降序
#         elif s == '8':
#             output_student_by_age_asc(infos)  # 升序
#         elif s == 'q':
#             break

# main()

# s1 = "1+2*3"  #s1是符合python语法规则的字符串表达式
# s2 = "x+y"
# v = eval(s1) 
# print(v)#7 s1是符合python语法规则的字符串表达式
# #v2 = eval(s2,{'x':10,'y':20}) #30,x,y都是全局变量
# #v2 = eval(s2,{'x':10,'y':20},{'y':2}) #12 x为全局变量,y为局部变量,首先使用局部变量


# v2 = eval(s2,{'x':10,'y':20}) #30,x,y都是全局变量
# # v2 = eval(s2,{'x':10,'y':20},{'y':2}) #12 x为全局变量,y为局部变量,首先使用局部变量
# print(v2)
# i = sum(map(lambda x:x**2,range(1,10)))
# for x in map(lambda x:x**2,range(1,10)):
#     print(x)
# print(i)
# L = list(filter(lambda x:x%2 ==0,range(10)))
# print(L)


# def fun(n):
#     return sum(map(lambda x:x**x,range(1,n+1)))
# print(fun(3))

def eval_test():
    l = '[1,2,3,4,[5,6,7,8,9]]'
    d = "{'a':123,'b':456,'c':789}"
    t = '([1,3,5],[5,6,7,8,9],[123,456,789])'

    print("-------------------------------------")
    print(type(l),type(eval(l)))
    print(type(d),type(eval(d)))
    print(type(t),type(eval(t)))
eval_test()

def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n-1)

print(func(5))