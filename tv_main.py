from classes_and_objects_chp7.tv import TV


def main():
    samsung = TV()
    samsung.turn_on()
    samsung.set_channel(45)
    samsung.set_volume_level(5)

    lg = TV()
    lg.turn_on()
    lg.set_channel(45)
    lg.set_volume_level(4)

    print("Samsung channel is", samsung.get_channel(), "and volume level is", samsung.get_volume_level())
    print("LG channel is", lg.get_channel(), "and volume level is", lg.get_volume_level())


main()