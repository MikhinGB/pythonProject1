
class Vehicle:

    vehicle_type = 'none'

class Car:
    price = 1000000

    def horse_powers(self):
        self.h_p = 141
        print('Мощность двигателя',  self.h_p, ' л/с')


class Nissan(Car, Vehicle):

    vehicle_type = 'легковой'
    price = 1900000

    def horse_powers(self):
        self.h_p = 160
        print('Мощность двигателя Nissan', self.h_p, ' л/с')



my_auto = Nissan()
my_auto.horse_powers()
print(my_auto.vehicle_type, my_auto.price)