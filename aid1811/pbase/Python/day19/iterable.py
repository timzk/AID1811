#----iterable迭代器------------------------------
class MyList:
    def __init__(self,iterable =[]):
        self.data = [x for x in iterable]
        print(type(self.data))
    def __repr__(self):
        return "MyList(%s)" % self.data
    
    def __iter__(self):
        '''有此方法的对象可以用iter(obj)来获取迭代器'''
        return MyListIterator(self.data)
   
class MyListIterator:
    '''此类用于创建一个迭代器,此迭代器可以用来访问MyList类型的对象'''
    def __init__(self,lst):
        self.data2 = lst
        self.index = 0 #用来记录此迭代器当前访问的地点
    def __next__(self):
        if self.index >= len(self.data2):
            raise StopIteration
        r = self.data2[self.index]
        self.index +=1
        return r

myl = MyList([1,-2,-3,-4,-5])
it = iter(myl)  #相当于 it = myl.__iter__()
while True:
    try:
        x = next(it) #相当于 x = it.__next__()
        print(x)
    except StopIteration:
        break

# class MyList:
#     def __init__(self,iterable=()):
#         self.data = [x for x in iterable]

#     def __iter__(self):
#         return 

# class MyListIterator:
#     def __init__(self,lst):
#         self.data2 = lst
#         self.index = 0
#     def __next__(self):
#         if self.index >= len(self.data2):
#             raise StopIteration
#         r = self.data2[self.index]
#         self.index += 1
#         return r