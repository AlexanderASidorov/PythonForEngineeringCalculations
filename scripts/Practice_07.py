# -*- coding: utf-8 -*-

'''
                Корреляция и косинусное сходство.
Коэффициент корреляции – это одно число, которое количественно описывает 
линейную взаимосвязь между двумя переменными. Коэффициенты корреляции 
варьируются от –1 до +1, причем –1 указывает на идеальную отрицательную 
взаимосвязь, +1 – на идеальную положительную взаимосвязь, а 0 указывает на
отсутствие линейной взаимосвязи.                
'''
import numpy as np
import matplotlib.pyplot as plt




N = 50




# set up figure
#_,axs = plt.subplots(2,2,figsize=(6,6))

fig, axs = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(12.0, 12.0)
fig.set_dpi(900)
plt.subplots_adjust(left=None,
                    bottom=None, 
                    right=None, 
                    top=None, 
                    wspace=0.3, 
                    hspace=0.3)




# позитивная корреляция

x01 = np.linspace(0,10,N) + np.random.randn(N)
y01 = x01 + np.random.randn(N)

axs[0,0].plot(x01,y01,'k.')
axs[0,0].set_title('Позитивная корреляция')
axs[0,0].set_xlabel('Переменная x')
axs[0,0].set_ylabel('Переменная y')




# негативная корреляция
x02 = x01.copy()
y02 = -y01.copy()

axs[0,1].plot(x02, y02,'k.')
axs[0,1].set_title('Негативная корреляция')
axs[0,1].set_xlabel('Переменная x')
axs[0,1].set_ylabel('Переменная y')



# нулевая корреляция #01
x03 = np.random.randn(N)
y03 = np.random.randn(N)

axs[1,0].plot(x03, y03,'k.')
axs[1,0].set_title('Нулевая корреляция')
axs[1,0].set_xlabel('Переменная x')
axs[1,0].set_ylabel('Переменная y')



# нулевая корреляция #02
x04 = np.cos(np.linspace(0,2*np.pi,N)) + np.random.randn(N)/20
y04 = np.sin(np.linspace(0,2*np.pi,N)) + np.random.randn(N)/20

axs[1,1].plot(x04, y04,'k.')
axs[1,1].set_title('Нулевая корреляция')
axs[1,1].set_xlabel('Переменная x')
axs[1,1].set_ylabel('Переменная y')




def pearson (x, y):
    '''
    функция для расчета Коэффициента корреляции (коэф Пирсона)

    Parameters
    ----------
    x : 1D numpy array.
    y : 1D numpy array.

    Returns
    -------
    pearson : float, коэффициент Пирсена

    '''
    # нормализуем x и y
    xm  = x-np.mean(x)
    ym  = y-np.mean(y)
    
    # числитель
    numirator = np.dot(xm , ym)
    # знаменатель
    denumirator = np.linalg.norm(xm) * np.linalg.norm(ym)
    # коэффициент
    pearson = numirator/denumirator
    return pearson
    
pearson01 = pearson(x01, y01)
pearson02 = pearson(x02, y02)
pearson03 = pearson(x03, y03)  
pearson04 = pearson(x04, y04)    
   

def cosin (x, y):
    '''
    функция для расчета косинусного сходства

    Parameters
    ----------
    x : 1D numpy array.
    y : 1D numpy array.

    Returns
    -------
    pearson : float, косинусное сходство

    '''   
    
    # числитель
    numirator = np.dot(x,y) 
    # знаменатель
    denumirator = np.linalg.norm(x) * np.linalg.norm(y)
    cos = numirator / denumirator
    return cos

cos01 = cosin(x01, y01)
cos02 = cosin(x02, y02)
cos03 = cosin(x03, y03)
cos04 = cosin(x04, y04)

#%%
'''
Проверим зачем нам модет понадобится нормализация, которая используется в 
коэффициенте Пирсона
'''

# Создаем вектор x
x = np.arange(10, dtype=float)
# создаем вектор смещения
delta = np.arange(-10, 11)
# это еще не y. y далее мы будем получать как сумму вектора x и скаляра delta[i]


# создаем пустой массив для записи резултатов расчета коэффициента Пирсона и
# косинусового сходства
results = np.zeros((len(delta),2))

# запускаем цикл:
for i in range(len(delta)):
    y = x + delta[i]
    results[i,:] = pearson(x, y), cosin(x, y)
    



# Выводим результаты на график
fig = plt.figure()
fig.set_size_inches(12.0, 6.0)
fig.set_dpi(900)

plt.plot(delta, results[:, 0], 'k.', label = 'Pearson')
plt.plot(delta, results[:, 1], 'r', label = 'Cosin')
plt.legend()
plt.xlabel('Cмещение y относительно x')
plt.ylabel('Коэф. Пирсона или косинусово сходство')


# Для лучшего понимания выводим зависимость y от x для некоторых i
fig01 = plt.figure()
fig01.set_size_inches(12.0, 6.0)
fig01.set_dpi(900)

plt.plot(x, x + delta[0], 'k.', label = '-10')
plt.plot(x, x + delta[5], 'r*', label = '-5')
plt.plot(x, x + delta[7], 'gx', label = '-3')


plt.legend()
plt.xlabel('x')
plt.ylabel('y')
















   
