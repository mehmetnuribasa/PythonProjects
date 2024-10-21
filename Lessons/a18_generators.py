def cube():
    result = []

    for i in range(5):
        result.append(i)
    
    return result

print(cube())



#generator obejct.
#Does not allocate any area in memory.
def cube():
    for i in range(5):
        yield i ** 3


# print(cube())   #generator object.


#same
for i in cube():
    print(i)


#same
iterator = iter(cube())
print(next(iterator))
print(next(iterator))
print(next(iterator))




#
myListt = [i**3 for i in range(5)]
print(myListt)

#
generator = (i**3 for i in range(5))
print(generator)

for i in generator:
    print(i)
