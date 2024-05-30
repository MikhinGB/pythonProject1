#  Пример работы библиотеки pandas

import pandas as pd

df = pd.read_excel('Спортивная, 10.xlsx')
# print(df)



# Выделим из общего DataFrame несколько столбцов. Для этого используем срез:

df_1 = df[['Наименование точки учета', 'Номер ПУ', 'Т1', 'Т2', 'Дата']]

df_1 = df_1.fillna('7777777,7')
# print(df_1)
count_rows = df_1.shape[0]

apartment = df_1['Наименование точки учета'].tolist()
IPU = df_1['Номер ПУ'].tolist()
DAY = df_1['Т1'].tolist()
# print(day)
NIGHT = df_1['Т2'].tolist()
DATE = df_1['Дата'].tolist()
# print(type(apartment[1]))
# list_IPU = []
# list_DATE = []
list_non_data = []
df_out = pd.DataFrame(columns=['Услуга', 'Номер ПУ', 'Дата', 'Показание'])
new = {}

for i in range(0, count_rows):
    if DAY[i] == '7777777,7':
        list_non_data.append(apartment[i])
    else:
        str_IPU = str(IPU[i])
        if len(str_IPU) > 9:
            str_IPU = str_IPU[5:]
            # list_IPU.append(str_IPU)

        str_DATE = DATE[i]
        str_DATE = str_DATE[:10]

        day = DAY[i]
        s = ','
        if day != '0':
            day = day[:(day.index(s) + 3)]


        night = NIGHT[i]
        if night != '0':
            night = night[:(night.index(s) + 3)]

        for k in range(1, 3):
            if k == 1:
                new = {'Услуга': 'Электроэнергия день', 'Номер ПУ': str_IPU, 'Дата': str_DATE, 'Показание': day}
                df_out = df_out._append(new, ignore_index=True)
            else:
                new = {'Услуга': 'Электроэнергия ночь', 'Номер ПУ': str_IPU, 'Дата': str_DATE, 'Показание': night}
                df_out = df_out._append(new, ignore_index=True)





print(f'По приборам учета квартир {list_non_data} данные не считаны. За информацией обратитесь к собственникам.')
gfg_csv_data = df_out.to_csv('Файл Кв24.csv', encoding='cp1251', index=False)
