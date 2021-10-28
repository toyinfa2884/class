class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.__width = width
        self.__height =height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height
