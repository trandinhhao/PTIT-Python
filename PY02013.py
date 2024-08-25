
from math import *
from sys import *

if __name__ == '__main__':
    for i in stdin:
        n = int(i)
        if n == 0:
            break
        cnt = 1
        while n != 1:
            cnt +=1
            if n % 2 ==0:
                n /= 2
            else:
                n = n*3 + 1
        print(cnt)