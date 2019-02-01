#自己创建一个类似enumerate
names = ['中国移动','中国电信','中国联通']

#//////////////自己写的/////////////////////
def myenumerate(x,y=0):
    iter1 = iter(x)
    while True:
        try:
            x1 = next(iter1)
            yield(i,y)
            y+=1
        except StopIteration:
            return
for t in myenumerate(names):
    print(t)        
#/////////////////////////////////////////

#方法2-------------------------------------
# def myenumerate(iterable,start = 0):
#     for x in iterable:
#         yield (start,x)
#         start +=1
