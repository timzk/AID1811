import os 
import pymysql

#把字典插入数据库
#create table words (id int primary key auto_increment,word varchar(32) not null, interpret text);
#create table hist (id int primary key auto_increment,name varchar(32) nuo null,word varchar(32) not null,time varchar(64))
#联合查询查询表hist中的单词,查询words中的解释和时间
#elect hist.word '单词',words.interpret '解释',hist.time '时间' from hist left join words on hist.word=words.word where hist.name ='ni'  order by time desc limit 10;

def dict_word():
    try:
        f = open('./dict.txt')
        db = pymysql.connect('localhost','root','123456','dict')
        cursor = db.cursor()#创建游标
    except Exception as e:
        print('打开失败',e)
    for line in f:
        tmp = line.split(' ')
        word = tmp[0]
        interpret = ' '.join(tmp[1:]).strip()
        # print(tmp)
        sql = '''insert into words (word,interpret) values ("%s","%s")
        '''%(word,interpret)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
    f.close()

dict_word()