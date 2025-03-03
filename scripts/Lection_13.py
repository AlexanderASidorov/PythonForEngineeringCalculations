# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:02:45 2025

@author: sidorow
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def simple_function (x):
    return 3*(x-3)**2-30


x = np.linspace(-10, 10)
y = simple_function(x)

plt.plot(x, y)
plt.grid()
plt.show()


x0=1

minimum = minimize(simple_function, x0)
print(f'Минимум функции = {minimum.x}')


from scipy.optimize import root

x0=[100.]

solution = root(simple_function, x0, tol=0.00000001)
print(f'Корень уравнения = {solution.x}')



#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve



def avrami (t, b, n):
    return 1-np.exp((-1/b)*(t**n))
    


b = 2
n = 3

integral, error = quad(avrami, 0, 2, args=(b, n))


t = np.linspace (0, 2)
f = avrami (t, b, n)

plt.plot (t, f)
plt.grid()
plt.show()


def system_avrami (coefs, times, fractions):
    b, n = coefs
    t01, t02 = times
    f01, f02 = fractions
    
    equation01 = f01 - avrami(t01, b, n)
    equation02 = f02 - avrami(t02, b, n)
    
    return [equation01, equation02]


system = system_avrami ((2, 3), (1., 2.), (0.4, 0.98))

times = (0.75, 1.5)
fractions = (0.2, 0.81)


x0 = [1, 1]

solution_02 = fsolve(system_avrami, x0, args = (times, fractions))

b, n = solution_02
f = avrami (t, b, n)
plt.plot (t, f)
plt.scatter (times, fractions)
plt.grid()
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d



def avrami (t, b, n):
    return 1-np.exp((-1/b)*(t**n))


t_data = np.array([0, 1, 2, 3, 4, 5])
f_data = np.array ([0, 0.1, 0.2, 0.5, 0.8, 0.9])

plt.scatter(t_data, f_data)
plt.show()




initia_guess = [100., 100.]

popt, pcov = curve_fit(avrami, t_data, f_data)

b, n = popt

t = np.linspace (0, 5)
f = avrami(t, b, n)

plt.scatter(t_data, f_data)
plt.plot (t, f)
plt.grid()
plt.show()


interp_nearest = interp1d( t_data, f_data, kind='nearest')
iterp_linear = interp1d( t_data, f_data)
interp_cube = interp1d( t_data, f_data, kind='cubic')


f_nearest = interp_nearest(t)
f_linear = iterp_linear (t)
f_cubic = interp_cube (t)

plt.scatter(t_data, f_data)
plt.plot (t, f_nearest)
plt.plot (t, f_linear)
plt.plot (t, f_cubic)
plt.grid()
plt.show()

 






    
    
    
    


































    
