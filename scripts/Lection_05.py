# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:58:51 2022

@author: sidorow
"""

# 1. Построение графиков в Python
# 
#



#%% Начнем с того, что импортируем необходимую для построения 
# графиков библиотеку matplotlib
import matplotlib.pyplot as plt

def polinom_3 (x):
    return round (2*x**3 + x**2 + 3*x + 1, 2)

def polinom_2(x):
    return round (6*x**2 + 2*x + 3, 2)



# Начнет с того, что создадим два списка с данными (по оси x и по оси y).
x_data_01 = [round (item*0.1, 1) for item in range (0, 11)]
y_data_01 = [polinom_3(x) for x in x_data_01]


# Самая базовая команда для построения графика в библиотеке 
# matplotlib является команда plot:
plt.plot(x_data_01 , y_data_01)
#%%
# Теперь, если вы работаете с IDE Spyder, перейдя в раздел 
# Plots в окне переменных вы увидите простейший график, которого 
# вам, в общем, впролне достаточно для понимания того, что 
# у вас в результате всех расчетов получилось
#
#
# Задав некоторые дополнительные атрибуты, мы можем 
# немного улучшить вид нашего графика. В частности, мы можем 
# задать тип линии, тип маркера и цвет линии.
plt.plot(x_data_01 , y_data_01, '--', color = 'red')
plt.plot(x_data_01 , y_data_01, '*-', color = 'green')
# цвет можно задавать в формате rgb
plt.plot(x_data_01 , y_data_01, 'x-', color = [0.255, 0.3, 0.186])
# можно в формате rgba
plt.plot(x_data_01 , y_data_01, 'o-', color = [0.5, 0.1, 0.8, 0.4])
# можно в формате 8-ми битного числа
# (смотрите https://en.wikipedia.org/wiki/RGB_color_model)
plt.plot(x_data_01 , y_data_01, '--', color = '#402040')

#%%
# Давайте созадим копию списка чисел x_data, а данные по y сгенерируем
# помощью функции polinom_2 (производная от полинома 3-го порядка)  

x_data_02 = x_data_01.copy()
y_data_02 = [polinom_2(x) for x in x_data_01]

# Отсортируем данные
# x_data_02 = sorted(x_data_01)
# y_data_02 = sorted(y_data_01)
# Что бы отобразить два набора данных на одном графике необходимо создать 
# объект типа рисунок для графика:  
fig01=plt.figure()
# 
# После этого мы можем все нужные нам графики отображать в одной 
# координатной плоскости 

# И строим его график:
plt.plot(x_data_01 , y_data_01, '-*', 
         color = 'green' , label = 'Полином третьего порядка')
plt.plot(x_data_02, y_data_02, '-x', 
         color = 'black', label = 'Полином второго порядка')
# выше мы каждому графику присвоили название (data_01 и data 02)
# мы можем вывести название этих графиков:
plt.legend()
# Можем добавить название осей:
plt.xlabel('x data')
plt.ylabel('y data')
# Можно задать пределы значений по каждой из осей:
plt.xlim(0, 1.1)
plt.ylim(0, 15.0)
# Можно добавить название графика
plt.title('График полиномов второго и третьего порядка')
# Можно добавить сетку
plt.grid(axis='both')

#%%
# Изобразим на графике несортированные данные.
# Для создания этих данных импортируем генератор случайных чилес
import random

# сгенерируем список из 50 случайных числе от 0 до 10, 
# округлив каждое до второго знака после запятой
x_data_03 = [round(random.uniform(0, 10.0), 2) for _ in range (0, 50)]
# с помощью функции polinom_3 сгенерируем набор данных по оси y
# при этом в качестве входного параметра в функцию подадим
# число x из списка  x_data_03 и прибавим к каждому из них
# члучайное число от 0 до 2
y_data_03_01 = [round(polinom_3 (x+random.uniform(0, 2)), 2) 
                for x in x_data_03]
y_data_03_02 = [round(polinom_3 (x+random.uniform(0, 2)), 2) 
                for x in x_data_03]

fig02=plt.figure()
# Для начала посмотрим, что нам покажет диаграмма с параметрами по 
# умолчанию

#plt.scatter(x_data_03, y_data_03)

# Изменим немного стиль отображения
plt.scatter(x_data_03, y_data_03_01, s=5, c='black', marker='x', 
            linewidths = 1.0, label = 'data 01')
plt.scatter(x_data_03, y_data_03_02, s=5, c='red', marker='*', 
            linewidths = 1.0, label = 'data 02')

plt.grid(axis='both')
plt.xlabel('x data')
plt.ylabel('y data')
plt.title('Несортированные данные')
plt.legend()

#%%
# Изобразим столбчатую диаграмму.
# Для этого сначала импортируем файл с именами, который мы с
# делали на прошлом практическом занятии
# лежит файл здесь:
# https://github.com/AlexanderASidorov/PythonForEngineeringCalculations/blob/main/data/names_with_duplicates.txt


# Создадим список интересующих нас имен:
x_data_04 = ['COLIN', 'JOHN', 'JAMES', 'ABBIE', 'IVAN', 
             'LEE', 'WONG', 'NATASHA', 'MARY']


# что бы создать список имен воспользуемся функцией, которую мы
# сделали на практическом занятии #3
from Practice_03 import read_names_from_file 


names, _, _ = read_names_from_file("../data/", "names_generated.txt")


# посчитаем как часто имя из списка x_data_04 встречается в списке
#  x_data_04
y_data_04 = [names.count(item) for item in x_data_04]


# Столбчатая диаграмма по умолчнаию будет выглядеть следующим образом:
plt.bar(x_data_04, y_data_04)  

# Попробуем ее немного "настроить"    
# создадим для этой диаграммы отдельную переменную типа рисунок
fig03=plt.figure()

# после этого мы можем настроить размер диаграммы (нирина и восота 
# в дюймах)
fig03.set_size_inches(9.0, 4.7)
# ее разрешение
fig03.set_dpi(600)

# с помощью генератора случайных чисел сгенерим цвета для каждого 
# из столбцов
colors = []
for _ in x_data_04:
    r= round(random.random(),3)
    g = round(random.random(),3)
    b = round(random.random(),3)
    colors.append([r, g, b])
# после чего построим диаграмму (созда)
plt.bar(x_data_04, y_data_04, color = colors)
# повернем именя на оси x на 90 градусов
plt.xticks(rotation=90)
# добавим подписи осей
plt.bar_label(plt.bar(x_data_04, y_data_04, color = colors), 
              labels=y_data_04)
# добавим пределы по оси y
plt.ylim(0, 30)
# и имя диаграммы
plt.title('Количество имен в списке') 

    
    
    
    
    
    
    
    
    

