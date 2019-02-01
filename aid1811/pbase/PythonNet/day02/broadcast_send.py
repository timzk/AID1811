from socket import *
from time import sleep

dest = ('176.209.103.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto('老子今天不上班爽翻'.encode(),dest)

s.close()