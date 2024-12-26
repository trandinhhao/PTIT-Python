from math import *

a = []
n = int(input())
for _ in range(n):
    a.append([int(x) for x in input().split()])
k = int(input())
tren = 0
duoi = 0
for i in range(n):
    for j in range(n):
        if i > j:
            duoi += a[i][j]
        elif i < j:
            tren += a[i][j]
if abs(tren - duoi) <= k:
    print('YES')
    print(abs(tren - duoi))
else:
    print('NO')
    print(abs(tren - duoi))