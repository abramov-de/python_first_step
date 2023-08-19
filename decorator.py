def decorator_1(func):
    print("First decoratior.")

    def wrapper():
        print("Before function 1.")
        func()

    return wrapper


def decorator_2(func):
    print("Second decorator.")

    def wrapper():
        print("Before function 2.")
        func()

    return wrapper


@decorator_1
@decorator_2
def basic_1():
    print("Basic function 1.")


@decorator_1
def basic_2():
    print("Basic function 2.")


print(">> Start.")
basic_1()
basic_2()
print(">> End.")
