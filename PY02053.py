
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
            if j>n-i-1:
                duoi += a[i][j]
            elif j<n-i-1:
                tren+= a[i][j]
    print('YES' if abs(tren - duoi) <= k else 'NO')
    print(abs(tren - duoi))