# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:02:55 2023

@author: sidorow
"""

"""
Решение задачи упругой деформации колонны переменного сечения методом конечных
элементов
"""
# Импорт нужных библиотек
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
# Исходные данные
E=200000 # модуль Юнга, Па
R=[6, 6.1, 6.2, 6.3, 6.5, 7] # изменение радиуса колонны, мм
L=1000 # длина колонны, мм
Q=100000 # нагрузка на стержень, Н
n=10 # количество конечных элементов
m=2 # количество степеней свободы элемента
#%% Определение закона изменения радиуса колонны по ее высоте. Предположим, что
# значение радиусов распределено равномерно по длине. Тогда:
YCoordForR=np.linspace(0, L, num=len(R)) # расстояние от вершины колоны до 
                                        # каждого из указанных радиусов
f = interpolate.interp1d(YCoordForR, R, kind='quadratic') # интерполяция данных
LElem=L/n # длина каждого из КЭ
YCoordForElem=np.linspace(LElem/2, L-LElem/2, num=n) # расстояние от вершины 
# колонны до центра каждого из элементов
RElem=f(YCoordForElem) # радиус элемента
plt.plot(RElem, -YCoordForElem, '-', R, -YCoordForR, 'o')
plt.show()
#%% Определение жесткости каждого из элементов
A=np.pi*RElem**2 #площадь поперечного сечения каждого из элементов
Stiffness=E*A/LElem #жесткость каждого из n элементов
#%% Собираем матрицу жесткости
# Общее количество степеней свободы в 1D системе равно n+1, где n - кол-во элементов
NDoF=n # с учетом, что счет мы начинаем с 0!!!!
# Пронумеруем все степени свободы:
DoF=np.linspace(0, NDoF, NDoF+1, dtype=int)
#
# Матрица жесткости одного эллемента:
k=np.array([[+1, -1], [-1, +1]])
# Матрица жесткости всей системы (размерность NDoF на NDoF):
K=np.zeros([len(DoF), len(DoF)], dtype=float)    
# Матрица топологии имеет размерность n на m
Topology=np.zeros([n, m], dtype=int) 
Topology[:,0]=np.linspace(0, NDoF-1, num=n)
Topology[:,1]=np.linspace(1,NDoF, num=n)
#%%
for item in range(NDoF):
    i,j=Topology[item]
    K[item,i]=(K[item,i]+1)+Stiffness[i]
    K[item,j]=(K[item,j]-1)-Stiffness[i]
    K[item+1,i]=(K[item+1,i]-1)-Stiffness[i]
    K[item+1,j]=(K[item+1,j]+1)+Stiffness[i]
#%% Собираем вектор внешних нагрузок
R=np.zeros(len(DoF))
R[0]=-Q
R[-1]=Q
#%% С учетом граничных условий, т.е. с учетомм, что перемещеине последнего узла
# сетки КЭ = 0 мы можем удалить шестую строку и шестой столбец в матрице жесткости,
# а так же шестую строку в векторе нагрузки.
# В резульате получаем:
K_NBC=np.array(K) # сохраним на всякий случай исходную матрицу жесткости
R_NBC= np.array(R) # то же самое для вектора внешних нагрузок
K=np.delete(K, NDoF, axis=0) # удаляем последнюю сторку
K=np.delete(K, NDoF, axis=1) # удяляем последний столбец
R=np.delete(R, NDoF)
#%% Решение методом Solve
USolve=np.linalg.solve(K, R)































