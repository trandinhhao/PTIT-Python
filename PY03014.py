

for i in range(int(input())):
    a = input()
    ar = []
    kq = []
    cnt = 1
    for i in a:
        if i == '(':
            ar.append(cnt)
            kq.append(cnt)
            cnt += 1
        elif i == ')':
            x = ar.pop()
            kq.append(x)
    print(*kq)