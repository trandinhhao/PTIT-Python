

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append([x for x in input().split()])
if n > m:
    for i in range(0,n):
        a.pop(i)
        if len(a) == m:
            break
if n < m:
    for i in range(n):
        for j in range(1,m):
            a[i].pop(j)
            if len(a[i]) == n:
                break
for i in range(min(n,m)):
    print(*a[i])
    