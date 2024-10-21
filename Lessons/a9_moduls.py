import math

value = dir(math)
# value = help(math)
# value = help(math.factorial)

value = math.floor(8.5)
print(value)



#
import math as proccess

value = proccess.ceil(8.9)
print(value)


#
# from math import *
from math import factorial, sqrt, ceil

value = factorial(4)
value = ceil(4.1)
value = sqrt(16)
print(value)






#Random Module
import random

result = random.random()  # 0.00 - 1.00
result = random.random() * 100  # 0.00 - 100.00

result = int(random.uniform(10, 100))
result = random.randint(1, 100)
print(result)


names = ["Ali", "Veli", "Osman", "Deniz"]

result = names[random.randint(0, len(names)-1)]
result = random.choice(names)
print(result)


myList = range(100)
result = random.sample(myList, 3)
result = random.sample(names, 2)
print(result)


a = list(range(10))
random.shuffle(a)
print(a)