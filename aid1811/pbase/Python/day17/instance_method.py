class Dog():

    def eat(self,food): #方法
        print("小狗正在吃",food)
    def sleep(self,hour):
        print("小狗睡了",hour,'小时')
    def play(self,obj):
        print("小狗正在玩",obj)

dog1 = Dog() #用Dog类来创建一个Dog类型的对象dog1,然后对象dog1就拥有了类里面的所有方法
dog1.eat('骨头')
dog1.sleep(1)
dog1.play("球")

dog2 = Dog()
dog2.eat("狗粮")
dog2.play("飞盘")
dog2.sleep(3)