
from math import *

def solve (a):
    print("1", sep ="", end = "")
    for i in range(2,isqrt(a)+1):
        cnt = 0
        while a % i == 0:
            cnt+=1
            a//=i
        if cnt != 0:
            print(" * " ,i, '^', cnt, sep = "", end = "")
    if a>1:
        print(" * " ,a, '^', 1, sep = "", end = "")
    print()
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        solve(int(input()))