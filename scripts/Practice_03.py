# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:53:49 2024

@author: sidorow
"""


'''
Задача: скачать из папки 
https://github.com/AlexanderASidorov/PythonForEngineeringCalculations/tree/main/data
файл names_with_duplicates.txt
и с помощью множества удалить все повторения
посчитать уникальное количестве имен 

'''


def read_names_from_file (path, filename):
    '''
    1. Считывает текстовый файл с именами
    2. Создает из них список
    3. Из каждого имени удаляет символы, не являющиеся буквами
    

    Parameters
    ----------
    path : string, путь к файлу
    filename : string, имя файла.

    Returns
    -------
    Список имен с дубликатами, множетсво имен и список имен без дубликатов 

    '''
    
    
    filepath = path + filename
    with open (filepath) as myfile:
        for names in myfile:
            names = names.split(",") # принимаем , в качастве разделителя
    
    names_temp = []        
    for item in names:
        item_temp = ''.join([ char if char.isalnum() 
                             else "" for char in item ])
        item = item_temp
        names_temp.append(item)
    names = names_temp
    print ('В списке ' + str(len(set(names))) + ' уникальных имен.')
    return names, set(names), list(set(names))        

        
   
_, _, names = read_names_from_file("../data/", "names_with_duplicates.txt")


#%%
'''
1. Найти все Пифагоровы тройки чисел меньше 100.
2. Найти все "примитивные" Пифагоровы тройки (т.е. все числа тройки являются 
взаимно простыми (не имеют общего делителя)) 
'''



def get_pythagorean_triplet_01 (max_c):
    '''
    Поиск Пифагоровых троек, в том числе имеющих общий делитель

    Parameters
    ----------
    max_c : integer, максимальное число.

    Returns
    -------
    pythagorean_triplet_list : list of lists of integers

    '''
    
    
    # создаем список, куда будем записывать найденные Пифагоровы тройки
    pythagorean_triplet_list = []
    
    # обозначим числа Пифагоровой тройки как a, b и с
    # a - минимальное числе, b - среднее, c - максимальное
    
    
    for a in range(1, int(max_c)): # a будем искать в диапазоне от 1 до max_c
        for b in range(2, int(max_c)): # b будем искать в диапазоне от 2 до max_c
                                        # 2, т.к. b>a
            c = (a**2+b**2)**0.5 # c - квадратный корень от суммы a и b
            if c% 1 >0 or c > max_c: # проверяем, что c - целое число, т.е.
                            # делится на 1 без остатка и что c < max_c
                pass # если одно из условий выполняется, то ничего не делаем 
            else: # если ни одно из условий не выполнилось, то проверяем, что
                # a < b < c и что a**2 + b**2 == c**2
                if a < b < c: 
                    # если все так, что мы нашли Пифагорову тройку и можем
                    # добавить ее в список, которой потом выведем в окно 
                    # переменных
                    pythagorean_triplet_list.append([a, b, c])
                else: pass
    return pythagorean_triplet_list 
        
    
triplet_list_01 = get_pythagorean_triplet_01 (100)


def get_pythagorean_triplet_02 (max_c):
    
    '''
    Поиск примитивных Пифагоровых троек

    Parameters
    ----------
    max_c : integer, максимальное число.

    Returns
    -------
    pythagorean_triplet_list : list of lists of integers

    '''
       
    
    pythagorean_triplet_list = []
    
    for a in range(1, int(max_c)):
        for b in range(2, int(max_c)):
            c = (a**2+b**2)**0.5
            if c% 1 >0 or c > max_c:
                pass
            
            else:
                if a < b < c:
                    
                    #####################################################
                    #####################################################
                    # часть, которую мы добавили, по сравнению с предыдущей функцией
                    # если все так, что мы нашли Пифагорову тройку, но нам
                    # надо проверить, что она не имеет общего делителя, кроме 1.
                    j=0
                    for i in range(2, a): # i - в данном случае делитель
                                        # мы ищем есть ли такое число в диапазоне от
                                        # 2 до a, на которое все три числа делятся
                                        # без отсатка
                        if a%i==0 and b%i==0 and c%i==0:
                           j+=1
                        
                    if j>0:
                        pass
                    #######################################################
                    #######################################################
                    else:
                       pythagorean_triplet_list.append([a, b, c])

                else: pass
            
    return pythagorean_triplet_list 
        
    
triplet_list_02 = get_pythagorean_triplet_02 (100)














