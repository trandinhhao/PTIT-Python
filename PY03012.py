
from math import *
from sys import *

def solve(n):
    return (-n[1][0], n[1][1], n[0])

if __name__ == '__main__':
    a = dict()
    for i in range(int(input())):
        ten = input()
        bai, submit = map(int, input().split())
        a[ten] = [bai, submit]
    res = list(a.items())
    res.sort(key = solve)
    for x in res:
        print(x[0], x[1][0], x[1][1])