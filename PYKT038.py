
from math import *
from sys import *

if __name__ == '__main__':
    s = input()
    tmp = len(s) % 3
    if tmp == 1:
        s = '00' + s
    elif tmp == 2:
        s= '0' + s
    kq = ''
    for i in range(0,len(s),3):
        res = list(int(x) for x in s[i:i+3])
        kq = kq + str(4 * res[0] + 2 * res[1] + res[2])
    print(kq)