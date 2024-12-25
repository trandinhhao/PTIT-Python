from math import *

def checkk(x):
    if x <= 1:
        return False
    for i in range(2, isqrt(x)+1):
        if x % i == 0:
            return False
    return True

# start
n = int(input())
a = list(map(int, input().split()))
ar = list()
tt = 0
tp = 0
check = True
for i in a:
    if i not in ar:
        ar.append(i)
        tp += i
for i in range(len(ar)):
    tt += ar[i]
    tp -= ar[i]
    if checkk(tt) and checkk(tp):
        print(i)
        check = False
        break

if check:
    print('NOT FOUND')