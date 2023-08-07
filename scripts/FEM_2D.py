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
#%%
# Исходные данные
E=200000 # модуль Юнга, Па
# R=[6, 6.1, 6.2, 6.3, 6.5, 7] # изменение радиуса колонны, мм
# Размеры поперечного сечения балки
a=10 # размер стороны квадрата, мм
Lbeam=500 # длина балки, мм
Qy=100000 # нагрузка на балку в направлении Y, Н
Qx=100000 # нагрузка на балку в направлении X, Н
phi=5# угол балки относительно закрепления
n=3 # количество конечных элементов
DofEl=4 # количество степеней свободы элемента
#%% Определение площади поперечного сечени бакли, мм**2:
A=a*a
#%% Определение матрицы жесткости каждого из элементов в локальной системе координат
SingleMatrix=np.array([[1, 0, -1, 0], [0, 0, 0, 0], [-1, 0, 1, 0], [0, 0, 0, 0]])
#длина элемента
L=Lbeam/n
klocal=((E*A)/L)*SingleMatrix
#%% Определяем направляющие sin и cos
m=np.sin(phi*(np.pi/180))
l=np.cos(phi*(np.pi/180))
T=np.array([[l, m, 0, 0], [-m, l, 0, 0], [0, 0, l, m], [0, 0, -m, l]])
# Ttranspose=T.transpose()
#%% Определение матрицы жесткости каждого из элементов в глобальной системе координат
k=np.matmul(T.transpose(), klocal)
k=np.matmul(k, T)
# k1=np.array([[l*l, l*m, -l*l, -l*m], [l*m, m*m, -l*m, -m*m], 
#             [-l*l, -l*m, l*l, l*m], [-l*m, -m*m, l*m, m*m]])
# k2=((E*A)/L)*k1


#%% Собираем матрицу жесткости
# Общее количество степеней свободы в 2D системе равно n*2+1, где n - кол-во элементов
NDoF=n*2+1 # с учетом, что счет мы начинаем с 0!!!!
# Пронумеруем все степени свободы:
DoF=np.linspace(0, NDoF, NDoF+1, dtype=int)
#
# Матрица жесткости одного эллемента:
# k=np.array([[+1, -1], [-1, +1]])
# Матрица жесткости всей системы (размерность NDoF на NDoF):
K=np.zeros([len(DoF), len(DoF)], dtype=float)    
# Матрица топологии имеет размерность n на m
Topology=np.zeros([n, DofEl], dtype=int)
Topology[0, :]=[0, 1, 2, 3]
#%% Собираем матрицу топологии
for i in range (1, n):
    Topology[i, :]=[Topology[i-1, 2], Topology[i-1, 3], 
                    Topology[i-1, 2]+2, Topology[i-1, 3]+2]
#%% Заполняем глобальную матрицу жесткости
for item in range(n):
    Line = Topology[item]
    K[Line[0]:Line[3]+1, Line[0]:Line[3]+1]=K[Line[0]:Line[3]+1, Line[0]:Line[3]+1]+k

#%% ПРОДОЛЖЕНИЕ Собираем вектор внешних нагрузок
R=np.zeros(len(DoF))
R[-2]=Qy
R[-1]=Qx
R[0]=-Qx
R[1]=-Qy
#%% С учетом граничных условий, т.е. с учетомм, что перемещеине первого узла
# сетки КЭ = 0 мы можем удалить нулевой и первый строки и столбцы в матрице жесткости,
# а так же нулевую и первую строки в векторе нагрузки.
# В резульате получаем:
K_NBC=np.array(K) # сохраним на всякий случай исходную матрицу жесткости
R_NBC= np.array(R) # то же самое для вектора внешних нагрузок
K=np.delete(K, [0,1], axis=0) # удаляем 0 и 1 сторку
K=np.delete(K, [0,1], axis=1) # удяляем 0 и 1 столбец
R=np.delete(R, [0,1]) # удаляем 0 и 1 сторку
#%% Метод наименьших квадратов
ULsqr=np.linalg.lstsq(K, R)
ULsqr=ULsqr[0]
# U=np.array([0,0])
U=np.concatenate(([0,0], ULsqr), axis=0)
#%% Визуализируем результаты
Ux=U[0:-1:2]
Uy=U[1:-1:2]
Uy=np.append(Uy, [U[-1]], axis=0)
#%%
Coordinates=np.linspace(0, Lbeam, num=n+1)
Uzero=np.zeros([len(Coordinates),1])
Coordinatedelta=Coordinates+Ux
#
# Создаем переменную для графика
fig01=plt.figure(1,figsize=(10,5))
# Определяем названия осей
plt.xlabel('Координата по X')
plt.ylabel('Деформация, мм')
# Начальное положение балки
plt.plot(Coordinates, Uzero, marker='o')
# Балка после деформации
plt.plot(Coordinatedelta, -Uy, marker='*')
#%%
# #%% Решение системы уравнению относительно перемещений U
# # Метод инверсии
# KInv=np.linalg.inv(K) # Находим матрицу обратную K
# SingleMatrix=np.matmul(K,KInv) # проверяем, что произведение матрици K и обратной
#                                 # ей KInv дает единичную матрицу
# Uinv=np.matmul(KInv,R) # находим вектор перемещений































