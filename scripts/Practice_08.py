# -*- coding: utf-8 -*-
"""
Создайте переменную, содержащую целые числа от 0 до 3,
и вторую переменную, равную первой переменной плюс некоторое смещение. 
Затем создайте симуляцию, в которой вы систематически варьируете
это смещение между –50 и +50 (то есть на первой итерации симуляции вторая
переменная будет равна [–50, –49, –48, –47]). В цикле for вычислите корреляцию 
и косинусное сходство между двумя переменными и сохраните эти
результаты. Затем постройте линейный график, показывающий, как среднее
смещение влияет на корреляцию и косинусное сходство. 
"""
import numpy as np
import matplotlib.pyplot as plt

def pearson (x, y):
    '''
    функция для расчета Коэффициента корреляции (коэф Пирсона)

    Parameters
    ----------
    x : 1D numpy array.
    y : 1D numpy array.

    Returns
    -------
    pearson : float, коэффициент Пирсена

    '''
    # нормализуем x и y
    xm  = x-np.mean(x)
    ym  = y-np.mean(y)
    
    # числитель
    numirator = np.dot(xm , ym)
    # знаменатель
    denumirator = np.linalg.norm(xm) * np.linalg.norm(ym)
    # коэффициент
    pearson = numirator/denumirator
    return pearson

def cosin (x, y):
    '''
    функция для расчета косинусного сходства

    Parameters
    ----------
    x : 1D numpy array.
    y : 1D numpy array.

    Returns
    -------
    pearson : float, косинусное сходство

    '''   
    
    # числитель
    numirator = np.dot(x,y) 
    # знаменатель
    denumirator = np.linalg.norm(x) * np.linalg.norm(y)
    cos = numirator / denumirator
    return cos








# Создаем вектор x
x = np.arange(10, dtype=float)
# создаем вектор смещения
delta = np.arange(-10, 11)
# это еще не y. y далее мы будем получать как сумму вектора x и скаляра delta[i]


# создаем пустой массив для записи резултатов расчета коэффициента Пирсона и
# косинусового сходства
results = np.zeros((len(delta),2))

# запускаем цикл:
for i in range(len(delta)):
    y = x + delta[i]
    results[i,:] = pearson(x, y), cosin(x, y)
    



# Выводим результаты на график
fig = plt.figure()
fig.set_size_inches(12.0, 6.0)
fig.set_dpi(900)

plt.plot(delta, results[:, 0], 'k.', label = 'Pearson')
plt.plot(delta, results[:, 1], 'r', label = 'Cosin')
plt.legend()
plt.xlabel('Cмещение y относительно x')
plt.ylabel('Коэф. Пирсона или косинусово сходство')


# Для лучшего понимания выводим зависимость y от x для некоторых i
fig01 = plt.figure()
fig01.set_size_inches(12.0, 6.0)
fig01.set_dpi(900)

plt.plot(x, x + delta[0], 'k.', label = '-10')
plt.plot(x, x + delta[5], 'r*', label = '-5')
plt.plot(x, x + delta[7], 'gx', label = '-3')


plt.legend()
plt.xlabel('x')
plt.ylabel('y')




     