f = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def convert(s, t):
    a = []
    while s != 0:
        a.append(s%t)
        s //= t
    a.reverse()
    return ''.join(f[x] for x in a)

n = int(input())
for _ in range(n):
    t = int(input())
    s = input()
    muoi = int(s, 2)
    print(convert(muoi, t))