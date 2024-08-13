
from math import *

def solve():
    n, x, m = map(float, input().split())
    x /= 100
    cnt = 0
    while True:
        if n>=m:
            return cnt
        n = n + n*x
        cnt+=1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print(solve())