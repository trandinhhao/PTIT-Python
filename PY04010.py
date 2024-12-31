

class ThiSinh:
    def __init__(self, ten, ns, d1, d2, d3):
        self.ten = ten
        self.ns = ns
        self.d1 = float(d1)
        self.d2 = float(d2)
        self.d3 = float(d3)
    def out(self):
        print(self.ten, self.ns, end = ' ')
        print("%.1f" % (self.d1 + self.d2 + self.d3), end = ' ')

ten = input().strip()
ns = input().strip()
d1 = input().strip()
d2 = input().strip()
d3 = input().strip()
ts = ThiSinh(ten, ns, d1, d2, d3)
ts.out()