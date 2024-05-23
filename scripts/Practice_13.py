# -*- coding: utf-8 -*-
"""
Created on Thu May 23 13:34:11 2024

@author: sidorow
"""

import numpy as np
from scipy.optimize import fsolve


# исходные данные.
# более подробно смотрите в pdf файле:
# https://github.com/AlexanderASidorov/PythonForEngineeringCalculations/blob/main/notes/Practice_13.pdf
t50 = 47.86
ts1 = 3.375
ts2 = 14.5
te = 324.99


# базовое уравнение Аврами будет включать в себя дополнительную функцию,
# расчет экспоненциальной части:


def exp (t, b, n):
    '''
    Эксплоненциальная часть уравнения Аврами

    Parameters
    ----------
    t : float of iterable, время.
    b : float, коэффициент b.
    n : float, коэффициент n.

    Returns
    -------
    numpy array of floats

    '''
               
    return np.exp((-1/b)*(t**n))


# расчитаем отрезки по времени, которые на понадобятся для решения системы
# уравнений:


def convert_times (ts1, ts2, t50, te):
    '''
    

    Parameters
    ----------
    ts1,  ts2, t50, te : float.

    Returns
    -------
    times : dict, словарь со значениями отрезков времени

    '''
         
    
    
    times = {}
    
    times['t051'] = t50 - ts1
    times['t052'] = t50 - ts2
    times['t12'] = te - ts2
    times['t11'] = te - ts1
    times['t_delta'] = ts2 - ts1
    
    return times


def log_times (time_dict):
    '''
    Логарифмирование отрезков врением, для более простого нахождения решения

    Parameters
    ----------
    time_dict : dict, словарь со значениями отрезков времени

    Returns
    -------
    time_dict : dict, словарь со значениями логарифмированных отрезков времени

    '''
    
    for key, value in time_dict.items():
        time_dict[key] = np.log10(value)
        
    return time_dict


# далее мы на вход функции log_times подаем функцию convert_times 
times = log_times(convert_times(ts1, ts2, t50, te))


# составляем систему уравнений:
    # уравнение 01 - сумма объемной лоли дочерних фаз в момент времени t05 равна 0.5
    # уравнение 02- сумма объемной лоли дочерних фаз в момент времени te равна 1.0
    # уравнение 03 - разность объемной доли дочерних фаз в момент времени te равно 
                    # объемной доле x1 в момент времени ts2
    # если n2 = None, то принимаем, что n1=n2. Если n2 - задано, то n1 расчитывается
    # как независимая переменная, а n2 не расчитывается совсем.


def system2solve(x, times, n2 = None, ):
    '''
    Система уравнений для поиска констант уравнения Аврами при извествных 
    времени начала образования первой и второй фаз, времени перехода 50% объема 
    материала в дочерние фазы и время окончания обоих фазовых превращений.

    Parameters
    ----------
    x : list of floats, [b1, b2, n1]
    times: dict, с отрезками времени
    n2 : float, но None по умолчанию.

    Returns
    -------
    system : система их трех уравнений. При правильно подобранных коэффициента
            все три уравнения должны возвращать ноль.

    '''
    
    
    
    if n2 == None:
        b1, b2, n1 = x
        n2 = n1
    else:
        b1, b2, n1 = x
        
   
    
    equation_01 = (1-exp(times['t051'], b1, n1)) + (1- exp(times['t052'], b2, n2)) - 0.5 
    equation_02 = (1 - exp(times['t11'], b1, n1)) +(1 - exp(times['t12'], b2, n2)) - 1
    equation_03 = exp(times['t11'], b1, n1) -  exp(times['t12'], b2, n2) - exp(times['t_delta'], b1, n1) + 1
    
    system = [equation_01, equation_02, equation_03]
    
    return system


def find_roots_iteratively (function, initial_guess, number_of_iterations, times, n2 = None):
    '''
    

    Parameters
    ----------
    function : функция, для которой мы ищем корни.
    initial_guess : list of floats, .
    number_of_iterations : максимальное количество итераций.
    times : dict, с отрезками времени.
    n2 : float, но None по умолчанию.

    Returns
    -------
    roots : list с корнями уравнения
    check_result : список [True, True, True] если все уравнения принимают 0, т.е.
                    корни найдены верно.

    '''
       
    
    
    j = 0
    
    while j <= number_of_iterations: # запускаем цикл 
        # находим корни и проверяем их на предмет близости обеих уравнений 
        # функции avrami_system к нуля
        roots = fsolve(function, initial_guess, args = (times, n2))
        check_result = np.isclose(function(roots, times ,n2), [0.0, 0.0, 0.0])
        if all (item == True for item in check_result) and 1 <= roots[2] <= 4:
            break # если условие выполняется, то цикл прерываем
        else: # если нет, то увеличиваем начальное приближение коэффициента b в 10 раз
            initial_guess = [initial_guess[0]*2, initial_guess[1]*2, 3]
            print(initial_guess)
            j +=1
    return roots, check_result


roots, check_result = find_roots_iteratively (system2solve, [1.0, 1.0, 3], 100, times,  n2=3)


        
        
































