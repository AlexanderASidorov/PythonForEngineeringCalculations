# -*- coding: utf-8 -*-

string_formula = ''

def polynome (x, *args):
    '''
    Расчет полинома произвольного порядка. Порядок полинома определяется 
    количеством коэффичиентов (аргументов *args)

    Parameters
    ----------
    x : float or integer, переменная полинома.
    *args : floats or integers, коэффициенты полиномов

    Returns
    -------
    coefs : list of floats, коэффициенты полиномов
    degrees : list of floats, степени полиномов
    f : float, значение функции при данном x.

    '''
    
    
    # создаем список из коэффициентов полинома    
    coefs = list(args)
    
    # проверка исходных данных функции
    for item in coefs:
        if not isinstance(item, (float, int)):
            raise TypeError ('Все коэффициенты полинома должны быть типа float или integer!!!')
    
    if not isinstance(x, (float, int)):
        raise TypeError ('Все переменная полинома должны быть типа float или integer!!!')
    
       
    
    
    # создаем список из степеной полинома
    degrees = [i for i, p in enumerate(coefs)]
    
    # в переменную f будем итерационно записывать сумму coefs[i]*(x**degrees[i])     
    
    f = 0
    
    for i in range (0, len(coefs)):
        f += coefs[i]*(x**degrees[i])
    
    return coefs, degrees, f

coefs, degrees, f = polynome(1, 4.5, 1.5, 3.1, 1, 1, 5.6)



def derivative (x, *args):
    '''
    Расчет производной полинома произволного порядка. Порядок полинома определяется 
    количеством коэффичиентов (аргументов *args) 

    Parameters
    ----------
    x : float or integer, переменная полинома
    *args : floats or integers, коэффициенты полиномов

    Returns
    -------
    derivative : float, значение проивзодной функции при данном x 

    '''
        
    
    coefs, degrees, f = polynome (x, *args)
    
    
    derivative = sum([coef*degree*(x**(degree-1)) for coef, degree in enumerate(coefs)])
    
    
    return  derivative



derivative_ = derivative (1, 4.5, 1.5, 3.1, 1.1, 1.2, 5.6)   
    


def derivative_rec (x, degree, *args):
    '''
    Рекурсивная функция расчета производной полинома произвольного порядка.

    Parameters
    ----------
    x : float or integer, переменная полинома
    degree : integer, степень полинома
    *args : floats or integers, коэффициенты полиномов

    Returns
    -------
    derivative : float, значение проивзодной функции при данном x 

    '''
    
    # создаем список из коэффициентов полинома    
    coefs = list(args)
    
    global string_formula
    
    
    # создаем список из коэффициентов полинома    
    coefs = list(args)
    
    # проверка исходных данных функции
    for item in coefs:
        if not isinstance(item, (float, int)):
            raise TypeError ('Все коэффициенты полинома должны быть типа float или integer!!!')
    
    if not isinstance(x, (float, int)):
        raise TypeError ('Все переменная полинома должны быть типа float или integer!!!')
        
          
     
    # задаем условие для выхода из рекурсии, удаляем последние 3 элемента строки: "_+_" и возвращаем 0
    if degree == -1:
        string_formula = string_formula[:-3]
        return 0
    
    
    # определяем формулу для рассчета производной полинома произвольной степени
    f = coefs[degree]*degree*x**(degree-1)
    
    # добавляем формулу производной полинома в строку string в строковом выражении
    if degree == 0:
        pass
    elif degree == 1:
        string_formula = str(coefs[degree]) + ' + ' + string_formula
    else:
        string_formula = str(coefs[degree]) + '*' + str(degree) + '*x^' + str(degree-1) + ' + ' + string_formula
    
    
    
    return f + derivative_rec(x, degree-1, *args)


derivative_rec_ = derivative_rec (1, 5 , 4.5, 1.5, 3.1, 1.1, 1.2, 5.6)  
    
    
    
    
    
    
    


































