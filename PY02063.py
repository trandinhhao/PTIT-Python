
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
hai = max (a[0]*a[1], a[-1] * a[-2])
ba = max(a[-1]*a[0]*a[1], a[-1]*a[-2]*a[-3])
print(max(hai, ba))