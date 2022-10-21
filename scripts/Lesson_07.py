"""
Библиотека Pandas
Библиотека Pandas - является фактически является заменой электронной таблицы
типа Excel и позволяет сортировать и "чистить" большие массивы данных.
В данном уроке мы попробуем рассмотреть базовые команды библиотеки на примере
работы с данными экспериментального графика напряжение-формация"""
## Для начала импортируем нужные библиотеки
import pandas as pd # библиотека Pandas
import numpy as np # библиотека NumPy (см. урок 06)
import matplotlib.pyplot as pl # библиотека Matplotlib (см. урок 05)
import os # библиотека для перемещения между директориями
os.chdir('../data') # переходим в корневую папку проекта
## Считываем данные из Excel файла (первый лист)
First_Sheet = pd.read_excel ('Lesson07.xlsx', header=None, sheet_name='Results')
# Считываем второй лист
Second_Sheet = pd.read_excel('Lesson07.xlsx', header=None, sheet_name='Data')
os.chdir('../scripts') # возвращаемся впапку scripts
## Далее мы будем работать со сторым листом, где приведены эксперементальные
## данные напряжение-деформация. Создадим отдельную переменную FlowStress_Data,
## с которой будем дальше работать, а переменную Second_Sheet оставим в качестве
## референсной
FlowStress_Data=Second_Sheet
# Для начала посмотрим, что именно мы считали с помощью команды describe
Description=FlowStress_Data.describe()
# здесь count - количество строк, unique - количество строк с уникальными значениями
# top  - максимально часто встречающееся в столбце значение, freq - количество
# повторений этого значения.
# Далее определим размер массива данных:
ShapeFlowStress_Data=FlowStress_Data.shape
# Нам необходимы данные из первых двух столбцов (Инженерная деформация - столбец 0
# и инженерное напряжение - столбец 1)
for i in range (2, ShapeFlowStress_Data[1]):
    FlowStress_Data.drop([i], axis=1, inplace=True)
del i
# Т.к. первые три строки нам так же не нужны, их мы удалим аналогичным образом
FlowStress_Data.drop([0, 1, 2], axis=0, inplace=True)
# ОБратите внимание, что удалив первые три строки мы сломали индексацию, теперь
# первым индексом у нас выступает число 3. Это можно поправить:
FlowStress_Data=FlowStress_Data.reset_index(drop=True)
# здесь с помощью атрибута drop=True мы даем понять, что не надо создавать новый
# столбец для индекса, а нужно просто записать новые индексы в старый
# Для удобства можем дать столбцам наименования:
FlowStress_Data.columns=['EngineeringStrain', 'EngineeringStress']
# Мы можем тперь, например, определить предел прочности для этого материала
Max_Tensile_Stress=FlowStress_Data['EngineeringStress'].max()
# Можем конфертировать данные из этих столбцов в NumPy array, что бы далее было
# проще с ними работать:
FlowStress_DataNumPy=FlowStress_Data.to_numpy(dtype=float)
# и записать их обратно в массив Pandas
FlowStress_Data['EngineeringStrain']=FlowStress_DataNumPy[:,0]
FlowStress_Data['EngineeringStress']=FlowStress_DataNumPy[:,1]
# Пересчитаем первый столбец из деформации в процентах в деформацию в долях от 1
FlowStress_Data['EngineeringStrain']=FlowStress_Data['EngineeringStrain']/100
# После чего добавить столбцы с расчетными значениями истинных напряжений и дефомраций
FlowStress_Data['TrueStrain']=np.log(1+FlowStress_Data['EngineeringStrain'])
FlowStress_Data['TrueStress']=FlowStress_Data['EngineeringStress']*(1+
    FlowStress_Data['EngineeringStrain'])
#
#
Fig_01=pl.figure(1)
pl.plot(FlowStress_Data['EngineeringStrain'], FlowStress_Data['EngineeringStress'], '-*k')
pl.plot(FlowStress_Data['TrueStrain'], FlowStress_Data['TrueStress'], '-or')
#
# Добавим названия осей:
pl.xlabel('Деформация')
pl.ylabel('Напряжение, МПа')
#
#%%
# Далее будем работать с графиком Истанных напряжений и деформаций
# Для этого создадим переменную True_Stress_Strain в формате NumPy array
True_Stress_Strain=np.array([FlowStress_Data['TrueStrain'], FlowStress_Data['TrueStress']])
True_Stress_Strain=np.transpose(True_Stress_Strain)
# Определим модуль Юнга для этого материала
# Для этого нам нужно выделить заведомо упругую часть массива
ElasticStrain = np.array([0.0, 0.0])
ElasticStress =np.array ([0.0, 0.0])
i=0
while ElasticStrain[1] < 0.001:
    ElasticStrain[1]=True_Stress_Strain[i,0]
    ElasticStress[1]=True_Stress_Strain[i,1]
    i=i+1
del i
# По закону Гука Sigma = E * Epsilon или E = Sigma/Epsilon, где E - модуль Юнга
# отсюда Модуль Юнга
E=ElasticStress[1]/ElasticStrain[1]
# Определим предел текучести из условия, что остаточная деформация больше или
# равна 0.002
i=0
Delta = 0
while Delta <= 0.002:
    Delta=True_Stress_Strain[i,0]-True_Stress_Strain[i,1]/E
    Sigma_02=True_Stress_Strain[i,1]
    i=i+1
# Найдем индекс массива True_Stress_Strain, где напряжение максимально (т.е. найдем
# момент начала образования шейки)
j=True_Stress_Strain[:,1].argmax()
# Удаляем все данные до предела текучести и после начала образования шейки
Plastic_Strain=True_Stress_Strain[(i-1):j, 0]
Plastic_Strain=Plastic_Strain-Plastic_Strain[0]
Plastic_Stress=True_Stress_Strain[(i-1):j, 1]
# Построим график пластическая деформация - напряжение
Fig_02=pl.figure(2)
pl.plot(Plastic_Strain, Plastic_Stress, 'r')
# Добавим названия осей:
pl.xlabel('Пластическая деформация')
pl.ylabel('Напряжение, МПа')
#%% Попробуем апроксимировать эти данные
# Для этого нам понадобится библиотека SciPy
from scipy.optimize import curve_fit
# и определим уравнение, которым мы будем апроксимировать, с помощью функции
def flow_curve (X_Data,K, n):
    return Sigma_02+K*X_Data**n
X_Data=Plastic_Strain
Y_Data=Plastic_Stress
Initial_Guess = [0,2]
popt, pcov = curve_fit(flow_curve, X_Data, Y_Data, Initial_Guess)
K=popt[0]
n=popt[1]
Fig_03=pl.figure(3)
pl.plot(Plastic_Strain, Plastic_Stress, 'r')
pl.plot(Plastic_Strain, flow_curve(Plastic_Strain, K, n), 'b')
# Добавим названия осей:
pl.xlabel('Пластическая деформация')
pl.ylabel('Напряжение, МПа')
    #%% Т.к. результат апроксимации далек от идеального, попробуем апроксимировать
# эти же данные простым полиномом третьего порядка
def polynom (x, a, b, c, d):
    return a*x**3+b*x**2+c*x+d
Initial_Guess = [1,1,1,1]
popt, pcov = curve_fit(polynom, X_Data, Y_Data, Initial_Guess)
constants=popt
Fig_04=pl.figure(4)
pl.plot(Plastic_Strain, Plastic_Stress, 'r')
pl.plot(Plastic_Strain, polynom(Plastic_Strain, constants[0], constants[1],
                               constants[2], constants[3]), 'b')
# # # Добавим названия осей:
pl.xlabel('Пластическая деформация')
pl.ylabel('Напряжение, МПа')
#%% Если хотим получить совсем идеальный результат, то можем попробовать
# увеличить размерность полинома
def polynom (x, a, b, c, d, e):
    return a*x**4+b*x**3+c*x**2+d*x+e
Initial_Guess = [1, 1, 1, 1, 1]
popt, pcov = curve_fit(polynom, X_Data, Y_Data, Initial_Guess)
constants=popt
Fig_05=pl.figure(5)
pl.plot(Plastic_Strain, Plastic_Stress, 'r')
pl.plot(Plastic_Strain, polynom(Plastic_Strain, constants[0], constants[1],
                               constants[2], constants[3], constants[4]), 'b')
# # # Добавим названия осей:
pl.xlabel('Пластическая деформация')
pl.ylabel('Напряжение, МПа')
