# def make_except():
#     print("开始")
#     # raise ValueError #触发ValueError类型的异常
#     #创建一个错误对象用error来绑定
#     error = ValueError("xxx大街yyy号着火了") #绑定错误对象
#     raise error #触发一个ValueError类型的错误对象

#     print("结束")
# try:
#     make_except()
#     print("make_except调用完成")
# except ValueError as error:
#     print("收到ValueError类型的错误通知",error)
# print("程序正常结束")


# def f1():
#     n = int(input("请输入整数:")) #此处可能触发ValueError错误

# def f2():
#     try:
#         f1()
#     except ValueError as err:
#         print("f1函数内出错")
#         print("f2里的err=",err)
#         raise err
# try:
#     f2()
# except ValueError as err:
#     print("f2内发生了ValueError类型的错误")
#     print(err)

#练习
def get_age():
    age = int(input("请输入年龄:"))
    if age <= 140:
        return age
    else :
        err = ValueError("年龄输入错误")
        raise err
    
try:
    age = get_age()
    print("用户输入的年龄是:",age)
except ValueError as err:
    print("用户输入的不是1-140之间的整数!!!")
    # print(err)