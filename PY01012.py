
from math import *
from sys import *

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    vt = int(input())
    tmp = ""
    for i in range(vt-1):
        tmp += s1[i]
    tmp += s2
    for i in range(vt-1,len(s1)):
        tmp+=s1[i]
    print(tmp)