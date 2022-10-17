# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:03:43 2022

@author: sidorow
"""
# Библиотека Pandas
"""
Библиотека Pandas - является фактически является заменой электронной таблицы 
типа Excel и позволяет сортировать и "чистить" большие массивы данных.
В данном уроке мы попробуем рассмотреть базовые команды библиотеки на примере
работы с данными экспериментального графика напряжение-формация  
"""
## Для начала импортируем нужные библиотеки
import pandas as pd # библиотека Pandas
import numpy as np # библиотека NumPy (см. урок 06)
import matplotlib.pyplot as pl # библиотека 
## Считываем данные из Excel файла
# Считываем первый лист
FirstSheet=pd.read_excel('Lesson07.xlsx', header=None, 
                             sheet_name='Results')
# Считываем второй лист
SecondSheet=pd.read_excel('Lesson07.xlsx', header=None, 
                             sheet_name='Data')
## Далее мы будем работать со сторым листом, где приведены эксперементальные
## данные напряжение-деформация. Создадим отдельную переменную FlowStressData,
## с которой будем дальше работать, а переменную SecondSheet оставим в качестве
## референсной
FlowStressData=SecondSheet
# Для начала посмотрим, что именно мы считали с помощью команды describe
Description=FlowStressData.describe()
# здесь count - количество строк, unique - количество строк с уникальными значениями
# top  - максимально часто встречающееся в столбце значение, freq - количество
# повторений этого значения.
# Далее определим размер массива данных:
ShapeFlowStressData=FlowStressData.shape
# Нам необходимы данные из первых двух столбцов (Инженерная деформация - столбец 0
# и инженерное напряжение - столбец 1)
for i in range (2, ShapeFlowStressData[1]):
    FlowStressData.drop([i], axis=1, inplace=True)
del i
# Т.к. первые три строки нам так же не нужны, их мы удалим аналогичным образом
FlowStressData.drop([0, 1, 2], axis=0, inplace=True)
# ОБратите внимание, что удалив первые три строки мы сломали индексацию, теперь
# первым индексом у нас выступает число 3. Это можно поправить:
FlowStressData=FlowStressData.reset_index(drop=True)
# здесь с помощью атрибута drop=True мы даем понять, что не надо создавать новый
# столбец для индекса, а нужно просто записать новые индексы в старый
# Для удобства можем дать столбцам наименования:
FlowStressData.columns=['EngineeringStrain', 'EngineeringStress']
# Мы можем тперь, например, определить предел прочности для этого материала
MaxTensileStress=FlowStressData['EngineeringStress'].max()
# Можем конфертировать данные из этих столбцов в NumPy array, что бы далее было
# проще с ними работать:
FlowStressDataNumPy=FlowStressData.to_numpy(dtype=float)
# и записать их обратно в массив Pandas
FlowStressData['EngineeringStrain']=FlowStressDataNumPy[:,0]
FlowStressData['EngineeringStress']=FlowStressDataNumPy[:,1]
# Пересчитаем первый столбец из деформации в процентах в деформацию в долях от 1
FlowStressData['EngineeringStrain']=FlowStressData['EngineeringStrain']/100
# После чего добавить столбцы с расчетными значениями истинных напряжений и дефомраций
FlowStressData['TrueStrain']=np.log(1+FlowStressData['EngineeringStrain'])
FlowStressData['TrueStress']=FlowStressData['EngineeringStress']*(1+FlowStressData['EngineeringStrain'])
# 
#
pl.plot(FlowStressData['EngineeringStrain'], FlowStressData['EngineeringStress'], '-*k')
pl.plot(FlowStressData['TrueStrain'], FlowStressData['TrueStress'], '-or')
#
# Добавим названия осей:
pl.xlabel('Деформация')
pl.ylabel('Напряжение, МПа')
#
#%%
# Далее будем работать с графиком Истанных напряжений и деформаций
# Для этого создадим переменную TrueStressStrain в формате NumPy array
TrueStressStrain=np.array([FlowStressData['TrueStrain'], FlowStressData['TrueStress']])
TrueStressStrain=np.transpose(TrueStressStrain)
# Определим модуль Юнга для этого материала
# Для этого нам нужно выделить заведомо упругую часть массива
ElasticStrain = np.array([0.0, 0.0])
ElasticStress =np.array ([0.0, 0.0])
i=0
while ElasticStrain[1] < 0.001:
    ElasticStrain[1]=TrueStressStrain[i,0]
    ElasticStress[1]=TrueStressStrain[i,1]
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
    Delta=TrueStressStrain[i,0]-TrueStressStrain[i,1]/E
    Sigma02=TrueStressStrain[i,1]
    i=i+1
# Найдем индекс массива TrueStressStrain, где напряжение максимально (т.е. найдем
# момент начала образования шейки)
j=TrueStressStrain[:,1].argmax()
PlasticStrain=TrueStressStrain[(i-1):j, 0]
PlasticStress=TrueStressStrain[(i-1):j, 1]
pl.plot(PlasticStrain, PlasticStress, 'r')
      
    


























