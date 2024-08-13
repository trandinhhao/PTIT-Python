
from math import *

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        res1 = s[0] + s[1]
        res2 = s[len(s)-2] + s[len(s)-1]
        if res1 == res2:
            print("YES")
        else:
            print("NO")