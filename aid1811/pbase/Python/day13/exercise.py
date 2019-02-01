#give_poke
import random
# 1. 写一个程序, 模拟斗地主发牌,牌共54张
#     种类有: 黑桃('\u2660'), 梅花('\u2663'),
#            红桃('\u2665'), 方块('\u2666)
#     数字有: A2-10JQK
#     大王和小王
#     输入回车, 打印第1个人的17张牌
#     输入回车, 打印第2个人的17张牌
#     输入回车, 打印第3个人的17张牌
#     输入回车, 打印3张底牌
L = ['大王','小王']
a = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
for i in a:
    L.append('\u2660'+i) 
    L.append('\u2663'+i)
    L.append('\u2665'+i)
    L.append('\u2666'+i)
while True:
    s = input('')
    if s =='': 
        L1 = random.sample(L,17)
        print(L1)
        for x in L1:
            L.remove(x)
    if len(L) ==3:
        print('底牌',L)
        break

# 2. 将学生信息管理程序拆分为模块
#     要求:
#       1. 主事件循环的main函数放在 main.py 中
#       2. 显示菜单的函数show_menu 放在 menu.py 中
#       3. 与学生信息操作相关的函数放在student_info.py 中
L = []# 创建一个列表,准备放字典
def input_student():
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

def del_student(s_nub):
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
def output_student_by_score_desc():  #成绩降序
    def get_score(L):
        return L['score']
    s = sorted(L,key = get_score,reverse=True)
    output_student(s)

def output_student_by_score_asc():#成绩升序
    def get_score(L):
        return L['score']
    s = sorted(L,key = get_score)
    output_student(s)

def output_student_by_age_desc():#年龄降序
    def get_score(L):
        return L['age']
    s = sorted(L,key = get_score,reverse=True)
    output_student(s)

def output_student_by_age_asc():#年龄升序
    def get_score(L):
        return L['age']
    s = sorted(L,key = get_score)
    output_student(s)

import menu
def main():
    while True:
        menu.show_main()
        s = input("请选择: ")
        if s == '1':
            input_student()
        elif s == '2':
            # 显示学生信息:
            output_student(L)
        elif s == '3':
            #删除学生信息
            s_nub = input("请输入要删除的学生编号:")
            del_student(s_nub)    
        elif s == '4':
            #修改学生成绩
            s_chg = input("请输入要修改的学生编号:")
            change_student(s_chg)
        elif s == '5':
            output_student_by_score_desc()  # 分数降序
        elif s == '6':
            output_student_by_score_asc()  # 分数升序
        elif s == '7':
            output_student_by_age_desc()  # 年龄降序
        elif s == '8':
            output_student_by_age_asc()  # 年龄升序    
        elif s == 'q':
            break
main()





