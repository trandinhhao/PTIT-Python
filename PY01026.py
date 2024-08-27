
from math import *
from sys import *

if __name__ == '__main__':
    t = int(input())
    for test in range(1,t+1):
        s1 = [x for x in input()]
        s2 = [x for x in input()]
        s1.sort()
        s2.sort()
        check = True
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                check = False
        print('Test ', test,': ', sep = '', end = '')
        if check:
            print("YES")
        else:
            print("NO")