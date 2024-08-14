
from math import *

        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        n = len(s)
        if s[n-1] == '6' and s[n-2] == '8':
            print("YES")
        else:
            print("NO")