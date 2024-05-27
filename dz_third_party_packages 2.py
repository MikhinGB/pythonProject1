#  Пример работы библиотеки pandas

import pandas as pd

df = pd.read_excel('names.xlsx')
print(df)

# Выделим из общего DataFrame несколько столбцов. Для этого используем срез:

df_1 = df[['Имя', 'Возраст']]
print(df_1)

# Посчитаем сколько строк с каждой профессией есть в таблице
df_2 = df.groupby('Профессия').count()
print(df_2)