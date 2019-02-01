class Singleton(object):
    def __new__(cls,*args,**kwargs):

        if not hasattr(cls,"_instance"):
            cls._instance = object.__new__(cls,*args,**kwargs)
        return cls._instance

class Foo(Singleton):
    pass

f1 = Foo()
f2 = Foo()

f1.value = 10
print(f2.value)
print(f1 is f2)

