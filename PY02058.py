
n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append([int(x) for x in input().split()])
save = False
ma = -1
mi = 1e10
for i in range (n):
    for j in range(m):
        ma = max(ma, a[i][j])
        mi = min(mi, a[i][j])
for i in range (n):
    if ma-mi in a[i]:
        save = True

if not save: print('NOT FOUND')
else:
    print(ma - mi)
    for i in range(n):
        for j in range(m):
            if a[i][j] == ma - mi:
                print('Vi tri [%s][%s]' % (i,j))