
from math import *

def rev(a):
    tmp = 0
    while a>0:
        tmp = tmp * 10 + a%10
        a//=10
    return tmp

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        b = rev(a)
        if gcd(a,b) == 1:
            print("YES")
        else:
            print("NO")