
from math import *

def check(n):
    s = 0
    for x in n:
        s += int(x)
        s %= 3
    if s == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        if check(n):
            print("YES")
        else:
            print("NO")