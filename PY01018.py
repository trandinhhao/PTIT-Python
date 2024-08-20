
from math import *
from sys import *

if __name__ == '__main__':
    p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    p = list(p)
    while True:
        res = input()
        if res == '0':
            break
        k, s = res.split()
        k = int(k)
        kq = ""
        for i in range(len(s)-1,-1,-1):
            tmp = p.index(s[i])
            kq += p[(tmp+k)%28]
        print(kq)