import re
pattern = r"(19)+\d+"
s = "张dd d=1991919fjf422, 李 a:199 5 abc_ i s  g!1996 199444"
# s1 = "Hello Jame,Beijing CBD_1"
#直接用re调用
# l = re.findall(pattern,s)
#compile对象调用
regex = re.compile(pattern)
l = regex.findall(s)
print(l)
#按照任意非空字符进行切割,返回一个列表
# l = re.split(r'\s+',"Hello  \r\n World")
# print(l)
# #把任意空格替换为##
# s = re.sub(r'\s+',"##","hello     world nihao kitty")
# print(s)
# #与sub相同,只是会多返回一个替换个数
# s = re.subn(r'\s+',"##","hello     world nihao kitty")
# print(s)

