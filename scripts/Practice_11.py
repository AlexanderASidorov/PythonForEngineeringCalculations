# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


array01 = np.loadtxt('C:/Users/sidorow/Documents/GitHub/PythonForEngineeringCalculationsFall2024/data/lection10_02.txt')
array02 = np.loadtxt('C:/Users/sidorow/Documents/GitHub/PythonForEngineeringCalculationsFall2024/data/lection10_01.txt')



X01 = np.ones([array01.shape[0], array01.shape[1]])
X01[:, 1:] = array01[:, :6]
# отмасштабируем последний столбец, что бы он был близкого порядка, по сравнению с отсальными
X01[:, -1] = np.log10(X01[:, -1])

y01 = array01[:, -1]


X02 = np.ones([array02.shape[0], array02.shape[1]])
X02[:, 1:] = array02[:, :1]
y02 = array02[:, -1]

#%% Подготовка данных

class DataPreparer:
    """
    Класс для подготовки данных: разделение на обучающую и тестовую выборки с рандомизацией.
    """

    def __init__(self):
        """
        Инициализация класса.

        """
        self.__X = None
        self.__y = None
        self.__X_train = None
        self.__X_test = None
        self.__y_train = None
        self.__y_test = None

    def set_Xy(self, X, y):
        """
        Установка данных X и y.
        Parameters:
            X : 2D numpy array.
            y : 1D numpy array.
        """
        # Валидация данных
        if not isinstance(X, np.ndarray) or not isinstance(y, np.ndarray):
            raise TypeError('X и y должны быть массивами NumPy!')
        if len(X.shape) != 2:
            raise ValueError('X должен быть двумерным массивом.')
        if len(y.shape) != 1:
            raise ValueError('y должен быть одномерным массивом.')
        if X.shape[0] != y.shape[0]:
            raise ValueError('Количество строк в X и y должно быть одинаковым.')

        self.__X = X
        self.__y = y
        
        return self.__X, self.__y


    def get_Xy(self):
        """
        Получение данных X и y.
        Returns:
            tuple: (X, y)
        """
        if self.__X is None or self.__y is None:
            raise ValueError('X и y не установлены. Воспользуйтесь методом set_Xy!')
        return self.__X, self.__y



    def split_data(self, test_size=0.1, randomize=True):
        """
        Разделение данных на обучающую и тестовую выборки с возможностью рандомизации.
        Parameters:
            test_size : float, доля тестовой выборки.
            randomize : bool, флаг для рандомизации данных.
        """
        if self.__X is None or self.__y is None:
            raise ValueError('X и y не установлены. Воспользуйтесь методом set_Xy!')

        num_of_rows = self.__X.shape[0]
        test_rows = int(num_of_rows * test_size)
        train_rows = num_of_rows - test_rows

        if randomize:
            # Объединяем X и y во временный массив для рандомизации
            combined_data = np.column_stack((self.__X, self.__y))
            # Генерируем случайные индексы
            shuffled_indices = np.random.permutation(num_of_rows)
            # Перемешиваем данные
            combined_data_shuffled = combined_data[shuffled_indices]

            # Разделяем обратно на X и y
            X_shuffled = combined_data_shuffled[:, :-1]
            y_shuffled = combined_data_shuffled[:, -1]

            # Разделяем на обучающую и тестовую выборки
            self.__X_train = X_shuffled[:train_rows, :]
            self.__y_train = y_shuffled[:train_rows]
            self.__X_test = X_shuffled[train_rows:, :]
            self.__y_test = y_shuffled[train_rows:]
        else:
            # Без рандомизации
            self.__X_train = self.__X[:train_rows, :]
            self.__y_train = self.__y[:train_rows]
            self.__X_test = self.__X[train_rows:, :]
            self.__y_test = self.__y[train_rows:]


    def get_train_data(self):
        """
        Получение обучающих данных.
        Returns:
            tuple: (X_train, y_train)
        """
        if self.__X_train is None or self.__y_train is None:
            raise ValueError('Данные не разделены. Воспользуйтесь методом split_data!')
        return self.__X_train, self.__y_train



    def get_test_data(self):
        """
        Получение тестовых данных.
        Returns:
            tuple: (X_test, y_test)
        """
        if self.__X_test is None or self.__y_test is None:
            raise ValueError('Данные не разделены. Воспользуйтесь методом split_data!')
        return self.__X_test, self.__y_test
    
    
# создаем объект data_preparer     
data_preparer = DataPreparer()

# установка данных X и y
data_preparer.set_Xy(X02, y02)

# разбиваем данные на данные для обучения и данные для проверки
data_preparer.split_data(test_size=0.1, randomize=True) 

#%% Линейная регрессия с помощью нормального уравнения

class LinearRegressionNormalEquation:
    """
    Класс для вычисления коэффициентов линейной регрессии с помощью нормального уравнения.
    """

    def __init__(self):
        """
        Инициализация класса.

        """
        self.__X_train = None
        self.__y_train = None
        self.__phi = None

    def set_data_normal_equation(self, X_train, y_train):
        """
        Установка обучающих данных.
        Parameters:
            X_train : 2D numpy array.
            y_train : 1D numpy array.
        """
        if not isinstance(X_train, np.ndarray) or not isinstance(y_train, np.ndarray):
            raise TypeError('X_train и y_train должны быть массивами NumPy!')
        if len(X_train.shape) != 2:
            raise ValueError('X_train должен быть двумерным массивом.')
        if len(y_train.shape) != 1:
            raise ValueError('y_train должен быть одномерным массивом.')
        if X_train.shape[0] != y_train.shape[0]:
            raise ValueError('Количество строк в X_train и y_train должно быть одинаковым.')

        self.__X_train = X_train
        self.__y_train = y_train

    def get_train_data(self):
        """
        Получение обучающих данных.
        Returns:
            tuple: (X_train, y_train)
        """
        if self.__X_train is None or self.__y_train is None:
            raise ValueError('Обучающие данные не установлены. Воспользуйтесь методом set_train_data!')
        return self.__X_train, self.__y_train

    def set_phi_normal_equation(self):
        """
        Вычисление коэффициентов регрессии с помощью нормального уравнения.
        """
        if self.__X_train is None or self.__y_train is None:
            raise ValueError('Обучающие данные не установлены. Воспользуйтесь методом set_train_data!')

        self.__phi = np.linalg.inv(self.__X_train.T @ self.__X_train) @ self.__X_train.T @ self.__y_train

    def get_phi_normal_equation(self):
        """
        Получение коэффициентов регрессии.
        Returns:
            1D numpy array: Коэффициенты регрессии.
        """
        if self.__phi is None:
            raise ValueError('Коэффициенты еще не рассчитаны. Воспользуйтесь методом normal_equation!')
        return self.__phi


# создаем объект
normal_equation = LinearRegressionNormalEquation()


# передаем в объект normal_equation данные для обучения, которые ранее
# получили при работе с объектом  data_preparer
normal_equation.set_data_normal_equation(data_preparer.get_train_data()[0], data_preparer.get_train_data()[1])
# запускаем метод set_phi, который расчитывает коэффициенты уравнения регрессии 
normal_equation.set_phi_normal_equation()
        

#%% Линейная регрессия с помощью метода градиентного спуска
class LinearRegressionGradientDecsent:
        
    def __init__ (self):
        
        """
        Инициализация класса.

        """
        self.__X_train = None
        self.__y_train = None
        self.__initial_phi = None
        self.__phi = None
        self.__learning_rate = None # скорость обучения
     
        
    def set_data_gradient_decent(self, X_train, y_train, learning_rate = 0.001, initial_phi = None):
        """
        Установка обучающих данных.
        Parameters:
            X_train : 2D numpy array.
            y_train : 1D numpy array.
            initil_phi: 1D numpy array или None
        """
        if not isinstance(X_train, np.ndarray) or not isinstance(y_train, np.ndarray):
            raise TypeError('X_train и y_train должны быть массивами NumPy!')
        if len(X_train.shape) != 2:
            raise ValueError('X_train должен быть двумерным массивом.')
        if len(y_train.shape) != 1:
            raise ValueError('y_train должен быть одномерным массивом.')
        if X_train.shape[0] != y_train.shape[0]:
            raise ValueError('Количество строк в X_train и y_train должно быть одинаковым.')
                    

        self.__X_train = X_train
        self.__y_train = y_train
        
        
        if initial_phi is None:
            self.__initial_phi = np.zeros(self.__X_train.shape[1], dtype = float)
            self.__phi = self.__initial_phi.copy()
        else:
            if not isinstance(initial_phi, np.ndarray):
                raise TypeError(' initial_phi должey быть массивами NumPy!')
            if X_train.shape[1] != initial_phi.shape[0]:
                raise ValueError('Количество столбцов в X_train и initial_phi должно быть одинаковым.')
                          
            self.__initial_phi = initial_phi
            self.__phi = self.__initial_phi.copy()
            
        if not isinstance(learning_rate, float) or not learning_rate > 0.:
            raise TypeError(' learning_rate должey быть положительным числом с плавающей заптой!')
            
        self.__learning_rate = learning_rate
            
   
     
        
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
        mse = np.mean ((self.__X_train.dot(phi) - self.__y_train)**2)
        
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
        N, _ = self.__X_train.shape
        
        # Расчитываем значение целефой переменной при заданных заданном векторе phi
        y_pred = self.__X_train.dot(phi)
        
        # расчитываем градиент
        gradient = (2/N)*self.__X_train.T.dot(y_pred - self.__y_train)
        
        return gradient
 
    
    def set_phi_gradien_descent(self, tolerance = 1e-3, n_iterations = 100):
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
        self.__cost_function_history = []
    
           
        
        for i in range (0, n_iterations):
            
            # Расчитываем значение целефой переменной при заданных заданном векторе phi
            y_pred = self.__X_train.dot(self.__phi)
            
            # Расчитываем значение функции потерь на текущей итерации
            cost_function_i = self.cost_function(self.__phi)
            
            # записываем значение функции потерь в переменную для ее хранения
            self.__cost_function_history.append(cost_function_i)
            
            # расчитываем градиент функции потерь для данного вектора phi
            gradient_i = self.gradient_cost_function(self.__phi)
            
            # пересчитываем phi путем вычитвания из текущего phi произведения
            # скорости обучения на градиент функции потерь 
            self.__phi -= self.__learning_rate*gradient_i
            
            # Проверка того, не нашли ли мы оптимум
            if i >3 and abs( self.__cost_function_history[-1] - self.__cost_function_history[-2] ) < tolerance:
                print (f'Ранняя остановка расчета на итерации #{i}')
                break
            
            # увеличиваем значение i на одну единицу
            i+=1
            
    def get_phi_gradient_descent(self):
        """
        Получение коэффициентов регрессии.
        Returns:
            1D numpy array: Коэффициенты регрессии.
        """
        if self.__phi is None:
            raise ValueError('Коэффициенты еще не рассчитаны. Воспользуйтесь методом set_phi_gradien_descent!')
        return self.__phi
            
            

gradientdecsent = LinearRegressionGradientDecsent()
gradientdecsent.set_data_gradient_decent(X02, y02)
gradientdecsent.set_phi_gradien_descent(n_iterations = 100000)

            
#%% Класс Linear Regression

class LinearGegression (DataPreparer, LinearRegressionNormalEquation, LinearRegressionGradientDecsent):
    def __init__(self, regression_method = 'normal equation'):
        super().__init__()
        self.__regression_method = regression_method
        
    def plot_predicted_vs_actual (self, X_test, y_test, phi):
        
        y_predicted = X_test.dot(phi)
        plt.scatter(y_test, y_predicted)
        plt.plot ([min(y_test), max(y_test)], [min(y_test), max(y_test)])
        plt.xlabel('Значения для тестирования')
        plt.ylabel('Расчетные значений')
        plt.grid()
        plt.show()
 
# создаем объект класса LinearGegression        
linear_regression = LinearGegression()

# передадим в объект матрицу признаков и вектор значений функции
linear_regression.set_Xy(X01, y01)

# разобьем данные на данные для тестирования и данные для обучения
linear_regression.split_data()


# создадим переменные из данных для обучения и данных для тестирования
X_train, y_train = linear_regression.get_train_data()
X_test, y_test = linear_regression.get_test_data()

#%%
# передадим данные для обучения в нормальное уравнение
linear_regression.set_data_normal_equation(X_train, y_train)
# расчитаем коэффициенты линейной регрессии
linear_regression.set_phi_normal_equation()

# создадим переменную с коэффициентами
phi_normal_equation = linear_regression.get_phi_normal_equation()
#%%


# передадим данные для обучения с помощью метода градиентного спуска
linear_regression.set_data_gradient_decent(X_train, y_train, learning_rate = 0.1)

# расчитаем коэффициенты линейной регрессии
linear_regression.set_phi_gradien_descent(n_iterations = 100000, tolerance=1e-06)
# создадим переменную с коэффициентами
phi_gradien_descent = linear_regression.get_phi_gradient_descent()

linear_regression.plot_predicted_vs_actual(X_test, y_test, phi_normal_equation)





         
        
        
        
        
        
        
        
        
        
    
    






