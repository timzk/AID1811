#二分查找
#原始数据value [1-13]
#待查找数据key 9
def binary(value, key, left, right):
    #退出条件
    if left > right:
        #查找失败,返回-1
        return -1
    # 获取中间元素对应下标值
    middle = (left + right) // 2
    #对比中间元素值与指定查找值
    #如果两者相同
    if value[middle] == key:
        #查找成功
        return middle
    # 如果指定值小于中间值
    elif value[middle] > key:
        # 则在左侧继续找
        # 查找范围减半:左侧下标值不变,右侧下标值为中间值-1
        return binary(value, key, left, middle-1)
    #如果指定值大于中间值
    else:
        #则在右侧继续查找
        #查找范围减半:右侧下标值不变
        #而左侧下标值为中间值的后一位置
        return binary(value, key, middle+1, right)

if __name__ == "__main__":
    value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    #待查找数据
    key = 9
    #二分查找
    res = binary(value,key,0,len(value)-1)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功,对应下标值:",res)