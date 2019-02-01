#sys.stdin用法:
import sys 
while True:
    print("请输入:")
    s = sys.stdin.readline()  #sys.stdin不能关闭
    print("你刚才输入的是:",s)

# s = sys.stdin.read()#输入ctrl+d 为输入文件结束符

