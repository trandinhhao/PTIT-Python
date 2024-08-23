
from math import *
from sys import *

if __name__ == '__main__':
    for t in range(int(input())):
        a = [int(i) for i in input()]
        for i in range(len(a) - 1, 0, -1):
            if a[i] >= 5:
                a[i - 1] = a[i - 1] + 1
            a[i] = 0
        if a[0] == 10:
            a[0] = 0
            a = [1] + a
        for i in a:
            print(i, end='')
        print()