
from math import *
from sys import *

if __name__ == '__main__':
    a = list()
    n = int(input())
    for i in range(n):
        a.append([int(x) for x in input().split()])
    k = int(input())
    tren = 0
    duoi = 0
    for i in range(n):
        for j in range(n):
            if i>j:
                duoi += a[i][j]
            elif i<j:
                tren+= a[i][j]
    print('YES' if tren - duoi <= k else 'NO')
    print(abs(tren - duoi))