

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

save = -1
for i in range(2):
    for j in range(2):
        if a[i] == b[j]:
            save = a[i]
check = True
if save != -1:
    for i in range(n-3):
        if str(save) not in input().split():
            check = False
            break
else:
    check = False

if check:
    print('Yes')
else:
    print('No') 