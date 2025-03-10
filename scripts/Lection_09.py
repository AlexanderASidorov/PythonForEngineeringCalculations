# -*- coding: utf-8 -*-
import numpy as np

'''
Умножение вектора на скаляр
'''
s = 2

a = np.unique([1, 2, 3, 3, 4, 4])
b = np.array([5, 6, 7, 8])

A = np.arange(1, 9).reshape(2, 4)

a2s = a*s

A2s = A*s

#%%
'''
Сложение вектора (матрицы) и скаляра
'''
A_minus_s = A - s

#%%
'''
Норма вектора (матрицы) представляет собой расстояние от хвоста вектора до головы и 
вычисляется с использованием стандартной формулы евклидова расстояния: 
квадратный корень из суммы квадратов элементов вектора
'''

norm_a = np.linalg.norm(a)

norm_A = np.linalg.norm(A)

#%%
'''
Адамово (поэлементное) умножение векторов и матриц
'''
A2a = A*a
#A2b = A*np.array([1, 2, 4, 5, 6]) # выдает ошибку, т.к. размер не совпадает

#%%
'''
Внешнее произведение – это способ создания матрицы из вектора-столбца и 
вектора-строки.
'''

a_outer = np.outer(a, a)
a2a = a*a


#%%
'''
Стандартное умножение матриц ()
'''

A2A_standart = A@A.T





#%%
'''
Точечное произведение – это одно число, которое предоставляет инфор-
мацию о взаимосвязи между двумя векторами. 
Пример вычисления точечного произведениея:
    [1 2 3 4] · [5 6 7 8] = 1×5 + 2×6 + 3×7 + 4×8
                            = 5 + 12 + 21 + 32
                            = 70.
'''
a_dot_b = np.dot(a, b)

a_inner_b = np.inner(a, b)

#%%
'''
Перекрестное произведение двух векторов.
cross product = (array1[1] * array2[2] - array1[2] * array2[1], 
                 array1[2] * array2[0] - array1[0] * array2[2], 
                 array1[0] * array2[1] - array1[1] * array2[0])

cross product = (2 * 6 - 3 * 5, 
                 3 * 4 - 1 * 6, 
                 1 * 5 - 2 * 4)


'''
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6 ])


a_cross_b = np.cross(array1, array2)

#%%

'''
Одним из ключевых, на мой взгляд, инструментом библиотеки NumPy является
модуль линейной алгебры. Более подробно мы изучим его на следующем занятии,
сегодня давайте попробуем решить СЛАУ вида:
    
    7x+4y−z=9
    −5x+8y+3z=15
    3x+2y−12z=35

'''
# обозначим коэффициенты этого уравнения как матрицу A:
    
A = np.array([[7, 4, -1], [-5, 8, 3], [3, 2, -12]])

# а свободные коэффициенты через вектор b
B = np.array([9, 15, 35])

# известно, что решением этой системы будет:
#  X = A**(-1) * B
# где X это x, y и z, A**(-1) - матрица, обратная A
#
# обратная матрица в NumPy расчитывается командой np.linalg.inv(A)
# итого получим решение:
#
X_01 = np.linalg.inv(A)@B
# обратите внимание, что умножение матрицы на вектор происходит с помощью
# знака @
# проыерим решение:
B_= np.array([A[i, :]@X_01 for i in range (np.shape(A)[0])])
# то же самое можно было получить следующим образом:
X_02=np.linalg.solve(A, B)
# а можно с помощью метода наименьших квадратов (но это лишне для нашего СЛАУ):
X_03 = np.linalg.lstsq(A, B)



#%%

'''
                Корреляция и косинусное сходство.
Коэффициент корреляции – это одно число, которое количественно описывает 
линейную взаимосвязь между двумя переменными. Коэффициенты корреляции 
варьируются от –1 до +1, причем –1 указывает на идеальную отрицательную 
взаимосвязь, +1 – на идеальную положительную взаимосвязь, а 0 указывает на
отсутствие линейной взаимосвязи.                
'''
import numpy as np
import matplotlib.pyplot as plt




N = 100




# set up figure
#_,axs = plt.subplots(2,2,figsize=(6,6))

fig, axs = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(12.0, 12.0)
fig.set_dpi(900)
plt.subplots_adjust(left=None,
                    bottom=None, 
                    right=None, 
                    top=None, 
                    wspace=0.3, 
                    hspace=0.3)




# позитивная корреляция

x01 = np.linspace(0,10,N) + np.random.randn(N)
y01 = x01 + np.random.randn(N)

axs[0,0].plot(x01,y01,'k.')
axs[0,0].set_title('Позитивная корреляция')
axs[0,0].set_xlabel('Переменная x')
axs[0,0].set_ylabel('Переменная y')




# негативная корреляция
x02 = x01.copy()
y02 = -y01.copy()

axs[0,1].plot(x02, y02,'k.')
axs[0,1].set_title('Негативная корреляция')
axs[0,1].set_xlabel('Переменная x')
axs[0,1].set_ylabel('Переменная y')



# нулевая корреляция #01
x03 = np.random.randn(N)
y03 = np.random.randn(N)

axs[1,0].plot(x03, y03,'k.')
axs[1,0].set_title('Нулевая корреляция')
axs[1,0].set_xlabel('Переменная x')
axs[1,0].set_ylabel('Переменная y')



# нулевая корреляция #02
x04 = np.cos(np.linspace(0,2*np.pi,N)) + np.random.randn(N)/20
y04 = np.sin(np.linspace(0,2*np.pi,N)) + np.random.randn(N)/20

axs[1,1].plot(x04, y04,'k.')
axs[1,1].set_title('Нулевая корреляция')
axs[1,1].set_xlabel('Переменная x')
axs[1,1].set_ylabel('Переменная y')














