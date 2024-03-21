# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:33:13 2024

@author: sidorow
"""

import matplotlib.pyplot as plt
from Practice_03 import read_names_from_file
import random 


def plot_name_frequency (names, names_dataset, 
                         plot_name = 'Количество имен в списке' ):
    '''
    

    Parameters
    ----------
    names : list of strings, список интересующих нас имен.
    names_dataset : list of strings, весь список имен.
    plot_name : strung, имя графика, по умолчанию 'Количество имен в списке'.

    Returns
    -------
    Ничего не возвращает, просто рисует столбчатую диаграмму с обозначением
    количества выбранных имен в датасете

    '''
    
    
    
    x_data = names
    y_data = [names_dataset.count(item) for item in x_data]
    
    
       
    # создадим для этой диаграммы отдельную переменную типа рисунок
    fig03=plt.figure()
    # после этого мы можем настроить размер диаграммы (нирина и восота 
    # в дюймах)
    fig03.set_size_inches(9.0, 4.7)
    # ее разрешение
    fig03.set_dpi(600)
    # с помощью генератора случайных чисел сгенерим цвета для каждого 
    # из столбцов
    colors = []
    for _ in x_data:
        r= round(random.random(),3)
        g = round(random.random(),3)
        b = round(random.random(),3)
        colors.append([r, g, b])
    # после чего построим диаграмму (созда)
    plt.bar(x_data, y_data, color = colors)
    # повернем именя на оси x на 90 градусов
    plt.xticks(rotation=90)
    # добавим подписи осей
    plt.bar_label(plt.bar(x_data, y_data, color = colors), 
                  labels=y_data)
    # добавим пределы по оси y
    #plt.ylim(0, 30)
    # и имя диаграммы
    plt.title(plot_name) 
    



# Создадим список интересующих нас имен:
names_01 = ['COLIN', 'MARYETTA', 'PETER', 'MELLIE', 'IVAN', 
             'LEE', 'WONG', 'NATASHA', 'MARY']
# Создадим список имен из файла names_generated.txt:
names_dataset, _, _ = read_names_from_file("../data/", "names_generated.txt")

# запустим в работу функцию plot_name_frequency, которая построит 
plot_name_frequency(names_01, names_dataset)



def get_most_frequent_names (names_dataset, number_of_names, search_type = 'max'):
    '''
    

    Parameters
    ----------
    names_dataset : list of strings, весь список имен.
    number_of_names : количество имен, которые нужно вывести на график
    search_type : string, 'min' - если нужно вывести самые редкие имена,
                        'max' - если самые частые 

   
    Returns
    -------
    list of strings, список имен длиной = number_of_names

    '''
    
    
    
    #создадим множество имем (т.е. избавимся от повторений)
    names_set = set(names_dataset)
    # посчитаем сколько раз каждое из имен множества встречается в списке
    repeats = [names_dataset.count(item) for item in names_set]
    # создадим словарь, где ключ - имя, количество повторений - значение
    dict_frequensy = dict(zip(names_set, repeats))
    i=0
    dict_frequent = {}
    while i < number_of_names:# найдем самое часто встречающееся в данный момент имя:
        
        if search_type != 'max' and search_type != 'min':
            raise TypeError ('Параметр search_type задан неверно')
        
        
        else:    
            if search_type == 'max':
                # максимальное количество повторений
                frequent_value = max(list(dict_frequensy.values()))
            if search_type == 'min':
                # максимальное количество повторений
                frequent_value = min(list(dict_frequensy.values()))
        
           
        
        # индекс этого числа
        frequent_index = list(dict_frequensy.values()).index(frequent_value)
        # имя (т.е. ключ словаря)
        frequent_key = list(dict_frequensy.keys())[frequent_index]
        # добавляем в новый словарь найденную пару имя/число повторений
        dict_frequent [frequent_key] = frequent_value
        # удаляем это имя из словаря dict_frequensy
        dict_frequensy.pop(frequent_key)
        i+=1
    return list(dict_frequent.keys())


     

names_02 = get_most_frequent_names (names_dataset, 20, search_type = 'max')

plot_name_frequency(names_02, names_dataset)





























    


