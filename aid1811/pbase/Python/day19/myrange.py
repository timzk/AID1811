# 自己定义的range类
# class MyRange:
#     def __init__(self,start,stop=None,step=None):
#         if stop is None:
#             stop = start#如果stop没有定义,就用start代替stop
#             stop = 0
#         if step is None:#如果step没有定义,默认为1
#             step  =1
#         self.start = start
#         self.stop = stop
#         self.step = step
#     def __iter__(self):
#         return MyRangeIterable(self.start,self.stop,self.step)
        
# class MyRangeIterable:#把得到的三个参数传递给MyRangeIterable
#     def __init__(self,start,stop,step):
#         self.start = start
#         self.stop = stop
#         self.step = step
#     def __next__(self):
#         if self.step > 0:
#             if self.start >= self.stop:
#                 raise StopIteration
#             r = self.start
#             self.start += self.step
#             return r
#         elif self.step<0:
#             if self.start <= self.stop:
#                 raise StopIteration
#             r = self.start
#             self.start += self.step
#             return r
#         else:
#             raise ValueError("步长等于0")
        
# print(sum(MyRange(1,101))) #5050
# L2 = [x for x in MyRange(1,10)]
# print(L2) #[1,4,7]
# for x in MyRange(10,0,-3):
#     print(x)  #打印:10,7,4,1

class MyRange:
    def __init__(self,start,stop=None,step=None):
        if stop ==None:
            stop = start#如果stop没有定义,就用start代替stop
            start = 0
        if step == None:#如果step没有定义,默认为1
            step = 1
        self.start = start
        self.stop = stop
        self.step =step
    
    def __iter__(self):
        return MyRangeIterable(self.start,self.stop,self.step) #把得到的三个参数传递给MyRangeIterable

class MyRangeIterable:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __next__(self):
        if self.step > 0:#如果步长大于0就执行顺序排序
            if self.start >= self.stop:#判断start是否大于stop
                raise StopIteration #如果大于stop就发送错误StopIteration
            r = self.start
            self.start += self.step #执行每一步后start加上步长
            return r
        elif self.step < 0:
            if self.start <= self.stop:
                raise StopIteration
            r = self.start
            self.start += self.step
            return r
        else:
            raise ValueError
try:        
    for a in MyRange(5,0,-1):
        print(a)
except ValueError:
    print("步长不能为0")

