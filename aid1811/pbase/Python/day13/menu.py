def show_main():
    print('1) 添加')
    print('2) 显示 ')
    print('3) 删除 ')
    print('4) 修改 ')
    print('5)按学生成绩高~低显示学生信息')
    print('6)按学生成绩低~高显示学生信息')
    print('7)按学生年龄高~低显示学生信息')
    print('8)按学生年龄低~高显示学生信息')
    print('q) 退出')
def mysum(n):
        if n ==1:
            return 1
        return n+mysum(n-1)
print(mysum(100))