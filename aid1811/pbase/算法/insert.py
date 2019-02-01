value = [50,60,70,80,90,55,65,75,85,50]

def insert(value):
    #外部循环:对应遍历所有无序数据,依次取出元素插入有序部分
    for i in range(1,len(value)):
    #获取当前无序数据
        temp = value[i]
    #存放该数据的位置
        pos = i
    #内部循环:对应从后向前扫描有序数据,找出取出元素的插入位置:
    #从当前无序数据(i)的前一位开始扫描-> i-1
    #直到遍历完下标为0的数据为止,包含0的位置 -> -1
    #要求从后向前扫描 -> -1
        for j in range(i-1,-1,-1):
            #对比有序数据和取出数据:
            if value[j] > temp:
                #若有序数据大于取出数据#则该有序数据后移
                value[j+1] = value[j]
                #更新插入取出数据的位置
                pos = j
            else:
                #若有序数据小于等于取出数据#则在该有序数据后插入取出数据
                pos = j + 1
                #找到插入位置后退出循环
                break
        # 在指定位置插入取出数据
        value[pos] = temp

insert(value)
print(value)


