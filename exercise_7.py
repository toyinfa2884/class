class Count:
    def __init__(self, count = 0):
        self.count = count


def increase(c, times):
    c.count += 1
    times += 1


def main():
    c = Count()
    times = 0
    for i in range(100):
        increase(c, times)
    print("count is", c.count)
    print("times is", times)


main()

