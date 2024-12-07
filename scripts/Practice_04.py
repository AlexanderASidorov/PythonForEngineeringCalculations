# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math

# генерируем равномерно распределенный список значений по оси x от -2*pi до +2*pi
# состоящий из 1000 значений (можно меньше)


# пустой список для записи значений
x=[]

# стартовая точка, откуда будем записывать значений
start_point = -2*math.pi

# шаг с которым будем добавлять значений
step = abs(2*start_point)/100

item = start_point 
while item <= abs(start_point) + step:
    x.append(round(item, 5))
    item += step
    



def check_data (x, function_type):
    '''
    Проверка исходных данных в последующих функциях

    Parameters
    ----------
    x : float, integer или iteratable.
    function_type : string, тип функции (['sin', 'cos', 'tg', 'ctg'])

    Raises
    ------
    ValueError
        проверка, что x - действительно float, integer или список из float или integer.

    Returns
    -------
    list_x : список со значениями x, даже если значение только одно.
    function_type : тип функции (['sin', 'cos', 'tg', 'ctg']).

    '''
    
    
    # если x - еденичная переменная типа float или integer, то мы просто создаем на ее
    # основе список list_x
    if isinstance(x, (float, int)):
        list_x = [x]
    # если x - сиписок, множество или кортеж, то проверяем, что все элементы этого
    # списка являются элеметами типа float или integer
    elif isinstance(x, (list, set, tuple())):
        for item in x:
            if not isinstance(item, (float, int)):
                raise ValueError ('все элементы списка должны быть типа float или integer')
        list_x = list(x)
        
    else:
        raise ValueError ('x должен быть переменной типа float, integer, либо одномерное множество с элементами типа float, integer')
        
        
    if function_type in ['sin', 'cos', 'tg', 'ctg']:
        pass
    
    else:
        function_type = 'sin'
        print ('Тип функции может быть только sin, cos, tg или ctg. Тип функции был переопределен на тип по умолчанию sin')
        
    return list_x,  function_type

    

def sin (x):
    '''
    Расчет sin для заданного списка x

    Parameters
    ----------
    x : float, integer или iteratable.

    Returns
    -------
    list of floats, значение функции на промежутке [x].

    '''
    
    list_x, _ = check_data(x, 'sin')
        
    
    
    return [round(math.sin(item), 3) for item in list_x], list_x




def cos (x):
    '''
    Расчет cos для заданного списка x

    Parameters
    ----------
    x : float, integer или iteratable..

    Returns
    -------
    list of floats, значение функции на промежутке [x].

    '''
    
    
    list_x, _ = check_data(x, 'cos')
    
    return [round(math.cos(item), 3) for item in list_x], list_x




def tg_ctg (x, function_type = 'ctg'):
    '''
    Расчет tg или ctg для заданного списка x

    Parameters
    ----------
    x : float, integer или iteratable
    function_type : string, тип функции, ctg или tg

    Returns
    -------
    function : значение функции на промежутке [x]

    '''
    
    
    
    list_x, _ = check_data(x, function_type)
    
    # Для последующего расчета необходимо посчитать cos и sin
    sin_x, _ = sin(list_x)
    cos_x, _ = cos(list_x)
    
    
    if function_type in ['tg', 'ctg']:
        pass
    
    else:
        function_type = 'tg'
        print ('Тип функции tg_ctg может быть только tg или ctg. Тип функции был переопределен на тип по умолчанию tg')
    
        
    # в зависмости от того, нужен нам tg или ctg назначаем что у нас
    # будет числителем (numinator), а что знаменателем (denuminator)
    match function_type:
        case 'tg':
            numinator = sin_x.copy()
            denuminator = cos_x.copy()
        case 'ctg':
            numinator = cos_x.copy()
            denuminator = sin_x.copy()
            
    # проблема в том, что обе функции являются прерывистыми и необходимо найти
    # точки, где знаменатель равен нулю. Для этого проделываем последующие манипуляции...    
    
    # создаем список, куда будем записывать значения функции. При этом нам необходимо
    # найти все значения x, при которых функция не существует на данном отрезке (на
    # на отрезке list_x). В этих точках функция будет равно None
    function = []
    
    # Так как некоторые точки при которой знаменатель равен 0 могли не попасть 
    # в список list_x мы ищем места перехода от отрицательных значений знаменателя
    # к положительным и наоборот. В этих местах мы добавим в список значение 
    # функции равное None, что позволит нам при построении графика функции иметь
    # разрывы
    values_near_zeros = []
    i_start = 0 
    i_end = len(denuminator)
    
    
    
    
    
    for i in range (i_start, i_end):
        j = i+1
        try:
            denuminator[j]
        except IndexError:
            break
        
        if denuminator[i] == 0:
            denuminator[i] = None
            numinator [i] = None
            list_x[i] = None
               
        elif denuminator [i] is not None and denuminator [i] > 0 and denuminator [j] <0:
            denuminator.insert(j, None)
            numinator.insert(j, None)
            list_x.insert(j, None)
            i_end +=1
            
        elif denuminator [i] is not None and denuminator [i] < 0 and denuminator [j] > 0:
             denuminator.insert(j, None)
             numinator.insert(j, None)
             list_x.insert(j, None)
             i_end +=1
        else:
            pass
  
        
    for i in range (0, len(denuminator)):
        
        if denuminator[i] is None:
            function.append(None)
        
        else:
            try:
                function.append(round(numinator[i]/denuminator[i], 3))
            except:
                function.append(None)
            
    return function, list_x


def derivative (x, function_type):
    '''
    Расчет производной sin, cos, tg или ctg для заданного x

    Parameters
    ----------
    x : float, integer или iteratable
    function_type : string, тип функции, sin, cos, ctg или tg

    Returns
    -------
    derivative : значение производной функции на промежутке [x]

    '''
    
        
    list_x, function_type = check_data(x, function_type)
    
      
    
    
    match function_type:
        case 'sin':
            derivative = cos(list_x)[0] # т.к. dsin(x)/dx = cos(x) 
            
        case 'cos':
            derivative = [item*(-1) for item in sin(list_x)[0]] # т.к. dcos(x)/dx = -sin(x)
        
        case 'tg':
            derivative = [] # dtg(x)/dx = (tg(x))**2 + 1
            tg_x, list_x = tg_ctg(list_x, 'tg')
            
            for i in range (0, len(tg_x)):
                if tg_x[i] is None:
                    derivative.append(None)
                else:
                    derivative.append(tg_x[i]**2 + 1)
                    
        case 'ctg':
             derivative = [] # dctg(x)/dx = -1 / (sin(x)**2)
             ctg_x, list_x  = tg_ctg(list_x, 'ctg')
             
             
             for i in range (0, len(list_x)):
                 if ctg_x[i] is None:
                     derivative.append(None)
                 else:
                     sin_x = sin(list_x[i])[0][0]
                     
                     derivative.append(-1/sin_x**2)
                     
    return derivative


def create_single_plot (x, y1, y2, x_lable = 'x', y1_lable = 'y1', y2_lable = 'y2'):
    '''
    Функция для построения графика функции и ее производной. Далее не используется, 
    так что можно не вчитываться
    '''
    
    
    # проверка исходных данных
    for item in [x, y1, y2]:
        if not isinstance(item, list):
            raise TypeError ('Все переменные должны быть типа list и иметь одинаковую длину!')
    
    if not len(x) == len (y1) == len(y2):
        raise ValueError ('Все переменные должны быть типа list и иметь одинаковую длину!')
    
    
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
        
    fig.set_size_inches (7, 7)
    
    # настройка разрешения
    fig.set_dpi (300)

    # построение графика функции    
    ax1.plot(x, y1, color = 'black', linestyle = '-')
    # назначаем имя оси x
    ax1.set_xlabel(x_lable)
    # назначаем имя для оси y
    ax1.set_ylabel(y1_lable, color='black')
    # добавляем сетку
    ax1.grid()
    
    # построение графика производной
    ax2.plot(x, y2, color = 'grey',  linestyle = '--')
    ax2.set_ylabel(y2_lable, color='black')
    
    return ax1, ax2, fig


#%%%
# воспользуемся выше определенными функциями и посчитаем функции и их производные
  
list_x, _ = check_data (x, 'sin')    

# функции
sin_x, _ = sin (list_x)
cos_x, _ = cos (list_x)
tg_x, list_x_tg = tg_ctg (list_x, function_type= 'tg')
ctg_x, list_x_ctg = tg_ctg (list_x, function_type= 'ctg')


# производные
derivative_sin_x = derivative (list_x, 'sin')
derivative_cos_x = derivative (list_x, 'cos')
derivative_tg_x = derivative (list_x, 'tg')
derivative_ctg_x = derivative (list_x, 'ctg')


#%%
# настройка общего вида графика

fig, (ax0, ax1) = plt.subplots(2, 2, constrained_layout=True) 

ax00 = ax0[0].twinx()
ax10 = ax1[0].twinx() 

ax01 = ax0[1].twinx()
ax11 = ax1[1].twinx() 


# можно настроить размер картинки 
fig.set_size_inches (14, 12)
# можно настроит разрешение
fig.set_dpi (300)


##################################
#### левый верхний угол ########## 
ax0[0].plot(list_x, sin_x, color='black', linestyle = '-', label = 'sin(x)') 
ax00.plot(list_x, derivative_sin_x, color='grey', linestyle = '--', label = 'dsin(x)/dx') 

ax0[0].tick_params(axis='y',  colors='black') 
ax00.tick_params(axis='y', colors='black')

# назначаем имя оси x
ax0[0].set_xlabel('x', fontsize = 24)
# выводим на экран легенду
ax0[0].legend(fontsize = 18, loc='upper left')
ax00.legend(fontsize = 18, loc='upper right')
# добавляем сетку
ax0[0].grid()


##################################
#### левый нижний угол ########## 
ax1[0].plot(list_x_tg, tg_x, color='black', linestyle = '-', label = 'tg(x)') 
ax10.plot(list_x_tg, derivative_tg_x, color='grey', linestyle = '--', label = 'dtg(x)/dx') 

ax1[0].tick_params(axis='y',  colors='black') 
ax10.tick_params(axis='y', colors='black')

# назначаем имя оси x
ax1[0].set_xlabel('x', fontsize = 24)
# выводим на экран легенду
ax1[0].legend(fontsize = 18, loc='upper left')
ax10.legend(fontsize = 18, loc='upper right')
# добавляем сетку
ax1[0].grid()


##################################
#### правый верхний угол ########## 
ax0[1].plot(list_x, cos_x, color='black', linestyle = '-', label = 'cos(x)') 
ax01.plot(list_x, derivative_cos_x, color='grey', linestyle = '--', label = 'dcos(x)/dx') 

ax0[1].tick_params(axis='y',  colors='black') 
ax01.tick_params(axis='y', colors='black')

# назначаем имя оси x
ax0[1].set_xlabel('x', fontsize = 24)
# выводим на экран легенду
ax0[1].legend(fontsize = 18, loc='upper left')
ax01.legend(fontsize = 18, loc='upper right')
# добавляем сетку
ax0[1].grid()




##################################
#### правый нижний угол ########## 
ax1[1].plot(list_x_ctg, ctg_x, color='black', linestyle = '-', label = 'ctg(x)') 
ax11.plot(list_x_ctg, derivative_ctg_x, color='grey', linestyle = '--', label = 'dctg(x)/dx') 

ax1[1].tick_params(axis='y',  colors='black') 
ax11.tick_params(axis='y', colors='black')

# назначаем имя оси x
ax1[1].set_xlabel('x', fontsize = 24)
# выводим на экран легенду
ax1[1].legend(fontsize = 18, loc='upper left')
ax11.legend(fontsize = 18, loc='upper right')
# добавляем сетку
ax1[1].grid()

plt.show()




  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
