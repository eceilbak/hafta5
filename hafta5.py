class hesap:
    def __init__(self, say1, say2):
        self.say1 = say1
        self.say2 = say2

    def carp(self):
        return self.say1 * self.say2

    def böl(self):
        return self.say1 / self.say2

    def çıkar(self):
        return self.say1 - self.say2

    def topla(self):
        return self.say1 + self.say2

    def yazdır(self):
        print('sayıların toplamı :', self.topla())
        print('sayıların çarpımı :', self.carp())

A = hesap(5, 3)
print(A.yazdır())
print(A.carp())
