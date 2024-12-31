

class HS:
    ten : str
    ar : list
    def __init__(self, id, ten, ar):
        self.id = 'HS' + str(id).zfill(2)
        self.ten = ten 
        self.ar = [float(x) for x in ar]
        self.tb = (sum(self.ar) + self.ar[0] + self.ar[1]) / 10 / 1.2
        if self.tb >= 9:
            self.type = 'XUAT SAC'
        elif self.tb >= 8:
            self.type = 'GIOI'
        elif self.tb >= 7:
            self.type = 'KHA'
        elif self.tb >= 5:
            self.type = 'TB'
        else:
            self.type = 'YEU'
    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + f'{self.tb:.1f}' + ' ' + self.type

a = []
for i in range(int(input())):
    ten = input()
    ar = [float(x) for x in input().split()]
    x = HS(i+1, ten, ar)
    a.append(x)
a.sort(key = lambda x: (-x.tb, x.id))
for i in a:
    print(i)