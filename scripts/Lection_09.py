# -*- coding: utf-8 -*-
#
# Библиотека NumPy (продолжение лекции #8). Кластеризация данных.

import numpy as np
import matplotlib.pyplot as plt

'''
Допустим у нас есть выборка из какого-то количества людей и ам известны
рост и вес каждого человека. Допустим нам нужно определить к какой группе
относится человек согласно индекса массы его тела.
Подробнее об индексе массы тела:
    https://ru.wikipedia.org/wiki/Индекс_массы_тела


'''



# Для создания искусственной выборки воспользуемся генератором случайных
# чисел понятием медианный вес и медианный индекс массы тела
# медианный вес человека в выборке
weight_avrg = 90.0

# медианный индекс массы тела человека
mass_index_avrg = 28.0
# возможный разброс по индексу массы тела человека
mass_index_delta = 12

high_avrg = 1.75



## количество людей в выборке
n_people = 1000

# сгенерируем данные о росте человека
hight = np.random.normal (high_avrg, 0.1, n_people)
print(f' самый высокий человек в выборке - {np.max(hight)}')
print(f' самый низкий человек в выборке - {np.min(hight)}')
print(f' средний рост людей в выборке - {np.mean(hight)}')

# сгенерируем данные об индексе массы тела
mass_index = mass_index_avrg + np.random.uniform(-1, 1, n_people)*mass_index_delta
# на основе массы тела и индекса тела расчитаем массу каждого человека
weight = mass_index*(hight)**2
print(f' самый грузный человек в выборке - {np.max(weight)}')
print(f' самый легкий человек в выборке - {np.min(weight)}')
print(f' средний вес людей в выборке - {np.mean(weight)}')


# Выводим результаты на графики
# строим график состоящий и 4 отдельных ячеек: 2 колонки и 2 столбца
fig01, ax = plt.subplots(nrows=3, ncols=1, sharex=False)
# устанавливаем размер картинки
fig01.set_size_inches(9.0, 12.0)
# ее разрешение
fig01.set_dpi(900)
plt.subplots_adjust(left=None,
                    bottom=None, 
                    right=None, 
                    top=None, 
                    wspace=None, 
                    hspace=0.5)




# строим график рост человека от его массы
ax[0].plot(weight, hight, 'ko', markerfacecolor='w')
ax[0].set_ylabel('Рост человека, м')
ax[0].set_xlabel('Масса человека, кг')
ax[0].set_title('Рост и масса тела человека в выбррке из ' + str(n_people) + ' человек' )

# строим график рост человека от его индекса массы тела
ax[1].plot(mass_index, hight, 'ko', markerfacecolor='w')
ax[1].set_ylabel('Рост человека, м')
ax[1].set_xlabel('Индекс массы тела')
ax[1].set_title('Рост и индекс массы тела человека в выбррке из ' + str(n_people) + ' человек' )

# строим график индекс массы тела человека от его массы тела
ax[2].plot(weight, mass_index, 'ko', markerfacecolor='w')
ax[2].set_ylabel('Индекс массы тела человека')
ax[2].set_xlabel('Масса человека, кг')
ax[2].set_title('Индекс массы тела человека и его масса в выбррке из ' + str(n_people) + ' человек' )

# объединим рост и вес в один массив с двумя столбцами
data = np.array([weight, hight]).transpose()

# пусть количетсво кластеров будет равно 3
k = 7
# количество итераций класстаризации - тоже 3
iteri = 70

for _ in range(iteri):
    # выберем первый центр каждого из трех кластеров
    ridx = np.random.choice(range(len(data)), k, replace=False)
    centroids = data[ridx,:]
    # сортируем эти точки по массе от меньшей к большей
    centroids=centroids[centroids[:,0].argsort()]
   


    # далее мы будем измерять рассточние от каждой из точек до центроида.
    # для этого создадим переменную dist: количество строк - количество точек,
    # количество столбцов - количество кластеров
    dists = np.zeros((data.shape[0], k))
    for i in range(k):
        dists[:,i] = np.sum(((data-centroids[i,:])**2)**0.5, axis=1)

    # определяем к какой группе относится человек 
    groupidx = np.argmin(dists, axis=1)

    # пересчитываем центроид
    for j in range(k):
        centroids[j,:] = [ np.mean(data[groupidx==j,0]), np.mean(data[groupidx==j,1]) ]
        
        
# Выводим результаты на графики
# строим график состоящий и 4 отдельных ячеек: 2 колонки и 2 столбца
fig02, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
# устанавливаем размер картинки
fig02.set_size_inches(12.0, 9.0)
# ее разрешение
fig02.set_dpi(900)
plt.subplots_adjust(left=None,
                    bottom=None, 
                    right=None, 
                    top=None, 
                    wspace=None, 
                    hspace=0.2)


# строим график рост человека от его массы
ax[0].plot(weight, hight, 'ko', markerfacecolor='w')
ax[0].set_ylabel('Рост человека, м')
ax[0].set_title('Рост и масса тела человека в выбррке из ' + str(n_people) + ' человек' )

# строим график рост человека от его массы
colours = [ "red", "blue", "green", "yellow", "purple", "orange", "grey" ]
labels = ['Дифицит', 'Недостаток', 'Норма', 'Избыток', 'Степень 1', 'Степень 2', 'Степень 3']


for i in range (k):
    ax[1].plot(data[groupidx==i][:, 0], data[groupidx==i][:, 1],'ko', markerfacecolor=colours[i], label = labels[i])
    
ax[1].plot(centroids[:, 0], centroids[:, 1], 'kX')
ax[1].set_ylabel('Рост человека, м')
ax[1].set_xlabel('Масса человека, кг')
ax[1].set_title('Рост и масса тела человека в выбррке из ' + str(n_people) + ' человек' )
ax[1].legend(loc="upper left")





