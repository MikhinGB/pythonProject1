import os
import csv
import pandas as pd
from pretty_html_table import build_table


class PriceMachine:
    
    def __init__(self):
        self.data = pd.DataFrame(columns=['наименование', 'цена', 'вес', 'файл', 'цена за кг.'])
        self.result = ''

    
    def load_prices(self, directorie='C:/Users/User/PycharmProjects/PracticalWork/price_list_analyzer/work_space'):
        """ Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт
                
            Допустимые названия для столбца с ценой:
                розница
                цена
                
            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка """

        # создаём пустой DataFrame с необходимыми столбцами

        for entry in os.scandir(directorie):
            if 'price' in entry.name and '.csv' in entry.name:
                path = f'{directorie}/{entry.name}'
                with open(path, encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        new_row = {}
                        # там, где необходимо переименовываем столбцы
                        if 'название' in row:
                            new_row['наименование'] = row.pop('название')
                        elif 'товар' in row:
                            new_row['наименование'] = row.pop('товар')
                        elif 'продукт' in row:
                            new_row['наименование'] = row.pop('продукт')
                        else:
                            new_row['наименование'] = row.pop('наименование')
                        if 'розница' in row:
                            new_row['цена'] = row.pop('розница')
                        else:
                            new_row['цена'] = row.pop('цена')
                        if 'фасовка' in row:
                            new_row['вес'] = row.pop('фасовка')
                        elif 'масса' in row:
                            new_row['вес'] = row.pop('масса')
                        else:
                            new_row['вес'] = row.pop('вес')
                        # добавляем пару ключ: значение - 'файл': значение
                        new_row['файл'] = entry.name
                        # добавляем пару ключ: значение - 'цена за кг.': значение, предварительно вычисляя значение.
                        price = int(new_row.get('цена'))
                        p = int(new_row.get('вес'))
                        new_row['цена за кг.'] = (100 * price // p) / 100
                        self.data = self.data._append(new_row, ignore_index=True)
        count = 1 + self.data.index.stop
        self.data = self.data.sort_values('цена за кг.')
        numers = []
        for i in range(1, count):
            numers.append(i)
        self.data.insert(0, '№', numers)
        return self.data

    def export_to_html(self, fname):
        self.fname = fname
        """        Сохраняем полученный массив данных в выходной файл в формате html        """
        html_table_blue_light = build_table(self.data, 'blue_light', index=False)
        # Save to html file
        with open(fname, 'w') as f:
            f.write(html_table_blue_light)
        return

    def find_text(self, product):

        data_filtered = self.data[self.data['наименование'].str.contains(product, case=False)]
        return print(data_filtered)




pm = PriceMachine()
pm.load_prices()
pm.export_to_html(fname='Позиции продуктов.html')

text = ''
while text != 'exit':
    text = input("Введите название позиции, например, скумбрия: ")
    pm.find_text(text)
else:
    print('Работа закончена! До свидания.')


"""  Логика работы программы

После запуска в консоли необходимо ввести слово, которое входит в название интересующего продукта, например, хек.
Программа выведет в консоль таблицу с позициями, в названии которых присутствует слово "хек". Это может быть и "Хек 
тушка",  и "Мясо хека (колбаса)", и проч. Если по запросу ввести конкретное название, например, "Хек тушка", то соот-
ветственно, программа выведет в консоль только эту позицию. 
Сортировка происходет по увеличению значений в столбце "цена за кг."

При вводе "exit" 
программа заканчивает работу выводом в консоль сообщения "Работа закончена! До свидания." В каталоге появляется файл 
"Позиции продуктов.html", в котором содержится информация, собранная с предоставленных прайсов производителей. 

"""



