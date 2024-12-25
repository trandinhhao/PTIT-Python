
if __name__ == '__main__':
    a = input()
    d = dict({})
    for i in range(1, len(a), 2):
        tmp = int(a[i-1] + a[i])
        if tmp not in d.keys():
            d[tmp] = 0
        d[tmp] += 1
    for x in d:
        print(x, d[x])