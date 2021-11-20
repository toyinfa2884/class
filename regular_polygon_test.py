from classes_and_objects_chp7.regular_polygon import RegularPolygon


def main():

    polygon1 = RegularPolygon()
    print("The perimeter of polygon1 is ", polygon1.get_perimeter(), "and the area is ", polygon1.get_area())

    polygon2 = RegularPolygon(6, 4)
    print("The perimeter of polygon2 is ", polygon2.get_perimeter(), "and the area is ", polygon2.get_area())

    polygon3 = RegularPolygon(10, 4, 5.6, 7.8)
    print("The perimeter of polygon3 is ", polygon3.get_perimeter(), "and the area is ", polygon3.get_area())


main()
