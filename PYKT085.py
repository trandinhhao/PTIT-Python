
check = 0
save = ''
a = dict()
cnt = 0
for _ in range(int(input())):
    s = input()
    if len(s) == 0:
        a[save] = cnt
        check = 0
        cnt = 0
        continue
    if check == 0:
        save = s
        a[s] = 0
        check = 1
    else:
        cnt += 1
a[save] = cnt
for i in a:
    print(i + ': ' + str(a[i]))