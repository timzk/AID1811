# #索引/切片运算符:[] 的重载

# class MyList:
#     def __init__(self,iterable= ()):
#         '''此处用给定的可迭代对象iterable创建一个新的列表,绑定此对象的data 实例变量中'''
#         self.iter = [x for x in iterable]
#     def __repr__(self): #创建一个新的列表,符合python3语法的对象返回给print来打印
#         return 'MyList(%s)' % self.iter

#     def __getitem__(self,i):
#         if type(i) is int:
#             print("索引")
#         elif type(i) is slice:
#             print("切片")
#         elif type(i) is str:
#             print("错误")
#         return self.iter[i]

#     def __setitem__(self,i,v): #不需要return
#         self.iter[i] = v

#     def __delitem__(self,i):
#         del self.iter[i]

#     #切片运算符重载
# L1 =MyList([1,-2,3,-4,5])
# v = L1[2]  #等同于v = L1.__getitem__(2)
# print(v)
# L1[1] = 2 #等同于 L1.__setitem__(1,+2)
# print(L1)
# del L1[3]  #等同于L1.__delitem__(3)
# print(L1)

