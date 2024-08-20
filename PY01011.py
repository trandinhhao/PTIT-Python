
from math import *
from sys import *

a = ['0','2','4','6','8']
res = []
n = 0
save = []

def Try(i):
    if i > len(str(n)):
        return
    for x in a:
        res.append(x)
        if i<= len(str(n))//2:
            tmp = res[::-1]
            s1 = ''.join(res)
            s2 = ''.join(tmp)
            s = s1 + s2
            if int(s)<n and len(str(int(s))) % 2 ==0 and s[0]!='0':
                save.append(int(s))
        Try(i+1)
        res.pop()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        res.clear()
        save.clear()
        Try(0)
        save.sort()
        for x in save:
            print(x, end = " ")
        print()