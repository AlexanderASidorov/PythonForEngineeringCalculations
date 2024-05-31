# -*- coding: utf-8 -*-


## Для начала импортируем нужные библиотеки
import pandas as pd # библиотека Pandas
import numpy as np # библиотека NumPy
import matplotlib.pyplot as plt # библиотека Matplotlib
from scipy.interpolate import interp1d


# путь в папку, где лежит файл 
folder = '../data/'
# имя файла
filename_xls = 'Lection_14.xlsx'
# полный путь к файлу
filepath_xls = folder + filename_xls

# собственно чтение данных из Excel
data_from_excel = pd.read_excel(filepath_xls, header=None, sheet_name='Data')

# Определим размер массива данных:
shape=data_from_excel.shape

# удаляем лишние столбцы
data_from_excel.drop([i for i in range (2, shape[1])], axis=1, inplace=True)

# удаляем первые три строки
data_from_excel.drop([0, 1, 2], axis=0, inplace=True)

# удаляем пустые строки
data_from_excel.dropna(inplace=True)

# переопределяем индексы
data_from_excel = data_from_excel.reset_index(drop=True)

# присваиваем имена колонкам
data_from_excel.columns=['EngineeringStrain', 'EngineeringStress']

# Мы можем теперь, например, определить предел прочности для этого материала
max_tensile_stress=data_from_excel['EngineeringStress'].max()

# Пересчитаем первый столбец из деформации в процентах в деформацию в долях от 1
data_from_excel['EngineeringStrain']= data_from_excel['EngineeringStrain']/100

# Изменим тип данных с floats на numpy.float64
data_from_excel = data_from_excel.astype(np.float64)

# После чего добавить столбцы с расчетными значениями истинных напряжений и дефомраций
data_from_excel['TrueStrain']= np.log(1+data_from_excel['EngineeringStrain'])
data_from_excel['TrueStress']=data_from_excel['EngineeringStress']*(1+data_from_excel['EngineeringStrain'])


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

#%%
# посмотрим повнимательнее на упругую часть:
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
    '''
    Модуль Юнга определяется как отношение напряжения к деформации.
    
    Parameters
    ----------
    true_strain : numpy array, столбец истинной деформации
    true_stress : numpy array, столбец истинного напряжения
    defined_strain : float, максимальная деформация в диапазоне которой мы
                    уверены, что деформация не перешла в пластическое состояние

    Returns
    -------
    float, модуль Юнга

    '''
    
    # разобьем отрезок упругой деформации на 10 отрезков 
    strain_list = np.linspace (0.0001, defined_strain, 10)
    
    # переменная, куда мы будем записывать отношение напряжения к деформации
    youngs = np.zeros(len(strain_list))
    
    
    # далее для каждого значения из массива strain_list расчитываем 
    # отношение напряжения к деформации
    for i in range (0,  len(strain_list)):
        
        # в массиве true_strain выделяем точки, значение которых меньше,
        # чем текущее значение из массива strain_list         
        filtr07 = true_strain.lt(strain_list[i])
        
        # создаем промежуточный массив деформаций, значения которых меньше,
        # чем strain_list[i]
        elastic_strain = true_strain[filtr07]
        # соответсвующий ему массив напряжений
        elastic_stress = true_stress[filtr07]
        
        # находим отношение максимально напряжения к максимальное деформации
        # и записываем их в ранее созданный массив youngs
        youngs[i] = elastic_stress.max()/elastic_strain.max()

        

    return np.mean(youngs) # модуль Юнга находим как среднее арифметическое 
                           # значений из массива youngs

youngs = youngs_modulus (data_from_excel['TrueStrain'], 
                         data_from_excel['TrueStress'],
                         0.0005)






#%%
# Задача #2
# Определить предел текучести (нарряжение, при котором остаточная пластическая
# деформация равна 0.002)

def yield_point (true_strain, true_stress, youngs):
    '''
    Условный предел текучести определяется как напряжение, которое обеспечивает
    0.2 % (0.002 в долях от 1) остаточной пластической деформации

    Parameters
    ----------
    true_strain : numpy array, столбец истинной деформации
    true_stress : numpy array, столбец истинного напряжения
    youngs : float, модуль Юнга

    Returns
    -------
    None.

    '''
    
    # вычитаем из общей деформации упругую из условия, что упругая деформация
    # это отношение напряжения к модулю Юнга    
    plastic_strain = true_strain - true_stress/youngs
    
    # находим индекс ячейки, абсолютное значение разности с 0.002 в которой
    # минимально
    idex_yield_stress = np.abs(plastic_strain - 0.002).argmin()
    
    # напряжение в этой ячейки и есть условный предел текучести
    yield_stress = true_stress[idex_yield_stress]
    
    return yield_stress


yield_stress = yield_point (data_from_excel['TrueStrain'], 
                         data_from_excel['TrueStress'],
                         youngs)



















