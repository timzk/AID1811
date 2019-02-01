import time
def input_student(L):
    L1 = []
    while True:
        h = 0
        n = input("请输入姓名: ")
        if n == '':  # if not n:
            break
        try:
            a = int(input("请输入年龄: "))
            s = int(input("请输入成绩: "))
            
        except ValueError:
            print("您的输入有错,请重新输入!!")
            time.sleep(1)
            continue
        nub = input("请输入编号: ")
        d = {}  # 每次创建一个
        d['name'] = n
        d['age'] = a
        d['score'] = s
        d['nub'] = nub
        for i in L1:
            if i['nub'] == nub :
                print("编号重复,请重新输入")
                h +=1
                time.sleep(1)
        for y in L:
            if y['nub'] == nub :
                print("编号重复,请重新输入")
                h +=1
                time.sleep(1)
        if h == 0:
           L1.append(d)


    return L1

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

def read_from_file():
    print("调用成功")
    L =[]
    try:
        fr = open('./student_info/info.txt')
        print("打开成功")
        while True:
            s = fr.readline() 
            if s == '':
                break
            s2 = s.rstrip()
            n,a,s,b=s2.split()
            a = int(a)
            s = int(s)
            L.append(dict(name=n,age=a,score=s,nub=str(s)))
        fr.close()
    except OSError:
        print("打开文件失败")
    return L
    
def save_to_file(L):
    try:
        c = open("./student_info/info.txt",'w')
        for d in L:
            c.write(str(d['name']))
            c.write(str(d['age']))
            c.write(str(d['score']))
            c.write(d['nub'])
        c.close()
    except OSError:
        print("打开失败")
    return L