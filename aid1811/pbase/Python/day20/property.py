# class Student:
#     def __init__(self,s):
#         self.__score = s
#     def getscore(self):
#         '''getter获取者'''
#         return self.__score
#     def setscore(self,s):  #使用方法来修改隐藏属性__score
#         '''setter摄取者'''
#         assert 0 <=s <= 100 ,'成绩修改失败'
#         self.__score =s

#     score = property(getscore,setscore)
# stu = Student(59)  #取值stu.getscore()
# print(stu.score)
# stu.setscore(99)   #赋值stu.setscore(99)
# print(stu.score)   #取值

#----------------------------------------------------
#用装饰器方式实现特性属性
# class Student:
#     def __init__(self,s):
#         self.__score = s
#     @property
#     def score(self):
#         '''getter获取者'''
#         return self.__score
#     @score.setter 
#     def score(self,s):  #使用方法来修改隐藏属性__score
#         '''setter设置者'''
#         assert 0 <= s <= 100, '成绩修改失败'
#         self.__score = s

# stu = Student(59)  #取值stu.getscore()
# print(stu.score)
# stu.score = 99   #赋值stu.setscore(99)
# print(stu.score)   #取值
for num in range(10): 
    if (num % 2 == 1): 
        continue 
    print(num)