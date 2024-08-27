
from math import *
from sys import *
from itertools import *

if __name__ == '__main__':
    s = input()
    k = len(s)
    n = range(1,k+1)
    for combo in permutations(n,k):
        for i in combo:
            print(s[i-1], end = '')
        print()