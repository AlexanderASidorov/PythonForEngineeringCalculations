# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
"""
Продолжение того, что было на лекции #6:
Построим график изменения населения Индии, Китая, России и США, объединав
это все в один график.
Данные из Википедии:
"""


China = {'1990': 1135185000, '1995': 1204855000 , '2000': 1262645000, 
         '2005': 1303720000 , '2010': 1337705000, '2015': 1379860000, 
         '2020': 1411100000}

India = {'1990': 870452000 , '1995': 964279000 , '2000': 1059634000, 
         '2005': 1154639000 , '2010': 1240614000, '2015': 1322866505, 
         '2020': 1396387127}


Russia = {'1990': 147665081, '1995': 148459937 , '2000': 146890128, 
         '2005': 143474219	 , '2010': 142856536, '2015': 146267288, 
         '2020': 146748590}

USA = {'1990': 249623000, '1995': 266278000 , '2000': 282172000, 
         '2005': 295753000	 , '2010': 309330000, '2015': 321442000, 
         '2020': 331449281}
 

# Преобразуем значения в милионы человек:   
for country in [India, USA, China, Russia]:
    for item in country:
        country[item] = round(float(country[item]/1000000), 0)   


# строим график состоящий и 4 отдельных ячеек: 2 колонки и 2 столбца
fig03, ax = plt.subplots(nrows=2, ncols=2, sharex=True)
# устанавливаем размер картинки
fig03.set_size_inches(8.0, 7.0)
# ее разрешение
fig03.set_dpi(900)




# строим зависимость для Китая (верхняя левая ячейка)
ax[0, 0].plot(list(China.keys()), list(China.values()))
ax[0, 0].set_ylabel('Population, milions of people')
ax[0, 0].grid(True)
ax[0, 0].set_title('Population in China')

# строим зависимость для Индии (верхняя правая ячейка)
ax[0, 1].plot(list(India.keys()), list(India.values()))
ax[0, 1].grid(True)
ax[0, 1].set_title('Population in India')

# строим зависимость для России (нижняя левая ячейка)
ax[1, 0].plot(list(Russia.keys()), list(Russia.values()))
ax[1, 0].set_ylabel('Population, milions of people')
ax[1, 0].grid(True)
ax[1, 0].set_title('Population in Russia')
ax[1, 0].set_xlabel('Year')

# строим зависимость для США (нижняя правая ячейка)
ax[1, 1].plot(list(USA.keys()), list(USA.values()))
ax[1, 1].grid(True)
ax[1, 1].set_title('Population in USA')
ax[1, 1].set_xlabel('Year')


#%%

"""
Задача из проекта Эйлера #50.
Простое число 41 может быть записано как сумма последовательности других 
простых чиcел:
    
    2+3+5+7+11+13=41

Это самая длинная цепочка простых чисел, которая образует другое простое
число меньше 100.

Самая длинная цепочка простых чисел, сумма которых образует простое числе
меньше 1000 насчитывает 21 число. Сумма этих чисел равна 953.

Выыести все простые числа из цепочки, сумма которой равна 953.

"""

def sieve(n):
    '''
    Поиск простых чисел меньше n с помощью решета Эратосфена
   https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D1%82%D0%BE_%D0%AD%D1%80%D0%B0%D1%82%D0%BE%D1%81%D1%84%D0%B5%D0%BD%D0%B0

    Parameters
    ----------
    n : integer

    Returns
    -------
    prime : list of integers, список простых чисел меньше n.

    '''
    
    # создаем список из чисел от 2 до n, учитывая, что 2 - первое простое число
    list_numbers = [i for i in range(2, n)] 
   
    # создаем список, куда будем записывать найденные простые числа
    # первым числом в списке будет число 2
    prime = [list_numbers[0]]
    
    # цикл будет работать до тех пор, пока мы не вычеркнем все числа из
    # списка list_numbers
    while len(list_numbers)>1:
        # переменной item присваиваем значение последнего члена из списка prime
        # т.е. в начале это будет 2, потом 3 и т.д.
        item = int(prime[-1])
        # создаем временный список, куда запишем все числа кратные числу item 
        temp_list = [i for i in range (item, n, item)]
        # далее проверяем каждое из чисел в списке temp_list 
        for item_ in temp_list:
            # если это число есть в списке list_numbers, то
            # мы его оттуда удаляем
            if item_ in list_numbers:
                list_numbers.remove(item_)
            else: pass
        # первое из оставшихся в списке list_numbers является простым
        # мы его добавляем в список простых чисел
        prime.append(list_numbers[0])
        # и присваеваем его переменной item и запускается новая итерация цикла.
        item = int(prime[-1])
        # Т.е. на первой итерации item = 2
        # мы создаем temp_list = [2, 4, 6, 8 и т.д.]
        # удаляем все числа из этого списка из списка list_numbers, в том числе 
        # 2. После этого у нас остается список list_numbers, где самым первым
        # числом является 3. Его мы добавляем в список prime.  
        # Дальше произволим аналогичные действия, только с item = 3 
    return prime




def isprime(number, primes):
    '''
    Проверяем, что число number есть в списке primes

    Parameters
    ----------
    number : integer.
    primes : list of integers, список простых чисел.

    Returns
    -------
    True of False

    '''
        
    if number in primes:
        return True
    else:
        return False
    



def get_summ (n):
    '''
    Решение задачи Project Euler #50

    Parameters
    ----------
    n : integer

    Returns
    -------
    result : integer, самма чисел меньше чем n.
    numbers: list of integers, цепочка чисел
    consecutive: integer, количество чисел в цепочке.

    '''
    
    
    #создадим список простых чисел меньше n 
    primes = sieve(n)
    # переменная, которая будет расчитывать количество чисел 
    # в самой длинной цепочке 
    consecutive = 0
    
    for i in range(len(primes)):
        # список, куда мы будем заносить числа из цепочки, которая 
        # создает сумму
        components = []
        # Переменная которая будет накапливать сумму
        summa = primes[i]
        # переменная, которая будет расчитывать количество чисел 
        # в текущей цепочке
        consec = 1
        # добавляем число primes[i] в цепочку
        components.append(primes[i])
        # после этого последовательно добавляем в переменную
        # summa числа из списка primes
        for j in range(i + 1, len(primes)):
            summa += primes[j]
            print ('i='+str(i)+' j='+str(j) + ' summa='+str(summa))
            consec += 1
            components.append(primes[j])
            # если сумма стала больше обозначенного чилса n, то прерываем
            # циклfor j in range(i + 1, len(primes)) 
            if summa >= n: 
                break
            # если сумма - простое число и если длинна цепочки
            # больше длинны полученной на предыдущем цикле,
            # значит в данный момент мы емеем дело с самой
            # длинной цепочко и записываем ее в ответ
            if isprime(summa, primes) and consec > consecutive:
                numbers = components.copy()
                result = summa
                consecutive = consec
            # если условия описанные выше не выполняются, то
            # возвращаемся назад и берем следующее значение i
            else: pass
    return result, numbers, consecutive
            

result, components, consecutive = get_summ(10000)
                    

































