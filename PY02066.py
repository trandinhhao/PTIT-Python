from sys import *

n = int(input())
a = []
for line in stdin:
    a.extend([int(x) for x in line.split()])
a.sort()
ma = a[-1]
check = True
for i in range(1, ma+1):
    if i not in a:
        print(i)
        check = False
if check:
    print('Excellent!')