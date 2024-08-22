
from math import *
from sys import *

if __name__ == '__main__':
    for t in range(int(input())):
        tong = 0
        tich = 1
        check = False
        s = input()
        for i in range (len(s)):
            if i % 2 == 0:
                if int(s[i])!=0:
                    tich *= int(s[i])
                    check = True
            else:
                tong += int(s[i])
        if check:
            print(tich, tong)
        else:
            print(0, tong)
            