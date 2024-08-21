
from math import *
from sys import *

if __name__ == '__main__':
    se = set({})
    t = int(input())
    for i in range(t):
        se.add(input())
    print(len(se))