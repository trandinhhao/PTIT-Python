
from math import *

def check(s):
    su = 0
    for x in s:
        su += int(x)
    for i in range(2,isqrt(su)+1):
        if su % i == 0:
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