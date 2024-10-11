


if __name__ == '__main__':
    s = input().strip()
    a = list()
    if len(s) % 2 == 1:
        s = s[0:len(s)-1]
    for i in range(0,len(s),2):
        a.append(int(s[i:i+2]))
    a = set(a)
    print(*sorted(a))