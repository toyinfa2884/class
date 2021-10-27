from classes_and_objects_chp7.bmi import BMI


def main():
    bmi1 = BMI("John Doe", 18, 145, 70)
    print("The BMI for", bmi1.get_name(), "is", bmi1.get_bmi(), bmi1.get_status())

    bmi2 = BMI("John Willey", 50, 215, 70)
    print("The BMI for", bmi2.get_name(), "is", bmi2.get_bmi(), bmi2.get_status())


main()