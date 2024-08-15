
from math import *

if __name__ == '__main__':
    n, k = map(int, input().split())
    left = 10 ** (k-1)
    right = 10 ** k -1
    cnt = 0
    for i in range(left, right+1):
        if gcd(i,n) == 1:
            print(i, end = " ")
            cnt +=1
            if cnt % 10 == 0:
                print()