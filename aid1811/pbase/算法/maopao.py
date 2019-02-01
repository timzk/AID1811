def bubble(vaule):
    # 外部循环: 对应走访数据的次数
    for i in range(len(value)-1):
        flag = False
    # 内部循环: 对应每次走访数据时,相邻数据对比次数
        for j in range(len(value)-i-1):
            #取从小到大排序
            #如果前者大于后者,则两者交换
            
            if value[j] > value[j + 1]:
                value[j] ,value[j+1] = value[j+1],value[j]
                flag = True
        if flag is False:
            break

    print("i",i+1)
# value = [105,120,110,98,140,130,125]
# value = [110,105, 120, 110, 98, 140, 130, 125]
value = [125,98, 105, 110, 110, 120, 125, 130, 140]
bubble(value)
print(value)





