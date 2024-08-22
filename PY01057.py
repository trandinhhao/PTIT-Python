
from math import *
from sys import *

def is_nt(x):
    if x <=1:
        return False
    else:
        for i in range(2,isqrt(x)+1):
            if x % i == 0:
                return False
        return True

if __name__ == '__main__':
    for i in range(int(input())):
        a = [2,3,5,7]
        s = input()
        check = True
        for i in range(0,len(s)):
            if (is_nt(i) and int(s[i]) in a) or (not is_nt(i) and int(s[i]) not in a):
                check = True
            else:
                check = False
                break
        if check:
            print('YES')
        else:
            print('NO')