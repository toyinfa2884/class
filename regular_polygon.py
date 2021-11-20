import math


class RegularPolygon:
    __n = int(3)
    __side = float(1.0)
    __x = float(0.0)
    __y = float(0.0)

    def __init__(self, n = 3, side = 1, x = 0, y = 0,):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def get_n(self):
        return self.__n

    def set_n(self, n):
        self.__n = n

    def get_side(self):
        return self.__side

    def set_side(self, side):
        self.__side = side

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_perimeter(self):
        return self.__n

    def get_area(self):
        return self.__n * self.__side *self.__side / 4 * math.tan(3.141592653589793 / self.__n)
