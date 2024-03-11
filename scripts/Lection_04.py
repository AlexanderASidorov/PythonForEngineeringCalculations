# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:59:20 2022

@author: sidorow
"""


# 1. ФУНКЦИИ в Python (продолжение)


#%%    ФУНКЦИИ в Python
"""
Функция в Python Это просто часть программы, которую вы можете 
периодически, когда вам это нужно, вызывать, определяя в качестве 
исходных данных для нее некоторые исходные параметры (какие-то 
переменные, другие функци и т.д.) и получая в качестве результата 
ее работы какие-то другие параметры (например, какие-то другие переменные).
Функция внутри тела программы определяется следующим образом:
  Ключевое слово def говорит о том, что мы начали определять функцию;
  На этой же строке мы определяем имя функции, с помощью которого 
  далее будем эту функцию вызывать;
  далее в скобках мы указываем исходные переменные, которые 
  будет необходимо этой функции сообщить;
  после чего ставим двоеточие, что означает, что далее мы 
  начинаем записывать команды, которые эта функция будет выполнять.
  после того, как мы нужные команды записали, ключевым словом return мы
  определяем какие переменные мы в результате действия функции получим.
"""
# Пример простейшей функции: извлечение кубического корня из суммы трех чисел
def simplefunction (a, b, c):
    '''
    Кубический корень из произведения трех чисел

    Parameters
    ----------
    a : float or integer, число #1
    b : float or integer, число #2
    c : float or integer, число #3

    Returns
    -------
    float, корень кубический их произведениея трех чисел

    '''
    
    return (a+b+c)**(1/3)




# Пример простейшей функции, но с параметрами по-умолчанию

def calculate_sum_of_3_numbers_and_power (a, b, c, d=1/3):
    '''
    Возведение в степень суммы

    Parameters
    ----------
    a : float or integer, число #1
    b : float or integer, число #2
    c : float or integer, число #3
    d : float or integer, показатель степени

    Returns
    -------
    float
    '''
    return (a+b+c)**(d)


cube_root = calculate_sum_of_3_numbers_and_power (4, 2, 2)
square_root_01 = calculate_sum_of_3_numbers_and_power (4, 2, 2, 1/2)
square_root_02 = calculate_sum_of_3_numbers_and_power (d=1/2, b=2, a=4, c=2)





def calculate_names_by_first_letter (names, first_letter):
    '''
    функция для создания списка имен, начинающихся на определенную букву

    Parameters
    ----------
    names : list of strings, список имен без дублирования.
    first_letter : string, первая буква в имени.

    Returns
    -------
    sum_names_with_first_tetter : integer, количество имен, начинающихся на 
                                выбранную букву
        
    list_of_names_with_first_letter : list of strings, список имен, 
                                    начинаюихся на выбранную букву

    '''
    
    
    sum_names_with_first_tetter = 0
    list_of_names_with_first_letter = []
    for item in names:
        name = list(item)
        if name[0] == first_letter:
            sum_names_with_first_tetter +=1 
            list_of_names_with_first_letter.append(item)
        else: pass
    return sum_names_with_first_tetter, list_of_names_with_first_letter


names_no_duplicates = ['Anna', 'Alina', 'Boris', 'Victor', 'Colin', 'Svetlana',
                       'John', 'Jacob', 'David', 'Ivan', 'Wong', 'Irina',
                       'Bredly', 'Konsantin', 'Cyrill', 'Ravshan', 'Yao', 'Many']

sum_, list_ = calculate_names_by_first_letter (names_no_duplicates, 'C')








# Пример простейшей функции, но с произвольным количеством входных параметров
def calculate_sum_of_numbers_and_power (*args, d=1/3):
    '''
    Возведение в степень суммы

    Parameters
    ----------
    *args : floats or integers
    
    d : float or integer, показатель степени

    Returns
    -------
    float
    '''
    sum_=sum(args)
    
    
    
    return sum_**(d)

list_=[2, 2, 3, 2]

square_root_03 = calculate_sum_of_numbers_and_power (*list_, d=1/2)





# пример простейшей функции, но с произволным количеством входных переметров в
# виде ключ-значение (в виде словаря, другими словами):
import math
    
def calculate_martensite_hardness(phi700, **kwargs):
    """
    Martensite Vickers hardness empirical equation
    (Maynier et al.)
    """
    comp = kwargs
        

        
    C = comp.get('C', 0)
    Mn = comp.get('Mn', 0)
    Si = comp.get('Si', 0)
    Ni = comp.get('Ni', 0)
    Cr = comp.get('Cr', 0)
    Mo = comp.get('Mo', 0)
    V = comp.get('V', 0)
        
    Hv_martensite = (127 + 949*C + 27*Si + 11*Mn + 8*Ni + 16*Cr + 21*math.log10(phi700*3600))
    
    return Hv_martensite

composition = {'GrainSize': 6.0, 'C': 0.28, 'Mn': 0.8, 'Si': 0.9, 'Ni': 0.2, 
               'Cr': 0.8, 'Mo': 0.0, 'W': 0.0, 'As': 0.0, 'V': 0.0, 'Cu': 0.0}


Hv_martensite_01 = calculate_martensite_hardness(5.0, **composition)

# в вункции в зависимости от тех или иных условий может быть несколько return

def calculate_hardness(phi700, **kwargs):
    """
    Martensite Vickers hardness empirical equation
    (Maynier et al.)
    """
         
    comp = kwargs
        

        
    C = comp.get('C', 0)
    Mn = comp.get('Mn', 0)
    Si = comp.get('Si', 0)
    Ni = comp.get('Ni', 0)
    Cr = comp.get('Cr', 0)
    Mo = comp.get('Mo', 0)
    V = comp.get('V', 0)
        
    if phi700 < 1:
        Hv_ferrite_pearlite = (42 + 223*C + 53*Si + 30*Mn + 12.6*Ni + 7*Cr + 19*Mo + \
                (10 - 19*Si + 4*Ni + 8*Cr + 130*V)*math.log10(phi700*3600))
        return Hv_ferrite_pearlite
        
    else:
        Hv_martensite = (127 + 949*C + 27*Si + 11*Mn + 8*Ni + 16*Cr + 21*math.log10(phi700*3600))
    
        return Hv_martensite

Hv_steel_01 = calculate_hardness(1.1, **composition)

# %% Функция высшего порядка - принимают одну или более функций 
# в качестве аргументов и возвращают функцию в качестве результата.
import math


def high_order_function (x, function):
    
    return function(x)





def function_01 (x):
    return x*2

def function_02 (x):
    return x**2

def function_03 (x):
    return x**x

def function_04(x):
    return math.sin(x)




high_order= high_order_function ((math.pi)/4, function_04)


#%%
# Рекурсивная функция - функция, ссылающаяся сама на себя:
# Ниже две функции, вычисления факториала числа. Факториал - 
# произведение всех положительных натуральных чисел меньше или равно 
# числу n

def factorial (n):
    '''
    Расчет факториала числа n

    Parameters
    ----------
    n : integer.

    Returns
    -------
    product : integer, факториал числа n.

    '''
    n=int(n) # округляем число до integer, если оно не таково
    
    product = 1 
    while n > 0:
        product = product*n
        n=n-1
    return product

factorial_4 = factorial(4.99)

# то же самое, но через рекурсивную функцию:
    
def factorial_rec (n):
    '''
    Расчет факториала числе n через рекурсию

    Parameters
    ----------
    n : integer.

    Returns
    -------
    product : integer, факториал числа n.

    '''
    n=int(n) # округляем число до integer, если оно не таково
    
    if n==0:
        return 1
    product = n*factorial_rec(n-1)
    print('n = ' + str(n) + '; ' + 'product = ' + str(product))
    return product


factorial_4_rec = factorial_rec(4.99) 



#%% Анонимная функция (Лямбда-функция) - коротакая функция, которую можно 
# определить с помощью оператора lambda, не давая ей название.

def factorial_with_lambda (n):
    '''
    Расчет факториала числа n с его округлением в большую сторону

    Parameters
    ----------
    n : float of integer.

    Returns
    -------
    product : integer, факториал числа n.

    '''
    if n%1 == 0:
        pass
    else: 
        lambda_n = lambda x:  x//1+1 # округляем число до integer 
                                     # в большую сторону, если оно не таково
        n = lambda_n(n)
        
    
    product = 1 
    
    while n > 0:
        product = product*n
        n=n-1
    return product

factorial_4 = factorial_with_lambda(4.99)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
















