
from math import *
from sys import *

if __name__ == '__main__':
    hop = set()
    giao = set()
    s1 = input().lower().split()
    s2 = input().lower().split()
    for i in s1:
        hop.add(i)
    for i in s2:
        hop.add(i)
        if i in s1:
            giao.add(i)
    print(*sorted(hop))
    print(*sorted(giao))