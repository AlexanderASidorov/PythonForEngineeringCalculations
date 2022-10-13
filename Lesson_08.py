# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:31:33 2022

@author: sidorow
"""
## Импортируем нужные библиотеки
import pandas as pd
import numpy as np
## Считываем данные из Excel файла
FlowStressData=pd.read_excel('1035_rough_data.xlsx', header=None, 
                             sheet_name='0.35')
# ## Определяем размер получившегося массива данных
ShapeDataFrame=FlowStressData.shape
## Копируем этот массив, что бы иметь его в первоначальном виде
CopyFlowStressData=FlowStressData
#%% Ищем значения температуры, скорости деформации и деформации в получившемся
# массиве. Для этого создаем функцию SearchingFor
def SearchingFor(word, dataframe):
    # word='Strain rate'
    # dataframe=FlowStressData
    # Определяем размер массива
    ShapeDataFrame=FlowStressData.shape
    # Переменнная TrueFals будет показывать есть ли в данной ячейки нужный нам
    # текст. Размерность этой переменной равна размерности массива
    TrueFalse=np.ones([ShapeDataFrame[0], ShapeDataFrame[1]])
    # сначала мы создали единичный массив NumPy
    # после чего конвертируем его в Pandas
    TrueFalse=pd.DataFrame(TrueFalse) # можно это и более коротко сделать
    # (см. далее, как мы этом сделаем для переменной Viriable)
    # Далее запускаем цикл, в ходе которого проверяем есть ли в
    # данном столбце слово, которое мы ищем
    for i in range(0, ShapeDataFrame[1]):
        TrueFalse[i]=FlowStressData[i].str.contains(word)
    # Создаем массив Variable, куда будем записывать интересующую
    # нас переменную
    del i
    Variable=list()
    for i in range(0, ShapeDataFrame[0]):
        for j in range(0, ShapeDataFrame[1]):
            if TrueFalse.iloc[i,j]==True:
                Temp= dataframe.iloc[i,j]
                #Temp=float(dataframe.iloc[i,j].split(':')[1])
                Variable.append(Temp)
    del i, j, Temp
    Variable=pd.Series(Variable) # конвертируем список в Pandas Series 
    # (одномерный) массив. После чего удаляем из него все "не цифры"
    Variable=Variable.str.replace(r"[a-zA-Z:'()]",'',regex=True)
    # Далее удаляем все повторяющиеся значения:
    Variable=Variable.drop_duplicates()
    # Конвертируем значения во float32
    Variable=Variable.astype('float32') 
    # И конвертируем переменную в NumPy array
    Variable=np.array([Variable]).transpose()
    return Variable
StrainRate=SearchingFor('Strain rate', FlowStressData)
Temperature=SearchingFor('temperature', FlowStressData)
#%%
## C деформацией (Strain) получается сложнее, т.к. в нашем исходном файле она
# прописана в нулевом столбце. В нулевом столбце данные могут быть трех типов:
# string, float и int. Нам нужно избавиться от тех строк, которые имеют тип
# string, т.к. это явно не деформация 
# Для этого состдадим переменную Index, в которой будем хранить данные о том,
# в каких строках нашего массива FlowStressData не содержится численных значений
Index=list()
# Что бы эти индексы определить нам нужна переменая, которая покажет нам какой 
# тип данных в данной ячейки (текстовый тип обозначчим как False, числовой - 
# как True). Создадим эту переменную 
DataType=list()
for ind in range(ShapeDataFrame[0]):
    if type(FlowStressData.iloc[ind,0])==float: # ищем floats
        DataType.append(True)
    elif type(FlowStressData.iloc[ind,0])==str: # ищем strings
        DataType.append(False)
        Index.append(ind)
    elif type(FlowStressData.iloc[ind,0])==int: # ищем int
        DataType.append(True)
#%%
# Создаем переменную для деформации
Strain=list()
for i in range(ShapeDataFrame[0]):
       if DataType[i]==True:
           Temp=float(FlowStressData.iloc[i,0]) 
           Strain.append(Temp)
# Сконвертируем список в Pannda DataFrame
Strain=pd.DataFrame(np.array(Strain))
# Удалим ячейки с неопределенными значениями
Strain = Strain.dropna()
# Удалим повторы
Strain = Strain.drop_duplicates()
# Сконвертируем деформацию в NumPy Array
Strain=np.array(Strain.astype('float32'))
#%% Удалим временные переменные
del i, ind, Temp
#%%
# Теперь начнем чистить основной наш массив FlowStressData, что бы потом 
# переконвертировать его в NumPy array
# Удалим из него строки, не содаржащие данных напряжение-деформация. Т.е. те
# строки, где у нас значения ячеек в массиве DataType = False
# Напоминаю, что мы выделили переменную Index, которая содержит номера строк
#, где DataType = False 
FlowStressData=FlowStressData.drop(axis=0, index=(Index))
# После этого удалим все строке, где нет данных
FlowStressData=FlowStressData.dropna(axis=0)
# После этого удалим столбец, в котором хранятся данные по деформации
FlowStressData=FlowStressData.reset_index(drop=True) #обновим нумерацию строк
FlowStressData=FlowStressData.drop(0, axis=1) # удаляем первый столбец (деформация)
ShapeDataFrame=FlowStressData.shape # на всякий случай определяем форму 
# получившегося массива
#%% Удалим временные переменные
del Index, DataType
#%%
# Конвертируем массив pandas в массив NumPy
FlowStress=np.array(FlowStressData)
# Далее переформатируем получившийся массив NumPy из двумерного в трехмерный
# Для этого определим количество ячеек по каждой из трех осей:
Axis_1=Temperature.shape[0] # количество точек по температуре
Axis_2=Strain.shape[0] # количество точек по дефорации
Axis_3= StrainRate.shape[0] # количество точек по скорости деформации
FlowStress=FlowStress.reshape(Axis_1,Axis_2,Axis_3)
del Axis_1, Axis_2, Axis_3               
