
from math import *
from sys import *

def check(n):
    se = set({})
    se.update([n[i] for i in range(0,len(n),2)])
    return len(se)==1

if __name__ == '__main__':
    for i in range(int(input())):
        n = input()
        print('YES' if (len(n)%2==1) and n[0]!=n[1] and check(n) else 'NO')