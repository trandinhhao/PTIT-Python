
from math import *
from sys import *

if __name__ == '__main__':
    s = input()
    log = len(s)
    log = log % 3
    if log == 1:
        s = "00" +s
    elif log == 2:
        s = "0" + s
    kq = ""
    for i in range(0,len(s),3):
        tmp = [int(x) for x in s[i:i+3]]
        kq += str(tmp[0] * 4 + tmp[1] *2 + tmp[2] *1)
    print(kq)