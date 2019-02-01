def binary(value,key):
    #获取左侧和右侧对应下标值
    left = 0
    right = len(value) -1 
    #若存在合法查找范围则查找数据
    while left <= right:
        #获取中间值对应下标
        middle = (left + right) // 2
        #比较中间值与要查找数据
        if value[middle] == key:
            #查找成功,返回对应下标值
            return middle
        #如果指定值大于中间值
        elif value[middle] < key:
            # 则在右侧继续查找
            left = middle + 1

        else:
            # 则在左侧继续查找
            right = middle -1 
    # 如果遍历完数据仍未找到
    # 查找失败,返回-1
    return -1

if  __name__  == "__main__":
    value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    #待查找数据
    key = 9
    res = binary(value,key)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功",res)
