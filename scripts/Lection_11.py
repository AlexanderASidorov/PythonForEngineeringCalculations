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
    
    def __init__(self):
        '''
        Parameters
        ----------
        a, b, c : list of floats, координата x и координата y
       
        Returns
        -------
        None.

        '''
        
        self.__a = np.array([0, 0])
        self.__b = np.array([0, 0])
        self.__c = np.array([0, 0])
        Trianngle_02.__amount +=1
        
        # двойное подчеркиване перед именем переменной означает запрет
        # на доступ к этой переменной "снаружи". Т.е. если мы, например, из
        # консоли попытаемся эту переменную изменить, у нас ничего не получится
        # в консоли будет выведена ошибка

        
    def __del__(self):
        Trianngle.amount -=1
        
    
    # для того, что бы защищенные переменные были доступны для чтения
    # снаружи, мы сделаем специальные функции, которые принято называть
    # геттерами
    
    def set_triangle_cord (self, a, b, c):
        '''
        Определение координат треугольника
        '''

        
        
        self.__a = np.array(a)
        self.__b = np.array(b)
        self.__c = np.array(c)
        
        
        
    
    
    def get_triangle_area (self):
        '''
        Рассчет площади треугольника
        '''

        coord = np.array([self.__a, self.__b, self.__c])
        
        matrix = np.array([ [  coord[0,0] - coord[2,0], coord[0,1] - coord[2,1]],
                            [coord[1,0] - coord[2,0], coord[1,1] - coord[2,1]] ])
        
        area = abs(0.5*np.linalg.det(matrix))
        
        return area
    
    def get_triangle_perimetr (self):
        '''
        Рассчет периметра треугольника
        '''
              
        ab = (np.sum((self.__a - self.__b)**2, axis=0))**0.5
        bc = (np.sum((self.__b - self.__c)**2, axis=0))**0.5
        ca = (np.sum((self.__c-self.__a)**2, axis=0))**0.5
        
        return ab+bc+ca
    


       
if __name__ == "__main__":
    # first_triangle =  Trianngle_01([0, 0], [5, 0], [2.5, 5])
    # area_01 = first_triangle.get_area()
    # perimeter_01 = first_triangle.get_perimetr() 
    
    # second_triangle =  Trianngle_01([0, 0], [10, 0], [5, 10])
    # area_02 = second_triangle.get_area()
    # perimete_02r = second_triangle.get_perimetr()
    
    
    third_triangle =  Trianngle_02()
    third_triangle.set_triangle_cord([0,0], [10, 0], [5, 10])
    area_03 = third_triangle.get_triangle_area()
    perimete_03 = third_triangle.get_triangle_perimetr() 

#%%    

'''
Наследование – процесс создания нового класса на основе существующего класса. 
Новый класс, называемый подклассом или производным классом, наследует свойства 
и методы существующего класса, называемого суперклассом или базовым классом.
'''    

import numpy as np
   
class Circle():
    """
    Расчет площади и периметра окружности по координатам ее центра
    и радиусу.
    
    """
    
    __amount = 0
    
    def __init__(self):
        '''
        Parameters
        ----------
        o, r : list of floats, координата x и координата y центра и точки, 
        лежащей на  окружности
        '''
        
        self.__o = np.array([0, 0])
        self.__r = np.array([0, 0])
        
        # радиус окружности измеряем как норму вектора проведенного
        # из точки o в точку r
        self.__radius = np.linalg.norm(self.__r - self.__o)
        
        
        
        Circle.__amount +=1
        
        
    def set_circle_cord (self, o, r):
        '''
        Определение координат и радиуса
        '''
                
        
        self.__o = np.array(o)
        self.__r = np.array(r)
        self.__radius = np.linalg.norm(self.__r - self.__o)
        
      
    
    def get_circle_area (self):
        '''
        Рассчет площади окружности
        '''
               
        return np.pi*((self.__radius)**2)
        
    def get_circle_perimetr (self):
        '''
        Рассчет периметра окружности
        '''
                
        return 2*np.pi*self.__radius
    
if __name__ == "__main__":
    first_circle = Circle()
    first_circle.set_circle_cord([0, 0], [0, 5])
    area = first_circle.get_circle_area()
    perimeter = first_circle.get_circle_perimetr()
    
    
class Simple_shape(Circle, Trianngle_02):
    
    __amount = 0
    
    def __init__(self):
        Simple_shape.__amount +=1
        
        
if __name__ == "__main__":
    first_shape = Simple_shape()
    first_shape.set_circle_cord([0, 0], [0, 5])
    circle_area = first_shape.get_circle_area()
    circle_perimeter = first_shape.get_circle_perimetr()
    
    first_shape.set_triangle_cord([0,0], [10, 0], [5, 10])
    triangle_area = first_shape.get_triangle_area()
    triangle_perimete = first_shape.get_triangle_perimetr() 
    
    
    
    
        
    
    
    
    
    
    
    
    
    