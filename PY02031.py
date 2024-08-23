
from math import *
from sys import *

def check(x):
    if x <=1:
        return False
    for i in range(2,isqrt(x)+1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list()
    for i in range(n):
        a.append([int(x) for x in input().split()])
    for i in range(n):
        for j in range(m):
            if check(a[i][j]):
                a[i][j]=1
            else:
                a[i][j]=0
    for i in range(n):
        for j in range(m):
            print(a[i][j], end = " ")
        print()