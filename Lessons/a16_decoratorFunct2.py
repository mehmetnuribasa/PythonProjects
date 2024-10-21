import math
import time


def calculateTime(funct):

    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1) #1 second sleeping the process..

        funct(*args, **kwargs)

        finish = time.time()

        print("The " + funct.__name__ + " function continious for " + str(finish-start) + " seconds.")

    return inner

@calculateTime
def involution(a, b):
    print(math.pow(a, b))

@calculateTime
def factorial(a):
    print(math.factorial(a))


involution(2, 3)
factorial(5)
