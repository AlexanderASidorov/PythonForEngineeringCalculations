# -*- coding: utf-8 -*-


import numpy as np


class Quad():
    """
    Расчет площади и периметра прямоугольника по его координатам.
    """
    
    def __init__(self, a, b, c, d):
        '''
        Parameters
        ----------
        a, b, c, d : list of floats, координата x и координата y
       
        Return
        -------
        None.

        '''
        
        self.a = np.array(a)
        self.b = np.array(b)
        self.c = np.array(c)
        self.d = np.array(d)
        
        if self.check_duplicates() == 4: 
               
            self.coordinates = self.sort_by_y()
            
            self.a_ = self.coordinates[self.coordinates[:, 1].argsort()][0, :]
            
            self.angles = np.zeros(3)
            self.lengths = np.zeros(3)
            
            
            for i in range (0, 3):
                self.angles[i], self.lengths = self.get_angle_len(self.coordinates[i+1, :])
                
            
            self.coord_quad = self.assemble_quad ()
            self.area = self.quad_area()
            self.perimeter = self.quad_perimeter
        
        
        
        
        else:
            print('Точки не должны дублировать друг друга')
            
    def check_duplicates (self):
        
        list_of_points = [self.a, self.b, self.c, self.d]
        
        set_of_points = set(tuple(item) for item in list_of_points)
        
        return len(set_of_points)
        
        
    def move2positive (self):
        '''
        Переносим все точки в позитивное пространство

        Returns
        -------
        coord_positive : numpy array of floats

        '''
        
        
        coord = np.array([self.a, self.b, self.c, self.d])
        coord_positive = np.zeros(coord.shape)
        coord_positive[:, 0] = coord[:, 0] - np.min(coord[:, 0])
        coord_positive[:, 1] = coord[:, 1] - np.min(coord[:, 1])
        return coord_positive
    
    
    def sort_by_y(self):
        '''
        
        Сортируем все точки по возрастанию координаты y

        Returns
        -------
        sorted_by_y : numpy array of floats

        '''
        # переводим координаты в позитивное пространство
        coord_positive = self.move2positive()
        
        # сортируем массив по координате y от меньшей к большей 
        sorted_by_y = coord_positive[coord_positive[:, 1].argsort()]
        
        return sorted_by_y        
    
    
    
    def get_angle_len (self, point):
        '''
        Выбираем точку a_ , которая лежит на оси x и от нее провидм векторы
        к остальным точка. Расчитываем угол между ветором и осью y

        Parameters
        ----------
        point : numpy array с координатами точки

        Returns
        -------
        angle : float, угол
        len_vector : float, длина вектора

        '''
        
        
        a_=self.a_
        
        # строим вектор от точки до точки a
        vector = point - a_
        
        # угол будем мерить относитльно вектора [0, 1], т.е. относительно
        # оси y
        refvec = np.array([0, 1])
        
        # длина вектора
        len_vector = np.linalg.norm(vector)
        
        # единичный вектор, ассоциативный с исходным
        normalized = (1/len_vector)*vector
        
        # точечное произведение единичного вектора и референса
        dotprod = np.dot(normalized, refvec)
        
        # векторное произведение
        crossprod = np.cross(normalized, refvec)
        
        # угол между вектором и осью y
        
        angle = np.arctan2(crossprod, dotprod)
        
        return angle, len_vector

       
    
    
    def assemble_quad (self):
        '''
        Собираем четырехугольник

        Returns
        -------
        coord_quad : numpy array с координатами в порядке от a до d.

        '''
        
        # т.к. точкой a мы задались с самого начала (как точка с наименьшей
        # координатой по y), то далее нам необходимо отсортировать оставшиеся
        # точки. Т.е. создаем массив из трех точек
        array2sort = self.coordinates[1:, :]
        
        # создаем пустой массив, куда запишем потом координаты в правильном порядке
        coord_quad = np.zeros(self.coordinates.shape)
        
        # критерием сортировки будет угол вектора от точки a до одной из
        # трех оставшихся точек
        # переменная sort_criteria это индексы массивы self.angles от мешьшего
        # к большему
        sort_criteria = np.argsort(self.angles)
        
        # отсортированный масив трех точек
        sorted_array = array2sort[sort_criteria]
        
        # собираем массив с координатами в порядке от a до d
        coord_quad [0, :] = self.a_
        coord_quad [1:, :] = sorted_array
        
        
                     
        return coord_quad
        
         
        
        
    
    def triangle_area (self, a, b, c):
        '''
        Рассчет площади треугольника
        '''

        coord = np.array([a, b, c])
        
        matrix = np.array([ [  coord[0,0] - coord[2,0], coord[0,1] - coord[2,1]],
                            [coord[1,0] - coord[2,0], coord[1,1] - coord[2,1]] ])
        
        triangle_area = abs(0.5*np.linalg.det(matrix))
        
        return triangle_area
    
    def quad_area (self):
        '''
        Расчет площади четырехуголника по площадям двух треугольников его
        образующих

        Returns
        -------
        None.

        '''
        # площадь треугольника abc
        area_traingle_01 = self.triangle_area(self.coord_quad[0, :],
                                              self.coord_quad[1, :],
                                              self.coord_quad[2, :])
        # площадь треугольника acd
        area_traingle_02 = self.triangle_area(self.coord_quad[0, :],
                                              self.coord_quad[2, :],
                                              self.coord_quad[3, :])
        # площадь четырехугольника
        quad_area = area_traingle_01 + area_traingle_02
        
        return quad_area
        
    
    
    
    
    def quad_perimeter (self):
        '''
        Рассчет периметра четырехугольника
        '''
        
              
        ab = (np.sum((self.coord_quad[0, :]-self.coord_quad[1, :])**2, axis=0))**0.5
        bc = (np.sum((self.coord_quad[1, :]-self.coord_quad[2, :])**2, axis=0))**0.5
        cd = (np.sum((self.coord_quad[2, :]-self.coord_quad[3, :])**2, axis=0))**0.5
        da = (np.sum((self.coord_quad[3, :]-self.coord_quad[0, :])**2, axis=0))**0.5
        
        return ab+bc+cd+da
  
        
if __name__ == "__main__":
    first_quad =  Quad([0, 0], [2.5, 5.5], [0, 6.2], [5, 0])
    second_quad =  Quad([0, 0], [-5, 0], [-2.5, -5], [0, -6])
    third_quad =  Quad([5, 4], [-5, 0], [-2.5, -5], [0, 6])
    fourth_quad =  Quad([-6, 6], [-9, -1], [-2, -3], [-8, -6])
    fifth_quad =  Quad([0, 0], [10.4, 0], [9.778, 10], [0, 10])
    
             
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
    
