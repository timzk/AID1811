#a='hello world'
#b='abcd'
#c='a'
#x=len(a)
#a= '%'+ str(len(a)) + 's')

#print(a % 'hello world')
#print("%20s" % 'abcd')
#print('%20s' % 'a')
#print (str(x))

#i=1
#while i<=10:
#    print("k")
#    i+=1
#else :
#    print(i)

#a=int(input ("输入："))
#num=1
#if a.isdigit():
#while num<=a:
 #  print ("这是第%d行" % num)
  # num +=1

#elif :
    #print("请输入数字" ,end='')
#if i %5 == 0 逢５后进行另外打操作
# begin=int(input("输入开始的整数："))
# end=int(input("输入结束的整数："))
# i=begin
# print_count=0
# while i<end:
#     print( i , end=' ' )
#     print_count+=1
#     if print_count % 5 == 0:
#      print()
#     i+=1  
# print()    
# 
#---------------打印矩形
# a=int(input("输入："))
# i=1
# while i<=a-2:
#    print("#" + " "*(a-2) + "#",flush=True)
#    i+=1

#--------------1-100每个数相加
# d=0 #用来累加的变量
# i=1
# while i<=100:
#    d+= i  #累加
#    i+=1　　#每次加１
# print(d)

#--------------数字矩形输入数字从１开始重复
# chang=int(input("输入："))
# n=1
# while n<=chang:
#     i=1
#     while i<=chang:
#         print(i,end=' ')
#         i+=1
#     print() 
#     n+=1

#------------输入打数字相加，直到输入负数
# sum_t=0
# while True:
#     sum_xt=int(input("请输入整数："))
#     if sum_xt<0:
#         sum_t+=sum_xt
#         break
#     else :
#         sum_t+=sum_xt
# print("你输入了负数，以上总和为"+str(sum_t))

#------------练习1-------
# s=0 #用于存储总和
# n=1
# sign=1 #代表当前的符号
# while n<= 10000:
#     s+=sign/(2*n-1)
#     n+=1
#     sign *=-1
# print("s=",s)
# print("s*4=",s*4)    


#-------练习题２，输入高度和宽度，打印三角形
# kd=int(input("请输入宽度："))
# ＜＜＜＜＜１＞＞＞＞＞   
# ****                        
# ***
# **
# *
# i=0
# while i<kd+i:
#     print("*" *kd )
#     i+=1
#     kd-=1
#  ＜＜＜＜＜２＞＞＞＞＞
#     *
#    **
#   ***
#  ****      
# i=0
# while i<kd+i:
#     print(" "*(kd-1)+"*"+i*"*")
#     i+=1
#     kd-=1
#  ＜＜＜＜＜3＞＞＞＞＞
#  *
#  **
#  ***
#  ****   
# i=0                              i=1    
# while i<kd+i:                    while i<=kd:
#     print("*"*(i+1))               print("*" * i)
#     i+=1                            i+=1       
#     kd-=1                         
#  ＜＜＜＜＜4＞＞＞＞＞
#  ****
#   ***
#    **
#     *   
# i=0
# while i<kd+i:
#     print(" "*(i+1)+"*"*(kd))
#     i+=1
#     kd-=1   

##-------练习题３，用while语句生成Ａ－Ｚ大写和Ａ－Ｚ小写
# a=65
# while True:  
#   if a>90:
#    break
#   else:
#    print(chr(a)+chr(a+32),end=' ')
#    a+=1
# print()





