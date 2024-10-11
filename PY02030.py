
from math import *

def checkk(x, y):
    if  x <=1 or y <=1:
        return False
    for i in range(2, isqrt(x)+1):
        if x % i == 0:
            return False
    for i in range(2, isqrt(y)+1):
        if y % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    a = [int(x) for x in input().split()]
    tmp = list()
    for x in a:
        if x not in tmp:
            tmp.append(x)
    a = tmp
    trai = a[0]
    phai = sum(a[1:len(a)])
    res = 0
    check = False
    while (res < len(a)):
        if checkk(trai,phai):
            print(res)
            check = True
            break
        res +=1
        if (res < len(a)):
            trai += a[res]
            phai -= a[res]
    if not check:
        print('NOT FOUND')