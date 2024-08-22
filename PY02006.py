
from math import *
from sys import *

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        t = int(input())
        a = sorted([int(x) for x in input().split()])
        b = sorted([int(x) for x in input().split()])
        check = True
        for j in range(t):
            if a[j] > b[j]:
                check = False
                break
        if check:
            print('YES')
        else:
            print('NO')