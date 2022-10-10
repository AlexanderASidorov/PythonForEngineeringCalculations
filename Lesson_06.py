# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:26:57 2022

@author: sidorow
"""

#  Библиотека NumPy
"""
Библиотека NumPy (Numeric Python) - основная причина, по которой Python
стал одним из самых популярных языков программирования алгоритмов машинного
обучения.
Почему вообще возникла и получила широкое распространение библиотека NumPy?
Допустим у нас есть список значений истинного напряжения (см. прошлый урок) и 
нам по каким-то причинам нужно все значения из этого списка увеличить на 10%
"""
PlasticStress= [355.0, 469.8766972916701, 584.7533945833402, 699.6300918750103, 
               814.5067891666804, 929.3834864583505, 1044.2601837500206,
               1159.1368810416907, 1274.0135783333608, 1388.8902756250309,
               1503.766972916701]
# Если мы просто умножим переменную PlasticStress на 1.1, то получится следующее:
# PlasticStress10=PlasticStress*1.1
# Как видите, в консоли появилось сообщение об ошибке:
# can't multiply sequence by non-int of type 'float'
#%% Т.е. для того, что бы все числа из этого списка увеличить на 10% нам 
# необходимо запустить цикл:
PlasticStress_10=list(PlasticStress) # копируем значения из списка PlasticStress
for i in range(len(PlasticStress)):
    PlasticStress_10[i]= PlasticStress[i]*1.1
#%% или то же самое можно сделать по-другому:
PlasticStress10=list() # создаем пустой список
j=-1 # создаем переменную для запуска счетчика
while j<(len(PlasticStress)-1): ## нам нужно, что бы на самой последней итерации
# значение j было равно значению индекса последнего числа в списке PlasticStress,
# т.е. 11
    j=j+1
    PlasticStress10.append(PlasticStress[j]*1.1)
#%%
"""
Приведенные выше два способа в общем простые, но все же удобнее было бы,
умножать весь список на число, как это реализовано, например в MatLab.
Самая главная проблема использования циклов, что в некомпелируемых языках
программирования циклы довольно медленно работают и их рекомендуется избегать
если есть такая возможность.
Для решения этой проблемы в Python был придуман самостоятельный тип данных
NumPy aarray.
Что бы им воспользоваться нам необходимо импортировать библиотеку NumPy. Она 
предустановлена в большинстве сред разработки для Python
"""
import numpy as np # здесь np - общепринятое сокращение для вызова компонентов
# этой библиотеки
# после этого мы можем создавать массивы типа numpy array
FirsNumPyArray = np.array([1, 2, 13, 3]) # массив целочисленных значений
SecondNumPyArray = np.array([1, 2, 12, 3.14]) # массив значений типа float
ThirdNumPyArray = np.array([[1, 3.14, 3], [4, 5, 4]]) # двумерный массив
# Можно преобразовать имеющиеся списки в массивы NumPy:
FourthNumPyArray=np.array([PlasticStress, PlasticStress10])
# Если нам нужен массив не 2 на 11, а 11 на 2, то его можно транспанировать:
FifthNumPyArray=np.array([PlasticStress, PlasticStress10]).transpose()
"""
все 5 массивов, которые мы создали выше имеют два основных ограничения:
 1. они имеют фиксированный размер, т.к. мы не можем добавлять в них строки
или колонки с помощью команд pop или append
 2. все элементы массива NumPy имеют один и тот же тип, т.е. не может быть
что часть массива integer, а часть float
Важным и часто используемым инструментом является комманда np.zeros([n, m]). 
Т.е. мы создаем массив NumPy состоящий из нулей, который потом можем заполнить 
нужными нам значениями 
"""
SixthNumPyArray = np.zeros([11, 2])
# Аналогично можно построить массив, состоящий из единиц:
SeventhNumPyArray=np.ones([2, 11])
# Иногла нужно бывает создать массив, например от n до m с шагом delta:
m=3
n=12
delta=0.5
EighthNumPyArray=np.arange(m,n,delta)
# Можно наоборот от n до m с отрицательным шагом delta
NinethNumPyArray=np.arange(n, m, -delta)
# а можно расстояние от m до n разбить на нужное количество отрезков:
TenthNumPyArran=np.linspace(m, n, 100)
# Возвращаясь к исходной задаче, где нам необходимо было увеличить все значения
# из списка PlasticStress на 10%, с помощью библиотеки NumPy это можно сделать
# следующим образом:
# Конвертируем список PlasticStress в массив NumPy
PlasticStressNumPyArray=np.array(PlasticStress)
# И теперь мы можем просто умножить получившийся массив на 1.1 и все его элементы
# в результате увеличатся на 10%
PlasticStressNumPyArray=PlasticStressNumPyArray*1.1
# По такому же принципу мы можем осуществлять действия над элементами двух
# масссивов, например почленно сложить значения:
SummPlasticStressNumPyArray=PlasticStressNumPyArray+np.array(PlasticStress)
# Можем, например, извлечь квадратный корень из каждого элемента
SqrtSummPlasticStressNumPyArray=np.sqrt(SummPlasticStressNumPyArray) 
# Изложенный выше подход называют ВЕКТОРИЗАЦИЕЙ.
#
#
# Индексация в массивах NumPy происходит аналогично индексации в списках:
MaximumStress=FifthNumPyArray[10,1]
# При необходимости мы можем поменять тот или иной член массива:
FifthNumPyArray[10,1]=FifthNumPyArray[10,1]*1.1
# а если нужно, например, обнулить массив, то необходимо указать все элементы 
# массива
FifthNumPyArray[:]=0
































