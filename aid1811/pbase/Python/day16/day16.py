#打开文件
# myfile = open("./code/test.txt")
# try:
#     # myfile = open('./txt.txt')
#     myfile = open("./code/test.txt")
   
# #读写文件
#     while True:
#         s = myfile.readlines()
#         if not s:
#             print("读取结束")
#             break
#         print("读取%d个字符:" %len(s),'内容是:',s)

#关闭文件
#     myfile.close()
# except FileNotFoundError:
#     print("打开失败")

#读取code里面的info.txt文本,然后打印,利用了split分割形式来进行,splitlines返回的是一行,然后用列表在split对' '进行分割,存入列表
# try:
#     myfile = open("./code/info.txt")
# #读写文件
#     while True:
#         s = myfile.read()
#         L = s.splitlines()
#         for _ in L:
#             L1 =_.split(' ')
#             print("%s今年%s岁,成绩是%s" % (L1[0],L1[1],L1[2]))
#         if not s:
#             print("读取结束")
#             break
# #关闭文件
#     myfile.close()
# except FileNotFoundError:
#     print("打开失败")


#此示例示意打开一个文本文件,并向里面写入内容
# try:
#     fw = open("./code/mynote.txt",'w') #'w'只写并创建文件,删除原有文件内容
#     #fw = open("./code/mynote.txt",'a') #'a'追加方式写文件,如果有原文件则追加到文件末尾
#     #fw = open("./code/mynote.txt",'x') #'x'只写,只创建新文件,文件存在则报错,FileExistsError错误
#     #写字符串到文件中...
#     fw.write("hello\n") #写入5个字符
#     fw.write("world\n")  #write写入

#     fw.close()
#     print("写入文件成功")

# except OSError:
#     print("打开文件失败")

# def inpu():
#     L = []
#     try:
#         fw = open("./code/mynumbers.txt",'w')
#         while True:
#             try:
#                 s = int(input("请输入正整数:"))
                
#             except ValueError:
#                 print("输入错误")
#                 continue
#             if s == -1:
#                 break
#             try:
#                 fw.write('%d\n' %s)
#                 L.append(s)
#             except OSError:
#                 print("文件打开失败!")
#         return L      
#     finally:
#         fw.close()
# inpu()

# try:        
#     fr = open('./code/mynote.txt','rb')
#     b = fr.read(10)
#     print(b)
#     fr.close()
#     s = b.decode()
#     print("解码后的内容为",s)
# except OSError:
#     print("打开失败")

# b  = bytes(range(256))
# try:
#     fw = open("mybinary.txt",'wb')
#     fw.write(b) #写入字节串
#     fw.close()
# except OSError:
#     print("写入文件失败")