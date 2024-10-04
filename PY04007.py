
from math import *

class Matrix:
    def __init__(self, n, m, xx):
        self.n = n
        self.m = m
        self.xx = xx
    def tichchuyenvi(self):
        kq = []
        for i in range(n):
            xx = []
            for j in range(n):
                tmp = 0
                for k in range(m):
                    tmp += self.xx[i][k] * self.xx[j][k]
                xx.append(tmp)
            kq.append(xx)
        for i in range(n):
            for j in range (n):
                print(kq[i][j], end = ' ')
            print()
if __name__ == '__main__':
    for i in range(int(input())):
        n, m = map(int, input().split())
        x = []
        for j in range(n):
            x.append(list(map(int,input().split())))
        a = Matrix(n,m,x)
        a.tichchuyenvi()