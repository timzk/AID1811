# student.py

# 此模块用于描述Student类的定义

class Student:
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s
    def get_infos(self):
        return (self.name, str(self.age), str(self.score))

    def get_name(self):
        return self.name

    def set_score(self, s):
        assert 0 <= s <= 100, '成绩不合法'
        self.score = s

    def get_score(self):
        return self.score

    def get_age(self):
        return self.age

    def write_to_file(self, file):
        file.write(self.name)
        file.write(' ')
        file.write(str(self.age))
        file.write(' ')
        file.write(str(self.score))
        file.write('\n')
        

