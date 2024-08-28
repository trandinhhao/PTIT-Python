
from math import *
from sys import *
from itertools import *

if __name__ == '__main__':
    m, k = map(int, input().split())
    a = set(input().split())
    a = list(sorted(a))
    n = range(1,len(a)+1)
    for combo in combinations(n,k):
        for i in combo:
            print(a[i-1], end = ' ')
        print()