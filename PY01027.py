
from math import *
from sys import *

if __name__ == '__main__':
    s = input()
    a = ['6', '8']
    check = True
    for i in s:
        if i not in a:
            check = False
            break
    if not check:
        print("NO")
    else:
        s = s.replace("688", "0")
        s = s.replace("68", "0")
        s = s.replace("6", "0")
        checkk = True
        for i in s:
            if i == '8':
                checkk = False
        if checkk:
            print("YES")
        else:
            print("NO")