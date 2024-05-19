# -*- coding: utf-8 -*-


"""
Рашаем следующую систему уравнений:
    3x + 4y + 5z = 37
    2x - 7y - 3x + 4k  = 24
    2y + 2z + k = 10
    -4x - 3y - 7z + 6k = -12
    
Неизвесные: x, y, z, k
"""

import numpy as np

# Матрица коэффициентов

A = np.array ([[3, 4, 5, 0],
              [2, -7, -3, 4],
              [0, 2, 2, 1],
              [-4, -3, -7, 6]])

# вектор свободных коэффициентов
b = np.array([37, 24, 10, -12])

inv_A = np.linalg.inv(A)

single_matrix = A@np.linalg.inv(A)



# решение
X_01 = np.linalg.inv(A)@b

# проверка
b_= np.array([A[i, :]@X_01 for i in range (0, 4)])


"""
Допустим наша система уравнений недоопределена, т.е. количество неизвестных
больше количества уравнений.
Такую систему можно решить численно методом наименьших квадратов.
Возьмем ту же систему, но добавим в нее еще одну переменную l:  

    3x + 4y + 5z - 2l + 2w = 32
    2x - 7y - 3x + 4k + l + 5w =27
    2y + 2z + k -4l + w = 13
    -4x - 3y - 7z + 6k - 7w = -12
"""
#%%
# Матрица коэффициентов
import numpy as np


A = np.array ([[3, 4, 5, 0, -2 , 2],
              [2, -7, -3, 4, 1, 5],
              [0, 2, 2, 1, -4, 1],
              [-4, -3, -7, 6, 0, -7]])

# вектор свободных коэффициентов
b = np.array([32, 27, 13, -12])

# точного решения эта система не имеет:
#X_01 = np.linalg.inv(A)@b # ошика: матрица A - не квадратная

# но всегда можно попробовать решить чистему численно:
solution = np.linalg.lstsq(A, b)
X_02 = solution[0]
# проверка:
b_= np.array([A[i, :]@X_02 for i in range (np.shape(A)[0])])


#%%
import numpy as np
import matplotlib.pyplot as plt

"""
Решим более сложную систему уравнений...
    x**4 + 2x**2 + 2 = 0
    5x**2 + 12x + 5 = 0

"""

# создаем функцию для первого уравнения
def equation_01 (x):
    return x**4 + 2*x**2 + 2

# создаем функцию для второго уравнения
def equation_02 (x):
    return 5*x**2 + 12*x + 5


# создаем массив значений по x
x = np.linspace(-5, 5, 500)
# на его основе и на основе функций с уравнениями
# создаем два массива со значениями y
y_01=equation_01(x)
y_02=equation_02(x)

# строим два графика
fig01 = plt.figure()
plt.plot(x , y_01)
plt.plot(x , y_02)
plt.grid()

# если нужно увидеть более четко пересечение между кривыми
# изменяем рамки массива значений по x (например  x = np.linspace(2.5, 3, 500))



