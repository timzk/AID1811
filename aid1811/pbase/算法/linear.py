#顺序查找

def linear(value,key):
    for i in range(len(value)):
        #如果出现相同值时
        if value[i] == key:
            #查找成功,返回对应下标值
            return i
    #遍历完所有数据仍为找到时
    else:
        #查找失败,返回-1
        return -1

def erfen(value,key):
    a = 9
    def a():

if __name__ == "__main__":
    #原始数据
    value = [3,9,8,2,1,5,4,6,10,7,13,12,11]
    #待查找数据
    key = 6
    #顺序查找
    res = linear(value,key)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功,对应下标值:",res)