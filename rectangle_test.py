from classes_and_objects_chp7.rectangle import Rectangle


def main():
    rectangle1 = Rectangle()
    print("The area of a rectangle with width = ", rectangle1.get_width(), "and height = ", rectangle1.get_height(),
          "is", rectangle1.get_area())
    print("The perimeter of a rectangle with width = ", rectangle1.get_width(), "and height = ", rectangle1.get_height(),
          "is", rectangle1.get_perimeter())

    rectangle2 = Rectangle(4, 40)
    print("The area of a rectangle with width = ", rectangle2.get_width(), "and height = ", rectangle2.get_height(),
          "is", rectangle2.get_area())
    print("The perimeter of a rectangle with width = ", rectangle2.get_width(), "and height = ", rectangle2.get_height(),
          "is", rectangle2.get_perimeter())

    rectangle3 = Rectangle(3.5, 35.7)
    print("The area of a rectangle with width = ", rectangle3.get_width(), "and height = ", rectangle3.get_height(),
          "is", rectangle3.get_area())
    print("The perimeter of a rectangle with width = ", rectangle3.get_width(), "and height = ", rectangle3.get_height(),
          "is", rectangle3.get_perimeter())



main()
