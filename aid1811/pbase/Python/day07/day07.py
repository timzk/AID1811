# t=()
# for x in range(1,10):
#     t+= (x**2,)
# print(t)

# t2= tuple([x**2 for x in range(1,10)])

# t = tuple("ABC")

# L = [x for x in t]
# print(t)
# sersons = {1:'春季有1,2,3月',2:'夏季有4,5,6月',3:'秋季有7,8,9月',4:'冬季有10,11,12月'}
# print(sersons)
# x=int(input("请输入整数:"))
# if x in sersons:
#     print(sersons[x])
# else :
#     print("信息不在")

# x = input("请输入一段字符串:")
# i = {}
# b = 0
# c = 0
# for i in x:
#     if i not in i:
# print(i)
# s = input("请输入")
# d = {}
# for ch in s:
#     d[ch] =s.count(ch) #d[]在字典d中存储ch的键为ch，值为个数
# print(d)

# for t in d.items():
#     print("%s:%d次" %t) #此时t为一个元组，这个元组里面包含两个数据，所以％后面只需要跟一个t
# s = input("请输入一段字符串:")
# #方法２
# d = {}
# for ch in s:
#     if ch in d:
#         d[ch] +=1
#     else:
#         d[ch] =1
# for t in d.items():
#     print("%s:%d次" %t) #此时t为一个元组，这个元组里面包含两个数据，所以％后面只需要跟一个  
#   
#字典
# e ={}
# while True:
#     x=input("请输入单词")
#     y=input("请输入解释")
#     if x !='':
#         e[x]=y  #用x作为键，y作为值存在字典e当中
#     else :
#         s=input("请输入查询单词")
#         if s in e:
#             print(s,"的解释为",e.get(s))　#查询键为s的值,作为解释打印出来
#         else:
#             print("没有此单词")
#             break
#老师的代码
# words = {}
# while True:
#     word = input("请输入单词")
#     if word == '' #输入回车后取消输入
#         break
#     thans  = input("请输入解释")
#     words[word] = thans  
# while True:
#     w = input("请输入要查询的单词")
#     if w in words:　　#如果输入的单词w(也为键)在字典words里面则打印出来
#         print(words[w])
#     else:
#         print("没有此单词")

# drinks = {
#     'mar' : {'vod','ver'},
#     'blc' : {'rue','kah'},
#     'white' : {'rye','vod'},
#     'sec' :{'org','ver'}
# }
# for name, contents in drinks.items():
#     if contents & {'rue','rye'}:
#         print(contents)
#         print(name)
# {'kah', 'rue'}
# blc
# {'rye', 'vod'}
# white

#-------推导表达式例子-------
# L=['tarena','xiaozhang','hello'] 
# d = {x:len(x) for x in L}
# print(d)

# list1 = [1001,1003,1008,1004]
# list2 = ['Tom','Jerry','Spike','Tyke']
# d = {}
# d = {x:y for x in list1
#             for y in list2}
# # for x,y in list1,list2:
# #     d[x]=y
# for x in list1:
    
# print(d)
#------------------练习----------------------
# 1.  有一只小猴子,摘了很多桃.
#      第一天吃了全部桃子的一半,感觉不饱又吃了一个
#      第二天吃了剩下的一半,感觉不饱又吃了一个
#      ... 以此类推
#      到第十天,发现只剩一个了
#     请问一共摘了多少桃子?
# total_taozi = 0 #桃子个数
# day10 =1
# day=[]
# for x in range(9,0,-1):
#   day[x]=day10
#   print(x)

# 2. 写一个程序,实现一个带有菜单界面的字典程序
#      菜单如下:
#         1) 添加单词
#         2) 删除单词
#         3) 查找单词
#         q) 退出
#     示意见:

# print("1) 添加单词：")
# print("2) 删除单词：")
# print("3) 查找单词：")
# print("4) 退出：")
# x=int(input("请输入:"))
# if x==1:
#    add_words={}
#    while True:
#        x = input("请输入单词")
#        if x =='':
#             break
#        thans =input("请输入解释")
#        add_words[x]=thans
# print("1) 添加单词：")
# print("2) 删除单词：")
# print("3) 查找单词：")
# print("4) 退出：")
# x=int(input("请输入:"))
# if x==2:
#      x=int(input("请输入:"))
#      while True:
#         y = input("请输入要删除的单词")
#         if y =='':
#             break
#         popL=add_words.pop(y)
#         print("删除的单词为:",y,"解释为:",popL)
#         print(add_words)

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

# 3. 项目(学生信息管理)
#     输入任意个学生的信息,形成字典后存入列表中
#        学生信息有: 姓名,年龄,成绩
#     如:
#       请输入姓名: tarena
#       请输入年龄: 15
#       请输入成绩: 99
#       请输入姓名: name2
#       请输入年龄: 20
#       请输入成绩: 80
#       请输入姓名: <回车> 结束输入
#     形成内部存储格式如下:
#     infos = [{'name': 'tarena', 'age':15, 'score':99},
#              {'name': 'name2', 'age':20, 'score':80}]
    
#     第二步以表格方式打印上述列表的内容:
#     +---------------+----------+----------+
#     |    姓名        |    年龄  |    成绩   |
#     +---------------+----------+----------+
#     |    tarena     |    15    |    99    |
#     |     name2     |    20    |    80    |
#     +---------------+----------+----------+




#     break
# add_words.pop(x)
# print(add_words)

# elif x==3:
#    print("3")
# else:
#     print("退出")
    
# words = {}
#  while True:
#      word = input("请输入单词")
#      if word == '' #输入回车后取消输入
#          break
#      thans  = input("请输入解释")
#      words[word] = thans  
#  while True:
#      w = input("请输入要查询的单词")
#      if w in words:　　#如果输入的单词w(也为键)在字典words里面则打印出来
#          print(words[w])
#      else:
#          print("没有此单词")