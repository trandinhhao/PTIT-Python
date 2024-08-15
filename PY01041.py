
from math import *

def solve(s):
    i = 0
    while i<len(s)-1 and s[i] < s[i+1]:
        i+=1
    if i == len(s)-1:
        return False
    while i<len(s)-1 and s[i] > s[i+1]:
        i+=1
    if i == len(s)-1:
        return True
    else:
        return False

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        if solve(s):
            print("YES")
        else:
            print("NO")
            