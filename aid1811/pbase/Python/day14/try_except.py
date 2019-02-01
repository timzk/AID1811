#try_except.py
#此示例示意用try-except语句来捕获异常,处理错误，将程序由异常状态转为正常状态
def div_apple(n):
    print("%d个苹果你想分给几个人?" %n)
    s = input('请输入人数:')
    try:
        count = int(s) #<---可能出发valueerror错误
        result = n /count  #<---可能出发zerodivisionError错误
        print("每个人分了",result,'个苹果')
    except ValueError:
        print("你输入出错了,异常退出")   
    except ZeroDivisionError:
        print("你输入了0,异常退出")   
    else:
        print("程序正常结束")
    finally:
        print("程序异常结束")
div_apple(10)

#方法2
def div_apple(n):
    print("%d个苹果你想分给几个人?" %n)
    s = input('请输入人数:')
    count = int(s) #<---可能出发valueerror错误
    result = n /count  #<---可能出发zerodivisionError错误
    print("每个人分了",result,'个苹果')  
try:      #函数内出现的异常可以直接截获
    div_apple(10)
    print("分苹果成功")
except ValueError:
    print("分苹果失败,苹果被收回!")
except ZeroDivisionError:
    print("没有人来,程序结束,苹果被收回")
print("程序正常结束")
#方法3
def div_apple(n):
    print("%d个苹果你想分给几个人?" %n)
    s = input('请输入人数:')
    count = int(s) #<---可能出发valueerror错误
    result = n /count  #<---可能出发zerodivisionError错误
    print("每个人分了",result,'个苹果')  
try:      #函数内出现的异常可以直接截获
    div_apple(10)
    print("分苹果成功")
except ValueError as err: #err绑定错误对象 ,把Traceback里的内容打印出来
    print("分苹果失败,苹果被收回!,err=",err)
except ZeroDivisionError:
    print("没有人来,程序结束,苹果被收回")
print("程序正常结束")

#方法4,可以把错误类型放到一起
def div_apple(n):
    print("%d个苹果你想分给几个人?" %n)
    s = input('请输入人数:')
    count = int(s) #<---可能出发valueerror错误
    result = n /count  #<---可能出发zerodivisionError错误
    print("每个人分了",result,'个苹果')  
try:      #函数内出现的异常可以直接截获
    div_apple(10)
    print("分苹果成功")
except (ValueError,ZeroDivisionError): #err绑定错误对象 ,把Traceback里的内容打印出来
    print("分苹果失败,苹果被收回!,err=",err)

print("程序正常结束")