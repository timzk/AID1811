from pymongo import MongoClient
# from pymongo import *
# import pymongo
from random import randint

#创建数据库连接
conn = MongoClient('localhost',27017)
# #创建数据库对象
db = conn.stu
# # #创建集合对象
myset = db['class2']
# create_index('name',sparse = True, unique = )
# myset.drop_indexes()
# index_name = myset.create_index('name')
# index_name = myset.create_index([('age',-1)],name = 'Age')
# print(index_name)
# for i in myset.list_indexes():
#     print(i)
#操作数据
myset.insert({'name':'唐国强','King':'雍正'})
#关闭连接
# cursor = myset.find({},{'_id':0})
#获取那么域存在值的文档
# cursor = myset.find({'name':{'$exists':True}},{'_id':0})
# for i in cursor:
#     print(i)
# print(cursor.next()) #获取下一个文档
# for i in cursor.skip(1).limit(3)
#     print(i)
#按照姓名排序,排序写法同mongo shell不同,用元组表达
# for i in cursor.sort([('name',1)])
#     print(i)
# print(pymongo.version)
# dic = {'$or':[{'King':'乾隆'},{'name':'陈道明'}]}
# d = myset.find_one(dic)
# print(d)

# myset.update_one({'King':'康熙'},{'$set':{'king_name':'玄烨'}},upsert=True)
# myset.delete_many({'king_name':{'$exists':False}})

#聚合操作
#删除没有gender的文档




#------------------------------------------------------------------
# myset.delete_many({'gender':{'$exists':False}})


# cursor = myset.find()

# for i in cursor:
#     myset.update_one({'_id':i['_id']},{'$set':{'score':{'chinese':randint(60,100),'math':randint(60,100),'english':randint(60,100)}}})

# l = [{'$mathch':{'gender':'w'}},{"$sort":{'score.english':-1}},{"$project":{'_id':0}}]
conn.close()