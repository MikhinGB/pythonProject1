
class Vehicle:

    vehicle_type = 'none'

class Car:
    price = 1000000

    def horse_powers(self, h_p):
        self.h_p = 141
        return


class Nissan(Car, Vehicle):

    vehicle_type = 'легковой'
    price = 1900000

    def horse_powers(self, h_p):
        self.h_p = h_p
        return



my_auto = Nissan()
my_auto.horse_powers(160)
print(my_auto.h_p)
print(my_auto.vehicle_type, my_auto.price)