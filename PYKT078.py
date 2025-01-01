
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    am = []
    duong = []
    maxx = max(a)
    a.insert(a.index(maxx), m)
    for i in a:
        if i < 0:
            am.append(i)
        else:
            duong.append(i)
    am.extend(duong)
    print(*am)