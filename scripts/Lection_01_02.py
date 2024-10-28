# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:11:11 2022

@author: sidorow
"""

# 1. ПЕРЕМЕННЫЕ
# 2. УСЛОВНЫЙ ОПЕРАТОР IF (ELIF и ELSE)
# 3. ОПЕРАТОР ЦИКЛА WHILE
# 4. ОПЕРАТОР FOR
# 4. КОНСТРУКЦИЯ match/case
#
#
#%%
"""
Поговорим о переменных в Python


В отличии от, например, Pascal или C++ в Python не нужно заранее декларировать
переменные, т.е. вы создаете переменные по мере необходимости в процессе решения 
задачи

Если вы знаете, что далее вы этой переменной пользоваться не будете, то в общем
ее можно удалить командой del, если вы уверены, что эта переменная расчитывается 
правильно и что ошибка ее расчета не повлечет за собой дальнейшие ошибки


"""
# Типы переменных Python назначает автоматически, т.е. если вы определяете:
a = 2
b=-11
c=1.2
d=5e-5
e = 'metal'
f = 'forming and heat treatment'
# то a и b автоматически принимают тип переменной integer (целое число)
# c и d автоматически принимают тип переменной float (число с плавающей точкой)
# e и f автоматически принимают тип переменной string (текст)
#%% 
# Переменные, конечно, могут менять свой тип, т.е мы можем присвоить переменной
# a вместо значение 1 значение 1.0 или 1.1
a=2.0
# и переменная изменит свой тип с int на float
#
#
#
# Операции сложения/вычитания/умножения/деления(+ 1 * /), как и скобки работают 
# в Python как в обычном калькуляторе. Возведение в степень производится с 
#помощью знака **
g=b**a
h=b/a
# Если вам вдруг понадобилось получить целое число от деления, то его можно 
# получить с помощью двойного значка деления //
i=b//a
#
#
#%%
"""
Условный оператор if позволяет запустить некоторую последовательность 
инструкций (команд) при условии, что выполняется некое определенное условие. 
В противном случае эта последовательность не выполняется. В Python нет 
специальных ключевых слов для закрытия условного оператора. От основного "тела" 
программы последовательность внутри оператора отделяется четырьмя пробелами.
Пример работы условного оператора if был рассмотрен ранее, на первом занятии,
но давайти для наглядности скопируем его и сюда:
"""
# Решение линейного уравнения  y=kx+b
print ('Решение линейного уравнения')
print ('Введите k')
# просим пользователя ввести коэфициент k, типа float (число c плавающей запятой)
k=float(input())
# тоже самое для b
print ('Введите b')
b=float(input())
# В общем случае корень уравнения находится как x=-b/k
# Но если k и b будут равны 0, то это уравнение будет иметь бесконечное 
# множествто решений
# Этот случай описывается как
if k==0 and b==0:
    print ('Бесконечное количество корней')
# Если 0 равно только k, то кореней это уравнение не будет иметь совсем
elif k==0:
    print ('Уравнение корней не имеет')
# во всех остальных случаях корень ищем по вышепреведенной формуле
else:
    x=-b/k
    print ('x=', x)
#%%
"""
Оператор цикла while позволяет запускать цикл который будет работать до 
тех пор пока некое условие будет выполняться. 
простейший пример: у нас есть некоторое число m и мы будем делить его на 2 до 
тех пор, пока оно не станет меньше 1
"""
m=453
while m>1:
    m=m/2
# можем сделать то же самое, но посчитать сколько раз мы поделили на 2, введя 
# для подсчета количества циклов переменную j:
n=453
j=0 
while n>1:
    j=j+1
    n=n/2
# допустим нам нужно, что бы деление на 2 происходило не более 10 раз. Для этого 
# мы можем усложнить условие в операторе while
s=2000
p=s
r=0
while p>1 and r<10:
    r=r+1
    p=p/2
#%%
"""
Оператор for позволяет нам итерировать через определенный набор данных. Т.е.
предположим нам нужно разделить все то же числе 2000 (см. предыдущий пример) на 
2 10 раз. Для этого нам нужно ввести переменную q, которая будет изменятся в
в диапазоне от 0 до 10 с шагом 1:
"""
w=s
for q in range(10):
    w=w/2
    print(w)
# аналогичным образом можно создать массив z, через который будем итерационно
# прогонять переменную v (начальное ее значение =2000) деля ее на 2
v=s
z=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for t in z:
    v=v/2
    
    
#%%
"""
Конструкция match - case позволяет выбрать действие при ограниченном количестве
возможных вариантов 

"""

a = 2
b = 2
action = 'division'

match action:
    case 'addition':
        print ('a + b = ' + str(a+b))
    case 'subtraction':
        print ('a - b = ' + str(a-b))
    case 'multiplication':
        print ('a * b = ' + str(a*b))
    case 'division':
        print ('a / b = ' + str(a/b))
        





























