
from math import *
from sys import *
from itertools import *

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        a = []
        for i in range(n):
            a.append(int(input()))
        a.sort()
        if a[0] == a[n-1]:
            print('BANG NHAU')
        else:
            print(a[0],a[n-1])