class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    __speed = 0
    __bool = False
    __radius = 5.0
    __color = "blue"

    def __init__(self, speed= SLOW, bool = False, radius = 5, color = "blue"):
        self.__speed = speed
        self.__bool = bool
        self.__radius = radius
        self.__color = color

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_bool(self):
        return self.__bool

    def set_bool(self, bool):
        self.__bool = bool

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
