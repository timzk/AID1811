#此程序示意导入mymod.py模块,并调用内部的函数,打印mymod.py内部的数据

import mymod #导入模块
from mymod import name2
from mymod import *
mymod.mysum(100)

print('name2=',name2)