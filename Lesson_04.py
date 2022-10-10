# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:59:20 2022

@author: sidorow
"""

# 1. ФУНКЦИИ в Python
# 
#
#
#%% Начнем с того, что импортируем необходимую нам библиотеку Math
import math
#%%    ФУНКЦИИ в Python
"""
Функция в Python Это просто часть программы, которую вы можете периодически,
когда вам это нужно, вызывать, определяя в качестве исходных данных для нее
некоторые исходные параметры (какие-то переменные, другие функци и т.д.) и 
получая в качестве результата ее работы какие-то другие параметры (например, 
какие-то другие переменные).
Функция внутри тела программы определяется следующим образом:
  Ключевое слово def говорит о том, что мы начали определять функцию;
  На этой же строке мы определяем имя функции, с помощью которого далее будем
  эту функцию вызывать;
  далее в скобках мы указываем исходные переменные, которые будет необходимо
  этой функции сообщить;
  после чего ставим двоеточие, что означает, что далее мы начинаем записывать
  команды, которые эта функция будет выполнять.
  после того, как мы нужные команды записали, ключевым словом return мы
  определяем какие переменные мы в результате действия функции получим.
"""
# Пример простейшей функции: извлечение кубического корня из суммы трех чисел
def simplefunction (a, b, c):
    return (a+b+c)**(1/3)
#
#
Test=simplefunction(20, 6, 1)
#
"""
В качестве более инстересного примера, давайте построим функцию, которая будет 
определять напряжение течения материала при заданной степени пластической
дефорации. Исходная формула будет линейной и выглядит следующим образом:
    Sigma = Sigma02 + K*Epsilon
    Здесь Sigma - напряжение течение материала
    Sigma02 - его условный предел текучести
    K - коэффициент при деформации
    Epsilon - истинная пластическая деформация (это переменная функции)
В качесте входных параметров этой функции мы будем использовать следующие 
переменные, доступные в справочниках как основные мех. свойства материала:
    Условный предел текучести (Sigma02);
    Предел прочности (SigmaB);
    Максимальное равномерное удлинение (Ag).
Необходимо отметить, что в литературе все мех. свойства приведены в инженерных
значениях, т.е. в теле функции нам необходимо пересчитать их в истинные
"""
def Sigma (Sigma02, SigmaB, Ag, Epsilon):
    # Пересчитаем все исходные переменные из инженерных в истинные помня что:
    # Истинная деформация = ln*(1+Инженерная деформация)
    # Истинное напряжение = Инженерное напряжение*(1 + Инженерная деформация)
    TrueAg=math.log(1+Ag)
    TrueSigmaB=SigmaB*(1+Ag)
    TrueSigma02=Sigma02 # т.к. деформация равна в этот момент 0
    # Определим коэффициент при деформации K, подставим в исходное уравнение
    # TrueAg, TrueSigmaB и TrueSigma02 (равное Sigma02)
    K=(TrueSigmaB-TrueSigma02)/TrueAg
    print (K)
    return TrueSigma02+K*Epsilon
# Проверим как работает функция на примере стали 45:
# согласно ГОСТ 1577-93 полоса имеет следующие мех. характеристики:
Sigma02_45=355
SigmaB_45=600
Ag_45=0.16 
# обратите внимание, что обычно в литературе равномерное удлинение
# приводят в процентах, наша же функция работает с долей от 1 для этой переменной.
# Источник здесь: (http://splav-kharkov.com/mat_start.php?name_id=87)
#
#
# При истинной деформации 0.1 напряжение течения будет:
TrurSigma01 = Sigma(Sigma02_45, SigmaB_45, Ag_45, 0.1)
# При истинной деформации 0.5 напряжение течения будет:
TrurSigma05 = Sigma(Sigma02_45, SigmaB_45, Ag_45, 0.5)
#
#
# Можем построить с помощью получившейся функции массив данных напряжение - 
# деформация, который потом перенести, при необходимости, в DEFORM или подобную 
# программу для моделирвоания процессов пластического деформирования
# Стоим для этого список со значением пластической деформации:
PlasticStrain=list(range(0,11))
PlasticStress=list(range(0,11))
for i in PlasticStrain:
    PlasticStrain[i]=PlasticStrain[i]*0.05
    PlasticStress[i]= Sigma(Sigma02_45, SigmaB_45, Ag_45, PlasticStrain[i])
#
#
# То же самое, можно сделать немного по-другому:
PlasticStrainAlternative=[x*0.05 for x in range(11)]
PlasticStressAlternative=[Sigma(Sigma02_45, SigmaB_45, Ag_45, Strain) 
                          for Strain in PlasticStrainAlternative]





















