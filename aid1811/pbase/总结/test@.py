def outmost(*args,**kwargs):
    def out(func):
        s = "执行外部函数"
        print(s)
        print(args)
        def innter(*args,**kwargs):
            print("++++++++")
            func(*args)
            print("++++++++")
        return innter
    return out
@outmost("hello")
def fun(a,b):
    print("函数执行:",a,b)

fun(1,2)
