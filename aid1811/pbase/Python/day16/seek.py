#此示例示意用文件流对象的seek方法来移动文件的读写指针位置
try:
     fr = open("./code/mynote.txt",'rb')
     b = fr.read(2)
     print(b) #'AB'
     print("当前的读写位置是:",fr.tell())
     fr.seek(5,0) #从文件头向后移动5个字节
     fr.seek(3,1) #从当前位置开始移动3位
     b = fr.read(5)
     print("移动后的b = ",b)

     fr.close()
except OSError:
    print("打开失败")

