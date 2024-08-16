
from math import *

def check(s):
    if len(s)<4:
        tmp = int(s)
    else:
        tmp = s[len(s)-4:]
    tmp = int(tmp)
    if tmp<=1:
        return False
    for i in range(2,isqrt(tmp)+1):
        if tmp % i == 0:
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