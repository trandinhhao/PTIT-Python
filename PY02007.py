
from math import *
from sys import *

if __name__ == '__main__':
    se = set()
    for x in stdin:
        se.add(int(x)%42)
    print(len(se))