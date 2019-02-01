class A(object):
    def __init__(self):
        self.item = {}
    def __call__(self):#相当于 ()
        print("Call方法被调用")

    def __getitem__(self,key):
        return self.item.get(key)
    def __setitem__(self,key,value):
        self.item[key] = value
a = A()
#自动调用__call__
a()
a['key'] = "Hello world"
print(a['key'])