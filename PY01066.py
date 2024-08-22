
from math import *
from sys import *

if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        rev = s[::-1]
        check = True
        for i  in range(1,len(s)):
            if abs(ord(s[i])-ord(s[i-1])) != abs(ord(rev[i])-ord(rev[i-1])):
                check = False
                break
        if check:
            print('YES')
        else:
            print('NO')