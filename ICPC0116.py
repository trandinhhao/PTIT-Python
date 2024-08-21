
from math import *
from sys import *

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        if n[0] == n[len(n)-1]:
            print("YES")
        else:
            print("NO")