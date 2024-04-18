# -*- coding: utf-8 -*-
#
#

import numpy as np
import matplotlib.pyplot as plt

'''
Допустим у нас есть выборка из какого-то количества людей и ам известны
рост и вес каждого человека. Допустим нам нужно определить к какой группе
относится человек согласно индекса массы его тела.
Подробнее об индексе массы тела:
    https://ru.wikipedia.org/wiki/Индекс_массы_тела


'''

#########################################################################
################## Исходные данные №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

# Для создания искусственной выборки воспользуемся генератором случайных
# чисел понятием медианный вес и медианный индекс массы тела
# медианный вес человека в выборке
weight_avrg = 90.0

# медианный индекс массы тела человека
mass_index_avrg = 28.0
# возможный разброс по индексу массы тела человека
mass_index_delta = 12

hight_avrg = 1.75

## количество людей в выборке
n_people = 1000


# пусть количетсво кластеров будет равно 3
k = 7
# количество итераций класстаризации - тоже 3
iteri = 7

#########################################################################


def generate_data (hight_avrg, mass_index_avrg, mass_index_delta, n_people, sigma=0.1):
    '''
    Генерация выборки из случайных чисел

    Parameters
    ----------
    hight_avrg : float, средний рост человека в выборке
    mass_index_avrg : float, средний индекс массы тела человека в выборке
    mass_index_delta : float, интервал варьирования индекса массы тела
    n_people : integer, количество людей в выборке
    sigma : float, дисперсия выборки

    Returns
    -------
    data : numpy array, 3 стоблбца: индекс массы тела, масса тела, рост человека

    '''
    
    
    
    
    
    # сгенерируем данные о росте человека
    hight = np.random.normal (hight_avrg, sigma, n_people)
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
    
    # объединим рост, вес и индекс в один массив с тремя столбцами
    data = np.array([mass_index, weight, hight]).transpose()
   
    return data
    
data =  generate_data (hight_avrg, mass_index_avrg, mass_index_delta, n_people, sigma=0.1)   
    
    





def plot_initial_data (hight, weight, mass_index):
    '''
    Визуализация данных для рост, масса, индекс массы

    Parameters
    ----------
    hight : 1-d numpy array
    weight : 1-d numpy array
    mass_index : 1-d numpy array

    Returns
    -------
    None.

    '''
    
    
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
    
    
plot_initial_data (data[:, 2], data[:, 1], data[:,0])






def k_means(data01, data02, k, iteri):
    '''
    Кластеризия данных методом к-средних

    Parameters
    ----------
    data01 : 1-d numpy array
    data02 : 1-d numpy array
    k : integer, количество кластеров
    iteri : integer, количество итераций кластеризации

    Returns
    -------
    groupidx : 1-d numpy array с номерами принадлежности

    '''
    
    
    data = np.array([data01, data02]).transpose()
    
    # выберем первый центр каждого из кластеров
    ridx = np.random.choice(range(len(data)), k, replace=False)
    centroids = data[ridx,:]
    # сортируем эти точки по массе от меньшей к большей
    centroids=centroids[centroids[:,0].argsort()]
    # далее мы будем измерять рассточние от каждой из точек до центроида.
    # для этого создадим переменную dist: количество строк - количество точек,
    # количество столбцов - количество кластеров
    dists = np.zeros([data.shape[0], k])
    
    
    for _ in range (iteri):
        
        for i in range(k):
            dists[:,i] = np.sum(((data-centroids[i,:])**2)**0.5, axis=1)
        
        # определяем к какой группе относится человек 
        groupidx = np.argmin(dists, axis=1)
        
        # пересчитываем центроид
        for j in range(k):
            centroids[j,:] = [ np.mean(data[groupidx==j,0]), np.mean(data[groupidx==j,1]) ]
            centroids=centroids[centroids[:,0].argsort()]
    return groupidx

      
# рост и масса   
groupidx01 = k_means(data[:, 1], data[:, 2],  k=7, iteri=70)       
# индекс массы тела и рост
groupidx02 = k_means(data[:, 0], data[:, 2],  k=7, iteri=70)          



def k_means_100_iterations (data01, data02, k):
    '''
    Кластеризия данных методом к-средних

    Parameters
    ----------
    data01 : 1-d numpy array
    data02 : 1-d numpy array
    k : integer, количество кластеров
    iteri : integer, количество итераций кластеризации

    Returns
    -------
    groupidx : 1-d numpy array с номерами принадлежности

    '''
    
    
    data = np.array([data01, data02]).transpose()
    
    # выберем первый центр каждого из кластеров
    ridx = np.random.choice(range(len(data)), k, replace=False)
    centroids = data[ridx,:]
    # сортируем эти точки по массе от меньшей к большей
    centroids=centroids[centroids[:,0].argsort()]
    # далее мы будем измерять рассточние от каждой из точек до центроида.
    # для этого создадим переменную dist: количество строк - количество точек,
    # количество столбцов - количество кластеров
    dists = np.zeros([data.shape[0], k])
    # переменная для подсчета количество точек в каждой из k групп
    number_of_points = np.zeros([100, k], int)
    
    
    for j in range (100):
        
        for i in range(k):
            dists[:,i] = np.sum(((data-centroids[i,:])**2)**0.5, axis=1)
            
        
        # определяем к какой группе относится человек 
        groupidx = np.argmin(dists, axis=1)
        # подсчитываем количество человек в каждой группе
        number_of_points[j, :] = np.array([np.count_nonzero(groupidx == i) for i in range (k)])
        # если количество не изменилось по сравнению с прошлой итерацией, значит
        # считаем, что можно прекращать кластеризацию
        if np.array_equal(number_of_points[j, :], number_of_points[j-1, :]):
            print (f'Количество людей в группах стабилизировалось за {j} итераций')
            break
           
            
        
        # если нет, то продолжаем
        else:
                    
            # пересчитываем центроид
            for j_ in range(k):
                centroids[j_,:] = [ np.mean(data[groupidx==j_,0]), np.mean(data[groupidx==j_,1]) ]
                centroids=centroids[centroids[:,0].argsort()]
            if j == 99:
                print ('Выполнено все 100 итерацийий')           
    return groupidx, number_of_points, j


# # рост и масса   
groupidx_01, _, _ = k_means_100_iterations(data[:, 1], data[:, 2],  k=7)       
# # индекс массы тела и рост
groupidx_02, _, _ = k_means_100_iterations(data[:, 0], data[:, 2],  k=7)  




def plot_clustering_results (data01, data02, groupidx, 
                             xlabel, ylabel, title):
    '''
    Визуализация результатов кластеризации

    Parameters
    ----------
    data01 : 1-d numpy array
    data02 : 1-d numpy array
    groupidx : 1-d numpy array с номерами принадлежности
    
    xlabel, ylabel, title : string, название осей y и x и общее название
                            графика

    Returns
    -------
    None.

    '''
    
    
    
    
    data = np.array([data01, data02]).transpose()
    
    # Выводим результаты на графики
    # строим график состоящий и 4 отдельных ячеек: 2 колонки и 2 столбца
    fig02, ax = plt.subplots(nrows=1, ncols=1, sharex=True)
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


    # # строим график рост человека от его массы
    # ax[0].plot(data[:, 0],data[:, 1], 'ko', markerfacecolor='w')
    # ax[0].set_ylabel(ylabel)
    # ax[0].set_title(title + ' в выбррке из ' + str(n_people) + ' человек' )

    # строим график рост человека от его массы
    colours = [ "red", "blue", "green", "yellow", "purple", "orange", "grey" ]
    labels = ['Дифицит', 'Недостаток', 'Норма', 'Избыток', 'Степень 1', 'Степень 2', 'Степень 3']


    for i in range (k):
        ax.plot(data[groupidx==i][:, 0], data[groupidx==i][:, 1],'ko', markerfacecolor=colours[i], label = labels[i])
        
    
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title + ' в выборке из ' + str(n_people) + ' человек' )
    ax.legend(loc="upper left")


        

plot_clustering_results (data[:, 0], data[:, 2], groupidx_02, 
                        'Индекс массы тела', 'Рост человека, м', 
                        'Рост и индекс массы тела человека')

plot_clustering_results (data[:, 1], data[:, 2], groupidx_01, 
                        'Масса человека, кг', 'Рост человека, м', 
                        'Индекс массы тела и рост')






