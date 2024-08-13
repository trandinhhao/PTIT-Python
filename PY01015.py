
from math import *

def check(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        if check(s):
            print('YES')
        else:
            print('NO')