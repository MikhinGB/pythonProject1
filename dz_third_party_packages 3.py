#  Пример работы библиотеки NumPy

import numpy as np

# создаем массив с рандомизированными целочисленными значениями размером 3х3
rand_arr = np.random.randint(1, 10, size=(3, 3))
print(rand_arr)

# Умножим каждый  элемент массива на 2
rand_arr = 2 * rand_arr

print(rand_arr)