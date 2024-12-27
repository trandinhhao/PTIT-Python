a = {1:1}
while True:
    ok = 0
    ar = []
    for i in a:
        if i < 10**18:
            if not ((i * 2) in a):
                ar.append(i * 2)
            if not ((i * 3) in a):
                ar.append(i * 3)
            if not ((i * 5) in a):
                ar.append(i * 5)
    for i in ar:
        ok = 1
        a[i] = 1
    if ok == 0:
        break
ar = sorted(list(a))
pos = 1
for i in ar:
    a[i] = pos
    pos += 1
#
n = int(input())
for _ in range(n):
    x = int(input())
    if x in a:
        print(a[x])
    else:
        print('Not in sequence')