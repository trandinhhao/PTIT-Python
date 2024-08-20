
from math import *
from sys import *

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        tmp = ""
        for x in s:
            if x <= '9' and x >= '0':
                tmp +=x
            else:
                tmp += ' '
        a = []
        for x in tmp.split():
            a.append(int(x))
        a.sort()
        print(a[0])