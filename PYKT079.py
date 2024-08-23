
from math import *
from sys import *

if __name__ == '__main__':
    for test in range(int(input())):
        n = int(input())
        a = list(int(x) for x in input().split())
        a.sort()
        se = set(a)
        a = list(se)
        print(a[len(a)-1]-a[0]-len(a)+1)