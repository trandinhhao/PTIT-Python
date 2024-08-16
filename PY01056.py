
from math import *

def check(s):
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
        if i % 2 == 0 and int(s[i]) % 2 != 0:
            return False
        elif i % 2 == 1 and int(s[i]) % 2 ==0:
            return False
    for i in range(2,isqrt(tong)+1):
        if tong % i == 0:
            return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        if check(n):
            print("YES")
        else:
            print("NO")