from classes_and_objects_chp7.circle import Circle


def main():
    circle1 = Circle()
    print("The area of the circle of radius", circle1.radius, "is", circle1.get_area())

    circle2 = Circle(25)
    print("The area of the circle of radius", circle2.radius, "is", circle2.get_area())

    circle3 = Circle(125)
    print("The area of the circle of radius", circle3.radius, "is", circle3.get_area())

    circle3.set_radius(100) # or circle3.radius = 100
    print("The  new area of the circle of radius", circle3.radius, "is", circle3.get_area())

    circle1 = Circle()
    print("The perimeter of the circle of radius", circle1.radius, "is", circle1.get_perimeter())

    circle2 = Circle(25)
    print("The perimeter of the circle of radius", circle2.radius, "is", circle2.get_perimeter())

    circle3 = Circle(125)
    print("The perimeter of the circle of radius", circle3.radius, "is", circle3.get_perimeter())

    circle3.set_radius(100)
    print("The new perimeter of the circle of radius", circle3.radius, "is", circle3.get_perimeter())


main()