#用类描述学生管理信息
# class Student:
#     # L = []
#     def __init__(self,n,a,s=0):
#         self.name = n
#         self.age = a
#         self.score =s

# infos = []
# def  add_student(infos,n,a,s):
#      stu= Student(n,a,s)
#      infos.append(stu)

# def del_student(infos):
#     n = input("请输入要删除的学生:")
#     for index,stu in enumerate(infos):
#         if s.name == n:
#             del infos[index]
#             print("删除",n,'成功')
#             return
#         print("删除",n,'失败')

# def get_avg_score(infos):
#     s = 0
#     for stu in infos:
#         s+=stu.score
#     return s/len(infos)

# add_student(infos,'小张',20,100)
# del_student(infos)
#--------------------------------------------------------------
# class Student:
#     infos = []
#     def __init__(self,n,a,s=0):
#         self.name = n
#         self.age = a
#         self.score =s

#     @classmethod
#     def add_student(cls,n,a,s):
#         stu= Student(n,a,s)
#         cls.infos.append(stu)
#     @classmethod
#     def del_student(cls):
#         n = input("请输入要删除的学生:")
#         for index,stu in enumerate(cls.infos):
            
#             if stu.name == n:
#                 del cls.infos[index]
#                 print("删除",n,'成功')
#                 return
#             print("删除",n,'失败')
#     @classmethod
#     def get_avg_score(cls):
#         s = 0
#         for stu in cls.infos:
#             s += stu.score
#         return s/len(cls.infos)

# Student.add_student('小张',20,100)
# Student.del_student()
#------------------------------------------------------------------

# class MyList(list):
#     def insert_head(self,n):
#         self.insert(0,n)
# myl = MyList(range(3,6))
# print(myl)
# myl.insert_head(2)
# print(myl)

# class A:
#     v = 100
#     def __init__(self): 
#         self.v = 200 
# a1 = A() 
# a2 = A() 
# del a2.v
# print(A.v)
# print(a1.v)
# print(a2.v)
a = {'one': 1, 'two': 2, 'three': 3} 
print(a.setdefault('one'), a.setdefault('four'))
print(a)