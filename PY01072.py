
from math import *
from sys import *

if __name__ == '__main__':
    n,k = map(int, input().split())
    se = set()
    se.update([int(x) for x in input().split()])
    a = [x for x in sorted(se)]
    n = len(a)
    f = [x for x in range(1,k+1)]
    while True:
        for x in f:
            print(a[x-1],end = " ")
        print()
        i = k - 1
        while(i>=0 and f[i]==n-k+i+1):
            i-=1
        if i == -1:
            break
        f[i]+=1
        for j in range(i+1,k):
            f[j] = f[j-1] + 1
        