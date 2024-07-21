from functional import *
import time


@timeit
@timeout(3)
def general_testing():
    print("Starting")
    time.sleep(1)
    print("1 second")
    time.sleep(1)
    print("2 seconds")


@timeout(2)
def calculate_sum(x, y):
    return x+ y

if __name__ == '__main__':
    general_testing()
    result = calculate_sum(4, 5)
    print(result)