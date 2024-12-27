

def move(n, a, b, c):
    if n == 1:
        print('%s -> %s' % (a,c))
    else:
        move(n-1, a, c, b)
        print('%s -> %s' % (a,c))
        move(n-1, b, a, c)
n = int(input())
move(n, 'A', 'B', 'C')