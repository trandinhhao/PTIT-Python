
from math import *

def check(x):
    if x<=1:
        return False
    for i in range(2,isqrt(x)+1):
        if x % i ==0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        res = n[len(n)-4:]
        res = int(res)
        if check(res):
            print("YES")
        else:
            print("NO")