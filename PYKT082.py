
from math import *
from sys import *

a = list()

a.append([int(x) for x in range(0,3)])
a.append([int(x) for x in range(3,5)])
a.append([int(x) for x in range(5,7)])
a.append([int(x) for x in range(7,10)])
a.append([int(x) for x in range(10,13)])
a.append([int(x) for x in range(13,16)])
a.append([int(x) for x in range(16,20)])
a.append([int(x) for x in range(20,23)])
a.append([int(x) for x in range(23,27)])
a.append([int(x) for x in range(27,30)])
a.append([int(x) for x in range(30,33)])
a.append([int(x) for x in range(33,35)])
a.append([int(x) for x in range(35,37)])
a.append([int(x) for x in range(37,39)])
a.append([int(x) for x in range(39,41)])

diem = [0, 2.5, 3, 3.5, 4, 4.5,5,5.5,6,6.5,7,7.5,8,8.5,9]

def solve(x,y,z,t):
    doc = 0
    nghe = 0
    for i in range(len(a)):
        if x in a[i]:
            doc += diem[i]
    for i in range(len(a)):
        if y in a[i]:
            nghe += diem[i]
    tb = (nghe+doc+z+t)/4
    tp = tb * 100 % 100
    nguyen = tb * 100 //100
    if tp <25:
        kq = nguyen
    elif tp <75:
        kq = nguyen + 0.5
    else:
        kq = nguyen + 1
    print("%.1f" % kq)

if __name__ == '__main__':
    for test in range(int(input())):
        x,y,z,t = map(float,input().split())
        solve(x,y,z,t)