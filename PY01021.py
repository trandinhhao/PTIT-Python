
from math import *
from sys import *

if __name__ == '__main__':
    for test in range(int(input())):
        a = [x for x in input()]
        tong = 0
        save = []
        for i in a:
            if i.isalpha():
                save.append(i)
            else:
                tong += int(i)
        save.sort()
        tmp =""
        for i in save:
            tmp += i
        tmp += str(tong)
        print(tmp)