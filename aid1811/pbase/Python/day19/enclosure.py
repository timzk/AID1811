#私有属性(封装)
class A:
    def __init__(self):
        self.__money =100 #私有属性,只能用此类的方法来调用

    def __m(self):  #私有方法,也只能通过此类的方法来调用
        print("私有方法__m被调用")

    def show_info(self):
        self.__m()
        print(self.__money)
    # def borror(self,x): #此类的方法可以访问私有属性
    #     if x < self.__money:
    #         self.__money -= x
    #         return x
    #     return 0
a = A()
a.show_info()


# print("借钱",a.borror(20))