
from math import *

def check():
    s = input()
    check = True
    for x in s:
        if x != '4' and x != '7':
            check = False
            break
    if check:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        check()