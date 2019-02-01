class Person(object):
    def __new__(cls1,*args,**kwargs): #先于__init__执行,属于一个类方法
        cls1.name = "zhang"
        return object.__new__(cls1)
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

p = Person(175,71)
print(p.name,p.height,p.weight)

