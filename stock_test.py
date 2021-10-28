from classes_and_objects_chp7.stock import Stock


def main():

    INTC = Stock("XYZ", "ABC", 20.5, 20.35)
    print("The price change percentage for", INTC.get_name(), "is", INTC.get_change_percent())


main()