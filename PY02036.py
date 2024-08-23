
from math import *
from sys import *

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if gcd(a[i],a[j]) == 1:
                print(a[i], a[j])