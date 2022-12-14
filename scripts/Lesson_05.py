# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:58:51 2022

@author: sidorow
"""

# 1. Построение графиков в Python
# 
#
#%% Начнем с того, что импортируем необходимую для построения графиков библиотеку
# matplotlib
import matplotlib.pyplot as pl
# Начнет с того, что создадим два списка с данными (по оси x и по оси y).
# Для данного примера мы просто скопируем данные из файла Lesson_04.py. По оси
# x у нас, как обычно, будет деформация, по оси y - напряжение
PlasticStrain = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
PlasticStress= [355.0, 469.8766972916701, 584.7533945833402, 699.6300918750103, 
                814.5067891666804, 929.3834864583505, 1044.2601837500206,
                1159.1368810416907, 1274.0135783333608, 1388.8902756250309,
                1503.766972916701]
#%%
# Самая базовая команда для построения графика в библиотеке matplotlib является
# команда plot:
pl.plot(PlasticStrain, PlasticStress)
# Теперь, если вы работаете с IDE Spyder, перейдя в раздел Plots в окне переменных
# вы увидите простейший график, которого вам, в общем, впролне достаточно для 
# понимания того, что у вас в результате всех расчетов получилось
#
#
# Задав некоторые дополнительные атрибуты, мы можем немного улучшить вид нашего
# графика. В частности, мы можем задать тип линии, тип маркера и цвет линии.
pl.plot(PlasticStrain, PlasticStress, '--or')
# Мы можем нанести несколько кривых на один граки, а можем построить отдельные
# графика для каждой кривй. Давайте создадим еще один список с напряжениями, но
# пусть эти напряжения будут нелинейно зависеть от деформации
#
# Создаем список для напряжений. Назовем переменную PlasticStressNonLinear
PlasticStressNonLinear=list(range(0,len(PlasticStrain)))
# Формула, по которой мы будем в данном случае рассчитывать напряжения:
    # Sigma = Sigma02 + K*Epsilon**n
# Где K мы получили ранее в Lesson_04
K=2297.533945833402
# Sigma02 возмем из списка PlasticStress как PlasticStress [0]
Sigma02=PlasticStress[0]
# Показателем n просто зададимся: 
n=0.75
# После чего расчитываем список PlasticStressNonLinear 
for i in range (0,len(PlasticStrain)):
    PlasticStressNonLinear[i]=Sigma02+K*PlasticStrain[i]**n
# И строим его график:
pl.plot(PlasticStrain, PlasticStressNonLinear, '-*k')
#
# Как правило, для публикации графика где-либо нужно добавить название осей:
pl.xlabel('Деформация')
pl.ylabel('Напряжение, МПа')
#
# Можно задать пределы значений по каждой из осей:
pl.xlim(0, 0.51)
pl.ylim(350,1800)
#
# Можно добавить название графика
pl.title('Кривая деформационного упрочнения стали 45')
#
#
# Если для каждого из набора данных нужно построить свой собственный график, то
# можно для каждого из них создать свою собственную переменную, где этот график 
# будет хранится:
fig01=pl.figure(2)
pl.plot(PlasticStrain, PlasticStress, '--or')
pl.xlabel('Деформация')
pl.ylabel('Напряжение, МПа')
pl.xlim(0, 0.51)
pl.ylim(350,1800)
pl.title('Кривая деформационного упрочнения стали 45 \n'
         '(линейная зависимость)')
#
#
fig02=pl.figure(3)
pl.plot(PlasticStrain, PlasticStressNonLinear, '-*k')
pl.xlabel('Деформация')
pl.ylabel('Напряжение, МПа')
pl.xlim(0, 0.51)
pl.ylim(350,1800)
pl.title('Кривая деформационного упрочнения стали 45 '
         '(нелинейная зависимость)')
#
# Более подробно о построении различных графиков можно почитать в документации
# к библиотеке matplotlib по адресу https://matplotlib.org
# Там, в разделе с примерами (https://matplotlib.org/stable/gallery/index.html) ,
# можно посмотреть на оформление тех или иных графиков и скопировать текст программы
# для построения интересующего вас.
#%% ДОМАШНЕЕ ЗАДАНИЕ 
"""
Имеется массив данных Инженерные напряжения - Инженерная деформация в области
пластической деформации
Значения инженерных напряжений (в МПа):
378.5  397.3  431.23  461.56  476.13  487.83  489.32  488.16  486.71  455.11
Знаяения инженерных деформаций (в долях от 1):
0 0.0125  0.025  0.05  0.075  0.1  0.125  0.15 0.175 0.2
Рассчитать Истинные напряжения и Истинную деформацию во всем диапазоне деформации
образца
Построить два графика (на одном) Инженерное напряжение - Инженерная деформация (тип линии
- сплошная, цвет - красный, маркеры - звездочки) и Истанное напряжение - Истинная
деформация (тип линии - штрих, цвет - зеленый, маркеры - плюсики)

Напоминание:
Истинная деформация = ln*(1+Инженерная деформация)
Истинное напряжение = Инженерное напряжение*(1 + Инженерная деформация)
"""    
    
    
    
    
    
    
    
    
    
    
    
    

