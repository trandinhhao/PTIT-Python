
from math import *
from sys import *

if __name__ == '__main__':
    for tc in range (int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        x = dict()
        for i in a:
            if i in x:
                x[i]+=1
            else:
                x[i]=1
        x = list(x.items())
        x.sort(key = lambda i: (-i[1],i[0]))
        if x[0][1] > n//2:
            print(x[0][0])
        else:
            print('NO')