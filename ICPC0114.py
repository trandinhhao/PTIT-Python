
from math import *
from sys import *

def check(x):
    a = [2,3,5,7]
    a = [str(x) for x in a]
    tmp = int(str(x)[::-1])
    tong = 0
    for i in str(x):
        if i not in a:
            return False
        else:
            tong += int(i)
    for i in range (2, isqrt(tong)+1):
        if tong % i ==0:
            return False
    for i in range(2,isqrt(x)+1):
        if x % i == 0:
            return False
    for i in range(2,isqrt(tmp)+1):
        if tmp % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if not check(n):
            print('No')
        else:
            print('Yes')