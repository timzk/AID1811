def fn(n):
    l = []
    for i in range(n):
        l.append(lambda x:x*i)
    return l
l = fn(4)
print(l[0](10))
print(l[1](10))
print(l[2](10))
#首先这个属于是一个闭包,fn(4)调用,l为空列表,for i in range(n):这里,i第一次为0,
# 然后执行l.append(lambda x:x*i),把匿名函数lambda x:x*i追加到列表l里面,
# 此时l列表里面就会产生l=[(lambda x:x*i),(lambda x:x*i),(lambda x:x*i),(lambda x:x*i)]
#因为这个是一个闭包,所以i的值一直存在,而且绑定的是for循环最后一次(3),
#然后执行print(l[0](10)),l的第一个索引为lambda x:x*i,然后(10)作为形参传入到匿名函数里面,也就是x=10,然后再乘以之前的for
#循环里面的i(3),所以得到的结果为30