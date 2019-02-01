from select import select
from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

print("监控IO")
rs, ws, xs = select([s], [], [])
print("就绪:",rs)
print("就绪:",ws)
print("就绪:",xs)


