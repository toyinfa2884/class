from classes_and_objects_chp7.fan import Fan


def main():
   fan1 = Fan()
   fan1.set_bool(True)
   fan1.set_speed(3)
   fan1.set_radius(10)
   fan1.set_color("yellow")

   fan2 = Fan()
   fan2.set_bool(False)
   fan2.set_speed(2)
   fan2.set_radius(5)
   fan2.set_color("blue")

   print("The properties of fan1 are: ", fan1.get_bool(),fan1.get_speed(), fan1.get_radius(), fan1.get_color())
   print("The properties of fan2 are; ", fan2.get_bool(), fan2.get_speed(), fan2.get_radius(), fan2.get_color())


main()
