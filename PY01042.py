
from math import *

def solve(s):
    a = ['0', '1', '2']
    for x in s:
        if x not in a:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        if solve(s):
            print("YES")
        else:
            print("NO")
            