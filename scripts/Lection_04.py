# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:59:20 2022

@author: sidorow
"""

# 1. Множества в Python
# 2. Кортежи в Python
# 3. Работа с текстовыми файлами
# 
# 
#
#
#
#%%
'''
Множество (в терминологии python - set) это набор неиндексированных 
данных без повторяющихся значений. Т.е. множество может иметь только 
одно значение 10, одно значение 'десять' и т.д. Создается множетсво 
с помощью фигурных скобок {}, т.е. аналогично словарю, но без разбивки 
на ключи и значение.
'''
first_set = {1, 2, 3, 10, 12, 17.8}
# пустое множество можно создать командрой
empty_set = set()

# основные методы при работе со множествами аналогичны методам при
# работе со списками:
# add() - добавление значение в имеющееся множетсво
first_set.add('ten')
first_set.add([1, 14, 3.14]) # выдаст ошибку, т.к. add позволяет 
                            # добавить только "примитивные" объекты 
                            # типа int, float, string 
# remove() - удаление значения из имеющегося множества
first_set.remove(17.8)
first_set.remove(14) # удаление несуществующего элемента приводит к ошибке
# discard () - удаляет значение, если оно присутствует
first_set.discard(14) # ничего не происходит, т.к. 14 нет во 
                        #множетсве first_set
first_set.discard(1) # из множетсва удаляется 1 
# update () - добавляет несколько значений
first_set.update([2, 45, 2.14])
# union () - объединяет два мнлжетсва (без дублирования)
second_set = {1, 2, 3, 10, 12, 17.8, 1000, 5e-5}
third_set = first_set.union(second_set)
# intersection () - создает "пересечение" двух множеств
fourth_set = first_set.intersection(second_set )
# difference () - создаеет множетсво, состоящее из уникальных 
# значений одного множетсва относительно второго
fifth_set = first_set.difference(second_set)
# symmetric_difference() - создаеет множетсво, состоящее 
# из уникальных значений для каждого из них
sixth_set = first_set.symmetric_difference(second_set)
# isdisjoint () - проверяет есть ли общие значения в двух множетсвах
isdisjoint_01_02 = first_set.isdisjoint(second_set)
isdisjoint_01_new = first_set.isdisjoint({11111, 222222, 3333, 5555})
# False - есть, True - нет

"""
Самый очевидный случай для использования множесвта - удаление повторяющихся
значений из списка. Например вернумся к задаче с именами, только в этот раз
прочитаем даныне из файла names_with_duplicates.txt (см. папку data 
 на github.com/AlexanderASidorov/PythonForEngineeringCalculations)
 
"""
#%%%
# открываем файл names.txt (дожен распалагаться в текущей папке, 
# иначе нужно) прописать путь до этого файла
with open ("../data/names_with_duplicates.txt") as myfile:
    for names in myfile:
        names = names.replace('"', '') # удаляем все "
        names = names.split(",") # принимаем , в качастве разделителя

# Список names мы можем сконвертировать во множество
names_set = set()
names_set.update(names)
# После чего можем мнова преобразовать эти данные в список (если это нужно):
names_no_duplicates = list(names_set)
# После чего, например, можем этот список отсортировать по алвафиту
names_no_duplicates.sort()

#%%
"""
Кортеж (в терминологии python - tuple) - упорядоченный и неизменяемый
набор данных.
Допускает наличие повторяющихся элементов.
Создается с помощью круглых скобок

"""
first_tuple = (1, 12, 3.14, 'ten', ['one', 'two', 'three'], 
               (12, 17.5, 'ten'), 17, 0.01)

# в приведенном кортеже мы не можем изменять переменные кортежа:
first_tuple[1] = 15 # выдасть ошибку
# но можем изменять, например список из этого кортежа
first_tuple[4][0] = 'one point one'
# добавлять переменные в кортеж мы так же не можем
first_tuple.add(0.5) # выдаст ошибку
# наиболее очевидный пример использования кортежей:
# допустим у нас есть две переменные:
a = 1000
b = 0.001
# и допустим нам надо присвоить a значение b, а значению b - значение a
# мыможем это сделать через третью переменную temp:
temp = a
a=b
b=temp
# то же самое можно сделать с помощью кортежа:
a, b = (b, a)
# Использование кортежей, когда это возможно, предпочтительнее нежели
# использование списков, т.к. они занимают меньше месиа в памяти 
# компьютера и их итерирование происходит быстрее 


    




    
    
    
    
    
    
















