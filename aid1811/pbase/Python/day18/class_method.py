#此示例示意用类方法来访问类属性和改变类变量
#类方法是用于描述类的行为的方法,类方法属于类,不属于类的实例

class A:
    v = 0 #类属性
    @classmethod 
    def get_v(cls):
        return cls.v
    @classmethod
    def set_v(cls,v):
        cls.v = v

#类方法需要使用@classmethod装饰器定义
#类方法至少有一个形参,第一个形参用于绑定类,约定写为'cls'
# print(A.v)
# print(A.get_v()) 
# A.set_v(80)
# print(A.get_v())
# print(A.v)

#类和该类的实例都可以调用类方法
h1 = A()
h1.get_v() #cls,传递是h1.__class__
print(h1.get_v())

#类方法不能访问此类创建的对象的实例属性
h1 = A()
h1.v = 9999 #创建一个实例属性
h1.set_v(8888) #修改的是类的属性
print(A.get_v()) #打印8888