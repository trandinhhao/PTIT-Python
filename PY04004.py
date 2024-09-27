
from math import *


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = int(tu)
        self.mau = int(mau)
    def cong(self, b):
        tren = self.tu * b.mau + self.mau * b.tu
        duoi = self.mau * b.mau
        tmp = gcd(tren,duoi)
        return str(int(tren/tmp)) + "/" + str(int(duoi/tmp))



if __name__ == '__main__':
    a = input().split()
    x = PhanSo(a[0], a[1])
    y = PhanSo(a[2], a[3])
    print(x.cong(y))