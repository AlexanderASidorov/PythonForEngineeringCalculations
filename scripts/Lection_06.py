# -*- coding: utf-8 -*-

# 1. Построение графиков в Python
# 
#



#%% Начнем с того, что импортируем необходимую для построения 
# графиков библиотеку matplotlib
import matplotlib.pyplot as plt
import math


# Начнет с того, что создадим два списка с данными (по оси x и по оси y).
# по оси x - список от 0 до 1 с шагом 0.1
x_data = [item*0.1 for item in range (-101, 101)]


# по оси y - sin и cos x
sin_x = [round (math.sin(x), 3) for x in x_data]

cos_x = [round (math.cos(x), 3) for x in x_data]

#%%%

# Самая базовая команда для построения графика в библиотеке 
# matplotlib является команда plot:
plt.plot(x_data , sin_x)
plt.plot(x_data , cos_x)

#plt.show() # для просмотра графика в консоли IDE типа VSC


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
plt.plot(x_data , sin_x, '--', color = 'red', label = 'sin x')
plt.plot(x_data , cos_x, '*-', color = 'green', label = 'cos x')



#%%
# цвет можно задавать в формате rgb
plt.plot(x_data , sin_x, 'x-', color = [0.255, 0.3, 0.186])
# можно в формате rgba
plt.plot(x_data , cos_x, 'o-', color = [0.5, 0.1, 0.8, 0.4])

#%%
# можно в формате 8-ми битного числа
# (смотрите https://en.wikipedia.org/wiki/RGB_color_model)
plt.plot(x_data , cos_x, '--', color = '#402040')

#%%
# Тонкие настройки графика удобно делать после создания отдельного объекта
# типа картинка:  
fig01=plt.figure()


# Настройка размера картинки 
fig01.set_size_inches (12, 7)
# Настройка разрешения
fig01.set_dpi (300)

# После этого мы можем все нужные нам графики отображать в одной 
# координатной плоскости, до тех пор, пока не создадим второй объект типа картинка 

# сосбтвенной строим графики:
plt.plot(x_data , sin_x, '--', color = 'black', label = 'sin x')
plt.plot(x_data , cos_x, '-', color = 'grey', label = 'cos x')

# выше мы каждому графику присвоили название (sin x и cos x)
# мы можем вывести название этих графиков:
plt.legend(fontsize = 18)

# Добавляем название осей:
plt.xlabel('x', fontsize = 24)
plt.ylabel('sin(x) и cos(x)', fontsize = 24)

# Можно задать пределы значений по каждой из осей:
plt.xlim(0, 11)
plt.ylim(-1.2, 1.2)

# Можно добавить название графика
plt.title('График sin(x) и cos(x)', fontsize = 18)

# Можно добавить сетку
plt.grid()

# можно сохранить рисунок в файл
plt.savefig('figure.png')


#%%
# То же самое можно отобразить как два графика с независимысми осями, но
# на одной картинке

fig02=plt.figure()

# можно насроить размер картинки 
fig02.set_size_inches (7, 14)
# можно настроит разрешение
fig02.set_dpi (300)



# Создаем первую область:
plt.subplot(2, 1, 1) # кол-во строк, количество колонок, номер графика в строке
plt.plot(x_data , sin_x, '-', color = 'red', linewidth = 3 ,label = 'sin x')
plt.legend(fontsize = 18, loc='upper right')
plt.xlabel('x', fontsize = 24)
plt.ylabel('sin(x)', fontsize = 24)
plt.xlim(0, 11)
plt.ylim(-1.2, 1.2)
plt.grid()



# Создаем вторую область:
plt.subplot(2, 1, 2) # кол-во строк, количество колонок, номер графика в строке
plt.plot(x_data , cos_x, '-', color = 'orange', linewidth = 3 ,label = 'cos x')
plt.legend(fontsize = 18, loc='upper right')
plt.xlabel('x', fontsize = 24)
plt.ylabel('cos(x)', fontsize = 24)
plt.xlim(0, 11)
plt.ylim(-1.2, 1.2)
plt.grid()

# можно сохранить рисунок в файл^
plt.savefig('figure.png')





#%%
# Изобразим на графике несортированные данные.
# Для создания этих данных импортируем генератор случайных чилес
import random

# в текущую ячейку еще раз испортируем библиотеки math и matplotlib
# что бы запускать эту ячейку автономно
import matplotlib.pyplot as plt
import math



# сгенерируем список из 50 случайных числе от 0 до 10, 
# округлив каждое до второго знака после запятой
x_data = [round(random.uniform(0, 10.0), 2) for _ in range (0, 500)]


# по оси y - sin и cos x
sin_x = [round (math.sin(x), 3) for x in x_data]
cos_x = [round (math.cos(x), 3) for x in x_data]

# добавим немного "разброса"
for i in range (0, len(sin_x)):
    sin_x[i] = sin_x[i]*random.uniform(0.9, 1.1)
    cos_x[i] = cos_x[i]*random.uniform(0.9, 1.1)





fig03=plt.figure()
# можно насроить размер картинки 
fig03.set_size_inches (14, 7)
# можно настроит разрешение
fig03.set_dpi (300)



# Изменим немного стиль отображения
plt.scatter(x_data, sin_x, s=5, c='red', marker='x', 
            linewidths = 1.0, label = 'sin x')
plt.scatter(x_data, cos_x, s=5, c='black', marker='o', 
            linewidths = 1.0, label = 'cos x')

plt.legend(fontsize = 18, loc='upper right')
plt.xlabel('x', fontsize = 24)
plt.ylabel('cos(x)', fontsize = 24)
plt.xlim(0, 11)
plt.ylim(-1.2, 1.2)
plt.grid()





#%%
# Изобразим столбчатую диаграмму.
# Для этого сначала импортируем файл с именами, который мы с
# делали на прошлом практическом занятии
# лежит файл здесь:
# https://github.com/AlexanderASidorov/PythonForEngineeringCalculations/blob/main/data/names.txt
# в текущую ячейку еще раз испортируем библиотеку matplotlib
# что бы запускать эту ячейку автономно
import matplotlib.pyplot as plt
import random

# Создадим список интересующих нас имен:
x_data = ['COLIN', 'JOHN', 'JAMES', 'ABBIE', 'IVAN', 
             'LEE', 'WONG', 'NATASHA', 'MARY']


############################# Исходные данные##################################
###############################################################################
path = 'C:/Users/sidorow/Documents/GitHub/PythonForEngineeringCalculationsFall2024/data/' # путь к папке в которой мы работаем 
file_name = 'names.txt' # имя исходного файла


f = open (path + file_name, 'r') # открываем файл для чтения
names_pure = f.read() # записываем содержимое файла в переменную names_pure
f.close() # Файл нам больше не нужем, можем его закрыть

names = names_pure.replace("'", "") # создаем переменную names и записываем в нее результат удаления символа ' из переменной names_pure
names = names.replace(" ", "") # удаляем все пробелы
names = names.split(",") # разбиваем переменную типа string на список с помощью запятой в качестве разделителя 

#############################################################################
############################################################################


# посчитаем как часто имя из списка x_data встречается в списке
#  списке names
y_data = [names.count(item) for item in x_data]


# с помощью генератора случайных чисел сгенерим цвета для каждого 
# из столбцов
colors = []
for _ in x_data:
    r= round(random.random(),3)
    g = round(random.random(),3)
    b = round(random.random(),3)
    colors.append([r, g, b])




fig03=plt.figure()
# можно насроить размер картинки 
fig03.set_size_inches (14, 7)
# можно настроит разрешение
fig03.set_dpi (300)

plt.bar(x_data, y_data)
# повернем именя на оси x на 90 градусов
plt.xticks(rotation=90)
# добавим подписи осей
plt.bar_label (plt.bar(x_data, y_data, color = colors), labels=y_data)




# добавим пределы по оси y
plt.ylim(0, 30)
# и имя диаграммы
plt.title('Количество имен в списке') 



