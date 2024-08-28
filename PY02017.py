
from math import *
from sys import *
from itertools import *

if __name__ == '__main__':
    for test in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        tmp = 0
        for i in a:
            tmp ^= i
        print(tmp)