import os

class Matematik:
    def __init__(self, sayi_1, sayi_2):
        self.sayi_1 = sayi_1
        self.sayi_2 = sayi_2

    def topla(self):
        return (self.sayi_1 + self.sayi_2)

    def cikar(self):
        return (self.sayi_1 - self.sayi_2)

    def bol(self):
        return (float(self.sayi_1) / self.sayi_2)

    def carp(self):
        return (self.sayi_1 * self.sayi_2)

    def ust_alma(self):
        return (self.sayi_1 ^ self.sayi_2)

