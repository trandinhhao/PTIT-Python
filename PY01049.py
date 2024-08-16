
from math import *

def check(s):
    cnt = len(s)
    if cnt<=1:
        return False
    for i in range(2,isqrt(cnt)+1):
        if cnt % i == 0:
            return False
    nt = 0
    knt = 0
    a = [2,3,5,7]
    for x in s:
        if int(x) in a:
            nt+=1
        else:
            knt+=1
    return nt>knt

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        if check(n):
            print("YES")
        else:
            print("NO")