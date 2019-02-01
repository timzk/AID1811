def fry_egg():
    try:
        print("打开天然气")
        try:
            count = int(input("请输入鸡蛋个数:"))
            print("完成剪鸡蛋,共煎了%d个鸡蛋"  % count)
        finally:
            print("关闭天然气")
    except:
        print("煎鸡蛋失败")
fry_egg()