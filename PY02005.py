
from math import *
from sys import *

if __name__ == '__main__':
    t = int(input())
    a = [int(x) for x in input().split()]
    cnt = 0
    for u in range(t):
        for v in range(u+1,t):
            if a[u] > a[v]:
                cnt += 1
    print(cnt)