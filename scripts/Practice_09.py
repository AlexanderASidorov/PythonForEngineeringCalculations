# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

array01 = np.loadtxt('C:/Users/sidorow/Documents/GitHub/PythonForEngineeringCalculationsFall2024/data/lection10_02.txt')
array02 = np.loadtxt('C:/Users/sidorow/Documents/GitHub/PythonForEngineeringCalculationsFall2024/data/lection10_01.txt')


array = array01.copy()

X = np.ones([array.shape[0], array.shape[1]])


X[:, 1:] = array[:, :6]
y = array[:, -1]


X02 = np.ones([array02.shape[0], array02.shape[1]])


X02[:, 1:] = array02[:, :1]
y02 = array02[:, -1]




class LinearRegression:
        
    def __init__ (self, X = None, y = None, phi = None):
        self.__X = X 
        self.__y = y
        self.__phi = phi
     
        
    def set_Xy (self, X, y, test_size = 0.1):
        '''
        Сеттер класса LinearRegression

        Parameters
        ----------
        X : 2D numpy array.
        y : 1D numpy array.
        '''
        
        # data validation
        if not isinstance(X, np.ndarray) or not isinstance(y, np.ndarray):
            raise TypeError ('X и y должны быть массивами NumPy!!!!!!')
            
        if len (X.shape) != 2:
            raise ValueError ('X должен быть двумерным массивом')
        
        if len (y.shape) != 1:
            raise ValueError ('y должен быть одномерным массивом')    
        
        if X.shape[0] != y.shape[0]:
            raise ValueError ('Количество строк в X и y должно быть одинаковым')

        self.__X = X
        self.__y = y
        
        self.split_data(test_size)
        self.normal_equation()
        
        
    def get_Xy (self):
        '''
        Сеттер класса LinearRegression

        '''
        return self.__X, self.__y
    
    def get_phi (self):
        
        if self.__phi is None:
            raise ValueError ('Кажется коэффициенты еще не расчитаны')
        
        return self.__phi 
        
        
        
    
    def split_data (self, test_size):
        '''
        Разбивает данные на данные для обучения и данные для проверки

        '''
        
        
        if self.__X is None or self.__y is None:
            raise ValueError ('X и y не установлены. Воспользуйтесь методом set_Xy!')
        
        
        num_of_raws = self.__X.shape[0]
        test_rows = int (num_of_raws * test_size)
        train_rows = num_of_raws - test_rows
        
        self.__X_train = self.__X[:train_rows, :]
        self.__y_train = self.__y[:train_rows]
        
        self.__X_test = self.__X[:test_rows, :]
        self.__y_test = self.__y[:test_rows]
        
        
    def normal_equation (self):
        
        if self.__X is None or self.__y is None:
            raise ValueError ('X и y не установлены. Воспользуйтесь методом set_Xy!')
        
        self.__phi = np.linalg.inv(self.__X.T@self.__X)@self.__X.T@self.__y
        
    def evaluate_results (self):
        
        if self.__X is None or self.__y is None:
            raise ValueError ('X и y не установлены. Воспользуйтесь методом set_Xy!')
        
        # Посчитаем значение y для X_test по phi
        y_pred = self.__X_test.dot(self.__phi)
        
        # Создадим график
        plt.figure (figsize=(8,6))
        plt.scatter(self.__y_test, y_pred)
        plt.plot ([min(self.__y_test), max(self.__y_test)], [min(self.__y_test), max(self.__y_test)], color = 'red')
        plt.xlabel ('Экспериментальные значения (y_test)')
        plt.ylabel ('Модельные значения (y_pred)')
        plt.grid()
        plt.show()
        
        
        
        
       
        
regresion_example = LinearRegression()
regresion_example.set_Xy(X, y, test_size = 0.2)
# regresion_example.split_data(0.1)
# regresion_example.normal_equation()

print (f'коэффициенты линейной регрессии равны: {regresion_example.get_phi()}')
regresion_example.evaluate_results()


regresion_example.set_Xy(X02, y02, test_size = 0.2)
print (f'коэффициенты линейной регрессии равны: {regresion_example.get_phi()}')
regresion_example.evaluate_results()



        
        
    
