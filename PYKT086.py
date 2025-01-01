fi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def muoi(s):
    s = s[::-1]
    save = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == '1':
            save += 2 ** i
    return save

def conv(a,b):
    sr = []
    while a != 0:
        tmp = a % b
        sr.append(fi[tmp])
        a//=b
    return ''.join(reversed(sr))

with open("DATA.in", "r") as f:
    lines = [x.strip() for x in f.readlines()]
    n = int(lines[0])
    i = 1
    for _ in range(n):
        b = int(lines[i])
        i += 1
        s = lines[i]
        i += 1
        a = muoi(s)
        print(conv(a,b))