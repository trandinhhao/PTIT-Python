
from math import *

def check1(s):
    tmp = 0
    for i in s:
        tmp += int(i)
    return tmp % 10 == 0

def check2(s):
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) != 2:
            return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        if check1(s) and check2(s):
            print("YES")
        else:
            print("NO")
        