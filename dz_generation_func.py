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
class Rect:
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __call__(self):
       return self.a * self.b

my_rect = Rect(2, 4)
print('Задача 3: ВЫЗЫВАЕМЫЕ ОБЪЕКТЫ')
print(f'Стороны: {my_rect.a}, {my_rect.b}')
print(f'Площадь: {my_rect()}')