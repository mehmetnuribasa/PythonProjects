numbers = []

for x in range(10):
    numbers.append(x**2)
print(numbers)


numbers = [x**2 for x in range(10)]
print(numbers)


numbers = [x*x for x in range(10) if x%3 == 0]
print(numbers)


#
myString = "hello"
myList = []

for letter in myString:
    myList.append(letter)
print(myList)


myList = [letter for letter in myString]
print(myList)


#
results = [x if x%2 == 0 else 'ODD' for x in range(1, 10)]
print(results)


#
result = []

for x in range(3):
    for y in range(3):
        result.append((x, y))

print(result)


result = [(x, y) for x in range(3) for y in range(3)]
print(result)