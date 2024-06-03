# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Посмотрим как работаем простейшая линецная регрессия


# сгенерируем данные для первой учебной задачи по линейной регрессии как
# y = f(x) (y = kx + b), т.е. как функцию одной переменной
x_01  = 10*np.random.rand(1,50)
y_01 = 2*x_01 +5 + 2*np.random.rand(1,50)

# визуализируем получившиеся данные
plt.scatter(x_01, y_01, marker='.')


## для построения линейной регрессии из библиотеки sklearn необходимо импортировать
# модуль линейной регрессии
from sklearn.linear_model import LinearRegression

# для начала создадим модель (экземпляр класса LinearRegression):
model_01 = LinearRegression (fit_intercept=True)

# fit_intercept означает, что мы будем расчитывать свободный коэффициент
# уравнения y = kx + b

# для дальнейшей работы с библиотекой sklearn данные (x) необходимо представлять в
# в виде массива размерностью [n_samples, n_features], т.е. сейчас нам необходимо
# [50, 1]:
    
x_01 = x_01.transpose()


# массив y должен быть длиной = n_features, т.е. 
y_01 = y_01[0]

# далее "обучаем" нашу модель:
model_01.fit(x_01, y_01)

# Посмотрим какие получились коэффициенты уравнения y = kx + b
print(model_01.coef_)
print(model_01.intercept_)  


# визуализируем получившийся результат, для чего создадим переменную x_test
# со значениями x
x_test_01 = np.linspace(0, 10, 11)
# преобразуем ее в вектор-столбец
x_test_01 = x_test_01[:, np.newaxis]

# и определим для каждого x_test расчетное значение y
y_test_01 = model_01.predict(x_test_01)

# посмотрим эти данные на общем графике
fig01 = plt.figure()
fig01.set_size_inches(8.0, 5.0)
fig01.set_dpi(600)

plt.scatter(x_01, y_01, marker='.')
plt.plot(x_test_01, y_test_01)

#%%
# Усложним задачу, сделав ее "немного" нелинейной:
x_02  = 10*np.random.rand(1,50)
y_02 = x_02**2 +5 + 5*np.random.rand(1,50)

# визуализируем получившиеся данные
plt.scatter(x_02, y_02, marker='.')


# коэффициенты будем искать в виде полинома второго порядка, т.е.
# y = a0 + a1*x + a2*x**2
# для этого воспользуемся модулем PolynomialFeatures:

from sklearn.preprocessing import PolynomialFeatures
poly_features_02 = PolynomialFeatures(degree = 2)

# приведем x к нужному формату
X = x_02.copy().transpose()

# массив y должен быть длиной = n_features, т.е. 
y_02 = y_02[0]

# с помощью класса poly_features преобразуем данные X в вид
# y = a0 + a1*x + a2*x**2 т.е. нужно добавим к X второй столбец, равный X**2  
X_02_poly = poly_features_02.fit_transform(X)

# создадим модель (экземпляр класса LinearRegression):
model_02 = LinearRegression (fit_intercept=True)
# "обучим" ее:
model_02.fit(X_02_poly, y_02)

# визуализируем получившийся результат, для чего создадим переменную x_test
# со значениями x
x_test_02 = np.linspace(0, 10, 11)
# преобразуем ее в вектор-столбец
x_test_02 = x_test_02[:, np.newaxis]
# и к этому ветору столбцу добавим столбец с X**2  
X_test_02_poly = poly_features_02.fit_transform(x_test_02) 

# и определим для каждого x_test расчетное значение y
y_test = model_02.predict(X_test_02_poly)

# посмотрим эти данные на общем графике
fig02 = plt.figure()
fig02.set_size_inches(8.0, 5.0)
fig02.set_dpi(600)

plt.scatter(x_02, y_02, marker='.')
plt.plot(x_test_02, y_test)





#%% Усложним задачу и посмотрим регрессию с большим количеством переменных
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression





# для этого импортируем подготовленный занарее датасет с данными
# зависимости твердости стали от ее химического состава и характера термической
# обработки
dataset = pd.read_csv('../data/Lection_15.csv')

# датасет нужно немного почистить:
# Найдем есть ли в датасете колонки со всеми нулевыми значениями
zero_cols = dataset.columns[(dataset == 0).all()]
# удаляем эти колонки
dataset.drop(labels=zero_cols, axis=1, inplace=True)


# найдем строки, где t85>500 (это значит, что охлаждение медленнее, чем просто
# на воздухе)
t85_gth_500 = dataset[(dataset.t85>500.0)]
# удалим эти строки
dataset.drop(index=t85_gth_500.index, axis=0, inplace = True)


# преобразовываем все столбцы датасетка кроме HV_total в массив numpy 
# Итого получаем 12 независимых переменных
X_03 = dataset.drop(dataset.columns[-1],axis=1).to_numpy()

# и одно значение функции (один y)
y_03 = dataset.iloc[:, -1].to_numpy()



# т.к. проверить результат расчета коэффициентов визуально в данном случае 
# невозможно (из-за многомерности пространства), принято разбивать датасет на 
# две части: для "обучения" и для "проверки". Делается это с помощью модуля
# train_test_split 
from sklearn.model_selection import train_test_split

# разобьем данные:
X_03_train, X_03_test, Y_03_train, Y_03_test = train_test_split(X_03, y_03, test_size=0.2)

# создадим модель (экземпляр класса LinearRegression):
model_03 = LinearRegression (fit_intercept=True)
# обучим эту модель
model_03.fit(X_03_train, Y_03_train)
# протестируем получившуюся модель с помощью оставшихся 10% данных (X_03_test
# и Y_03_test)
print (model_03.score(X_03_test, Y_03_test))

#%%
# попробуем увеличить точность модели за счет увеличения степени полинома
from sklearn.preprocessing import PolynomialFeatures


poly_features_04 = PolynomialFeatures(degree = 2, interaction_only=False)
# interaction_only означает наличие или отсутсвие квадратичного члена, т.е.
# в случае True у нас уравнение будет в виде y = a0 + a1*x1 + a2*x2 + a3*x1*x2
# в случае False (по-умолчанию):
#           y = a0 + a1*x1 + a2*x2 + a3*x1*x2 + a4*x1**2 + a5*x2**2

X_04_train_poly = poly_features_04.fit_transform(X_03_train)
X_04_test_poly = poly_features_04.fit_transform(X_03_test)

Y_04_train = Y_03_train.copy()
Y_04_test = Y_03_test.copy()

# создадим модель (экземпляр класса LinearRegression):
model_04 = LinearRegression (fit_intercept=True)
# обучим эту модель
model_04.fit(X_04_train_poly, Y_04_train)

# протестируем получившуюся модель с помощью оставшихся 10% данных (X_04_test_poly
# и Y_04_test)
print (model_04.score(X_04_test_poly, Y_04_test))


# Проверим результат "в лоб"


# номер строки из датасета
line_number = 0

x_from_dataset = dataset.iloc[line_number, :-1].to_numpy().reshape(1, -1)
x_from_dataset_poly = poly_features_04.fit_transform(x_from_dataset)

print(model_04.predict(x_from_dataset_poly))






























 




