import re
import sys
f = open('test.txt')
data = f.read()


# # pattern = r'[A-Z]+\w*'  #大写字母
# pattern = r"-?\d+\.?/?\d*%?"
# l = re.findall(pattern,data) #数字
# print(l)

#search查找第一个
pattern = r"\n\n[A-Za-z]+\S+"
# l = re.search(pattern,data).group()
l = re.findall(pattern,data)
list1 = []
for i in l:
    list1.append(str(i).split('\n')[2])
print(list1)

pattern = r


#通过findall查找全部
# pattern = r"\n\n.*$\s"
# l = re.findall(pattern,data)

# for i in l:
#     print(str(i))

# def get_address(port):
#     f = open('test.txt')
#     while True:
#         data = ""
#         for line in f:
#             if line != "\n":
#                 data += line
#             else:
#                 break
#         if not data:
#             return "Not Found"
#         try :
#             PORT = re.match(r'\S+',data).group()
#         except Exception as e:
            
#     print(data)
# if __name__ == "__main__":
#     port = sys.argv[1]
#     addr = get_address(port)
#     print(addr)
