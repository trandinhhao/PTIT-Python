
from math import *
from sys import *

def check(x):
    tmp = x
    res = 0
    while x>0:
        res += factorial(x%10)
        x//=10
    return tmp == res

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if not check(n):
            print('No')
        else:
            print('Yes')