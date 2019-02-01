# class Human:
#     def set_info(self,name,age,address='不详'):
#         self.name = name
#         self.age  = age
#         self.address = address
        
#     def show_info(self):
#         print(self.name,'今年',self.age,'岁,家住:',self.address)
# h1 = Human()
# h1.set_info('小张',20,'成都')
# h2 = Human()
# h2.set_info('小李',18)
# h1.show_info()
# h2.show_info()

# class Student:
#     def __init__(self,n,a,s=0):
#         self.name = n
#         self.age = a
#         self.score = s
    
#     def set_score(self,score):
#         self.score = score
#     def show_info(self):
#         print(self.name,self.age,self.score)

# # Student('小张',20,100).show_info()

# L = []
# L.append(Student('小张',20,100))
# L.append(Student('小李',18,98))
# L.append(Student('小王',19))
# L[2].set_score(80)
# for s in L:
#     print(type(s))
#     s.show_info()

class Human:
    def __init__(self,a,n):
        self.age = a
        self.name = n
        self.money = 0
        self.skill = []
    def teach(self,name):

        print(self.name,'教',name,'学python')
        print(self.name,'教',name,'学王者荣耀')
    def work(self):
        pass
    def borrow(self):
        pass
    def show_info(self):
        print(self.age,'岁的',self.name,'有钱',self.money,'元,它学会的技能是:',self.skill)
zhangsan = Human(35,'张三')
lisi = Human(15,'李四')
zhangsan.teach('李四')
lisi.teach('张三')


