import random
x = random.randint(1,100)
while True:
    y = int(input('请猜数字:'))
    if x == y:
        print("恭喜你猜对了")
        break
    elif y > x:
        print("你猜大了")
    elif y < x:
        print("你猜小了")    