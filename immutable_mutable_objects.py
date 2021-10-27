from classes_and_objects_chp7.circle import Circle


def print_area(c, times):
    print("Radius \t\t\tArea")
    while times >= 1:
        print(c.radius, "\t\t\t", c.get_area())
        c.radius += 1
        times -= 1



def main():

    myCircle = Circle()
    n = 5
    print_area(myCircle, n)
    print("\nRadius is", myCircle.radius)
    print("n is", n)


main()
