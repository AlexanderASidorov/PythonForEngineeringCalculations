"""
Библиотека Pandas - фактически является заменой электронной таблицы
типа Excel и позволяет сортировать и "чистить" большие массивы данных.
В данном уроке мы попробуем рассмотреть базовые команды библиотеки на примере
работы с данными экспериментального графика напряжение-формация
"""
## Для начала импортируем нужные библиотеки
import pandas as pd # библиотека Pandas
import numpy as np # библиотека NumPy
import matplotlib.pyplot as plt # библиотека Matplotlib

# и попробуем прочитать данные из подготовленного заранее Excel файла Lection_14.xlsx
# 

# путь в папку, где лежит файл 
folder = '../data/'
# имя файла
filename_xls = 'Lection_14.xlsx'
# полный путь к файлу
filepath_xls = folder + filename_xls

# собственно чтение данных из Excel
data_from_excel = pd.read_excel (filepath_xls)
#%%
# как видите, по-умолчанию команда read_excel считывает только первый лист. Нам же,
# нужен второй, поэтому необходимо задать ей определенные параметры
data_from_excel = pd.read_excel (filepath_xls, sheet_name='Data')
# что бы первая строка не воспринималась как имя колонки, нужно задать еще один
# параметр
data_from_excel = pd.read_excel(filepath_xls, header=None, sheet_name='Data')
#%%
# можем сделать определенное резюме того, что мы считали:
description = data_from_excel.describe()
# здесь count - количество строк, 
# unique - количество строк с уникальными значениями
# top  - максимально часто встречающееся в столбце значение, 
# freq - количество повторений этого значения.
# Далее определим размер массива данных:
shape=data_from_excel.shape
#%%
# Нам необходимы данные из первых двух столбцов (Инженерная деформация - столбец 0
# и инженерное напряжение - столбец 1), поэтому все столбцы, кроме нулевого
# и первого можно удалить:
data_from_excel.drop([i for i in range (2, shape[1])], axis=1, inplace=True)
# здесь параметр axis = 0, если нам надо удалить строку, axis = 1, если столбец
# inplace = True - когда нам не надо сохранять данные в изначальном виде
# если же, все-таки надо, то мы можем создать новую переменную для усеченного
# массива, а изначальный оставить как есть:
#
# new_dataframe = data_from_excel.drop([i for i in range (2, shape[1])], axis=1, inplace=False)
# 
# Первые три строки нам так же не понадобятся, поэтому их можем аналогичным
# образом удалить
data_from_excel.drop([0, 1, 2], axis=0, inplace=True)
# кроме того, в файле присутсвовали пустые строки, которые прочитались как nan
# их тоже можно почистить:
data_from_excel.dropna(inplace=True)
# обратите внимание, что у нас индексация автоматически не обновилась
# и мы имеем 3 в качестве первого индекса. Это можно поправить:
data_from_excel.reset_index(drop=True, inplace=True)
# здесь с помощью атрибута drop=True мы даем понять, что не надо создавать новый
# столбец для индекса, а нужно просто записать новые индексы в старый
#%%
# аналогичный результат мы могли бы получить заранее подготовив данные
# в Excel и сохранив их в csv формате
# имя файла
filename_csv = 'Lection_14.csv'
# полный путь к файлу
filepath_csv = folder + filename_csv
# собственно чтение данных из csv
data_from_csv = pd.read_csv(filepath_csv)
# как видно, прочиталось с первого раза не очень хорошо, поэтому нужно:
# задать параметр, отвечающий за отделение столбцов друг от друга и
# запретить востринимать первую строку как заголовок
data_from_csv = pd.read_csv(filepath_csv, sep = ';' , header=None)

#%%

# далее будем работать с массивом data_from_excel, но в общем они идентичны 
# с массивом data_from_csv, кроме того, что data_from_csv изначально прочитался
# как массив чисел  numpy.float64, а data_from_excel как массив floats 

# Для удобства можем дать столбцам наименования:
data_from_excel.rename(columns={0: "EngineeringStrain", 1: "EngineeringStress"}, inplace = True)
# Мы можем тперь, например, определить предел прочности для этого материала
max_tensile_stress=data_from_excel["EngineeringStress"].max()

# обращение к конкретной ячейке осуществляется с помощью метода iloc
print(data_from_excel.iloc[100, 1])
# либо, что то же самое, через имя столца и номер строки:
print(data_from_excel['EngineeringStress'][100])
#%%

# Давайте найдем найдем индекс ячейки, где напряжение максимально:
index_max = data_from_excel.index[data_from_excel['EngineeringStress'] == max_tensile_stress][0]
# можем здесь же дать какое-то более сложное условие и получить список индексов:
filtr01 = (data_from_excel['EngineeringStress'] > max_tensile_stress*0.75) & (data_from_excel['EngineeringStress'] < max_tensile_stress*0.9)
# более элегантный способ сделать то же самое:
filtr02 = data_from_excel['EngineeringStress'].between(max_tensile_stress*0.75, max_tensile_stress*0.9)
filtr03 = data_from_excel['EngineeringStress'].gt(max_tensile_stress*0.75)
filtr04 = data_from_excel['EngineeringStress'].lt(max_tensile_stress*0.9)

#%%
indexes = data_from_excel.index[filtr02].tolist()
values = data_from_excel['EngineeringStress'][filtr02]


# можем изменить тип данных с floats на numpy.float64
data_from_excel = data_from_excel.astype(np.float64)

# а можем просто преобраховать весь массив в numpy array
data_array = data_from_excel.to_numpy(dtype=float)

# Как видите, некоторые значения в первой колонке у нас отрицательные. Это артефакт 
# измерений деформации. При этом физический смысл первой колонки подразумевает,
# что значения деформации должны монотонно возрастать. Т.е имеет смысл данные 
# упорядочить по возрастанию первой колонки
data_from_excel = data_from_excel.sort_values(by = ['EngineeringStrain'])
# необязательно, но желатьельно удалить все значения деформации < 0, т.к.
# они не имеют физического смысла
filtr05 = data_from_excel['EngineeringStrain'].lt(0.0) # создадим фильтр для этих целей 
# командой drop удалим все отрицательные точки
data_from_excel = data_from_excel.drop (index = data_from_excel[filtr05].index, axis = 0)

# далее удалим все повторяющиеся значения
data_from_excel = data_from_excel.drop_duplicates(subset=['EngineeringStrain'])
# переопределим индексы
data_from_excel = data_from_excel.reset_index(drop=True)

# Пересчитаем первый столбец из деформации в процентах в деформацию в долях от 1
data_from_excel['EngineeringStrain']= data_from_excel['EngineeringStrain']/100

# После чего добавить столбцы с расчетными значениями истинных напряжений и дефомраций
data_from_excel['TrueStrain']=np.log(1+data_from_excel['EngineeringStrain'])
data_from_excel['TrueStress']=data_from_excel['EngineeringStress']*(1+data_from_excel['EngineeringStrain'])


# резульат можем снова сохранить в Excel или csv
data_from_excel.to_csv(folder + 'TrueStressTrueStrain.csv')


#%%
# визуализируем все наши промежуточные результаты:

fig01 = plt.figure()
fig01.set_size_inches(8.0, 5.0)
fig01.set_dpi(600)

# отображаем кривую напряжение - деформация
plt.plot(data_from_excel['EngineeringStrain'],data_from_excel['EngineeringStress'], '-k', label = 'Инженерное напряжение')
plt.plot(data_from_excel['TrueStrain'],data_from_excel['TrueStress'], '-r', label = 'Истинное напряжение')

# Добавим названия осей:
plt.xlabel('Деформация, мм/мм')
plt.ylabel('Напряжение, МПа')
plt.grid()
plt.legend()
plt.title('График напряжение - деформация')


# посмотрим повнимательнее на упругую часть:
fig02 = plt.figure()
fig02.set_size_inches(8.0, 5.0)
fig02.set_dpi(600)

# отображаем кривую напряжение - деформация
plt.plot(data_from_excel['EngineeringStrain'],data_from_excel['EngineeringStress'], '-k', label = 'Инженерное напряжение')
plt.plot(data_from_excel['TrueStrain'],data_from_excel['TrueStress'], '-r', label = 'Истинное напряжение')

# Добавим названия осей:
plt.xlabel('Деформация, мм/мм')
plt.ylabel('Напряжение, МПа')
plt.grid()
plt.legend()
plt.title('График напряжение - деформация (упругая часть графика)') 
# Предельное значение по оси x - 0.004 (0.4 %)
plt.xlim([0, 0.004])

# отфильтруем все ячейки, которые больше заданного значения
filtr06 = data_from_excel['TrueStrain'].lt(0.004) 

# Предельным значением по оси y будет значения напряжения в точке с деформацией
# 0.004 увеличенное на 10%
plt.ylim([0, 1.1*data_from_excel['TrueStress'][filtr06].max()])




#%%
# Задача #1
# Определить модуль Юнга.

def youngs_modulus (true_strain, true_stress, defined_strain):
    
    
    strain_list = np.linspace (0.0001, defined_strain, 10)
    
    youngs = np.zeros(len(strain_list))
    
    
    for i in range (0,  len(strain_list)):
        filtr07 = true_strain.lt(strain_list[i])
        
        elastic_strain = true_strain[filtr07]
        elastic_stress = true_stress[filtr07]
        
        youngs[i] = elastic_stress.max()/elastic_strain.max()

    
    return np.mean(youngs) 

youngs = youngs_modulus (data_from_excel['TrueStrain'], 
                         data_from_excel['TrueStress'],
                         0.0005)


