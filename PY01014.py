
from math import *

if __name__ == '__main__':
    a, k, n = map(int,input().split())
    start = (a//k +1) * k
    check = 0
    for i in range(start, n+1, k):
        print(i-a, end = " ")
        check = 1
    if check == 0:
        print(-1)