
from math import *

if __name__ == '__main__':
    l, r = map(int,input().split())
    for x in range(l,r+1):
        for y in range(x+1,r+1):
            for z in range(y+1,r+1):
                if gcd(x,y) == 1 and gcd(x,z) == 1 and gcd(y,z) == 1:
                    print('(', x,', ', y, ', ' , z, ')', sep ="")