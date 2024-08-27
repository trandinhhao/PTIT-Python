
from math import *
from sys import *
from itertools import *

if __name__ == '__main__':
    n,k = map(int, input().split())
    se = set()
    se.update([int(x) for x in input().split()])
    a = [x for x in sorted(se)]
    n = len(a)
    f = range(1,n+1)
    for combo in combinations(f,k):
        x = list(combo)
        for i in x:
            print(a[i-1],end = ' ')
        print()