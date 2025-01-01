
x = dict()
n = int(input())
for _ in range(n):
    a = [x for x in input().split()]
    if a[3] == 'IN':
        if a[4] not in x.keys():
            x[a[4]] = 0
        if a[1] == 'Xe_con':
            if a[2] == '5':
                x[a[4]] += 10000
            else:
                x[a[4]] += 15000
        elif a[1] == 'Xe_khach':
            if a[2] == '29':
                x[a[4]] += 50000
            else:
                x[a[4]] += 70000
        else:
            x[a[4]] += 20000
for i in x:
    print(i + ': ' + str(x[i]))