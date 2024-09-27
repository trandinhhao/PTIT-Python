
from math import *


class PhanSo:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    def rutgon(self):
        tmp = gcd(self.x, self.y)
        self.x /= tmp
        self.y /= tmp
        return str(int(self.x)) + "/" + str(int(self.y))

if __name__ == '__main__':
    a = input().split()
    x = PhanSo(a[0], a[1])
    print(x.rutgon())