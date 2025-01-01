from sys import *

n = int(input())
a = []
for i in range(n):
    a.append([x for x in input().split()])
save = []
i = 0
while i < len(a):
    if len(a[i]) == 7:
        save.append('2')
        i += 4
    else:
        if (len(save) != 0 and save[len(save)-1] != '1') or len(save) == 0:
            save.append('1')
        i += 2
print(len(save))
for i in save:
    print(i)