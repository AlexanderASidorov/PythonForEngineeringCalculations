# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.misc import derivative



"""
Задача 5. Дифференцирование.

На практике уравнение Аврами часто имеет более сложную форму, чем мы приводили 
ранее из-за того, что в реальности одновременно может происходить несколько 
фазовых превращений конкурирующих друг с другом.
Сильно вдаваться в подробности не будем, просто обозначим, что уравнение
X = 1 - exp((-1/b)*(t**n))
приходится записывать в виде:
X = Xeq*(1 - exp((-1/b)*(t**n)))

здесь Xeq - постоянный коэффициент, который варьируется от 0 до 1 и фактически
пропорционально уменьшает X
b, n - коэффициенты, где n имеет физический смысл, в который мы, опять же не
будем вдаваться, но отметим, что n варьируется в пределах от 2 до 4.
t - время

Мало того, на практике, часто нам может понадобится не собственно
функция X(t), а ее производная, которая имеет физический смысл скорости
фазового перехода.

Создадим функцию для этого уравнения и функцию для определения его 
коэффициентов (аналогично задаче 2 лекции 12):
"""

def avrami(t, Xeq ,b, n):
    '''
    Уравение Аврами

    Parameters
    ----------
    t : float, время изотермической выдержки;
    Xeq: float, коэффициент Xeq (фактчески Xmax);
    b : float, коэффициент b;
    n : float, коэффициент n;
    

    Returns
    -------
    fraction : float в пределах от 0 до 1. Объемная доля дочерней фазы. 

    '''
      
    fraction = Xeq*(1 - np.exp((-1/b)*(t**n)))
    
    return fraction

# Исходные условия для поиска коэффициентов (аналогично лекции #12)
t1 = 98.2
x1 = 0.77
t2 = 54.1
x2 = 0.5
Xeq = 0.8




def avrami_system (x, t1, t2, x1, x2, Xeq):
    '''
    Система из двух уравненией Аврами при различном времени выдержки в 
    изотермических условиях

    Parameters
    ----------
    x : NumPy array, коэффициенты b и n.
    t1, t2: float, время необходимое для образования x1 и x2
    x1, x2: float, объемная доля образовавшаяся за время t1 и t2
    Xeq: float, коэффициент Xeq (фактчески Xmax)
    

    Returns
    -------
    Если коэффициенты подобраны правильно, то функция должна возвращать список
    из двух нулей или близкие им значения

    '''
       
    b = x[0]
    n = x[1]
    
    equation_1 = avrami(t1, Xeq, b, n) - x1 
    equation_2 = avrami(t2, Xeq, b, n) - x2
    
    
             
    return [equation_1,  equation_2]





root = fsolve(avrami_system, [100, 3.0], args=(t1, t2, x1, x2, Xeq))
check_result = np.isclose(avrami_system(root, t1, t2, x1, x2, Xeq), [0.0, 0.0])

# можно заметить, что резальтат сильно успех или неуспех решения сильно зависит
# от начального предположения (от x0)
# давайте попробуем автоматизировать процесс поиска правильно начально приближения

j = 0 # счетчик итераций
number_of_iteration = 100 # максимальное количество итераций
initial_gues = [1.0, 3] # начальное приближение

while j <= number_of_iteration: # запускаем цикл
    # находим корни и проверяем их на предмет близости обеих уравнений 
    # функции avrami_system к нуля
    root = fsolve(avrami_system, initial_gues, args=(t1, t2, x1, x2, Xeq))
    check_result = np.isclose(avrami_system(root, t1, t2, x1, x2, Xeq), [0.0, 0.0])
    if all (item == True for item in check_result):
        break # если условие выполняется, то цикл прерываем
    else: # если нет, то увеличиваем начальное приближение коэффициента b в 10 раз
        initial_gues = [initial_gues[0]*10, 3]
        j +=1
        

# Решение мы нашли, далее давайте его визуализируем. Для этого создадим 
# массив значенией времени
time = np.linspace(1, t1*1.05)

# и расчитаем для каждого значения времени объемную долю
fraction = avrami(time, Xeq, root[0], root[1]) 



# Создадим объект fig01 и настроем его размер и разрешение    
fig01, ax1 = plt.subplots()
fig01.set_size_inches(8.0, 5.0)
fig01.set_dpi(600)

# отображаем кривую время - объемная доля
f_avrami = ax1.plot(time, fraction, '-*', label = 'Уравнение Аврами')
# отображаем две исходные точки, на основе которых мы решали уравнение
f_initial = ax1.plot([t2, t1], [x2, x1], 'o', label = 'Исходные данные')
# отображаем Xeq
f_Xeq = ax1.plot(time, np.full(time.shape, Xeq), '--', label = 'Xeq')

# отобразим на графике сетку
ax1.grid()
# зададим пределы осей
ax1.set_xlim([0, t1*1.05])
ax1.set_ylim ([0, 1])

# обозначим ось x и y
ax1.set_xlabel('Время, с')
ax1.set_ylabel('Объемная доля')
#ax1.legend()



# теперь найдем скорость фазового перехода как производную функции
# avrami по времени

velocity = derivative(avrami, time, dx = 0.01, args=(Xeq, root[0], root[1]))

# результат добавим на наш график, но т.к. значения скорсоти и объемной доли
# имеют разные масштабы, для скорсоти добавим вторую ось y
ax2 = ax1.twinx() # при этом ось x два графика буду делить


d_avrami = ax2.plot(time, velocity, label = 'Производная уравнения Аврами')
ax2.set_ylim ([np.min(velocity), np.max(velocity)*1.05])
ax2.set_ylabel('Скорость превращения, 1/сек')



def fraction(time, velocity):
    
    fraction = np.zeros(len(time))
    for i in range (1, len(time)):
        fraction[i] = fraction[i-1] + 0.5*(velocity[i-1]+velocity[i])*(time[i]-time[i-1])
    return fraction

f_derivative = ax1.plot(time, fraction(time, velocity), label = 'Обхемная доля из скорости')

# что бы показать легенду сделаем следующее:
# объединим все линии в список
lines = f_avrami + f_initial + f_Xeq + f_derivative + d_avrami
#  из этого списка вытащим все названия линий, которые мы ранее задали
labels = [l.get_label() for l in lines]
# и выведим их на график
ax1.legend(lines, labels)

        
    

















