
from math import *
from sys import *

def sxep(n):
    tmp = n
    res = 0
    while n>0:
        res += n%10
        n//=10
    return (res,tmp)

if __name__ == '__main__':
    for test in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        a.sort(key= sxep)
        print(*a)