
from math import *
from sys import *

if __name__ == '__main__':
    for test in range (int(input())):
        s = input()
        k = input()
        tmp = ' ' * len(k)
        x = s.replace(k, tmp)
        cnt = 0
        for i in x:
            if i != ' ':
                cnt += 1
        kq = (len(s)-cnt)/len(k)
        print(int(kq))