total = 0
n = int(input())
save = [0] * n
for _ in range(n):
    cnt = 0
    a = [x for x in input()]
    for i in range(len(a)):
        if a[i] == 'C':
            cnt += 1
            save[i] += 1
    total += cnt * (cnt - 1) // 2
for i in save:
    total += i * (i -1) // 2
print(total)