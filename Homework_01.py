# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 18:00:07 2022

@author: sidorow
"""

#%% ДОМАШНЕЕ ЗАДАНИЕ 
# Имеется массив данных Инженерные напряжения - Инженерная деформация в области
# пластической деформации
# Значения инженерных напряжений (в МПа):
# 378.5  397.3  431.23  461.56  476.13  487.83  489.32  488.16  486.71  455.11
# Знаяения инженерных деформаций (в долях от 1):
# 0 0.0125  0.025  0.05  0.075  0.1  0.125  0.15 0.175 0.2
# Рассчитать Истинные напряжения и Истинную деформацию во всем диапазоне деформации
# образца
#
# Напоминание:
# Истинная деформация = ln*(1+Инженерная деформация)
# Истинное напряжение = Инженерное напряжение*(1 + Инженерная деформация)
#
#
# Импортируем нужные библиотеки: math - для математических функций и mathplotlib
# для построения графиков
import math
import matplotlib.pyplot as plt
# Исходные данные
EngineeringStress=[378.5,  397.3,  431.23,  461.56,  476.13,  487.83,  489.32,  488.16,  486.71,  455.11]
EngineeringStrain=[0, 0.0125,  0.025,  0.05,  0.075,  0.1,  0.125,  0.15, 0.175, 0.2]
# Определяем длину списка:
Length=len(EngineeringStress)
# Создаем переменные для Истинных напряжения и деформации
TrueStress=list()
TrueStrain=list()
# Расчитываем инженерные напряжения и деформации по приведенным выше формулам итерационно
# для каждой пары значений
for i in range(Length):
    # Stress и Strain - значения истинных напряжений и деформаций на i-й итерации
    Strain=math.log(1+EngineeringStrain[i])
    Stress=EngineeringStress[i]*(1+EngineeringStrain[i])
    # На каждой итерации, полученный на ней результат записываем с помощью команды append
    # в соответвующий список
    TrueStress.append(Stress)
    TrueStrain.append(Strain)
# Строим график, что бы визуально увидеть что получилось:
# Определяем переменную, в которой будет график хранится. Атрибутом figsize задаем
# размеры графика 
fig01=plt.figure(1,figsize=(5,5))
# Определяем названия осей
plt.xlabel('Деформация')
plt.ylabel('Напряжением, МПа')
# Определяем списки из которых брать значение для кривых:
plt(EngineeringStrain, EngineeringStress)
    # plt.semilogx(Pearlite.Phase001,Pearlite.Temperature, label='Pearlite 1%')