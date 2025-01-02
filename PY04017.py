from datetime import datetime

class RN:
    def __init__(self, ten, dc, time):
        self.id = ''
        a = dc.split()
        b = ten.split()
        for i in a:
            self.id += i[0].upper()
        for i in b:
            self.id += i[0].upper()
        self.ten = ten
        self.dc = dc
        self.time = (datetime.strptime(time, '%H:%M') - datetime.strptime('06:00', '%H:%M')).seconds / 3600
        self.vt = 120 / self.time
    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + self.dc + ' ' + str(round(self.vt)) + ' Km/h'

a = []
for i in range(int(input())):
    ten = input().strip()
    dc = input().strip()
    time = input().strip()
    x = RN(ten, dc, time)
    a.append(x)
a.sort(key = lambda x: -x.vt)
for i in a:
    print(i)