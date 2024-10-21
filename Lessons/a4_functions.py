def add(*params):
    #print(params)
    #print(params[1])
    return sum(params)

def add(*params):
    result = 0
    for x in params:
        result += x
    return result

print(add(10, 20, 30))
print(add(10, 20, 30, 40 ,50))



#
def displayUser(**params):  #represent the dictionary
    for key, value in params.items():
        print('{} is {}'.format(key, value))
    
    # for item in params.items():
    #     print(f"Name: {item[1]}")

displayUser(name = 'Ali', age = 23, city = 'Istanbul')
displayUser(name = 'Ahmet', age = 20, city = 'Ankara')




#
def process_data(data):
    for item in data:
        print(f"Name: {item['name']}, Age: {item['age']}")

# Create a list of dictionaries
data_list = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

process_data(data_list)
