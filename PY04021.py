

class Player:
    def __init__(self, id, ten, start, end):
        self.id = id
        self.ten = ten
        a = start.split(':')
        b = end.split(':')
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        self.total = -((a[0]) * 60 + a[1]) + (b[0] * 60 + b[1])
    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + str(self.total // 60) + ' gio ' + str(self.total % 60) + ' phut'

a = []
for i in range(int(input())):
    x = Player(input(), input(), input(), input())
    a.append(x)
a.sort(key = lambda x: -x.total)
for i in a:
    print(i)