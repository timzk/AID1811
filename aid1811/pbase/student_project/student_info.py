
from student import Student  # 导入类

def input_student():
    L = []   # 创建一个列表,准备放字典
    while True:
        n = input("请输入姓名: ")
        if n == '':  # if not n:
            break
        try:
            a = int(input("请输入年龄: "))
            s = int(input("请输入成绩: "))
        except ValueError:
            print("您的输入有错,请重新输入!!!")
            import time
            time.sleep(2)
            continue

        d = Student(n, a, s)
        L.append(d)
    return L

def output_student(L):
    print("+---------------+----------+----------+")
    print("|    姓名       |   年龄   |   成绩   |")
    print("+---------------+----------+----------+")
    for d in L:
        sn, sa, ss = d.get_infos()
        print("|%s|%s|%s|" % (sn.center(15), 
                            sa.center(10),
                            ss.center(10)))
    print("+---------------+----------+----------+")

def remove_student(L):
    name = input("请输入要删除学生的姓名: ")
    for i in range(len(L)):  # i代表列表的索引
        d = L[i]
        if d.get_name() == name:
            del L[i]
            print("删除成功")
            return
    print("删除失败")

def modify_student(L):
    name = input("请输入要修改成绩的学生姓名: ")
    for d in L:
        if d.get_name() == name:
            score = int(input("请输入学生成绩:"))
            # d['score'] = score
            d.set_score(score)
            print("修改成功!")
            return
    print("修改失败！")

def output_student_by_score_desc(L):
    def get_score(d):
        # return d['score']
        return d.get_score()
    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)

def output_student_by_score_asc(L):
    L2 = sorted(L, key=lambda d: d.get_score())
    output_student(L2)

def output_student_by_age_desc(L):
    L2 = sorted(L, key=lambda d: d.get_age(), reverse=True)
    output_student(L2)

def output_student_by_age_asc(L):
    L2 = sorted(L, key=lambda d: d.get_age())
    output_student(L2)

def read_from_file(filename='si.txt'):
    L = []
    try:
        fr = open(filename)
        while True:
            s = fr.readline() # '张三 20 100\n'
            if not s:
                break
            s2 = s.rstrip()  # '张三 20 100' 去掉右边的空白字符?
            n, a, s = s2.split()  # ['张三', '20', '100']
            a = int(a)
            s = int(s)  # 转为整数
            L.append(Student(n, a, s))

        fr.close()
        print("读取数据成功!!")
    except OSError:
        print("读取数据失败")
    return L

def save_to_file(L):
    try:
        fw = open("si.txt", 'a')
        for d in L:
            # n, a, s = d.get_infos()
            # print(n, a, s, file=fw)
            d.write_to_file(fw)
        fw.close()
        print("保存成功")
    except OSError:
        print("保存失败!")





