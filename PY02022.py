
from math import *
from sys import *

def check(x):
    if x <=1:
        return False
    for i in range(2, isqrt(x)+1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    a = [int(x) for x in input().split()]
    mp = dict()
    for x in a:
        if x in mp:
            mp[x] += 1
        else:
            mp[x] = 1
    for x in a:
        if x in mp and check(x):
            print(x, mp[x])
            mp.pop(x)