class Car:
    '''此类定义一个小汽车类'''
    def __init__(self,c,b,m): #初始化定义
        self.color = c
        self.brand = b
        self.model = m
        print("__init__初始化方法被调用")
    def run(self,speed):
        print(self.color,'的',self.brand,self.model,'正在以',speed,'公里/小时的速度行驶')
a4 = Car("红色",'奥迪','A4')
a4.run(199)

t1 = Car('黑色','Tesla','Model X')

t1.run(200)