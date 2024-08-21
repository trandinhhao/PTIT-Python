
from math import *
from sys import *

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        a = [x for x in input().split()]
        for i in range(k,len(a)):
            print(a[i], end = " ")
        for i in range(0,k):
            print(a[i], end = " ")
        print()