
from math import *
from sys import *

if __name__ == '__main__':
    for test in range(int(input())):
        n = int(input())
        a = list(int(x) for x in input().split())
        b = list(int(x) for x in input().split())
        a.sort()
        b.sort()
        check = True
        for i in range(len(a)):
            if a[i]>b[i]:
                check = False
                break
        if check:
            print('YES')
        else:
            print('NO')