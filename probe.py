class Car:
    price = 1000000

    def horse_powers(self, h_p):
        self.h_p = h_p
        return


class Nissan(Car):

    price = 1900000

    def horse_powers(self, h_p):
        self.h_p = h_p
        return


class Kia(Car):
    price = 900000

    def horse_powers(self, h_p):
        self.h_p = h_p
        return


my_auto = Nissan()
frend_auto = Kia()

my_auto.horse_powers(160)
print(my_auto.price)
print(my_auto.h_p)

frend_auto.horse_powers(150)
print(frend_auto.price)
print(frend_auto.h_p)

