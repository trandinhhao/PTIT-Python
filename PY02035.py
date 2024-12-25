

if __name__ == '__main__':
    a = input()
    d = dict({})
    k = int(input())
    for i in range(1, len(a), 2):
        tmp = int(a[i-1] + a[i])
        if tmp not in d.keys():
            d[tmp] = 0
        d[tmp] += 1
    check = False
    for x in sorted(d.keys()):
        if d[x] >= k:
            print(x, d[x])
            check = True
    if not check:
        print('NOT FOUND')