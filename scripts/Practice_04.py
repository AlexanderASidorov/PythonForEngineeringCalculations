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
    
    
    if a>b or a%1 >0 or b%1 >0:
        return None 
    
    else:
        c = (a**2+b**2)**0.5
        if c>b>a and c%1 == 0:
            return c
        else:
            return None

# test_01 = get_c(a=10, b=2)
# test_02 = get_c(a=2, b=4)
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
      
    if not c>b>a or not c%1 == 0 or not b%1 == 0 or not a%1 == 0: 
        return False
    
    else:    
        for i in range(2, a):
            if a%i==0 and b%i==0 and c%i==0:
                return False
                break
        return True
   
# test_01 =  check_for_common_devider (10, 8, 6)           
# test_02 =  check_for_common_devider (3.2, 4, 5)
# test_03 =   check_for_common_devider (6, 8, 10)
# test_04 = check_for_common_devider (3, 4, 5)



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
        
    
triplet_list_02 = get_pythagorean_triplet_02 (100.1)
            
 #%%           

"""
Необходимо взять тектовый файл с именами
https://github.com/AlexanderASidorov/PythonForEngineeringCalculations/tree/main/data
файл names.txt
на его основе, с помощью генератора случайных чисел сгенерировать файл
names_with_duplicates.txt, содержащий 50 000 имен, в том числе дубликатов 
существующих

"""

import random

random_int = random.randint(0, 100) # генерация случайного целого числа
random_float = random.random() # генерация числа типа float от 0 до 1
random_from_range = random.randrange(0, 100, 5) # генерация числа типа int
                                                   # в диапазоне, но с шагом 
random_choise = random.choice(triplet_list_02)
random.shuffle (triplet_list_02) # разупорядочевает список

#%%%%

# открываем файл names.txt (дожен распалагаться в текущей папке, иначе нужно)
# прописать путь до этого файла
with open ("../data/names.txt", 'r') as myfile:
    for names in myfile:
        names = names.replace('"', '') # удаляем все "
        names = names.split(",") # принимаем , в качастве разделителя
names_with_duplicates = names.copy()

i=0
while i < (100000 - len(names)): # задаем число повторений (фактически длину нового списка)
    i = i+1
    random_name = random.choice(names) # выбираем произвольное имя из списка names
    names_with_duplicates.append(random_name) # дописываем его список names_with_duplicates 
random.shuffle(names_with_duplicates) # разупорядочиваем получившийся список

# записываем разультат (список names_with_duplicates в файл names_generated.txt)
with open("../data/names_generated.txt", "w") as myfile:
    myfile.write(str(names_with_duplicates))


       

    



















