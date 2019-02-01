class Dog:
    def eat(self,food):
        print(self.color,'的',self.kinds,"正在吃",food)
        self.last_food = food #添加变量,记住上次调用的food的值
    def food_info(self):
        print(self.color,'的',self.kinds,'上次吃的是',self.last_food)


dog1 = Dog() #创建一个实例
dog1.color = '白色' #为dog1对象添加color属性,绑定'白色'
dog1.kinds = '京巴' #添加kinds属性
# print(self.kinds,'正在吃',food)
dog1.eat("骨头")
 
dog1.food_info()  #调用类里面另一个方法
