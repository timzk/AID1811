#多继承冲突

class Plane:
    def fly(self,height):
        print("飞机以海拔",height,'米高空飞行')
    def m(self):
        print("这是Plane里的方法")

class Car:
    def run(self,speed):
        print("汽车以",speed,'公里/小时的速度行驶')
    def m(self):
        print("这是Car里的方法")

class PlaneCar(Car,Plane):
    '''PlaneCar继承自Plane和Car类'''
    pass

p1 = PlaneCar()

p1.m() #调用的第一个