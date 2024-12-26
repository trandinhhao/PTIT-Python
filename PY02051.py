

a = list()
n = int(input())
for _ in range(n):
    a.append([int(x) for x in input().split()])
if n == 2:
    tmp = a[0][1]//2
    print(tmp, tmp)
else:
    res = [0] * n
    res[0] = a[0][1] + a[0][2] - a[1][2]
    res[0] //= 2
    for i in range(1, n):
        res[i] = a[0][i] - res[0]
    print(*res)