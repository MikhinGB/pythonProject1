#Фабрика функций для сложения и вычитания:
def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add # возвращаем функцию, как объект!! Тут скобки не нужны
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract
my_func_add = create_operation("add")
my_func_subtract = create_operation("subtract")
print('Задача 1: ФАБРИКА ФУНКЦИЙ')
print(my_func_add(1,2))              # Выводит 3
print(my_func_subtract(1,2))         # Выводит -1

# Пример лямбда функции с аналогом через def
multiply = lambda x, y: x * y
print('Задача 2.1: ЛЯМБДА-ФУНКЦИЯ (безымянная)')
print(multiply(2, 3)) # Выводит 6


print('Задача 2.2: def-АНАЛОГ ЛЯМБДА-ФУНКЦИИ')
def multiply_def(x, y):
   return x * y
print(multiply_def(2, 3)) # Выводит 6

#Пример создания вызываемого объекта
class Repeater:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return [self.value] * n

repeat_five = Repeater(5)
print('Задача 3: ВЫЗЫВАЕМЫЕ ОБЪЕКТЫ')
print(repeat_five(3)) # Выводит [5, 5, 5]