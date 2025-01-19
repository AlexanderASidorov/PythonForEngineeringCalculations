import numpy as np
import matplotlib.pyplot as plt

# загрузим данные из текстового файла
# столбец 0 - содержание углерода
# столбец 1 - содержание марганца
# столбец 2 - содержание кремния
# столбец 3 - содержание никеля
# столбец 4 - содержание хрома
# столбец 5 - скорость охлаждения
# столбец 6 - твердость по Викерсу
array_02 = np.loadtxt('lection10_02.txt')
array_01 = np.loadtxt('lection10_01.txt')


array = array_01
# разобьем данные на данные для обучения и данные для проверки регрессионной
# модели
splitting_point = int(array.shape[0]*0.8)
training_array = array[:splitting_point, :]
tesing_array = array [splitting_point:, :]


# построим сначала модель завасимости твердости от содержания углерода
# т.е. уравнение будем иметь вид HV = a*C + b, где С - содержание углерода

# Матрица X для обучения будет состоять из двух столбцов, первый из котороых 
# всегда равен 1, т.к. служит для расчета свободного коэффициента:
X = np.ones((training_array.shape[0], training_array.shape[1]))
X[:, 1:] = training_array[:, :-1]  
# вектор y
y =  training_array [:, -1]

# коэффициенты линейного уравнения определяются аналитически по формуле из лекции
# (см. самую последнюю формулу)
phi = np.linalg.inv(X.T@X)@X.T@y


#%%
# тестируем полученную модель
# на основе данных из массива tesing_array создаем матрицу X и y
X_test = np.ones((tesing_array.shape[0], tesing_array.shape[1]))
X_test[:, 1:] = tesing_array[:, :-1]  
y_test = tesing_array [:,1]

# модельные значения будут равны векторнуму произведению матрицы X_test на вектор коэффициентов phi 
y_model =X_test@phi 

# сравним результаты на графике
plt.scatter(tesing_array [:, 0], tesing_array [:,1], marker='x')
plt.scatter(tesing_array [:, 0], y_model)
plt.show()


        
        
        
        
        










        
        
        
        
        
        
        
        
        
        
        
        
        
        
    


