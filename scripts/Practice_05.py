'''
Найти все "примитивные" Пифагоровы тройки (т.е. все числа a, b и с 
являются взаимно простыми (не имеют общего делителя)) где максимальное 
число = 100. Сделать это необходимо с помощью трех функций:

    
1. Проверка a и b на принадлежность ко множетсву натуральных чисел и 
определение с, с аналогичной проверкой с.

2. Проверка на то, что a, b и с не имеют общего делителя отличного от 1.

3. Поиск троек и запись их в список.

'''

def get_c (a, b):
    '''
    Проверяем, что a<b, рассчитываем c и проверяем, что оно целое число.
    Если все условия выполнены, то возвращаем с.
    Если нет, то возвращаем None

    Parameters
    ----------
    a : integer, число a.
    b : integer, число b.

    Returns
    -------
    c : integer or None, число c.

    '''
    # проверяем, что a и b - переменные целочисленного типа
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError ('a и b должны быть целыми числами типа int')
    
    # проверяем, что a не равно b    
    if a == b:
        return None
    # на случай, если b<a
    elif  a>b: 
        return None
    else:
           
        c = (a**2+b**2)**0.5
    
        if c>b>a and c%1 == 0:
            return int(c)
        else:
            return None


#c = get_c(a=3, b=4)
#c  = get_c(a=2, b=4)
# test_03 = get_c (a=3, b=4)
# test_04 = get_c ('три', 'четыре')
# test_05 = get_c(a=2.2, b=4.3)


def check_for_common_devider (a, b, c):
    '''
    Проверяем, что a<b<c и что все три числа являются натуральными
    Если нет, то функция возвращает False
    Далее прверяем, что все три числа не имеют общего делителя. Если
    имеют, то функция возвращает False
    Если не имею, то то функция возвращает True

    Parameters
    ----------
    a : integer, число a.
    b : integer, число b.
    c : integer, число c.

    Returns
    -------
    True - если все три числа натуральные и не имеют общего делителя
    False - если нет

    '''
    
    for item in [a, b, c]:
        if not isinstance(item, int):
            raise ValueError ('все переменные должны быть целыми числами типа int')
            
    if not c>b>a:
        raise ValueError ('число c должно быть больше числа b, а число b должно быть больше числа a')
        
    # проверяем, что числа не имеют общего делителя:
    for i in range(2, a):
        if a%i==0 and b%i==0 and c%i==0:
            return False
            break
    return True
   
   
#test_01 =  check_for_common_devider (15, 20, 25)           
# test_02 =  check_for_common_devider (3.2, 4, 5)
# test_03 =   check_for_common_devider (6, 8, 10)
#test_04 = check_for_common_devider (10, 72, 98)



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
    
    if not isinstance(max_c, int):
        raise TypeError ('Переменная max_c должна быть целым числом типа int')
        
    
    pythagorean_triplet_list = []
    
    for a in range(1, max_c):
        for b in range(2, max_c):
            if b<=a:
                pass
            else:
                c = get_c(a, b) # используем функцию get_c
                if c == None or c>max_c: #проверяем, что функция get_c не 
                                    # вернула нам None или число большее max_c 
                    pass # ничего не делаем, если хоть одно из условий выполнилось
            
                else: # если не выполнилось, то с помощью функции check_for_common_devider
                    # проверяем, что a b c не имеют общего делителя отличного от 1
                    common_devider_passed = check_for_common_devider(a, b, c)
                    if common_devider_passed == False:
                        pass
                    else:
                        pythagorean_triplet_list.append([a, b, c])

                            
    return pythagorean_triplet_list 
        
    
triplet_list_02 = get_pythagorean_triplet_02 (100)








