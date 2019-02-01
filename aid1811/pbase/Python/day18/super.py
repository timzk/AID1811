#super超类
#借助于b来调用A类的方法

class A:
    def work(self):
        print("A.work被调用")

class B(A):
    def work(self):
        print("B.work被调用")
    def do_somthing(self):
        #1.调用自己的work
        self.work()
        #2.调用父类的work
        # super(B,self).work()
        super().work() #因为此时self本来就是自己,所以可以省略
b = B()
# super(B,b).work()  #查找上一层
b.do_somthing()