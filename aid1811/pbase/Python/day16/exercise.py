#   1. 写程序,实现文件的复制,(注:只复制文件,不复制文件夹)
#     要求:
#       1) 要考虑文件关闭的问题
#       2) 要考虑超大文件无法一下加载到内存的问题
#       3) 要能复制二进制文件(非文本文件)
# try:
#     L = []
#     f =  open("./code/mynote.txt",'rb')
#     for line in f:
#         L.append(line)  #每次line绑定一行数据
#     f.close()
#     c = open("./code/copynote.txt",'w')
#     for _ in L:
#         c.flush()
#         c.write(_.decode('utf-8'))
#     c.close()
#     print("复制文件成功")
# except EOFError:
#     print("打开失败")


#<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>#
def copy(src_file,dst_file):
    '''src_file:源文件
       dst_file:目标文件
       '''
    fr = open(src_file,'rb')
    fw = open(dst_file,'wb')
    while True:
        s = fr.read(4096)
        if not b:
            break
        fw.write(s)
    
    fr.close()
    fw.close()
    return True
src = input("请输入源文件名:")
dst = input("请输入目标文件名:")
if copy(src,dst):
    print("复制文件成功")
else:
    print("失败")