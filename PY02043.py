for _ in range(int(input())):
    s = input().strip()
    k = input().strip()
    a = s.split(k)
    x = 0
    for i in a:
        x += len(i)
    print((len(s) - x) // len(k))