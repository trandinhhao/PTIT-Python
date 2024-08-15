
from math import *

def solve(s):
    if s[0] == s[1]:
        return False
    else:
        for i in range(0, len(s)-2,2):
            if s[i] != s[i+2]:
                return False
        for i in range(1,len(s)-2,2):
            if s[i] != s[i+2]:
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
            