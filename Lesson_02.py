# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:11:11 2022

@author: sidorow
"""

# Поговорим о переменных в Python
#
#
# В отличии от, например, Pascal или C++ в Python не нужно заранее декларировать
# переменные, т.е. вы создаете переменные по мере необходимости в процессе решения задачи
#
# Если вы знаете, что далее вы этой переменной пользоваться не будете, то в общем
# ее можно удалить командой del, если вы уверены, что эта переменная расчитывается 
# правильно и что ошибка ее расчета не повлечет за собой дальнейшие ошибки
#
#
#
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
# в Python как в обычном калькуляторе. Возведение в степень производится с помощью знака **
g=b**a
h=b/a
# Если вам вдруг понадобилось получить целое число от деления, то его можно 
# получить с помощью двойного значка деления //
i=b//a
#
#
#%%
# Условный оператор if позволяет запустить некоторую последовательность инструкций
# (команд) при условии, что выполняется некое определенное условие. В противном случае
# эта последовательность не выполняется. В Python нет специальных ключевых слов для
# закрытия условного оператора. От основного "тела" программы последовательность
# внутри оператора отделяется четырьмя пробелами.
# Пример работы условного оператора if был рассмотрен ранее, на первом занятии,
# но давайти для наглядности скопируем его и сюда:
# Решение линецного  y=kx+b
print ('Решение линейного уравнения')
print ('Введите k')
# просим пользователя ввести коэфициент k, типа float (число c плавающей запятой)
k=float(input())
# тоже самое для b
print ('Введите b')
b=float(input())
# В общем случае корень уравнения находится как x=-b/k
# Но если k и b будут равны 0, то это уравнение будет иметь бесконечное множествто решений
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
































