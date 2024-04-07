#  Библиотека NumPy (продолжение лекции #07)
#
#
import numpy as np


## Рассмотрим возможности библиотеки NumPy по фильтрации данных:
# обратимся снова к нашему списку имен...
from Practice_03 import read_names_from_file
names_dataset, _, _ = read_names_from_file("../data/", "names_generated.txt")

# преобразуем этот список в массив NumPy
names_np = np.array(names_dataset)
# если мы проверим тип объекта, то обнаружим, что мы столкнулись с 
# новым для нас типом:
print(type(names_np))
print(type(names_np[0]))

# допустим у нас задача найти все имена, начинающиемя на 'N'
# для этого создадим отдельную переменную, которая представляет собой
# массив NumPy, где значение True означает, что имя начинается на 'N',
# а значение False, что нет
filtr01 = np.array([item[0] == 'N' for item in names_np])
# теперь мы можем отфильтровать данные:
names_start_N_all = names_np[filtr01]
# если мы хотим выкинуть все дупликаты, то это можно сделать через
# множество, а можно оставаясь в рамках библиотеки NumPy:
names_start_N_original = np.unique(names_start_N_all)


# обратите внимание, что сделать то же самое, но через список у нас не получится:
# т.е. создать фильтр мы можем
filtr02 = [item[0] == 'N' for item in names_dataset]
# но не можем без цикла его применить к исходному списку
#names_start_N = names_dataset[filtr02]
# хотя через цикл - можем
names_start_N_list = list(set([item for item in names_dataset if item[0] == 'N']))

#%%
import numpy as np
import time

## Рассмотрим возможности библиотеки NumPy по фильтрации данных:
# обратимся снова к нашему списку имен...
from Practice_03 import read_names_from_file
names_dataset, _, _ = read_names_from_file("../data/", "names_generated.txt")


# Давайте попробуем замерить, какой из способов фильтрации лучше с точки
# с точки зрения времени выполнения. Для этого создадим две функции фильтрации:
# через список и через библиотеку NumPy



def f_filtr01 (list_, letter_):
    '''
    Фильтрация имен по первой букве с помощью NumPy

    Parameters
    ----------
    list_ : list of strings, список имен.
    letter_ : string, буква по которой нужно отфильтровать список.

    Returns
    -------
    names_start : Numpy array of strings, массив имен начинающихся 
    на букву letter_.

    '''
    
    names = np.array(list_)
    filtr = np.array([item[0] == letter_ for item in names])
    names_start_all = names[filtr]
    names_start = np.unique(names_start_all)
    return names_start




def f_filtr02 (list_, letter_):
    '''
   Фильтрация имен по первой букве с помощью списков

   Parameters
   ----------
   list_ : list of strings, список имен.
   letter_ : string, буква по которой нужно отфильтровать список.

   Returns
   -------
   names_start : list of strings, список имен начинающихся 
   на букву letter_.

    '''
    
    names_start = list(set([item for item in list_ if item[0] == letter_]))
    return names_start


# фиксируем время начала выполнения функции
start_time = time.time()
   
names_start_C_np = f_filtr01(names_dataset, 'C')
print ('С помощью библиотеки NumPy время выполнения фильтрации: ' +
       str(time.time()-start_time))


start_time = time.time()
names_start_C_list_ = f_filtr02(names_dataset, 'C')  
print ('С помощью списка время выполнения фильтрации: ' + 
       str(time.time()-start_time))   
    


#%%
import numpy as np

#                ЛИНЕЙНАЯ АЛГЕБРА С ПОМОЩЬЮ БИБЛИОТЕКИ NumPy
#
# В линейной алгебре вектор – это упорядоченный список чисел.

# одномерный массив:
v01 = np.array([12, 17, 34.5, 112, 74]) # не транспонируется
# вектор-строка
v02 = np.array([ [12, 17, 34.5, 112, 74] ])
# вектор-столбец (получаем с помощью операции транспонирования)
v03 = v02.transpose()

"""
Сложение и вычитание двух векторов
"""
v01 = np.array([ 4, 5, 6])
v02  = np.array([10,20,30])
v03 = np.array([ 0, 3, 6, 9])
v01Plusv02 = v01 + v02
v01Minusv02 = v01 - v02
#v01Plusv03 = v01 + v03 # ошибка! измерения не совпадают!

# попробуем то же самое, но для случая, когда у нас есть вектор-столбец и 
# и вектор-строка:
# вектор-строка
v02 = np.array([ [12, 17, 34.5, 112, 74] ])
# вектор-столбец
v03 = v02.transpose()
# их сумма:
v02Plusv03 = v02 + v03 # сложение при помощи транслирования
# Транслирование, по существу, означает многократное повторение операции 
# между одним вектором и каждым элементом другого вектора.

"""
Умножение вектора на  скаляр, сложение вектора и скаляра
"""
# для вектора-столбца
v03Multiple2 = v03*2
v03Plus10 = v03+10
# для вектора-строки
v02Multiple2 = v02*2

'''
Модуль вектора, также именуемый геометрической длиной, или нормой, представляет 
собой расстояние от хвоста до головы вектора и вычисляется с использованием 
стандартной формулы евклидова расстояния: квадратный корень из суммы квадратов 
элементов вектора
'''
v01 = np.array([1, 2, 3, 7, 8, 9])
v01_dim = len(v01) # математическая размерность
v01_norm = np.linalg.norm(v01) # матем. модуль, длина или норма вектора

# Существуют приложения, в которых нужен вектор, геометрическая длина
# которого равна единице, и такой вектор называется единичным вектором.
# Что бы найти единичный вектор, ассоциативный с исходным нам как раз может 
# понадобится норма вектора:
v01_one = (1/v01_norm)*v01
# норма этого вектора равна 1:
v01_one_norm = np.linalg.norm(v01_one)

'''
Точечное произведение – это одно число, которое предоставляет информацию о 
взаимосвязи между двумя векторами.
Это базовый вычислительный блок, на основе которого строятся
многие операции и алгоритмы, включая свертку, корреляцию, результаты
преобразования Фурье, матричное умножение, извлечение линейных признаков, 
фильтрацию сигналов и т. д.
    Пример вычисления точечного произведения
    [1 2 3 4] · [5 6 7 8] = 1×5 + 2×6 + 3×7 + 4×8 =
                            = 5 + 12 + 21 + 32 =
                            = 70. 
'''
v = np.array([1, 2, 3, 4])
w = np.array([5, 6, 7, 8])
dot = np.dot(v,w)

#%%

'''
                Корреляция и косинусное сходство.
Коэффициент корреляции – это одно число, которое количественно описывает 
линейную взаимосвязь между двумя переменными. Коэффициенты корреляции 
варьируются от –1 до +1, причем –1 указывает на идеальную отрицательную 
взаимосвязь, +1 – на идеальную положительную взаимосвязь, а 0 указывает на
отсутствие линейной взаимосвязи.                
'''
import numpy as np
import matplotlib.pyplot as plt




N = 50




# set up figure
#_,axs = plt.subplots(2,2,figsize=(6,6))

fig, axs = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(12.0, 12.0)
fig.set_dpi(900)
plt.subplots_adjust(left=None,
                    bottom=None, 
                    right=None, 
                    top=None, 
                    wspace=0.3, 
                    hspace=0.3)




# позитивная корреляция

x01 = np.linspace(0,10,N) + np.random.randn(N)
y01 = x01 + np.random.randn(N)

axs[0,0].plot(x01,y01,'k.')
axs[0,0].set_title('Позитивная корреляция')
axs[0,0].set_xlabel('Переменная x')
axs[0,0].set_ylabel('Переменная y')




# негативная корреляция
x02 = x01.copy()
y02 = -y01.copy()

axs[0,1].plot(x02, y02,'k.')
axs[0,1].set_title('Негативная корреляция')
axs[0,1].set_xlabel('Переменная x')
axs[0,1].set_ylabel('Переменная y')



# нулевая корреляция #01
x03 = np.random.randn(N)
y03 = np.random.randn(N)

axs[1,0].plot(x03, y03,'k.')
axs[1,0].set_title('Нулевая корреляция')
axs[1,0].set_xlabel('Переменная x')
axs[1,0].set_ylabel('Переменная y')



# нулевая корреляция #02
x04 = np.cos(np.linspace(0,2*np.pi,N)) + np.random.randn(N)/20
y04 = np.sin(np.linspace(0,2*np.pi,N)) + np.random.randn(N)/20

axs[1,1].plot(x04, y04,'k.')
axs[1,1].set_title('Нулевая корреляция')
axs[1,1].set_xlabel('Переменная x')
axs[1,1].set_ylabel('Переменная y')




def pearson (x, y):
    '''
    функция для расчета Коэффициента корреляции (коэф Пирсона)

    Parameters
    ----------
    x : 1D numpy array.
    y : 1D numpy array.

    Returns
    -------
    pearson : float, коэффициент Пирсена

    '''
    # нормализуем x и y
    xm  = x-np.mean(x)
    ym  = y-np.mean(y)
    
    # числитель
    numirator = np.dot(xm , ym)
    # знаменатель
    denumirator = np.linalg.norm(xm) * np.linalg.norm(ym)
    # коэффициент
    pearson = numirator/denumirator
    return pearson
    
pearson01 = pearson(x01, y01)
pearson02 = pearson(x02, y02)
pearson03 = pearson(x03, y03)  
pearson04 = pearson(x04, y04)    
   

def cosin (x, y):
    '''
    функция для расчета косинусного сходства

    Parameters
    ----------
    x : 1D numpy array.
    y : 1D numpy array.

    Returns
    -------
    pearson : float, косинусное сходство

    '''   
    
    # числитель
    numirator = np.dot(x,y) 
    # знаменатель
    denumirator = np.linalg.norm(x) * np.linalg.norm(y)
    cos = numirator / denumirator
    return cos

cos01 = cosin(x01, y01)
cos02 = cosin(x02, y02)
cos03 = cosin(x03, y03)
cos04 = cosin(x04, y04)   
    
    











