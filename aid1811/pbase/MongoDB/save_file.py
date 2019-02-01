from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.image
myset = db.boy
#保存图片到数据库

# -----------------读取图片--------------------------
# with open('./98.pdf','rb') as f:
#     data =f.read()
# #转换mongo格式
# conntent = bson.binary.Binary(data)
# #将内容插入集合
# doc = {'filename':'98.pdf','data':conntent}
# myset.insert_one(doc)
#---------------------------------------------------
#------------------获取图片--------------------------
img = myset.find_one({'filename':'98.pdf'})

with open('99.pdf','wb') as f:
    f.write(img['data'])


conn.close()