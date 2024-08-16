
from math import *

def check_nt(x):
    if x <=1:
        return False
    for i in range(2, isqrt(x)+1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        cnt = 0
        for i in range(n):
            if gcd(i,n) == 1:
                cnt+=1
        if check_nt(cnt):
            print("YES")
        else:
            print("NO")