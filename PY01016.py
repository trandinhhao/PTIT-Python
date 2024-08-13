
from math import *

def check(s):
    for i in range(1, len(s), 2):
        for j in range(int(s[i])):
            print(s[i-1], end = "")
    print()


        
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        check(s)