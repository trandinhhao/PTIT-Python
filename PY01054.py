
from math import *

def check(s):
    res = 1
    for x in s:
        if x != '0':
            res *= int(x)
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(check(n))