
from math import *
from sys import *

f = [True] * (10**6+1)
f[0] = f[1] = False
nt = list([0])

for i in range(2,isqrt(10**6)+1):
    if f[i]:
        nt.append(i)
        for j in range(i*i,10**6+1,i):
            f[j] = False

for i in range(isqrt(10**6) + 1, 10**6 + 1):
    if f[i]:
        nt.append(i)

if __name__ == '__main__':
    n, x = map(int, input().split())
    for i in range(0,n+1):
        print(x + nt[i], end = ' ')
        x = x + nt[i]