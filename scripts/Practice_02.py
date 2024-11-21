# -*- coding: utf-8 -*-

"""
файл names.txt содержит 100 000 тысяч имен.
Необходимо открыть файл и создать на его основе сиписок names, отсортированый
по алфавиту и без дубликатов
"""

import time # библиотека для измерения времени

############################# Исходные данные##################################
###############################################################################
path = 'C:/Users/sidorow/Documents/GitHub/PythonForEngineeringCalculationsFall2024/data/' # путь к папке в которой мы работаем 
file_name = 'names.txt' # имя исходного файла
file_name_new = 'names_sorted.txt' # имя файла, куда запишем 
##############################################################################
############################################################################

#%%
######################### Variant 01 ##########################################
###############################################################################
start01 = time.time() # запускаем счетчик времени

f = open (path + file_name, 'r') # открываем файл для чтения
names_pure = f.read() # записываем содержимое файла в переменную names_pure
f.close() # Файл нам больше не нужем, можем его закрыть

names = names_pure.replace("'", "") # создаем переменную names и записываем в нее результат удаления символа ' из переменной names_pure
names = names.replace(" ", "") # удаляем все пробелы
names = names.split(",") # разбиваем переменную типа string на список с помощью запятой в качестве разделителя 

set_names = set(names) # пользуясь тем, что множества не "допускают" повторений, удаляем из names все дубликаты

names = sorted(set_names) # сортируем множество по алфавиту, и записываем результат в переменную names
# эту часть можно пропустить, если не мешают скобки в файле
names = str(names)  # конвертируем список в переменную типа list в переменную типа str
names = names.replace("[", '').replace("]", '') # удаляем скобки


f_new = open (path + file_name_new, 'w') # создаем файл для записи 

f_new.write(names) # записываем в него переменную names
f_new.close() # закрываем файл

end01 = time.time() # выключаем счетчик времени
print(end01 - start01)

##############################################################################
##############################################################################
#%%

######################### Variant 02 ##########################################
###############################################################################
start02 = time.time()

named = []

file = open(path + file_name, 'r')

file_edit = file.read()
file_edit = file_edit.replace("'","").split(', ')
file.close()

for i in file_edit:
    if named.count(i) == 0:
        named.append(i)

new_file = open(path + file_name_new , 'w+')
new_file.write(str(named))
new_file.close()




end02 = time.time()
print(end02 - start02)

##############################################################################
##############################################################################

#%%

"""
файл names.txt содержит 100 000 тысяч имен.
Необходимо открыть файл и создать на его основе сиписок names, отсортированый
по алфавиту и без дубликатов (см. код выше). 
Далее для каждого имени необходимо посчитать числовой рейтинг.
Числовой рейтинг - сумма номеров каждой буквы имени в латинском алфавите. 

Т.е. буква A - номер 1, буква C - номер 3, буква Z - номер  26. 
Таким образом рейтинг имени COLIN будет 3+15+12+9+14 = 53.
После этого необходимо для каждого имени числовой рейтинг умножить на номер
имени в списке names, где номер начинается с 1, а не с 0, как обычно в Python.
Т.е. в случае COLIN имеем 53*(937+1) = 49714.

Посчитать сумму всех рейтингов
"""

############################# Исходные данные##################################
###############################################################################
path = 'C:/Users/sidorow/Documents/GitHub/PythonForEngineeringCalculationsFall2024/data/' # путь к папке в которой мы работаем 
file_name = 'names.txt' # имя исходного файла
file_name_new = 'names_sorted.txt' # имя файла, куда запишем 
##############################################################################
############################################################################


f = open (path + file_name_new, 'r') # открываем файл для чтения
names_pure = f.read() # записываем содержимое файла в переменную names_pure
f.close() # Файл нам больше не нужем, можем его закрыть



names = names_pure.replace("'", "").split(", ") # разбиваем переменную типа string на список с помощью запятой в качестве разделителя 



# создаем словарь для присвоения каждому имени в списке рейтинга
# ключ к словарю - буква латинского алфавита
# значение - номер в латинском алфавите

letters = [] # список для записи ключей 
letter_number = [] # список для номера
for i in range(65, 91): # каждый символ в python имеет свой номер, с помощью которого
                        # с помощью которого символ можно вызывать ключевым словом chr()
                        # A-Z соотвтетсвуют номера от 65 до 91
    letters.append(chr(i))
    letter_number.append(len(letters)) 

alphabet = dict(zip(letters, letter_number)) # создаем словарь



sum_ = 0 # в эту переменную будем записывать сумму рейтингов

for i in range (0, len(names)): # итерируем по списку names
    name = list(names[i]) # каждое имя из списка names преобразуем в список из букв, составляющих это имя
    for item in name: # для каждой буквы находим ее номер, через словарь alphabet
        sum_ += alphabet[item] # и поочередно суммируем номера
 





