

class Tax:
    def __init__(self, i, ten, cu, moi):
        self.id = 'KH' + str(i).zfill(2)
        self.ten = ten
        x = int(moi) - int(cu)
        if x > 100:
            self.total = ((x-100) * 200 + 50 * (100+150)) * 1.05
        elif x > 50:
            self.total = ((x-50) * 150 + 50 * (100)) * 1.03
        else:
            self.total = x * 100 * 1.02
    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + f'{self.total:.0f}'
a = []
for i in range(int(input())):
    ten = input()
    start = input()
    end = input()
    x = Tax(i+1, ten, start, end)
    a.append(x)
a.sort(key = lambda x: -x.total)
for i in a:
    print(i)