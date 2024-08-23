
from math import *
from sys import *

if __name__ == '__main__':
    t = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in a:
        if i+1 not in a:
            print(i+1)
            break