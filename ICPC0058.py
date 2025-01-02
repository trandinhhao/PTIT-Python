from collections import *

ke = []

def bfs(a,u,v):
    visited = [False] * (a+1)
    q = deque()
    q.append(u)
    visited[u] = True
    while len(q) != 0:
        x = q.popleft()
        for j in ke[x]:
            if not visited[j]:
                visited[j] = True
                q.append(j)
    if not visited[v]:
        return True
    else:
        return False

t = int(input())
for _ in range(t):
    ke.clear()
    a, b, u, v = map(int, input().split())
    for _ in range(a+1):
        ke.append([])
    cnt = 0
    for _ in range(b):
        x, y = map(int, input().split())
        ke[x].append(y)
    for i in range(1, a+1):
        if i == u or i == v:
            continue
        else:
            save = ke[i]
            ke[i] = []
            check = bfs(a,u,v)
            ke[i] = save
            if check:
                cnt += 1
    print(cnt)