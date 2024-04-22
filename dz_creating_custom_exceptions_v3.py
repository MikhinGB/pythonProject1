class MyCustomError(Exception):

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        print('вызов str')
        if self.message:
            return f'MyCustomError, {self.message}'
        else:
            return 'MyCustomError был поднят по тревоге'


def divide(a, b):
   if b == 0:
       raise MyCustomError('Хьюстон! У нас проблемы!')
   else:
       return a / b


a = 4
b = 0
 
try:
    d = divide(a, b)
    print(d)
except MyCustomError as exc:
    print(exc)

for i in range(1, 6):
    print(f'i = {i}')
