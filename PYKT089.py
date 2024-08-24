
from math import *
from sys import *

if __name__ == '__main__':
    n = int(input())
    a = list()
    for x in stdin:
        tmp = [int(i) for i in x.split()]
        for i in tmp:
            a.append(i)
        if len(a)==n:
            break

    vt = [True] * n 
    chan = []
    le = []
    for i in range(n):
        if a[i] % 2 == 0:
            chan.append(a[i])
        else:
            le.append(a[i])
            vt[i] = False
    chan.sort()
    le.sort(reverse = True)
    c = 0
    l = 0
    for i in range(n):
        if vt[i] == True:
            print(chan[c], end =" ")
            c+=1
        else:
            print(le[l], end = " ")
            l+=1