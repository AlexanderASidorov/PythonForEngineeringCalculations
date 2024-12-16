# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


# предел текучести материала - 150 МПа
yield_stress = 150 # MPa
youngs_modulus = 210000 # MPa


# cоздадим массив случайных чисел 10 на 10 от 0 до 160. И предствим себе,
# что это напряжения в точках 
array_stress = np.random.random((10, 10))*160


# метод np.any()
# проверим, есть ли в массиве значения больше предела текучести
more_then_yield_stress = np.any(array_stress>150)

# метод np.all()
# проверим не весь ли массив больше предела текучести
all_more_then_yield_stress = np.all(array_stress>150)



# метод np.where()
# найдем эти места в массиве:
indexes = np.where (array_stress>150)

# почти то же самое, но более наглядно (здесь True, значит, что напряжение 
# меньше предела текучести):
filtr_01 = array_stress<150    

    

# метод np.max() np.min()
# найдем максимальное и минимальное значения:
max_value = np.max(array_stress)
min_value = np.min(array_stress)
#
# метод np.argmax(), np.argmin()
# найдем индексы максимального и минимального значения:
indx_max_value = np.argmax(array_stress, axis=-1)
indx_min_value = np.argmin(array_stress, axis= 1)

# если все-таки нужно найти индекс именно, например, глобального максимума, то
# можно воспользоваться методом np.where()
indx_max = np.where (array_stress == np.max(array_stress))



# метод np.sort()
# отсортируем массив от минимума к максимуму
array_02 = np.sort(array_stress.copy(), axis=-1)
array_03 = np.sort(array_stress.copy(), axis=None)


# умножение матрицы на число
# посчитаем упругую деформация в точких, напряжения в которых меньше предела
# текучести
# Массив, в который мы будем записывать значения
array_strain = np.full(array_stress.shape, np.nan)
array_strain[filtr_01] = array_stress[filtr_01]/youngs_modulus

plt.scatter(array_strain, array_stress)




#%%
# посмотрим, что нам даст библиотека numpy при работе с текстом
import numpy as np
import os

# запоминаем текущую директорию
cwd = os.getcwd()
# переходим в директорию с файлами данных
os.chdir('../data/')

 
f = open ('names.txt') # открываем файл для чтения
names = f.read() # записываем содержимое файла в переменную names_pure
f.close() # Файл нам больше не нужем, можем его закрыть
os.chdir(cwd) # возвращаемся в директорию с нашим рабочим скриптом

names = names.replace("'", "") # создаем переменную names и записываем в нее результат удаления символа ' из переменной names_pure
names = names.replace(" ", "") # удаляем все пробелы
names = names.split(",") # разбиваем переменную типа string на список с помощью запятой в качестве разделителя 

# конвертируем список names в массив NumPy
names_array = np.array(names)

# допустим нам надо отсортировать массив^
names_array.sort()

# метод np.unique()
# удалим все дубликаты из массива
names_array = np.unique(names_array)

# создадим массив имен с первой буквой N
names_N_array = names_array[np.array([item[0] == 'N' for item in names_array])]






































































