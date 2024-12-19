#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Поиск Пифагоровых троек

import time

def get_abc (n, m):
    '''
    Расчет a и b по заданным n и m

    Parameters
    ----------
    n : integer
    m : integer
   
    Returns
    -------
    a : integer
    b : integer
    c : integer

    '''
    
    for item in [n, m]:
        if not isinstance(item, int):
            raise TypeError ('m и n должны быть переменными типа integer')
    if not m>n:
        raise ValueError ('m должно быть больше n')
    
    # базовые формулы для расчета a, b и c
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    
    return a, b, c


def get_n_max (c):
    '''
    Расчет максимального значения n производится из следующих соображений:
        a = m**2 - n**2     
        b = 2*m*n
        c = m**2 + n**2
        
        третье уравнение записываем в виде:
        m**2 = c - n**2 или m = (c - n**2)**0.5
        таким образом систему можно переписать в виде:
        a = c - 2n**2
        b = 2n*(c - n**2)**0.5
        
        т.к. a > 0, можно сделать вывод, что c - 2n**2 > 0
        откуда можно, в свою очередь, сделать вывод, что n < (c/2)**0.5
        
    Parameters
    ----------
    c : integer

    Returns
    -------
    n : integer

    '''
    
    
    if not isinstance(c, int) and not c>0:
        raise TypeError ('c должна быть переменной типа integer больше 0')
        
    n_max = int((c/2)**0.5)
    return n_max





def get_n_m (n_max, c):
    '''
    Ищем значения m и n, которые позволяют по формулам, описанным в функции
    get_abc получить получить все Пифагоровы тройки для заданного c  

    Parameters
    ----------
    n : integer
    c : integer

    Returns
    -------
    list_n : list of integers, список значений n.
    list_m : list of integers, список значений m.

    '''
    n = n_max
    
    for item in [n, c]:
        if not isinstance(item, int):
            raise TypeError ('c и n должны быть переменными типа integer')
    if not c>n:
        raise ValueError ('c должно быть больше n')
    
    
    list_n = [] 
    list_m = []
         
    while n >= 1:
        # расчитываем m для n
        m = (c-n**2)**0.5
        # на всякий случай m конвертируем во float
        m = float(m)
        # проверяем, что m > n и что m - целое число
        if not m%1 == 0 or not m>n:
            # если нет, то уменьшаем n на единицу и пытаемся еще раз посчитать m
            n-=1   
        else:
            # если да, то проверяем, что n**2 + m**2 = c 
            if n**2 + m**2 == c:
                # если да, то m конвертируем в int
                m = int(m)
                # и цикл прерываем
    
            # проверяем, что m типа int
            if isinstance(m, int):
                # если да, то проверяем, что n и m не имеют общего делителя
                status_denoninator = check_n_m (n, m)
                if not status_denoninator:
                    status = True
                else:
                    status = False
                    n -= 1
              
                # если тест пройден, то добавляем n и m в список
                if status == True:
                    list_n.append(n)
                    list_m.append(m)
                    n -= 1
    
    return list_n, list_m


def check_n_m (n, m):
    '''
    Проверка, что n и m не имеют общего делителя

    Parameters
    ----------
    n : integer.
    m : integer.

    Returns
    -------
    status : True of False.

    '''
   
    for item in [n, m]:
        if not isinstance(item, (int)):
            raise TypeError ('m и n должны быть переменными типа integer')
    if not m>n:
        raise ValueError ('m должно быть больше n')
    status = False
    
    for item in range (2, n+1):
        if m%item == 0 and n%item == 0:
            status = True
            break
    return status


def check_a_b_c (a, b, c):
    '''
    Проверка a, b и c на наличие общего делителя

    Parameters
    ----------
    a : integer.
    b : integer.
    c : integer.

   
    Returns
    -------
    status : True of False.

    '''
    
    for item in [a, b, c]:
        if not isinstance(item, int):
            raise TypeError ('a, b и с должны быть переменными типа integer')
    
    if not a<b<c:
        list_a_b_c = [a, b, c]
        list_a_b_c.sort()
        a, b, c = list_a_b_c[0], list_a_b_c[1], list_a_b_c[2]

    status = False
    
    for item in range (2, a+1):
        if a%item == 0 and b%item == 0 and c%item ==0:
            status = True
            break
    return status



def get_triplet ():
    '''
    Поиск Пифагоровых троект:
        1. итерационное уменьшение глобальной переменной C
        2. запись Пифагоровой тройки в глобальную переменную triplets
 
    Returns
    -------
    None.

    '''
      
    global c
    global triplets
    
    
    if not isinstance(c, int):
        raise TypeError ('m и n должны быть переменными типа integer')
       
    while c > 3:
        #print (c)
        n_max = get_n_max(c)
        list_n, list_m = get_n_m(n_max, c)
        if len(list_n) == 0:
            c-=1
        
        else:
            for i in range (0, len(list_n)):
                a, b, c = get_abc(list_n[i], list_m[i])
                status = check_a_b_c(a, b, c)
                #status = False
                if not status:
                    triplets.append([a, b, c])
                else:
                    pass
            c-=1
 

               
start_time = time.time()
c = 100000
triplets =[]
a_b_c = get_triplet()
end_time = time.time()
print(end_time - start_time)


#%%
# вариант Магомедкади Алиева (он лучше)

import math

def simple(a, b):
    while b:
        a, b = b, a % b
    return a

a = simple (10, 5)



def Pifagorov_3(z):
    troiki = []

    # Используем формулу Евклида: a = m^2 - n^2, b = 2mn, c = m^2 + n^2
    for m in range(2, int(math.sqrt(z)) + 1):
        for n in range(1, m):

            # m и n должны быть взаимно простыми и нечетно-чётной парой
            if (m - n) % 2 == 1 and simple(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2

                if c > z:
                    break

                troiki.append((a, b, c))

    # Упорядочим a, b, c так, чтобы a < b < c
    troiki = [tuple(sorted(triple)) for triple in troiki]

    return sorted(troiki)

troiki = Pifagorov_3(100000)
#print(Pifagorov_3(100000))












    
    
        
        
    
    
        
    
    




            