# L = []# 创建一个列表,准备放字典
def input_student():
    L = []
    x = 0
    while True:
        n = input("请输入姓名: ")
        if n == '':  # if not n:
            break
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
        nub = input("请输入编号: ")
        d = {}  # 每次创建一个
        d['name'] = n
        d['age'] = a
        d['score'] = s
        d['nub'] = nub
        for i in L:
            if i['nub'] == nub:
                print("编号重复,请重新输入")
                x += 1
        if x == 0:
            L.append(d)
    return L

def output_student(L):
    print("+---------------+----------+----------+----------+")
    print("|    姓名       |   年龄   |   成绩   |   编号   |")
    print("+---------------+----------+----------+----------+")   
    print("+---------------+----------+----------+----------+") 
    for d in L:
        sn = d['name']
        sa = str(d['age'])  # 转为字符串,容易居中
        ss = str(d['score'])
        snub = d['nub']
        print("|%s|%s|%s|%s|" % (sn.center(14), 
                            sa.center(10),
                            ss.center(10),snub.center(10)))
    print("+---------------+----------+----------+----------+")

def del_student(L):
    s_nub = input("请输入要删除的学生编号:")
    x = 0
    y = 0
    for i in L:
        if i['nub'] == s_nub:
            L.pop(x)
            print("删除成功")
            y += 1
        else :
            x+=1
    if y == 0:        
        print("没有你输入的学生信息!")
 
def change_student(s_chg):
    s_chg = input("请输入要修改的学生编号:")
    x = 0
    for i in L:
        if i['nub'] == s_chg:
            sa = input("请输入要修改的年龄:")
            ss = input("请输入要修改的成绩:")
            i['age'] = sa
            i['score'] = ss
            print("修改成功")
            x += 1
    if x == 0:
        print("没有找到你学生信息")
def output_student_by_score_desc(L):  #成绩降序
    def get_score(L):
        return L['score']
    s = sorted(L,key = get_score,reverse=True)
    output_student(s)

def output_student_by_score_asc(L):#成绩升序
    def get_score(L):
        return L['score']
    s = sorted(L,key = get_score)
    output_student(s)

def output_student_by_age_desc(L):#年龄降序
    def get_score(L):
        return L['age']
    s = sorted(L,key = get_score,reverse=True)
    output_student(s)

def output_student_by_age_asc(L):#年龄升序
    def get_score(L):
        return L['age']
    s = sorted(L,key = get_score)
    output_student(s)
import menu
def main():
    infos = []
    while True:
        menu.show_main()
        s = input("请选择: ")
        if s == '1':
            infos += input_student()
        elif s == '2':
            # 显示学生信息:
            output_student(infos)
        elif s == '3':
            #删除学生信息
            del_student(infos)    
        elif s == '4':
            #修改学生成绩
            change_student(infos)
        elif s == '5':
            output_student_by_score_desc(infos)  # 分数降序
        elif s == '6':
            output_student_by_score_asc(infos)  # 分数升序
        elif s == '7':
            output_student_by_age_desc(infos)  # 年龄降序
        elif s == '8':
            output_student_by_age_asc(infos)  # 年龄升序    
        elif s == 'q':
            break
main()