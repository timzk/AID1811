#math对象属性和方法
import re
pattern = r"(ab)cd(?P<dog>ef)"

#通过compile生成对象
regex = re.compile(pattern)
#获取match对象
obj = regex.search("abcdefghijkabcdefghijk",pos=0,endpos=10)
#obj属性变量
print(obj.pos)#目标字符串开始位置
print(obj.endpos)#目标字符串的结束位置
print(obj.re) #正则表达式
print(obj.string)#目标字符串
print(obj.lastgroup)#最后一组名称
print(obj.lastindex)#最后一组是第几组
print("-------------------------------")
#obj方法
print(obj.span()) #匹配内容的起止位置
print(obj.start())#匹配内容的开始位置
print(obj.end())#匹配内容的结束位置
print(obj.group())#整体匹配
print(obj.group(2)) #获取第二组
print(obj.group('dog'))#通过捕获组别名来获取,dog组内容
print(obj.groupdict())#获取捕获组字典
print(obj.groups())#获取所有子组对应内容

