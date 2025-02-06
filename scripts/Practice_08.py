import numpy as np
import matplotlib.pyplot as plt

# загрузим данные из текстового файла
array_01 = np.loadtxt('C:/Users/sidorow/Documents/GitHub/PythonForEngineeringCalculationsFall2024/data/Practice_08_01.txt')
array_02 = np.loadtxt('C:/Users/sidorow/Documents/GitHub/PythonForEngineeringCalculationsFall2024/data/Practice_08_02.txt')


# Посмотрим на данные:
plt.scatter(array_01[:, 0], array_01[:,1], color = 'black', marker= '.')
plt.xlabel('Переменная x')
plt.ylabel('Переменная y')
plt.show()

plt.scatter(array_02[:, 0], array_02[:,1], color = 'black', marker= '.')
plt.xlabel('Переменная x')
plt.ylabel('Переменная y')
#plt.axis('Переменная x', 'Переменная y')
plt.show()




#%%
# выберем массив, с которым будем работать:
array = array_01
# разобьем данные на данные для обучения и данные для проверки регрессионной модели
# для начала, на всякий случай, массив сделаем разупорядочным 
np.random.shuffle(array)

# назначим строку для разбиения массива на два
splitting_point = int(array.shape[0]*0.9)
# массив для обучения
training_array = array[:splitting_point, :]
# массив для тестирования
tesing_array = array [splitting_point:, :]


#%%

n = 1 # степень полинома

# количество столбцов соответсвует степени полинома + 1 (+1  - для свободного члена)
X = np.ones((training_array.shape[0], n+1))
for i in range (1, n+1):
    X[:, i] = (training_array[:, 0])**i
    

# вектор y
y =  training_array [:, 1]


# коэффициенты линейного уравнения определяются аналитически по формуле из лекции
# (см. самую последнюю формулу)
phi = np.linalg.inv(X.T@X)@X.T@y


#%%
# тестируем полученную модель
# на основе данных из массива tesing_array создаем матрицу X и y
X_test = np.ones((tesing_array.shape[0], n+1))

for i in range (1, n+1):
    X_test[:, i] = (tesing_array[:, 0])**i  



y_test = tesing_array [:,1]

# модельные значения будут равны векторнуму произведению матрицы X_test на вектор коэффициентов phi 
y_model =X_test@phi 

# сравним результаты на графике
plt.scatter(tesing_array [:, 0], tesing_array [:,1], marker='.', color = 'black')
plt.scatter(tesing_array [:, 0], y_model, color = 'red')
plt.xlabel('Переменная x')
plt.ylabel('Переменная y')
plt.grid()
plt.show()


        
        
        
        
        










        
        
        
        
        
        
        
        
        
        
        
        
        
        
    


