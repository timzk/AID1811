import stu_menu
import stu_info
def main():
    infos = [] 
    while True:
        stu_menu.show_main()
        s = input("请选择: ")
        if s == '1':
            infos += stu_info.input_student(infos)
        elif s == '2':
            # 显示学生信息:
            stu_info.output_student(infos)
        elif s == '3':
            #删除学生信息
            stu_info.del_student(infos)    
        elif s == '4':
            #修改学生成绩
            stu_info.change_student(infos)
        elif s == '5':
            stu_info.output_student_by_score_desc(infos)  # 分数降序
        elif s == '6':
            stu_info.output_student_by_score_asc(infos)  # 分数升序
        elif s == '7':
            stu_info.output_student_by_age_desc(infos)  # 年龄降序
        elif s == '8':
            stu_info.output_student_by_age_asc(infos)  # 年龄升序 
        elif s == '9':
            infos+=stu_info.read_from_file()   #读取文本文件里的数据
        elif s == '10':
            stu_info.save_to_file(infos)
            pass
        elif s == 'q':
            break
main()