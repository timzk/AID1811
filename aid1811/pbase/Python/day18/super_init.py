#显示调用基类的初始化方法__init__

class Human:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def show_info(self):
        print("姓名:",self.name)
        print("年龄:",self.age)

class Student(Human):
    def __init__(self,n,a,s =0):
        self.score = s
        super().__init__(n,a)  #显示调用父类的方法

    def show_info(self):
        super().show_info()
        print("成绩:",self.score)
s = Student("小张",20)
s.show_info()