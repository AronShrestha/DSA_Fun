import threading


def print_cube(num):
    print("Cube : {}".format(num**3))


def print_square(num):
    print("Square : {}".format(num*num))


if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(11,))
    t2 = threading.Thread(target=print_cube, args=(12,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely eecuted
    t1.join()
     
    # wait until thread 2 is competely executed
    t2.join()

    # when both threads comletely executes
    print("Done")

    