# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:33:33 2024

@author: sidorow
"""
from scipy.integrate import quad
from scipy.interpolate import interp1d


import numpy as np
import matplotlib.pyplot as plt

"""
Задача #5. Интегрирование.
Допустим у нас есть график силы по перемещению:
 
"""

# перемещение
s = np.linspace(0, 10, 100)
# сила
def force(s):
    return 100 + s**2.1
    
f = force(s)

 
# Создадим объект fig01 и настроем его размер и разрешение    
fig01 = plt.figure()
fig01.set_size_inches(8.0, 5.0)
fig01.set_dpi(600)

# отображаем кривую время - объемная доля
plt.plot(s, f)

# отобразим на графике сетку
plt.grid()
# обозначим ось x и y
plt.xlabel('Перемещение, мм')
plt.ylabel('Сила, Н')
# обозначим пределы оси y
plt.ylim([0, 300])

def interp_load_stroke (stroke, force):
    f_linear  = interp1d(stroke, force, kind='quadratic')
    return f_linear

# интегрирование функции force
work_function = quad(force, s[0], s[-1], epsabs=1.49e-08)

# интегрирование функции interp_load_stroke 
work_interp = quad(interp_load_stroke(s, f), s[0], s[-1], epsabs=1.49e-08)
