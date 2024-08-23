
from math import *
from sys import *

if __name__ == '__main__':
    while True:
        a,b,c,d = map(int, input().split())
        x = [a,b,c,d]
        cnt = 0
        if a == 0 and b == 0 and c == 0 and d == 0:
            break
        cnt = 0
        while True:
            if x[0] == x[1] == x[2] == x[3]:
                break
            cnt +=1
            a1 = abs(x[0]-x[1])
            b1 = abs(x[1]-x[2])
            c1 = abs(x[2]-x[3])
            d1 = abs(x[3]-x[0])
            x = [a1,b1,c1,d1]
        print(cnt)