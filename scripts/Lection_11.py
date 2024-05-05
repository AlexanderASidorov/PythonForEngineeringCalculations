# -*- coding: utf-8 -*-
"""
Объектно-ориентированное программирование (ООП) – это стиль программирования, 
в которой для представления данных и для проведения операций над этими данными 
используются объекты (экземпляры класса).

Класс - шаблон для создания объекта.

Классы определяют:
    структуру данных, которые характеризуют объект;
    свойства (атрибуты) и статус (состояние) объекта;
    операции, которые можно совершать с данными объекта (методы).

"""

#%%
'''
Инкапсуляция – механизм сокрытия деталей реализации класса от других объектов. 
Достигается путем использования модификаторов доступа public, private и 
protected, которые соответствуют публичным, приватным и защищенным атрибутам.

'''

import numpy as np



# Возьмем класс, который мы создали на прошлой лекции (для расчета площади
# и периметра треугольника) и немного его переделаем, закрыв большую часть
# его переменных для доступа извне
# вот так наш класс выглядел изначально

class Trianngle():
    """
    Расчет площади и периметра треугальника по его координатам.
    
    """
    
    amount = 0
    
    def __init__(self, a, b, c):
        '''
        Parameters
        ----------
        a, b, c : list of floats, координата x и координата y
       
        Returns
        -------
        None.

        '''
        
        self.a = np.array(a)
        self.b = np.array(b)
        self.c = np.array(c)
        Trianngle.amount +=1
        
        
        self.coord = np.array([a, b, c])
        
        self.triangle_area = self.area()
        self.triangle_perimeter = self.perimeter()
        
        
    def __del__(self):
        Trianngle.amount -=1
        
    
    def area (self):
        '''
        Рассчет площади треугольника
        '''

        coord = self.coord
        
        matrix = np.array([ [  coord[0,0] - coord[2,0], coord[0,1] - coord[2,1]],
                            [coord[1,0] - coord[2,0], coord[1,1] - coord[2,1]] ])
        
        area = abs(0.5*np.linalg.det(matrix))
        
        return area
    
    def perimeter (self):
        '''
        Рассчет периметра треугольника
        '''
              
        ab = (np.sum((self.a-self.b)**2, axis=0))**0.5
        bc = (np.sum((self.b-self.c)**2, axis=0))**0.5
        ca = (np.sum((self.c-self.a)**2, axis=0))**0.5
        
        return ab+bc+ca
 

# мы закроем доступ ко всем переменным кроме исходных координат:

   
class Trianngle_01():
    """
    Расчет площади и периметра треугальника по его координатам.
    
    """
    
    __amount = 0
    
    def __init__(self, a, b, c):
        '''
        Parameters
        ----------
        a, b, c : list of floats, координата x и координата y
       
        Returns
        -------
        None.

        '''
        
        self.a = np.array(a)
        self.b = np.array(b)
        self.c = np.array(c)
        Trianngle_01.__amount +=1
        
        # двойное подчеркиване перед именем переменной означает запрет
        # на доступ к этой переменной "снаружи". Т.е. если мы, например, из
        # консоли попытаемся эту переменную изменить, у нас ничего не получится
        # в консоли будет выведена ошибка
        self.__coord = np.array([a, b, c])
        
        self.__triangle_area = self.area()
        self.__triangle_perimeter = self.perimeter()
        
        
    def __del__(self):
        Trianngle.amount -=1
        
    
    def area (self):
        '''
        Рассчет площади треугольника
        '''

        coord = self.__coord
        
        matrix = np.array([ [  coord[0,0] - coord[2,0], coord[0,1] - coord[2,1]],
                            [coord[1,0] - coord[2,0], coord[1,1] - coord[2,1]] ])
        
        area = abs(0.5*np.linalg.det(matrix))
        
        return area
    
    def perimeter (self):
        '''
        Рассчет периметра треугольника
        '''
              
        ab = (np.sum((self.a-self.b)**2, axis=0))**0.5
        bc = (np.sum((self.b-self.c)**2, axis=0))**0.5
        ca = (np.sum((self.c-self.a)**2, axis=0))**0.5
        
        return ab+bc+ca
    
    # для того, что бы защищенные переменные были доступны для чтения
    # снаружи, мы сделаем специальные функции, которые принято называть
    # геттерами
    
    def get_area (self):
        '''
        возвращает площадь треугольника
        
        '''
        
        return self.__triangle_area
    
    def get_perimetr (self):
        '''
        возвращает периметр треугольника
        
        '''

        return self.__triangle_perimeter
    
# Хорошим тоном в программировании является так же закрытия доступа ко всем 
# включая исходные данные. В этом случае взаимодействие с пользователем 
# осуществляется с помощью специальных функций 'геттеров' и 'сеттеров'.
# Еще раз перепишем наш класс, но закроем дуступ извне для a, b и c


class Trianngle_02():
    """
    Расчет площади и периметра треугальника по его координатам.
    
    """
    
    __amount = 0
    
    def __init__(self, a = [0, 0], b = [0, 0], c = [0, 0]):
        '''
        Parameters
        ----------
        a, b, c : list of floats, координата x и координата y
       
        Returns
        -------
        None.

        '''
        
        self.__a = np.array(a)
        self.__b = np.array(b)
        self.__c = np.array(c)
        Trianngle_01.__amount +=1
        
        # двойное подчеркиване перед именем переменной означает запрет
        # на доступ к этой переменной "снаружи". Т.е. если мы, например, из
        # консоли попытаемся эту переменную изменить, у нас ничего не получится
        # в консоли будет выведена ошибка
        self.__coord = np.array([a, b, c])
        
        self.__triangle_area = self.area()
        self.__triangle_perimeter = self.perimeter()
        
        
    def __del__(self):
        Trianngle.amount -=1
        
    
    def area (self):
        '''
        Рассчет площади треугольника
        '''

        coord = self.__coord
        
        matrix = np.array([ [  coord[0,0] - coord[2,0], coord[0,1] - coord[2,1]],
                            [coord[1,0] - coord[2,0], coord[1,1] - coord[2,1]] ])
        
        area = abs(0.5*np.linalg.det(matrix))
        
        return area
    
    def perimeter (self):
        '''
        Рассчет периметра треугольника
        '''
              
        ab = (np.sum((self.a-self.b)**2, axis=0))**0.5
        bc = (np.sum((self.b-self.c)**2, axis=0))**0.5
        ca = (np.sum((self.c-self.a)**2, axis=0))**0.5
        
        return ab+bc+ca
    
    # для того, что бы защищенные переменные были доступны для чтения
    # снаружи, мы сделаем специальные функции, которые принято называть
    # геттерами
    
    def get_area (self):
        '''
        возвращает площадь треугольника
        
        '''
        
        return self.__triangle_area
    
    def get_perimetr (self):
        '''
        возвращает периметр треугольника
        
        '''

        return self.__triangle_perimeter






       
if __name__ == "__main__":
    first_triangle =  Trianngle_01([0, 0], [5, 0], [2.5, 5])
    area_01 = first_triangle.get_area()
    perimeter_01 = first_triangle.get_perimetr() 
    
    second_triangle =  Trianngle_01([0, 0], [10, 0], [5, 10])
    area_02 = second_triangle.get_area()
    perimete_02r = second_triangle.get_perimetr() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    