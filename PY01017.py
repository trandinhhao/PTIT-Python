
from math import *

def check(s):
    i = 0
    while i < len(s):
        cnt = 0
        j = i
        while j < len(s) and s[i]==s[j]:
            cnt += 1
            j += 1
        if cnt>0:
            print(cnt,s[i], sep = '', end = '')
        i = j
    print()

        
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        check(s)