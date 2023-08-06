# Program to generate powers of two from 2 to 256

def get_next_num():
    n = 2

    # loop for power generation
    while True:
        yield n
        n *= 2  # The next call to get_next_num()
        # will continue execution from here


# test get_next_num()
for num in get_next_num():
    if num > 10000:
        break
    print(num)
