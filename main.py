import pandas as pd
from sys import getsizeof
import numpy as np

gl = pd.read_csv('game_logs.csv')
gl.head()


def mem_usage(pandas_obj):
    if isinstance(pandas_obj, pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else:  # исходим из предположения о том, что если это не DataFrame, то это Series
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b / 1024 ** 2  # преобразуем байты в мегабайты
    return "{:03.2f} MB".format(usage_mb)


gl_int = gl.select_dtypes(include=['int'])
converted_int = gl_int.apply(pd.to_numeric, downcast='unsigned')

print(mem_usage(gl_int))
print(mem_usage(converted_int))

compare_ints = pd.concat([gl_int.dtypes, converted_int.dtypes], axis=1)
compare_ints.columns = ['before', 'after']
compare_ints.apply(pd.Series.value_counts)
print(compare_ints)

# gl.info(memory_usage='deep')

for dtype in ['float', 'int', 'object']:
    selected_dtype = gl.select_dtypes(include=[dtype])
    mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
    mean_usage_mb = mean_usage_b / 1024 ** 2
    print("Average memory usage for {} columns: {:03.2f} MB".format(dtype, mean_usage_mb))


gl_obj = gl.select_dtypes(include=['object']).copy()
gl_obj.describe()

dow = gl_obj.day_of_week
print(dow.head())

dow_cat = dow.astype('category')
print(dow_cat.head())

print(dow_cat.head().cat.codes)

print(mem_usage(dow))
print(mem_usage(dow_cat))
# print(f'Оптимизация использования памяти: улучшение составило {1 - int(mem_usage(dow_cat))/int(mem_usage(dow))} %')


converted_obj = pd.DataFrame()

for col in gl_obj.columns:
    num_unique_values = len(gl_obj[col].unique())
    num_total_values = len(gl_obj[col])
    if num_unique_values / num_total_values < 0.5:
        converted_obj.loc[:, col] = gl_obj[col].astype('category')
    else:
        converted_obj.loc[:, col] = gl_obj[col]

print(mem_usage(gl_obj))
print(mem_usage(converted_obj))

compare_obj = pd.concat([gl_obj.dtypes, converted_obj.dtypes], axis=1)
compare_obj.columns = ['before', 'after']
compare_obj.apply(pd.Series.value_counts)

optimized_gl[converted_obj.columns] = converted_obj

mem_usage(optimized_gl)
