
from math import *

def solve(a, b):
    tmp = gcd(a,b)
    res = 0
    while tmp>0:
        res += tmp%10
        tmp //=10
    if res == 1:
        return False
    for i in range(2,isqrt(res)+1):
        if res % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        if solve(a,b):
            print('YES')
        else:
            print('NO')