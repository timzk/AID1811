#继承的语法和用法

class Human:
    '''定义人类的基类'''
    def say(self,what):
        print("说",what)
    def walk(self,distance):
        print("走了",distance,'公里')
    
class Student(Human):
    def study(self,subject):
        print("学习:",subject)

class Teacher(Human):
    def teach(self,subject):
        print("教",subject)

h1 = Teacher()
h1.say("天气变冷了")
h1.walk(5)
h1.teach("python")


