import re
#忽略大小写--------------------------------------
# s = "Hello World"
# pattern = r'hello'
# regex = re.compile(pattern,flags=re.IGNORECASE)

#使用ASCII字符 
# s = "Hello 你好"
# pattern = r'\w+'
# regex = re.compile(pattern,flags=re.A)

#使用S == DOTALL  使.匹配\n
# s = '''Hello world
# nihao  China
# '''
# pattern = r'.+'
# regex = re.compile(pattern,flags=re.S)

# M 匹配每行开头结尾
# s = '''Hello world  
# nihao  China
# '''
# pattern = r'China$'
# regex = re.compile(pattern,flags=re.M|re.X)

# X 给正则表达式每行加#注释
s = 'abcdefgh'
pattern = r'''(ab) #第一行分组
\w+     #任意字符串
(?P<dog>ef)   #dog捕获组
'''
regex = re.compile(pattern,flags=re.X)

l = regex.findall(s)
print(l)
