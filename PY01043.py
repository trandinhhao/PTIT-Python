
from math import *

def check3(x):
    if len(str(x)) % 2 ==0:
        return True
    else:
        return False
    
def check12(x):
    res = str(x)
    l = 0
    r = len(res)-1
    while l<=r:
        if res[l] != res[r]:
            return False
        l+=1
        r-=1
    for i in res:
        if int(i) % 2 == 1:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        for i in range(22, n,2):
            if check3(i) and check12(i):
                print(i, end = " ")
        print()