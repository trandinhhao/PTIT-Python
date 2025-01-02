from datetime import datetime
class Room:
    def __init__(self, i, ten, room, start, end, them):
        self.id = 'KH' + str(i).zfill(2)
        self.ten = ten
        self.room = room
        st = datetime.strptime(start, "%d/%m/%Y")
        end = datetime.strptime(end, "%d/%m/%Y")
        self.cnt = (end - st).days + 1
        if room.startswith("1"):
            self.cost = 25
        elif room.startswith("2"):
            self.cost = 34
        elif room.startswith("3"):
            self.cost = 50
        else:
            self.cost = 80
        self.cost = self.cost * self.cnt + them

n = int(input())
a = []
for j in range(n):
    ten = input().strip()
    room = input().strip()
    st = input().strip()
    end = input().strip()
    them = int(input())
    x = Room(j+1, ten, room, st, end, them)
    a.append(x)
a.sort(key = lambda x : x.cost, reverse = True)
for i in a:
    print(i.id + ' ' + i.ten + ' ' + i.room + ' ' + str(i.cnt) + ' ' + str(i.cost))