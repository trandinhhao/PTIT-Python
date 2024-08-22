
from math import *
from sys import *

def check(x,y):
    if x<=1 or y<=1:
        return False
    else:
        for i in range(2,isqrt(dau)+1):
            if dau % i ==0:
                return False
        for i in range(2,isqrt(cuoi)+1):
            if cuoi % i ==0:
                return False
        return True

if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        dau = int(s[0:3])
        cuoi = int(s[-3:])
        print('YES' if check(dau,cuoi) else 'NO')