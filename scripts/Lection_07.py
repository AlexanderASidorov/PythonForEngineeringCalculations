# -*- coding: utf-8 -*-
# Лекция #7. Создание массива NumPy

# импорт библиотеки
import numpy as np

# создание массива
array = np.array ([1, 2, 3, 4])

# свойства массива:
# 1. размер массива
shape = array.shape
# 2. тип переменной массива
type_ = array.dtype 
#%%
# создание массива нулей, единиц или его заполнение заданным значением
array_zeros = np.zeros((3,3), dtype = float)
array_ones = np.ones((3,3), dtype = int)
array_full = np.full((3, 3), 'value')
#%%
# Разбиение отрезка на определенное количество точек
array_linspace = np.linspace(0, 10, 21, dtype= float)
array_arange = np.arange(0, 10, 0.25)

#%%
# Создание массива случайных чисел
array_random = np.random.random ((5, 5))
# то же самое, но массив случайных чисел с нормальным распределением
# подробнее здесь https://ru.wikipedia.org/wiki/Нормальное_распределение
array_random_normal = np.random.normal (1, 0.2, (3, 3))
#%%
# Создание единичной матрицы
array_eye = np.eye(3,3)

#%%
# Доступ к отдельной ячейке/столбцу/строке
raw_1 = array_random [1]
column_1 = array_random[:, 1]
cell_1_1 = array_random[1, 1]
#%%
# Срез массива
array_slice = array_random[1:3, 1:4]






















