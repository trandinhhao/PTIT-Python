
for _ in range(int(input())):
    x, k = map(int, input().split())
    a = []
    while x != 0:
        if x % k < 10:
            a.append(str(x % k))
        else:
            a.append(chr(x % k - 10 + ord('A')))
        x //= k
    print(''.join(reversed(a)))
