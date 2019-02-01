# s = {'唐僧','悟空','八戒','沙僧'}

# for x in s:
#     print(x)
# else:
#     print("遍历结束")

# print("------------------")
# it = iter(s)
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         print("遍历结束")

#----------皮球落地--------
def get_last_heigt(meter,times):
    '''此函数计算小球从meter高度下落反弹times次后的最终高度'''
    for x in range(times):
        meter /=2
    return meter
print(get_last_heigt(100,10))
    
def get_distance(meter,times):
    '''此函数计算小球从meter高米下落10次反弹高度
       并返回'''
    s = 0
    for x in range(times):
        #累加下落高度
        s += meter
        meter /= 2 #算出反弹高度
        s +=meter  #累加反弹高度
    return s
print(get_distance(100,10))
