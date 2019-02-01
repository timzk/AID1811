#析构
class Car:
    def __init__(self,info):
        self.info = info
        print("汽车",info,'对象被创建')
    def __del__(self):
        print("汽车",self.info,'对象将被销毁!')
c1 = Car("BYD E6")
input("请输入回车键继续:")

print("程序正常退出")