#快速排序
value = [50,60,70,80,90,55,65,75,85,50]
def quick(value):
    #退出条件
    if len(value) < 2:
        return value
    mark = value[0]
    #找出所有小于关键数据的
    small = [x for x in value if x < mark]
    #找出所有等于关键数据的
    equal = [x for x in value if x == mark]
    #找出所有大于关键数据的
    big = [x for x in value if x > mark]

    #从小到大顺序排序
    return quick(small) + equal + quick(big)

print(quick(value))