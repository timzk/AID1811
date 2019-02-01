# day05
# s="ABC DE"
# for ch in s:
#     print("ch------>",ch)
#     print(ord(ch))
# else:
#     print("结束")

#练习：
#  1.任意输入一段字符串,写程序做如下两件事:　　
#l=input("请随意输入:")
# i=0
# print(l[1])
# for n in l:
#    if n ==' ':
#        i+=1
# else:
#     print("空格个数",i)
#-----while实现????
# while i<len(l):
# b=-1
# s=input("输入:")
# while len(s)>=0:
#  for a in s[b]:
#    print(a)
#    b-=1
# index = len(s)-1
# for ch in l[::-1]:　利用切片来实现，-1代表从右向左开始获取索引
#     print (ch)
# for x in range(1,21):
#     print(x,end=' ')
#     print()
#公式x*(x+1)% 11== 8:的０－１００里的数
# for x in range(1,101):
#   if x*(x+1)% 11== 8:
#     print(x)
# y=0
# for x in range(1,100,2):
#     y+=x
# print(y)
#-----------练习－－－－－－－－－
# 1234
# 2345
# 3456
# 4567
# y=int(input("请输入正方形长度:"))
# for x in range(y):
#     j=x+1
#     z = y+j
#     for z in range(j,z):
#        print(z,end=' ',flush=True)  
#     print()

#-----------continue
# for x in range(5):
#     if x==2:
#         continue  #跳过２这个数
#     print(x)    
# for num in range(10):#跳过基数，打印偶数
#     if num %2 == 1:　　#取余
#         continue:
#     print(num)
# y=0    
# for x in range(1,101):
#     if x%2==0 or x%3==0 or x%5==0 or x%7==0: #条件或同时判断
#         continue
#     else:
#         y+=x
#     print(y)
# if 2<3 and 2>3:
#     print("dd")
# else:
#     print("yy")

#------练习--------
# L1=input("请输入文字")
# L2=input("请输入文字")
# L3=input("请输入文字")
# L =[]
# L+=[L1]
# L+=[L2]
# L+=[L3]
# print(L)
#------------------
# i=0
# L=[]
# while True:
#  x=int(input("请输入正整数"))
#  if x>0:
#        L+=[x]
#        i+=x
#  else:
#        print("输入的数字为" + str(L))
#        print("输入的总和为" + str(i))
#        break

#------------练习1-------

#------------99乘法表------------   
# i=0
# for x in range(1,10):
#     for y in range(1,11):
#         if  y<10:
#             print(x,"*",i+1,"=",x*(i+1),sep='',end=' ',flush=True)
#             i+=1
#         else :
#             i=0
#             print()
#             continue    

#-------------练习2------
# 写一个程序,任意输入一个整数,判断这个数是否为素数prime
#     素数(也叫质数),是只能被1和自身整数的正整数
#     如:  2 3 5 7 11 13 17 19 ...
#     提示:
#       用排除法: 当判断x是否为素数时,只要让x分别除以
#        2, 3, 4, 5, 6 ... x-1,只要有一次被整除,则x不是
#        素数,否则x是素数
#方法１---------------------------------------
x = int(input('请输入一个整数: '))
if x < 2:
    print(x, '不是素数')
else:
    # 用一个变量Flag作为标志,很假设x是素数,Flag=True
    # 当不是素数时,把变量值改变False,最后由变量Flag的真假值
    # 来判断x是否为素数
    flag = True  # 先假设x为素数
    for i in range(2, x):  # i为2,3,4,.... x-1
        if x % i == 0:
            # print(x, '不是素数')
            flag = False
            break
    if flag:
        print(x, '是素数')
    else:
        print(x, '不是素数')
#方法２----------------------------------------
x = int(input('请输入一个整数: '))
if x < 2:
    print(x, '不是素数')
else:
    for i in range(2, x):  # i为2,3,4,.... x-1
        if x % i == 0:
            print(x, '不是素数')
            break
    else:
        print(x, '是素数')


#-------------练习3------
# 输入一个整数,此整数代表树干的高度,打印一棵如下形状的圣
#     诞树
# i=int(input("请输入一个整数:"))
# h=0
# for x in range(1,i+1):
#     print (" "*(i-x)+"*"*(h+1),flush=True)
#     h+=2
# for y in range(1,i+1):
#     print(" "*(i-1)+"*")

#------------练习4--------
# 算出 100 ~ 999 范围内的水仙花数(Narcissistic Number)
#     水仙花数是指百位的3次方 + 十位的3次方 + 个位的3次方 等于原
#     数的整数
#     如:
#       153 = 1**3 + 5**3 + 3**3
#     答案:
#       153, 370, ....

# for x in range(100,1000):
# w=567
# w1=w/100
# w2=w/10%10
# w3=w%10
# print(int(w1),int(w2),int(w3))    #5,6,7
for bai in range(1,10):
    for shi in range(0,10):
        for ge in range(0,10):
            #print(bai,shi,ge)
            x= bai *100 +shi *10 +ge
            if x == bai **3+ shi **3+ge **3:
                print(x)

# L=[0,1.2,2,3,4,5,6,7,8]
# #L2=L[1:8:2] #L2 = [1,3,5,7]
# L[:]=[]
# print(L)

# L=[1,2,3,4]
# L2=L
# L=[]
# print(L2)

# L=[1,2,3,4,]
# L2= L
# L[:]=[] #此处与上面不同
# print(L2)