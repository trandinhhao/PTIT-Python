
from math import *
from sys import *

def check(x):
    return x == x[::-1]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        tong = sum(int(i) for i in n)
        if len(str(tong)) > 1 and check(str(tong)):
            print('YES')
        else:
            print('NO')