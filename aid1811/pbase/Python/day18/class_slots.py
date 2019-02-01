#限定一个类创建的实例只能有固定的实例属性,不允许添加此列表意外的实例属性
class Human:
    #此__slots__列表限定Human类型的对象只能用一个age属性
    '''这个是字符串'''
    __slots__ = ['age']
    def __init__(self,age):
        self.age = age
    def show_info(self):
        print("年龄:",self.age)

h1 = Human(10)
h1.show_info()
h1.age = 11
h1.show_info() 
print(dir())