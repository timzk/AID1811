#类属性说明

class Human:
    '''此示例示意类属性'''
    count = 0# 创建类属性(变量)

print(Human.count) #获取类变量绑定的值
Human.count = 100  #修改类属性count的值
print(Human.count)

#------------类属性可以通过类的实例直接访问,h1就是实例-----------
h1 = Human()
print(h1.count) #访问类的属性(而不是实例属性)

h1.count = 100 #创建实例属性(而不是修改类属性)
print(h1.count) #打印100, 优先访问实例属性(当实例属性不存在时才访问类属性) 
print(Human.count) #打印0

#-------------类属性可以通过此类的对象的__class__属性间接访问-------
h1 = Human()
h1.__class__.count = 100 #可以通过__class__属性访问类
print(Human.count) #100

#-------------类属性是类的变量,此属性属于类,不属于此类的实例-----------
class Human:
    count  = 0
    def __init__(self,name):
        print(name,'对象被创建')
        self.name = name
        self.__class__.count += 1
    def __del__(self):
        print(self.name,'对象被销毁')
        self.__class__.count -=1
    
L = [Human('孙悟空'),Human('猪八戒')]
h1 = Human()
h1.Human('沙僧')
print("现在共有",Human.count,'个对象')  #打印3个
del L
print("现在共有",Human.count,'个实例对象') #打印1个