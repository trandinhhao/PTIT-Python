

class DN:
    def __init__(self, id,  ten, lt, th):
        self.id = 'TS0' + str(id)
        self.ten = ten
        x = lt/10 if lt > 10 else lt
        y = th/10 if th > 10 else th
        self.tb = (x+y)/2
        if self.tb > 9.5:
            self.type = 'XUAT SAC'
        elif self.tb >= 8:
            self.type = 'DAT'
        elif self.tb >= 5:
            self.type = 'CAN NHAC'
        else:
            self.type = 'TRUOT'
    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + f'{self.tb:.2f}' + ' ' + self.type

def func(x):
    return -x.tb

a = []
for i in range(int(input())):
    ten = input()
    lt = float(input())
    th = float(input())
    x = DN(i+1, ten, lt, th)
    a.append(x)
a.sort(key = func)
for i in a:
    print(i)