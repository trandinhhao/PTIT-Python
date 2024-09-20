
from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = sorted(set(int(x) for x in input().split()))
    b = sorted(set(int(x) for x in input().split()))
    for x in a:
        if x in b:
            print(x, end = ' ')
    print()
    for x in a:
        if x not in b:
            print(x, end = ' ')
    print()
    for x in b:
        if x not in a:
            print(x, end =' ')
    print()