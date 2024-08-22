
from math import *
from sys import *

if __name__ == '__main__':
    s = input().lower()
    if '.py' == s[-3:]:
        print('yes')
    else:
        print('no')