# 3**4 = 81    => 3 üzeri 4
# 10//3 = 3    => tam bölme, aşağı yuvarlıyor
# -15 // 4 = -4

#x, y, name, isStudent = (1, 2.3, 'cınar', True)    we can assign a lot of variables at the same time like this.

#knowledge(input) that gets from the input method is always string.
x = input('number 1: ')
y = input("number 2: ")

print(type(x))  #Convert the str to the int.
print(type(y))

result = int(x) + int(y)
print(result)

#Strings..
sentence = 'cghjklçömnbvcxdfgh'
length = len(sentence)

print(sentence[length-1])
print(sentence[3:4])
print(sentence[2:7:2])  #prints the characters two by two

# 
name = 'mehmet'
surname = 'basa'
age = 21

print("My name is {} {} and I'm {} years old.".format(name, surname, age))    #We can use the age as integer. we dont need to convert to the string in this way.
print("My name is {1} {0}.".format(name, surname))    # first of all, writes the surname.
print("My name is {s} {n}.".format(n=name, s=surname))

#
result = 200/700
print("the result is {:1.4}".format(result))
print("the result is {r:1.4}".format(r=result))

#
print(f"My name is {name} {surname}.")


#string methods..


#lists
my_list = ['one', 2, True, 4.5] #we can hold the different type in a list.

list1 = ["Ali", 23]
list2 = ["Veli", 36]

users = list1 + list2   #Adds two lists to the users list.

users = [list1, list2]  #create a two dimensional list.
print(users[0][1])

#
cars = ['toyota', 'renault', 'bmw', 'tofas']
result = 'Mercedes' in cars

result = cars[-2] #bmw

result = cars[:3] #the first three elements

cars[-2:] = ['Mercedes', 'Audi'] #changes the last two element.

del cars[-1]

result = cars[::-1] #Writes the list backward.


#list methods..


#tuples
example = (1, 'two', 3.5)
example = ('damla', 'ayse')
#example[0] = 'ali' #Can not change the tuple elements individually.


#dictionary   like map in java
users = {
    'mehmet':21,
    'ali':10
}

print(users['mehmet'])

users = {
    'mehmet': {
        'age': 21,
        'roles': ['admin', 'user'],
        'address': 'Antalya',
        'phone': 123456
    },

    'ali': {
        'age': 10,
        'roles': ['user'],
        'address': 'Kocaeli',
        'phone': 123456
    }
}

print(users['mehmet'])
print(users['mehmet']['address'])

#update dictionary
users['ali'] = {
    'age': 11,
    'roles': ['user'],
    'address': 'Kocaeli',
    'phone': 123456
}

users.update( { #same with above
    'ali': {
        'age': 11,
        'roles': ['user'],
        'address': 'Kocaeli',
        'phone': 123456
    }
})

print(users['ali'])


#sets
fruits = {'apple', 'orange', 'banana'}

#print(fruits[0])    #Set object does not suport indexing

#We can access set's elements with this way
for x in fruits:
    print(x)

#In sets each elemnt can only found once And there is no queue in the set so, when adding new element or printing elements, it addss the randomly order
fruits.add('cherry')
fruits.update(['mango', 'grape', 'apple'])

fruits.remove('apple')
fruits.discard('apple')
fruits.pop()

#
my_list = [1,2,3,4,4,5,5,5,6,1]
set(my_list) #Convert the list to set.(Writes same elements only one times.)



#Assign Operators
values = 1, 2, 3, 4, 5

x, y, *z = values
print(x, y, z)
print(x, y, z[1])


#Identity Operator: is (Checks if the reference of object)
x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y) #true
print(x==z) #true
print(x is y) #true
print(x is z) #false



#Membership Operator: in
x = ['banana', 'apple']
print('banana' in x) #true

name = 'Ali'
print("'A" in name) #true
print("'b" in name) #false






