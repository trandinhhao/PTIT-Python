
from math import *
from sys import *

if __name__ == '__main__':
    t = int(input())
    a = [float(x) for x in input().split()]
    a.sort()
    minn = a[0]
    maxx = a[t-1]
    s = 0
    cnt = 0
    for i in a:
        if i != minn and i != maxx:
            cnt += 1
            s += i
    print("%.2f" % (s/cnt))