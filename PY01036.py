
from math import *

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        s = 0
        tmp = n%2
        if tmp == 0:
            tmp = 2
        for j in range(tmp,n+1,2):
            s += 1/j
        print('%.6f' % s)