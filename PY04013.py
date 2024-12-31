def to_minute(s):
    h, m = s.split(':')
    return int(h)*60+int(m)

class Tram:
    def __init__(self, ten, start, end, sl):
        self.ten = ten
        self.tgian = to_minute(end)-to_minute(start)
        self.sl = sl
    def __str__(self):
        return self.ten + ' ' + f'{self.sl / (self.tgian/60):.2f}'
a = dict()
t = 1
for _ in range(int(input())):
    ten = input()
    bdau = input()
    kthuc = input()
    sl = input()
    x = Tram(ten, bdau, kthuc, int(sl))
    check = True
    for i in a.values():
        if i.ten == x.ten:
            check = False
            i.sl += x.sl
            i.tgian += x.tgian

    if check:
        x.id = 'T' + str(t).zfill(2)
        t += 1
        a[x.id] = x
for i in a:
    print(i, a[i])