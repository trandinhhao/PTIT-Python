
from math import *
from sys import *

def solve(x,y,z,t):
    one = int(x.replace(t,z)) + int(y.replace(t,z))
    
    two = int(x.replace(z,t)) + int(y.replace(z,t))
    
    print(min(one,two), max(one,two))

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a,b = input().split()
        s = input().split()
        if len(s) == 1:
            x1 = s[0]
            x2 = input()
        else:
            x1,x2 = s
        MIN = min(a,b)
        MAX = max(a,b)
        solve(x1,x2,MIN,MAX)