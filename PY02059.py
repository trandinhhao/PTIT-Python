f = [True] * 1050
def sieve():
    f[0] = f[1] = False
    for i in range(2, 32):
        if f[i]:
            for j in range(i*i, 1024,i):
                f[j] = False

sieve()
n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append([int(x) for x in input().split()])
save = -1
for i in range (n):
    for j in range(m):
        if f[a[i][j]] and a[i][j] > save:
            save = a[i][j]
if save == -1: print('NOT FOUND')
else:
    print(save)
    for i in range(n):
        for j in range(m):
            if a[i][j] == save:
                print('Vi tri [%s][%s]' % (i,j))