

if __name__ == '__main__':
    n = int(input())
    a = []
    su = 0
    for _ in range(n):
        s = input()
        ngang = 0
        ar = [0] * n
        for i in range(len(s)):
            if s[i] == 'C':
                ngang += 1
                ar[i] += 1
        a.append(ar)
        su += ngang * (ngang-1) // 2
    for i in range(n):
        doc = 0
        for j in range(n):
            doc += a[j][i]
        su += doc * (doc - 1) // 2
    print(su)