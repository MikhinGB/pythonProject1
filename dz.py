class Car:
    price = 1000000

    def horse_powers(self):
        return 141


class Nissan(Car):

    price = 1900000

    def horse_powers(self):
        return 160


class Kia(Car):
    price = 900000

    def horse_powers(self):
        return 150


my_auto = Nissan()
frend_auto = Kia()

print(my_auto.price)
print(my_auto.horse_powers())

print(frend_auto.price)
print(frend_auto.horse_powers())

