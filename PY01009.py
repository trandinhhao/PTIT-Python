
from math import *

if __name__ == '__main__':
    s = input()
    thg = 0
    hoa = 0
    for x in s:
        if x >= 'A' and x <= 'Z':
            hoa+=1
        else:
            thg +=1
    if thg >= hoa:
        s = s.lower()
    else:
        s = s.upper()
    print(s)