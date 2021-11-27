import math


class QuadraticEquation:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_discriminant(self):
        if self.__b * self.__b - 4 * self.__a * self.__c:
            return self.__b * self.__b - 4 * self.__a * self.__c
        else:
            return 0

    def get_root1(self):
        return (- self.__b + math.sqrt(self.__b * self.__b) - 4 * self.__a * self.__c) / 2 * self.__a

    def get_root2(self):
        return (- self.__b - math.sqrt(self.__b * self.__b) - 4 * self.__a * self.__c) / 2 * self.__a

