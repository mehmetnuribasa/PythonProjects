numbers = [1,3,5,9]

def square(num): return num ** 2

result = map(square, numbers) #This gives location of result.


# Using map to apply the square function to each element in numbers
#prints..
result = list(map(square, numbers))
print(result)

#prints..
for item in result:
    print(item)



#
numbers = [1,3,5,9]

#prints..
result = list(map(lambda num: num ** 2, numbers))
print(result)



#
numbers = [1,3,5,9]

square = lambda num: num ** 2

#prints..
result = square(3)
print(result)
result = list(map(square, numbers))
print(result)







#
numbers = [1,3,5,9,10,2]

def check_even(num): num % 2 == 0

# Using filter with the check_even function to filter elements in numbers
result = list(filter(lambda num: num%2 == 0, numbers))
print(result)







