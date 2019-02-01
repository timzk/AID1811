def get_score():
    try:
        s = int(input("请输入成绩(0-100):"))
    except:
        print("输入失败")
        return 0
    if 0 >= s <=100:
        return 0
       
scr = get_score()

print("学生的成绩是:",scr)