# For Loop
d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)


for item in d.items():
    print(item)


for key, value in d.items():
    print(key, value)


tuple = [(1,2), (1,3), (3,5), (5,7)]

for a in tuple:
    print(a)


for a, b in tuple:
    print(a, b)



# While Loop
name = "" #False

while not name.strip(): #strip method. removes all whitespace characters.
    name = input("Enter your name: ")
print(f"Merhaba {name}")

#example
products = []
quantity = int(input("How many products are there: "))
i=0
while (i<quantity):
    name = input("Product name: ")
    price = input("Product price: ")

    products.append({
        'name': name,
        'price': price
    })

    i += 1

count = 1
for i in products:
    print(f"{count}. product name: {i['name']}, product price: {i['price']}")
    count += 1



# Range Method
for item in range(5, 10):
    print(item)
    
for item in range(5, 100, 10):
    print(item)

print(list(range(10, 100, 6)))



# Enumerate
index = 0
greeting = 'Hello There'

for item in greeting:
    print(f'index: {index}, letter: {item}')
    index += 1


for index, letter in enumerate(greeting):
    #print(f'index: {index}, letter: {letter}')
    print(item)


for item in enumerate(greeting):
    #print(type(item))   #tuple
    print(item)




# Zip
list1 = [1,2,3,4,5, 6]
list2 = ['a', 'b', 'c', 'd', 'e', 'w']

print(zip(list1, list2))    #Writes location of zip object
print(list(zip(list1, list2)))  #Writes content of zip object

for item in zip(list1, list2):
    print(item)

for a,b in zip(list1, list2):
    print(a, b)