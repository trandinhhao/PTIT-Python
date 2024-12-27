def check(s):
    if len (s) == 1: return False
    if int(s) == int(s[::-1]):
        return True
    else:
        return False

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append([int(x) for x in input().split()])
save = -1
for i in range (n):
    for j in range(m):
        if check(str(a[i][j])) and a[i][j] > save:
            save = a[i][j]
if save == -1: print('NOT FOUND')
else:
    print(save)
    for i in range(n):
        for j in range(m):
            if a[i][j] == save:
                print('Vi tri [%s][%s]' % (i,j))