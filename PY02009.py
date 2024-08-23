
from math import *
from sys import *

if __name__ == '__main__':
    for test in range(int(input())):
        n = int(input())
        d = dict()
        for i in range(n):
            x = int(input())
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        tmp = list(d.items())
        tmp.sort(key = lambda x : (-x[1], x[0]))
        print(tmp[0][0])