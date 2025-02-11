# -*- coding: utf-8 -*-
import numpy as np

'''
Что такое класс?
Класс — это шаблон, который определяет структуру и поведение объектов.  Внутри 
класса можно определять методы (функции) и атрибуты (переменные).
Объект — экземпляр класса, который имеет собственные значения атрибутов.
Пример задачи:
Создадим класс Triangle, который будет рассчитывать площадь треугольника по координатам его вершин.
'''

class Triangle:
    '''
    Класс содержит следующие атрибуты: 
        координаты вершин треугольника в 2D пространстве
        площадь треугольника, расчитываемая по заданным координитам
    Класс содержит следующие методы:
        length - расчет расстояния между двумя вершинами треугольника
        area - расчет площади треугольника
    '''
    
    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Проверка типа исходных данных
        for item in (x1, y1, x2, y2, x3, y3):
            if not isinstance(item, (int, float)):
                raise TypeError("Координаты должны быть переменными типа int или float")
            
        # Координаты вершин треугольника
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        
        # Площадь треугольника
        self.s01 = self.area()

    # Метод для вычисления длины стороны между двумя точками
    def length(self, x1, y1, x2, y2):
        '''
        Расчет длины стороны треугольника по координатам вершин
        '''
        return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Метод для вычисления площади треугольника по формуле Герона
    def area(self):
        '''
        Расчет площади треугольника по формуле Герона
        '''
        # Вычисляем длины сторон
        a = self.length(self.x1, self.y1, self.x2, self.y2)
        b = self.length(self.x2, self.y2, self.x3, self.y3)
        c = self.length(self.x3, self.y3, self.x1, self.y1)

        # Периметр
        p = (a + b + c)
             
        # Площадь по формуле Герона
        s = np.sqrt(p/2*(p/2 - a)*(p/2 - b)*(p/2 - c))
            
        return s
    
    
# Создание объекта треугольника 01
triangle01 = Triangle(0, 0, 4, 0, 0, 4)
# Расчет площади
s01 = triangle01.area()


"""
Наследование
Пример: Добавим класс RightTriangle, который наследуется от Triangle и проверяет, 
является ли треугольник прямоугольным.
"""

class RightTriangle(Triangle):
    '''
    Класс содержит следующие атрибуты: 
        Наследованные от класса Triangle:
            координаты вершин треугольника в 2D пространстве
            площадь треугольника, расчитываемая по заданным координитам
        Собственные:
            check -  True если треугольник - прямоугольный, False - если нет 
    Класс содержит следующие методы:
        Наследованные от класса Triangle:
            length - расчет расстояния между двумя вершинами треугольника
            area - расчет площади треугольника
        Собственные:
            is_right - проверка условия теоремы Пифагора
            
    '''
    
    def __init__(self, x1, y1, x2, y2, x3, y3):
        # метод super() используется для вызова конструктора родительского 
        # класса, чтобы инициализировать общие атрибуты
        super().__init__(x1, y1, x2, y2, x3, y3)
        self.check = self.is_right()

    def is_right(self):
        '''
        Проверка условия теоремы Пифагора

        Returns
        -------
        True or False

        '''
        # Вычисляем длины сторон
        a = self.length(self.x1, self.y1, self.x2, self.y2)
        b = self.length(self.x2, self.y2, self.x3, self.y3)
        c = self.length(self.x3, self.y3, self.x1, self.y1)

        # Сортируем стороны по возрастанию
        sides = sorted([a, b, c])

        # Проверяем условие теоремы Пифагора
        if np.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2):
            self.check = True  # Если треугольник прямоугольный, устанавливаем check в True
            return True
        else:
            return False
    


right_triangle = RightTriangle(0, 0, 4, 0, 0, 4)


'''
Инкапсуляция - сокрытии внутренней реализации объекта и предоставлении доступа 
к его данным только через определенные интерфейсы (методы).
Мы можем сделать координаты вершин приватными, чтобы их нельзя было изменить напрямую.
'''

class Triangle_private:
    '''
    Класс содержит следующие атрибуты: 
        координаты вершин треугольника в 2D пространстве
        площадь треугольника, расчитываемая по заданным координитам
    Класс содержит следующие методы:
        get_coordinates - служит для чтения координатам треугольника
        set_coordinates - служит для записи координатам треугольника
        length - расчет расстояния между двумя вершинами треугольника
        area - расчет площади треугольника
    '''
    
    def __init__ (self, x1, y1, x2, y2, x3, y3):
        
        # Проверка типа исходных данных
        for item in (x1, y1, x2, y2, x3, y3):
            if not isinstance(item, (int, float)):
                raise TypeError("Координаты должны быть переменными типа int или float")
        
        # Координаты вершин треугольника
        self.__x1 = x1
        self.__y1= y1
        self.__x2 = x2
        self.__y2= y2
        self.__x3 = x3
        self.__y3= y3
        
        # Площадь треугольника
        self.__object_area = self.area()
        
    
    def length (self, x2, x1, y2, y1):
        '''
        Расчет длины стороны треугольника по координатам вершин
        '''
        length = np.sqrt ((x2-x1)**2 + (y2 - y1)**2)
        return length
    
    
    def area (self):
        '''
        Расчет площади треугольника по формуле Герона
        '''
        a = self.length(self.__x2, self.__x1, self.__y2, self.__y1)
        b = self.length(self.__x3, self.__x2, self.__y3, self.__y2)
        c = self.length(self.__x1, self.__x3, self.__y1, self.__y3)
        
        p = a + b+ c
        
        s = np.sqrt (p/2 * (p/2 - a) * (p/2 - b) * (p/2 - c))
        
        return s
    
    def get_coordinates (self):
        '''
        Чтение координатам треугольника из экземпляра класса
        '''
        
        return (self.__x1, self.__y1), (self.__x2, self.__y2), (self.__x3, self.__y3)
    
    
    def set_coordinates (self, x1, y1, x2, y2, x3, y3):
        '''
        Запись координат треугольника в экземпляр класса и пересчет площади 
        треугольника по заданным координатам
        '''
        # Проверка типа исходных данных
        for item in (x1, y1, x2, y2, x3, y3):
            if not isinstance(item, (int, float)):
                raise TypeError("Координаты должны быть переменными типа int или float")
        self.__x1 = x1
        self.__y1= y1
        self.__x2 = x2
        self.__y2= y2
        self.__x3 = x3
        self.__y3= y3
        
        self.__object_area = self.area()

private_triangle = Triangle_private(0, 1, 4, 0, 0, 4)
point01, point02, point03 = private_triangle.get_coordinates()
private_triangle.set_coordinates(0, 0, 10, 0, 0, 10)


'''
Полиморфизм - принцип объектно-ориентированного программирования, который 
позволяет использовать один интерфейс для работы с объектами разных типов.
Создадим функцию, которая работает с разными типами фигур 
(например, треугольник и квадрат).
'''

class Square:
    '''
    Класс содержит следующие атрибуты:
        длина стороны квадрата
        площадь квадрата, расчитываемая по заданной длине стороны
    и один метод:
        area - расчет площади квадрата
    '''
    def __init__(self, side):
        
        # Проверка типа исходных данных
        if not isinstance(side, (int, float)):
            raise TypeError("Координаты должны быть переменными типа int или float")
        
        self.side = side
        self.area_square = self.area()
             
    def area (self):
        '''
        Расчет площади квадрата
        '''
        area = self.side**2 
        return area
    
    @staticmethod
    def calculate_area (shape):
        return shape.area()
    
    

square01 = Square(4)


print (f'Площадь прямоугольника = {Square.calculate_area(square01)} мм')
print (f'Площадь треугольника = {Square.calculate_area(triangle01)} мм')
    
















