class InvalidDataException(Exception):
    """ Класс исключения при отправке данных принтеру """
    def __init__(self, *args):
        self.message = args[0] if args else None
    def __str__(self):
        return f'Ошибка: {self.message}'

class ProcessingException():
    def print(self, data):
        self.send_data(data)
        print(f'печать: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise InvalidDataException('принтер не отвечает')

    def send_to_print(self, data):
        return False

p = ProcessingException()
p.print('321')
# try:
#     p.print('321')
# except InvalidDataException:
#     print('принтер не отвечает')

