#-----练习
# L=[3,5]
#索引和切片操作，将原列表改为:

# L[0:0]=[1,2]
# L[3:3]=[4]
# L[6:6]=[6]
# print(L)

# 用反转后的新列表的内容替换掉原列表的全部内容　L[]=L[::-1]
# 删除最后一个 L[-1:]＝[]
# L[::]=[]
# L[0:7]=[6,5,4,3,2]
# print(L)


# L=[]

# while True :
#     x = int(input("shuru"))
#         if x <0:
#             break
#         L +=[x] #追加到列表
# for x in L:
#     print(x)
#     print(L)
#     print(sumn(L))
#     print(sum(L)/len(L))

# L=[]
# while True:
#     x=int(input("请输入:"))
#     if x < 0:
#         if len(L)>2
#             break
#         else :
#             continue
#     L+=[x]
#     if L.count(x)>=2: 
#         L.remove(x)元素
#         print(L)
# L = list('hello')
# s1 = ' '.join(L)
# s2 = '-'.join(L)
# print(s1,s2)
# x = [x for b in range(1,100,2)]
# print(x)
# L = []
# for b in range(1,100,2):
#     L.append(b)
# print(L)
# L= [x+y for x in ['A','B','C'] 
#             for y in ['1','2','3']]
# print(L,flush=True)

#-----------练习１----
# 1. 输入一个开始的整数 用begin绑定
#     输入一个结束的整数 用end绑定
#     将从begin开始,到end结束(不包含end)的偶数存于列表中,
#     并打印此列表
#     (建议用列表推导式实现)
# begin= int(input("开始数"))
# end = int (input("结束数"))
# L=[x for x in range(begin,end)  if x%2 ==0]
# print(L)
#-------------练习2------------
# 已知有字符串:
#      s = '100,200,300,500,800'
#      将其转化为列表,列表的内部都为数字:
#      L = [100, 200, 300, 500, 800]
# s = '100,200,300,500,800'
# L = s.split(',')
# M = []
# for x in L:
#     M.append(int(x))
# print(M)

#------------------练习3------------
# 已知有一个列表中存有很多数,还有重复的,如:
#      L = [1, 3, 2, 1, 6, 4, 2, ...., 98, 82]
#      1) 将列表中出现数字存入一个列表L2中
#         要求: 重复出现多次的数字只能在L2中保留一份(去重)
#      2) 将L列表中出现两次的数字存于另一个列表L3中,在L3中
#         只保留一份
# L = [1,2,3,1,1,2,4,2,4,5,6,7,8,9,4,6,11,14,16]
# import copy
# L2 = copy.deepcopy(L)
#用ｉｎ来操作，如果已经在列表中来，就忽略操作
# print("这是L2删除重复数字前",L2)
# L.remove(2)
# print("这是L2",L2)
# print("这是L",L)
#L2 = [x for x in L2 if L2.count(x)<=2]
# LL=[]
# for x in L2 :
#     if x not in L2
#         LL.append(x)
#************and #断路运算，一旦前面出结果，后面不会执行****************
# 2) 将L列表中出现两次的数字存于另一个列表L3中,在L3中
#         只保留一份
# L3 = []
#     for x in L:
#         if L.coun(x)==2 and x not in L3:
#             L3.append(x)
# print(L2)

#---------------练习4------------------
# 写程序,生成前40个斐波那契数(Fibonacci)
#     1  1  2  3  5  8  13  ....
#     要求将这些数的存于一个列表中,最后打印这些数
#方法１
# a = 0 #代表当前要求取的数的前一个 
# b = 1# 代表当前要求取的数
# L=[] #创建一个容器，准备向里面放数据
# while len(L) <40:
#     #在此循环内，每次生成一个数，然后放到列表L中
#     L.append(b)
#     #算出下一个fibonacci数,再用b绑定，准备下次放入
#     c = a+ b
#     a = b #让a依旧绑定新数的前一个
#     b = c #b绑定新数
# #方法２
# a = 0 #代表当前要求取的数的前一个 
# b = 0# 代表当前要求取的数
# L=[] #创建一个容器，准备向里面放数据
# while len(L) <40:
#     #在此循环内，每次生成一个数，然后放到列表L中
#     L.append(b)
#     #算出下一个fibonacci数,再用b绑定，准备下次放入
#     a,b = b ,a+b
# #方法3
# L = [1,1]
# while len(L)<40:
#     L.append(L[-1]+L[-2])
print(1 + 1.2222)