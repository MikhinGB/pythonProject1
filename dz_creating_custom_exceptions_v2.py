class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def divide(a, b):
   if b == 0:
       raise InvalidDataException('Деление на 0')
   elif type(a) != int:
       raise ProcessingException(f'{a} - неверный тип данных')
   elif type(b) != int:
       raise ProcessingException(f'{b} - неверный тип данных')
   else:
       return a / b



a = 4
b = 2



try:
    d = divide(a, b)
    print(d)
except InvalidDataException as exc:
    print(exc)
except ProcessingException as exc:
    print(exc)


for i in range(1, 6):
    print(f'i = {i}')
