#file:mypack/games/contar.py

def play():
    print('正在玩　魂斗罗...')

print('魂斗罗模块被加载!!')

def gameover():
    '''此函数示意包的相对导入.在当前contra.py模块中导入上一级(mypack)模块的menu.py里的show_menu
    然后调用
    '''
    print('游戏结束')
    import time
    time.sleep(2)

    #绝对导入:
    from ..menu import show_menu
    show_menu()

    #错误导入
    #　from ...mypack.menu import show_menu