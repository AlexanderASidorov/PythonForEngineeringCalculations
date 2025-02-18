# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


# Импортируем массив из лекции #10 (смотрите папку data)
array = np.loadtxt('C:/Users/sidorow/Documents/GitHub/PythonForEngineeringCalculationsFall2024/data/lection10_02.txt')

# Создаем загатовку для матрицы признаков
X = np.ones([array.shape[0], array.shape[1]])
# Копируем первые шесть стобцов массива в матрицу признаков. Нулевой столбец
# матрицы признаков оставляем равным 1 для расчета свободного коэффициента уравнения
X[:, 1:] = array[:, :6]
# создаем вектор целефой переменный. Это последний столбец импортировагнного массива
y = array[:, -1]



class LinearRegression:
        
    def __init__ (self, X, y, initial_phi = None, learning_rate = 0.000001):
        
        self.X = X # матрица признаков 
        self.y = y # вектор целевой переменной
        
        ############################
        ## начальное заданное значение вектора коэффициентов. 
        ### По-молчанию - все нули.
        if initial_phi is None:
            self.initial_phi = np.zeros(X.shape[1], dtype = float)
        else:
            self.initial_phi = initial_phi
        
        self.phi = self.initial_phi.copy()  # в атрибут self.phi мы будем записывать
                                # значения phi после каждой итерации. Т.е. в
                                # начальный момент он равен initial_phi, но далее
                                # будет постоянно перезаписываться
                
        self.learning_rate = learning_rate # скорость обучения
     
        
    def cost_function (self, phi):
        '''
        Функция потерь (смотрите формулу в лекции)

        Parameters
        ----------
        phi : 1D NumPy с коэффициентами регрессии.

        Returns
        -------
        mse : float, среднеквадратичная ошибка.

        '''
        mse = np.mean ((self.X.dot(phi) - self.y)**2)
        
        return mse
    
    
    def gradient_cost_function (self, phi):
        '''
        Градиент функции потерь (вектор частных производных функции
                                 потерь по phi. Cмотрите формулу в лекции)

        Parameters
        ----------
        phi : 1D NumPy с коэффициентами регрессии.

        Returns
        -------
        mse : 1D NumPy, вектор частных производных функции потерь по phi.

        '''
              
        # почситаем количество данных (количество строк в метрице признаков или 
        # в векторе целевой переменной).
        N, _ = self.X.shape
        
        # Расчитываем значение целефой переменной при заданных заданном векторе phi
        y_pred = self.X.dot(phi)
        
        # расчитываем градиент
        gradient = (2/N)*self.X.T.dot(y_pred - self.y)
        
        return gradient
 
    
    def gradien_descent(self, n_iterations = 100):
        '''
        Метод градиентного спуска

        Parameters
        ----------
        n_iterations : integer, максимальное количество итериций

        Returns
        -------
        None.

        '''
        # в переменную cost_function_history будем записывать значение функции
        # потерь на каждой итерации
        self.cost_function_history = []
    
           
        
        for i in range (0, n_iterations):
            
            # Расчитываем значение целефой переменной при заданных заданном векторе phi
            y_pred = self.X.dot(self.phi)
            
            # Расчитываем значение функции потерь на текущей итерации
            cost_function_i = self.cost_function(self.phi)
            
            # записываем значение функции потерь в переменную для ее хранения
            self.cost_function_history.append(cost_function_i)
            
            # расчитываем градиент функции потерь для данного вектора phi
            gradient_i = self.gradient_cost_function(self.phi)
            
            # пересчитываем phi путем вычитвания из текущего phi произведения
            # скорости обучения на градиент функции потерь 
            self.phi -= self.learning_rate*gradient_i
            
            # увеличиваем значение i на одну единицу
            i+=1
            
    def plot_cost_function(self):
        '''
        Вывод графика изменения функции потерь по итерациям

        Returns
        -------
        None.

        '''
        # создаем переменную для хранения номера итерации
        iterations = np.arange(0, len(self.cost_function_history))
        
        # создаем график изменения функции потерь        
        plt.figure (figsize=(10, 6))
        plt.plot (iterations, self.cost_function_history)
        plt.xlabel("Номер итерации")
        plt.ylabel("Значение функции потерь")
        plt.grid()
        plt.show()
            
        
        
# learning_rate = 0.01 дает ошибку     
model = LinearRegression(X = X, y = y, learning_rate = 0.01)
model.gradien_descent(n_iterations=100)
model.plot_cost_function()

# уменьшение learning_rate до 0.00001 ошибку устраняет     
model = LinearRegression(X = X, y = y, learning_rate = 0.00001)
model.gradien_descent(n_iterations=100)
model.plot_cost_function()








