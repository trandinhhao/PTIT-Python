
from math import *

if __name__ == '__main__':
    t = 1
    for i in range(t):
        s = input()
        if len(s)<3:
            print(s)
            continue
        tmp = ""
        for i in range(len(s)-1,-1,-3):
            tmp = s[i-2:i+1] + "," + tmp
        for i in range(len(s)%3-1,-1,-1):
            tmp = s[i] +tmp
        for i in range(0,len(tmp)-1):
            print(tmp[i], sep ="", end = "")
        print()