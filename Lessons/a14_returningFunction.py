#exponential numbers
def involution(number):

    def inner(power):
        return number ** power

    return inner    #Returning a function.

two = involution(2)
print(two(3))   # 2 ** 3



#
def operation(operationName):

    def addition(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
    
    def multiplication(*args):
        product = 1
        for i in args:
            product *= i
        return product
    
    if operationName == "addition" or operationName == "Addition":
        return addition
    else:
        return multiplication
    

summing = operation("Addition")
print(summing(2,3,4,8))