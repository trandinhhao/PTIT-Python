
from math import *
from sys import *
from itertools import *

if __name__ == '__main__':
    for test in range(int(input())):
        s = input().split()
        res = ''
        for i in s:
            if len(res) + len(i) +1<=100:
                res = res + i +' '
            else:
                break
        print(res)