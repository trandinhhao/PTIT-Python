
class SV:
    def __init__(self, id, name, lop):
        self.id = id
        self.name = name
        self.lop = lop
        self.diem = 10
        
    def __str__(self):
        tmp = ''
        if self.diem <= 0:
            self.diem = 0
            tmp = 'KDDK'
        return self.id + " " + self.name + " " + self.lop + " " + str(self.diem) + " " + tmp

a = []
n = int(input())
for _ in range(n):
    id = input()
    ten = input()
    lop = input()
    x = SV(id, ten, lop)
    a.append(x)
for _ in range(n):
    x, y = input().split()
    for i in a:
        if x == i.id:
            for j in y:
                if j == 'm':
                    i.diem -= 1
                elif j == 'v':
                    i.diem -= 2
for i in a:
    print(i)