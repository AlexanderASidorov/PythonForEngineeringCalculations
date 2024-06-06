# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:30:35 2024

@author: sidorow
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Practice_09 import plot_initial_data, plot_clustering_results
from sklearn.cluster import KMeans


# считаем исходные данные
data = pd.read_csv('../data/Practice_15.csv')


# количество кластеров
k = 7
# исходные центроиды (можно и без них)
centroids = np.array([[40, 1.5], 
                      [50, 1.6], 
                      [60, 1.7], 
                      [70, 1.8], 
                      [80, 1.9],
                      [90, 2.0],
                      [100, 2.1]])



# # подготовим данные
# # метки
# y = data['Индекс массы тела'].to_numpy()
# # признаки
# X =  data[['Масса', 'Рост']].to_numpy()


#y = data['Рост'].to_numpy()
X =  data[['Масса', 'Рост']].to_numpy()




# посмотрим исходные данные, для чего мы импортировали функцию plot_initial_data
# из файла Practice_09.py
plt.scatter(X[:,0], X[:, 1], marker = '.', c = 'black')



# создадим объект класса KMeans
model = KMeans(n_clusters=k, init=centroids, n_init= 100)
# и обучим его
model.fit(X)



# если у нас появляются новые данные, то мы можем  проверить к какой группе
# новая точка будет относиться
test_point = np.array([65, 2.01]).reshape(1, -1)
print(model.predict(test_point))

# создадим переменную, которая будет хранить номер группы, к которой относится
# тот или иной человек из выборки
groupidx = model.predict(X)

# визуализируем результат с помощью функции plot_clustering_results из файла
# Practice_09.py
plot_clustering_results (X[:, 0], X[:, 1], groupidx, 
                        'Масса человека, кг', 'Рост человека, м', 
                        'Рост и индекс массы тела человека')

























