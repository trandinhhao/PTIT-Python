from math import *

def check(x):
    for i in a:
        if int(i / x) == int(i / (x+1)):
            return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
kq = 0
for i in range(min(a), 0,-1):
    if check(i):
        for j in range(n):
            kq += a[j]//(i+1)+1
        break
print(kq)