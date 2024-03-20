# 1. Создайте новый класс House
# 2. Задайте ему новый атрибут numberOfFloors = 10
# 3. В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"
# 4. Полученный код напишите в ответ к домашему заданию

class House():
    def __init__(self):
        self.numberOfFloors = 9
        self.numberOfEntrances = 3
        self.numberOfApartaments = 125

my_house = House()

# Имитация состояния пожарных датчиков в i-й момент времени.
# Предполагается, что в каждом подъезде, на каждом этаже стоит датчик.

fire_detectors = [
    0, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 0, 0, 0, 0
]

# Проверяем состояние датчиков
if 1 not in  fire_detectors:
    print('В Багдаде ВСЁ спокойно!')
else:
    for k in range((my_house.numberOfEntrances * my_house.numberOfFloors) - 1):
        if fire_detectors[k] == 1:
            print(
                'ВНИМАНИЕ! Пожар в ', 1 + k // my_house.numberOfFloors, 'подъезде, на ',
                1 + k % my_house.numberOfFloors, ' этаже'
            )
