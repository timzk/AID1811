#运算符重载
# class MyNumber:
#     def __init__(self,value):
#         self.data = value
#     def __repr__(self):
#         return 'MyNumber(%d)' % self.data #创建一个新的列表,符合python3语法的对象返回给print来打印
#     def __add__(self,other):
#         s = self.data + other.data
#         return MyNumber(s)  #创建一个新的对象并返回

#     def __sub__(self,other):
#         b = self.data - other.data
#         type(other)
#         return MyNumber(b)

# n1 = MyNumber(500)
# n2 = MyNumber(200)
# n3 = n1 + n2 #等同于n3 = n1.__add__(n2)
# print(n3)
# print(n1,'+',n2,'=',n3)
# n4 = n1 - n2
# print(n4)#等同于n4 = n1.__sub__(n2)


class MyList:
    def __init__(self, iterable=()):
        '''此处用给定的可迭代对象iterable创建一个新的列表,绑定此对象的data 实例变量中'''
        self.iter = [x for x in iterable]
    def __repr__(self): #创建一个新的列表,符合python3语法的对象返回给print来打印
        return 'MyList(%s)' % self.iter

    def __add__(self, other):
        s = self.iter + other.iter
        return MyList(s)  #创建一个新的对象并返回

    def __sub__(self, other):
        b = self.iter - other.iter
        return MyList(b)

    def __mul__(self, other):
    
        b = self.iter * other
        return MyList(b)
    def __rmul__(self, other):
        print("__rmul__被调用")
        b = self.iter * other
        return MyList(b)

    #此示例示意一元运算符的重载
    def __neg__(self):
        gen = (-x for x in self.iter)
        return MyList(gen)

    def __pos__(self):
        gen = (abs(x) for x in self.iter)
        return MyList(gen)

    def __invert__(self):
        gen = (~x for x in self.iter)
        return MyList(gen)

    def __contains__(self,e):  # in / not in运算符
        return e in self.iter

L7 = MyList([1,-2,-3,-4,-5])

print(-3 in L7)

L1 = MyList([1,2,3])
L2 = MyList(range(4,7))
L3 = L1 + L2
print(L3)  #MyList([1,2,3,4,5,6])
L4 = L2 + L1
print(L4) #MyList([4,5,6,1,2,3])
L5 = L1 *2 
print(L5) #MyList([1,2,3,1,2,3])
L6 = 2 * L1
print(L6)
L1 = L1 + L2  #此时L1与之前的L1的id不同 ,结果与L1 += L2相同,但是id不同
print(L1)     

