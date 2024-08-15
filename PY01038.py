
from math import *

def dob(n):
    tmp = n
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n//=10
    return tmp + res

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if n % 7 ==0:
            print(n)
        else:
            cnt = 0    
            while cnt <= 1000:
                cnt+=1
                n = dob(n)
                if n % 7 ==0:
                    print(n)
                    break
            if cnt > 1000:
                print(-1)
            