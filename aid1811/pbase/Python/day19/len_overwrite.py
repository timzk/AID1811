#__len__函数
class MyList:
    def __init__(self,iterable = ()):
        self.data = [x for x in iterable]
    def __repr__(self):
        return "MyList(%s)" % self.data
    def __len__(self):
        '''此方法必须返回整数'''
        # return self.data.__len__()
        return len(self.data)
    def __abs__(self):
        L = [abs(x) for x in self.data]
        #构造函数
        lst = MyList(L) #创建MyList类型的新列表
        return lst
myl = MyList([1,-2,3,-4])
print(myl)
print(len(myl))
print(abs(myl))

#---------------int------------------
# class MyNumber:
#     '''自定义一个数字类,用来表示自己定义的数字信息'''
#     def __init__(self,value):
#         '''初始化方法'''
#         self.data = value
    
#     def __repr__(self):
#         return "MyNumber(%d)" % self.data

#     def __int__(self):
#         n = int(self.data)
#         return n
# n1 = MyNumber("100")
# i = int(n1)
# print('i=' ,i)

#-----bool------------------------------
class MyList:
    def __init__(self,iterable = ()):
        self.data = [x for x in iterable]
    def __repr__(self):
        return "MyList(%s)" % self.data
    def __len__(self):
        '''此方法必须返回整数'''
        # return self.data.__len__()
        return len(self.data)
    def __abs__(self):
        L = [abs(x) for x in self.data]
        #构造函数
        lst = MyList(L) #创建MyList类型的新列表
        return lst
    def __bool__(self):
        print("__bool__被调用")
        for x in self.data:
            if bool(x) == False:
                return False
        return True
myl = MyList([1,1,3,0,5])
print(bool(myl))
if myl:
    print("真")
else:
    print("假")